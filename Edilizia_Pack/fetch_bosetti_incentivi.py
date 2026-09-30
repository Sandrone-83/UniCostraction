# -*- coding: utf-8 -*-
"""Scarica atti legislativi IT su incentivi/energia da Bosetti e Gatti (atti pubblici)."""
import os, re, sys, time, urllib.request

BASE = "https://www.bosettiegatti.eu/info/norme/statali/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw", "norme_it")

HDRS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Referer": "https://www.bosettiegatti.eu/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9,en;q=0.8",
}

ACTS = [
    ("2011_0028", "DLgs_28_2011_FER.htm",        "D.Lgs 28/2011 - FER e obbligo agibilita"),
    ("2021_0199", "DLgs_199_2021_CER.htm",       "D.Lgs 199/2021 - CER, autoconsumo, agibilita energetica"),
    ("2014_0102", "DLgs_102_2014_EE_TEE.htm",    "D.Lgs 102/2014 - Efficienza energetica, diagnostica, TEE"),
    ("2012_0282", "DM_28_12_2012_ContoTermico2.htm","DM 28/12/2012 - Conto Termico 2.0"),
    ("2005_0192", "DLgs_192_2005_APE.htm",       "D.Lgs 192/2005 - Certificazione energetica (APE)"),
    ("2020_0034", "DL_34_2020_rilancio.htm",     "D.L. 34/2020 - Rilancio (110%, ecobonus 110%)"),
    ("2021_0176", "DLgs_176_2021_REDII.htm",     "D.Lgs 176/2021 - Recepimento direttiva FER RED II"),
]

def fetch(url):
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

os.makedirs(OUT, exist_ok=True)
ok, fail = [], []
for act, fname, desc in ACTS:
    path = os.path.join(OUT, fname)
    if os.path.exists(path) and os.path.getsize(path) > 20000:
        ok.append(fname); continue
    url = BASE + act + ".htm"
    try:
        data = fetch(url)
        text = data.decode("utf-8", errors="replace")
        # verifica che non sia una pagina di errore
        if "Errore" in text[:2000] and len(text) < 20000:
            raise RuntimeError("pagina errore")
        # paginazione: aggiungi eventuali pagine successive
        pages = []
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        n2 = 2
        while True:
            purl = url[:-4] + f"_{n2}.htm"
            try:
                pdata = fetch(purl).decode("utf-8", errors="replace")
                if len(pdata) < len(text) * 0.5 or pdata.strip() == text.strip():
                    break
                with open(path, "a", encoding="utf-8") as f:
                    f.write("\n<!--PAGINA %d-->\n" % n2 + pdata)
                n2 += 1
                time.sleep(2)
            except Exception:
                break
        print(f"OK {fname} ({len(text)} chars) - {desc}")
        ok.append(fname)
        time.sleep(3)
    except Exception as e:
        print(f"FAIL {fname}: {e}")
        fail.append(fname)
    time.sleep(3)

print("---")
print(f"OK: {len(ok)}  FAIL: {len(fail)}")
for f_ in fail: print("  fallito:", f_)
