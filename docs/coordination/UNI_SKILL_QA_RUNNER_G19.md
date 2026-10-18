# UniCostraction Markdown Skill QA Runner — G19

Data: 2026-10-18
Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`

## Scopo

`tools/run_skill_library_qa_g19.py` è un piccolo adapter deterministico per il
validator Markdown G18. Riceve una directory di libreria, importa
`tools.validate_skill_markdown_g18`, invoca `validate_library` e stampa un solo
report JSON su una riga.

Il runner non modifica la libreria, non esegue richieste di rete e non include
nel report percorsi assoluti, timestamp o altri valori variabili.

## Report

Il contratto JSON contiene esattamente questi campi:

```json
{
  "count": 1,
  "exit_status": 0,
  "findings": []
}
```

- `count`: numero dei file `SKILL.md` scoperti dal catalogatore G18;
- `findings`: findings G18 deduplicati e ordinati lessicograficamente;
- `exit_status`: `0` se `findings` è vuoto, altrimenti `1`.

La serializzazione usa chiavi ordinate e separatori compatti. Il codice di
uscita del processo coincide con `exit_status`.

## Uso

```text
python tools\run_skill_library_qa_g19.py <skill-library>
```

Esempio di controllo mirato:

```text
python -m unittest tests\coordination\test_skill_library_qa_runner_g19.py
```

I test del runner usano un fixture path in memoria e mock della discovery e del
validator: non creano directory nella temp di sistema e quindi non dipendono
dalle ACL locali.

## Limiti e confini

Il report è esclusivamente strutturale e rappresenta l'esito del contratto
locale G18. Anche un report con `exit_status: 0` non dimostra correttezza
fattuale, educativa, tecnica, normativa, di sicurezza, professionale o legale;
non dimostra l'autorevolezza, l'attualità o la compatibilità di una fonte o
licenza; e non sostituisce revisione umana o professionale.
