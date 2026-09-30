#!/usr/bin/env python3
"""fetch_wiki_engineering.py — quarto giro Wikipedia (en+it): strutture, geotecnica,
infrastrutture, impianti meccanici/idraulici/antincendio, rilievo, BIM, sostenibilita',
gestione progetto. Download sequenziale (1 voce per richiesta, throttling Wikimedia)."""
import json, os, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "KimiResearchBot/1.0 (educational corpus; contact research@example.com)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parsed", "wiki_engineering")
os.makedirs(OUT, exist_ok=True)

IT = [
    # Strutture / statica / scienza delle costruzioni
    "Statica","Struttura (ingegneria)","Scienza delle costruzioni","Analisi strutturale",
    "Tensione (meccanica)","Deformazione (meccanica)","Modulo di elasticità","Carico (fisica)",
    "Carico permanente","Carico accidentale","Sovraccarico","Trazione (fisica)","Compressione (fisica)",
    "Flessione","Taglio (fisica)","Torsione","Instabilità delle strutture","Punto critico (statica)",
    "Criterio di resistenza","Tensione ammissibile","Stato limite","Fatica dei materiali",
    "Cedimento delle fondazioni","Fondazione (edilizia)","Fondazione superficiale","Fondazione profonda",
    "Palificazione","Pozzetto di fondazione","Platea (edilizia)","Fascio (ingegneria)",
    "Trave","Trave continua","Trave appoggiata","Mensola (architettura)","Pilastro","Pilastro di sostegno",
    "Telaio","Controvento","Nodo strutturale","Tirante (meccanica)","Puntone","Arco (architettura)",
    "Volta (architettura)","Cupola","Ponte","Viadotto","Galleria (ingegneria)","Dighe","Sbarramento",
    "Argine","Muro di sostegno","Muro di contenimento","Paratia","Consolidamento dei terreni",
    "Iniezione di cemento","Jet grouting","Palazzo (ingegneria)","Telaio in cemento armato",
    "Cemento armato precompresso","Acciaio strutturale","Calibro (metallurgia)","Giunto strutturale",
    "Saldatura","Bullone","Chiodatura","Vite (meccanica)","Dado (meccanica)",
    # Geotecnica / terreni / geologia
    "Geotecnica","Meccanica del terreno","Terreno (geologia)","Roccia","Stratigrafia",
    "Portanza (geotecnica)","Terra (materiale)","Sabbia","Argilla","Limo (geologia)","Ghiaia",
    "Granulometria","Densità del terreno","Contenuto d'acqua","Limite di Atterberg","Permeabilità (geologia)",
    "Pressione dei pori","Falda acquifera","Pozzo","Sondaggio geognostico","Geologia applicata",
    "Idrogeologia","Idraulica","Moto uniforme","Equazione di Bernoulli","Portata (fluidodinamica)",
    "Tirante idraulico","Pendenza (geometria)","Modello fisico","Strada","Pavimentazione stradale",
    "Fondazione stradale","Sopraelevata","Rotatoria","Intersezione stradale",
    # Impianti meccanici / idraulici / antincendio
    "Impianto idrico-sanitario","Impianto termoidraulico","Impianto di climatizzazione",
    "Condizionamento dell'aria","Deumidificazione","Umidificazione","Ricambio d'aria",
    "Condotto (edilizia)","Tubo","Raccordo (tubi)","Valvola","Valvola a sfera","Valvola a farfalla",
    "Valvola di ritegno","Valvola di sfioro","Valvola di sicurezza","Miscelatore (rubinetteria)",
    "Rubinetto","Scarico (idraulica)","Sifone (idraulica)","Pozzetto (impianti)","Caditoia",
    "Pompa (macchina)","Pompa centrifuga","Pompa a immersione","Pompa di calore","Compressore",
    "Ventilatore (macchina)","Ventilconvettore","Fan coil","Unità esterna","Unità interna",
    "Split (climatizzazione)","Multisplit","Impianto a tutt'aria","VMC (ventilazione)",
    "Depurazione delle acque","Fognatura","Fognatura bianca","Acque reflue","Pozzo nero",
    "Fossa settica","Depuratore","Acqua potabile","Addolcimento dell'acqua","Antincendio",
    "Estintore","Idrante","Naspo","Sprinkler","Rivelatore di fumo","Rivelatore di incendio",
    "Porta tagliafuoco","Compartimentazione (edilizia)","Vie di esodo","Scala antincendio",
    "Casetta DSU","Impianto di rilevazione incendi","Controllo accessi (sicurezza)",
    # Rilievo / topografia / misura
    "Rilievo (architettura)","Rilievo topografico","Topografia","Geodesia","Cartografia",
    "Sistema di coordinate","Coordinate geografiche","Coordinate piane","Gauss-Boaga",
    "Fuso (geodesia)","Catasto (Italia)","Mappa catastale","Cassero (topografia)",
    "Livella (topografia)","Teodolite","Stazione totale","GPS","GNSS","Rilievo laser scanner",
    "Fotogrammetria","Telerilevamento","Lidar","Distanziometro laser","Clinometro",
    "Bussola","Livellazione geometrica","Quota (topografia)","Acropoli (geometria)",
    "Direttrice (geometria)","Angolo","Goniometro","Radiante","Grado (geometria)",
    # BIM / digitale / interoperabilità
    "Building Information Modeling","BIM","IFC (formato file)","Industry Foundation Classes",
    "COBie","Level of development","Modello digitale","Digital twin","Gemello digitale",
    "Reality capture","Scan to BIM","CAD","Disegno tecnico","Proiezioni ortogonali",
    "Vista (disegno tecnico)","Sezione (disegno tecnico)","Quota (disegno tecnico)",
    "Scala (disegno tecnico)","Cartiglio (disegno tecnico)","Normalizzazione (disegno tecnico)",
    "Tolleranza (meccanica)","Rugosità","Simbologia tecnica","Rappresentazione tecnica",
    "Software CAD","AutoCAD","Revit","ArchiCAD","Allplan","Tekla Structures","FreeCAD",
    "Open CASCADE","Blender (programma)","SketchUp","Rhinoceros 3D","Grasshopper 3D",
    "Archivio digitale","Gestione documentale","Protocollo informatico","Conservazione digitale",
    "Firma digitale","Fatturazione elettronica","Identità digitale","SPID","CAD (normativa)",
    "Piano triennale ICT","AgID"," interoperabilità",
    # Sostenibilità / ambiente / certificazione
    "Sostenibilità","Sostenibilità ambientale","Impatto ambientale","Valutazione di impatto ambientale",
    "Analisi del ciclo di vita","Dichiarazione ambientale di prodotto","Carbon footprint",
    "Water footprint","Ecologico","Ecolabel","Marchio ambientale","LEED","BREEAM","Protocollo ITACA",
    "CasaClima","EnerPHit","Edilizia sostenibile","Edilizia a basse emissioni","Economia circolare",
    "Riciclo","Rifiuto","Raccolta differenziata","Smaltimento","Bonifica","Amianto","Suolo (geologia)",
    "Consumo di suolo","Paesaggio","Tutela paesaggistica","Beni culturali","Restauro architettonico",
    "Consolidamento strutturale","Manutenzione (ingegneria)","Manutenzione programmata",
    "Manutenzione predittiva","Life cycle assessment","Indoor environmental quality",
    "Ventilazione naturale","Schermatura","Verde urbano","Copertura verde","Tetto verde",
    "Parete verde","Pavimento permeabile","Drenaggio urbano","Sostenibilità idrica",
    # Gestione progetto / contratti / direzione lavori
    "Project management","Gestione del progetto","Project manager","PMI","PMP","PRINCE2",
    "Metodo del percorso critico","Diagramma di Gantt","Work breakdown structure",
    "Gestione del rischio","Gestione della qualità","Assicurazione qualità","Controllo qualità",
    "Lean construction","BIM management","Direzione lavori","Direttore dei lavori",
    "Contabilità dei lavori","Stato avanzamento lavori","Sal (edilizia)","Certificato di pagamento",
    "Subappalto","Appalto","Appalto pubblico","Codice dei contratti pubblici","ANAC",
    "Corruzione (penale)","Trasparenza amministrativa","Accesso civico","FOIA","Whistleblowing",
    "Antiriciclaggio","Due diligence","Responsabilità penale","Reato (diritto)","Ne bis in idem",
    "Prescrizione (diritto)","Decreto ingiuntivo","Sfratto","Locazione","Contratto preliminare",
    "Rogito","Atto notarile","Procura","Successione (diritto)","Usufrutto","Servitù (diritto)",
    "Ipoteca","Pegno (diritto)","Garanzia (diritto)","Fideiussione","Cauzione (edilizia)",
    "Assicurazione","RC professionale","Polizza (assicurazione)","Rischio (economia)",
    # Economia / estimo / valutazioni
    "Estimo","Valutazione immobiliare","Metodo comparativo","Metodo finanziario",
    "Metodo patrimoniale","Reddito (economia)","Tasso di attualizzazione","Valore attuale netto",
    "Tasso interno di rendimento","Payback period","Ammortamento","Ammortamento tecnico",
    "Costo capitale","Costo opportunità","Capitale (economia)","Investimento","Finanza pubblica",
    "Contabilità pubblica","Bilancio comunale","Mutuo ipotecario","Leasing","Rent to buy",
    "Crowdfunding immobiliare","Real estate","Asset management","Facility management",
    "Property management","Facility management integrato","Global service","Energy manager",
    "Audit energetico","Sistema energetico","Catasto energetico","Certificato energetico",
    "Obbligo energetico","Contabilità energetica","Misura energetica","Monitoraggio energetico",
]

