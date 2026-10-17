# UNI Corpus G0 — audit tecnico, fonti e provenance

Data audit: 2026-10-17  
Worktree: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-corpus`  
Branch: `codex/uni-corpus`  
Base osservata: `afab387` (`v1.3.0-7-gafab387`)

## Scopo e limiti

Questo è un audit di censimento, non una validazione tecnica o giuridica
definitiva. La scansione è stata limitata a README, COURSE, manifest/licenze,
indici, directory `raw`, formule e metadati strutturali. Non sono state modificate
le schede didattiche, non sono state rigenerate le serializzazioni e non sono
state riportate domande o risposte d'esame.

La classificazione `source_kind` è deliberatamente conservativa:

- `primary/official`: fonte normativa o tecnica istituzionale, da usare solo con
  identificativo, versione/data e URL o file sorgente verificabili;
- `manufacturer`: documentazione di produttore, da usare solo con titolare,
  modello, revisione e permesso di riuso espliciti;
- `internal interpretation`: sintesi, scheda o formula redatta internamente;
- `example`: esempio, modello o dato dimostrativo, non prova normativa;
- `hypothesis`: affermazione di README/INDEX/manifest ancora da collegare a
  evidenza di fonte e licenza a livello di record.

## Snapshot del materiale già presente

| Area | Evidenza osservata | Stato audit |
| --- | --- | --- |
| `UNIVERSITA_EDILIZIA` | 71 directory `*_PACK`, 71 `COURSE.yaml`, 71 `schede/schede.jsonl`, 69 `README.md`, 73 directory esame | Struttura ampia; provenance non uniforme nei pack | 
| README mancanti | `ACUSTICA_EDILIZIA_PACK`, `CONTABILITA_APPALTI_PACK`, `ENERGETICA_INCENTIVI_PACK`, `GEOTECNICA_E_FONDAZIONI_PACK` | Gap documentale, nessuna modifica fatta | 
| `Edilizia_Pack` | `README.md`, `HANDOFF.md`, `manifest.json`, `licenze_audit.json`; fonti raw in manuali USA, eCFR, norme italiane, UFGS, NPS/FEMA e BIM/IFC | Registro esistente; `parsed/` dichiarata nei documenti non presente nel worktree osservato | 
| `Fondamenti_Pack` | `README.md`, `HANDOFF.md`, `manifest.json`, `licenze_audit.json`, 14 file raw Gutenberg e directory `parsed` | È il candidato più semplice per un primo lotto source-preserving | 
| Fonti locali universitarie | `UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/README.md` e `Regole_Applicative_CT_3_0_GSE.pdf` | Fonte ufficiale locale presente, ma ambito dinamico e singola provenance esplicita | 
| Formule | `MATEMATICA_PER_COSTRUIRE_PACK`, `FORMULARIO_STRUTTURE_PACK`, `FORMULARIO_FISICA_IMPIANTI_PACK` con schema didattico a 11 campi | Curabili come interpretazione/esempio dopo audit formula-per-formula | 

## Registro di corpus e decisione di curabilità

| source_kind | Corpus/file già presenti | Licenza / provenance osservata | Limiti e gap | Disposizione G0 |
| --- | --- | --- | --- | --- |
| `primary/official` | `Edilizia_Pack/raw/manuals_txt/`, `raw/us_gov_pdf/`, `raw/ufgs_specs/`, `raw/ecfr/`, `raw/norme_it/`; PDF GSE nel pack incentivi | `Edilizia_Pack/licenze_audit.json` dichiara public domain per fonti Governo USA/OSHA, CC BY-SA per alcune edizioni, e “atto pubblico” per atti italiani; il README GSE indica documento ufficiale GSE scaricato da `gse.it` | L'audit locale non riconvalida termini correnti, catena di download, hash per file o diritto di riuso di ogni edizione. Un atto pubblico va distinto da una trascrizione/edizione di terzi; norme UNI/EN, Eurocodici e prezzari non sono da includere per default | **Lotto 1A candidato**: preservare i file sorgente istituzionali con identificativo, data/versione, URL, hash e nota di uso. La serializzazione `parsed` di `Edilizia_Pack` manca e va trattata come lavoro successivo, non come corpus già ingestibile |
| `primary/official` | Normativa citata nei pack `UNIVERSITA_EDILIZIA` e nei `COURSE.yaml` (D.Lgs, DPR, DM, UNI/EN, CEI, GSE/MASE/ARERA) | I pack dichiarano riferimenti e in alcuni casi prudenza temporale; la presenza del numero di norma non costituisce provenance | Mancano nei pack universitari un registro per-record con fonte, versione, licenza e stato di verifica; le norme tecniche protette non vanno riprodotte senza autorizzazione | Tenere come riferimenti da mappare; non promuovere automaticamente a corpus curato |
| `manufacturer` | Nella scansione limitata non è emerso un registro curato di datasheet, manuali di produttore, modelli/revisioni o autorizzazioni | Nessuna provenance/licenza di produttore pronta per ingestione | Non si possono attribuire prestazioni, valori U/COP/portate/resistenze o comparazioni commerciali a un marchio senza documento identificato e vigente | **Fuori dal lotto 1**; aprire solo con manifest dedicato e prova di riuso |
| `internal interpretation` | `UNIVERSITA_EDILIZIA/*_PACK/schede/schede.jsonl`, README/COURSE; sintesi redazionali e glossari dei pack base | Licenza repository: proprietaria Auratrix; le schede usano schema comune a 11 campi. `Edilizia_Pack` e `Fondamenti_Pack` dichiarano inoltre sintesi originali in audit dedicati | Il campo `normative` non sostituisce una fonte; nei pack universitari non c'è record-level `attribution`, `source_url`, `source_version` o `license`. I costi sono dichiarati indicativi e devono restare tali | **Lotto 1B differito**: curare solo dopo aggiunta di manifest esterno per scheda/tema, separando fatto ufficiale, interpretazione e ipotesi |
| `example` | Formule e svolgimenti nei tre pack formulario; esempi didattici dichiarati in `Edilizia_Pack`; modelli IFC in `raw/bim_ifc/ifc_models/` con LICENSE | Formule/esempi: sintesi interna; IFC: HANDOFF/licenza indicano MIT per i modelli, da verificare per file e dataset originario | Un esempio numerico non dimostra conformità a un edificio reale né sostituisce NTC/UNI/CEI; eventuali formule devono avere simboli, unità, ipotesi, dominio di validità e fonte metodologica | **Lotto 1C differito controllato**: audit formula e metadati senza trasformarlo in norma o prestazione garantita |
| `hypothesis` | Affermazioni di `UNIVERSITA_EDILIZIA/INDEX.md`, `VERSIONE.md`, README e manifest, inclusi conteggi, “verificato”, `commercial_ok` e copertura esami | Sono dichiarazioni di progetto; alcune rimandano a `CHANGELOG.md` o a `licenze_audit.json` | Non sono prove sufficienti senza collegamento a file sorgente, revisione, hash e responsabile della verifica. I dati incentivi e fiscali cambiano nel tempo | Usare solo per pianificare il lavoro; nessuna affermazione ipotetica entra nel lotto curato |

## Primo lotto curabile senza inventare fonti o prestazioni

### Lotto 1A — fonti istituzionali già conservate

1. `Fondamenti_Pack/raw/gutenberg/` (14 opere) e i file già presenti in
   `Fondamenti_Pack/parsed/`, limitatamente alle opere con record e URL nel
   `manifest.json`; separare public domain da CC BY-SA 4.0 e conservare
   attribuzione.
2. Sottoinsieme pubblico/istituzionale di `Edilizia_Pack/raw/`: manuali e
   report Governo USA, eCFR/OSHA, UFGS e documenti NPS/FEMA, usando
   `Edilizia_Pack/licenze_audit.json` come indice da riconfermare, non come
   prova unica.
3. Il PDF GSE locale del Conto Termico 3.0 come fonte primaria di verifica,
   mantenendo data di acquisizione, URL e hash; non estendere da questo file
   conclusioni a incentivi diversi.

Il lotto 1A è “curabile” come pacchetto di fonti e metadati, ma non è ancora un
rilascio train-ready completo: per `Edilizia_Pack` il README/HANDOFF dichiara
file `parsed/*.jsonl` che non risultano presenti nella scansione osservata.

### Esplicitamente fuori dal primo lotto

- norme UNI/EN, Eurocodici, CEI e prezzari, salvo licenza/autorizzazione
  esplicita e record di provenance;
- datasheet o prestazioni di produttori non ancora registrati;
- schede universitarie come fatti verificati solo perché contengono un numero di
  norma o una formula;
- dati fiscali/incentivi temporali senza una verifica della versione vigente;
- domande d'esame e chiavi: nel presente audit sono stati contati solo i
  contenitori/metadati, senza riportare testo di domande o risposte.

## Residui e gap per il coordinatore

1. Creare un manifest di provenance separato dalle schede con almeno:
   `record_or_scope`, `source_kind`, `title`, `issuer`, `version_date`, `url_or_path`,
   `retrieved_at`, `sha256`, `license_basis`, `attribution`, `verification_status`,
   `reviewer`.
2. Risolvere i 4 README mancanti dei pack indicati nello snapshot.
3. Riconciliare `manifest.json`/`HANDOFF.md` con la presenza effettiva dei
   `parsed/*.jsonl` prima di dichiarare ingestione pronta.
4. Per le formule: controllo dimensionale, unità, ipotesi, dominio di validità,
   esempio indipendente e riferimento bibliografico; marcare gli esempi come
   esempi, non come prestazioni garantite.
5. Registrare fonti locali e normative per tema, senza copiare testo protetto e
   senza trattare la licenza del codice o del repository come licenza automatica
   di ogni fonte incorporata.
6. Mantenere le chiavi d'esame fuori dal corpus operativo e verificare solo la
   pipeline di valutazione con accesso riservato.

## Controlli eseguiti

- branch e stato iniziale: `git status --short --branch` → `codex/uni-corpus`,
  worktree pulito;
- censimento limitato di directory/file: `Get-ChildItem` e `rg --files` su
  README, COURSE, manifest, licenze, raw e fonti locali;
- lettura mirata di `INDEX.md`, `VERSIONE.md`, README/COURSE dei formulari,
  `Edilizia_Pack/README.md`, `Fondamenti_Pack/README.md`, HANDOFF e registri
  `manifest.json`/`licenze_audit.json`;
- nessuna modifica a `schede.jsonl`, `domande.md` o chiavi d'esame;
- `git diff --check`: da eseguire dopo la creazione di questo documento e prima
  del commit locale.

## Decisione G0

Il corpus non è ancora “curato” in senso di rilascio: esiste un buon nucleo di
fonti raw con registri di licenza, ma la provenance per-record e la riconciliazione
tra raw/parsed e schede universitarie sono incomplete. Il coordinatore può
revisionare questo manifesto e autorizzare il lotto 1A; nessun push è previsto
da questo worktree.
