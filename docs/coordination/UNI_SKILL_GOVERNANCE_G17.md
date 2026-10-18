# UniCostraction skill library governance — G17-C

Data: 2026-10-18
Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`

## Scopo

G17-C prepara il controllo strutturale per una futura libreria di skill. Non
modifica né il corpus né l'inventory. Il validator è fail-closed: un record
mancante, illeggibile, non UTF-8, non JSON, ambiguo o fuori contratto produce
un finding e un exit code diverso da zero.

Il perimetro è intenzionalmente separato dalla validità del contenuto. Un
risultato `valid` dimostra soltanto che la forma del record e i metadati
dichiarati rispettano il contratto locale. Non dimostra che una fonte sia
autorevole, che una licenza sia utilizzabile, che un procedimento sia corretto
o aggiornato, né che una indicazione normativa, legale, di sicurezza o
professionale sia vera. Queste valutazioni richiedono revisione umana e, dove
necessario, professionale.

## Layout e contratto

La libreria passata a `tools/validate_skill_library_g17.py` è una directory
contenente esclusivamente file JSON UTF-8. Ogni skill deve stare esattamente in
`<categoria>/<id>.json`; il campo `path` deve essere lo stesso percorso POSIX
relativo alla root della libreria. `category` deve coincidere con la directory
e `id` con lo stem del file. Gli ID e le categorie sono slug minuscoli con
trattini (`[a-z0-9]+(?:-[a-z0-9]+)*`).

Ogni record richiede:

```json
{
  "id": "skill-cila-basics",
  "title": "CILA basics",
  "summary": "Descrizione non certificativa.",
  "category": "edilizia",
  "path": "edilizia/skill-cila-basics.json",
  "workflow": [
    {"step_id": "inspect-input", "action": "...", "output": "..."}
  ],
  "source_refs": [{"ref": "...", "kind": "official"}],
  "license_status": "pending",
  "safety_legal_boundary": {
    "human_review_required": true,
    "professional_review_required": true,
    "automatic_execution_prohibited": true,
    "legal_advice_prohibited": true,
    "factual_correctness_requires_review": true,
    "boundary_note": "..."
  },
  "provenance_status": "pending"
}
```

Il workflow deve essere una lista non vuota di step non vuoti, con `step_id`,
`action` e `output`; gli `step_id` non possono ripetersi. `source_refs` deve
essere una lista non vuota di oggetti con `ref` e `kind`. Il validator accetta
solo questi `kind`: `official`, `normative`, `institutional`, `user_provided`,
`internal`, `other`. Non verifica il contenuto o la raggiungibilità del
riferimento.

Gli stati di licenza ammessi sono:

`unreviewed`, `pending`, `reviewed`, `restricted`, `not_applicable`.

Gli stati di provenienza ammessi sono:

`unreviewed`, `pending`, `verified`, `blocked`.

`reviewed`/`restricted` richiedono `license_evidence_ref`; `verified` richiede
`provenance_evidence_ref`. In entrambi i casi il riferimento è solo evidenza
del percorso di review: non è una certificazione automatica di conformità,
licenza o correttezza.

I cinque flag di confine devono essere esplicitamente `true`: revisione umana,
revisione professionale, divieto di esecuzione automatica, divieto di consulenza
legale e necessità di verificare la correttezza fattuale. Anche `boundary_note`
è obbligatorio e non vuoto. Questi campi rendono il limite operativo visibile;
non provano che il testo della skill lo rispetti.

## Controlli deterministici

Il guard controlla:

- UTF-8 strict, JSON valido, oggetti senza chiavi duplicate e nessun file non
  JSON nella root della libreria;
- campi obbligatori, assenza di campi sconosciuti e slug normalizzati;
- mapping reale `path`/`category`/`id` e layout esatto;
- unicità degli ID esatti tra tutti i file e degli step dentro ogni workflow;
- workflow e riferimenti di fonte non vuoti;
- domini chiusi per stato licenza e stato provenienza, con evidenza richiesta
  per gli stati che la dichiarano;
- boundary safety/legal espliciti e conservativi.

I findings sono ordinati per percorso e testo, così la stessa libreria produce
lo stesso output. Il validator non stampa i contenuti dei record e non cerca di
trasformare i riferimenti in giudizi di merito.

## Comandi di QA

```text
python tools\validate_skill_library_g17.py <future-skill-library>
python -m unittest tests\coordination\test_skill_library_contract_g17.py
python -m compileall -q tests tools
git diff --check
```

Il comando sul validator restituisce `0` solo con una libreria interamente
valida. Directory mancante, directory vuota o qualsiasi finding restituiscono
un risultato non valido; errori di contenuto vengono riportati senza
interpretazioni fattuali o legali.
