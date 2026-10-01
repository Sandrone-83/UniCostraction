# Facility Management e Manutenzione Programmata — Pack didattico

- **Facoltà:** FACOLTA_GESTIONE_SISTEMA
- **Livello:** L2-L3
- **Schede:** 12
- **Lingua:** italiano
- **Formato:** JSONL (una scheda per riga in `schede/schede.jsonl`)

## Contenuto

Il pack copre la gestione operativa degli edifici nel corso della loro vita: dalla definizione del facility management ai piani di manutenzione programmata (UNI 10329), dalle scadenze legali su impianti termoidraulici, antincendio, elettrici e gas alla gestione della legionella, dalla gestione dei guasti con SLA alla contrattualistica di appalto, dalla digitalizzazione con CMMS/GMAO all'economia della manutenzione, dalla diagnostica con sensori all'organizzazione del team e al piano pluriennale di conservazione dell'edificio che invecchia.

## Struttura delle schede

Ogni scheda è un oggetto JSON con 11 campi: `categoria`, `nome`, `descrizione`, `tecnologia`, `applicazioni`, `vantaggi`, `limiti`, `costi_e_economia`, `casi_real_world`, `normative`, `note_cantiere`.

I riferimenti normativi sono consolidati (UNI 10329, UNI CEI 64-8, DPR 412/1993, D.Lgs 81/2008, D.Lgs 28/2011) e formulati con prudenza dove necessario. I costi sono espressi come ordini di grandezza indicativi per il contesto italiano.

## Uso per l'addestramento

Adatto come materiale di addestramento per LLM specializzati in edilizia: ogni scheda è autosufficiente, con testo corposo nel campo `tecnologia` e casi realistici nel campo `casi_real_world`. Per l'addestramento caricare `schede/schede.jsonl` riga per riga, usando `nome` come chiave e i restanti 10 campi come attributi. Il campo `note_cantiere` fornisce indicazioni operative pratiche da usare come supervisione di stile (sapienza pratica, niente teoria vuota).
