# UniCostraction QA full checkout — G16-C

G16-C estende il full-checkout guard ai workflow umani per la review dei
template/import-export e dei report pack/source.

## Contratto congelato

- `UNI_TEMPLATE_IMPORT_EXPORT_REVIEW_G16.json`: 2 record `pending`, uno per
  template e uno per import/export;
- `UNI_REPORT_PACK_SOURCE_REVIEW_G16.json`: 2 record `pending`, uno per report
  pack e uno per source;
- ogni record dichiara `state`, `evidence_ref`, `reviewer`, `rationale` e
  `decision`;
- nei canonici iniziali `decision` è esplicitamente `null`;
- una decisione non nulla richiede stato `resolved`, evidenza, reviewer e
  rationale non vuoti.

Il guard controlla anche che gli stati appartengano all'elenco dichiarato e
che le cardinalità restino stabili. Un riferimento di evidenza è un puntatore
di workflow: non dimostra da solo correttezza, licenza, conformità o validità
professionale.

## Protezione del checkout pubblico

Restano attivi i blocchi contro i campi strutturati `answer_key`, `response`,
`grade`, `solution`, `score`, `correct option` e contro le mappe numeriche
domanda-valore. I canonici G16 sono metadata-only e non contengono materiale
di soluzione o valutazione.

## Gate locale

```text
py -3 -m unittest tests\coordination\test_exam_separation_g1.py ... tests\coordination\test_human_workflow_guard_g16.py
py -3 -m compileall -q tools tests
git diff --check
```
