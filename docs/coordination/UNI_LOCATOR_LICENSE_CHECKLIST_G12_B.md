# G12-B — checklist locator/licenza senza promozione

Il report machine-readable è [UNI_LOCATOR_LICENSE_CHECKLIST_G12_B.json](./UNI_LOCATOR_LICENSE_CHECKLIST_G12_B.json), con schema [UNI_LOCATOR_LICENSE_CHECKLIST_G12_B_SCHEMA.json](./UNI_LOCATOR_LICENSE_CHECKLIST_G12_B_SCHEMA.json). È stato costruito a partire dal commit G11 `5609b4eb965e4b45d4520a563f2403b1f9fce980` e considera esclusivamente i due elementi `source_records` dei manifest G5 e G10.

Il controllo è metadata-only: non modifica manifest, fonti, XML, HTML, PDF, schede, esami o contenuti. Non copia payload e non autorizza estrazione, riproduzione, riuso commerciale, interpretazione normativa o pubblicazione di claim.

## Semantica dei cinque campi

- `locator_reachable_observed` distingue `observed_live` (locator raggiunto e osservato), `observed_local` (locator dichiarato e osservato nei metadata locali) e `blocked` (prova insufficiente). Il controllo live è conservato separatamente in `live_check`.
- `official_context_observed` registra il contesto ufficiale osservato, ma il contesto non equivale a licenza.
- `license_source_specific` è `observed_local` per la dichiarazione locale associata a OSHA-1926, ma senza clearance indipendente; per la Direttiva UE è `blocked` perché il contesto EUR-Lex non è una licenza source-specific.
- `legal_clearance_required.required` è `true` per entrambi: la checklist non è un parere legale.
- `claim_ready` è `false` per entrambi e lo schema vieta la promozione a `true` in questo tranche.

## Esito sui due record

| source_record | locator | contesto ufficiale | licenza source-specific | clearance legale | claim-ready |
| --- | --- | --- | --- | --- | --- |
| `G5-001` — 29 CFR Part 1926 | `observed_local` / live `blocked` | `observed_local` / live `blocked` | `observed_local` | richiesta | `false` |
| `G10-B-001` — Direttiva (UE) 2024/1275 | `observed_live` | `observed_live` | `blocked` | richiesta | `false` |

Per eCFR il controllo live dell'URL esatto non ha prodotto una prova completa perché la risposta ha superato il limite di fetch; è quindi mantenuto `observed_local` e non viene promosso. Per EUR-Lex l'ELI e la pagina di contesto sono stati raggiunti live, ma la pagina di riuso e la Decisione 2011/833/UE restano contesto generale: non sono una licenza source-specific per il singolo atto.

## Riproducibilità e limiti

Ricostruzione deterministica del report:

```text
python tools/build_locator_license_checklist_g12_b.py
```

La verifica live è stata osservata il `2026-10-18` e serializzata come evidenza nel report; il generatore non effettua rete. Se una futura verifica non è disponibile, deve mantenere `blocked` nel controllo live e/o `observed_local` nel dato locale, senza introdurre uno stato `verified` o impostare `claim_ready=true`.
