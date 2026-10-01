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
| ACUSTICA | ✅ 220 domande | chiavi: jsonl |
| ARCHITETTURA | ✅ 250 domande | chiavi: jsonl |
| ASCENSORI | ✅ 300 domande | chiavi: jsonl |
| BONIFICA_SITI | ✅ 250 domande | chiavi: jsonl |
| CAD_BIM | ✅ 200 domande | chiavi: jsonl |
| CAPOLAVORI | ✅ 300 domande | chiavi: jsonl |
| CARPENTERIA | ✅ 250 domande | chiavi: jsonl |
| CONTABILITA_APPALTI | ✅ 200 domande | chiavi: jsonl |
| COSTRUZIONI_LEGNO | ✅ 220 domande | chiavi: jsonl |
| COSTRUZIONI_SPECIALI | ✅ 220 domande | chiavi: jsonl |
| DATA_CENTER | ✅ 200 domande | chiavi: jsonl |
| DESIGN_GUSTO | ✅ 174 domande | chiavi: jsonl |
| DIMENSIONAMENTO_FV_EOLICO | ✅ 220 domande | chiavi: jsonl |
| DIMENSIONAMENTO_TERMOTECNICO | ✅ 250 domande | chiavi: jsonl |
| DIGHE_IDRAULICA | ✅ 250 domande | chiavi: jsonl |
| DISEGNO_TECNICO | ✅ 250 domande | chiavi: jsonl |
| DOMOTICA | ✅ 300 domande | chiavi: jsonl |
| EDILIZIA_AGRICOLA | ✅ 250 domande | chiavi: jsonl |
| EDILIZIA_INDUSTRIALE | ✅ 200 domande | chiavi: jsonl |
| EDILIZIA_SCOLASTICA | ✅ 250 domande | chiavi: jsonl |
| ENERGETICA_INCENTIVI | ✅ 250 domande | chiavi: jsonl |
| FACILITY_MANAGEMENT | ✅ 250 domande | chiavi: jsonl |
| FISCO_IMPRESA_EDILE | ✅ 250 domande | chiavi: jsonl |
| FORMULARIO_FISICA | ✅ 220 domande | chiavi: jsonl |
| FORMULARIO_STRUTTURE | ✅ 250 domande | chiavi: jsonl |
| FOTOVOLTAICO_CER | ✅ 400 domande | chiavi: jsonl |
| FERROVIE | ✅ 250 domande | chiavi: jsonl |
| GEOMETRA_ESTIMO | ✅ 250 domande | chiavi: jsonl |
| GEOTECNICA | ✅ 250 domande | chiavi: jsonl |
| GESTIONE_CONDOMINIO | ✅ 250 domande | chiavi: jsonl |
| HOTEL | ✅ 200 domande | chiavi: jsonl |
| IMPIANTI_SPORTIVI | ✅ 250 domande | chiavi: jsonl |
| IMPIANTI_COMPLETA | ✅ 350 domande | chiavi: jsonl |
| IMPIANTI_FV_EOLICO | ✅ 1000 (legacy) domande | chiavi: jsonl |
| INFRASTRUTTURE | ✅ 175 domande | chiavi: jsonl |
| INGEGNERIA_CIVILE | ✅ 250 domande | chiavi: jsonl |
| INTERIOR_TECNICO | ✅ 200 domande | chiavi: jsonl |
| LEGISLAZIONE_EDILIZIA | ✅ 167 domande | chiavi: jsonl |
| MACCHINE_TERMICHE | ✅ 250 domande | chiavi: jsonl |
| MASTER_DESIGN | ✅ 250 domande | chiavi: jsonl |
| MASTER_IMPRESA | ✅ 173 domande | chiavi: jsonl |
| MATEMATICA | ✅ 220 domande | chiavi: jsonl |
| MATERIALEDILE | ✅ 1000 (legacy) domande | chiavi: jsonl |
| MATERIALI_COMPONENTI | ✅ 250 domande | chiavi: jsonl |
| MATERIALI_FUTURO | ✅ 220 domande | chiavi: jsonl |
| MURATURE_INTONACI | ✅ 250 domande | chiavi: jsonl |
| METODI_COSTRUTTIVI | ✅ 250 domande | chiavi: jsonl |
| OSPEDALI | ✅ 200 domande | chiavi: jsonl |
| PISCINE | ✅ 200 domande | chiavi: jsonl |
| PERIZIE_STIME | ✅ 250 domande | chiavi: jsonl |
| PIETRE_NATURALI | ✅ 250 domande | chiavi: jsonl |
| POSA_IN_OPERA | ✅ 300 domande | chiavi: jsonl |
| PREFABBRICAZIONE | ✅ 250 domande | chiavi: jsonl |
| REAL_ESTATE | ✅ 180 domande | chiavi: jsonl |
| RESTAURO_CONSERVAZIONE | ✅ 223 domande | chiavi: jsonl |
| RISANAMENTO | ✅ 277 domande | chiavi: md (legacy) |
| ROBOTICA | ✅ 350 domande | chiavi: jsonl |
| RINNOVABILI_IDRO | ✅ 250 domande | chiavi: jsonl |
| SICUREZZA_ANTINCENDIO | ✅ 220 domande | chiavi: jsonl |
| SICUREZZA_CANTIERE | ✅ 250 domande | chiavi: jsonl |
| STRUTTURE | ✅ 300 domande | chiavi: jsonl |
| TETTI_COPERTURE | ✅ 220 domande | chiavi: jsonl |
| URBANISTICA | ✅ 180 domande | chiavi: jsonl |
| VERDE_URBANO | ✅ 159 domande | chiavi: jsonl |

Copertura: esame per ognuno dei 63 corsi della repository. I tre esami «legacy» dei primi giri
(MATERIALEDILE, IMPIANTI_FV_EOLICO, RISANAMENTO) usano il formato dei primi generatori:
chiavi complete e valide, schema dei campi diverso dal generatore attuale.

## Metodo di generazione
Script `build_esami.py`: 15 modelli di domanda per scheda (definizione, categoria,
tecnologia, vantaggi, limiti, normative, applicazioni, costi, note di cantiere,
vero/falso diretti e incrociati, riconoscimento inverso), con deduplica MD5,
mescolamento fissato (seed 42) per riproducibilità e tracciamento della scheda-fonte.
