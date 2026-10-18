# G11-B — matrice evidence/licenza

La matrice [UNI_EVIDENCE_LICENSE_MATRIX_G11_B.json](./UNI_EVIDENCE_LICENSE_MATRIX_G11_B.json) è un indice deterministico e metadata-only dei due manifest che espongono il campo `source_records` nel checkout di G11-B:

- `docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json` (`G5-001`)
- `docs/coordination/UNI_CORPUS_LOTTO_G10_B.json` (`G10-B-001`)

Il report non apre né copia XML, HTML, PDF, testo di fonte, schede o contenuti d'esame. I record con chiave `records` dell'audit G6 non vengono reinterpretati come `source_records`; il loro audit resta il riferimento storico separato.

## Semantica degli stati

`observed_local` significa che il dato è dichiarato e osservabile nei file locali, nei registri o nei manifest del checkout. Non significa che l'URL sia stato raggiunto in rete, che la versione esterna sia corrente o che esista una clearance legale indipendente.

`blocked` significa che manca una prova sufficiente per il passaggio successivo. In particolare, in questo run non sono state eseguite verifiche live: la matrice non emette stati più forti di `observed_local` e conserva un `blocker` per ogni riga.

## Risultato G11-B

| source_record | locator | contesto ufficiale | licenza | evidence | claim-ready | blocker |
| --- | --- | --- | --- | --- | --- | --- |
| `G5-001` — 29 CFR Part 1926 | `observed_local` | `observed_local` | `observed_local` | `observed_local` | `false` | URL/termini correnti/clearance legale non verificati live |
| `G10-B-001` — Direttiva (UE) 2024/1275 | `observed_local` | `observed_local` | `blocked` | `blocked` | `false` | il contesto EUR-Lex non è una licenza source-specific; nessuna promozione a claim-ready |

La Direttiva (UE) 2024/1275 è inclusa come record ufficiale metadata-only. Non sono stati aggiunti testo, soglie, scadenze, interpretazioni normative o una licenza inventata. La pagina ELI, la pagina di contesto EUR-Lex e il riferimento alla Decisione 2011/833/UE sono soltanto locator/contesto registrati, non prova di licenza specifica per l'atto.

La data `2026-10-18` è la data di osservazione del checkout. Non è una data di verifica live o di validità normativa.

## Riproducibilità e limiti

Il report è ricostruibile con:

```text
python tools/build_evidence_license_matrix_g11_b.py
```

Il generatore ordina le righe per percorso manifest e `source_record_id`, usa esclusivamente i due manifest dichiarati nello schema e non effettua richieste di rete. La matrice non autorizza estrazione, riproduzione, riuso commerciale, interpretazione normativa o pubblicazione di claim.
