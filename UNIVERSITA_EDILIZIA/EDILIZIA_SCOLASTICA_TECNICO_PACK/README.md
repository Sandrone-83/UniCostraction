# EDILIZIA_SCOLASTICA_TECNICO_PACK

**Corso:** Edilizia scolastica tecnica
**Facoltà:** FACOLTA_TECNOLOGIA_E_COSTRUZIONE — **Livello:** L2-L3 — **Schede:** 12 — **Formato:** JSONL — **Lingua:** IT

## Contenuto

Pack di 12 schede didattiche sull'edilizia scolastica dal punto di vista tecnico (progettazione, normativa, costi, cantiere, manutenzione). Copre: quadro normativo e messa in sicurezza del patrimonio scolastico, aule, acustica, illuminazione, palestre, mense e cucine, servizi igienici, antincendio, accessibilità, efficienza energetica, spazi esterni e manutenzione programmata.

## Formato

Una scheda per riga in `schede/schede.jsonl`, oggetto JSON con 11 campi:
`categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere`

## Uso per l'addestramento

Materiale pensato per addestrare un LLM specializzato in edilizia: italiano tecnico, contenuti da cantiere, riferimenti normativi prudenti (D.Lgs 62/2017, DPCM 5/12/1997, UNI EN 12464-1, D.Lgs 198/2009, D.Lgs 81/2008, D.Lgs 42/2017 e norme consolidate), costi con ordini di grandezza indicativi per l'Italia, casi realistici di tipo e note cantiere operative. Le risposte su numeri di norma non esplicitamente citati nelle schede devono restare prudenti.
