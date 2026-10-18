# UniCostraction — coda revisione pack/esami G5-A

## Esito

G5-A aggiunge una coda JSON deterministica per la revisione umana dei casi
lasciati aperti dalla mappatura G4. Il report è
[`UNI_PACK_EXAM_REVIEW_G5.json`](UNI_PACK_EXAM_REVIEW_G5.json) e viene generato
da [`uni_pack_exam_review_g5.py`](../../tools/uni_pack_exam_review_g5.py).

Nel checkout osservato la coda contiene sei item:

| Classe | Item | Esito automatico |
| --- | --- | --- |
| pack ambiguo | `AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK` | 2 candidati osservati |
| pack ambiguo | `FORMULARIO_STRUTTURE_PACK` | 2 candidati osservati |
| esame ambiguo | `INFRASTRUTTURE` | 2 candidati osservati |
| esame ambiguo | `STRUTTURE` | 2 candidati osservati |
| esame legacy non abbinato | `IMPIANTI_FV_EOLICO` | nessun candidato osservato |
| esame legacy non abbinato | `MATERIALEDILE` | nessun candidato osservato |

Ogni item ha ordine stabile, priorità, percorsi sorgente, evidenze e candidati
osservati. Parte con `review_status: "pending"` e con una decisione nulla.
`classification: "ambiguous"`, `classification: "unmatched_exam"`,
`uncertainty`, `legacy_observed` e `candidate_ids` non vengono riscritti come
equivalenze canoniche.

## Regole di revisione

- I candidati sono segnali di nome/documentazione derivati da G4, non prove di
  copertura, identità o equivalenza semantica.
- Per gli item ambigui il revisore può associare solo sulla base di evidenza
  esplicita, mantenere il caso irrisolto o rinviarlo.
- Per i due legacy non abbinati `candidate_ids` resta vuoto: il revisore deve
  trovare evidenza esplicita oppure mantenerli non abbinati. Non è ammesso un
  fallback basato sul solo dominio nominale.
- Il tool non legge domande, risposte o contenuto delle schede per dedurre
  associazioni e non modifica il corpus.

La coda è un registro di lavoro, non un’approvazione didattica, normativa,
semantica o di provenienza.
