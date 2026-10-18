# UNI QA full-checkout guard — G13-C

Il comando `python tools/validate_full_checkout_g13.py` scansiona il checkout
Git completo nei domini `UNIVERSITA_EDILIZIA/ESAMI`, `docs/coordination` e nei
file testuali identificati come manifest, audit o ledger.

Controlla la separazione della chiave protetta, l'assenza di strutture
answer-key/response/grade/solution/score/correct-option, le mappe numeriche
domanda-valore, l'integrità SHA-256 del manifest pubblico e la coerenza di
limiti, stati ed `evidence_ref`. Le fixture negative del test usano soltanto
`None` e `placeholder`.

Il risultato è strutturale e metadata-only: non legge né ricostruisce la
answer key e non dimostra correttezza didattica, fattuale, normativa, legale,
professionale o semantica.
