# UniCostraction — gate release-readiness inventario G7-A

Stato gate: **BLOCKED**  
Release-ready: **no**  
Stato revisione: **pending**  
Mismatch espliciti: **0**

<!-- G7-A gate: status=blocked; release_ready=false; pending=6; unmatched_legacy=2 -->

## Snapshot strutturale osservato

| Indicatore | Valore |
| --- | ---: |
| Pack osservati | 71 |
| Righe JSONL `schede` osservate | 963 |
| Esami osservati | 73 |
| Coppie esame-pack osservate | 73 |
| Item G5 in coda | 6 |
| Item G5 pending | 6 |
| Esami legacy unmatched | 2 |

## Gate

Il gate confronta il filesystem ricalcolato con i JSON G6/G5 tracciati e con i
marker numerici nella documentazione. Un mismatch non viene nascosto: è
riportato nel campo `mismatches` del JSON con percorso, atteso e osservato.

Condizioni correnti:

- pending_human_review: 6 G5 item remain pending
- unmatched_legacy: 2 legacy exam remain unmatched

I 6 item G5 restano `pending` e i 2 esami legacy restano `unmatched`. Il gate
non assegna associazioni canoniche, non chiude la coda e non legge né modifica
contenuto didattico.

Per rigenerare il report dal checkout selezionato:

```powershell
python tools/uni_release_readiness_g7.py
```
