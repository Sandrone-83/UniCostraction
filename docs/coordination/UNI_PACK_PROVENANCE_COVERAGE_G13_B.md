# G13-B — coverage provenance dei pack

Il report machine-readable è [UNI_PACK_PROVENANCE_COVERAGE_G13_B.json](./UNI_PACK_PROVENANCE_COVERAGE_G13_B.json), con schema [UNI_PACK_PROVENANCE_COVERAGE_G13_B_SCHEMA.json](./UNI_PACK_PROVENANCE_COVERAGE_G13_B_SCHEMA.json). L’audit parte dal commit G12 `5563510cbf40c1e2a5476cb64be845947c68e710` e osserva i 71 `UNIVERSITA_EDILIZIA/**/COURSE.yaml` insieme ai record dei cinque manifest locali elencati nel report.

## Regola di confronto

Il collegamento pack→manifest è ammesso soltanto quando un metadata locale esplicito identifica il percorso del pack: `scope.package` esatto, `scope.source_path` sotto il pack oppure `locator.path`/`source.local_path` sotto il pack. Il campo `fonti`, il nome del corso, i titoli dei documenti, gli argomenti e la similitudine testuale non sono usati per inferire fonti.

L’audit è metadata-only. Non esegue richieste live, non legge o copia payload di PDF/XML/HTML/schede/esami e non promuove alcuno stato a `verified`. Tutte le lacune restano `blocked`; le sole osservazioni locali ammesse sono `observed_local`.

## Esito

| dimensione | `observed_local` | `blocked` |
| --- | ---: | ---: |
| `source_record_present` | 1 | 70 |
| `locator_present` | 1 | 70 |
| `license_status` | 0 | 71 |
| `evidence_status` | 0 | 71 |

Un solo pack ha una relazione esplicita: `ENERGETICA_INCENTIVI_PACK`, con i due record del manifest G3. Il locator è presente nei metadata locali, ma la licenza è `not_declared` e gli stati di verifica dei record sono `blocked`/`context_only`; quindi anche l’evidence del pack resta `blocked` e la remediation è richiesta.

Gli altri 70 pack non hanno un record associato da un percorso esplicito. Anche se alcuni `COURSE.yaml` dichiarano un campo `fonti`, questa dichiarazione non viene trasformata in un collegamento a un manifest: per ciascuno restano `source_record_present`, `locator_present`, `license_status` ed `evidence_status` a `blocked`.

## Riproducibilità

```text
python tools/audit_pack_provenance_g13_b.py
python -m unittest tests/test_g13_b_pack_provenance_coverage.py
```

Il report registra la copertura metadata disponibile nel checkout al `2026-10-18`. Non costituisce clearance legale, verifica di vigenza, prova di accuratezza dei contenuti o autorizzazione di riuso.
