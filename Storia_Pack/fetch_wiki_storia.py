#!/usr/bin/env python3
"""fetch_wiki_storia.py — Storia di architettura, costruzioni e ingegneria (Wikipedia en+it).
Focus: storia completa + epoca 1950-oggi. Output: parsed/wiki_storia/. Riprendibile."""
import json, os, time, urllib.parse, urllib.request

UA = {"User-Agent": "KimiResearchBot/1.0 (educational corpus; contact research@example.com)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parsed", "wiki_storia")
os.makedirs(OUT, exist_ok=True)

EN = [
    # Storia generale
    "History of architecture","History of construction","History of structural engineering",
    "History of civil engineering","History of bridges","History of road transport",
    "History of canals","History of rail transport","History of water supply and sanitation",
    "History of electrical engineering","History of plumbing","History of heating",
    "Timeline of architecture","Architectural history","Architectural theory",
    # Antichità
    "Ancient Egyptian architecture","Greek temple","Ancient Greek architecture",
    "Ancient Roman architecture","Roman engineering","Roman concrete","Opus caementicium",
    "Roman bridge","Roman aqueduct","Roman roads","Roman temple","Roman amphitheatre",
    "Arch of Constantine","Pantheon, Rome","Colosseum","Parthenon","Great Pyramid of Giza",
    "Ziggurat","Ancient Roman bathing","Villa rustica","Byzantine architecture","Hagia Sophia",
    # Medioevo
    "Romanesque architecture","Gothic architecture","Gothic cathedrals and churches",
    "Flying buttress","Rib vault","Pointed arch","Medieval architecture","Venetian Gothic architecture",
    "Islamic architecture","Moorish architecture","Mudéjar","Ottoman architecture",
    # Rinascimento-Barocco-Ottocento
    "Renaissance architecture","Filippo Brunelleschi","Leon Battista Alberti","Andrea Palladio",
    "Donato Bramante","Michelangelo","St. Peter's Basilica","Florence Cathedral",
    "Baroque architecture","Gian Lorenzo Bernini","Francesco Borromini","Andrea Pozzo",
    "Neoclassical architecture","Georgian architecture","Victorian architecture",
    "Industrial Revolution","Architecture of the Industrial Revolution","Cast-iron architecture",
    "Crystal Palace","Eiffel Tower","Statue of Liberty","World's Columbian Exposition",
    "Beaux-Arts architecture","City Beautiful movement","Art Nouveau","Art Deco",
    "Victorian decorative arts","Garden city movement","Ebenezer Howard","Garden city",
    # Ingegneri e pionieri
    "Isambard Kingdom Brunel","Thomas Telford","John Rennie (engineer)","George Stephenson",
    "Robert Stephenson","John Smeaton","Gustave Eiffel","John A. Roebling","Washington Roebling",
    "Emily Warren Roebling","Othmar Ammann","David B. Steinman","Fazlur Rahman Khan",
    "William LeMessurier","Ove Arup","Frei Otto","Buckminster Fuller","François Hennebique",
    "Eugène Freyssinet","Robert Maillart","Pier Luigi Nervi","Riccardo Morandi",
    "Antonio Gaudí","Eero Saarinen","El Lissitzky",
    # Moderno e 1950-oggi
    "Modern architecture","International Style (architecture)","Bauhaus","De Stijl",
    "Constructivism (art)","Expressionist architecture","Art Deco architecture",
    "Streamline Moderne","Case Study Houses","Pruitt–Igoe","Urban renewal","New towns movement",
    "Radiant City","Ville Radieuse","Broadacre City","Organic architecture","Fallingwater",
    "Team 10","Metabolism (architecture)","Archigram","Brutalist architecture","Structuralism (architecture)",
    "Postmodern architecture","Deconstructivism","Blobitecture","Parametricism","Neo-futurism",
    "High-tech architecture","Digital architecture","Critical regionalism","Sustainable architecture",
    "New Urbanism","Smart city","Contemporary architecture","Starchitect","Iconic architecture",
    "Skyscraper","Early skyscrapers","Home Insurance Building","Skyscraper design and construction",
    "Burj Khalifa","Empire State Building","Willis Tower","Seagram Building","Sydney Opera House",
    "Guggenheim Museum Bilbao","Centre Pompidou","Lloyd's building","HSBC Main Building",
    "30 St Mary Axe","The Shard","Millau Viaduct","Channel Tunnel","Hoover Dam","Panama Canal",
    "Itaipu Dam","Three Gorges Dam","Gotthard Base Tunnel",
    "Post-war architecture","Mid-century modern","Googie architecture",
    "Metabolism (architecture)","Structural expressionism",
    # Maestri 1950-oggi
    "Rem Koolhaas","Richard Rogers","Jean Nouvel","Peter Zumthor","Herzog & de Meuron",
    "SANAA","Kazuyo Sejima","Ryue Nishizawa","Bjarke Ingels","Moshe Safdie","I. M. Pei",
    "Oscar Niemeyer","Kenzo Tange","Fumihiko Maki","Rafael Moneo","Álvaro Siza",
    "Eduardo Souto de Moura","Glenn Murcutt","Balkrishna Doshi","Lina Bo Bardi",
    "Paulo Mendes da Rocha","Luis Barragán","Walter Burley Griffin","Jørn Utzon",
    # Tecniche e materiali storici
    "Reinforced concrete","Prestressed concrete","Precast concrete","Autoclaved aerated concrete",
    "Thin-shell structure","Space frame","Geodesic dome","Tensegrity","Cable-stayed bridge",
    "Diagrid","Curtain wall","Structural glazing","Membrane structure","Tensile architecture",
    "Earthquake-resistant structures","Base isolation","Damping","Offshore construction",
    "Tunnel boring machine","Caisson (engineering)","Falsework","Scaffolding","Crane (machine)",
    "Tower crane","Elevator","Escalator","Domestic water system","Central heating",
    "History of air conditioning","Air conditioning","Heat pump","District heating",
    "Electrification","Electrical grid","Hydroelectricity","Nuclear power","Solar power",
    "Building-integrated photovoltaics","Wind power","History of lighting","Incandescent light bulb",
    "Fluorescent lamp","LED lamp","Smart grid",
]
IT = [
    "Storia dell'architettura","Storia dell'ingegneria","Storia delle costruzioni",
    "Architettura dell'antico Egitto","Architettura greca","Architettura romana",
    "Ingegneria romana","Opus caementicium","Calcestruzzo romano","Ponti romani",
    "Acquedotto romano","Strade romane","Pantheon (Roma)","Colosseo","Partenone",
    "Piramidi di Egitto","Architettura bizantina","Santa Sofia","Architettura romanica",
    "Architettura gotica","Architettura islamica","Architettura rinascimentale",
    "Filippo Brunelleschi","Leon Battista Alberti","Andrea Palladio","Donato Bramante",
    "Michelangelo","Basilica di San Pietro in Vaticano","Cupola di Santa Maria del Fiore",
    "Architettura barocca","Gian Lorenzo Bernini","Francesco Borromini",
    "Architettura neoclassica","Architettura liberty","Rivoluzione industriale",
    "Palazzo di cristallo","Torre Eiffel","Esposizione universale","Città giardino",
    "Ebenezer Howard","Movimento moderno","Storia del grattacielo","Grattacielo",
    "Isambard Kingdom Brunel","Gustave Eiffel","Pier Luigi Nervi","Riccardo Morandi",
    "Sergio Musmeci","Antonio Gaudí","Movimento razionalista","Architettura razionalista",
    "BBPR","Ernesto Nathan Rogers","Giuseppe Samonà","Ignazio Gardella","Franco Albini",
    "Luigi Moretti","Adalberto Libera","Giovanni Michelucci","Carlo De Carli",
    "Vittorio Gregotti","INA-Casa","Ricostruzione postbellica in Italia",
    "Architettura italiana del Novecento","Brutalismo","Architettura postmoderna",
    "Architettura contemporanea","Architettura ad alta tecnologia","Architettura parametrica",
    "Architettura sostenibile" ,"New Urbanism","Smart city","Città smart",
    "Renzo Piano","Massimiliano Fuksas","Stefano Boeri","Mario Cucinella","Cino Zucchi",
    "5+1AA","ABDR","King Memorandum","Torre dei venti","Grattacielo Pirelli",
    "Torre Velasca","Villaggio Olimpico (Roma)","Milano moderna","Padova Urbs picta",
    "Calcestruzzo armato","Calcestruzzo precompresso","Precompressione","Strutture a guscio",
    "Capriate","Tralicci","Geodetica","Tensegrity","Ponte strallato","Ponte sospeso",
    "Isolamento sismico","Strutture antisismiche","Tunnel","Traforo del Gottardo",
    "Piano regolatore","Urbanistica","Piano regolatore generale","RIU","Piano regolatore italiano",
    "Edilizia residenziale pubblica italiana","Fondo edilizio","Lotto edilizio",
    "Impresa edile","Storia dell'impresa edile","Mezzadria",
]

