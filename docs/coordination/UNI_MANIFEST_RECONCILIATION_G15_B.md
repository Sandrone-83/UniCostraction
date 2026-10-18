# G15-B — riconciliazione manifest e report G5-G14

Il report [UNI_MANIFEST_RECONCILIATION_G15_B.json](./UNI_MANIFEST_RECONCILIATION_G15_B.json) è un indice deterministico e metadata-only del checkout `codex/uni-corpus` al base commit `8567297743ea5e4c94c1c0b6a0f18c7886ebc6fc`.

## Esito del perimetro

| Dimensione | Esito |
| --- | ---: |
| Input attesi G5-G14 | 10 |
| Input presenti nel checkout | 9 |
| Input assente | G8 |
| Manifest inventariati | 5 |
| Record riconciliati | 34 |
| Gruppi alias esatti path+SHA-256 | 14 |
| Rappresentazioni in gruppi alias | 28 |
| Pack G13 riconciliati | 71 |
| Pack G14 bloccati | 70 |
| Record claim-ready | 0 |

G8 è marcato `missing_in_checkout`. Non viene importato da altri branch, ricostruito, dedotto o usato come prova sostitutiva.

## Regole di riconciliazione

- Ogni rappresentazione presente resta visibile. Un gruppo alias significa stesso `local_path` e stesso SHA-256 dichiarati nei report, non una decisione di deduplicazione.
- Il matching usa soltanto `record_key`, path manifest, identità path+hash e `manifest.scope.package` espliciti.
- Nomi di corso, titoli, argomenti, `COURSE.yaml fonti`, similarità testuale e corrispondenze presunte non sono basi ammissibili.
- Gli stati di licenza ed evidenza sono copiati dal report più specifico disponibile o mantenuti bloccati/non dichiarati. Il report non concede licenze, clearance, vigenza o stato claim-ready.
- I riferimenti di remediation collegano i record a G7/G9/G11/G12 e i pack a G13/G14; non chiudono automaticamente alcun item.

## Campi principali

`record_reconciliation` contiene per record:

- chiave, manifest, tipo e report sorgente;
- `path_hash` con path locale, algoritmo, SHA-256 e identità composta;
- `package_scope` con valore dichiarato e base del dato;
- `license_status` ed `evidence_status`, inclusi i livelli G6/G9/G11/G12;
- gruppi alias e remediation collegata.

`pack_reconciliation` contiene per i 71 pack:

- scope manifest esatto, se presente;
- stato source-record, licenza ed evidenza osservato da G13;
- item e codici bloccanti G14, quando presenti.

## Rigenerazione e test

Dal root del worktree:

```powershell
python tools/reconcile_manifest_g15_b.py
python -m unittest tests/test_g15_b_manifest_reconciliation.py
```

La generazione non legge payload di fonti, schede o esami e non esegue richieste di rete.

## Limiti

La riconciliazione non dimostra accuratezza tecnica, vigenza normativa, raggiungibilità corrente degli URL, validità della licenza, clearance legale o correttezza didattica. Queste verifiche restano gate separati e gli stati bloccati/aperti rimangono tali.
