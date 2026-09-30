#!/usr/bin/env python3
"""fetch_wiki_corpus.py — corpus tecnico edilizia da Wikipedia (en + it), licenza CC BY-SA.

Raccoglie il testo integrale (plain text) delle voci selezionate via MediaWiki API.
Ogni record JSONL riporta titolo, URL, licenza e testo — pronto per l'addestramento.
"""
import json, os, time, urllib.parse, urllib.request

UA = {"User-Agent": "KimiResearchBot/1.0 (educational corpus; contact research@example.com)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parsed", "wiki_construction")
os.makedirs(OUT, exist_ok=True)

EN = [
    # Strutture / materiali
    "Building construction","Civil engineering","Structural engineering","Reinforced concrete",
    "Prestressed concrete","Concrete","Cement","Concrete admixture","Aggregate (composite)",
    "Asphalt concrete","Structural steel","Steel frame","Timber framing","Wood preservation",
    "Masonry","Brickwork","Mortar (masonry)","Formwork","Scaffolding","Anchor bolt","Rebar",
    "Welding","Bolted joint","Corrosion","Building envelope","Drywall","Plaster","Stucco",
    "Roof","Roof shingle","Insulation (construction)","Waterproofing","Window","Door","Curtain wall (architecture)",
    "Glass fiber reinforced concrete","Precast concrete","Cast-in-place concrete","Composite material",
    # Geotecnica / fondazioni
    "Foundation (engineering)","Deep foundation","Pile (construction)","Shallow foundation",
    "Retaining wall","Soil mechanics","Geotechnical engineering","Earthworks (engineering)",
    "Excavation (archaeology)","Groundwater control","Dewatering","Land grading","Soil compaction",
    "Bearing capacity","Settlement (structural)","Landslide","Rock mechanics",
    # Impiantistica / MEP
    "HVAC","Heating, ventilation, and air conditioning","Plumbing","Drainage","Sanitary sewer",
    "Storm drain","Water heating","Fire sprinkler system","Fire protection engineering",
    "Passive fire protection","Active fire protection","Smoke detector","Fire alarm system",
    "Electrical wiring","Electrical system","Low-voltage","Switchgear","Transformer",
    "Building automation","Elevator","Escalator","Building services engineering","Mechanical, electrical, and plumbing",
    "Ventilation (architecture)","Air conditioning","Heat pump","Radiator (heating)","Underfloor heating",
    "Photovoltaics","Solar water heating","Rainwater harvesting","Greywater","Septic tank",
    # Progettazione / fisica dell'edificio
    "Building code","Building regulations in the United Kingdom","International Building Code",
    "Eurocode","Architecture","Architectural drawing","Technical drawing","Blueprint",
    "Building information modeling","Industry Foundation Classes","Green building","Sustainable architecture",
    "Building physics","Building science","Acoustics","Architectural acoustics","Daylighting",
    "Lighting","Energy efficiency in buildings","Thermal insulation","Passive house",
    "Seismic analysis","Earthquake engineering","Wind engineering","Fire-resistance rating",
    "Accessibility","Universal design","Architectural design","Interior design","Landscape architecture",
    "Urban planning","Zoning","Floor plan","Elevation (architecture)","Cross section (geometry)",
    # Processo / cantiere / management
    "Construction management","Critical path method","Program evaluation and review technique",
    "Construction schedule","Quantity surveyor","Cost estimate","Construction estimating software",
    "Construction contract","Lien waiver","General contractor","Subcontractor","Construction worker",
    "Carpentry","Mason","Electrician","Plumber","Ironworker","Heavy equipment operator",
    "Crane (machine)","Forklift","Excavator","Bulldozer","Concrete mixer","Dump truck",
    "Construction site","Construction safety","Occupational safety and health","Personal protective equipment",
    "Lean construction","Construction procurement","Bid","Construction bidding","Construction law",
    "Delay (construction)","Construction claim","Retention (construction)","Snagging",
    "Commissioning (building)","Facility management","Building maintenance","Renovation","Retrofitting",
    "Demolition","Deconstruction (building)","Prefabrication","Modular building","3D printing in construction",
    # Infrastrutture
    "Road construction","Asphalt","Pavement (architecture)","Curb","Bridge","Cantilever bridge",
    "Suspension bridge","Arch bridge","Tunnel","Tunnel boring machine","Dam","Levee",
    "Canal","Water supply network","Sewerage","Wastewater treatment","Landfill",
    "Retaining structure","Geosynthetics","Erosion control","Drainage system (geotechnical)",
]
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
    "Norme tecniche per le costruzioni","Regolamento edilizio"," zonizzazione",
]
IT = [t.strip() for t in IT]

def fetch(lang, titles):
    api = f"https://{lang}.wikipedia.org/w/api.php"
    out = os.path.join(OUT, f"wiki_{lang}.jsonl")
    mode = "a" if os.path.exists(out) else "w"
    done = set()
    if mode == "a":
        with open(out, encoding="utf-8") as f:
            for line in f:
                try: done.add(json.loads(line)["title"])
                except Exception: pass
    got, miss = 0, []
    with open(out, mode, encoding="utf-8") as fo:
        for i in range(0, len(titles), 20):
            batch = [t for t in titles[i:i+20] if t not in done]
            if not batch: continue
            params = {
                "action": "query", "format": "json", "redirects": "1",
                "prop": "extracts", "explaintext": "1", "exlimit": "max",
                "titles": "|".join(batch),
            }
            url = api + "?" + urllib.parse.urlencode(params)
            for retry in range(3):
                try:
                    req = urllib.request.Request(url, headers=UA)
                    with urllib.request.urlopen(req, timeout=90) as r:
                        d = json.loads(r.read().decode("utf-8"))
                    break
                except Exception as e:
                    print(f"[retry {retry}] {lang}: {e}"); time.sleep(15 * (retry + 1))
            else:
                print(f"[SALTO batch] {lang} {batch}"); continue
            pages = d.get("query", {}).get("pages", {})
            found = set()
            for pid, pg in pages.items():
                title = pg.get("title", "")
                found.add(title)
                txt = pg.get("extract", "")
                if not txt or len(txt) < 400: continue
                rec = {
                    "source": f"wikipedia_{lang}", "license": "CC BY-SA 4.0",
                    "commercial_ok": True, "attribution": f"{title} — Wikipedia ({lang}), CC BY-SA 4.0",
                    "url": f"https://{lang}.wiki pedia.org/wiki/".replace(" ", "") + urllib.parse.quote(title.replace(" ", "_")),
                    "title": title, "text": txt,
                }
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); got += 1
            redir = {v["to"] for v in d.get("query", {}).get("redirects", [])}
            for t in batch:
                if t not in found and t not in redir:
                    miss.append(t)
            time.sleep(3)
    print(f"[{lang}] nuove voci: {got} | mancanti: {len(miss)}")
    if miss: print("  mancanti:", ", ".join(miss[:25]))

print("=== EN ==="); fetch("en", EN)
print("=== IT ==="); fetch("it", IT)
n = sum(1 for _ in open(os.path.join(OUT, "wiki_en.jsonl"), encoding="utf-8"))
m = sum(1 for _ in open(os.path.join(OUT, "wiki_it.jsonl"), encoding="utf-8"))
print(f"totale voci: en={n} it={m}")
