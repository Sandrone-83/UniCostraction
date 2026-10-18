# UniCostraction — curriculum e dependency graph G18

Snapshot osservato il **2026-10-18** nel worktree richiesto:

- checkout: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-inventory`
- branch: `codex/uni-inventory`
- fonte G17: [`UNI_SKILL_TAXONOMY_G17.json`](UNI_SKILL_TAXONOMY_G17.json)
- commit G17 osservato: `7baaf477b6333fda44d345d407a217e5a750a312`
- grafo machine-readable: [`UNI_SKILL_DEPENDENCY_GRAPH_G18.json`](UNI_SKILL_DEPENDENCY_GRAPH_G18.json)

## Scopo e decisione di non-ridondanza

G17 fornisce **12 rami canonici e 36 skill canoniche**. G18 non crea un nuovo ramo tecnico e non ricopia i domini AEC, PA, storia, digitale, scienze, documenti, business o media. Aggiunge otto famiglie trasversali proposte: capacità di governare fonti, contesto, evidenze, mapping, prove, valutazione, review e percorso prodotto.

Ogni skill di dominio mantiene il proprio `skill_id` e proprietario G17. Un alias, una faccetta geografica o temporale, una fase di apprendimento o un percorso AuraTrix/AulaFIX è un riferimento o un filtro, non una nuova skill. Le otto famiglie G18 e le sei fasi del percorso sono **assunzioni di progettazione**, non conteggi di contenuti implementati.

## Evidenza deterministica ereditata da G17

| Indicatore | Valore | Stato / limite |
| --- | ---: | --- |
| Rami canonici G17 | 12 | osservato nel JSON G17 |
| Skill canoniche G17 | 36 | osservato nel JSON G17 |
| `COURSE.yaml` totali | 83 | conteggio G17; non misura qualità |
| Pack universitari | 71 | conteggio G17 |
| Pack root con corso | 12 | conteggio G17 |
| Righe `schede.jsonl` | 963 | conteggio fisico G17 |
| File esame pubblico | 73 | contenuto pubblico, non chiavi |
| Domande d’esame pubbliche | 18.689 | QA strutturale, non correttezza |
| Unità schede + domande | 19.652 | conteggio strutturale |
| Item G5 pending / decided | 6 / 0 | review aperta |
| Esami legacy unmatched | 2 | mapping aperto |
| Cluster G14 open / total | 85 / 85 | review aperta |
| Conoscenza promossa | 0 | il contenuto resta `reference_only` |
| Release readiness | `blocked` | stato ereditato da G17 |

Questi sono gli unici conteggi usati come fatti. Le quantità “8 famiglie”, “6 fasi” e “44 nodi del grafo” sono assunzioni verificabili del presente artefatto: 36 skill G17 + 8 famiglie G18; i 12 rami sono raggruppamenti e non nodi aggiuntivi.

## Famiglie G18 proposte

| Family ID | Funzione | Si collega soprattutto a | Output controllabile |
| --- | --- | --- | --- |
| `g18.provenance_source_governance` | Separare fonte, interpretazione, esempio e ipotesi; registrare versione, diritti e contesto | `documents.*`, PA, storia, media | record di provenienza e packet di review |
| `g18.context_jurisdiction_time` | Applicare geografia, periodo, decorrenza e ciclo di vita | PA, storia, business, documenti | unità annotata e flag di staleness |
| `g18.semantic_mapping_nonredundancy` | Risolvere alias/ID e trasformare la similarità in coda di review | documenti, dati, media | mapping canonico e review queue |
| `g18.evidence_document_control` | Governare stati, versioni, decisioni e audit trail | documenti, delivery, appalti | evidence packet e log revisori |
| `g18.runtime_interoperability_validation` | Eseguire prove riproducibili su CAD/BIM/coding/dati | digitale, calcolo | risultato runtime e failure record |
| `g18.evaluation_exam_integrity` | Valutare apprendimento proteggendo le risposte | documenti, scienze, PA, storia | evaluation set protetto e rubric |
| `g18.professional_review_release` | Assegnare il review umano e bloccare la release quando serve | PA, sicurezza, calcolo, finanza, diritti | decisione gate e release readiness |
| `g18.learning_orchestration_auratrix_aulafix` | Instradare learner e caso attraverso skill e gate esistenti | delivery, documenti, digitale, media | learner record e handoff |

La regola pratica è: G17 insegna o rappresenta il dominio; G18 decide come contestualizzarlo, provarlo, valutarlo e fermarlo. G18 non trasforma un riferimento in conoscenza verificata.

## Facet geografiche e temporali

Il vocabolario è quello già ammesso da G17: geografia `IT`, `EU`, `world`, `comparative`, `unknown`; periodo `1800-1899`, `1900-1945`, `1946-1989`, `1990-2009`, `2010-present`, `current-law`, `unknown`.

Ogni unità G18 deve portare, quando pertinente:

- territorio o confronto esplicito: una regola italiana non è automaticamente europea o mondiale;
- periodo storico oppure data di efficacia: `current-law` non è una dichiarazione senza fonte e data;
- fase di ciclo di vita: brief, design, approval, procurement, construction, commissioning, operation, maintenance, diagnosis, recovery o decommissioning;
- tipo di artefatto e rischio: per distinguere una spiegazione, un calcolo, un permesso, un report, un esame o un media asset.

`unknown` è un valore di arresto informativo: indica che la risposta non deve colmare il vuoto per inferenza. `comparative` richiede di mantenere visibili le differenze tra territori o periodi, non di fonderle.

## Dipendenze principali

Il grafo completo è nel JSON. La catena didattica minima è:

```text
scienza di base -> formule/misure -> calcolo spiegabile -> dominio tecnico
design/rappresentazione -> materiali -> involucro -> metodi di esecuzione
storia 1800-1945 -> storia 1946-1989 -> storia 1990-present/comparativa
CAD/BIM -> validazione asset/dati     coding/automazione -> validazione asset/dati
evidenza/provenienza -> contesto geo-temporale -> document control
provenienza -> mapping non-ridondante -> valutazione protetta
contesto + evidenza + valutazione + runtime -> review professionale/release
review/release + delivery -> orchestrazione AuraTrix/AulaFIX
```

Sono relazioni di curriculum, non certificazioni di sufficienza del contenuto. In particolare, il calcolo spiegabile può alimentare lo studio strutturale, ma non autorizza un progetto; un test runtime può dimostrare una prova riproducibile, ma non la sicurezza produttiva.

## Gate di valutazione

| Gate | Superato quando | Non dimostra |
| --- | --- | --- |
| `G18-E01` inventario | 12 rami, 36 skill e ID risolti senza duplicati | correttezza o completezza |
| `G18-E02` provenienza/contesto | fonte, interpretazione, data/periodo, territorio e diritti separati | verità della fonte o dell’interpretazione |
| `G18-E03` facet/route | faccette e stop condition presenti | consulenza legale o copertura universale |
| `G18-E04` mapping | alias a un ID; similarità solo in review; esami separati | equivalenza semantica o qualità didattica |
| `G18-E05` evidenza/lifecycle | stato, versione, decisione, revisore e audit trail registrati | autorizzazione a depositare, certificare o eseguire |
| `G18-E06` runtime | prova nell’ambiente target con input/output riproducibili | sicurezza produttiva o conformità professionale |
| `G18-E07` review professionale | evaluation riproducibile, ruolo qualificato e limiti registrati | autorevolezza di materiale non revisionato |
| `G18-E08` release | gate strutturali, provenance, semantici, runtime e professionali coerenti | completezza globale o certificazione |

## Percorso progressivo AuraTrix / AulaFIX

Le sei fasi seguenti sono una proposta operativa, non sei corsi già presenti nel repository.

| Fase | Prerequisiti | G17 dominante | Output | AuraTrix | AulaFIX |
| --- | --- | --- | --- | --- | --- |
| A0 Orientamento | — | scienze, evidenza, storia | scope map, facet card, source posture | spiega e chiede il contesto | crea intake bounded |
| A1 Fondamenti | A0 | misure, calcolo, design, materiali, CAD/BIM | concept annotato, disegno/modello, assunzioni | tutor non-autorevole | conserva artefatto e unità |
| A2 Sistemi e ciclo di vita | A1 | involucro, strutture, MEP, energia, ambiente, diagnosi | lifecycle case map, confronto opzioni, evidence packet | confronta e segnala limiti | mantiene stato e domande aperte |
| A3 Sistema italiano e delivery | A2 | PA, urbanistica, appalti, documenti, impresa | bozza contestualizzata, reviewer matrix, handoff | instrada e si ferma prima del filing | traccia versioni, evidenze e blocker |
| A4 Digitale e valutazione | A3 | coding, asset/data, diritti, storia contemporanea | canonical mapping, runtime record, evaluation protetta | allena mapping senza esporre chiavi | esegue check e conserva log |
| A5 Caso supervisionato | A4 | safety, valuation, delivery, media, document gate | case summary, release record, handoff umano | sintetizza noto/ignoto/bloccato | pacchettizza per il revisore |

### Confine di review professionale

Il percorso deve fermarsi e consegnare a un ruolo qualificato quando riguarda:

- diritto vigente, urbanistica, permessi, appalti, fisco o sicurezza;
- calcolo strutturale, dimensionamento MEP/energia, diagnosi, patologie o decisioni tecniche;
- stime, investimenti, mercato, assicurazioni o valutazioni;
- diritti d’autore, privacy, brand, consenso e pubblicazione;
- documenti destinati a firma, deposito, certificazione, pagamento o esecuzione.

Il fatto che un contenuto abbia forma di report, che un test passi o che un esame sia strutturalmente valido non sostituisce la review. Nessuna fase autorizza invio automatico, pagamento, pubblicazione, filing, certificazione o esecuzione.

## Non-azioni e stato di release

Questo G18 non modifica `docs/coordination/UNI_SKILL_TAXONOMY_G17.json`, pack, schede, esami, fixture o corpus. Non deduplica e non cancella materiale. Non espone chiavi d’esame. Non promuove contenuto a `verified_knowledge`.

Il release status resta **BLOCKED**, ereditato dai 6 pending G5, dai 2 esami legacy unmatched e dagli 85 cluster G14 open già registrati da G17. La validazione del presente lavoro deve quindi controllare solo struttura, coerenza degli ID, aciclicità/risoluzione del grafo, conteggi dichiarati e diff limitato ai due file richiesti.
