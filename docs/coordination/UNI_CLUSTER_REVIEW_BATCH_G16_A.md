# UniCostraction — workflow import/export review batch G16-A

G16-A accompagna i packet canonici G13 e G14 con una busta separata per un
solo lotto. Il workflow è metadata-only: esporta identificativi, priorità,
anchor e riferimenti osservati, ma non copia testo di esami o card.

## Export

```powershell
python tools/uni_cluster_review_batch_g16_a.py --root . export `
  --batch-id batch-01 `
  --output work/g16_batch-01.template.json
```

Il template nasce con `decision`, `evidence_ref`, `reviewer` e `rationale`
tutti a `null`. L'output deve restare un file di lavoro separato.

## Inserimento umano e import

La persona che revisiona può modificare solo `review`. Sono ammessi due stati:

- tutti e quattro i campi `null`, per lasciare il cluster in sospeso;
- una decisione G12 valida con `evidence_ref`, `reviewer` e `rationale` tutti
  presenti e non vuoti.

Una decisione con prova mancante, oppure una review parziale, viene rifiutata
prima della scrittura. Il comando confronta inoltre batch, cluster, riferimenti
e hash dei source report con i G13/G14 correnti.

```powershell
python tools/uni_cluster_review_batch_g16_a.py --root . import `
  --input work/g16_batch-01.review.json `
  --output work/g16_batch-01.imported.json
```

L'import produce una busta `mode=reviewed` separata. Non modifica
`UNI_CLUSTER_REVIEW_PACKET_G13_A.json`, `UNI_CLUSTER_REVIEW_PROGRESS_G14_A.json`,
card, esami o altri contenuti canonici. Una decisione è un esito di review, non
un comando di merge, reject, delete o riscrittura.

## Gate

La validazione applica lo stesso contratto a ogni entry: `decision=null` deve
avere gli altri tre campi `null`; una decisione non-null richiede i tre campi
completi. Le fixture del test usano soltanto identificativi e placeholder
sintetici `None`, senza testo d'esame.
