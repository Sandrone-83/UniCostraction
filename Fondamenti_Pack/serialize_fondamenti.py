#!/usr/bin/env python3
"""serialize_fondamenti.py — converte i testi grezzi di Fondamenti_Pack in JSONL
training-ready. I file parsed/wiki_fondamenti/*.jsonl (Wikipedia/Wikibooks) sono
già pronti: questo script serializza raw/gutenberg/*.txt (classici public domain)."""
import json, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "parsed")
os.makedirs(OUT, exist_ok=True)

CHUNK = 6000
OVERLAP = 250

GUTENBERG = {
    "Euclid_Elements.txt": ("The Elements of Euclid", "Euclid (ed. school edition)", 1882, "https://archive.org/details/elementsofeuclid00eucl_0"),
    "Calculus_Made_Easy_Thompson.txt": ("Calculus Made Easy", "Silvanus P. Thompson", 1914, "https://archive.org/details/in.ernet.dli.2015.94125"),
    "Flatland_pg201.txt": ("Flatland: A Romance of Many Dimensions", "Edwin A. Abbott", 1884, "https://www.gutenberg.org/ebooks/201"),
    "Plato_Republic_pg1497.txt": ("The Republic", "Plato (tr. Benjamin Jowett)", 1892, "https://www.gutenberg.org/ebooks/1497"),
    "Aristotle_Ethics_pg8438.txt": ("The Nicomachean Ethics", "Aristotle (tr. W. D. Ross)", 1925, "https://www.gutenberg.org/ebooks/8438"),
    "Marcus_Meditations_pg2680.txt": ("Meditations", "Marcus Aurelius (tr. George Long)", 1862, "https://www.gutenberg.org/ebooks/2680"),
    "Russell_Problems_pg5827.txt": ("The Problems of Philosophy", "Bertrand Russell", 1912, "https://www.gutenberg.org/ebooks/5827"),
    "Descartes_Discourse_pg59.txt": ("Discourse on the Method", "René Descartes", 1637, "https://www.gutenberg.org/ebooks/59"),
    "Kant_Critique_pg4280.txt": ("The Critique of Pure Reason", "Immanuel Kant (tr. J. M. D. Meiklejohn)", 1855, "https://www.gutenberg.org/ebooks/4280"),
    "Origin_Species_pg1228.txt": ("On the Origin of Species", "Charles Darwin", 1859, "https://www.gutenberg.org/ebooks/1228"),
    "Einstein_Relativity_pg30155.txt": ("Relativity: The Special and General Theory", "Albert Einstein (tr. Robert W. Lawson)", 1920, "https://www.gutenberg.org/ebooks/30155"),
    "Lavoisier_Chemistry_pg30775.txt": ("Elements of Chemistry", "Antoine Lavoisier (tr. Robert Kerr)", 1790, "https://www.gutenberg.org/ebooks/30775"),
    "Newton_Principia_pg28233.txt": ("Philosophiae Naturalis Principia Mathematica (English)", "Isaac Newton (tr. Andrew Motte)", 1729, "https://www.gutenberg.org/ebooks/28233"),
    "Wittgenstein_Tractatus_tractatuslogicop1971witt.txt": ("Tractatus Logico-Philosophicus", "Ludwig Wittgenstein (tr. C. K. Ogden)", 1922, "https://archive.org/details/tractatuslogicop1971witt"),
}

def clean(t):
    t = re.sub(r"\r\n?", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()

def chunks(text, source, url, attribution, extra):
    paras = re.split(r"\n\s*\n", text)
    out, buf, idx = [], [], 1
    def flush():
        nonlocal buf, idx
        if not buf: return
        body = "\n\n".join(buf).strip()
        if len(body) < 80: buf = []; return
        rec = {"doc_id": f"{source}_{idx:04d}", "source": source,
               "license": "Public domain", "commercial_ok": True,
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
recs = []
for fn, (title, author, year, url) in GUTENBERG.items():
    path = os.path.join(RAW, "gutenberg", fn)
    if not os.path.exists(path):
        print("MANCANTE:", fn); continue
    text = clean(open(path, encoding="utf-8", errors="ignore").read())
    c = chunks(text, "classici_fondamenti", url,
               f"{title}, {author} ({year}) - public domain",
               {"title": title, "author": author, "year": year})
    recs += c
    manifest.append({"file": "parsed/classici_fondamenti.jsonl", "doc": title,
                     "records": len(c), "license": "Public domain", "url": url})
with open(os.path.join(OUT, "classici_fondamenti.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"classici_fondamenti.jsonl: {len(recs)} record")

for f in glob.glob(os.path.join(OUT, "wiki_fondamenti", "*.jsonl")):
    n = sum(1 for _ in open(f, encoding="utf-8"))
    manifest.append({"file": os.path.relpath(f, HERE), "doc": os.path.basename(f),
                     "records": n, "license": "CC BY-SA 4.0", "url": "https://wikimedia.org"})
    print(os.path.basename(f), n)

with open(os.path.join(HERE, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("manifest.json scritto")