def fetch(lang, titles, fname):
    api = f"https://{lang}.wikipedia.org/w/api.php"
    out = os.path.join(OUT, fname)
    done = set()
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            for line in f:
                try: done.add(json.loads(line)["title"])
                except Exception: pass
    got, miss = 0, []
    with open(out, "a", encoding="utf-8") as fo:
        for i in range(0, len(titles), 20):
            batch = [t for t in titles[i:i+20] if t not in done]
            if not batch: continue
            params = {"action":"query","format":"json","redirects":"1",
                      "prop":"extracts","explaintext":"1","exlimit":"max",
                      "titles":"|".join(batch)}
            url = api + "?" + urllib.parse.urlencode(params)
            d = None
            for r in range(3):
                try:
                    req = urllib.request.Request(url, headers=UA)
                    with urllib.request.urlopen(req, timeout=90) as resp:
                        d = json.loads(resp.read().decode("utf-8"))
                    break
                except Exception as e:
                    print(f"[retry {r}] {lang}: {e}"); time.sleep(15*(r+1))
            if not d: print("[SALTO]", batch); continue
            pages = d.get("query", {}).get("pages", {})
            found = set()
            for pid, pg in pages.items():
                title = pg.get("title",""); found.add(title)
                txt = pg.get("extract","")
                if not txt or len(txt) < 400: continue
                rec = {"source": f"wikipedia_{lang}", "license": "CC BY-SA 4.0",
                       "commercial_ok": True,
                       "attribution": f"{title} — Wikipedia ({lang}), CC BY-SA 4.0",
                       "url": f"https://{lang}.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ","_")),
                       "title": title, "text": txt}
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); got += 1
            redir = {v["to"] for v in d.get("query", {}).get("redirects", [])}
            miss += [t for t in batch if t not in found and t not in redir]
            time.sleep(3)
    print(f"[{lang}] nuove voci: {got} | mancanti: {len(miss)}")
    if miss: print("  mancanti:", ", ".join(miss[:25]))

print("=== EN ==="); fetch("en", EN, "wiki_storia_en.jsonl")
print("=== IT ==="); fetch("it", IT, "wiki_storia_it.jsonl")
for f in sorted(os.listdir(OUT)):
    print(f, sum(1 for _ in open(os.path.join(OUT, f), encoding="utf-8")))
