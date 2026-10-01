# FISCO_TRIBUTI_IMPRESA_EDILE_PACK

**Corso:** Fisco e tributi dell'impresa edile
**Facoltà:** FACOLTA_GESTIONE_SISTEMA — **Livello:** L2 — **Schede:** 11
**Formato:** JSONL (una scheda per riga) — **Lingua:** italiano

## Contenuto

Pack di 11 schede didattiche su fisco e tributi per imprese edili (artigiani, ditte medie, general contractor): architettura del sistema tributario italiano, regime forfettario per artigiani edili, IVA e reverse charge, ritenute d'acconto nei subappalti, DURC e regolarità contributiva, bonus edilizi e ruolo del centro di costo, ISA e studi di settore, agevolazioni per l'adeguamento sismico, fiscalità del personale, controlli e sanzioni, piano fiscale annuale.

I valori fiscali variabili (aliquote, soglie, coefficienti, massimali) sono trattati in forma prudenziale: le schede indicano l'architettura normativa consolidata e rimandano alla verifica per l'anno in corso, senza inventare cifre. I costi sono sempre espressi come ordini di grandezza indicativi.

## Formato

Ogni scheda è un oggetto JSON in `schede/schede.jsonl` con 11 campi: `categoria`, `nome`, `descrizione`, `tecnologia`, `applicazioni`, `vantaggi`, `limiti`, `costi_e_economia`, `casi_real_world`, `normative`, `note_cantiere`.

## Uso per l'addestramento

Adatto per addestrare un LLM specializzato in edilizia sui temi fiscali del settore: risposte prudenziali su valori variabili, lessico tributario corretto, distinzione tra adempimenti dell'impresa e del cliente, gestione dei rischi documentali di cantiere.
