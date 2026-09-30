#!/usr/bin/env python3
"""fetch_wiki_fondamenti.py — Fondamenti_Pack: Wikipedia + Wikibooks (CC BY-SA 4.0)
su matematica, fisica, chimica, metodo scientifico e filosofia (en + it)."""
import json, os, time, urllib.parse, urllib.request

UA = {"User-Agent": "KimiResearchBot/1.0 (educational corpus; contact research@example.com)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parsed", "wiki_fondamenti")
os.makedirs(OUT, exist_ok=True)

BOOKS = [  # (wikibook prefix, lingua) — i 3 più utili per il calcolo strutturale
    ("Trigonometry", "en"), ("Calculus", "en"), ("Physics", "en"),
]

WIKI_EN = [
    # Matematica
    "Arithmetic","Algebra","Geometry","Trigonometry","Calculus","Differential calculus",
    "Integral","Linear algebra","Matrix (mathematics)","Vector space","Equation",
    "Function (mathematics)","Limit (mathematics)","Derivative","Statistics","Probability",
    "Combinatorics","Number theory","Euclidean geometry","Analytic geometry","Solid geometry",
    "Conic section","Pi","Pythagorean theorem","Quadratic equation","Logarithm",
    "Exponential function","Trigonometric functions","Polynomial","Fraction","Percentage",
    "Ratio","Unit of measurement","Dimensional analysis","Rounding","Scientific notation",
    "Mathematical notation","Theorem","Mathematical proof","Axiom","Set theory",
    "Mathematical logic","Greek letters used in mathematics, science, and engineering",
    "Trigonometric identities","Hyperbolic functions","Sequence","Series (mathematics)",
    "Complex number","Imaginary number","Square root","Exponentiation",
    "System of linear equations","Determinant","Eigenvalues and eigenvectors",
    "Dot product","Cross product","Coordinate system","Cartesian coordinate system",
    "Polar coordinate system","Angle","Circle","Triangle","Quadrilateral","Polygon",
    "Area","Volume","Perimeter","Surface area","Symmetry","Similarity (geometry)",
    "Transformation (function)","Graph of a function","Slope","Asymptote","Tangent",
    "Optimization","Numerical analysis","Approximation","Mathematical model",
    # Fisica
    "Physics","Classical mechanics","Mechanics","Newton's laws of motion","Kinematics",
    "Dynamics (mechanics)","Work (physics)","Energy","Kinetic energy","Potential energy",
    "Power (physics)","Momentum","Torque","Angular momentum","Friction","Gravity",
    "Gravitation","Projectile motion","Circular motion","Oscillation","Simple harmonic motion",
    "Wave","Sound","Acoustics","Optics","Light","Reflection (physics)","Refraction",
    "Lens (optics)","Electromagnetism","Electric charge","Electric current","Voltage",
    "Electrical resistance and conductance","Ohm's law","Electric field","Magnetic field",
    "Electromagnetic induction","Thermodynamics","Heat","Temperature","Entropy",
    "Laws of thermodynamics","Pressure","Fluid mechanics","Buoyancy","Bernoulli's principle",
    "Modern physics","Theory of relativity","Quantum mechanics","Atomic physics",
    "Nuclear physics","Radioactive decay","Standard Model","Photon","Electron",
    "Measurement","International System of Units","Accuracy and precision","Force",
    "Mass","Weight","Density","Speed","Velocity","Acceleration","Free fall","Inertia",
    "Elasticity","Stress (mechanics)","Strain (mechanics)","Young's modulus","Hooke's law",
    "Shear modulus","Poisson's ratio","Moment of inertia","Beam (structure)",
    "Structural load","Tension (physics)","Compression (physics)","Bending",
    # Chimica / scienza
    "Chemistry","Matter","Atom","Molecule","Chemical element","Periodic table",
    "Chemical bond","Chemical reaction","Acid","Base (chemistry)","PH","Solution",
    "Chemical compound","Organic chemistry","States of matter","Density","Metal",
    "Oxidation","Corrosion","Catalysis","Polymer","Thermoplastic","Thermosetting polymer",
    "Science","Scientific method","Observation","Hypothesis","Experiment","Theory",
    "Scientific theory","Scientific modelling","History of science","Natural science",
    "Peer review","Scientific consensus","Reproducibility",
    # Filosofia
    "Philosophy","Western philosophy","Ancient philosophy","Ancient Greek philosophy",
    "Plato","Aristotle","Socrates","Stoicism","Epicureanism","Eastern philosophy",
    "Indian philosophy","Chinese philosophy","Medieval philosophy","Scholasticism",
    "Thomas Aquinas","Renaissance philosophy","Modern philosophy","Rationalism",
    "Empiricism","René Descartes","John Locke","David Hume","Immanuel Kant",
    "Georg Wilhelm Friedrich Hegel","Friedrich Nietzsche","Karl Marx","Utilitarianism",
    "John Stuart Mill","Jeremy Bentham","Existentialism","Søren Kierkegaard",
    "Jean-Paul Sartre","Martin Heidegger","Phenomenology (philosophy)","Edmund Husserl",
    "Analytic philosophy","Bertrand Russell","Ludwig Wittgenstein","Logic",
    "Deductive reasoning","Inductive reasoning","Argument","Fallacy","Epistemology",
    "Metaphysics","Ethics","Aesthetics","Political philosophy","Philosophy of science",
    "Thomas Kuhn","Paradigm","Falsifiability","Occam's razor","Pragmatism",
    "John Dewey","Confucius","Laozi","Sun Tzu","Niccolò Machiavelli","Baruch Spinoza",
    "Gottfried Wilhelm Leibniz","Voltaire","Jean-Jacques Rousseau","Arthur Schopenhauer",
    "Simone de Beauvoir","Hannah Arendt","Philosophy of mathematics","Philosophy of physics",
]
WIKI_IT = [
    "Matematica","Aritmetica","Algebra","Geometria","Geometria euclidea","Trigonometria",
    "Calcolo infinitesimale","Derivata","Integrale","Equazione","Funzione (matematica)",
    "Matrice","Vettore (matematica)","Teorema","Dimostrazione matematica","Probabilità",
    "Statistica","Numero complesso","Radice quadrata","Logaritmo","Successione (matematica)",
    "Serie (matematica)","Limite (matematica)","Teorema di Pitagora","Circonferenza",
    "Cerchio","Triangolo","Poligono","Area","Volume","Perimetro","Sistema internazionale di unità di misura",
    "Grandezza fisica","Misura","Fisica","Meccanica","Termodinamica","Elettromagnetismo",
    "Ottica","Onda (fisica)","Acustica","Relatività","Meccanica quantistica","Forza",
    "Massa","Peso","Densità","Velocità","Accelerazione","Energia","Lavoro (fisica)",
    "Quantità di moto","Momento angolare","Gravità","Oscillazione","Moto armonico",
    "Fluido","Pressione","Galileo Galilei","Isaac Newton","Albert Einstein",
    "Chimica","Atomo","Molecola","Elemento chimico","Tavola periodica","Legame chimico",
    "Reazione chimica","Acido","Base (chimica)","PH","Soluzione (chimica)",
    "Scienza","Metodo scientifico","Osservazione","Ipotesi","Teoria scientifica",
    "Storia della scienza","Filosofia","Filosofia antica","Filosofia greca","Platone",
    "Aristotele","Socrate","Stoicismo","Epicureismo","Scuola dei giardini","Filosofia medievale",
    "Scolastica","Tommaso d'Aquino","Filosofia moderna","Razionalismo","Empirismo",
    "Cartesio","John Locke","David Hume","Immanuel Kant","Hegel","Friedrich Nietzsche",
    "Karl Marx","Utilitarismo","John Stuart Mill","Esistenzialismo","Kierkegaard",
    "Jean-Paul Sartre","Martin Heidegger","Fenomenologia","Edmund Husserl",
    "Filosofia analitica","Bertrand Russell","Ludwig Wittgenstein","Logica",
    "Ragionamento deduttivo","Ragionamento induttivo","Epistemologia","Metafisica",
    "Etica","Estetica","Filosofia politica","Filosofia della scienza","Paradigma",
    "Rasoio di Occam","Pragmatismo","Confucio","Laozi","Sun Tzu","Niccolò Machiavelli",
    "Baruch Spinoza","Gottfried Wilhelm Leibniz","Voltaire","Jean-Jacques Rousseau",
    "Arthur Schopenhauer","Bioetica","Filosofia del diritto","Ontologia",
]

