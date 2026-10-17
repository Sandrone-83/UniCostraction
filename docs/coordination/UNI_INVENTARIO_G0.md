# UniCostraction — inventario G0

Data audit: 2026-10-17
Worktree: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-inventory`
Branch: `codex/uni-inventory`
Base osservata: `afab387`

## Perimetro e metodo

Audit mirato di root, manifesto/versione, pack/corsi, esami, asset e registri. La scansione è stata interrotta su richiesta dopo la raccolta delle evidenze essenziali. Non sono stati modificati contenuti didattici e non è stata eseguita alcuna deduplicazione automatica.

Le categorie sono mantenute separate:

- **Fonte**: file e metadati effettivamente presenti nel checkout, più il messaggio del commit di base.
- **Interpretazione**: raggruppamenti e conteggi derivati dai percorsi e dai campi osservati.
- **Esempio**: campioni usati per capire la forma dei dati; non rappresentano l’intero corpus.
- **Ipotesi / residui**: segnali da verificare prima di qualunque consolidamento.

## Fonte — evidenze osservate

### Root e manifesto

- Root `README.md`: identifica UniCostraction, dichiara la licenza proprietaria Auratrix e rimanda a `LICENSE`.
- `UNIVERSITA_EDILIZIA/VERSIONE.md`: documento di versione/metodologia; dichiara v1.2.0, 66 corsi e 67 esami per quella release storica.
- `UNIVERSITA_EDILIZIA/VERSION`: contiene `v1.3.0`.
- Il commit di base osservato (`afab387`) dichiara nel messaggio: `71 pack/963 schede/73 esami`.

### Pack e corsi

- File `COURSE.yaml` tracciati: **83**.
- Pack sotto `UNIVERSITA_EDILIZIA/`: **71**, con **71** file `schede/schede.jsonl`.
- Pack/corsie di root fuori da `UNIVERSITA_EDILIZIA/`: **12** (`CAD_Library`, `Coding_Master_Pack` e moduli `_2`–`_5`, `Digitale_Marketing_Pack`, `Edilizia_Pack`, `Fondamenti_Pack`, `Italia_Sistema_Pack`, `MATERIALEDILE_PACK`, `Storia_Pack`).
- Il formato osservato nei corsi universitari usa almeno i campi `corso`, `facolta`, `livello`, `schede`, `formato`, `lingua`, `schema_campi`, `fonti`, `nota_metodologica`.

### Esami

- File esame `UNIVERSITA_EDILIZIA/ESAMI/**/domande.md`: **73**.
- Registri/documenti di controllo nella stessa area: `README.md`, `PROTOCOLLO_VALUTAZIONE.md`, `AUDIT_CONTENT_LOCKED.md`.
- I nomi delle directory d’esame non sono una copia letterale dei nomi dei pack: sono presenti alias sintetici come `CAD_BIM`, `DIMENSIONAMENTO_FV_EOLICO`, `STRUTTURE` e `IMPIANTI_FV_EOLICO`.

### Asset, fonti e registri rilevati

- `CAD_Library/`: **5.859** percorsi tracciati; è il principale aggregato di asset/dataset della root.
- `Edilizia_Pack/`: **297** percorsi tracciati; include, tra gli altri, `raw/`, `discovery/`, `manifest.json`, `licenze_audit.json` e script di costruzione/estrazione.
- `Coding_Master_Pack/` e `Coding_Master_Pack_2/` contengono `licenze_audit.json` e materiale `parsed/`.
- `discovery_ufgs_one.json` è presente in root; ulteriori registri discovery sono presenti in `Edilizia_Pack/discovery/`.

## Interpretazione — duplicati e sovrapposizioni

### Duplicati nominali

- Non sono stati rilevati duplicati **esatti** nei valori `corso:` dei 83 `COURSE.yaml` osservati.
- Esistono sovrapposizioni lessicali legittime, per esempio “Disegno tecnico e dataset CAD” e “Disegno tecnico e rappresentazione”; sono segnali di possibile area tematica comune, non duplicati nominali esatti.
- La differenza tra **71 pack universitari** e **73 esami** è un disallineamento nominale/di copertura da mappare, non una prova di duplicazione.

### Duplicati strutturali

Confronto SHA-256 eseguito sui nuclei a maggiore rischio di copia:

| Nucleo | Gruppi di file identici rilevati |
|---|---:|
| `COURSE.yaml` | 0 |
| `README.md` dei pack | 0 |
| `schede.jsonl` | 0 |
| `ESAMI/**/domande.md` | 0 |

I pack universitari condividono una struttura ricorrente (`COURSE.yaml`, `README.md`, `schede/schede.jsonl`, con builder opzionale). Questa è una **somiglianza di schema**, non un duplicato di contenuto; nessun file è stato rimosso o accorpato.

## Esempio — campione non generalizzabile

`UNIVERSITA_EDILIZIA/ACUSTICA_EDILIZIA_PACK/COURSE.yaml` mostra il formato del corso e dichiara `schede: 12`, con fonti normative e nota metodologica. Il campione serve solo a documentare la forma del manifesto di pack; non costituisce una verifica normativa o didattica dell’intero repository.

## Ipotesi / residui per il coordinatore

1. Va costruita una tabella esplicita pack ↔ esame per spiegare i 71 pack e i 73 file `domande.md`, mantenendo gli alias e gli eventuali esami legacy come stati separati.
2. Il riferimento storico v1.2.0 in `VERSIONE.md` e il messaggio del commit di base con 71/963/73 descrivono snapshot diversi: non vanno fusi senza una verifica di versione/tag e senza decidere quale registro sia normativo per il coordinamento.
3. Le somiglianze tematiche e di struttura non autorizzano una deduplicazione: ogni consolidamento richiede confronto semantico, provenienza e approvazione del coordinatore.
4. Non è stata fatta una validazione completa delle righe JSONL né una revisione dei contenuti degli esami: restano fuori dal G0.

## Controlli e stato di modifica

- Controlli eseguiti: inventario tracciato con `git ls-files`, conteggi mirati, lettura dei manifesti/versioni, confronto SHA-256 dei quattro nuclei indicati.
- Controllo eseguito dopo la scrittura: `git diff --check` con esito positivo (`exit 0`).
- Modifiche ammesse: questo solo documento sotto `docs/coordination/`.
- Push: non eseguito e da non eseguire prima della revisione del coordinatore.
