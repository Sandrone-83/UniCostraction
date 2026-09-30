#!/usr/bin/env python3
"""fetch_wiki_materiale_design.py — secondo giro Wikipedia (en+it): materiali, design,
domotica/smart home, estetica. Stesso formato di fetch_wiki_corpus.py, output separato."""
import json, os, time, urllib.parse, urllib.request

UA = {"User-Agent": "KimiResearchBot/1.0 (educational corpus; contact research@example.com)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parsed", "wiki_construction")
os.makedirs(OUT, exist_ok=True)

EN = [
    # Domotica / smart home / building automation
    "Home automation","Domotics","Smart home","Home automation for the elderly and disabled",
    "KNX (standard)","BACnet","LonWorks","Modbus","Zigbee","Z-Wave","Matter (standard)",
    "MQTT","Thread (network protocol)","Thread Group","Lighting control system",
    "DALI","Digital addressable lighting interface","Occupancy sensor","Smart thermostat",
    "Smart plug","Smart meter","Home energy monitor","Demand response","Net zero building",
    "Building management system","Intelligent building","Internet of things","Voice user interface",
    "Amazon Alexa","Google Home","Home Assistant","HomeKit","IFTTT","OpenHAB",
    # Materiali da costruzione
    "Building material","Materials science","Concrete masonry unit","Cross-laminated timber",
    "Engineered wood","Glued laminated timber","Wood veneer","Plywood","Oriented strand board",
    "Fiberboard","Particle board","Medium-density fibreboard","Hardwood","Softwood","Cedar wood",
    "Oak","Beech","Walnut (wood)","Larch","Bamboo construction","Mass timber",
    "Glass wool","Mineral wool","Polyurethane foam","Polystyrene","Extruded polystyrene foam",
    "Expanded polystyrene","Polyisocyanurate","Rock wool","Aerogel","Vacuum insulated panel",
    "Marble","Granite","Travertine","Limestone","Slate","Sandstone","Basalt","Quartzite",
    "Ceramic tile","Porcelain","Terracotta","Stoneware","Glass","Float glass","Laminated glass",
    "Tempered glass","Insulated glazing","Low-emissivity","Structural glass","Curtain wall",
    "Stainless steel","Weathering steel","Aluminium alloy","Copper in architecture","Zinc",
    "Titanium","Bronze","Corrugated galvanised iron","Standing seam","Asphalt shingle",
    "Membrane (building)","Bitumen","Ethylene propylene diene monomer","Thermoplastic polyolefin",
    "Fiber-reinforced concrete","Self-consolidating concrete","Ultra-high-performance concrete",
    "Geopolymer cement","Calcium aluminate cements","White Portland cement","Mortar (masonry)",
    "Lime mortar","Rammed earth","Adobe","Straw-bale construction","Cob (material)","Hempcrete",
    "Mycelium-based materials","Recycled concrete aggregate","Ashcrete","Reclaimed lumber",
    "Sustainable flooring","Bamboo flooring","Parquetry","Terrazzo","Linoleum","Vinyl composition tile",
    "Carpet tile","Resilient flooring","Grout","Caulking","Sealant","Fireproofing","Intumescent",
    # Estetica / design / architettura
    "Interior design","Color theory","Colour wheel","Complementary colors","Color psychology",
    "Modern architecture","Contemporary architecture","Bauhaus","International Style (architecture)",
    "Minimalism","Deconstructivism","Brutalist architecture","Organic architecture","Vernacular architecture",
    "Classical architecture","Gothic architecture","Renaissance architecture","Baroque architecture",
    "Neoclassical architecture","Art Deco","Art Nouveau","Mid-century modern","Postmodern architecture",
    "High-tech architecture","Parametric design","Biophilic design","Sustainable design",
    "Universal design","Inclusive design","Design thinking","Industrial design","Product design",
    "Furniture design","Lighting design","Kitchen","Bathroom","Living room","Bedroom",
    "Open plan","Loft","Penthouse apartment","Villa","Single-family detached home",
    "Townhouse","Duplex (building)","Apartment","Mansion","Facade","Portico","Loggia","Courtyard",
    "Italian garden","Landscape design","Hardscape","Garden design","Urban design",
    "New Urbanism","Mixed-use development","Tall building","Skyscraper","Passive solar building design",
    "Architectural design values","Proportion (architecture)","Golden ratio","Symmetry","Hierarchy (art)",
    "Rhythm (art)","Balance (design)","Contrast (visual)","Emphasis (design)","Harmony (art)",
    "Form follows function","Ornament (art)","Molding (decorative)","Wainscoting","Crown molding",
    "Baseboard","Cornice","Architrave","Skirting board","Stucco decoration","Frieze","Pediment",
    "Column","Pilaster","Capital (architecture)","Entablature","Arch","Vault (architecture)",
    "Dome","Buttress","Spire","Cupola","Atrium (architecture)","Peristyle","Colonnade",
    "Vitruvius","De architectura","De re aedificatoria","The Four Books of Architecture",
    "Treatise","Pattern language","A Pattern Language","Christopher Alexander","Le Corbusier",
    "Frank Lloyd Wright","Ludwig Mies van der Rohe","Alvar Aalto","Louis Kahn","Renzo Piano",
    "Norman Foster","Zaha Hadid","Santiago Calatrava","Tadao Ando","Frank Gehry","Richard Meier",
    "Philip Johnson","Eero Saarinen","Walter Gropius","Marcel Breuer","Charles and Ray Eames",
    "Florence Knoll","Eileen Gray","Ludwig Mies van der Rohe furniture",
    # Comfort / vivibilità / benessere
    "Thermal comfort","Indoor air quality","Sick building syndrome","Daylighting (architecture)",
    "View (architecture)","Noise control","Sound insulation","Reverberation","Lighting design (architecture)",
    "Circadian rhythm","Melatonin","Glare (vision)","Visual comfort","Ergonomics","Biophilia hypothesis",
    "Air change rate","Ventilation (architecture)","Relative humidity","Mean radiant temperature",
    "Operative temperature","Predicted mean vote","Adaptive comfort","Overheating (buildings)",
    "Acoustic quiet","Privacy","Spatial planning","Room","Ceiling","Corridor","Staircase","Handrail",
    "Accessibility","Visitability","Aging in place","Elderly care","Multigenerational home",
    # Prezzi / mercato / economia costruzioni
    "Construction economics","Cost overrun","Cost–benefit analysis","Life-cycle cost analysis",
    "Value engineering","Cost planning","Construction price","Building cost","Construction inflation",
    "Housing affordability","Real estate appraisal","Construction industry","Housing market",
    "Construction productivity","Lean construction","Integrated project delivery","Design–build",
    "Construction management at-risk","Public–private partnership","Build to rent","Build to suit",
]
IT = [
    # Domotica / smart home
    "Domotica","Casa intelligente","Building automation","Automazione edilizia","KNX (standard)",
    "BACnet","Zigbee","Z-Wave","Matter (standard)","MQTT","Thread (protocollo di rete)",
    "Sistema di gestione degli edifici","Edificio intelligente","Internet delle cose","Contatore elettronico",
    "Termostato intelligente","Domotica per la sicurezza","Antifurto","Videocitofono","Impianto di allarme",
    "Controllo accessi","Sensoristica","Sensore di presenza","Attuatore (domotica)","Gateway (reti)",
    "Automazione industriale","Supervisory control and data acquisition",
    # Materiali da costruzione
    "Materiale da costruzione","Blocchi di cemento","Legno lamellare","Legno massiccio incrociato",
    "Legno ingegnerizzato","Compensato","Legno","Legno duro","Legno tenero","Rovere (legno)","Castagno (legno)",
    "Noce (legno)","Larice (legno)","Bambù (materiale)","Bioedilizia","Paglia (materiale edile)",
    "Terra cruda","Fibra di vetro","Lana minerale","Poliuretano espanso","Polistirene espanso",
    "Polistirene estruso","Aerogel","Marmo","Granito","Travertino (roccia)","Calcare","Ardesia",
    "Pietra arenaria","Basalto","Quarzite","Ceramica (materiale)","Gres porcellanato","Terracotta",
    "Vetro","Vetro float","Vetro stratificato","Vetro temperato","Vetro camera","Vetrocamera",
    "Vetro bassoemissivo","Acciaio inox","Acciai corten","Alluminio","Rame","Zinco (materiale)",
    "Titanio (materiale)","Bronzo","Lamiera grecata","Membrana impermeabilizzante","Bitume (materiale)",
    "Calcestruzzo fibrorinforzato","Calcestruzzo ad alta resistenza","Calcestruzzo alleggerito",
    "Cemento geopolimerico","Malta (edilizia)","Malta di calce","Calce (materiale)","Gesso (materiale)",
    "Intonaco (materiale)","Malta cementizia","Parquet","Tarsie","Massetto","Pavimento in resina",
    "Linoleum","Pavimento in PVC","Moquette","Gres","Stucco veneziano","Spatolato",
    "Stucco (materiale)","Stucco veneziano","Cemento resinato","Malta traslucida","Resina epossidica",
    "Sigillante (edilizia)","Mastice","Guarnizione (edilizia)","Coibentazione","Isolamento termico",
    "Isolamento acustico","Isolamento a cappotto","Cappotto termico","Riflettanza (edilizia)",
    "Materiali da costruzione riciclati","Edilizia ecosostenibile","Edilizia verde","Materiali bio-based",
    "Canapa edile","Sughero (materiale)","Sughero espanso","Fibra di cellulosa (isolante)",
    "Legno di recupero","Materiali riciclati (edilizia)",
    # Estetica / design / architettura
    "Interior design","Colorimetria","Ruota dei colori","Colori complementari","Psicologia del colore",
    "Architettura moderna","Architettura contemporanea","Bauhaus","Stile internazionale (architettura)",
    "Minimalismo (arte)","Architettura brutalista","Architettura organica","Architettura vernacolare",
    "Architettura classica","Architettura gotica","Architettura rinascimentale","Architettura barocca",
    "Architettura neoclassica","Art déco","Liberty (stile)","Architettura razionalista","Architettura fascista",
    "Architettura postmoderna","High-tech (architettura)","Design parametrico","Design biophilic",
    "Progettazione sostenibile","Design thinking","Design industriale","Design del prodotto",
    "Design del mobile","Lighting design","Cucina (architettura)","Bagno (architettura)","Soggiorno",
    "Camera da letto","Open space","Loft","Attico","Villa (architettura)","Casa unifamiliare",
    "Villetta a schiera","Bifamiliare","Appartamento","Dimora storica","Facciata (architettura)",
    "Portico","Loggia","Cortile","Giardino all'italiana","Progettazione del paesaggio",
    "Arredo urbano","Edilizia","Grattacielo","Architettura bioclimatica","Architettura passiva",
    "Architettura sostenibile","Forma segue funzione","Ornato (architettura)","Cornice (architettura)",
    "Battiscopa","Stucchi decorativi","Fregio (architettura)","Frontone","Colonna","Pilastro",
    "Capitello","Arco (architettura)","Volta (architettura)","Cupola","Arcata","Atrio (architettura)",
    "Colonnato","Vitruvio","De architectura","Alberti Leon Battista","Andrea Palladio","I quattro libri dell'architettura",
    "Christopher Alexander","Le Corbusier","Frank Lloyd Wright","Ludwig Mies van der Rohe","Alvar Aalto",
    "Louis Kahn","Renzo Piano","Norman Foster","Zaha Hadid","Santiago Calatrava","Tadao Ando",
    "Frank Gehry","Carlo Scarpa","Gio Ponti","Gae Aulenti","Achille Castiglioni","Ettore Sottsass",
    "Marco Zanuso","Vico Magistretti","Bruno Munari","Joe Colombo","Afra e Tobia Scarpa",
    "Aldo Rossi","Paolo Portoghesi","Mario Botta","Massimiliano Fuksas","Cino Zucchi",
    # Comfort / vivibilità
    "Comfort termico","Qualità dell'aria interna","Sindrome dell'edificio malato","Illuminazione naturale",
    "Controllo del rumore","Isolamento acustico","Riverbero","Ergonomia","Ritmo circadiano",
    "Abbagliamento (illuminazione)","Comfort visivo","Tasso di ricambio d'aria","Ventilazione meccanica controllata",
    "Ventilazione (edilizia)","Umidità relativa","Temperatura radiante media","Temperatura operativa",
    "Adaptive comfort","Privacy (architettura)","Progettazione spaziale","Stanza","Soffitto","Corridoio",
    "Scala (edilizia)","Corrimano","Accessibilità","Vivibilità","Abitabilità","Dimensionamento degli ambienti",
    "Invecchiamento attivo","Casa per anziani","Multigenerational home","Design inclusivo",
    "Progettazione universale","Design for all","Barriere architettoniche","Abbattimento delle barriere architettoniche",
    # Prezzi / economia
    "Economia dell'edilizia","Costruzione","Costo di costruzione","Computo metrico","Stima dei costi",
    "Contabilità dei lavori","Prezzario","Listino prezzi","Inflazione edilizia","Mercato immobiliare",
    "Valorizzazione immobiliare","Stima immobiliare","Perito immobiliare","Indice dei prezzi",
    "Produttività nel settore delle costruzioni","Lean construction","Project management",
    "Gestione dei progetti","Appalto integrato","Design-build","Public–private partnership",
    "Build to rent","Sostenibilità economica","Life cycle cost","Costo del ciclo di vita",
    "Valutazione economica","Analisi costi-benefici","Value management","Value engineering",
    "Building cost","Construction cost","Prezzi dei materiali da costruzione",
]

def fetch(lang, titles, fname):
    api = f"https://{lang}.wikipedia.org/w/api.php"
    out = os.path.join(OUT, fname)
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
                    "url": f"https://{lang}.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")),
                    "title": title, "text": txt,
                }
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); got += 1
            redir = {v["to"] for v in d.get("query", {}).get("redirects", [])}
            for t in batch:
                if t not in found and t not in redir:
                    miss.append(t)
            time.sleep(3)
    print(f"[{lang}] nuove voci: {got} | mancanti: {len(miss)}")
    if miss: print("  mancanti:", ", ".join(miss[:30]))

print("=== EN ==="); fetch("en", EN, "wiki_en.jsonl")
print("=== IT ==="); fetch("it", IT, "wiki_it.jsonl")
for f in ("wiki_en.jsonl", "wiki_it.jsonl"):
    p = os.path.join(OUT, f)
    if os.path.exists(p):
        print(f, sum(1 for _ in open(p, encoding="utf-8")))
