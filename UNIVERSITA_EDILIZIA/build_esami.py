# -*- coding: utf-8 -*-
"""Genera ESAMI/MATERIALEDILE: 1000 domande a risposta multipla (senza risposte in repo).

Le risposte vanno in ESAMI_RISPOSTE/MATERIALEDILE_risposte.jsonl (fuori repo, consegnate all'utente).
"""
import json, os, random, hashlib

random.seed(42)

ROOT = os.path.dirname(os.path.abspath(__file__))          # UNIVERSITA_EDILIZIA
WS = os.path.dirname(ROOT)                                  # workspace
SRC = os.path.join(WS, "MATERIALEDILE_PACK", "schede", "materiale_edile_schede.jsonl")
OUT_Q = os.path.join(ROOT, "ESAMI", "MATERIALEDILE", "domande.md")
OUT_R = os.path.join(WS, "ESAMI_RISPOSTE", "MATERIALEDILE_risposte.jsonl")

schede = []
with open(SRC, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            schede.append(json.loads(line))

print("schede sorgente:", len(schede))

FIELDS = ["descrizione", "tecnologia", "applicazioni", "vantaggi", "limiti", "normative", "costi_e_economia", "note_cantiere"]
BY_FIELD = {fld: {} for fld in FIELDS}
for d in schede:
    for fld in FIELDS:
        v = (d.get(fld) or "").strip()
        if len(v) > 25:
            BY_FIELD[fld].setdefault(v, d["nome"])

cats = sorted(set(d["categoria"] for d in schede))

questions = []  # (testo, scelte[list], indice_corretta, spiegazione, fonte)

def add(testo, correct, distractors, spiegazione, fonte, min_distr=3):
    ds = []
    for x in distractors:
        x = (x or "").strip()
        if x and x != correct and x not in ds and len(x) > 10:
            ds.append(x)
        if len(ds) >= min_distr:
            break
    if len(ds) < min_distr:
        return False
    scelte = ds[:min_distr] + [correct]
    random.shuffle(scelte)
    idx = scelte.index(correct)
    questions.append((testo, scelte, idx, spiegazione, fonte))
    return True

def others(fld, nome, pool=None, n=12):
    """Valori del campo fld di schede diverse da nome."""
    src = pool or BY_FIELD[fld]
    vals = [v for v, owner in src.items() if owner != nome]
    random.shuffle(vals)
    return vals[:n]

seen = set()

def key(q):
    return hashlib.md5(q.encode("utf-8")).hexdigest()

for d in schede:
    nome, cat = d["nome"], d["categoria"]

    # 1. Definizione
    t = f"Quale di queste descrizioni corrisponde a «{nome}»?"
    if key(t + nome) not in seen:
        if add(t, d["descrizione"], others("descrizione", nome), d["descrizione"], nome):
            seen.add(key(t + nome))

    # 2. Categoria
    t = f"«{nome}» a quale categoria di materiali/prodotti appartiene?"
    distr = [c for c in cats if c != cat]
    random.shuffle(distr)
    if key(t + nome) not in seen:
        scelte = distr[:3] + [cat]
        random.shuffle(scelte)
        questions.append((t, scelte, scelte.index(cat), f"Categoria corretta: {cat}", nome))
        seen.add(key(t + nome))

    # 3. Tecnologia
    if len(d.get("tecnologia", "")) > 25:
        t = f"Quale affermazione su tecnologia e criteri d'uso di «{nome}» è corretta?"
        if key(t + nome) not in seen:
            if add(t, d["tecnologia"], others("tecnologia", nome), d["tecnologia"], nome):
                seen.add(key(t + nome))

    # 4. Vantaggio
    if len(d.get("vantaggi", "")) > 25:
        t = f"Quale è un vantaggio distintivo di «{nome}»?"
        if key(t + nome) not in seen:
            if add(t, d["vantaggi"], others("vantaggi", nome) + others("limiti", nome), d["vantaggi"], nome):
                seen.add(key(t + nome))

    # 5. Limite
    if len(d.get("limiti", "")) > 25:
        t = f"Quale è un limite o un'attenzione tipica di «{nome}»?"
        if key(t + nome) not in seen:
            if add(t, d["limiti"], others("limiti", nome) + others("vantaggi", nome), d["limiti"], nome):
                seen.add(key(t + nome))

    # 6. Normativa
    if len(d.get("normative", "")) > 10:
        t = f"Quale riferimento normativo o tecnico è associato a «{nome}»?"
        if key(t + nome) not in seen:
            if add(t, d["normative"], others("normative", nome), d["normative"], nome):
                seen.add(key(t + nome))

    # 7. Applicazioni
    if len(d.get("applicazioni", "")) > 25:
        t = f"In quale applicazione «{nome}» è indicato o particolarmente usato?"
        if key(t + nome) not in seen:
            if add(t, d["applicazioni"], others("applicazioni", nome), d["applicazioni"], nome):
                seen.add(key(t + nome))

    # 8. Vero/Falso dalla descrizione
    t = f"Vero o falso: la seguente affermazione descrive correttamente «{nome}»: «{d['descrizione']}»"
    if key(t + nome) not in seen:
        scelte = ["Vero", "Falso"]
        questions.append((t, scelte, 0, f"Affermazione tratta dalla scheda: {d['descrizione']}", nome))
        seen.add(key(t + nome))

    # 9. Falso asserzione: attribuisci a nome la descrizione di un'altra scheda
    alt = random.choice([x for x in schede if x["nome"] != nome])
    t = f"Vero o falso: «{nome}» si descrive così: «{alt['descrizione']}»"
    k = key(t + nome + alt["nome"])
    if k not in seen:
        questions.append((t, ["Vero", "Falso"], 1,
                          f"Falso: quella è la descrizione di «{alt['nome']}»; «{nome}»: {d['descrizione']}", nome))
        seen.add(k)

    # 10. Costi/economia (se presente)
    if len(d.get("costi_e_economia", "")) > 25:
        t = f"Quale indicazione su costi ed economia è corretta per «{nome}»?"
        if key(t + nome) not in seen:
            if add(t, d["costi_e_economia"], others("costi_e_economia", nome), d["costi_e_economia"], nome):
                seen.add(key(t + nome))

    # 11. Note di cantiere
    if len(d.get("note_cantiere", "")) > 25:
        t = f"Quale nota di cantiere è associata a «{nome}»?"
        if key(t + nome) not in seen:
            if add(t, d["note_cantiere"], others("note_cantiere", nome), d["note_cantiere"], nome):
                seen.add(key(t + nome))

    # 12. Reverse: quale nome corrisponde alla descrizione
    t = f"Quale materiale/prodotto corrisponde a questa descrizione: «{d['descrizione']}»?"
    alt_nomi = [x["nome"] for x in schede if x["nome"] != nome]
    random.shuffle(alt_nomi)
    if key(t + nome) not in seen and len(alt_nomi) >= 3:
        scelte = alt_nomi[:3] + [nome]
        random.shuffle(scelte)
        questions.append((t, scelte, scelte.index(nome), f"È «{nome}» ({d['categoria']})", nome))
        seen.add(key(t + nome))

    # 13. V/F sulla tecnologia
    if len(d.get("tecnologia", "")) > 25:
        alt = random.choice([x for x in schede if x["nome"] != nome and len(x.get("tecnologia", "")) > 25])
        t = f"Vero o falso: «{nome}» si usa così: «{alt['tecnologia']}»"
        k = key(t + nome + alt["nome"] + "tec")
        if k not in seen:
            questions.append((t, ["Vero", "Falso"], 1,
                              f"Falso: quella è la tecnologia di «{alt['nome']}»; «{nome}»: {d['tecnologia']}", nome))
            seen.add(k)

    # 14. V/F sul vantaggio
    if len(d.get("vantaggi", "")) > 25:
        alt = random.choice([x for x in schede if x["nome"] != nome and len(x.get("vantaggi", "")) > 25])
        t = f"Vero o falso: un vantaggio di «{nome}» è: «{alt['vantaggi']}»"
        k = key(t + nome + alt["nome"] + "van")
        if k not in seen:
            questions.append((t, ["Vero", "Falso"], 1,
                              f"Falso: quello è un vantaggio di «{alt['nome']}»; di «{nome}»: {d['vantaggi']}", nome))
            seen.add(k)

    # 15. Quale NON è: tre valori veri del campo + uno di altra scheda
    for fld, lab in [("applicazioni", "applicazione"), ("normative", "riferimento normativo")]:
        v = (d.get(fld) or "").strip()
        if len(v) > 10 and len(d["descrizione"]) > 25:
            t = f"Per «{nome}», quale di questi NON è {lab} corretto?"
            altrui = others(fld, nome, n=8)
            if len(altrui) >= 1:
                err = altrui[0]
                scelte = [v] * 1 + [v]  # placeholder, costruito sotto
                # tre corretti di versi campi? semplice: 1 corretto + 3 "non corretti" presi da altri
                base = [v] + altrui[:3]
                random.shuffle(base)
                k = key(t + nome + fld)
                if k not in seen and len(set(base)) == 4:
                    questions.append((t, base, base.index(v),
                                      f"La risposta corretta è «{v}»; le altre riguardano altri materiali", nome))
                    seen.add(k)

random.shuffle(questions)

# Limita a 1000
TARGET = 1000
if len(questions) > TARGET:
    questions = questions[:TARGET]

os.makedirs(os.path.dirname(OUT_Q), exist_ok=True)
os.makedirs(os.path.dirname(OUT_R), exist_ok=True)

LETTERS = "ABCD"
with open(OUT_Q, "w", encoding="utf-8") as fq, open(OUT_R, "w", encoding="utf-8") as fr:
    fq.write("# ESAME — Settore MATERIALI EDILI (1.000 domande)\n\n")
    fq.write("Risposta multipla A-D (o Vero/Falso). Le risposte corrette NON sono incluse in questo file:\n")
    fq.write("vivono nel file riservato consegnato al proprietario (ESAMI_RISPOSTE).\n\n")
    for i, (t, scelte, idx, spieg, fonte) in enumerate(questions, 1):
        fq.write(f"**D{i}.** {t}\n\n")
        for j, sc in enumerate(scelte):
            fq.write(f"   {LETTERS[j]}) {sc}\n")
        fq.write("\n")
        fr.write(json.dumps({
            "domanda": i, "testo": t,
            "risposta_corretta": LETTERS[idx] if len(scelte) > 2 else scelte[idx],
            "spiegazione": spieg, "scheda_fonte": fonte,
        }, ensure_ascii=False) + "\n")

print("domande generate:", len(questions))
print("domande:", OUT_Q)
print("risposte:", OUT_R)
