#!/usr/bin/env python3
"""fetch_wiki_incentivi.py — terzo giro Wikipedia (en+it): incentivi energetici,
Conto Termico, bonus edilizi, CER/autoconsumo, TEE, efficienza energetica, FER.
Stesso formato degli altri fetcher wiki, output separato."""
import json, os, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "KimiResearchBot/1.0 (educational corpus; contact research@example.com)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parsed", "wiki_incentivi")
os.makedirs(OUT, exist_ok=True)

IT = [
    # Conto Termico / bonus edilizi / detrazioni
    "Conto termico","Superbonus","Ecobonus","Detrazione per riqualificazione energetica",
    "Bonus edilizia","Bonus facciate","Bonus mobili","Bonus verde","Bonus ristrutturazioni",
    "Detrazione fiscale","Iperammortamento","Credito d'imposta","Cessione del credito",
    "Sismabonus","Bonus barriere architettoniche","Bonus prima casa","Detrazione affitto",
    # Efficienza energetica edifici
    "Efficienza energetica","Riqualificazione energetica","Isolamento termico","Cappotto termico",
    "Coibentazione","Attestato di prestazione energetica","Certificatore energetica",
    "Certificazione energetica degli edifici","Diagnosi energetica","Audit energetico",
    "Edificio a energia quasi zero","Obbligo di agibilità energetica","Legge 10",
    "Zona climatica","Grado giorno","Fabbisogno energetico","Prestazione energetica degli edifici",
    "Pompa di calore","Pompa di calore aria-aria","Solare termico","Caldaia a condensazione",
    "Caldaia a pellet","Biomassa","Teleriscaldamento","Cogenerazione","Trigenerazione",
    "Ventilazione meccanica controllata","Recupero di calore","Schermatura solare",
    "Ponti termici","Trasmittanza termica","Serramento","Vetrocamera","Riscaldamento a pavimento",
    "Termoarredo","Valvola termostatica","Contabilizzazione del calore","Building automation",
    # Incentivi elettrici / FER / mercato energia
    "Fotovoltaico","Impianto fotovoltaico","Conto energia","Ritiro dedicato","Ritiro semi-obbligatorio",
    "Scambio sul posto","Autoconsumo","Comunità energetica","Autoconsumo collettivo",
    "Fonti di energia rinnovabile","Energia rinnovabile","Titolo di efficienza energetica",
    "Certificato verde","Oneri generali","Tariffe elettriche","Mercato elettrico","GME",
    "Gestore dei mercati energetici","Gestore dei servizi energetici","ARERA",
    "Accumulo di energia","Batteria agli ioni di litio","Wallbox","Ricarica di veicoli elettrici",
    "Colonnina di ricarica","Veicolo elettrico","Smart grid","Demand response",
    "Potenza (fisica)","Energia elettrica","Rete elettrica","Distribuzione di energia elettrica",
    "Trasmissione di energia elettrica","Efficienza (fisica)","Coefficiente di prestazione",
    "Rendimento (fisica)","Gas naturale","Biometano","Idrogeno","Pompa di calore geotermica",
    "Geotermia","Pannelli solari","Energia solare","Eolico","Idroelettricità",
    # Contratti / esco / appalti energetici
    "Energy Performance Contract","Esco","Servizi energetici","Contratto di servizio energetico",
    "Energy manager","Gestione energetica","Sistema di gestione dell'energia","EN ISO 50001",
    "Consulenza energetica","Piano nazionale integrato per l'energia e il clima",
    "Decarbonizzazione","Povertà energetica","Transizione energetica","Decreto FER",
    "Direttiva case verdi","Pacchetto case verdi","Rinnovabili (Italia)",
    # Fiscale / catastale utile agli incentivi
    "Catasto","Categoria catastale","Rendita catastale","Bonus 110%","Pratica edilizia",
    "Titolo edilizio","Permesso di costruire","SCIA","CILA","Conformità urbanistica",
    "Asseverazione","Visto di conformità","Direttore dei lavori","Direzione lavori",
    "Collaudo","Certificato di collaudo","Certificato di fine lavori",
]

