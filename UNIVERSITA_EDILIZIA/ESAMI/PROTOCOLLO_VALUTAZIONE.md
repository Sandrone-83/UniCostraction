# Protocollo di valutazione AuraTrix — Esami di settore

Questo protocollo definisce come far sostenere a un LLM (o a una persona) gli esami
della repository e come valutarli in modo oggettivo. Le chiavi corrette non entrano
mai nella repository pubblica: vivono in `ESAMI_RISPOSTE/` (fuori repository, solo
macchina del proprietario).

## 1. Cosa serve

- `ESAMI/<SETTORE>/domande.md` — banca domande pubblica (70 settori al momento).
- `ESAMI_RISPOSTE/<SETTORE>_risposte.jsonl` — chiave riservata (NON committare mai).
- `ESAMI/RISPOSTE_CANDIDATO/` — cartella in cui il candidato consegna le risposte
  (creata dal correttore, esclusa da git tramite `.git/info/exclude`).

## 2. Amministrazione dell'esame

1. Consegna al candidato il file `ESAMI/<SETTORE>/domande.md` (solo quello).
2. Il candidato risponde con un file di testo, una domanda per riga, nel formato:

   ```
   1;A
   2;C
   3;B
   ```

   (numero della domanda, punto e virgola, lettera A/B/C/D — maiuscole o minuscole).
3. Salva il file come `ESAMI/RISPOSTE_CANDIDATO/<SETTORE>.txt`.

Per generare una scheda vuota pronta da compilare:

```
python UNIVERSITA_EDILIZIA/valuta_esami.py template <SETTORE>
python UNIVERSITA_EDILIZIA/valuta_esami.py template --tutti   # tutti i 70 settori
```

## 3. Correzione

```
python UNIVERSITA_EDILIZIA/valuta_esami.py valuta <SETTORE>
python UNIVERSITA_EDILIZIA/valuta_esami.py valuta --tutti
```

Il correttore:

- confronta ogni riga con la chiave riservata (campo `lettera`);
- scrive il verbale in `ESAMI/RISPOSTE_CANDIDATO/VERBALE_VALUTAZIONE.md`;
- per ogni settore riporta: domande sostenute, corrette, percentuale, giudizio;
- elenca **solo le domande sbagliate o mancanti**, con la lettera corretta e la
  fonte (pack/scheda) da ripassare — le risposte esatte delle domande corrette
  restano segrete;
- conclude con il giudizio complessivo e i settori da riprendere.

## 4. Giudizi

| Percentuale risposte corrette | Giudizio |
|---|---|
| ≥ 90% | Eccellente |
| 80-89% | Buono |
| 70-79% | Sufficiente |
| 50-69% | Insufficiente — ripassare le schede indicate |
| < 50% | Da rifare — gap sistemico sul settore |

Un settore si considera consolidato solo a «Eccellente» o «Buono» con errori
ricondotti a gap puntuali (stessa scheda fonte), non distribuiti.

## 5. Regole di riservatezza

- Le chiavi (`ESAMI_RISPOSTE/`) non vanno mai copiate, committate o pubblicate.
- I verbali contengono le risposte corrette **solo delle domande sbagliate**:
  restano comunque nella cartella candidato (locale), non in repository.
- Se un verbale deve circolare, diffondi solo la tabella dei giudizi, non il dettaglio.
