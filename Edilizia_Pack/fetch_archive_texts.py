#!/usr/bin/env python3
"""fetch_archive_texts.py — scarica il testo integrale (_djvu.txt) di elementi archive.org."""
import json, os, sys, time, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (research; contact research@example.com)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw", "manuals_txt")
ITEMS = [
    "utilitiesmani024854mbp",      # US Navy Utilitiesman I (1989) - idraulica/impianti
    "utilitiesmanii024855mbp",     # US Navy Utilitiesman II
    "utilitiesmaniii024856mbp",    # US Navy Utilitiesman III
    "earthmanualwater00kiss",      # USBR Earth Manual (1974) - geotecnica
    "concretemanualma00unit",      # USBR Concrete Manual (1975)
    "designofsmalldam0000vari",    # USBR Design of Small Dams (1974)
]

def get(url, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read() if binary else r.read().decode("utf-8", "ignore")

os.makedirs(OUT, exist_ok=True)
for it in ITEMS:
    dest = os.path.join(OUT, it + ".txt")
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        print(f"[skip] {it} gia' presente"); continue
    try:
        meta = json.loads(get(f"https://archive.org/metadata/{it}"))
        names = [f["name"] for f in meta.get("files", []) if f["name"].endswith("_djvu.txt")]
        if not names:
            print(f"[!!] nessun _djvu.txt per {it}"); continue
        url = f"https://archive.org/download/{it}/{urllib.request.quote(names[0])}"
        data = get(url, binary=True)
        open(dest, "wb").write(data)
        print(f"[ok] {it}: {len(data):,} byte")
        time.sleep(1)
    except Exception as e:
        print(f"[ERRORE] {it}: {e}")
