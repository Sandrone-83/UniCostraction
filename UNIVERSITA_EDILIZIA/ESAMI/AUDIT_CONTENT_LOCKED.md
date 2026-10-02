# AUDIT — capacità discriminante degli esami (verifica reale sul corpus)

Data: 2026-10-02 · Metodologia: classificazione di ogni stelo di domanda negli esami di `ESAMI/<SETTORE>/domande.md`.

## Il problema scoperto (gara di ammissione di prova)

Un candidato senza alcun accesso al pack DESIGN_GUSTO ha risposto al suo esame ottenendo **168/174 (97%)** ragionando solo sulle affinità tematiche tra le opzioni: i distrattori dei generatori (`build_esami_giro5.py` e successivi) sono frasi delle schede *sorelle dello stesso pack*, quindi la domanda "quale frase appartiene alla scheda X" si risolve riconoscendo il tema di ogni frase, senza conoscere la scheda. Gli unici errori (6/174) sono caduti sulle domande davvero bloccate sul contenuto: quadri normativi testuali e una domanda con opzione troncata (Q174).

**Conseguenza:** un esame così composto non misura l'apprendimento del corpus; misura la competenza generale. Per la gara di ammissione di AuraTrix serve una quota maggioritaria di domande *content-locked*.

## Classificazione

- **LOCKED** — la risposta corretta non è deducibile senza aver letto la scheda: note di cantiere testuali, dati economici con cifre specifiche, quadri normativi testuali, casi real world con dettagli propri del pack.
- **MISTO** — vantaggi/limiti: parzialmente deducibili dalla logica dell'enunciato.
- **PATTERN** — "appartiene alla tecnologia", "NON appartiene", "riassunto", "applicazioni": risolvibili per tematica senza il corpus.

## Risultati per settore (73 esami, 16.388 domande)

% LOCK: medio-basso la maggioranza dei settori; in fondo i peggiori.

| Fascia | Settori |
|---|---|
| < 8% LOCK (critico) | DIMENSIONAMENTO_TERMOTECNICO 2%, ENERGETICA_INCENTIVI 2%, CAPOLAVORI 4%, CONTABILITA_APPALTI 4%, DIGHE_IDRAULICA 4%, FORMULARIO_FISICA 4%, DIMENSIONAMENTO_FV_EOLICO 5%, EDILIZIA_AGRICOLA 5%, EDILIZIA_SCOLASTICA 5%, EMERGENZE 5%, FOTOVOLTAICO_CER 5%, POSA_IN_OPERA 5%, AEROPORTI 5%, ACUSTICA 6%, FACILITY_MANAGEMENT 6%, FISCO_IMPRESA_EDILE 6%, GEOTECNICA 6%, INGEGNERIA_CIVILE 6%, MATERIALI_COMPONENTI 6%, PORTI_MARITTIMI 6%, PATOLOGIE_DIAGNOSTICA 7%, CARPENTERIA 7%, GESTIONE_CONDOMINIO 8%, GEOMETRA_ESTIMO 8%, MATERIALEDILE*, MATEMATICA 8%, METODI_COSTRUTTIVI 6%, MURATURE_INTONACI 8% |
| 8–20% | DISEGNO_TECNICO 9%, FERROVIE 9%, RISANAMENTO 9%, SOLLEVAMENTO 10%, CAD_BIM 10%, MASTER_DESIGN 8%, LEGNO 13%, DOMOTICA 13%, ILLUMINAZIONE 13%, MACCHINE_TERMICHE 14%, TETTI_COPERTURE 14%, STRUTTURE 6%, ARCHITETTURA 11%, SPECIALI 12%, MATERIALI_FUTURO 8%, INTERIOR_TECNICO 8%, PIETRE_NATURALI 8%, REAL_ESTATE 19%, URBANISTICA 19%, DATA_CENTER 20%, INDUSTRIALE 20%, OSPEDALI 22%, HOTEL 22%, IMPIANTI_SPORTIVI 23%, PISCINE 26%, BONIFICA_SITI 29%, ROBOTICA 29%, SICUREZZA_ANTINCENDIO 34%, SICUREZZA_CANTIERE 41%, LEGISLAZIONE_EDILIZIA 36%, MASTER_IMPRESA 46%, RESTAURO 46%, VERDE_URBANO 45%, INFRASTRUTTURE 40%, IMPIANTI_COMPLETA 21% |
| Formato su misura | IMPIANTI_FV_EOLICO (1000 domande, prevalentemente calcoli numerici = di fatto LOCKED), MATERIALEDILE (1000 domande, matching descrizione↔materiale: parzialmente pattern) |

**Totale: 2.114 domande locked su 16.388 (13%).**

## Piano correttivo

1. **DESIGN_GUSTO rigenerato** (questo giro): nuovo generatore con domande cloze (frase della scheda con un dato cancellato: numero, norma, nome proprio) + peso maggioritario su costi, note di cantiere, casi reali, quadri normativi. Le domande cloze non sono risolvibili senza il testo della scheda.
2. **Audit per campioni**: lo stesso candidato "non addestrato" sostiene il nuovo esame per verificare che il punteggio scenda sotto la soglia di sufficienza attesa per un non lettore.
3. **Graduale**: rigenerare con lo stesso criterio i settori sotto il 10% di LOCK, partendo da quelli che AuraTrix userà prima (DIMENSIONAMENTO_TERMOTECNICO, ENERGETICA_INCENTIVI, FOTOVOLTAICO_CER).

## Nota di trasparenza

Le righe "ZERO domande riconosciute" dei primi audit erano un artefatto del formato `**D1.**` usato dai due esami su misura da 1.000 domande; sono stati classificati a mano qui sopra.
