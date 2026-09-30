#!/usr/bin/env python3
"""build_glossario.py — glossario tecnico bilingue IT-EN dell'edilizia.
Coppie di termini dai collegamenti interlinguistici Wikipedia delle voci del corpus,
con definizione di contesto (primo periodo del testo della voce). Licenza CC BY-SA 4.0."""
import json, os, re, sys, time, urllib.parse, urllib.request

UA = {"User-Agent": "KimiResearchBot/1.0 (educational corpus; contact research@example.com)"}
HERE = os.path.dirname(os.path.abspath(__file__))
PARSED = os.path.join(HERE, "parsed")

# raccogli titoli e testi dalle voci wiki del corpus
TITLES = {}   # title -> (pack_dir, first_sentence)
for d in ("wiki_construction", "wiki_incentivi", "wiki_engineering", "wiki_design"):
    pdir = os.path.join(PARSED, d)
    if not os.path.isdir(pdir):
        continue
    for fn in os.listdir(pdir):
        if not fn.endswith(".jsonl"):
            continue
        lang = "it" if fn.endswith("_it.jsonl") else "en"
        for line in open(os.path.join(pdir, fn), encoding="utf-8"):
            try:
                r = json.loads(line)
            except Exception:
                continue
            t = r.get("title", "").strip()
            txt = r.get("text", "")
            m = re.split(r"(?<=[.!?])\s+", txt.strip())
            first = m[0][:400] if m else ""
            if t:
                TITLES.setdefault((lang, t), (d, first))
print("voci nel corpus:", len(TITLES))

def langlinks_batch(lang, titles):
    """Ritorna dict titolo -> equivalente nell'altra lingua (best effort)."""
    api = f"https://{lang}.wikipedia.org/w/api.php"
    other = "en" if lang == "it" else "it"
    out = {}
    for i in range(0, len(titles), 25):
        batch = titles[i:i+25]
        params = {"action": "query", "format": "json", "redirects": "1",
                  "prop": "langlinks", "lllang": other, "lllimit": "max",
                  "titles": "|".join(batch)}
        url = api + "?" + urllib.parse.urlencode(params)
        d = None
        for retry in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                    d = json.loads(r.read().decode("utf-8"))
                break
            except Exception as e:
                print(f"[retry {retry}] {lang}: {e}"); time.sleep(15 * (retry + 1))
        if not d:
            continue
        redir = {v["from"]: v["to"] for v in d.get("query", {}).get("redirects", [])}
        for pg in d.get("query", {}).get("pages", {}).values():
            t = pg.get("title", "")
            links = pg.get("langlinks", [])
            if links:
                out[t] = links[0]["*"]
        time.sleep(2.2)
    return out

it_titles = sorted({t for (l, t) in TITLES if l == "it"})
en_titles = sorted({t for (l, t) in TITLES if l == "en"})
print("titoli IT:", len(it_titles), "| titoli EN:", len(en_titles))

pairs = {}   # it_term -> (en_term, definizione, pack)
ll_it = langlinks_batch("it", it_titles)
print("coppie IT->EN:", len(ll_it))
for it_t, en_t in ll_it.items():
    pack, first = TITLES.get(("it", it_t), ("", ""))
    pairs[it_t] = (en_t, first, pack)

# anche EN->IT per i titoli EN senza coppia
ll_en = langlinks_batch("en", en_titles)
print("coppie EN->IT:", len(ll_en))
for en_t, it_t in ll_en.items():
    if it_t not in pairs:
        pack, first = TITLES.get(("en", en_t), ("", ""))
        pairs[it_t] = (en_t, first, pack)

OUT = os.path.join(PARSED, "glossario_bilingue.jsonl")
DOMINIO = {"wiki_construction": "edilizia e costruzioni",
           "wiki_incentivi": "incentivi ed energia",
           "wiki_engineering": "ingegneria, impianti e progetto",
           "wiki_design": "design, materiali e stile"}
n = 0
with open(OUT, "w", encoding="utf-8") as f:
    for it_t in sorted(pairs):
        en_t, first, pack = pairs[it_t]
        rec = {
            "termine_it": it_t,
            "termine_en": en_t,
            "dominio": DOMINIO.get(pack, "edilizia"),
            "definizione": first,
            "source": "wikipedia_langlinks",
            "license": "CC BY-SA 4.0",
            "commercial_ok": True,
            "attribution": f"{it_t} / {en_t} — Wikipedia (it/en), CC BY-SA 4.0",
            "url": "https://it.wikipedia.org/wiki/" + urllib.parse.quote(it_t.replace(" ", "_")),
        }
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        n += 1
print("glossario:", n, "coppie ->", OUT)
