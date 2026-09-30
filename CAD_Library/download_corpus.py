# -*- coding: utf-8 -*-
"""Scarica in blocco i file CAD a licenza pulita per il corpus di training.
Fonti: LibreDWG test-data (DXF), ezdxf examples (MIT), assimp test/models (BSD),
ladybug-tools 3d-models (MIT). Esclusi: jscad (nessuna licenza), assimp models-nonbsd,
virtualagc (NOASSERTION)."""
import json, os, urllib.request, concurrent.futures, time

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "training_corpus", "raw")
DISC = os.path.join(ROOT, "discovery")

def raw_url(repo, path, branch="master"):
    return "https://raw.githubusercontent.com/%s/%s/%s" % (repo, branch, path)

jobs = []  # (url, dest_path, source, licenza)

# --- LibreDWG: tutti i DXF di test/test-data ---
lib = json.load(open(os.path.join(DISC, "libredwg.json"), encoding="utf-8"))["tree"]
for t in lib:
    p = t["path"]
    if p.startswith("test/test-data/") and p.lower().endswith(".dxf"):
        rel = p[len("test/test-data/"):]
        jobs.append((raw_url("LibreDWG/libredwg", p),
                     os.path.join(OUT, "libredwg", rel),
                     "LibreDWG/libredwg",
                     "GPL-3.0 (progetto); file di test di varia provenienza"))

# --- ezdxf examples_dxf (MIT) ---
ezd = json.load(open(os.path.join(DISC, "ezdxf_examples.json"), encoding="utf-8"))
for t in ezd:
    if t["name"].lower().endswith(".dxf"):
        jobs.append((t["download_url"],
                     os.path.join(OUT, "ezdxf", t["name"]),
                     "mozman/ezdxf", "MIT"))

# --- assimp test/models BSD: DXF + 3DS ---
ass = json.load(open(os.path.join(DISC, "assimp.json"), encoding="utf-8"))["tree"]
for t in ass:
    p = t["path"]
    if (p.startswith("test/models/DXF/") and p.lower().endswith(".dxf")) or \
       (p.startswith("test/models/3DS/") and p.lower().endswith(".3ds")):
        jobs.append((raw_url("assimp/assimp", p),
                     os.path.join(OUT, "assimp", os.path.basename(p)),
                     "assimp/assimp (test/models, BSD)", "BSD"))

# --- ladybug STEP (MIT) ---
lady = json.load(open(os.path.join(DISC, "ladybug_models.json"), encoding="utf-8"))["tree"]
for t in lady:
    p = t["path"]
    if p.lower().endswith(".stp"):
        jobs.append((raw_url("ladybug-tools/3d-models", p),
                     os.path.join(OUT, "ladybug", os.path.basename(p)),
                     "ladybug-tools/3d-models", "MIT"))

def fetch(job):
    url, dest, source, lic = job
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return (dest, True, "cached")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "cad-training-corpus"})
            data = urllib.request.urlopen(req, timeout=60).read()
            with open(dest, "wb") as f:
                f.write(data)
            return (dest, True, str(len(data)))
        except Exception as e:
            err = str(e); time.sleep(2)
    return (dest, False, err)

print("Download pianificati:", len(jobs))
ok = fail = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for dest, success, msg in ex.map(fetch, jobs):
        if success: ok += 1
        else:
            fail += 1
            print("FALLITO:", dest, msg)
print("OK:", ok, "| falliti:", fail)
