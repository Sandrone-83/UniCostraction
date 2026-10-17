# UniCostraction — review anti-ridondanza G2

Data audit: 2026-10-17
Worktree: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-inventory`
Branch: `codex/uni-inventory`
Base verificata: `e7d4547`
Input principale: `docs/coordination/UNI_DUPLICATE_MATRIX_G1.json`
Tool/test esaminati: `tools/uni_inventory_g1.py`, `tests/coordination/test_uni_inventory_g1.py`

## Esito

Nel perimetro G1 non risultano duplicati confermati né candidati da sottoporre a revisione. Non è stata eseguita alcuna cancellazione, fusione, sovrascrittura o movimentazione di file.

Questo è un esito strutturale, non una certificazione di equivalenza semantica: G1 confronta byte, testo con line ending normalizzati e il primo campo `corso:` dei manifesti. Non decide se due lezioni, domande o fonti abbiano lo stesso significato.

## Perimetro osservato

| Categoria | File |
| --- | ---: |
| `course_cards` | 71 |
| `course_manifest` | 83 |
| `readme` | 82 |
| `exam_questions` | 73 |
| `exam_document` | 2 |
| `exam_readme` | 1 |
| **Totale** | **312** |

Il perimetro è quello dichiarato dalla matrice G1: `COURSE.yaml`, `README.md`, `schede.jsonl` e contenuti sotto `ESAMI/**`, con esclusione di `.git`, `tests` e `work`. Il risultato non si estende automaticamente a raw, discovery, asset, registri o altri file non indicizzati dal tool.

## Classificazione dei risultati

| Classificazione | Esito G2 | Motivazione ed evidenza |
| --- | --- | --- |
| **Duplicato confermato** | **Nessuno** | Le 312 evidenze hanno SHA-256 distinti. G1 non ha prodotto gruppi `exact_sha256_match`; quindi non esiste una prova di copia byte-per-byte nel perimetro. |
| **Candidato da revisione** | **Nessuno** | `possible_duplicate_groups` è una lista vuota. Non ci sono collisioni di hash dopo normalizzazione dei line ending né collisioni tra i `course_title_key` dei 83 manifesti. |
| **Variante legittima** | **Schema ricorrente, non duplicato** | La ripetizione dei ruoli `COURSE.yaml`/`README.md`/`schede.jsonl` nei pack e dei documenti negli esami è coerente con una struttura didattica comune. Il formato condiviso non è stato promosso a candidato: i contenuti e i manifesti restano distinti. |
| **Nessun segnale** | **312 file** | Ogni voce della matrice ha `signals: []`. Questo significa che nessun segnale G1 ha coinvolto il file; non significa che il contenuto sia stato semanticamente confrontato o approvato in assoluto. |

Le categorie “variante legittima” e “nessun segnale” operano a livelli diversi: la prima descrive la struttura ricorrente del corpus, la seconda il risultato dei segnali associati alle singole evidenze. Nessuna delle due autorizza deduplicazioni.

## Perché il report ha zero gruppi candidati

Il tool costruisce i gruppi solo da tre segnali:

1. uguaglianza dello SHA-256 dei byte;
2. uguaglianza del testo dopo normalizzazione dei line ending, quando gli SHA-256 byte-level differiscono;
3. uguaglianza normalizzata del titolo `corso:` nei soli `COURSE.yaml`.

Nel report corrente tutti e tre gli insiemi sono senza collisioni. Di conseguenza `candidate_groups` resta vuoto, nessun percorso viene inserito in `groups_by_path` e ogni entry riceve `signals: []`. Il valore zero è quindi coerente con la logica del tool e con i dati osservati, non con un’assunzione che nomi simili o schemi comuni siano impossibili.

## Verifiche future necessarie

Prima di qualsiasi consolidamento servono almeno queste verifiche:

1. **Confronto semantico strutturato.** Parsare YAML e JSONL, confrontare ID, titoli, testo delle schede, fonti, domande e risposte; aggiungere una ricerca di near-duplicate che gestisca whitespace, punteggiatura, ordinamento dei campi e varianti minime. G1 non esegue questi confronti.
2. **Mappatura pack–esame.** Spiegare il rapporto tra 71 pack universitari e 73 file `domande.md`, mantenendo separati alias, esami legacy e casi senza pack omonimo. Un nome di directory non è un’identità canonica.
3. **Estensione controllata del perimetro.** Valutare raw, discovery, manifest, registri e altri asset solo con un inventario esplicito e una regola di ownership; non mescolare automaticamente materiali di lavoro e fonti pubblicabili.
4. **Provenienza e versione.** Per ogni eventuale sovrapposizione verificare origine, data/versione, autore, licenza, destinazione didattica e ruolo canonico. Una somiglianza non dimostra quale copia debba sopravvivere.
5. **Controllo umano prima di modificare.** Solo dopo il confronto semantico e la verifica di provenienza il coordinatore può decidere se una voce è duplicato confermato, variante intenzionale o contenuto da correggere. Il tool deve restare osservativo.
6. **Riproducibilità.** Rieseguire il tool sul checkout esatto, confrontare la matrice generata con quella tracciata e registrare commit, output e residui. Un controllo formale pulito non sostituisce la validazione del contenuto reale.

## Controlli G2

Il test strutturale G2 verifica che la matrice tracciata corrisponda al checkout corrente e che l’esito pulito resti esplicito: zero gruppi, hash byte-level distinti, hash normalizzati distinti, titoli distinti e nessun segnale associato ai file.

Comandi da eseguire nel worktree indicato:

```text
python -m unittest tests/coordination/test_uni_inventory_g1.py tests/coordination/test_uni_inventory_g2.py
python -m compileall -q tools/uni_inventory_g1.py
git diff --check
```

Il documento e il test sono gli unici artefatti aggiunti da questa review; nessun file sorgente del corpus è stato cancellato o fuso.
