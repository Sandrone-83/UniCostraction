# UniCostraction — catalogo master e tassonomia globale G17

Snapshot osservato il **2026-10-18** nel worktree esatto:

- checkout: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-inventory`
- branch: `codex/uni-inventory`
- commit osservato: `7baaf477b6333fda44d345d407a217e5a750a312`
- remote: `https://github.com/Sandrone-83/UniCostraction.git`

Questo catalogo è un registro di coordinamento per AuraTrix/AulaFIX. Il contratto machine-readable è [`UNI_SKILL_TAXONOMY_G17.json`](UNI_SKILL_TAXONOMY_G17.json). Il perimetro conteggia il solo HEAD tracciato; G16 era già presente nel branch prima del lavoro G17, non è attribuito a G17 e non è stato modificato.

## Decisione di catalogo

La tassonomia globale ha **12 rami canonici** e **36 skill canoniche**. Ogni pack o skill ha un solo proprietario primario. Le sovrapposizioni normali del mondo costruzioni non generano copie: si registrano con facet e riferimenti.

La chiave unica è `skill_id`. I facet ammessi sono:

- geografia: `IT`, `EU`, `world`, `comparative`, `unknown`;
- periodo: `1800-1899`, `1900-1945`, `1946-1989`, `1990-2009`, `2010-present`, `current-law`, `unknown`;
- ciclo di vita: brief, design, approval, procurement, construction, commissioning, operation, maintenance, diagnosis, recovery, decommissioning;
- artefatto: concept, calculation, drawing, model, specification, estimate, contract, permit, report, exam, dataset, media_asset;
- rischio: educational, technical, legal, financial, safety, privacy, licensing, publication.

Regola operativa: un alias punta a un `skill_id` esistente; non crea una skill parallela. Un pack viene assegnato una volta nel campo `primary_pack_refs` del JSON; un cross-link tematico non sposta la proprietà primaria.

## Inventario deterministico dello snapshot

| Indicatore | Valore | Evidenza / limite |
| --- | ---: | --- |
| File tracciati totali | 6.767 | `git ls-files`, include test e fixture |
| File tracciati esclusi test | 6.708 | perimetro corpus/catalogo |
| `COURSE.yaml` totali esclusi test | 83 | 71 pack `UNIVERSITA_EDILIZIA` + 12 pack root |
| Pack universitari | 71 | ogni pack ha manifest e `schede/schede.jsonl` |
| Pack root con corso | 12 | CAD, coding 1–5, marketing, edilizia, fondamenti, Italia, materiali, storia |
| File `schede.jsonl` universitari | 71 | conteggio percorso |
| Righe `schede.jsonl` | 963 | coerente con ledger G8 |
| File esame pubblico | 73 | `UNIVERSITA_EDILIZIA/ESAMI/**/domande.md` |
| Domande d’esame | 18.689 | audit statico G10; non sono chiavi di risposta |
| Unità schede + domande pubbliche | 19.652 | conteggio strutturale, non qualità didattica |
| File JSONL esclusi test | 255 | include asset/dataset CAD e altri JSONL |
| Righe JSONL escluse test | 37.381 | conteggio fisico delle righe, non unità omogenee |
| Percorsi tracciati `CAD_Library` | 5.859 | asset/dataset; presenza non prova interoperabilità |
| Percorsi tracciati `Edilizia_Pack` | 297 | fonti/raw/manifest/tool; licenza da verificare |

### Stati di copertura e gate

Il catalogo distingue sempre presenza strutturale da conoscenza promossa:

| Stato | Uso nel G17 |
| --- | --- |
| `verified_structural` | Path, manifest, conteggio o report osservato e riproducibile nel checkout. |
| `reference_only` | Materiale esistente utilizzabile come riferimento, ma non autorizzato come risposta autorevole. È lo stato del contenuto corrente. |
| `needs_review` | Mappatura, provenienza, equivalenza semantica, copertura o decisione umana ancora aperta. |
| `blocked` | Un gate impedisce promozione o automazione. |
| `future` | Ramo o sotto-skill desiderata ma non evidenziata come implementata nello snapshot. |
| `verified_knowledge` | Stato di promozione riservato a contenuti versionati, con fonti, diritti, revisione ed evaluation; conteggio corrente: **0**. |

Il gate di release resta **BLOCKED**: G5 ha 6 item `pending` e 0 `decided`; 2 esami legacy sono `unmatched`; G14 ha 85 cluster, tutti `open`. I conteggi di mapping esame-pack sono 14 coppie a nome esatto e 59 alias osservati. Questi segnali organizzano la review e non autorizzano fusione, cancellazione o riscrittura.

Fonti di coordinamento: [`UNI_COMPLETENESS_LEDGER_G8.json`](UNI_COMPLETENESS_LEDGER_G8.json), [`UNI_RELEASE_READINESS_G7.json`](UNI_RELEASE_READINESS_G7.json), [`UNI_REDUNDANCY_AUDIT_G10_A.json`](UNI_REDUNDANCY_AUDIT_G10_A.json) e [`UNI_CLUSTER_REVIEW_PROGRESS_G14_A.json`](UNI_CLUSTER_REVIEW_PROGRESS_G14_A.json).

## Rami della skill library aggiunti in G17

I nomi canonici, i 36 `skill_id` e l’elenco esatto dei pack primari sono nel JSON. La tabella è la vista di lavoro; tutti i rami presenti nello snapshot sono ancora `reference_only` e `needs_review` per la promozione.

