# MURATURE_INTONACI_E_FINITURE_PACK

**Corso:** Murature, intonaci e finiture murali
**Facoltà:** FACOLTA_TECNOLOGIA_E_COSTRUZIONE
**Livello:** L1-L2
**Schede:** 12
**Lingua:** IT

## Contenuto

Pack di schede didattiche sulla tecnologia dei materiali per murature, intonaci e finiture murali: laterizi e blocchi alleggeriti, malte, setti in cls, intonaci tradizionali e speciali, rasanti e vernici, patologie e involucri perimetrali. Il pack copre il MATERIALE e le sue prestazioni, non la posa in opera.

Le schede sono distribuite per categoria: **Murature** (laterizi, blocchi alleggeriti e AAC, malte, setti, patologie, involucri a telaio), **Intonaci** (tradizionali, premiscelati, a calce e pregiate finiture), **Finiture murali** (rasanti e silossanico/quarzo, vernici silicatiche e acriliche, finiture decorative effetto).

## Formato

- `schede/schede.jsonl` — una scheda per riga, oggetto JSON con 11 campi: `categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere`
- `COURSE.yaml` — metadati del corso

## Uso per l'addestramento

Le schede sono pensate come corpus di addestramento per un LLM specializzato in edilizia: ogni scheda presenta un materiale o un sistema con le sue prestazioni, applicazioni, limiti, economia, riferimenti normativi (di consolidata certezza, senza numerazioni inventate) e note pratiche di cantiere. I costi sono sempre espressi come ordini di grandezza indicativi per il mercato italiano. I casi real world descrivono tipologie di intervento e non aziende specifiche.
