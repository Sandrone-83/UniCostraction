# UNI QA integrato — G11-C

Data: 2026-10-18

Il guard integrato estende il controllo metadata-only ai candidate-review
clusters, alle priority queues e alla matrice evidence/licenza. Ogni contratto
dichiara limiti, stati ammessi e separazione della chiave protetta; questi
artefatti non pubblicano materiale di correzione.

La scansione esplicita verifica i 73 payload pubblici `*/domande.md`,
comprendendo i due formati già coperti dal contratto precedente. Il conteggio,
i percorsi e gli hash sono metadati di integrità e non rappresentano risposte,
valutazioni o risultati.

## Limiti

Il controllo cerca soltanto strutture nominate e mappe numeriche domanda-valore.
Non valuta la correttezza didattica, fattuale, normativa, legale o professionale,
non revisiona il testo libero e non prova l'autorevolezza o l'utilizzabilità di
una fonte o licenza. Gli stati `pending`, `open`, `blocked` e `resolved` sono
stati di workflow; non sono esiti d'esame. La chiave protetta resta separata,
fuori dagli artefatti pubblici.

Le fixture negative usano esclusivamente `None` o `placeholder`: servono a
verificare la forma del divieto senza inserire risposte reali.
