# -*- coding: utf-8 -*-
"""Genera ESAMI/ASCENSORI (300) ed ESAMI/FOTOVOLTAICO_CER (400).

Risposte in ESAMI_RISPOSTE/ (fuori repo).
Distrattori = frasi di schede DELLO STESSO pack: errori plausibili dello stesso settore.
"""
import json, os, random, hashlib, io, re

ROOT = os.path.dirname(os.path.abspath(__file__))   # UNIVERSITA_EDILIZIA
WS = os.path.dirname(ROOT)

random.seed(41)

def clauses(text):
    out = []
    for c in re.split(r'[;.]\s*', text or ''):
        c = c.strip(' ;.')
        if len(c) > 15:
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

def add(testo, correct, distractors, spiegazione, fonte, min_d=3):
    ds = []
    for x in distractors:
        x = (x or "").strip()
        if x and x != correct and x not in ds:
            ds.append(x)
        if len(ds) >= min_d:
            break
    if len(ds) < min_d:
        return False
    scelte = ds[:min_d] + [correct]
    random.shuffle(scelte)
    QUESTIONS.append((testo, scelte, scelte.index(correct), spiegazione, fonte))
    return True

def pool_of(schede, field, nome):
    vals = []
    for d in schede:
        if d["nome"] != nome:
            vals.extend(clauses(d.get(field, "")))
    random.shuffle(vals)
    return vals

