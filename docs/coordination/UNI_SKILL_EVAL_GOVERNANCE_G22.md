# UniCostraction skill evaluation governance — G22

Data: 2026-10-19
Worktree QA: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`

## Scopo

G22 estende il gate G20 dal solo envelope eval al contratto pubblicato
manifest/evals. Il controllo resta deterministico, locale e fail-closed: un
campo mancante, sconosciuto, vuoto, duplicato o incoerente produce findings e
un esito non valido.

Il gate è QA strutturale e di provenienza dichiarata. Non dimostra correttezza
fattuale, educativa, tecnica, normativa, professionale o legale; non approva
fonti, licenze, certificazioni, calcoli o output del modello. I limiti
professionali richiedono revisione umana qualificata e, quando necessario,
l'autorità o il professionista competente.

## Manifest pubblicato

Quando è presente il formato pubblicato, `manifest.json` deve avere esattamente
questi campi top-level:

```json
{
  "library": "UniCostraction/AuraTrix-AulaFIX",
  "version": "0.4.0",
  "generated_at": "2026-10-19",
  "rights_policy": "Original summaries only; verify rights and limits before use.",
  "skills": []
}
```

`library`, `version` e `rights_policy` sono stringhe non vuote;
`generated_at` è una data `YYYY-MM-DD`; `skills` è una lista non vuota. Ogni
entry richiede esattamente:

`id`, `path`, `title`, `domain`, `scope`, `source_refs`, `rights_state`.

Gli ID sono slug minuscoli con trattini e il path è esattamente
`<skill-id>/SKILL.md`. `source_refs` è una lista non vuota con oggetti che
richiedono `url`, `authority`, `purpose` e `rights_state`, tutti non vuoti.
Questi sono metadati di tracciabilità e diritti dichiarati, non una verifica
esterna della fonte o della licenza.

## Evals pubblicati

`evals/evals.json` mantiene lo schema pubblicato
`g19-skill-library-evals-1`, anche per il lotto G22. L'envelope ha esattamente:

- `schema_version` con il valore esatto pubblicato;
- `library` non vuoto e coerente con `manifest.json.library` quando presente;
- `milestone` nel formato `G<number>`; la fixture G22 usa `G22`;
- `purpose` non vuoto;
- `rights_and_safety` con `content_origin`, `source_policy`, `evaluation_limit` ed `escalation_policy`, tutti non vuoti;
- `cases`, lista non vuota.

Ogni case richiede `case_id`, `skill_id`, `prompt`, `expected_behavior`,
`required_boundaries`, `evidence_expectation` e `grading_rubric`. Le liste sono
non vuote e composte da stringhe non vuote; la rubrica contiene esattamente
`score_0`, `score_2`, `score_4`. `required_boundaries` deve esprimere un limite
professionale, un divieto di certificazione o un'escalation.

## Copertura e anti-answer-key

Ogni skill del manifest ha esattamente un case, ogni case punta a un ID del
manifest e ogni `case_id` è unico. Il controllo ricorsivo answer-key si applica
sia al manifest sia all'envelope eval, includendo liste e oggetti annidati.
Campi come `answer`, `answer_key`, `correct_answer`, `expected_answer`,
`gold_answer`, `reference_answer`, `solution` e `target_answer` sono proibiti.

I fixture legacy continuano a supportare `negative_case` e
`negative_case_markers` con whitelist esplicita. Il formato pubblicato non può
mischiare campi legacy.

## Compatibilità G19 e limiti del runner

`tools/run_skill_library_qa_g19.py` non viene modificato. Continua a validare il
mapping filesystem-manifest e a segnalare in modo fail-closed skill `SKILL.md`
non indicizzate, entry mancanti o path inesistenti. G22 aggiunge controlli al
validator evals senza sostituire il gate Markdown G18/G19.

Comandi:

```text
python tools\run_skill_library_qa_g19.py <skill-library>
python tools\validate_skill_evals_g20.py <skill-library>
python -m unittest tests\coordination\test_skill_evals_contract_g20.py
python -m unittest tests\coordination\test_skill_library_qa_runner_g19.py
git diff --check
```

Il nuovo lotto G22 è rappresentato nei test con fixture in-memory; nessun
corpus o inventory viene modificato da questo worktree QA.
