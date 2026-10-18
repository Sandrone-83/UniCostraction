# UNI QA / Provenance - G4 guardia contro chiavi esame pubbliche

Data: 2026-10-18

Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`

Branch: `codex/uni-qa-provenance`

Base richiesta: `3a7ce72cf47da31c8efe730eda217017ea862880`

## Obiettivo

G4 aggiunge `tests/coordination/test_public_exam_key_guard_g4.py`, un controllo
negativo di repository per evitare che materiale pubblico tracciato esponga
strutture di chiave d'esame, punteggio o risposta corretta.

Il perimetro è scoperto tramite `git ls-files` e comprende:

- ogni file tracciato sotto `UNIVERSITA_EDILIZIA/ESAMI/`;
- ogni file tracciato il cui nome contiene `manifest`, quindi anche i manifest
  dei pack e `PUBLIC_EXAM_FIXTURE_MANIFEST_G3.json`.

Il test non contiene risposte attese, lettere corrette, testo di opzioni,
punteggi attesi o fixture di chiavi. Controlla solo nomi di campi strutturati
e forme di dati: campi come `answer`, `risposta_corretta`, `lettera`,
`score`/`punteggio` e mappe numeriche domanda-valore senza etichetta.

## Marker documentali leciti

Il rilevamento richiede una forma di campo (`:`/`=` o cella delimitata), non la
semplice presenza di una parola. Restano quindi leciti gli avvisi documentali
come `Risposte NON presenti`, `chiave fuori repository`, le righe sulle chiavi
esterne e le frasi delle domande che usano `corretta`. Il test include casi
espliciti per verificare questa distinzione.

Non viene trattato come fuga il testo libero di una domanda o di un'opzione,
né il termine generico `chiave`/`chiavi`: questi elementi descrivono il
protocollo pubblico e non sono, da soli, un payload di correzione.

## Verifiche e significato

Il controllo ha dato esito positivo sul materiale tracciato del checkout e
protegge il confine del repository contro nuovi campi o strutture riconoscibili
come chiavi/punteggi. È una garanzia strutturale e negativa, non un correttore.

Limiti dichiarati:

- non rileva una risposta corretta mascherata nel testo libero, nelle opzioni,
  in codifiche non riconosciute o tramite semantica equivalente;
- una mappa numerica domanda-valore viene trattata in modo conservativo come
  struttura sospetta, senza interpretare il valore né confrontarlo con una
  risposta attesa;
- non valuta correttezza didattica, fattuale, normativa o professionale delle
  domande, delle opzioni o dei materiali;
- non verifica completezza o accuratezza della chiave esterna
  `ESAMI_RISPOSTE/`, che deve rimanere fuori repository;
- `compileall`, test unitari e `git diff --check` non costituiscono un esame
  superato né una validazione educativa.

## Comandi previsti

```text
python -m unittest tests\coordination\test_exam_separation_g1.py tests\coordination\test_exam_separation_g2.py tests\coordination\test_exam_provenance_g3.py tests\coordination\test_public_exam_key_guard_g4.py
python -m compileall -q tests
git diff --check
```