def gen(pack, titolo, target):
    global QUESTIONS
    QUESTIONS = []
    schede = load(pack)
    ST1 = ["Per «{n}», quale di questi elementi appartiene alla tecnologia descritta nella scheda?",
           "Nella scheda «{n}» la tecnologia comprende anche:",
           "Quale di questi componenti/processi è descritto nella scheda «{n}»?",
           "Secondo la scheda «{n}», quale elemento fa parte della tecnologia dell'argomento trattato?"]
    ST2 = ["Quale accorgimento è nelle note di cantiere della scheda «{n}»?",
           "Per lavorare correttamente su «{n}», cosa raccomandano le note di cantiere?",
           "Quale di questi errori di cantiere è segnalato nella scheda «{n}»?",
           "Una nota di cantiere della scheda «{n}» recita:"]
    ST3 = ["Quale di questi è un vantaggio documentato di «{n}»?",
           "Tra questi, quale vantaggio è attribuito a «{n}» dalla scheda?",
           "Perché «{n}» conviene secondo la scheda? Scegli il vantaggio corretto:",
           "Quale affermazione sui vantaggi di «{n}» è quella documentata nella scheda?"]
    ST4 = ["Quale di questi è un limite o svantaggio documentato di «{n}»?",
           "Tra questi, quale limite è dichiarato nella scheda «{n}»?",
           "Qual è il punto debole di «{n}» secondo la scheda?",
           "Quale affermazione sui limiti di «{n}» è quella corretta?"]
    ST5 = ["Quali sono le applicazioni tipiche di «{n}» secondo la scheda?",
           "La scheda «{n}» indica quali ambiti di applicazione?",
           "Dove si applica l'argomento della scheda «{n}»?"]
    STC = ["Quale dato economico o di costo è citato nella scheda «{n}»?",
           "Secondo la scheda «{n}», quale indicazione di costo è corretta?",
           "Quale ordine di grandezza economico è riportato per «{n}»?"]
    STN = ["Quale riferimento normativo è citato nella scheda «{n}»?",
           "Secondo la scheda «{n}», a quali riferimenti normativi fare riferimento?",
           "Il quadro normativo di «{n}» comprende anche:"]
    STNOT = ["Per la scheda «{n}», quale di questi elementi NON è citato tra la sua tecnologia?",
             "Quale di questi NON appartiene alla tecnologia descritta nella scheda «{n}»?"]
    seen = set()
    for d in schede:
        nome = d["nome"]
        tech = clauses(d["tecnologia"])
        # T-NOT: tecnologia della scheda come distrattori, corretta da altra scheda
        for i, alt in enumerate(pool_of(schede, "tecnologia", nome)):
            if len(QUESTIONS) >= target: break
            if not tech: break
            distr = random.sample(tech, min(3, len(tech)))
            if alt in distr or len(set(distr)) < 3: continue
            add(STNOT[i % len(STNOT)].format(n=nome), alt, distr,
                f"Gli altri tre elementi sono citati nella tecnologia della scheda «{nome}»; questo no.",
                f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        for i, c in enumerate(tech):
            if len(QUESTIONS) >= target: break
            key = (nome, c)
            if key in seen: continue
            seen.add(key)
            add(ST1[i % len(ST1)].format(n=nome),
                c, pool_of(schede, "tecnologia", nome),
                f"È un elemento tecnologico della scheda «{nome}». Le altre opzioni appartengono ad altre schede dello stesso settore.",
                f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        for i, c in enumerate(clauses(d.get("note_cantiere", ""))):
            if len(QUESTIONS) >= target: break
            key = (nome, c)
            if key in seen: continue
            seen.add(key)
            add(ST2[i % len(ST2)].format(n=nome),
                c, pool_of(schede, "note_cantiere", nome),
                f"È una nota di cantiere della scheda «{nome}»; le altre opzioni sono note di cantiere di schede diverse dello stesso settore.",
                f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        for i, c in enumerate(clauses(d["vantaggi"])):
            if len(QUESTIONS) >= target: break
            key = (nome, c)
            if key in seen: continue
            seen.add(key)
            dist = clauses(d["limiti"]) + pool_of(schede, "limiti", nome)
            add(ST3[i % len(ST3)].format(n=nome),
                c, dist,
                f"È un vantaggio della scheda «{nome}»; gli altri sono limiti o svantaggi, spesso della stessa scheda: l'errore tipico è scambiare un limite per un vantaggio.",
                f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        for i, c in enumerate(clauses(d["limiti"])):
            if len(QUESTIONS) >= target: break
            key = (nome, c)
            if key in seen: continue
            seen.add(key)
            dist = clauses(d["vantaggi"]) + pool_of(schede, "vantaggi", nome)
            add(ST4[i % len(ST4)].format(n=nome),
                c, dist,
                f"È un limite della scheda «{nome}»; gli altri sono vantaggi: l'errore tipico è sottovalutare un limite dichiarato.",
                f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        for i, c in enumerate(clauses(d.get("applicazioni", ""))):
            if len(QUESTIONS) >= target: break
            key = (nome, "app", c)
            if key in seen: continue
            seen.add(key)
            add(ST5[i % len(ST5)].format(n=nome),
                c, pool_of(schede, "applicazioni", nome) + pool_of(schede, "tecnologia", nome),
                f"È un campo di applicazione della scheda «{nome}»; le altre opzioni appartengono ad altre schede dello stesso settore.",
                f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        for i, c in enumerate(clauses(d.get("costi_e_economia", ""))):
            if len(QUESTIONS) >= target: break
            key = (nome, "costi", c)
            if key in seen: continue
            seen.add(key)
            add(STC[i % len(STC)].format(n=nome),
                c, pool_of(schede, "costi_e_economia", nome),
                f"È un dato economico della scheda «{nome}»; le altre opzioni sono dati economici di schede diverse dello stesso settore.",
                f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        for i, c in enumerate(clauses(d.get("normative", ""))):
            if len(QUESTIONS) >= target: break
            key = (nome, "norme", c)
            if key in seen: continue
            seen.add(key)
            add(STN[i % len(STN)].format(n=nome),
                c, pool_of(schede, "normative", nome),
                f"È un riferimento normativo della scheda «{nome}»; le altre opzioni sono riferimenti di schede diverse dello stesso settore.",
                f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break

    # T5/T6/T7: campi interi (una tantum per scheda)
    for d in schede:
        nome = d["nome"]
        if len(QUESTIONS) >= target: break
        add(f"Quale riassunto corrisponde alla scheda «{nome}»?",
            d["descrizione"], [x["descrizione"] for x in schede if x["nome"] != nome],
            f"È la descrizione della scheda «{nome}».", f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        add(f"Qual è il caso reale (casi real world) descritto nella scheda «{nome}»?",
            d["casi_real_world"], [x["casi_real_world"] for x in schede if x["nome"] != nome],
            f"È il caso reale della scheda «{nome}».", f"{pack} / {nome}")
        if len(QUESTIONS) >= target: break
        add(f"Quale quadro normativo è citato nella scheda «{nome}»?",
            d["normative"], [x["normative"] for x in schede if x["nome"] != nome],
            f"È il quadro normativo della scheda «{nome}».", f"{pack} / {nome}")
    # dedup su (testo, risposta): stesso stelo può ripetersi con opzioni diverse
    uniq = {}
    for q in QUESTIONS:
        uniq.setdefault((q[0], q[1][q[2]]), q)
    QUESTIONS = list(uniq.values())
    random.shuffle(QUESTIONS)
    QUESTIONS = QUESTIONS[:target]

    outdir = os.path.join(ROOT, "ESAMI", titolo)
    os.makedirs(outdir, exist_ok=True)
    lines = [f"# ESAME — {titolo.replace('_', ' ')} ({len(QUESTIONS)} domande)\n",
             "Risposte NON presenti: il file chiave è riservato (fuori repository).",
             "Le opzioni sbagliate sono errori tipici di uno specialista del settore, pertinenti alla materia della domanda.\n"]
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
    print(titolo, "domande:", len(QUESTIONS), "->", outdir)

gen("ASCENSORI_E_MOVIMENTAZIONE_VERTICALE_PACK", "ASCENSORI", 300)
gen("FOTOVOLTAICO_CAMPI_AGRIVOLTAICO_CER_PACK", "FOTOVOLTAICO_CER", 400)
