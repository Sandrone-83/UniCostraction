# UNI QA decision records — G12-C

Data: 2026-10-18

Il guard G12-C estende la scansione metadata-only ai decision records dei
cluster di ridondanza e alla checklist source/licence. Ogni record dichiara
stato, reviewer e rationale non vuoti. Una decisione non nulla richiede anche
un evidence_ref non vuoto; una decisione nulla può lasciare il riferimento a
`None` mentre il record resta in lavorazione.

## Contratto

Gli stati ammessi sono `blocked`, `pending`, `open` e `resolved`. I due
contratti dichiarano la separazione della chiave protetta: la answer key non è
pubblicata e non è rappresentata nei record o nelle checklist. Il guard blocca
campi strutturati per answer key, correct option, explanation, solution, score,
response e grade, oltre alle mappe numeriche domanda-valore.

## Limiti

Il controllo verifica soltanto forma, metadati, separazione e presenza di
puntatori. Non valuta duplicati semanticamente, correttezza didattica,
fattuale, normativa, legale o professionale, né dimostra che una fonte o una
licenza sia autorevole, corrente o commercialmente utilizzabile. Un
`evidence_ref` è un riferimento di review, non una prova del contenuto.

Le fixture negative usano esclusivamente `None` o `placeholder`: non includono
risposte, lettere di opzione, spiegazioni reali, soluzioni o punteggi.