def api_get(host, params, retries=3):
    url = f"https://{host}/w/api.php?" + urllib.parse.urlencode(params)
    for r in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=90) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"[retry {r}] {host}: {e}"); time.sleep(15 * (r + 1))
    return None

def fetch_extracts(lang, titles, fname):
    api = f"{lang}.wikipedia.org"
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
            d = api_get(api, {"action":"query","format":"json","redirects":"1",
                              "prop":"extracts","explaintext":"1","exlimit":"max",
                              "titles":"|".join(batch)})
            if not d: print("[SALTO]", lang, batch); continue
            pages = d.get("query", {}).get("pages", {})
            found = set()
            for pid, pg in pages.items():
                title = pg.get("title", ""); found.add(title)
                txt = pg.get("extract", "")
                if not txt or len(txt) < 400: continue
                rec = {"source": f"wikipedia_{lang}", "license": "CC BY-SA 4.0",
                       "commercial_ok": True,
                       "attribution": f"{title} — Wikipedia ({lang}), CC BY-SA 4.0",
                       "url": f"https://{lang}.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")),
                       "title": title, "text": txt}
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); got += 1
            redir = {v["to"] for v in d.get("query", {}).get("redirects", [])}
            miss += [t for t in batch if t not in found and t not in redir]
            time.sleep(3)
    print(f"[{lang}] nuove voci: {got} | mancanti: {len(miss)}")
    if miss: print("  mancanti:", ", ".join(miss[:25]))

