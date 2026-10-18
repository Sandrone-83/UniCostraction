# UniCostraction Markdown Skill Library Governance — G18

Data: 2026-10-18
Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`

## Scopo

G18 aggiunge un gate strutturale fail-closed per la libreria di skill in
Markdown. Il validator controlla soltanto forma, presenza e coerenza dei
metadati dichiarati. Un risultato `valid` non dimostra correttezza fattuale,
educativa, tecnica, normativa, legale, di sicurezza o professionale, né
l'attualità o l'utilizzabilità commerciale di una fonte o licenza. Questi
giudizi restano a revisione umana e, quando necessario, professionale.

## Layout e manifest

La root passata a `tools/validate_skill_markdown_g18.py` deve contenere:

```text
<skill-library>/
  manifest.json
  <categoria>/<skill-id>/SKILL.md
```

`manifest.json` è JSON UTF-8 senza chiavi duplicate e ha questa forma:

```json
{
  "schema_version": "g18",
  "skills": [
    {
      "id": "skill-cila-basics",
      "category": "edilizia",
      "path": "edilizia/skill-cila-basics/SKILL.md"
    }
  ]
}
```

Gli ID, le categorie e i componenti di percorso sono slug minuscoli con
trattini. Ogni skill deve comparire una sola volta nel manifest e ogni percorso
deve puntare a un file presente. Il validator confronta inoltre `id`,
`category` e `path` con il percorso reale e rifiuta file estranei, symlink,
percorsi Windows, `.` e `..`.

## Front matter e sezioni operative

Ogni `SKILL.md` è UTF-8 non vuoto e inizia con front matter delimitato da
`---`. Sono richiesti questi campi top-level:

```yaml
---
name: skill-cila-basics
description: Descrizione breve e non certificativa.
metadata:
  skill_id: skill-cila-basics
  category: edilizia
  version: 1
---
```

`name` e `metadata.skill_id` devono coincidere. `metadata` deve essere una
mappa non vuota e contenere almeno `skill_id` e `category`; il parser locale è
intenzionalmente un sottoinsieme YAML deterministico, non un interprete YAML
generale.

Il corpo deve contenere, con contenuto non vuoto, questi titoli H2 esatti:

1. `Purpose`
2. `Inputs and Preconditions`
3. `Operational Workflow`
4. `Outputs and Handoff`
5. `Sources and Provenance`
6. `Rights and Use`
7. `Professional and Legal Boundaries`
8. `Verification and Escalation`

## Fonti, diritti e confini

La sezione `Sources and Provenance` deve dichiarare almeno un riferimento:
URL `http`/`https` oppure ID di registro `SRC-...`. Il gate non verifica
raggiungibilità, autorevolezza, versione o correttezza della fonte.

La sezione `Rights and Use` deve contenere una dichiarazione esplicita su
licenza/diritti, redistribuzione, attribuzione, copyright, permesso o procedura
originale. La presenza di una parola chiave non è una clearance legale.

La sezione `Professional and Legal Boundaries` deve esplicitare tutti i
seguenti limiti: `human review`, `professional review`, `automatic execution`
o `automatic action`, `legal advice` e `factual correctness`. Il validator
controlla la presenza testuale dei confini; non giudica se il testo li rispetti
né se il limite sia adeguato al caso concreto.

## Comandi di QA

```text
python tools\validate_skill_markdown_g18.py <skill-library>
python -m unittest tests\coordination\test_skill_markdown_contract_g18.py
python -m compileall -q tools tests
git diff --check
```

Il comando restituisce `0` solo quando manifest, file e controlli strutturali
sono tutti validi. Directory mancante, directory vuota, file vuoti, testo non
UTF-8, JSON ambiguo, skill non registrate o manifest non coerente producono un
risultato non valido. Il validator non modifica la libreria e non esegue
richieste di rete.
