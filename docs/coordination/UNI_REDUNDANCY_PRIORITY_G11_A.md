# UniCostraction — coda prioritaria anti-ridondanza G11-A

## Scopo e risultato

Il tool [`uni_redundancy_priority_g11_a.py`](../../tools/uni_redundancy_priority_g11_a.py)
legge il report G10-A e costruisce una coda deterministica per la revisione
umana dei suoi `candidate_review`. L'output machine-readable è
[`UNI_REDUNDANCY_PRIORITY_G11_A.json`](UNI_REDUNDANCY_PRIORITY_G11_A.json),
con contratto in
[`UNI_REDUNDANCY_PRIORITY_G11_A.schema.json`](UNI_REDUNDANCY_PRIORITY_G11_A.schema.json).

La relazione non viene ricalcolata: ogni pair già presente in
`results.candidate_review` è un arco e i gruppi sono esclusivamente le sue
componenti connesse. Per lo snapshot G10 sono attesi 303 pair; la coda li
conserva tutti, una sola volta, dentro i rispettivi componenti.

## Priorità trasparente

Ogni componente contiene `priority_key`, `priority_rank`, il conteggio dei
pair e la copertura dei contenitori sorgente. `collision_count` significa
numero di pair `candidate_review` conservati nel componente: non è un
conteggio di duplicati esatti e non autorizza alcuna fusione.

La coda è ordinata con questa chiave, in modo decrescente dove indicato:

1. `collision_count` desc — più pair collegati, maggiore urgenza di revisione;
2. `coverage_count` desc — `pack_count + exam_count`;
3. `pack_count` desc;
4. `exam_count` desc;
5. `node_count` desc;
6. `source_group` asc;
7. `component_id` asc come spareggio stabile.

Per le card, `pack_paths` identifica i pack distinti; per gli esami,
`exam_paths` identifica i file d'esame distinti. I conteggi sono derivati dai
metadati G10 (`source_path`, `source_group`, `unit_id`), senza copiare corpi di
domande o contenuti di schede.

## Revisione umana e confini

Ogni componente dichiara `human_review.required: true` e lascia
`human_review.decision` a `null`. Il report conserva i record originali dei
pair — inclusi metrica, score, soglia e identificativi — per consentire una
revisione tracciabile. La decisione umana deve considerare provenienza, scopo
didattico e contenuto prima di qualunque azione successiva.

Il tool non legge chiavi di risposta, non deduplica, non cancella, non modifica
file sorgente e non copia testo didattico. Una componente connessa è solo una
unità organizzativa della coda, non una prova di equivalenza semantica,
didattica, fattuale, normativa o di licenza.

Rigenerazione:

```powershell
python tools/uni_redundancy_priority_g11_a.py
```
