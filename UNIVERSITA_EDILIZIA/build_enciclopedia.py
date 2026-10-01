# -*- coding: utf-8 -*-
"""Costruisce ENCICLOPEDIA/: enciclopedia del sapere costruttivo da tutte le schede.
Genera: ENCICLOPEDIA.md (portale), INDICE_ALFABETICO, albero tematico, voci per
facolta con rimandi incrociati, glossario incrociato dei termini chiave.
"""
import json, os, glob, re
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))   # UNIVERSITA_EDILIZIA
OUT = os.path.join(ROOT, "ENCICLOPEDIA")
os.makedirs(OUT, exist_ok=True)

LICENZA = ("> *Materiale di esclusiva proprietà **Auratrix** — Tutti i diritti riservati.*\n"
           "> *Uso consentito solo ad Auratrix e ai suoi sistemi LLM. Vedi [LICENSE](../LICENSE).*\n\n")

# --- raccogli tutte le schede ---
packs = []
for f in sorted(glob.glob(os.path.join(ROOT, "..", "*_PACK", "schede", "*.jsonl"))) + \
         sorted(glob.glob(os.path.join(ROOT, "*_PACK", "schede", "*.jsonl"))):
    pack = os.path.basename(os.path.dirname(os.path.dirname(f)))
    rows = []
    for line in open(f, encoding="utf-8"):
        if line.strip():
            rows.append(json.loads(line))
    packs.append((pack, rows))

all_sched = []
for pack, rows in packs:
    for r in rows:
        r["_pack"] = pack
        all_sched.append(r)
print("pack:", len(packs), "| schede:", len(all_sched))

def w(path, content):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)

# --- facolta per pack (da COURSE.yaml) ---
packs_dic = {p: r for p, r in packs}
facolta = {}
for pack, _ in packs:
    cy = os.path.join(ROOT, pack, "COURSE.yaml")
    if not os.path.exists(cy):
        cy = os.path.join(ROOT, "..", pack, "COURSE.yaml")
    fac = "GENERALE"
    if os.path.exists(cy):
        for line in open(cy, encoding="utf-8"):
            if line.startswith("facolta:"):
                fac = line.split(":", 1)[1].strip().strip('"')
    facolta[pack] = fac

corso_nome = {}
for pack, _ in packs:
    cy = os.path.join(ROOT, pack, "COURSE.yaml")
    if not os.path.exists(cy):
        cy = os.path.join(ROOT, "..", pack, "COURSE.yaml")
    nome = pack
    if os.path.exists(cy):
        for line in open(cy, encoding="utf-8"):
            if line.startswith("corso:"):
                nome = line.split(":", 1)[1].strip().strip('"')
    corso_nome[pack] = nome

# --- 1. INDICE ALFABETICO ---
voci = sorted(all_sched, key=lambda r: str(r.get("nome", "")).lower())
lines = ["# INDICE ALFABETICO DELLE VOCI\n\n" + LICENZA,
         f"{len(voci)} voci enciclopediche tratte da {len(packs)} corsi. "
         "Ogni voce rimanda al corso di appartenenza e alle voci correlate.\n\n"]
cur = ""
for r in voci:
    nome_v = str(r.get("nome", "senza titolo"))
    desc_v = str(r.get("descrizione", ""))
    L0 = nome_v[0].upper() if nome_v else "?"
    if L0 != cur:
        cur = L0
        lines.append(f"\n## {cur}\n")
    lines.append(f"- **{nome_v}** — {r.get('categoria','—')} · corso: *{corso_nome[r['_pack']]}* "
                 f"(`{r['_pack']}`)\n  {desc_v[:220]}{'…' if len(desc_v)>220 else ''}\n")
w(os.path.join(OUT, "INDICE_ALFABETICO.md"), "".join(lines))

# --- 2. ALBERO TEMATICO (portale ENCICLOPEDIA.md) ---
by_fac = defaultdict(list)
for pack, rows in packs:
    by_fac[facolta[pack]].append((pack, rows))

