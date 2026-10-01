# -*- coding: utf-8 -*-
"""Genera ESAMI/IMPIANTI_FV_EOLICO: domande a risposta multipla da DIMENSIONAMENTO_FV_EOLICO_ACCUMULO_PACK.

Parte A: modelli semantici sulle 10 schede didattiche (campi: descrizione, tecnologia,
applicazioni, vantaggi, limiti, costi, casi reali, normative, note cantiere).
Parte B: banco di calcoli parametrizzati (FV, stringhe, accumulo, eolico, solare termico,
pompa di calore, off-grid): parametri random, risposta calcolata, distrattori = errori tipici.

Domande in repository; risposte in ESAMI_RISPOSTE/IMPIANTI_FV_EOLICO_risposte.jsonl (fuori repo).
"""
import json, os, random, hashlib, math

random.seed(42)

ROOT = os.path.dirname(os.path.abspath(__file__))          # UNIVERSITA_EDILIZIA
WS = os.path.dirname(ROOT)                                  # workspace
SRC = os.path.join(ROOT, "DIMENSIONAMENTO_FV_EOLICO_ACCUMULO_PACK", "schede", "schede.jsonl")
OUT_Q = os.path.join(ROOT, "ESAMI", "IMPIANTI_FV_EOLICO", "domande.md")
OUT_R = os.path.join(WS, "ESAMI_RISPOSTE", "IMPIANTI_FV_EOLICO_risposte.jsonl")

