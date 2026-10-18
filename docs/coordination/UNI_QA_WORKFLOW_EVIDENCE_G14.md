# UNI QA workflow evidence — G14-C

Il full-checkout guard G13-C include i registri di avanzamento dei cluster e
la coda per-pack G14-C.

Ogni record G14-C dichiara uno stato in `allowed_states` e conserva
`evidence_ref`, `reviewer` e `rationale`. Gli stati `blocked` e `open` restano
non risolti: non possono portare una decisione o un flag di promozione positiva.
La transizione `resolved` richiede un riferimento di evidenza non vuoto.

Le fixture sono metadata-only e usano soltanto `None` o `placeholder` nei test
negativi. Il guard rifiuta strutture `answer_key`, `response`, `grade`,
`solution`, `score`, `correct option` e mappe numeriche domanda-valore.
Non legge né ricostruisce la chiave protetta e non dimostra correttezza
didattica, fattuale, normativa, legale, professionale o semantica.
