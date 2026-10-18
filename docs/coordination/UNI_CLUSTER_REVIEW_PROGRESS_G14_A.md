# UniCostraction — registro avanzamento review cluster G14-A

Questo registro accompagna `UNI_CLUSTER_REVIEW_PACKET_G13_A.json` e non lo modifica.
Copre 85 cluster in 9 lotti.
Lo stato iniziale è `open` per ogni cluster; i tre campi di audit sono placeholder `null`.

## Stati e gate

- `open`: nessun audit field valorizzato; il cluster è ancora in coda.
- `in_review`: `reviewer` e `rationale` non vuoti; `evidence_ref` può restare `null` durante il lavoro.
- `decided`: `evidence_ref`, `reviewer` e `rationale` non vuoti; senza evidenza il cluster non si può chiudere.

Il validatore applica il gate a ogni record, quindi non è possibile chiudere nemmeno un cluster — e a maggior ragione più di uno — senza `evidence_ref`.
Le decisioni restano esiti di review umana: non sono comandi per modificare, fondere, rigettare o cancellare card ed esami.

## Avanzamento iniziale

| Lotto | Cluster | Open | In review | Decided |
| --- | ---: | ---: | ---: | ---: |
| `batch-01` | 10 | 10 | 0 | 0 |
| `batch-02` | 10 | 10 | 0 | 0 |
| `batch-03` | 10 | 10 | 0 | 0 |
| `batch-04` | 10 | 10 | 0 | 0 |
| `batch-05` | 10 | 10 | 0 | 0 |
| `batch-06` | 10 | 10 | 0 | 0 |
| `batch-07` | 10 | 10 | 0 | 0 |
| `batch-08` | 10 | 10 | 0 | 0 |
| `batch-09` | 5 | 5 | 0 | 0 |

## Rigenerazione

```powershell
python tools/uni_cluster_review_progress_g14_a.py
```

Il comando legge soltanto il packet G13 e scrive il registro G14 e questa guida.