| Branch canonico | Copertura primaria | Stato attuale | Lacuna / confine |
| --- | --- | --- | --- |
| `aec.design_representation` | Architettura, disegno, interni, edifici speciali, verde e spazio pubblico | strutturale presente; reference-only | non prova completezza progettuale o conformità |
| `aec.materials_methods` | Materiali, involucro, finiture, posa, prefabbricazione e metodi | strutturale presente; reference-only | scheda tecnica e posa richiedono fonte/versione e controllo tecnico |
| `aec.structures_infrastructure` | Strutture, geotecnica, civile, trasporti, porti, aeroporti, dighe | strutturale presente; reference-only | formule e opere non sono autorizzazione al calcolo o al progetto |
| `aec.building_systems_energy` | MEP, energia, rinnovabili, illuminazione, automazione, data center, sicurezza tecnica | strutturale presente; reference-only | current-law, sicurezza e dimensionamento restano da verificare |
| `aec.environment_resilience` | Bonifica, LCA, circolarità, patologie, recupero, restauro, ricostruzione | strutturale presente; reference-only | diagnosi e decisioni di intervento richiedono professionista e fonti |
| `pa.italy_legal_admin` | PA italiana, urbanistica, edilizia, appalti, fisco, diritto e sicurezza | strutturale presente; reference-only | ogni risposta normativa deve avere territorio, decorrenza e fonte |
| `history.world_construction_1800_present` | Storia mondiale della costruzione e dell’architettura dal 1800 a oggi | strutturale presente; reference-only | presenza dei pack non dimostra copertura mondiale o bilanciamento storico |
| `digital.tools_data` | CAD/BIM, coding, robotica, dati, automazione e interoperabilità | strutturale presente; reference-only | asset presenti o esempi statici non provano runtime o produzione |
| `science.foundation_calculation` | Matematica, fisica, formule e calcolo spiegabile | strutturale presente; reference-only | servono assunzioni, unità, campo di validità e review |
| `documents.evidence_workflows` | Perizie, stime, registri tecnici, evidenze e review gate | strutturale parziale; reference-only | documento presente non significa workflow completo o utilizzabile |
| `business.real_estate_operations` | Impresa, real estate, facility, condominio, hospitality e delivery | strutturale presente; reference-only | dati di mercato, fisco, investimenti e assicurazioni sono versionati |
| `media.communication` | Marketing, linguaggio visivo, contenuti, diritti e pubblicazione | strutturale presente; reference-only | nessuna autorizzazione automatica a pubblicare o usare asset |

### Aree mancanti o bloccate

- **Mancante / `future`**: registro unico di fonti authoritative per ogni skill; storia mondiale 1800–present con copertura comparativa esplicita; versioning della normativa italiana; template documentali con lifecycle e autorizzazioni; prove runtime CAD/BIM/coding; diritti e provenance degli asset media.
- **Da review / `needs_review`**: assegnazione semantica dei 83 manifesti ai rami; 6 item G5; 2 esami legacy unmatched; 85 cluster G14; alias fra pack ed esami; qualità e completezza dei contenuti.
- **Bloccato / `blocked`**: promozione a `verified_knowledge`, release readiness, risposte di current law, sicurezza, fisco, investimento, dimensionamento e uso professionale. Il blocco non viene aggirato con un conteggio statico.
- **Non affermato**: non si dichiara che il corpus sia corretto, aggiornato, completo, concesso in licenza per ogni uso o idoneo a sostituire un professionista.

## Roadmap con confini di evidenza

| Fase | Stato | Obiettivo | Cosa può essere dichiarato |
| --- | --- | --- | --- |
| G17 baseline | `verified_structural` | Freeze dello snapshot, ID canonici, one-owner rule, facet e stati | Struttura e conteggi osservati; contenuto ancora reference-only |
| G18 resolution | `needs_review` | Chiudere con evidenza i 6 pending, i 2 legacy e gli 85 cluster | Decisioni umane tracciate; nessuna dedup automatica |
| G19 provenance | `blocked_until_evidence` | Fonti, versione/data, giurisdizione/periodo, diritti e reviewer per skill | Solo record con gate superati possono avvicinarsi a verified knowledge |
| G20 branch expansion | `future` | Colmare storia mondiale, PA versionata, documenti controllati, runtime digitale, business/media con diritti | Nuove skill solo se assegnate a un ID canonico, senza rami duplicati |
| G21 release | `blocked` | Concordare gate strutturali, provenance, semantici, runtime e professionali | Release soltanto con test mirati, controlli reali e sign-off qualificato |

### Criterio di promozione a conoscenza verificata

Un record può passare da `reference_only` a `verified_knowledge` solo quando sono presenti: fonte primaria o dichiarata, versione/data e giurisdizione o periodo, licenza/diritti, separazione fra fonte e interpretazione, revisione umana competente, evaluation riproducibile e — per strumenti o flussi — verifica runtime pertinente. Per diritto, sicurezza, finanza, calcolo e documenti professionali serve inoltre un confine esplicito sull’uso e sul sign-off.

## Non-azioni G17

G17 non modifica pack, schede, esami, fixture, tool o test. Non espone chiavi di risposta, non deduplica, non cancella, non pubblica, non invia e non certifica conformità professionale o legale.