schede = []
with open(SRC, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            schede.append(json.loads(line))
print("schede sorgente:", len(schede))

FIELDS = ["descrizione", "tecnologia", "applicazioni", "vantaggi", "limiti",
          "normative", "costi_e_economia", "casi_real_world", "note_cantiere"]
BY_FIELD = {fld: {} for fld in FIELDS}
for d in schede:
    for fld in FIELDS:
        v = (d.get(fld) or "").strip()
        if len(v) > 25:
            BY_FIELD[fld].setdefault(v, d["nome"])

cats = sorted(set(d["categoria"] for d in schede))
questions = []  # (testo, scelte, indice_corretta, spiegazione, fonte)
seen = set()

def key(q):
    return hashlib.md5(q.encode("utf-8")).hexdigest()

def add(testo, correct, distractors, spiegazione, fonte, min_distr=3):
    ds = []
    for x in distractors:
        x = (x or "").strip()
        if x and x != correct and x not in ds and len(x) > 2:
            ds.append(x)
        if len(ds) >= min_distr:
            break
    if len(ds) < min_distr or not correct:
        return False
    scelte = ds[:min_distr] + [correct]
    random.shuffle(scelte)
    questions.append((testo, scelte, scelte.index(correct), spiegazione, fonte))
    return True

def others(fld, nome, pool=None, n=12):
    src = pool or BY_FIELD[fld]
    vals = [v for v, owner in src.items() if owner != nome]
    random.shuffle(vals)
    return vals[:n]

# ---------------- PARTE A: modelli semantici sulle schede ----------------
for d in schede:
    nome, cat = d["nome"], d["categoria"]

    t = f"Quale di queste descrizioni corrisponde a «{nome}»?"
    if key(t + nome) not in seen:
        if add(t, d["descrizione"], others("descrizione", nome), d["descrizione"], nome):
            seen.add(key(t + nome))

    t = f"«{nome}» a quale area del dimensionamento impiantistico appartiene?"
    distr = [c for c in cats if c != cat]
    random.shuffle(distr)
    if key(t + nome) not in seen:
        scelte = distr[:3] + [cat]
        random.shuffle(scelte)
        questions.append((t, scelte, scelte.index(cat), f"Area corretta: {cat}", nome))
        seen.add(key(t + nome))

    for fld, richiesta in [
        ("tecnologia", "Quale affermazione su tecnologia e criteri d'uso di «{n}» è corretta?"),
        ("vantaggi", "Quale è un vantaggio distintivo di «{n}»?"),
        ("limiti", "Quale è un limite o un'attenzione tipica di «{n}»?"),
        ("normative", "Quale riferimento normativo o tecnico è associato a «{n}»?"),
        ("applicazioni", "In quale applicazione «{n}» è indicato o particolarmente usato?"),
        ("costi_e_economia", "Quale indicazione su costi ed economia è corretta per «{n}»?"),
        ("casi_real_world", "Quale caso reale è documentato per «{n}»?"),
        ("note_cantiere", "Quale nota di cantiere è associata a «{n}»?"),
    ]:
        v = (d.get(fld) or "").strip()
        if len(v) > 20:
            t = richiesta.format(n=nome)
            if key(t + nome + fld) not in seen:
                pool = others(fld, nome) + (others("limiti", nome) if fld == "vantaggi" else []) \
                                            + (others("vantaggi", nome) if fld == "limiti" else [])
                if add(t, v, pool, v, nome):
                    seen.add(key(t + nome + fld))

    t = f"Vero o falso: la seguente affermazione descrive correttamente «{nome}»: «{d['descrizione']}»"
    if key(t + nome) not in seen:
        questions.append((t, ["Vero", "Falso"], 0, f"Affermazione tratta dalla scheda: {d['descrizione']}", nome))
        seen.add(key(t + nome))

    alt = random.choice([x for x in schede if x["nome"] != nome])
    t = f"Vero o falso: «{nome}» si descrive così: «{alt['descrizione']}»"
    k = key(t + nome + alt["nome"])
    if k not in seen:
        questions.append((t, ["Vero", "Falso"], 1,
                          f"Falso: quella è la descrizione di «{alt['nome']}»; «{nome}»: {d['descrizione']}", nome))
        seen.add(k)

    t = f"Quale argomento/procedura corrisponde a questa descrizione: «{d['descrizione']}»?"
    alt_nomi = [x["nome"] for x in schede if x["nome"] != nome]
    random.shuffle(alt_nomi)
    if key(t + nome) not in seen and len(alt_nomi) >= 3:
        scelte = alt_nomi[:3] + [nome]
        random.shuffle(scelte)
        questions.append((t, scelte, scelte.index(nome), f"È «{nome}» ({d['categoria']})", nome))
        seen.add(key(t + nome))

print("parte A (semantiche):", len(questions))

# ---------------- PARTE B: banco di calcoli parametrizzati ----------------
N = 68  # varianti per generatore
fmt0 = lambda v: f"{v:,.0f}".replace(",", ".")                                     # 1.575
fmt1 = lambda v: f"{v:,.1f}".replace(",", "#").replace(".", ",").replace("#", ".")  # 3,5

ZONES = {"nord": (1150, 1450), "centro": (1250, 1550), "sud": (1350, 1650)}
ZONE_MID = {"nord": 1300, "centro": 1400, "sud": 1500}

def uniq_add(testo, scelte, idx, spieg, fonte):
    k = key(testo + "|" + "||".join(scelte))
    if k in seen:
        return False
    seen.add(k)
    questions.append((testo, scelte, idx, spieg, fonte))
    return True

def num_choices(correct, mistakes, fmt, unit):
    """4 opzioni numeriche: corretta + errori tipici, formattate, con unità di misura."""
    target = f"{fmt(correct)} {unit}"
    opts = {target}
    raw = list(mistakes)
    random.shuffle(raw)
    for m in raw:
        opts.add(f"{fmt(m)} {unit}")
        if len(opts) >= 4:
            break
    if len(opts) < 4:
        return None
    scelte = list(opts)
    random.shuffle(scelte)
    return scelte, scelte.index(target)

def emit(testo, correct, mistakes, fmt, unit, spieg, fonte):
    c = num_choices(correct, mistakes, fmt, unit)
    if not c:
        return
    scelte, idx = c
    uniq_add(testo, scelte, idx, spieg, fonte)

# B1: FV potenza da consumo  P = consumo × fattore / specifica
for _ in range(N):
    consumo = random.randrange(2000, 9001, 100)
    zona = random.choice(list(ZONES))
    spec = random.randrange(*ZONES[zona], 50)
    fatt = random.choice([0.5, 0.6, 0.7, 0.8])
    P = consumo * fatt / spec
    emit(f"Un edificio in zona {zona} (produzione specifica {fmt0(spec)} kWh/kWp) consuma {fmt0(consumo)} kWh/anno. "
         f"Dimensionando il fotovoltaico sull'autoconsumo con fattore {fatt}, qual è la potenza indicativa?",
         P, [consumo / spec, consumo * min(1.0, fatt + 0.2) / spec, consumo * fatt / (spec - 200)],
         fmt1, "kWp",
         f"P = {fmt0(consumo)} × {fatt} / {fmt0(spec)} ≈ {fmt1(P)} kWp",
         "Il dimensionamento del fotovoltaico: dal consumo ai kWp")

# B2: superficie tetto  m² = kWp × 5,5 (regola 5-6 m²/kWp)
for _ in range(N):
    kwp = random.randrange(20, 110, 5) / 10
    mq = kwp * 5.5
    emit(f"Un impianto fotovoltaico da {fmt1(kwp)} kWp richiede indicativamente quale superficie di tetto "
         f"(regola 5-6 m² per kWp)?",
         mq, [kwp * 4, kwp * 8, kwp * 10], fmt0, "m²",
         f"{fmt1(kwp)} × 5,5 ≈ {fmt0(mq)} m²", "Il dimensionamento del fotovoltaico: dal consumo ai kWp")

# B3: peso impianto  kg = m² × kg/m² (12-18)
for _ in range(N):
    mq = random.randrange(20, 140, 5)
    kg_m2 = random.randrange(12, 19)
    kg = mq * kg_m2
    emit(f"Un campo FV di {fmt0(mq)} m² con modulo da {kg_m2} kg/m² pesa complessivamente circa quanto?",
         kg, [mq * 25, mq * 8, mq * 30], fmt0, "kg",
         f"{fmt0(mq)} m² × {kg_m2} kg/m² = {fmt0(kg)} kg", "Il dimensionamento del fotovoltaico: dal consumo ai kWp")

# B4: produzione annua  E = kWp × specifica
for _ in range(N):
    kwp = random.randrange(20, 100, 5) / 10
    zona = random.choice(list(ZONES))
    spec = random.randrange(*ZONES[zona], 50)
    E = kwp * spec
    alt_zone = random.choice([z for z in ZONES if z != zona])
    emit(f"Un impianto da {fmt1(kwp)} kWp installato in zona {zona} (produzione specifica {fmt0(spec)} kWh/kWp) "
         f"produce indicativamente quanti kWh l'anno?",
         E, [kwp * ZONE_MID[alt_zone], kwp * (spec + 300), kwp * spec * 1.2], fmt0, "kWh/anno",
         f"{fmt1(kwp)} kWp × {fmt0(spec)} kWh/kWp ≈ {fmt0(E)} kWh/anno",
         "Il dimensionamento del fotovoltaico: dal consumo ai kWp")

# B5: energia autoconsumata  E_auto = produzione × quota
for _ in range(N):
    kwp = random.randrange(20, 80, 5) / 10
    spec = random.randrange(1250, 1600, 50)
    prod = kwp * spec
    quota = random.choice([0.2, 0.25, 0.3, 0.35, 0.4, 0.5])
    auto = prod * quota
    emit(f"Un impianto da {fmt1(kwp)} kWp (produzione {fmt0(prod)} kWh/anno) con quota di autoconsumo {int(quota*100)}% "
         f"immette in autoconsumo diretto quanta energia l'anno?",
         auto, [prod * (1 - quota), prod * min(0.9, quota + 0.15), prod], fmt0, "kWh/anno",
         f"{fmt0(prod)} × {quota} ≈ {fmt0(auto)} kWh/anno",
         "Il dimensionamento dell'accumulo in batteria: autoconsumo e backup")

# B6: immissione in rete  E_rete = produzione - autoconsumo
for _ in range(N):
    prod = random.randrange(3000, 9001, 100)
    quota = random.choice([0.3, 0.4, 0.5, 0.6])
    rete = prod * (1 - quota)
    emit(f"Un impianto produce {fmt0(prod)} kWh/anno e autoconsuma il {int(quota*100)}%. Quanta energia immette in rete?",
         rete, [prod * quota, prod * 0.9, prod * (1 - quota) * 1.25], fmt0, "kWh/anno",
         f"{fmt0(prod)} × (1 - {quota}) ≈ {fmt0(rete)} kWh/anno venduti/scambiati",
         "Esempio svolto: impianto FV 6 kWp con accumulo 5 kWh per una famiglia tipo")

# B7: tensione stringa  V = n × Vmpp
for _ in range(N):
    n = random.randrange(8, 17)
    vm = random.randrange(30, 41)
    V = n * vm
    emit(f"Una stringa fotovoltaica con {n} moduli da {vm} V di tensione di massima potenza (Vmpp) ha quale tensione di stringa?",
         V, [(n - 2) * vm, (n + 2) * vm, n * vm * 2], fmt0, "V",
         f"{n} × {vm} V = {fmt0(V)} V", "Il dimensionamento delle stringhe e degli inverter")

# B8: corrente AC trifase  I = P×1000 / (√3 × 400)
for _ in range(N):
    kw = random.randrange(3, 21)
    I = kw * 1000 / (math.sqrt(3) * 400)
    emit(f"Un inverter trifase da {kw} kW erogato su linea 400 V assorbe circa quale corrente di linea?",
         I, [kw * 1000 / 400, kw * 1000 / 230, I * 1.5], fmt1, "A",
         f"I = {fmt0(kw*1000)} / (1,732 × 400) ≈ {fmt1(I)} A", "Il cablaggio DC e AC del fotovoltaico: sezioni e protezioni")

# B9: batteria da fabbisogno  kWh = kWh/giorno × giorni / DoD
for _ in range(N):
    kwh_g = random.randrange(20, 90, 5) / 10
    gg = random.choice([1, 2, 3])
    dod = random.choice([0.8, 0.9])
    bat = kwh_g * gg / dod
    emit(f"Serve coprire {fmt1(kwh_g)} kWh/giorno per {gg} giorni con batteria a DoD {int(dod*100)}%. "
         f"Quale capacità nominale è necessaria?",
         bat, [kwh_g * gg, kwh_g * gg / 0.5, kwh_g * gg * dod], fmt1, "kWh",
         f"{fmt1(kwh_g)} × {gg} / {dod} ≈ {fmt1(bat)} kWh nominali",
         "Il dimensionamento dell'accumulo in batteria: autoconsumo e backup")

# B10: ore di autonomia backup  ore = kWh × DoD / kW
for _ in range(N):
    kwh = random.randrange(5, 21)
    kw = random.choice([1.0, 1.5, 2.0, 2.5, 3.0])
    dod = random.choice([0.8, 0.9])
    ore = kwh * dod / kw
    emit(f"Una batteria da {kwh} kWh (DoD {int(dod*100)}%) alimenta un carico essenziale da {fmt1(kw)} kW. "
         f"Quante ore di autonomia garantisce?",
         ore, [kwh / kw, kwh / kw / 0.5, kwh * dod / kw * 1.5], fmt1, "ore",
         f"{kwh} × {dod} / {fmt1(kw)} ≈ {fmt1(ore)} h",
         "Il dimensionamento dell'accumulo in batteria: autoconsumo e backup")

# B11: eolico produzione  E = kW × ore equivalenti
for _ in range(N):
    kw = random.choice([5, 10, 15, 20, 30, 50, 60])
    h = random.randrange(1200, 2300, 100)
    E = kw * h
    emit(f"Una piccola turbina eolica da {kw} kW in un sito con {fmt0(h)} ore equivalenti piene produce "
         f"indicativamente quanti kWh/anno?",
         E, [kw * (h + 500), kw * (h - 400), kw * h * 1.5], fmt0, "kWh/anno",
         f"{kw} kW × {fmt0(h)} h ≈ {fmt0(E)} kWh/anno (la realtà dipende fortemente dal sito)",
         "Il dimensionamento dell'eolico: la curva di potenza e la realtà dei siti")

# B12: solare termico ACS  collettori = ceil(persone/2), accumulo = persone × 60 l
for _ in range(N):
    pers = random.randrange(2, 7)
    coll = math.ceil(pers / 2)
    litri = pers * 60
    w = "collettore" if coll == 1 else "collettori"
    w1, w2, w3 = (("collettore" if coll + 1 == 1 else "collettori"),
                  ("collettore" if max(1, coll - 1) == 1 else "collettori"),
                  ("collettore" if coll == 1 else "collettori"))
    target = f"{coll} {w} / {fmt0(litri)} l"
    opts = {target, f"{coll+1} {w1} / {fmt0(litri+100)} l",
            f"{max(1,coll-1)} {w2} / {fmt0(litri-50)} l", f"{coll} {w3} / {fmt0(pers*40)} l"}
    if len(opts) == 4:
        scelte = list(opts)
        random.shuffle(scelte)
        uniq_add(f"Per l'acqua calda sanitaria di {pers} persone (regola: 1 collettore da ~2 m² ogni 2 persone, "
                 f"50-75 l di accumulo a persona), qual è il dimensionamento indicativo?",
                 scelte, scelte.index(target),
                 f"{coll} collettori e {fmt0(litri)} l di accumulo", "Il dimensionamento del solare termico: collettori e accumulo")

# B13: pompa di calore  E_elettrica = Q_termica / COP
for _ in range(N):
    q = random.randrange(4000, 20001, 500)
    cop = random.choice([2.5, 3.0, 3.2, 3.5, 3.8, 4.0, 4.5])
    ee = q / cop
    emit(f"Una pompa di calore con COP {cop} deve coprire un fabbisogno termico di {fmt0(q)} kWh/anno. "
         f"Quanta energia elettrica assorbe indicativamente?",
         ee, [q * cop, q / 2, q * 1.2 / cop], fmt0, "kWh/anno",
         f"{fmt0(q)} / {cop} ≈ {fmt0(ee)} kWh elettrici/anno",
         "Il dimensionamento della pompa di calore: il metodo binario completo")

# B14: off-grid batteria  kWh = consumo × giorni / DoD
for _ in range(N):
    kwh_g = random.randrange(50, 160, 5) / 10
    gg = random.choice([2, 3, 4])
    bat = kwh_g * gg / 0.8
    emit(f"Un sistema off-grid con consumo di {fmt1(kwh_g)} kWh/giorno e {gg} giorni di autonomia richiede "
         f"quale banco batterie (DoD 80%)?",
         bat, [kwh_g * gg, kwh_g * gg * 0.8, kwh_g * gg / 0.5], fmt1, "kWh",
         f"{fmt1(kwh_g)} × {gg} / 0,8 ≈ {fmt1(bat)} kWh", "Il dimensionamento off-grid: l'autonomia totale senza rete")

# B15: off-grid sovradimensionamento FV  kWp = consumo × 1,3 / specifica
for _ in range(N):
    kwh_g = random.randrange(50, 160, 5) / 10
    zona = random.choice(list(ZONES))
    spec = ZONE_MID[zona]
    annuo = kwh_g * 365
    kwp = annuo * 1.3 / spec
    emit(f"In un sistema off-grid in zona {zona}, con consumo di {fmt1(kwh_g)} kWh/giorno, qual è la potenza FV "
         f"indicativa sovradimensionata del 30%?",
         kwp, [annuo / spec, annuo * 1.3 / (spec + 200), annuo * 1.6 / spec], fmt1, "kWp",
         f"{fmt1(kwh_g)} × 365 = {fmt0(annuo)} kWh/anno; × 1,3 / {fmt0(spec)} ≈ {fmt1(kwp)} kWp",
         "Il dimensionamento off-grid: l'autonomia totale senza rete")

# B16: performance ratio  E_reale = kWp × h × PR
for _ in range(N):
    kwp = random.randrange(30, 90, 5) / 10
    h = random.randrange(1300, 1700, 50)
    pr = random.choice([0.75, 0.8, 0.85])
    reale = kwp * h * pr
    emit(f"Un impianto da {fmt1(kwp)} kWp con {fmt0(h)} ore equivalenti e performance ratio {pr} produce "
         f"realmente quanti kWh/anno?",
         reale, [kwp * h, kwp * h * 0.6, kwp * h * 1.1], fmt0, "kWh/anno",
         f"{fmt1(kwp)} × {fmt0(h)} × {pr} ≈ {fmt0(reale)} kWh/anno",
         "Il dimensionamento del fotovoltaico: dal consumo ai kWp")

# B17: V/F su regole di dimensionamento
VF_POOL = [
    ("Il fotovoltaico si dimensiona sul consumo, non sul tetto disponibile", True,
     "Regola fondamentale: il tetto è un vincolo, il punto di partenza è la bolletta."),
    ("Regola pratica: servono circa 5-6 m² di tetto per ogni kWp installato", True,
     "1 kWp ≈ 5-6 m² di superficie occupata."),
    ("Un impianto fotovoltaico pesa tipicamente 40-60 kg/m²", False,
     "Il peso tipico è 12-18 kg/m²: quasi sempre il tetto regge senza rinforzi."),
    ("In Italia la produzione specifica annua è circa 1.200-1.700 kWh per kWp a seconda della zona", True,
     "Nord 1.150-1.450, centro 1.250-1.550, sud 1.350-1.650 kWh/kWp."),
    ("La produzione reale di un impianto FV può variare del ±15% rispetto alle stime a causa del meteo", True,
     "Per questo i contratti devono parlare di stime, non di promesse."),
    ("In una stringa FV i moduli si collegano in parallelo per sommare le tensioni", False,
     "In serie si sommano le tensioni; in parallelo si sommano le correnti."),
    ("Una batteria al litio si può scaricare tipicamente fino all'80-90% (DoD)", True,
     "Il DoD 80-90% è tipico del litio; al piombo si ferma intorno al 50%."),
    ("Il dimensionamento dell'eolico può basarsi solo sulla potenza nominale della turbina", False,
     "Serve la curva di potenza e i dati del vento del sito: la nominale da sola non basta."),
    ("Per il solare termico la regola è circa 1 collettore da 2 m² ogni 2 persone", True,
     "Con 50-75 litri di accumulo a persona."),
    ("Una pompa di calore con COP 3 assorbe un terzo dell'energia termica che eroga", True,
     "E_elettrica = Q / COP: COP 3 → un terzo dell'energia elettrica rispetto al calore."),
    ("In un sistema off-grid conviene sovradimensionare il campo FV del 20-30% rispetto al dimensionamento su rete", True,
     "Per coprire giornate povere di irraggiamento e ricaricare le batterie."),
    ("Il performance ratio (PR) tipico di un impianto FV ben progettato è intorno a 0,75-0,85", True,
     "PR = energia reale / energia teorica: ombre, temperature, perdite di conversione."),
    ("Il fotovoltaico si dimensiona partendo dalla superficie del tetto disponibile", False,
     "È l'errore classico: si parte dal consumo in bolletta, il tetto è il vincolo."),
    ("Il dimensionamento dell'accumulo si fa solo sulla potenza nominale della batteria", False,
     "Conta l'energia utile: kWh × DoD, non la nominale."),
    ("In una stringa FV i moduli in serie sommano le correnti e mantengono la tensione", False,
     "In serie si sommano le tensioni; le correnti si sommano in parallelo."),
]
for testo, corretto, spieg in VF_POOL:
    t = f"Vero o falso: {testo}."
    if key(t) not in seen:
        seen.add(key(t))
        questions.append((t, ["Vero", "Falso"], 0 if corretto else 1, spieg, "Regole di dimensionamento impianti"))

print("parte A+B totale:", len(questions))

random.shuffle(questions)
TARGET = 1000
if len(questions) > TARGET:
    questions = questions[:TARGET]

os.makedirs(os.path.dirname(OUT_Q), exist_ok=True)
os.makedirs(os.path.dirname(OUT_R), exist_ok=True)

LETTERS = "ABCD"
with open(OUT_Q, "w", encoding="utf-8") as fq, open(OUT_R, "w", encoding="utf-8") as fr:
    fq.write(f"# ESAME — Settore IMPIANTI FV / EOLICO / ACCUMULO ({len(questions)} domande)\n\n")
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