def fetch_wikibooks(prefix, lang):
    host = f"{lang}.wikibooks.org"
    out = os.path.join(OUT, f"wikibooks_{lang}.jsonl")
    done = set()
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            for line in f:
                try: done.add(json.loads(line)["title"])
                except Exception: pass
    # elenca sottopagine del libro
    subpages = []
    cont = {}
    while True:
        params = {"action":"query","format":"json","list":"allpages",
                  "apprefix": prefix + "/","aplimit":"max"}; params.update(cont)
        d = api_get(host, params)
        if not d: break
        subpages += [p["title"] for p in d.get("query", {}).get("allpages", [])]
        if "continue" in d: cont = d["continue"]
        else: break
    titles = [prefix] + subpages
    print(f"[wikibooks {lang}] '{prefix}': {len(titles)} pagine")
    got = 0
    with open(out, "a", encoding="utf-8") as fo:
        for i in range(0, len(titles), 20):
            batch = [t for t in titles[i:i+20] if t not in done]
            if not batch: continue
            d = api_get(host, {"action":"query","format":"json","redirects":"1",
                               "prop":"extracts","explaintext":"1","exlimit":"max",
                               "titles":"|".join(batch)})
            if not d: continue
            for pid, pg in d.get("query", {}).get("pages", {}).items():
                title = pg.get("title",""); txt = pg.get("extract","")
                if not txt or len(txt) < 300: continue
                rec = {"source": f"wikibooks_{lang}", "license": "CC BY-SA 4.0",
                       "commercial_ok": True,
                       "attribution": f"{title} — Wikibooks ({lang}), CC BY-SA 4.0",
                       "url": f"https://{host}/wiki/" + urllib.parse.quote(title.replace(" ","_")),
                       "book": prefix, "title": title, "text": txt}
                fo.write(json.dumps(rec, ensure_ascii=False) + "\n"); got += 1
            time.sleep(3)
    print(f"  -> nuove pagine: {got}")

for prefix, lang in BOOKS:
    fetch_wikibooks(prefix, lang)
print("=== Wikipedia EN ==="); fetch_extracts("en", WIKI_EN, "wiki_fondamenti_en.jsonl")
print("=== Wikipedia IT ==="); fetch_extracts("it", WIKI_IT, "wiki_fondamenti_it.jsonl")
for f in sorted(os.listdir(OUT)):
    print(f, sum(1 for _ in open(os.path.join(OUT, f), encoding="utf-8")))
