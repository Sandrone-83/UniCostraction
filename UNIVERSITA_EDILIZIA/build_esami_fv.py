# -*- coding: utf-8 -*-
"""Genera ESAMI/IMPIANTI_FV_EOLICO: domande a risposta multipla da DIMENSIONAMENTO_FV_EOLICO_ACCUMULO_PACK.

CRITERIO QUALITÀ (richiesto dal proprietario): ogni risposta sbagliata deve
1) appartenere alla STESSA materia della domanda, 2) essere l'errore che farebbe
davvero un tecnico sul campo.

Parte A: modelli semantici sulle 10 schede. I distrattori NON sono più contenuti
di altre schede: sono ERRORI TIPOICI curati per ciascun argomento (banche sotto).
Parte B: banco di calcoli parametrizzati (FV, stringhe, accumulo, eolico, solare termico,
pompa di calore, off-grid): parametri random, risposta calcolata, distrattori = errori
di calcolo reali (fattore dimenticato, DoD sbagliato, zona sbagliata, √3 dimenticato).

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

# ---------------------------------------------------------------------------
# BANCHE DI ERRORI TIPOICI (stessa materia della scheda, errori da tecnico vero)
# ---------------------------------------------------------------------------
ERROR_BANK = {
    "Il dimensionamento del fotovoltaico: dal consumo ai kWp": [
        "Si parte dalla superficie del tetto riempiendola tutta di pannelli: il consumo in bolletta non serve",
        "La produzione specifica in Italia è identica ovunque, circa 1.000 kWh/kWp",
        "1 kWp occupa indicativamente 2-3 m² di tetto",
        "Un impianto FV pesa in genere oltre 50 kg/m² e richiede quasi sempre il rinforzo del tetto",
        "La potenza si ottiene dividendo il consumo annuo per la produzione specifica, senza nessun fattore di autoconsumo",
        "Il primo dato da raccogliere è l'orientamento del tetto, la bolletta arriva dopo",
        "In montagna (zona nord) la produzione specifica supera sempre i 1.700 kWh/kWp",
        "La verifica dei carichi sul tetto è superflua perché i pannelli sono leggeri",
    ],
    "Il dimensionamento delle stringhe e degli inverter": [
        "I moduli in serie sommano le correnti e mantengono invariata la tensione",
        "La tensione di stringa si calcola sommando le correnti dei singoli moduli",
        "L'inverter si sceglie solo in base ai kWp del campo, senza verificare l'intervallo MPPT",
        "Inserire più moduli in serie di quanto consenta l'MPPT aumenta la resa senza alcun rischio",
        "La tensione a vuoto (Voc) non ha rilevanza nel dimensionamento della stringa",
        "Le stringhe in parallelo devono avere tensioni diverse tra loro per funzionare",
        "L'inverter va dimensionato sempre pari ai kWp del campo: il sovradimensionamento è sempre un errore",
        "In caso di ombra parziale conviene allungare la stringa ombreggiata per recuperare potenza",
    ],
    "Il cablaggio DC e AC del fotovoltaico: sezioni e protezioni": [
        "In corrente continua si possono usare sezioni più piccole che in AC a parità di potenza",
        "Le protezioni DC si scelgono come quelle AC, senza interruttori specifici per corrente continua",
        "Il cavo DC non necessita di polarità marcata né di guaina dimensionata per la tensione",
        "La caduta di tensione sul lato DC è irrilevante e non va mai verificata",
        "In DC l'arco elettrico si estingue da solo più facilmente che in AC",
        "La corrente di linea di un inverter trifase si calcola dividendo la potenza per 230 V",
        "Le protezioni AC vanno scelte con corrente nominale pari alla corrente di cortocircuito",
        "I connettori DC di marca diversa si possono accoppiare liberamente se 'quasi uguali'",
    ],
    "Il dimensionamento dell'accumulo in batteria: autoconsumo e backup": [
        "La batteria si dimensiona sulla potenza nominale in kW, l'energia in kWh non conta",
        "Una batteria al litio va scaricata fino allo 0% per sfruttarla al massimo",
        "Il DoD utile del litio è paragonabile a quello del piombo-acido, circa 50%",
        "Con la batteria tutta la produzione FV viene autoconsumata anche di giorno, senza strategie",
        "L'autonomia in backup si calcola sui kWh nominali, senza applicare il DoD",
        "Una batteria da 10 kWh con carico da 2 kW garantisce 5 ore di autonomia",
        "Qualsiasi batteria si può abbinare a qualsiasi inverter senza verifiche di compatibilità",
        "La batteria aumenta la produzione dell'impianto FV, non solo lo sfruttamento dell'energia",
    ],
    "Il dimensionamento dell'eolico: la curva di potenza e la realtà dei siti": [
        "La potenza nominale della turbina da sola basta per stimare la produzione annua",
        "L'eolico in Italia rende come in Nord Europa con la stessa turbina",
        "La velocità del vento cresce in modo lineare con l'altezza dal suolo",
        "La curva di potenza è identica per tutte le turbine dello stesso diametro",
        "Un sito con vento medio di 4 m/s rende come uno a 7 m/s",
        "L'eolico residenziale urbano rende quasi sempre quanto dichiarato dal venditore",
        "La produzione eolica annua si stima come kW nominali × 8.760 ore",
    ],
    "I sistemi ibridi FV + batteria + rete + generatore: il dimensionamento integrato": [
        "Nell'ibrido il generatore di backup si può eliminare sempre, in ogni condizione",
        "L'inverter ibrido gestisce solo il fotovoltaico, le batterie servono un secondo inverter",
        "In caso di black-out l'impianto ibrido con batteria lascia comunque tutta la casa al buio",
        "Il generatore di backup si dimensiona sulla potenza di picco del campo FV",
        "L'ibrido con batteria non ha bisogno di nessuna logica di priorità tra le sorgenti",
    ],
    "Il dimensionamento off-grid: l'autonomia totale senza rete": [
        "L'off-grid si dimensiona con gli stessi calcoli di un impianto su rete",
        "Il sovradimensionamento del campo FV in off-grid è inutile e spreca denaro",
        "I giorni di autonomia si scelgo a caso, non servono le statistiche meteo locali",
        "In off-grid la batteria si dimensiona senza considerare il DoD",
        "Per l'off-grid basta il consumo annuo, il profilo giornaliero e stagionale non serve",
        "Un impianto off-grid senza generatore di emergenza è sempre la scelta migliore",
    ],
    "Il dimensionamento della pompa di calore: il metodo binario completo": [
        "La pompa di calore si dimensiona sulla potenza di picco invernale, esattamente come una caldaia a gas",
        "Con COP 3 la pompa di calore consuma il triplo dell'energia che eroga",
        "La COP è costante a qualsiasi temperatura esterna",
        "La pompa di calore aria-acqua non funziona sotto lo zero",
        "Il metodo binario confronta solo i prezzi di acquisto, non i consumi",
        "Una pompa di calore sovradimensionata lavora sempre meglio a bassa velocità",
        "L'unità esterna della pompa di calore non produce rumore rilevante per i vicini",
    ],
    "Il dimensionamento del solare termico: collettori e accumulo": [
        "Il numero di collettori non dipende dal numero di persone da servire",
        "L'accumulo si dimensiona in litri pari ai kWh del consumo annuo",
        "In inverno il solare termico copre sempre il 100% dell'acqua calda sanitaria",
        "Un impianto a circolazione forzata non ha bisogno né di circolatore né di elettricità",
        "Se c'è già il fotovoltaico il solare termico è inutile, punto",
        "L'orientamento e l'inclinazione dei collettori sono irrilevanti per la resa",
    ],
    "Esempio svolto: impianto FV 6 kWp con accumulo 5 kWh per una famiglia tipo": [
        "Per una famiglia da 2.700 kWh/anno servono almeno 8-10 kWp",
        "Con 6 kWp e consumo di 2.700 kWh l'autoconsumo senza batteria supera il 90%",
        "La batteria da 5 kWh azzera sempre la bolletta elettrica",
        "I 6 kWp richiedono più di 60 m² di tetto",
        "Il payback di un impianto così è garantito sotto i due anni",
    ],
}

# Errori normativi plausibili: norme REALI del mondo impianti/costruzioni che un
# tecnico potrebbe davvero confondere con le citazioni corrette delle schede.
NORM_ERRORS = [
    "CEI 11-20 (impianti elettrici con tensione superiore a 1 kV in corrente alternata)",
    "UNI 10349 (progettazione e dimensionamento degli impianti termici)",
    "UNI 7129 (impianti a gas per uso domestico)",
    "EN 1991 (azioni sulle strutture: neve, vento, carichi)",
    "UNI EN 13501 (classificazione di reazione e resistenza al fuoco)",
    "UNI 9182 (impianti di condizionamento dell'aria)",
    "CEI 31-35 (impianti elettrici degli ambienti medici)",
    "UNI 11018 (realizzazione di impianti di messa a terra)",
]

def errors_of(nome, n=3, exclude=()):
    bank = [e for e in ERROR_BANK.get(nome, []) if e not in exclude]
    random.shuffle(bank)
    return bank[:n]

questions = []
seen = set()

def key(q):
    return hashlib.md5(q.encode("utf-8")).hexdigest()

def push(testo, scelte, idx, spiegazione, fonte):
    questions.append((testo, scelte, idx, spiegazione, fonte))

# ---------------- PARTE A: modelli semantici con errori della stessa materia ----------------
for d in schede:
    nome = d["nome"]
    desc = d["descrizione"]

    # A1. Definizione: distrattori = errori tipici dello STESSO argomento
    t = f"Quale di queste affermazioni descrive correttamente «{nome}»?"
    if key(t + nome) not in seen:
        errs = errors_of(nome)
        if len(errs) == 3:
            seen.add(key(t + nome))
            scelte = errs + [desc]
            random.shuffle(scelte)
            push(t, scelte, scelte.index(desc),
                 f"Descrizione corretta: {desc}", nome)

    # A2. Tecnologia/criteri d'uso: corretto vs errori stesso argomento
    for fld, richiesta in [
        ("tecnologia", "Quale affermazione su tecnologia e criteri d'uso di «{n}» è corretta?"),
        ("vantaggi", "Quale affermazione sui vantaggi di «{n}» è corretta?"),
        ("limiti", "Quale affermazione su limiti e attenzioni di «{n}» è corretta?"),
        ("applicazioni", "Quale affermazione sulle applicazioni di «{n}» è corretta?"),
        ("costi_e_economia", "Quale affermazione su costi ed economia di «{n}» è corretta?"),
        ("casi_real_world", "Quale affermazione sul caso reale di «{n}» è corretta?"),
        ("note_cantiere", "Quale nota di cantiere è corretta per «{n}»?"),
    ]:
        v = (d.get(fld) or "").strip()
        if len(v) > 20:
            t = richiesta.format(n=nome)
            if key(t + nome + fld) not in seen:
                errs = errors_of(nome, exclude=(v,))
                if len(errs) == 3:
                    seen.add(key(t + nome + fld))
                    scelte = errs + [v]
                    random.shuffle(scelte)
                    push(t, scelte, scelte.index(v), f"Corretto: {v}", nome)

    # A3. Normativa: corretta vs norme reali dello stesso mondo impianti
    v = (d.get("normative") or "").strip()
    if len(v) > 10:
        t = f"Quale riferimento normativo o tecnico è associato a «{nome}»?"
        if key(t + nome + "norm") not in seen:
            norm_pool = [e for e in NORM_ERRORS if e != v]
            random.shuffle(norm_pool)
            if len(norm_pool) >= 3:
                seen.add(key(t + nome + "norm"))
                scelte = norm_pool[:3] + [v]
                random.shuffle(scelte)
                push(t, scelte, scelte.index(v), f"Riferimenti corretti: {v}", nome)

    # A4. Vero/Falso: affermazione corretta della scheda
    t = f"Vero o falso: la seguente affermazione descrive correttamente «{nome}»: «{desc}»"
    if key(t + nome) not in seen:
        seen.add(key(t + nome))
        push(t, ["Vero", "Falso"], 0, f"Affermazione tratta dalla scheda: {desc}", nome)

    # A5. Vero/Falso: errore tipico della STESSA materia attribuito alla scheda → Falso
    bank = ERROR_BANK.get(nome, [])
    if bank:
        err = random.choice(bank)
        t = f"Vero o falso: «{nome}» funziona così: «{err}»"
        k = key(t + nome + err)
        if k not in seen:
            seen.add(k)
            push(t, ["Vero", "Falso"], 1,
                 f"Falso: «{err}» è un errore tipico. Corretto: {desc}", nome)

    # A6. Quale è FALSA: 3 affermazioni vere della scheda + 1 errore tipico
    vere = [x for x in [desc, d.get("tecnologia", ""), d.get("vantaggi", ""),
                        d.get("casi_real_world", ""), d.get("note_cantiere", "")]
            if len((x or "").strip()) > 20]
    vere = list(dict.fromkeys(vere))
    if len(vere) >= 3 and bank:
        random.shuffle(vere)
        vere3 = vere[:3]
        err = random.choice([e for e in bank if e not in vere3])
        t = f"Per «{nome}», quale di queste affermazioni è FALSA?"
        k = key(t + nome + err)
        if k not in seen:
            seen.add(k)
            scelte = vere3 + [err]
            random.shuffle(scelte)
            push(t, scelte, scelte.index(err),
                 f"Falsa: «{err}». Le altre tre sono contenuti della scheda.", nome)

print("parte A (semantiche):", len(questions))

# ---------------- PARTE B: banco di calcoli parametrizzati ----------------
# Distrattori = errori di calcolo che un tecnico farebbe davvero:
# fattore dimenticato, DoD ignorato, zona sbagliata, √3 dimenticato,
# serie/parallelo confusi, quota scambiata con il complementare.
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
# Errori: fattore dimenticato, fattore maggiorato, specifica di una zona più sfavorevole
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
# Errori: moduli vecchi (8-10 m²/kWp), stima per difetto a 4 m²/kWp
for _ in range(N):
    kwp = random.randrange(20, 110, 5) / 10
    mq = kwp * 5.5
    emit(f"Un impianto fotovoltaico da {fmt1(kwp)} kWp richiede indicativamente quale superficie di tetto "
         f"(regola 5-6 m² per kWp)?",
         mq, [kwp * 4, kwp * 8, kwp * 10], fmt0, "m²",
         f"{fmt1(kwp)} × 5,5 ≈ {fmt0(mq)} m²", "Il dimensionamento del fotovoltaico: dal consumo ai kWp")

# B3: peso impianto  kg = m² × kg/m² (12-18)
# Errori: dimenticare le strutture di supporto (8 kg/m²) o sovrastimare come copertura pesante (25-30)
for _ in range(N):
    mq = random.randrange(20, 140, 5)
    kg_m2 = random.randrange(12, 19)
    kg = mq * kg_m2
    emit(f"Un campo FV di {fmt0(mq)} m² con modulo da {kg_m2} kg/m² pesa complessivamente circa quanto?",
         kg, [mq * 25, mq * 8, mq * 30], fmt0, "kg",
         f"{fmt0(mq)} m² × {kg_m2} kg/m² = {fmt0(kg)} kg", "Il dimensionamento del fotovoltaico: dal consumo ai kWp")

# B4: produzione annua  E = kWp × specifica
# Errori: usare la specifica di un'altra zona, maggiorare del 20% 'per sicurezza'
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
# Errori: scambiare quota con il complementare (immissione), quota maggiorata, tutta la produzione
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
# Errori: scambiare con l'autoconsumo, stimare il 90% fisso, maggiorare il 25%
for _ in range(N):
    prod = random.randrange(3000, 9001, 100)
    quota = random.choice([0.3, 0.4, 0.5, 0.6])
    rete = prod * (1 - quota)
    emit(f"Un impianto produce {fmt0(prod)} kWh/anno e autoconsuma il {int(quota*100)}%. Quanta energia immette in rete?",
         rete, [prod * quota, prod * 0.9, prod * (1 - quota) * 1.25], fmt0, "kWh/anno",
         f"{fmt0(prod)} × (1 - {quota}) ≈ {fmt0(rete)} kWh/anno venduti/scambiati",
         "Esempio svolto: impianto FV 6 kWp con accumulo 5 kWh per una famiglia tipo")

# B7: tensione stringa  V = n × Vmpp
# Errori: due moduli in meno/più, raddoppio (confusione serie/parallelo)
for _ in range(N):
    n = random.randrange(8, 17)
    vm = random.randrange(30, 41)
    V = n * vm
    emit(f"Una stringa fotovoltaica con {n} moduli da {vm} V di tensione di massima potenza (Vmpp) ha quale tensione di stringa?",
         V, [(n - 2) * vm, (n + 2) * vm, n * vm * 2], fmt0, "V",
         f"{n} × {vm} V = {fmt0(V)} V", "Il dimensionamento delle stringhe e degli inverter")

# B8: corrente AC trifase  I = P×1000 / (√3 × 400)
# Errori: dimenticare la √3 (usare 400 V), usare 230 V monofase, maggiorare del 50%
for _ in range(N):
    kw = random.randrange(3, 21)
    I = kw * 1000 / (math.sqrt(3) * 400)
    emit(f"Un inverter trifase da {kw} kW erogato su linea 400 V assorbe circa quale corrente di linea?",
         I, [kw * 1000 / 400, kw * 1000 / 230, I * 1.5], fmt1, "A",
         f"I = {fmt0(kw*1000)} / (1,732 × 400) ≈ {fmt1(I)} A", "Il cablaggio DC e AC del fotovoltaico: sezioni e protezioni")

# B9: batteria da fabbisogno  kWh = kWh/giorno × giorni / DoD
# Errori: ignorare il DoD, usare il DoD del piombo (50%), moltiplicare invece di dividere
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
# Errori: ignorare il DoD, usare DoD 50% (piombo), maggiorare del 50%
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
# Errori: ore sovrastimate/ sottostimate, contare le 8.760 h piene
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
# Errori: un collettore in meno/più, accumulo sottodimensionato a 40 l/persona o sovradimensionato
for _ in range(N):
    pers = random.randrange(2, 7)
    coll = math.ceil(pers / 2)
    litri = pers * 60
    w = "collettore" if coll == 1 else "collettori"
    w1 = "collettore" if coll + 1 == 1 else "collettori"
    w2 = "collettore" if max(1, coll - 1) == 1 else "collettori"
    target = f"{coll} {w} / {fmt0(litri)} l"
    opts = {target, f"{coll+1} {w1} / {fmt0(litri+100)} l",
            f"{max(1,coll-1)} {w2} / {fmt0(litri-50)} l", f"{coll} {w} / {fmt0(pers*40)} l"}
    if len(opts) == 4:
        scelte = list(opts)
        random.shuffle(scelte)
        uniq_add(f"Per l'acqua calda sanitaria di {pers} persone (regola: 1 collettore da ~2 m² ogni 2 persone, "
                 f"50-75 l di accumulo a persona), qual è il dimensionamento indicativo?",
                 scelte, scelte.index(target),
                 f"{coll} {w} e {fmt0(litri)} l di accumulo", "Il dimensionamento del solare termico: collettori e accumulo")

# B13: pompa di calore  E_elettrica = Q_termica / COP
# Errori: moltiplicare invece di dividere (il classico), dimezzare, COP 'di sicurezza' maggiorato
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
# Errori: ignorare il DoD, moltiplicare per il DoD, usare il 50% del piombo
for _ in range(N):
    kwh_g = random.randrange(50, 160, 5) / 10
    gg = random.choice([2, 3, 4])
    bat = kwh_g * gg / 0.8
    emit(f"Un sistema off-grid con consumo di {fmt1(kwh_g)} kWh/giorno e {gg} giorni di autonomia richiede "
         f"quale banco batterie (DoD 80%)?",
         bat, [kwh_g * gg, kwh_g * gg * 0.8, kwh_g * gg / 0.5], fmt1, "kWh",
         f"{fmt1(kwh_g)} × {gg} / 0,8 ≈ {fmt1(bat)} kWh", "Il dimensionamento off-grid: l'autonomia totale senza rete")

# B15: off-grid sovradimensionamento FV  kWp = consumo × 1,3 / specifica
# Errori: non sovradimensionare, specifica pessimista, sovradimensionare eccessivo (60%)
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
# Errori: contare la produzione teorica senza perdite, PR sottostimato, maggiorare del 10%
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

# B17: V/F su regole di dimensionamento (corrette ed errori tipici)
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
    fq.write("Criterio qualità: ogni risposta errata appartiene alla stessa materia della domanda\n")
    fq.write("ed è l'errore che un tecnico farebbe realisticamente sul campo.\n\n")
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
