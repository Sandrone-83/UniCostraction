#!/usr/bin/env python3
"""fetch_ufgs.py — scarica le specifiche edilizie UFGS (US DoD, PUBLIC DOMAIN) dal bucket S3 WBDG.
Sezioni selezionate su tutte le divisioni CSI: generali, demolizione, calcestruzzo,
muratura, acciaio, legno, coperture, serramenti, finiture, antincendio, idraulico,
climatizzazione, elettrico, movimento terra, esterno, reti.
Riprendibile: salta i file gia' presenti."""
import json, os, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw", "ufgs_specs")
os.makedirs(RAW, exist_ok=True)
S3 = "https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com"

SEZIONI = [
    # Divisione 01 - Generali / gestione cantiere
    "01 33 00", "01 45 00", "01 32 16.00 20", "01 57 19", "01 78 23",
    # Divisione 02-06 - Demolizione, indagini, struttura e materiali
    "02 41 00", "02 32 00", "03 30 00", "03 20 00.00 10", "04 20 00",
    "05 12 00", "05 50 13", "06 10 00", "06 17 19",
    # Divisione 07-10 - Involucro e finiture
    "07 21 13", "07 92 00", "08 11 13", "08 44 00", "08 51 13",
    "09 22 00", "09 29 00", "09 51 00", "09 65 00.00 40", "09 90 00", "10 28 13",
    # Divisione 11-14 - Impianti speciali
    "14 21 13",
    # Divisione 21-28 - Antincendio, idraulico, HVAC, elettrico
    "21 13 13", "22 05 48.00 20", "22 05 83.63", "22 14 29", "22 33 30", "22 42 00.00 40",
    "23 05 48", "23 05 15", "23 05 93", "23 07 00", "23 21 13", "23 23 00", "23 52 00",
    "26 05 19.00 10", "26 05 33", "26 24 13", "26 27 14.00 20", "26 51 00",
    # Divisione 31-34 - Lavori esterni e infrastrutture
    "31 00 00", "31 23 00", "32 12 16.16", "32 13 16.16", "32 16 19",
    "33 11 00", "33 30 00", "33 46 16", "34 11 00",
    # Secondo lotto - approfondimento impianti e strutture
    "23 73 00", "23 64 26", "23 81 00", "23 82 00", "23 51 00", "23 41 00",
    "21 08 00", "21 13 17",
    "22 11 00", "22 13 00", "22 33 00", "22 07 19",
    "26 05 00", "26 28 00", "26 32 13", "26 41 00", "26 43 00",
    "03 40 00", "03 35 00", "03 39 00", "05 31 00", "04 22 00",
    "07 24 00", "07 62 00", "07 84 00", "08 71 00", "09 30 00", "09 68 00",
    "01 33 16", "01 91 13", "02 26 00", "02 65 00", "32 16 13", "33 49 00",
]

cat = json.load(open(os.path.join(HERE, "discovery", "wbdg_all.json"), encoding="utf-8"))["data"]
docs = [x for x in cat if x.get("type") == "UFGS"]

def media_of(d):
    return d.get("mediaFiles") or []

def find_docs(sec):
    prefix = f"UFGS {sec}"
    cand = [x for x in docs if (x.get("title") or "").startswith(prefix)]
    with_media = [x for x in cand if media_of(x)]
    cand = with_media or cand
    cand.sort(key=lambda x: x.get("publishDate") or "", reverse=True)
    return cand

UA = {"User-Agent": "Mozilla/5.0 (research)"}
ok, fail = [], []
for sec in SEZIONI:
    dest = None
    tried = []
    for d in find_docs(sec):
        tasks = []
        for mf in media_of(d):
            fn = mf["fileName"]
            safe = fn.replace(" ", "%20")
            if fn.lower().endswith(".pdf"):
                folders = ("UFGS_ARCHIVES", "UFGS")
            else:
                folders = ("UFGS", "UFGS_ARCHIVES")
            tasks.append((fn, [f"{S3}/FFC/DOD/{f}/{safe}" for f in folders]))
        for rm in (d.get("relatedMaterials") or []):
            fu = rm.get("fileUrl")
            if not fu: continue
            fn = (rm.get("label") or os.path.basename(fu)).replace("/", "_")
            if not os.path.splitext(fn)[1]: fn += os.path.splitext(fu)[1] or ".bin"
            tasks.append((fn, [fu]))
        for fn, urls in tasks:
            local = os.path.join(RAW, fn.replace(" ", "_"))
            if os.path.exists(local) and os.path.getsize(local) > 1000:
                ok.append((sec, fn, "gia' presente")); dest = local; break
            safe = fn.replace(" ", "%20")
            urls = [f"{S3}/FFC/DOD/{f}/{safe}" for f in
                    ("UFGS_ARCHIVES", "UFGS") if fn.lower().endswith(".pdf")] + \
                   [f"{S3}/FFC/DOD/{f}/{safe}" for f in
                    ("UFGS", "UFGS_ARCHIVES") if not fn.lower().endswith(".pdf")]
            for url in urls:
                tried.append(url)
                try:
                    req = urllib.request.Request(url, headers=UA)
                    with urllib.request.urlopen(req, timeout=90) as r, open(local, "wb") as f:
                        f.write(r.read())
                    sz = os.path.getsize(local)
                    if sz < 500:
                        os.remove(local); raise IOError(f"troppo piccolo ({sz}B)")
                    ok.append((sec, fn, f"{sz:,}B")); dest = local; break
                except Exception:
                    continue
            if dest: break
        if dest: break
        # doc senza media scaricabili: prova il successivo
    if not dest and find_docs(sec):
        # fallback: API del singolo documento (contiene fileUrl firmati)
        try:
            alias = find_docs(sec)[0].get("urlAlias")
            if alias:
                slug = alias.rstrip("/").split("/")[-1]
                req = urllib.request.Request(f"https://www.wbdg.org/api/documents/{slug}", headers=UA)
                with urllib.request.urlopen(req, timeout=60) as r:
                    one = json.loads(r.read().decode("utf-8", "ignore")).get("data", {})
                for mf in (one.get("mediaFiles") or []):
                    fu, fn = mf.get("fileUrl"), mf.get("fileName")
                    if not fu or not fn: continue
                    local = os.path.join(RAW, fn.replace(" ", "_"))
                    if os.path.exists(local) and os.path.getsize(local) > 1000:
                        ok.append((sec, fn, "gia' presente")); dest = local; break
                    req2 = urllib.request.Request(fu, headers=UA)
                    with urllib.request.urlopen(req2, timeout=90) as r2, open(local, "wb") as f:
                        f.write(r2.read())
                    ok.append((sec, fn, f"{os.path.getsize(local):,}B")); dest = local; break
        except Exception as e:
            fail.append((sec, f"fallback API: {e}"))
    if not dest and not any(sec == s for s, _ in fail):
        fail.append((sec, "nessun file scaricabile"))
    time.sleep(0.3)

print(f"scaricate/OK: {len(ok)}")
for s, fn, note in ok: print(f"  [ok] {s} {fn} {note}")
print(f"fallite: {len(fail)}")
for s, why in fail: print(f"  [!!] {s} -> {why}")
