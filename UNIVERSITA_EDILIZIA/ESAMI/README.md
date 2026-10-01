# ESAMI DI VALUTAZIONE — Università Edilizia per LLM

Ogni settore ha un esame a risposta multipla generato dalle schede didattiche.
Le domande sono in repository; le risposte corrette sono in un archivio riservato
fuori repository (ESAMI_RISPOSTE/), consegnato solo al proprietario, che le usa
con Claude Code per valutare il proprio LLM: risposte esatte/sbagliate e giudizio
di apprendimento per settore.

## Struttura
- `ESAMI/<SETTORE>/domande.md` — elenco domande (A-D o Vero/Falso), senza risposte.
- `ESAMI_RISPOSTE/<SETTORE>_risposte.jsonl` — fuori repo: risposta corretta,
  spiegazione e scheda-fonte per ogni domanda.

## Settori

| Settore | Stato | Note |
| --- | --- | --- |
| MATERIALEDILE | ✅ 1.000 domande | dimostratore completo (162 schede) |
| DISEGNO_TECNICO | in coda | 14 schede |
| CAD_BIM | in coda | 12 schede |
| EDILIZIA_GENERALE | in coda | Edilizia_Pack |
| IMPIANTI_TERMICI | in coda | Macchine termiche + dimensionamento |
| IMPIANTI_FV_EOLICO | ✅ 1.000 domande | dimensionamento FV/eolico/accumulo (10 schede + banco calcoli) |
| ASCENSORI | ✅ 300 domande | ascensori, piattaforme, montacarichi, scale mobili (10 schede) |
| FOTOVOLTAICO_CER | ✅ 400 domande | campi FV a terra, agrivoltaico, CER/AUC/GAC, BESS (15 schede) |
| SICUREZZA_CANTIERE | ✅ 250 domande | D.Lgs 81/08, PSC, POS, ponteggi, scavi, attrezzature (13 schede) |
| MURATURE_INTONACI | ✅ 250 domande | laterizi, AAC, malte, intonaci, finiture, patologie (12 schede) |
| FACILITY_MANAGEMENT | ✅ 250 domande | piani manutenzione, legionella, adempimenti ricorrenti, CMMS (12 schede) |
| FISCO_IMPRESA_EDILE | ✅ 250 domande | IVA edilizia, forfettario 86%, ritenute, DURC, ISA (11 schede) |
| DISEGNO_TECNICO | ✅ 250 domande | proiezioni, quotatura, tavole esecutive, rilievo (14 schede) |
| DOMOTICA | ✅ 300 domande | protocolli, attuatori, scenari, sicurezza informatica (29 schede) |
| POSA_IN_OPERA | ✅ 300 domande | getti, murature, massetti, pavimenti, serramenti (22 schede) |
| MATERIALI_COMPONENTI | ✅ 250 domande | tubi, raccordi, valvole, quadri elettrici, protezioni (18 schede) |
| INGEGNERIA_CIVILE | ✅ 250 domande | dighe, strade, ferrovie, gallerie, opere marittime (16 schede) |
| DOMOTICA | in coda | 29 schede |
| POSA_IN_OPERA | in coda | 22 schede |
| STRUTTURE | in coda | ingegneria strutturale + formulario |
| INGEGNERIA_CIVILE | in coda | 16 schede |
| ARCHITETTURA_DESIGN | in coda | architettura + master design |
| INTERIOR_TECNICO | in coda | 11 schede |
| DESIGN_TENDENZE | in coda | 11 schede |
| ROBOTICA_EDILIZIA | in coda | 27 schede |
| GEOMETRA_ESTIMO | in coda | 15 schede |
| STORIA_CAPOLAVORI | in coda | 25 schede |
| MATEMATICA_FISICA | in coda | matematica + formulari |
| CODING | in coda | Coding_Master_Pack 1-5 |

## Metodo di generazione
Script `build_esami.py`: 15 modelli di domanda per scheda (definizione, categoria,
tecnologia, vantaggi, limiti, normative, applicazioni, costi, note di cantiere,
vero/falso diretti e incrociati, riconoscimento inverso), con deduplica MD5,
mescolamento fissato (seed 42) per riproducibilità e tracciamento della scheda-fonte.
