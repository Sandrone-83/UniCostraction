# UniCostraction — guida di revisione a lotti G13-A

Questo documento accompagna `UNI_CLUSTER_REVIEW_PACKET_G13_A.json`.
È un indice metadata-only dei 85 cluster G11, ordinato per priorità,
con riferimenti osservati a esami e candidati pack. Non contiene testo
didattico, risposte, né una decisione di revisione.

## Regole del packet

- Ogni cluster compare una sola volta nell'indice perché è una unità di lavoro G11; non vengono deduplicati né riscritti gli anchor `unit_refs`.
- Le associazioni pack/esame sono riportate come osservate da G4: `ambiguous` e `unmatched_exam` restano tali e non diventano associazioni canoniche.
- Il contratto decisionale è quello G12: `distinct`, `merge_candidate`, `reject_candidate`, `needs_source_review`.
- Prima di una decisione non-null, compilare `evidence_ref`, `reviewer` e `rationale`; `evidence_ref` deve puntare a un'evidenza verificabile.
- `merge_candidate` e `reject_candidate` sono esiti da sottoporre a revisione, non comandi esecutivi; non modificare o cancellare card/esami durante questa fase.
- La decisione umana non certifica correttezza didattica, normativa, legale, fattuale o di licenza.

## Sequenza per ogni lotto

1. Aprire il lotto in ordine di `priority_rank` e controllare gli identificativi e gli anchor, senza copiare il testo delle domande.
2. Verificare separatamente i riferimenti `exam_refs` e i candidati `pack_refs`; conservare eventuali stati unmatched o ambiguous.
3. Raccogliere l'evidenza esterna necessaria e registrare il riferimento verificabile nel record del cluster.
4. Solo dopo l'intervento umano, valorizzare decisione, reviewer e rationale; fino ad allora tutti i quattro campi `review` devono restare `null`.
5. Rieseguire la validazione strutturale del packet e lasciare ogni azione sui contenuti a un flusso esplicitamente autorizzato e successivo.

## Lotti deterministici

| Lotto | Priorità G11 | Cluster | Stato iniziale |
| --- | ---: | --- | --- |
| `batch-01` | 1–10 | `component-0036`, `component-0025`, `component-0033`, `component-0001`, `component-0002`, `component-0004`, `component-0007`, `component-0011`, `component-0012`, `component-0022` | 10 pending |
| `batch-02` | 11–20 | `component-0071`, `component-0072`, `component-0073`, `component-0074`, `component-0075`, `component-0076`, `component-0079`, `component-0080`, `component-0083`, `component-0084` | 10 pending |
| `batch-03` | 21–30 | `component-0081`, `component-0082`, `component-0003`, `component-0005`, `component-0009`, `component-0010`, `component-0024`, `component-0028`, `component-0032`, `component-0035` | 10 pending |
| `batch-04` | 31–40 | `component-0037`, `component-0038`, `component-0039`, `component-0043`, `component-0048`, `component-0051`, `component-0052`, `component-0050`, `component-0006`, `component-0008` | 10 pending |
| `batch-05` | 41–50 | `component-0013`, `component-0014`, `component-0015`, `component-0016`, `component-0017`, `component-0018`, `component-0019`, `component-0020`, `component-0021`, `component-0023` | 10 pending |
| `batch-06` | 51–60 | `component-0026`, `component-0027`, `component-0029`, `component-0030`, `component-0031`, `component-0034`, `component-0040`, `component-0041`, `component-0042`, `component-0044` | 10 pending |
| `batch-07` | 61–70 | `component-0045`, `component-0046`, `component-0047`, `component-0049`, `component-0053`, `component-0054`, `component-0055`, `component-0056`, `component-0057`, `component-0058` | 10 pending |
| `batch-08` | 71–80 | `component-0059`, `component-0060`, `component-0061`, `component-0062`, `component-0063`, `component-0064`, `component-0065`, `component-0066`, `component-0067`, `component-0068` | 10 pending |
| `batch-09` | 81–85 | `component-0069`, `component-0070`, `component-0077`, `component-0078`, `component-0085` | 5 pending |

## Gate di chiusura del lotto

- nessun campo `review` valorizzato senza evidenza, reviewer e rationale;
- nessun testo didattico o risposta inseriti nel packet;
- nessuna deduplicazione o modifica automatica di card/esami;
- ordine e copertura dei cluster invariati rispetto a G11;
- eventuali decisioni umane restano tracciate come contratto G12 e non come azioni eseguite.