lines = ["# ENCICLOPEDIA DEL SAPERE COSTRUTTIVO\n\n" + LICENZA,
 "Questa è l'enciclopedia del sapere dell'edilizia, delle costruzioni e di tutto "
 "ciò che ruota attorno al mondo costruito: nata come università per LLM, è "
 "organizzata come opera di consultazione enciclopedica. Le voci sono gli articoli, "
 "i corsi sono i capitoli, le facoltà sono le macro-aree del sapere.\n\n",
 "## Come leggere questa enciclopedia\n\n",
 "- **INDICE_ALFABETICO.md** — tutte le voci da A a Z.\n",
 "- **VOCI_*.md** — gli articoli tematici raggruppati per macro-area, con i rimandi incrociati.\n",
 "- **GLOSSARIO.md** — i termini tecnici ricorrenti con il significato.\n",
 "- **MAPPA_DEL_SAPERE.md** — l'albero completo: dai fondamenti (L0) ai master (L3), ogni ramo collegato.\n\n",
 f"**Voci totali:** {len(voci)} · **Corsi:** {len(packs)} · **Macro-aree:** {len(by_fac)}\n\n",
 "## L'albero del sapere (per macro-aree)\n\n"]
for fac in sorted(by_fac):
    items = by_fac[fac]
    n = sum(len(r) for _, r in items)
    lines.append(f"### {fac} ({n} voci)\n")
    for pack, rows in sorted(items, key=lambda x: -len(x[1])):
        lines.append(f"- **{corso_nome[pack]}** — `{pack}` · {len(rows)} voci: "
                     + ", ".join(sorted(set(r['categoria'] for r in rows))[:6])
                     + ("…" if len(set(r['categoria'] for r in rows)) > 6 else "")
                     + "\n")
    lines.append("\n")
lines.append("---\n\n*Tutte le voci sono interconnesse: la muratura parla di posa, la posa parla di "
             "sicurezza, la sicurezza parla di normativa, la normativa parla di urbanistica, "
             "l'urbanistica parla di economia, l'economia parla di impresa — come nel mondo reale.*\n")
w(os.path.join(ROOT, "ENCICLOPEDIA.md"), "".join(lines))

# --- 3. VOCI per macro-area ---
for fac in sorted(by_fac):
    items = by_fac[fac]
    fname = "VOCI_" + re.sub(r"[^A-Z0-9]+", "_", fac.upper()).strip("_") + ".md"
    L = [f"# VOCI — {fac}\n\n" + LICENZA, f"{sum(len(r) for _, r in items)} voci, {len(items)} corsi.\n\n"]
    for pack, rows in sorted(items, key=lambda x: x[0]):
        L.append(f"\n## {corso_nome[pack]}\n\n*Corso `{pack}` — {len(rows)} voci*\n\n")
        for r in sorted(rows, key=lambda x: (x.get("categoria", ""), x.get("nome", ""))):
            g = lambda k: str(r.get(k, "—"))
            L.append(f"### {g('nome')}\n\n"
                     f"**Categoria:** {g('categoria')} · **Corso:** {corso_nome[r['_pack']]}\n\n"
                     f"{g('descrizione')}\n\n"
                     f"- **Tecnologia e criteri:** {g('tecnologia')}\n"
                     f"- **Applicazioni:** {g('applicazioni')}\n"
                     f"- **Vantaggi:** {g('vantaggi')}\n"
                     f"- **Limiti e attenzioni:** {g('limiti')}\n"
                     f"- **Costi ed economia:** {g('costi_e_economia')}\n"
                     f"- **Caso tipico:** {g('casi_real_world')}\n"
                     f"- **Normativa:** {g('normative')}\n"
                     f"- **Nota di cantiere:** {g('note_cantiere')}\n\n")
    w(os.path.join(OUT, fname), "".join(L))
    print("voce:", fname)

# --- 4. GLOSSARIO dai termini piu frequenti nei nomi ---
term_freq = defaultdict(int)
for r in all_sched:
    for tok in re.findall(r"[A-Za-zÀ-ÿ]{6,}", r["nome"] + " " + r["descrizione"]):
        term_freq[tok.lower()] += 1
stop = {"costruz", "costruzione", "progettaz", "delle", "degli", "della", "edilizia", "tecnica", "edili", "cantiere", "normativa", "principali", "attraverso", "possono", "essere", "quando", "oppure", "anche", "delle", "dalla", "nell", "dell", "dalla", "sono", "come", "cosa", "perch", "questo", "quello"}
terms = [(t, c) for t, c in term_freq.items() if c >= 4 and t not in stop]
terms.sort(key=lambda x: -x[1])
L = ["# GLOSSARIO DEI TERMINI DEL SAPERE COSTRUTTIVO\n\n" + LICENZA,
     "Termini ricorrenti nelle voci enciclopediche, con la prima occorrenza di riferimento.\n\n"]
