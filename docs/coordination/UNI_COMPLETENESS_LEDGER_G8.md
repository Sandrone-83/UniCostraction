# UniCostraction — ledger evidenza completezza G8-A

Il report deterministico è [`UNI_COMPLETENESS_LEDGER_G8.json`](UNI_COMPLETENESS_LEDGER_G8.json) ed è accompagnato dallo schema [`UNI_COMPLETENESS_LEDGER_G8.schema.json`](UNI_COMPLETENESS_LEDGER_G8.schema.json). Si rigenera dal checkout selezionato con:

```powershell
python tools/uni_completeness_ledger_g8.py
```

## Snapshot osservato

| Indicatore | Valore |
| --- | ---: |
| Pack | 71 |
| Righe JSONL `schede` | 963 |
| Esami | 73 |
| Coppie esame-pack | 73 |
| G5 pending | 6 |
| Esami legacy unmatched | 2 |

Ogni record `pack:*` e `exam:*` elenca i `source_files` osservati e un
`dashboard_reference` con i percorsi dei conteggi nel dashboard G6 e i valori
osservati. `evidence_present` descrive evidenza strutturale presente; non è una
certificazione didattica, normativa, legale o semantica.

| Tipo | `evidence_present` | `human_review_required` |
| --- | ---: | ---: |
| Pack | 69 | 2 |
| Esame | 69 | 4 |

La coda G5 resta aperta: i 6 item sono ancora `pending` e
i 2 esami legacy restano unmatched. Il ledger
non assegna associazioni canoniche e non chiude alcun item.

## Confini

- alias, ambiguità e unmatched restano classificazioni osservate;
- nessun contenuto didattico viene letto per inferire associazioni;
- nessun file di domande, risposte, schede o decisione di revisione viene modificato;
- il ledger indica dove guardare e cosa il dashboard conta, non sostituisce la revisione umana.
