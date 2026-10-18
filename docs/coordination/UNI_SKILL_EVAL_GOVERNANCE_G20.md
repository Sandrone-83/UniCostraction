# UniCostraction skill evaluation governance — G20

Data: 2026-10-18
Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`

## Scopo

G20 aggiunge un gate strutturale deterministico per `evals/evals.json`. Il
validator confronta gli evaluation case con gli ID dichiarati in
`manifest.json`; non modifica i dati e non esegue richieste di rete.

Il risultato è esclusivamente QA della forma e dei metadati. Un passaggio G20
non dimostra correttezza fattuale, educativa, tecnica, normativa, professionale
o legale; non dimostra che l'evidenza sia autorevole o attuale; non esegue il
modello e non valuta le sue risposte.

## Layout e contratto

La root passata a `tools/validate_skill_evals_g20.py` contiene:

```text
<skill-library>/
  manifest.json
  evals/evals.json
```

`manifest.json` deve esporre una lista non vuota `skills`, con un campo `id`
per ogni entry. Il validator usa gli ID validi come insieme di riferimento e
segnala duplicati nel manifest. La validazione completa del manifest e delle
skill resta responsabilità dei validator G17/G18 esistenti.

`evals/evals.json` è una lista non vuota. Ogni elemento è esattamente un
oggetto con questi campi:

```json
{
  "case_id": "case-cila-basics",
  "skill_id": "skill-cila-basics",
  "prompt": "Review the supplied context and identify the next safe handoff.",
  "boundary": "Do not present the draft as legal or professional advice; require human review.",
  "evidence": ["SRC-EXAMPLE-001"],
  "rubric": ["Names missing context", "Records a review handoff"],
  "negative_case": true,
  "negative_case_markers": ["missing-context"]
}
```

`case_id`, `skill_id`, `prompt` e `boundary` sono stringhe non vuote; gli ID
sono slug minuscoli con trattini. `evidence` e `rubric` sono liste non vuote
di stringhe non vuote. Il validator non interpreta il contenuto delle fonti,
del boundary o della rubrica.

Ogni skill dichiarata nel manifest deve avere esattamente un case e ogni case
deve riferirsi a una skill dichiarata: quindi il numero dei case deve coincidere
con il numero degli ID del manifest. I `case_id` devono essere unici.

## Confini e negative case

`negative_case` è obbligatorio e deve essere booleano. Se vale `true`,
`negative_case_markers` deve contenere almeno un marker distinto scelto da
questa whitelist:

`ambiguous-input`, `conflicting-evidence`, `missing-context`, `out-of-scope`,
`professional-review-required`, `unsafe-automation`.

Se `negative_case` vale `false`, la lista dei marker deve essere vuota. Il
validator rifiuta marker non riconosciuti e duplicati: questo impedisce che un
case negativo introduca etichette arbitrarie o apparentemente sicure senza
una decisione contrattuale esplicita.

## Separazione dall'answer key

Non sono ammessi campi answer-key, né al livello del case né dentro liste o
oggetti annidati. Il controllo intercetta, tra gli altri, `answer`,
`answer_key`, `correct_answer`, `expected_answer`, `gold_answer`,
`reference_answer`, `solution` e `target_answer`, anche con maiuscole o
trattini/spazi equivalenti. La rubrica deve restare una lista di criteri
osservabili, non una soluzione attesa.

## Comandi di QA

```text
python tools\validate_skill_evals_g20.py <skill-library>
python -m unittest tests\coordination\test_skill_evals_contract_g20.py
python -m compileall -q tools\validate_skill_evals_g20.py tests\coordination\test_skill_evals_contract_g20.py
git diff --check
```

I test G20 usano fixture in memoria e non creano directory temporanee. Un
errore di percorso, encoding, JSON duplicato, campo mancante o contratto
violato produce findings ordinati e un exit code diverso da zero.
