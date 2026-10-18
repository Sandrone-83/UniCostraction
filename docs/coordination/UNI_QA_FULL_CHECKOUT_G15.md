# UNI QA full checkout — G15-C

G15-C estende il guard full-checkout G13-C con un controllo deterministico
dell'inventario tracciato, la verifica completa dei path e degli SHA-256 dei
manifest pubblici e uno snapshot dei conteggi/stati dei report G10-G14.

## Contratto congelato

- perimetro `UNIVERSITA_EDILIZIA/ESAMI/`: 76 file testuali, di cui 73
  payload `domande.md`;
- `PUBLIC_EXAM_FIXTURE_MANIFEST_G3.json`: 73 path POSIX relativi, tracciati,
  ordinati, univoci, con digest SHA-256 verificato;
- G10: entrambi gli audit dichiarano 76 file e 76 file testuali, con i due
  stati di audit in `pending`;
- G11: candidate-review `1/pending`, priority queue `1/open`,
  evidence/licence matrix `1/pending`;
- G12: decision records `1/pending`, source/licence checklist `2/pending`;
- G14: cluster progress `2` con `blocked/open`, per-pack queue `2` con
  `blocked/open`.

L'ordine dei path tracciati e delle liste di stato è stabile e viene
controllato a ogni scansione. Un report mancante, non tracciato, con JSON
invalido, stato non dichiarato o cardinalità diversa produce un finding.

## Fixture e limiti

Le fixture negative G15-C usano soltanto `None` e `placeholder`. Restano
attivi i blocchi contro i campi strutturati `answer_key`, `response`, `grade`,
`solution`, `score`, `correct option` e contro le mappe numeriche domanda-valore.
Il guard non legge né ricostruisce la chiave protetta e non dimostra
correttezza didattica, fattuale, normativa, legale, professionale o semantica.

## Gate locale

```text
py -3 -m unittest tests\coordination\test_exam_separation_g1.py ... tests\coordination\test_full_checkout_qa_g15.py
py -3 -m compileall -q tools tests
git diff --check
```