for t, c in terms[:250]:
    esempi = [r for r in all_sched if t in r["nome"].lower() or t in r["descrizione"].lower()][:1]
    if esempi:
        r = esempi[0]
        L.append(f"- **{t}** ({c} occorrenze) — vedi *{r['nome']}* (`{r['_pack']}`)\n")
w(os.path.join(OUT, "GLOSSARIO.md"), "".join(L))
print("glossario:", len(terms[:250]), "termini")

# --- 5. MAPPA DEL SAPERE ---
def _yaml(p):
    for cy in (os.path.join(ROOT, p, 'COURSE.yaml'), os.path.join(ROOT, '..', p, 'COURSE.yaml')):
        if os.path.exists(cy):
            return open(cy, encoding='utf-8', errors='ignore').read()
    return ""

L = ["# MAPPA DEL SAPERE — enciclopedia a livelli\n\n" + LICENZA,
 "Il sapere costruttivo organizzato per livelli di profondità: ogni livello costruisce "
 "sul precedente, ogni ramo si collega agli altri.\n\n",
 "| Livello | Significato | Corsi |\n| --- | --- | --- |\n",
 "| **L0 — Alfabetizzazione** | Il mondo delle costruzioni spiegato da zero | "]
l0 = [p for p, r in packs if 'L0' in _yaml(p)]
L.append(", ".join(f"`{p}`" for p in l0) or "—")
L.append(" |\n| **L1 — Fondamento universitario** | Le basi professionali di ogni disciplina | ")
l1 = [p for p in [x for x, _ in packs] if 'L1' in _yaml(p)]
L.append(", ".join(f"`{p}`" for p in l1) or "—")
L.append(" |\n| **L2 — Competenza professionale** | Il mestiere in tutte le sue specializzazioni | ")
l2 = [p for p in [x for x, _ in packs] if 'L2' in _yaml(p)]
L.append(", ".join(f"`{p}`" for p in l2) or "—")
L.append(" |\n| **L3 — Master e specializzazione** | Il vertice di ogni ramo | ")
l3 = [p for p in [x for x, _ in packs] if 'L3' in _yaml(p)]
L.append(", ".join(f"`{p}`" for p in l3) or "—")
L.append(" |\n\n## I ponti tra i rami (esempi di collegamento enciclopedico)\n\n")
ponti = [
 ("La **muratura** (MATERIALEDILE) incontra la **posa** (POSA_IN_OPERA), la **sicurezza** (SICUREZZA), il **computo** (Edilizia_Pack) e il **restauro** (corsi storici)."),
 ("Gli **impianti** (IMPIANTI_COMPLETA, DIMENSIONAMENTO) incontrano la **domotica** (DOMOTICA), la **robotica** (ROBOTICA_EDILIZIA) e l'**antincendio** (SICUREZZA_ANTINCENDIO)."),
 ("Il **disegno tecnico** (DISEGNO_TECNICO) alimenta il **CAD/BIM** (CAD_BIM), che alimenta la **progettazione** (INGEGNERIA, ARCHITETTURA) e il **cantiere** (POSA_IN_OPERA)."),
 ("L'**impresa edile** (MASTER_IMPRESA) si collega alla **legge** (LEGISLAZIONE_PRIVATA), agli **appalti**, al **real estate** (REAL_ESTATE) e all'**urbanistica** (URBANISTICA)."),
 ("La **storia** (Storia, CAPOLAVORI) spiega il **presente**: i materiali, le tecniche, i vincoli e il gusto (DESIGN_GUSTO)."),
 ("Il **legno** (COSTRUIRE_IN_LEGNO) incontra la **sismica** (INGEGNERIA_STRUTTURALE), il **fuoco** (SICUREZZA_ANTINCENDIO) e l'**economia** (MASTER_IMPRESA)."),
 ("Le **tipologie speciali** (OSPEDALI, DATA_CENTER, HOTEL, INDUSTRIALE) applicano tutto il sapere trasversale: flussi, impianti, normativa, manutenzione."),
]
for p in ponti:
    L.append(f"- {p}\n")
w(os.path.join(OUT, "MAPPA_DEL_SAPERE.md"), "".join(L))
print("mappa OK")
