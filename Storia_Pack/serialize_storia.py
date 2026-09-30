#!/usr/bin/env python3
"""serialize_storia.py — Storia_Pack: classici storici + cataloghi edilizia d'epoca
in JSONL training-ready. I file parsed/wiki_storia/*.jsonl sono gia pronti."""
import json, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "parsed")
os.makedirs(OUT, exist_ok=True)
CHUNK, OVERLAP = 6000, 250

CLASSICI = {
    "Fletcher_History_of_Architecture_1905.txt": ("A History of Architecture on the Comparative Method (5th ed.)", "Banister Fletcher", 1905, "https://archive.org/details/ahistoryarchite01fletgoog"),
    "Choisy_Histoire_Architecture_1899.txt": ("Histoire de l'architecture (in francese)", "Auguste Choisy", 1899, "https://archive.org/details/histoire-de-larchitecture"),
    "ViolletLeDuc_Dictionnaire_EN_1858.txt": ("A Rational Dictionary of French Architecture (selezione EN)", "Eugène Viollet-le-Duc", 1858, "https://archive.org/details/5630691_1"),
    "Laugier_Essai_Architecture_1753.txt": ("Essai sur l'architecture (in francese)", "Marc-Antoine Laugier", 1753, "https://archive.org/details/essaisurlarchite00laug"),
    "Durand_Precis_1802.txt": ("Précis des leçons d'architecture données à l'École polytechnique (in francese)", "Jean-Nicolas-Louis Durand", 1802, "https://archive.org/details/prcisdesleon01dura"),
    "FHWA_Americas_Highways_1776_1976.txt": ("America's Highways 1776-1976: A History of the Federal-Aid Program", "U.S. Federal Highway Administration", 1976, "https://archive.org/details/americashighways00unit"),
    "USACE_History_Corps_Engineers_1998.txt": ("The History of the U.S. Army Corps of Engineers", "U.S. Army Corps of Engineers", 1998, "https://archive.org/details/historyofusarmyc00alex"),
}
HABS_HAER = {
    "HABS_Catalog_1941.txt": ("Historic American Buildings Survey - Catalog of the Measured Drawings (1941)", "U.S. National Park Service / Library of Congress", 1941, "https://archive.org/details/historicamerican00nati"),
    "HAER_Boston_Elevated_Railway_1986.txt": ("HAER - Boston Elevated Railway, Massachusetts (ricognizione ingegneristica storica)", "U.S. National Park Service / Library of Congress", 1986, "https://archive.org/details/ma1288data"),
}
CATALOGHI = {
    "Catalogo_vetri_1919.txt": ("Official List of Window Glass", "National Glass Distributors Association", 1919, "https://archive.org/details/OfficialListOfWindowGlass"),
    "Catalogo_acciaio_strutturale_1910.txt": ("Catalogue of Structural Steel & Iron for Architects, Engineers & Contractors", "Cambria Steel Company", 1910, "https://archive.org/details/CatalogueOfStructuralSteelIronForArchitectsEngineersContractors"),
    "Catalogo_infissi_StLouis_1895.txt": ("St. Louis Sash & Door Works - Combined Book of Designs", "St. Louis Sash & Door Works", 1895, "https://archive.org/details/st.-louis-sash-door-works-1895"),
    "Catalogo_legname_infissi_1917.txt": ("Haley Bros. & Co. - Lumber, Doors, Sashes, Interior Finish", "Haley Bros. & Co.", 1917, "https://archive.org/details/HaleyBros.Co.LumberMerchantsManufacturersOfDoorsSashesInterior"),
}

def clean(t):
    t = re.sub(r"\r\n?", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()

def chunks(text, source, url, attribution, extra, license_):
    paras = re.split(r"\n\s*\n", text)
    out, buf, idx = [], [], 1
    def flush():
        nonlocal buf, idx
        if not buf: return
        body = "\n\n".join(buf).strip()
        if len(body) < 80: buf = []; return
        rec = {"doc_id": f"{source}_{idx:04d}", "source": source,
               "license": license_, "commercial_ok": True,
               "attribution": attribution, "url": url, "text": body}
        rec.update(extra); out.append(rec); idx += 1; buf = []
    for p in paras:
        p = p.strip()
        if not p: continue
        if sum(len(b) for b in buf) + len(p) > CHUNK and buf:
            flush()
        if len(p) > CHUNK:
            for i in range(0, len(p), CHUNK - OVERLAP):
                buf = [p[i:i+CHUNK]]; flush()
            buf = []
        else:
            buf.append(p)
    flush()
    return out

manifest = []
for fname, outname, source in [("storia_classici","storia_classici.jsonl","storia_classici"),
                               ("cataloghi_edilizia","cataloghi_edilizia.jsonl","cataloghi_edilizia"),
                               ("habs_haer","habs_haer.jsonl","habs_haer")]:
    META = CLASSICI if fname == "storia_classici" else (CATALOGHI if fname == "cataloghi_edilizia" else HABS_HAER)
    recs = []
    for fn, (title, author, year, url) in META.items():
        path = os.path.join(RAW, fname, fn)
        if not os.path.exists(path):
            print("MANCANTE:", fn); continue
        text = clean(open(path, encoding="utf-8", errors="ignore").read())
        lic = "Public domain (opera del Governo federale USA)" if year > 1929 and "U.S." in author else "Public domain (pubblicato prima del 1930, scan archive.org)"
        c = chunks(text, source, url, f"{title}, {author} ({year}) - public domain",
                   {"title": title, "author": author, "year": year}, lic)
        recs += c
        manifest.append({"file": f"parsed/{outname}", "doc": title, "records": len(c),
                         "license": lic, "url": url})
    with open(os.path.join(OUT, outname), "w", encoding="utf-8") as f:
        for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{outname}: {len(recs)} record")

for f in sorted(glob.glob(os.path.join(OUT, "wiki_storia", "*.jsonl"))):
    n = sum(1 for _ in open(f, encoding="utf-8"))
    manifest.append({"file": os.path.relpath(f, HERE), "doc": os.path.basename(f),
                     "records": n, "license": "CC BY-SA 4.0", "url": "https://wikipedia.org"})
    print(os.path.basename(f), n)

with open(os.path.join(HERE, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("manifest.json scritto")
