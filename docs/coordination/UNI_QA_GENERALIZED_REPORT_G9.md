# G9-C — Gate QA generalizzato

Questo report documenta un guard strutturale riutilizzabile per report,
manifest e ledger QA pubblici tracciati sotto `docs/coordination/` e `reports/`.
Il checker valida i contratti JSON e, per i formati testuali, intercetta campi
strutturati che potrebbero esporre `answer_key`, `response`, `grade` o
`solution`. Le mappe numeriche domanda-valore sono rilevate soltanto per forma.

## Contratto controllato

Ogni artefatto JSON nel perimetro deve dichiarare limiti espliciti e una lista
`allowed_states` composta da `blocked`, `pending`, `open` e `resolved` quando
questi sono gli stati del contratto. Gli stati eventualmente presenti negli
elenchi di `entries`, `artifacts`, `records`, `findings`, `checks` o `items`
devono appartenere a quella lista. Una voce `resolved` richiede un
`evidence_ref` non vuoto.

## Limiti

Il gate è strutturale: non prova correttezza fattuale, educativa, normativa,
legale, professionale o di pubblicazione. Un `evidence_ref` è soltanto una forma
di puntatore auditabile e non dimostra che la fonte sia aggiornata, completa,
autorevole o corretta. Il guard non interpreta il testo libero, le immagini,
gli asset binari o eventuale materiale di risposta dissimulato semanticamente.

Le fixture dei test sono sintetiche e usano soltanto `None` o `placeholder`;
non contengono risposte reali, lettere di opzione, spiegazioni, soluzioni,
valutazioni o punteggi.