EN = [
    # Incentives & policy
    "Energy subsidy","Feed-in tariff","Net metering","Energy policy","Energy transition",
    "Energy Performance Certificate","Building energy rating","Energy retrofit","Building retrofit",
    "Deep energy retrofit","Nearly zero-energy building","Zero-energy building","Green building",
    "Sustainable architecture","Energy efficiency in British housing","German renewable energy",
    "Renewable energy in Italy","Photovoltaics in Italy","Solar power in Italy","Wind power in Italy",
    "Geothermal power in Italy","Hydroelectricity in Italy","Bioenergy in Italy",
    # Technologies
    "Heat pump","Air source heat pump","Ground source heat pump","Heat pump water heater",
    "Hybrid heat pump","Solar thermal collector","Solar water heating","Condensing boiler",
    "Biomass heating system","Wood pellet","Pellet fuel","District heating","Cogeneration",
    "Combined heat and power","Trigeneration","Micro combined heat and power","Heat recovery",
    "Mechanical ventilation","Heat recovery ventilation","Solar shading","Thermal bridge",
    "U-value","Insulated glazing","Underfloor heating","Radiator (heating)","Thermostatic radiator valve",
    "Heat metering","Building automation","Home energy monitor","Smart thermostat",
    # Electricity / FER / markets
    "Photovoltaics","Solar panel","Solar cell","Energy storage","Grid energy storage",
    "Lithium-ion battery","Electric vehicle charging network","Charging station","Electric vehicle",
    "Smart grid","Demand response","Virtual power plant","Electricity market","Electricity generation",
    "Electric power transmission","Electric power distribution","Power station","Renewable energy",
    "Sustainable energy","Capacity factor","Coefficient of performance","Efficiency",
    "Thermal efficiency","Energy return on investment","Natural gas","Biomethane","Hydrogen",
    "Geothermal energy","Geothermal heating","Solar energy","Wind power","Hydropower",
    "Wave power","Tidal power","Bioenergy","Anaerobic digestion","District cooling",
    # Certificates / ESCO / contracts
    "Energy service company","Energy performance contracting","Energy management",
    "ISO 50001","Energy audit","Energy conservation","White certificate","Renewable energy certificate",
    "Guarantee of origin","Renewable portfolio standard","Energy mix","Energy poverty",
    "Energy security","Decarbonisation","Carbon neutrality","Carbon offset","Carbon tax",
    "Emissions trading","Greenhouse gas","Global warming potential","Life-cycle assessment",
    # Codes & practice
    "International Energy Conservation Code","Energy code","Building code","Passive house",
    "Passive solar building design","Low-energy house","Green building in Italy","Superbonus",
]

def fetch(lang, titles, fname):
    api = f"https://{lang}.wikipedia.org/w/api.php"
    out = os.path.join(OUT, fname)
    mode = "a" if os.path.exists(out) else "w"
    written = set()
    if mode == "a":
        with open(out, encoding="utf-8") as f:
            for line in f:
                try: written.add(json.loads(line)["title"])
                except Exception: pass
    got, miss, empty = 0, [], 0
    req_path = out + ".req"
    reqs = set()
    if os.path.exists(req_path):
        reqs = set(open(req_path, encoding="utf-8").read().splitlines())
    fo = open(out, mode, encoding="utf-8")
    fr = open(req_path, "a", encoding="utf-8")
    for t in titles:
        if t in written or t in reqs: continue
        params = {
            "action": "query", "format": "json", "redirects": "1",
            "prop": "extracts", "explaintext": "1",
            "titles": t,
        }
        url = api + "?" + urllib.parse.urlencode(params)
        d = None
        for retry in range(3):
            try:
                req = urllib.request.Request(url, headers=UA)
                with urllib.request.urlopen(req, timeout=90) as r:
                    d = json.loads(r.read().decode("utf-8"))
                break
            except Exception as e:
                print(f"[retry {retry}] {lang} {t}: {e}"); time.sleep(15 * (retry + 1))
        if d is None:
            miss.append(t); continue
        fr.write(t + "\n"); fr.flush()
        pages = d.get("query", {}).get("pages", {})
        redir_from = {v["from"] for v in d.get("query", {}).get("redirects", [])}
        rec_written = False
        for pid, pg in pages.items():
            title = pg.get("title", "")
            if "missing" in pg:
                continue
            txt = pg.get("extract", "")
            if not txt or len(txt) < 400:
                empty += 1
                continue
            if title in written: continue
            rec = {
                "source": f"wikipedia_{lang}", "license": "CC BY-SA 4.0",
                "commercial_ok": True, "attribution": f"{title} — Wikipedia ({lang}), CC BY-SA 4.0",
                "url": f"https://{lang}.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")),
                "title": title, "text": txt,
            }
            written.add(title)
            fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); got += 1; rec_written = True
        if not rec_written and t not in redir_from:
            miss.append(t)
        time.sleep(2.2)
    fo.close(); fr.close()
    print(f"[{lang}] nuove voci: {got} | vuote: {empty} | mancanti: {len(miss)}")
    if miss: print("  mancanti:", ", ".join(miss[:30]))

only = sys.argv[1] if len(sys.argv) > 1 else None
if only in (None, "en"):
    print("=== EN ==="); fetch("en", EN, "wiki_en.jsonl")
if only in (None, "it"):
    print("=== IT ==="); fetch("it", IT, "wiki_it.jsonl")
for f in ("wiki_en.jsonl", "wiki_it.jsonl"):
    p = os.path.join(OUT, f)
    if os.path.exists(p):
        print(f, sum(1 for _ in open(p, encoding="utf-8")))
