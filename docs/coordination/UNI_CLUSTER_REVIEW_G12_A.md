# UniCostraction — contratto decisioni umane sui cluster G12-A

Questo contratto machine-readable prepara la revisione umana dei
**85 componenti** della coda G11-A.
Ogni componente ha una sola registrazione `review`; la decisione iniziale
è `null` e non implica alcuna fusione, rigetto o approvazione.

## Input e rigenerazione

- input: `docs/coordination/UNI_REDUNDANCY_PRIORITY_G11_A.json` (`g11a.v1`)
- componenti: **85**
- hash ID componenti: `b5467541d289c3773aca6ab982e7604459203be2f54ed93ecd9601f7ce47d234`

```powershell
python tools/uni_cluster_review_g12_a.py
```

## Campi della decisione

Ogni record contiene sempre `decision`, `evidence_ref`, `reviewer` e
`rationale`. I valori iniziali sono tutti `null` come placeholder di
revisione. Prima di registrare una decisione non-null, il revisore deve
compilare tutti e tre i campi di audit; `evidence_ref` deve puntare a
un'evidenza verificabile.

Decisioni ammesse: `distinct`, `merge_candidate`, `reject_candidate`,
`needs_source_review`.

## Confini

- la coda è a livello di componente connesso, non di singola risposta;
- non vengono lette, copiate o generate risposte d'esame;
- card ed esami restano immutati: il contratto non esegue azioni automatiche;
- `merge_candidate` e `reject_candidate` sono esiti di revisione, non comandi esecutivi;
- la decisione umana non certifica correttezza didattica, normativa, legale o fattuale.
