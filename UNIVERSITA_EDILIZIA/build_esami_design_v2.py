# -*- coding: utf-8 -*-
"""DESIGN_GUSTO v2 — esame rigenerato con criterio content-locked.

Lezione della gara di ammissione (2026-10-02): un candidato senza corpus ha
ottenuto 97% sull'esame v1 perché i distrattori delle schede sorelle rendono
le domande "appartiene alla tecnologia" risolvibili per tematica.

V2 cambia la composizione:
- CLOZE numeriche: frase vera della scheda con UN dato cancellato (numero+unità);
  i distrattori sono dati numerici di altre schede dello stesso settore.
  Non risolvibili senza aver letto la scheda.
- Mantenuti solo i tipi locked: casi real world, costi, note di cantiere,
  quadri normativi, vantaggi/limiti (quota ridotta).
- Eliminati: ST1 "appartiene alla tecnologia", STNOT, applicazioni, riassunti.
"""
import json, os, random, io, re

ROOT = os.path.dirname(os.path.abspath(__file__))   # UNIVERSITA_EDILIZIA
WS = os.path.dirname(ROOT)

random.seed(73)

ABBR = r'(D\.Lgs|D\.P\.R|D\.M|D\.L|Art|art|C\.M|ecc|circ|Circ|Prot|prot|n)'

# Unità in ordine di lunghezza decrescente (la regex prova le alternative in ordine:
# prima "kW" di "kWh" lascerebbe "h" orfano idem per m/ml/mln, g/kg, mesi/m...).
# Il lookahead finale vieta che l'unità sia solo un prefisso della parola successiva
# (es. "18 m" dentro "18 mesi" o "500 ml" dentro "500 mln"): in quel caso il match
# dell'unità fallisce e si cade sul numero da solo, che è corretto.
NUM = re.compile(r"\d+(?:[.,]\d+)?(?:-\d+(?:[.,]\d+)?)?\s?(?:€/punto luce|€/giorno|€/ml|€/m²|€/\s?5\s?L|giorni|anni|mesi|mani|kWh|MWh|kWp|mln|kW|MW|GW|kJ|mm|cm|m²|ml|kg|bar|°C|V|A|W|g|t|K|m|€|%)?(?![a-zàèéìòù])")
PROP = re.compile(r"\b[A-ZÀÈÉÌÒÙ][a-zàèéìòù]{2,}\b")
STOP = set(["La","Le","Il","I","Lo","Gli","Un","Una","Uno","E","O","Ma","Che","Chi","Cosa","Come","Quando","Dove","Per","Con","Non","È","Sono","Ha","Hanno","Si","Lo","Al","Allo","Alla","Alle","Ai","Ne","Il","Questo","Questa","Queste","Da","Di","Del","Della","Dello","Delle","Dei","In","A","Su","Se","Una","Vero","Falso"])

def clauses(text):
    t = re.sub(ABBR + r'\.', r'\1§', text or '')
    out = []
    for c in re.split(r'[;]|(?<!\d)\.\s+', t):
        c = c.replace('§', '.').strip(' ;.')
        # scarta clausole troncate (es. "(es") o troppo corte/lunghe
        if len(c) > 25 and len(c) < 420 and not c.endswith(('(es', '(', 'es', 'vs')):
            out.append(c)
    return out

def load(pack):
    path = os.path.join(ROOT, pack, "schede", "schede.jsonl")
    out = []
    with io.open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                out.append(json.loads(line))
    return out

QUESTIONS = []

def add(testo, correct, distractors, spiegazione, fonte):
    ds = []
    for x in distractors:
        x = (x or "").strip()
        if x and x != correct and x not in ds:
            ds.append(x)
        if len(ds) >= 3:
            break
    if len(ds) < 3 or correct in ds:
        return False
    scelte = ds[:3] + [correct]
    random.shuffle(scelte)
    QUESTIONS.append((testo, scelte, scelte.index(correct), spiegazione, fonte))
    return True

def numeric_pool(schede, nome):
    """Tutti i token numerici (con unità) delle altre schede, per distrattori cloze."""
    vals = []
    for d in schede:
        if d["nome"] == nome:
            continue
        for fld in ("tecnologia", "costi_e_economia", "note_cantiere", "vantaggi", "limiti", "descrizione"):
            for m in NUM.finditer(d.get(fld, "")):
                v = m.group(0).strip()
                if len(v) >= 2:
                    vals.append(v)
    random.shuffle(vals)
    return vals

def unit_of(tok):
    m = re.search(r'[a-zA-Z€°%/²³]+$', tok.strip())
    return m.group(0) if m else ""

