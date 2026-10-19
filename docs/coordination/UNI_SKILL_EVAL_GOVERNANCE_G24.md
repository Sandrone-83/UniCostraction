# UniCostraction skill evaluation governance — G24

Data: 2026-10-19
Worktree QA: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`

## Scopo

G24 estende il controllo QA del manifest e dell'envelope eval pubblicato senza
modificare corpus o inventory. Il gate resta deterministico e fail-closed:
metadati mancanti, campi sconosciuti, date impossibili, path duplicati, case
non coperti, provenance incompleta o answer-key producono findings.

Il controllo riguarda forma, tracciabilità dichiarata e limiti espliciti. Non
certifica correttezza fattuale, educativa, tecnica, normativa, professionale o
legale; non approva fonti o licenze; non sostituisce professionisti, autorità,
revisori o approvazioni di progetto.

## Manifest pubblicato

Il formato pubblicato mantiene i cinque campi top-level:

```json
{
  "library": "UniCostraction/AuraTrix-AulaFIX",
  "version": "0.4.0",
  "generated_at": "2026-10-19",
  "rights_policy": "Original summaries only; verify rights and limits before use.",
  "skills": []
}
```

`library`, `version` e `rights_policy` sono stringhe non vuote; `generated_at`
è una data di calendario `YYYY-MM-DD`; `skills` è una lista non vuota. Ogni
entry richiede esattamente `id`, `path`, `title`, `domain`, `scope`,
`source_refs` e `rights_state`. Gli ID sono slug minuscoli, il path è
`<skill-id>/SKILL.md` e i path devono essere unici.

Ogni `source_refs` è una lista non vuota di oggetti con esattamente `url`,
`authority`, `purpose` e `rights_state`, tutti non vuoti. Questi campi
registrano la provenienza dichiarata e la policy d'uso; non rendono la fonte
automaticamente autorevole, corrente o redistribuibile.

## Envelope eval attuale e lotto G24

`evals/evals.json` usa lo schema pubblicato `g19-skill-library-evals-1`,
anche per il lotto G24. L'envelope richiede esattamente:

- `schema_version` con il valore pubblicato;
- `library` non vuoto e uguale a `manifest.json.library` quando presente;
- `milestone` nel formato `G<number>`; le fixture G24 usano `G24`;
- `purpose` non vuoto;
- `rights_and_safety` con `content_origin`, `source_policy`, `evaluation_limit` ed `escalation_policy`, tutti non vuoti;
- `cases`, lista non vuota.

Ogni case richiede `case_id`, `skill_id`, `prompt`, `expected_behavior`,
`required_boundaries`, `evidence_expectation` e `grading_rubric`. Le liste sono
non vuote e composte da stringhe non vuote; `grading_rubric` contiene
esattamente `score_0`, `score_2` e `score_4`. I `case_id` e `skill_id` sono slug
minuscoli; `required_boundaries` deve esprimere un limite professionale,
un divieto di certificazione o un'escalation.

## One-to-one, anti-answer-key e limiti

Ogni skill manifest ha esattamente un case, ogni case punta a una skill
manifest e ogni `case_id` è unico. Il controllo answer-key è ricorsivo sul
manifest e sull'envelope eval, inclusi oggetti e liste annidati. Sono proibiti
`answer`, `answer_key`, `correct_answer`, `expected_answer`, `gold_answer`,
`reference_answer`, `solution` e `target_answer`.

I fixture legacy restano compatibili con `negative_case` e
`negative_case_markers`, ma i marker sono limitati alla whitelist esistente e
il formato pubblicato non può mischiare campi legacy. Provenance, rights policy
evaluation limit non sono una licenza, una certificazione o un parere
professionale.

## Runner G19

`tools/run_skill_library_qa_g19.py` non viene modificato. Il runner continua a
verificare il mapping filesystem-manifest e a fallire quando una skill è
mancante, extra o non indicizzata. Il validator evals G20/G24 aggiunge i gate
manifest/evals senza sostituire la verifica Markdown G18/G19. Il selettore `--milestone G24` è opzionale e rende esplicita la verifica del lotto; senza selettore restano compatibili gli envelope G19+ già pubblicati.

```text
python tools\run_skill_library_qa_g19.py <skill-library>
python tools\validate_skill_evals_g20.py --milestone G24 <skill-library>
python -m unittest tests\coordination\test_skill_evals_contract_g20.py
python -m unittest tests\coordination\test_skill_library_qa_runner_g19.py
git diff --check
```

Le fixture G24 sono in-memory; il worktree QA non scrive nel corpus o
nell'inventory.