EN = [
    # Structures / structural engineering
    "Statics","Structural engineering","Structural analysis","Stress (mechanics)","Strain (mechanics)",
    "Young's modulus","Load (physics)","Dead load","Live load","Structural load","Tension (physics)",
    "Compression (physics)","Bending","Shear stress","Torsion","Buckling","Yield (engineering)",
    "Yield strength","Ultimate tensile strength","Factor of safety","Limit state design",
    "Fatigue (material)","Fracture mechanics","Foundation (engineering)","Shallow foundation",
    "Deep foundation","Pile (foundation)","Caisson (engineering)","Well foundation","Pad footing",
    "Strip footing","Raft foundation","Settlement (structural)","Beam (structure)","Continuous beam",
    "Simply supported beam","Cantilever","Column","Frame","Bracing","Structural joint","Tie (engineering)",
    "Strut","Arch","Vault","Dome","Bridge","Viaduct","Tunnel","Dam","Levee","Retaining wall",
    "Sheet pile","Soil nailing","Ground freezing","Grouting","Reinforced concrete","Prestressed concrete",
    "Structural steel","Rivet","Bolted joint","Welding","Screw","Nut (hardware)",
    # Geotechnical / soils
    "Geotechnical engineering","Soil mechanics","Soil","Rock (geology)","Stratigraphy (archaeology)",
    "Bearing capacity","Sand","Clay","Silt","Gravel","Grain size","Permeability (earth sciences)",
    "Pore water pressure","Aquifer","Water well","Borehole","Engineering geology","Hydrogeology",
    "Hydraulics","Bernoulli's principle","Discharge (hydrology)","Hydraulic head","Open-channel flow",
    "Road","Pavement (road)","Subbase (pavement)","Interchange (road)","Roundabout","Culvert",
    # Mechanical / plumbing / fire
    "Plumbing","HVAC","Air conditioning","Dehumidifier","Humidifier","Ventilation (architecture)",
    "Duct (HVAC)","Pipe (fluid conveyance)","Pipe fitting","Valve","Ball valve","Butterfly valve",
    "Check valve","Relief valve","Faucet","Trap (plumbing)","Catch basin","Storm drain","Pump",
    "Centrifugal pump","Submersible pump","Compressor","Fan (machine)","Fan coil unit","Heat exchanger",
    "Variable refrigerant flow","Air handler","Chiller","Cooling tower","Boiler","Radiator (heating)",
    "Water treatment","Sewage","Sanitary sewer","Septic tank","Wastewater treatment","Drinking water",
    "Water softening","Fire protection","Fire extinguisher","Fire hydrant","Standpipe (firefighting)",
    "Fire sprinkler system","Smoke detector","Fire alarm system","Fire-rated door","Compartmentalization",
    "Means of egress","Fire escape","Firefighting","Passive fire protection",
    # Surveying / measurement
    "Surveying","Geodesy","Cartography","Geographic coordinate system","Projected coordinate system",
    "Cassini-Soldner","Map projection","Levelling","Theodolite","Total station","GNSS",
    "3D scanner","Photogrammetry","Remote sensing","Lidar","Laser rangefinder","Inclinometer",
    "Compass","Geographic information system","Bathymetry","Triangulation","Trilateration",
    "Angle","Radian","Degree (angle)",
    # BIM / digital / CAD
    "Building information modeling","Industry Foundation Classes","Construction Operations Building Information Exchange",
    "Digital twin","Reality capture","Computer-aided design","Engineering drawing","Orthographic projection",
    "Multiview projection","Sectional view","Engineering tolerance","Surface roughness","Technical drawing",
    "Blueprint","Computer-aided manufacturing","Product lifecycle management","Data exchange",
    "Interoperability","Digital signature","Electronic invoicing","Electronic identity","Open data",
    "Public procurement data",
    # Sustainability / environment / certification
    "Sustainability","Environmental impact assessment","Life-cycle assessment","Environmental product declaration",
    "Carbon footprint","Water footprint","Ecolabel","Eco-label","LEED","BREEAM","Green building",
    "Sustainable architecture","Circular economy","Recycling","Waste","Waste management","Landfill",
    "Environmental remediation","Asbestos","Land consumption","Cultural heritage","Architectural conservation",
    "Structural strengthening","Maintenance","Preventive maintenance","Predictive maintenance",
    "Natural ventilation","Solar shading","Urban green space","Green roof","Living wall","Permeable paving",
    "Sustainable drainage system","Indoor environmental quality","Daylighting",
    # Project management / contracts
    "Project management","Project manager","Project Management Institute","PRINCE2",
    "Critical path method","Gantt chart","Work breakdown structure","Risk management",
    "Quality management","Quality assurance","Quality control","Lean construction",
    "Construction management","Construction accounting","Schedule of values","Payment application",
    "Subcontractor","Construction contract","Public procurement","Corruption","Transparency (behavior)",
    "Freedom of information","Whistleblower","Anti-money laundering","Due diligence",
    "Criminal responsibility","Statute of limitations","Eviction","Lease","Preliminary contract",
    "Deed","Notary","Power of attorney","Inheritance","Usufruct","Easement","Mortgage",
    "Pledge (law)","Surety bond","Bid bond","Insurance","Professional liability insurance",
    "Risk (economics)",
    # Economics / appraisal / RE
    "Real estate appraisal","Sales comparison approach","Income approach","Cost approach",
    "Discounted cash flow","Internal rate of return","Net present value","Payback period",
    "Amortization","Capital cost","Opportunity cost","Capital (economics)","Investment",
    "Public finance","Municipal bond","Mortgage loan","Leasing","Real estate crowdfunding",
    "Real estate investing","Asset management","Facility management","Property management",
    "Energy management","Energy accounting","Building automation",
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
