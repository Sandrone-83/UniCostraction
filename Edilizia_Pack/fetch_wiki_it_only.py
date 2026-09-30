#!/usr/bin/env python3
"""fetch_wiki_it_only.py — completa SOLO le voci italiane mancanti, con attese lunghe."""
import json, os, time, urllib.parse, urllib.request

UA = {"User-Agent": "KimiResearchBot/1.0 (educational corpus; contact research@example.com)"}
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "parsed", "wiki_construction")
os.makedirs(OUT, exist_ok=True)

IT = [
    "Edilizia","Ingegneria civile","Ingegneria strutturale","Calcestruzzo armato","Cemento armato",
    "Calcestruzzo","Cemento","Aggregato (costruzione)","Acciaio strutturale","Struttura in acciaio",
    "Muratura","Mattone","Intonaco","Cartongesso","Cassaforma","Ponteggio","Ferro (materiale edile)",
    "Fondazione (edilizia)","Fondazioni profonde","Fondazioni superficiali","Palificazione",
    "Muro di sostegno","Meccanica del terreno","Geotecnica","Scavo","Compattazione del terreno",
    "Portanza (geotecnica)","Cedimento (ingegneria)","Impianto idraulico","Impianto di condizionamento",
    "Condizionamento dell'aria","Riscaldamento","Idraulica","Scarico (edilizia)","Fognatura",
    "Antincendio","Sprinkler","Impianto elettrico","Cabina elettrica","Ascensore","Domotica",
    "Impiantistica","Ventilazione (edilizia)","Pompa di calore","Riscaldamento a pavimento",
    "Fotovoltaico","Acqua piovana","Normativa sismica","Ingegneria sismica","Ingegneria del vento",
    "Codice di prevenzione incendi","Certificazione energetica degli edifici","Coibentazione",
    "Fisica tecnica","Acustica edilizia","Illuminazione naturale","Illuminotecnica",
    "Progettazione architettonica","Disegno tecnico","Tavola (disegno tecnico)","Computer-aided design",
    "Building information modeling","Industry Foundation Classes","Progettazione sostenibile",
    "Bioedilizia","Progetto architettonico","Planimetria","Prospetto (architettura)","Sezione (architettura)",
    "Direzione lavori","Computo metrico","Capitolato (appalto)","Appalto (ordinamento italiano)",
    "Appalto pubblico","Subappalto","Contraente generale","General contractor","Cantiere",
    "Sicurezza nei cantieri","Ponteggi (sicurezza)","Attrezzature di cantiere","Gru (macchina)",
    "Ruspa","Escavatore","Betoniere","Mezzo d'opera","Muratore","Carpentiere","Elettricista",
    "Idraulico","Falegname","Imbianchino","Posatore","Geometra","Perito industriale","Ingegnere edile",
    "Architetto","Programmazione dei lavori","Cronoprogramma","Metodo del percorso critico",
    "Contabilità lavori","Stima dei costi","Variante in corso d'opera","Collaudo","Manutenzione edilizia",
    "Restauro architettonico","Riqualificazione energetica","Demolizione","Prefabbricato",
    "Costruzione modulare","Strada","Pavimentazione stradale","Ponte","Galleria (ingegneria)",
    "Diga","Condotta forzata","Rete idrica","Depurazione delle acque","Discarica","Opere di urbanizzazione",
    "Concessione edilizia","Permesso di costruire","Catasto","Docfa","Classamento energetico",
    "Norme tecniche per le costruzioni","Regolamento edilizio","Zonizzazione",
]

def fetch_it():
    api = "https://it.wikipedia.org/w/api.php"
    out = os.path.join(OUT, "wiki_it.jsonl")
    done = set()
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            for line in f:
                try: done.add(json.loads(line)["title"])
                except Exception: pass
    got, miss = 0, []
    with open(out, "a", encoding="utf-8") as fo:
        for i in range(0, len(IT), 10):  # batch piu' piccoli
            batch = [t for t in IT[i:i+10] if t not in done]
            if not batch: continue
            params = {"action": "query", "format": "json", "redirects": "1",
                      "prop": "extracts", "explaintext": "1", "exlimit": "max",
                      "titles": "|".join(batch)}
            url = api + "?" + urllib.parse.urlencode(params)
            d = None
            for retry in range(4):
                try:
                    req = urllib.request.Request(url, headers=UA)
                    with urllib.request.urlopen(req, timeout=90) as r:
                        d = json.loads(r.read().decode("utf-8"))
                    break
                except Exception as e:
                    print(f"[retry {retry}] {e}"); time.sleep(20 * (retry + 1))
            if d is None:
                print(f"[SALTO batch] {batch}"); continue
            pages = d.get("query", {}).get("pages", {})
            found = set()
            for pid, pg in pages.items():
                title = pg.get("title", ""); found.add(title)
                txt = pg.get("extract", "")
                if not txt or len(txt) < 400: continue
                rec = {"source": "wikipedia_it", "license": "CC BY-SA 4.0",
                       "commercial_ok": True,
                       "attribution": f"{title} - Wikipedia (it), CC BY-SA 4.0",
                       "url": "https://it.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")),
                       "title": title, "text": txt}
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); got += 1
            redir = {v["to"] for v in d.get("query", {}).get("redirects", [])}
            for t in batch:
                if t not in found and t not in redir: miss.append(t)
            time.sleep(6)
    print(f"[it] nuove voci: {got} | mancanti: {len(miss)}")
    if miss: print("  mancanti:", ", ".join(miss))

fetch_it()