CLOZE_STEMS = [
    "La scheda «{n}» afferma: «{c}». Quale valore manca?",
    "Completa la frase della scheda «{n}»: «{c}»",
    "Nella frase della scheda «{n}» un dato è stato sostituito da ___: «{c}». Quale è il valore corretto citato dalla scheda?",
    "Quale cifra è citata nella scheda «{n}» nella frase seguente? «{c}»",
]

def gen(pack, titolo, target):
    global QUESTIONS
    QUESTIONS = []
    schede = load(pack)

    # ---- TIPO 1: cloze numeriche (la spina dorsale dell'esame) ----
    # Ammesse anche frasi con più numeri: uno solo cancellato per domanda, e nessun
    # distrattore può essere un numero ancora visibile nella frase.
    for d in schede:
        nome = d["nome"]
        for fld in ("tecnologia", "costi_e_economia", "note_cantiere", "descrizione"):
            for c in clauses(d.get(fld, "")):
                ms = [m for m in NUM.finditer(c) if len(m.group(0).strip()) >= 2]
                if not ms:
                    continue
                m = random.choice(ms)
                raw = m.group(0)
                tok = raw.strip()
                # indici della parte stripped: evita che la \s? della regex mangi lo spazio dopo il numero
                s0 = m.start() + (len(raw) - len(raw.lstrip()))
                s1 = m.end() - (len(raw) - len(raw.rstrip()))
                prev = c[:s0].rstrip().split(" ")[-1].rstrip(".:") if c[:s0].strip() else ""
                if prev in ("Legge", "D.Lgs", "D.M", "DM", "Art", "n", "del", "CIR", "Circ"):
                    continue  # mai cancellare numeri che sono parte del nome di legge/decreto/articolo
                cloze = (c[:s0] + "___" + c[s1:]).strip()
                if "___" not in cloze or len(cloze) < 30:
                    continue
                visibili = {x.group(0).strip() for x in ms} - {tok}
                pool = numeric_pool(schede, nome)
                same_u = [v for v in pool if unit_of(v) == unit_of(tok) and v != tok and v not in visibili]
                dist = same_u[:2] + [v for v in pool if v != tok and v not in visibili and v not in same_u]
                add(random.choice(CLOZE_STEMS).format(n=nome, c=cloze), tok, dist,
                    f"Il valore «{tok}» è citato testualmente nella scheda «{nome}»; gli altri valori appartengono ad altre schede del settore.",
                    f"{pack} / {nome}")

    # ---- TIPO 1b: cloze su nomi propri (designer, marchi, eventi) ----
    def prop_pool(nome):
        vals = []
        for d2 in schede:
            if d2["nome"] == nome:
                continue
            for fld in ("tecnologia", "note_cantiere", "descrizione", "casi_real_world", "vantaggi", "limiti"):
                for c2 in clauses(d2.get(fld, "")):
                    for m2 in PROP.finditer(c2):
                        if m2.group(0) not in STOP:
                            vals.append(m2.group(0))
        random.shuffle(vals)
        return vals

    for d in schede:
        nome = d["nome"]
        for fld in ("tecnologia", "note_cantiere", "descrizione", "casi_real_world"):
            for c in clauses(d.get(fld, "")):
                cands = [m for m in PROP.finditer(c)
                         if m.start() > 2 and m.group(0) not in STOP]
                if not cands:
                    continue
                m = random.choice(cands)
                tok = m.group(0)
                cloze = (c[:m.start()] + "___" + c[m.end():]).strip()
                if len(cloze) < 30 or tok in cloze:
                    continue
                # i distrattori non devono contenere nomi ancora visibili nella frase
                dist = [v for v in prop_pool(nome)
                        if v not in STOP and v not in cloze and v != tok]
                add(random.choice(CLOZE_STEMS).format(n=nome, c=cloze), tok, dist,
                    f"Il nome «{tok}» è citato testualmente nella scheda «{nome}»; gli altri nomi appartengono ad altre schede del settore.",
                    f"{pack} / {nome}")

    # ---- TIPO 2: casi real world (dettagli specifici del pack) ----
    for d in schede:
        nome = d["nome"]
        add(f"Qual è il caso reale (casi real world) descritto nella scheda «{nome}»?",
            d["casi_real_world"], [x["casi_real_world"] for x in schede if x["nome"] != nome],
            f"È il caso reale documentato nella scheda «{nome}».", f"{pack} / {nome}")

    # ---- TIPO 3: costi ----
    STC = ["Quale dato economico o di costo è citato nella scheda «{n}»?",
           "Secondo la scheda «{n}», quale indicazione di costo è corretta?"]
    for d in schede:
        for i, c in enumerate(clauses(d.get("costi_e_economia", ""))):
            add(STC[i % 2].format(n=d["nome"]), c,
                pool_of(schede, "costi_e_economia", d["nome"]),
                f"È un dato economico della scheda «{d['nome']}»; le altre opzioni sono dati economici di schede diverse dello stesso settore.",
                f"{pack} / {d['nome']}")

    # ---- TIPO 4: note di cantiere ----
    ST2 = ["Quale accorgimento è nelle note di cantiere della scheda «{n}»?",
           "Per lavorare correttamente su «{n}», cosa raccomandano le note di cantiere?"]
    for d in schede:
        for i, c in enumerate(clauses(d.get("note_cantiere", ""))):
            add(ST2[i % 2].format(n=d["nome"]), c,
                pool_of(schede, "note_cantiere", d["nome"]),
                f"È una nota di cantiere della scheda «{d['nome']}»; le altre opzioni sono note di schede diverse dello stesso settore.",
                f"{pack} / {d['nome']}")

    # ---- TIPO 5: quadri normativi ----
    for d in schede:
        add(f"Quale quadro normativo è citato nella scheda «{d['nome']}»?",
            d["normative"], [x["normative"] for x in schede if x["nome"] != d["nome"]],
            f"È il quadro normativo della scheda «{d['nome']}».", f"{pack} / {d['nome']}")

    # ---- TIPO 6: vantaggi/limiti (quota ridotta, solo se avanza spazio) ----
    ST3 = "Quale di questi è un vantaggio documentato di «{n}»?"
    ST4 = "Tra questi, quale limite è dichiarato nella scheda «{n}»?"
    for d in schede:
        for c in clauses(d.get("vantaggi", ""))[:1]:
            add(ST3.format(n=d["nome"]), c,
                clauses(d.get("limiti", "")) + pool_of(schede, "limiti", d["nome"]),
                f"È un vantaggio della scheda «{d['nome']}»; gli altri sono limiti o svantaggi.", f"{pack} / {d['nome']}")
        for c in clauses(d.get("limiti", ""))[:1]:
            add(ST4.format(n=d["nome"]), c,
                clauses(d.get("vantaggi", "")) + pool_of(schede, "vantaggi", d["nome"]),
                f"È un limite della scheda «{d['nome']}»; gli altri sono vantaggi.", f"{pack} / {d['nome']}")

    # dedup e taglio
    uniq = {}
    for q in QUESTIONS:
        uniq.setdefault((q[0], q[1][q[2]]), q)
    QUESTIONS = list(uniq.values())
    random.shuffle(QUESTIONS)
    QUESTIONS = QUESTIONS[:target]

    outdir = os.path.join(ROOT, "ESAMI", titolo)
    os.makedirs(outdir, exist_ok=True)
    lines = [f"# ESAME — {titolo.replace('_', ' ')} ({len(QUESTIONS)} domande) — VERSIONE 2 content-locked\n",
             "Risposte NON presenti: il file chiave è riservato (fuori repository).",
             "Criterio: le domande verificano la conoscenza TESTUALE delle schede del pack (dati, frasi, casi).",
             "Le opzioni sbagliate sono errori plausibili di uno specialista della stessa materia.\n"]
    for i, (testo, scelte, idx, spieg, fonte) in enumerate(QUESTIONS, 1):
        lines.append(f"## Domanda {i}\n")
        lines.append(testo + "\n")
        for lettera, s in zip("ABCD", scelte):
            lines.append(f"- {lettera}) {s}")
        lines.append("")
    io.open(os.path.join(outdir, "domande.md"), "w", encoding="utf-8").write("\n".join(lines))

    rdir = os.path.join(WS, "ESAMI_RISPOSTE")
    os.makedirs(rdir, exist_ok=True)
    with io.open(os.path.join(rdir, f"{titolo}_risposte.jsonl"), "w", encoding="utf-8") as f:
        for i, (testo, scelte, idx, spieg, fonte) in enumerate(QUESTIONS, 1):
            f.write(json.dumps({"n": i, "testo": testo, "risposta": scelte[idx],
                                "lettera": "ABCD"[idx], "spiegazione": spieg, "fonte": fonte},
                               ensure_ascii=False) + "\n")
    print(titolo, "v2 domande:", len(QUESTIONS))

def pool_of(schede, field, nome):
    vals = []
    for d in schede:
        if d["nome"] != nome:
            vals.extend(clauses(d.get(field, "")))
    random.shuffle(vals)
    return vals

if __name__ == "__main__":
    gen("DESIGN_GUSTO_TENDENZE_PACK", "DESIGN_GUSTO", 200)
