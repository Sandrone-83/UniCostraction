# -*- coding: utf-8 -*-
"""Coding_Master_Pack_2: secondo livello di profondità — 30 schede nuove, corpus mai coperti."""
import json, os

BASE = r"C:\Users\alessandro\Documents\kimi\tasks\2026-09-26\15-14-07-e3d653af\Coding_Master_Pack_2\parsed"
os.makedirs(BASE, exist_ok=True)

LIC = "Sintesi didattica originale Kimi (pubblico dominio)"
ATT = "Corpus coding master 2 a cura di Kimi"

def rec(id_, cat, tema, title, text):
    return {"id": id_, "categoria": cat, "tema": tema, "title": title, "text": text,
            "source": f"coding_master_2_{cat}_kimi", "license": LIC, "commercial_ok": True,
            "attribution": ATT, "url": ""}

devops = [
rec("DVO-001","devops","docker","DOCKER E CONTAINER: 'SUL MIO PC FUNZIONAVA' E' MORTO",
"""Il container risponde al problema antico del software: funziona sulla mia macchina ma non su quella del cliente.

CONCETTI CHIAVE:
1. IMMAGINE vs CONTAINER: l'immagine e' il progetto (read-only), il container e' l'istanza in esecuzione. Si costruisce l'immagine con un Dockerfile — una ricetta riga per riga: FROM (immagine base), COPY (il codice), RUN (installazioni), CMD (comando di avvio).
2. ISOLAMENTO: il container porta con se' SO, librerie e dipendenze: stesso ambiente in sviluppo, test e produzione. Addio 'dipende dalla versione di PHP del server'.
3. LIVELLI E CACHE: ogni istruzione del Dockerfile crea uno strato riusabile: ordinare dal piu' statico (dipendenze) al piu' volatile (codice) per sfruttare la cache e velocizzare le build.
4. VOLUMI E RETI: i dati persistenti (database) vivono in volumi, non nel container; i container parlano tra loro su reti dedicate.

DOCKER COMPOSE: il file YAML che orchestra piu' container insieme (app + database + cache): un comando e l'intero ambiente di sviluppo si alza identico per ogni membro del team.

REGOLE PRATICHE: immagini piccole (partire da alpine/distroless), niente segreti nelle immagini (solo variabili d'ambiente a runtime), un processo per container, healthcheck per sapere se il servizio e' vivo.

L'ANALOGIA EDILE: il container e' la casa prefabbricata costruita in fabbrica con tutti gli impianti collaudati, portata in cantiere e installata in un giorno invece di costruire sul posto."""),

rec("DVO-002","devops","cicd","CI/CD: PIPELINE CHE TESTANO, COSTRUISCONO E RILASCIANO DA SOLI",
"""La Continuous Integration e Continuous Delivery trasformano il rilascio da evento traumatico in routine quotidiana.

LA PIPELINE TIPO (ogni push sul repository):
1. LINT + TYPECHECK: stile e tipi — 30 secondi, cattura l'ovvio.
2. TEST: unitari, integrazione, end-to-end. Il cuore della pipeline: se falliscono, si ferma tutto.
3. BUILD: compilazione del pacchetto o dell'immagine Docker, con versione calcolata automaticamente (git commit hash o versione semver).
4. DEPLOY IN STAGING: ambiente identico alla produzione dove si fa il collaudo finale.
5. DEPLOY IN PRODUZIONE: manuale (click) o automatico, dietro strategie di rilascio sicure.

STRATEGIE DI RILASCIO:
- BLUE/GREEN: due ambienti identici, si sposta il traffico istantaneamente; rollback immediato.
- CANARY: si rilascia prima all'1% degli utenti, poi al 10%, poi a tutti: il difetto colpisce pochi prima di colpire tutti.
- FEATURE FLAG: il codice nuovo si rilascia SPENTO e si accende per gruppi di utenti — separa il rilascio dall'attivazione.

REGOLE D'ORO: pipeline veloce (sotto 10-15 minuti, altrimenti si aggira), mai dipendere da passi manuali, ogni artefatto prodotto dalla pipeline e' immutabile e tracciabile, rollback sempre possibile in un comando.

IL PRINCIPIO: la fiducia nel deploy non viene dalla cautela, viene dai test. Chi ha 500 test verdi spinge in produzione alle 17 di venerdi' senza sudare."""),

rec("DVO-003","devops","kubernetes_iac","KUBERNETES E INFRASTRUCTURE AS CODE: LA FABBRICA DEI CONTAINER",
"""Quando i container diventano decine, serve un regista: Kubernetes. E l'infrastruttura va scritta come codice, non cliccata a mano.

KUBERNETES IN 5 CONCETTI:
1. POD: l'unita' minima — uno o piu' container che viaggiano insieme.
2. DEPLOYMENT: dichiari lo stato desiderato ('3 copie di questa app, sempre') e Kubernetes ci pensa: se una muore, ne rispawna una.
3. SERVICE: l'indirizzo stabile davanti ai pod instabili — chi chiama il service non sa quanti pod ci sono.
4. CONFIGMAP/SECRET: configurazione e segreti separati dal codice.
5. AUTO-SCALING: piu' traffico = piu' pod automatici; meno traffico = si scala giu' e si risparmia.

QUANDO SERVIRE (E QUANDO NO): Kubernetes e' potentissimo e complesso. Se hai un'app e un database: bastano Docker Compose o un PaaS (Vercel, Railway, Fly.io). Kubernetes quando: molti servizi, traffico variabile, team di piattaforma. La regola onesta: non adottarlo per moda.

INFRASTRUCTURE AS CODE (Terraform, Pulumi): server, database e reti dichiarati in file versionati. Vantaggi: ambienti identici creati in minuti, ogni cambiamento e' una code review, niente 'ho cliccato qualcosa sul pannello e non ricordo cosa'. Il cloud smette di essere un salotto da arrangiare e diventa un progetto da computo.

REGOLA FINALE: automa prima cio' che fai piu' spesso e che peggio ti farebbe sbagliare."""),

rec("DVO-004","devops","osservabilita","OSSERVABILITA': METRICHE, LOG, TRACING E ALLERTE",
"""Un sistema in produzione senza osservabilita' e' un cantiere senza sopralluoghi: si scopre il problema quando crolla.

LE TRE COLONNE:
1. LOG: gli eventi dettagliati (gia' nel corpus base: strutturati, livellati, senza dati sensibili). Rispondono a 'cosa e' successo?'.
2. METRICHE: numeri nel tempo (richieste/sec, latenza, errori %, uso CPU/memoria). Rispondono a 'com'e' la salute?'. Il trio d'oro: latenza, traffico, errori (con satuzione come quarto).
3. TRACING: una richiesta che attraversa 6 servizi lascia una traccia unica per ogni passo: si vede DOVE si perde il tempo. Con i microservizi e' indispensabile.

L'ERRORE DA EVITARE: monitorare il server e non l'esperienza. Il server puo' essere verde mentre gli utenti aspettano 10 secondi: si misura la SLO definita sull'utente ('99% delle richieste < 300ms').

ALLERTE CHE FUNZIONANO: poche, su sintomi (gli utenti soffrono), non su cause (il disco e' all'82% — e allora?). Ogni allarme deve avere un runbook: cosa fare quando suona. Un allarme che suona sempre viene ignorato; uno mai verificato non si sa se funziona.

STRUMENTI OPEN SOURCE: Prometheus (metriche), Grafana (dashboard), Loki/Elasticsearch (log), Jaeger/Tempo (tracing). Combinazione standard: tutto gratis, tutto consolidato.

PRINCIPIO: si progetta l'osservabilita' PRIMA del problema, come si progettano i collaudi prima della consegna dell'opera."""),

rec("DVO-005","devops","cloud_costi","CLOUD E COSTI: LA FATTURA CHE DIVENTA ARCHITETTURA",
"""Il cloud fatta pagare l'effettivo uso, e questo cambia le decisioni tecniche: l'architettura giusta e' anche quella economicamente sostenibile.

I MODELLI:
- IAAS (macchine virtuali nude): massimo controllo, massima responsabilita'.
- PAAS (piattaforme gestite: database, hosting app): meno controllo, zero manutenzione — il default giusto per la maggior parte.
- SERVERLESS (funzioni a consumo): paghi solo l'esecuzione. Ideale per carichi irregolari: zero traffico = quasi zero costo. Attenzione al costo a carichi ALTI e costanti.

LE FAMIGLIE DI COSTO E COME CONTENERLE:
1. COMPUTE: spegnere cio' che non serve (i dev environment la notte e il weekend: -60%), autoscaling, istanze spot/preemptibili per i lavori interrompibili.
2. STORAGE: il dato freddo costa meno del caldo: policy di archiviazione automatiche.
3. DATASBASE GESTITO: comodissimo ma la voce che cresce piu' in fretta: valutare dimensionamento, connection pooling, e non dare al database dimensioni da aereo per una bicicletta.
4. TRAFFICO IN USCITA: trasferire dati fuori dal cloud si paga: CDN e compressioni riducono.

FINOPS (disciplina dei costi cloud): budget e allarmi di spesa, etichette su ogni risorsa (chi, cosa, ambiente), revisione mensile dei top costi, il costo come criterio di design nelle code review.

REGOLA PRATICA: la domanda giusta non e' 'quanto costa il cloud?' ma 'quanto costa QUESTO servizio PER utente?'. Quando si conosce il costo unitario, le decisioni architetturali diventano semplici: si confrontano numeri, non opinioni."""),
]

frontend = [
rec("FRO-001","frontend","react_deep","REACT/NEXT.JS DA SENIOR: STATO, RENDERING E ARCHITETTURA",
"""React e' una libreria piccola con un ecosistema enorme: la competenza senior sta nelle decisioni che la libreria non prende per te.

CONCETTI PROFONDI:
1. IL MODELLO MENTALE: l'interfaccia e' una FUNZIONE dello stato: UI = f(state). Se l'interfaccia sbaglia, lo stato e' sbagliato. Si progetta prima lo stato, poi la UI.
2. SERVER COMPONENTS (Next.js App Router): il componente viene renderizzato sul server e arriva gia' pronto: meno JavaScript inviato, caricamento piu' veloce, dati letti vicino al database. Il client interattivo solo dove serve ('use client').
3. GESTIONE DELLO STATO: gerarchia di soluzioni per grandezza del problema: useState per il locale -> context per il condiviso semplice -> store esterno (Zustand/Redux Toolkit) per il complesso. REGOLA: non introdurre uno store globale prima che il passaggio dei props diventi davvero doloroso.
4. DATA FETCHING: le Server Actions e le route handler di Next.js eliminano mezza complessita' delle API; React Query (TanStack) per caching, rinfresco e stati di loading gestiti bene.
5. PERFORMANCE REATTIVA: React.memo, useMemo e useCallback SOLO quando misurato — l'ottimizzazione preventiva rende il codice peggio senza guadagni.

ARCHITETTURA DI UN PROGETTO SERIO: cartella per feature (non per tipo di file), componenti piccoli e componibili, design system come unica fonte di stile, TypeScript strict, test sui componenti critici con Testing Library (si testa il comportamento, non l'implementazione).

ERRORE TIPICO: componenti da 500 righe che fanno tutto. La decomposizione non e' estetica: e' il modo in cui il codice resta comprensibile."""),

rec("FRO-002","frontend","css_design_system","CSS MODERNO E DESIGN SYSTEM: L'INTERFACCIA COME PROGETTO EDILE",
"""Il CSS moderno e' un linguaggio di layout potente: chi lo padroneggia smette di combattere e inizia a progettare.

LE BASI 2026:
1. FLEXBOX per righe/colonne unidimensionali, GRID per layout bidimensionali: sono complementari, non alternativi. Grid con 'repeat(auto-fit, minmax(280px, 1fr))' crea griglie responsive senza media query.
2. CUSTOM PROPERTIES (variabili CSS): '--colore-primario' definito una volta: il tema intero cambia aggiornando un valore.
3. CONTAINER QUERIES: responsive rispetto al CONTENITORE, non alla finestra: un componente si adatta ovunque sia messo.
4. LOGICA NATIVE: :has(), nesting nativo, calc(): molto di cio' per cui serviva JavaScript ora e' CSS puro.

IL DESIGN SYSTEM: la scaletta grafica dell'azienda digitale: colori (con regole di contrasto), tipografia (poche gerarchie ben definite), spaziatura (scale a passi costanti: 4/8/16/24), componenti documentati (bottoni, campi, card). Tool: Figma + Storybook. Un design system fa si' che ogni schermata sembri progettata dalle stesse mani — l'equivalente dello stile costruttivo dell'impresa.

UTILITY-FIRST (Tailwind): classi atomiche composte nel markup. Vantaggi: velocita', coerenza forzata, niente CSS morto. Critica: markup denso — si mitiga con componenti.

ACCESSIBILITA' DI BASE: focus visibili, contrasto minimo 4.5:1, non comunicare solo col colore, rispettare prefers-reduced-motion.

PRINCIPIO: il frontend buono e' invisibile: l'utente completa il compito senza pensare all'interfaccia."""),

rec("FRO-003","frontend","web_performance","WEB PERFORMANCE: LA VELOCITA' E' UNA FEATURE",
"""La velocita' di caricamento e' la prima impressione dell'app: la metodologia per ottenerla e' misurata e ripetibile.

LE METRICHE UTENTE (Core Web Vitals):
- LCP (largest contentful paint): il contenuto principale e' visibile entro 2,5s?
- INP (interaction to next paint): la pagina risponde ai click in meno di 200ms?
- CLS (cumulative layout shift): gli elementi saltano mentre carica? (max 0,1)

LEVE IN ORDINE DI IMPATTO:
1. IMMAGINI: il peso n.1 di quasi ogni sito. Compressione (WebP/AVIF), dimensioni giuste per il dispositivo (srcset), lazy loading sotto la piega.
2. JAVASCRIPT: meno codice = meno da scaricare, parsare, eseguire. Code splitting per rotta, tree shaking automatico, dipendenze controllate (un'icona non giustifica una libreria da 50KB).
3. FONT: subset (solo i caratteri usati), display swap, preload.
4. CACHING: cache del browser con etag/versioni, CDN per i contenuti statici vicino all'utente.
5. RENDERING: server side rendering o statico per il primo caricamento; idratazione differita per i componenti non visibili.

IL PROCESSO: misurare con Lighthouse e i dati di campo (CrUX), fissare un budget di performance (es. 'max 200KB di JS per pagina') trattato come requisito in code review, verificare a ogni rilascio.

L'ANALOGIA EDILE: una pagina web e' come un cantiere: prima si porta il ponteggio (HTML), poi il materiale nell'ordine in cui serve, e ogni viaggio in piu' del camion e' tempo buttato. La logistica qui si chiama critical rendering path."""),

rec("FRO-004","frontend","accessibilita","ACCESSIBILITA': SOFTWARE USABILE DA TUTTI, SENZA ECCEZIONI",
"""L'accessibilita' non e' un optional: e' qualita' del software, requisito legale per la PA in Italia (Legge Stanca / AGID) e apertura del mercato.

I PRINCIPI (WCAG, organizzati per POUR):
1. PERCEPTIBLE: contenuti percepibili da tutti i sensi — testi alternativi per le immagini, sottotitoli per i video, contrasto sufficiente (4.5:1 per il testo normale).
2. OPERABLE: tutto azionabile da tastiera (tab logico, focus visibile), niente contenuti lampeggianti, tempo sufficiente per interagire.
3. UNDERSTANDABLE: linguaggio chiaro, comportamenti prevedibili, errori spiegati con suggerimento di correzione ('il CAP e' di 5 cifre').
4. ROBUST: funziona con tecnologie assistive: screen reader, zoom 200%, tecnologie future.

IN PRATICA (il 20% che copre l'80%):
- HTML SEMANTICO: button per i click, a per i link, h1-h6 in ordine, label collegate ai campi. Il 70% dell'accessibilita' e' HTML corretto.
- ARIA solo quando il semantico non basta (es. widget complessi) — ARIA usata male peggiora.
- TEST: tabulare l'intera pagina a occhi chiusi: si capisce dove si e'? Si puo' fare tutto? Screen reader di prova (NVDA, VoiceOver) almeno una volta.
- AUTOMATISMO: axe/Lighthouse catturano il 30-40% dei problemi: vanno nella CI.

L'ARGOMENTO COMMERCIALE: siti accessibili sono piu' usabili per TUTTI (contrasto buono = leggibile al sole), meglio indicizzati (Google legge come uno screen reader) e coprono un mercato che altri ignorano."""),

rec("FRO-005","frontend","progetti_frontend","PROGETTI FRONTEND REALI: DALLA LANDING AL DASHBOARD",
"""La competenza frontend si consolida su progetti veri. Tre archetipi con la loro architettura.

PROGETTO 1 — LANDING/SITO VETRINA (Next.js + Tailwind):
Obiettivo: velocita' e SEO. Strategia: rendering statico, immagini ottimizzate dal framework, form di contatto con validazione e anti-spam (honeypot), analytics con mascheramento. Budget: 1-2 settimane. Le conversioni si misurano: click-to-call e invii form.

PROGETTO 2 — DASHBOARD/GESTIONALE (React + TypeScript + TanStack Query + component library):
Obiettivo: tabelle dense, filtri, form complessi senza impazzire. Strategia: stato server separato dallo stato UI (React Query per i dati, useState per i filtri locali), componenti tabella con virtualizzazione sopra le 100 righe, form gestiti con react-hook-form + zod (validazione condivisa col backend). Il 90% dei gestionali sono: lista -> dettaglio -> form: padroneggiare questi tre pattern copre tutto.

PROGETTO 3 — APP INTERATTIVA (es. configuratore edile):
Obiettivo: stato complesso e sincronizzato (wizard a step, anteprima live, preventivo calcolato). Strategia: macchina a stati (XState o useReducer) invece di dieci booleani impazziti: ogni step ha stati espliciti e transizioni valide. Calcoli in funzioni pure testate a parte. Salvataggio bozza in locale per non perdere il lavoro.

REGOLE COMUNI AI TRE: TypeScript ovunque, design system minimo fin dal giorno 1, il responsive non e' un refactor finale, misura le performance prima di ottimizzare.

PERCORSO DI APPRENDIMENTO: rifare il proprio sito -> dashboard su dati pubblici -> un progetto con stato complesso. Ognuno insegna un livello diverso."""),
]

data_ai = [
rec("DAE-001","data_ai","pipeline_dati","DATA ENGINEERING: PIPELINE DATI AFFIDABILI DALLA SORGENTE AL REPORT",
"""I dati dell'azienda viaggiano come i materiali in cantiere: servono trasporti affidabili, registrazioni e punti di controllo.

IL FLUSSO TIPO (ETL/ELT):
1. ESTRAZIONE: dai sistemi sorgente (gestionale, CRM, fogli Excel, API) — con API, connettori o export programmati.
2. CARICAMENTO: nel data warehouse (BigQuery, Snowflake, Postgres + dbt) — prima grezzo, poi trasformato (ELT moderno: la potenza del cloud fa le trasformazioni dopo).
3. TRASFORMAZIONE: dbt (data build tool) — le regole di business in SQL versionato e testato: 'ricavo_netto = ricavo - sconti', testati come codice.
4. CONSUMO: dashboard (Metabase, Power BI, Looker Studio) e modelli ML.

LE REGOLE DI QUALITA' (i collaudi dei dati):
- I dati arrivano? Monitor di freschezza (i dati di ieri sono qui oggi alle 8?).
- Sono plausibili? Controlli di distribuzione: il fatturato mensile non puo' scendere del 90% senza motivo.
- Sono completi? Conteggi e chiavi mancanti.
- Sono coerenti? Lo stesso cliente ha due nomi diversi nei due sistemi?

IDEMPOTENZA: ogni esecuzione della pipeline deve poter ripartire senza duplicare: chiavi deterministiche e 'merge' invece di 'append'.

ARCHITETTURA MINIMA PER UNA PMI: export giornalieri -> Postgres -> dbt -> Metabase. Tre strumenti open source/ gratuiti che coprono il 90% del valore dei progetti enterprise da sei zeri."""),

rec("DAE-002","data_ai","warehouse_modellazione","DATA WAREHOUSE E MODELLAZIONE ANALITICA: FAKTO E DIMENSIONI",
"""Modellare per l'analisi e' diverso da modellare per le operazioni: si denormalizza di proposito.

IL MODELLO A STELLA (star schema): al centro la TABELLA DEI FATTI (gli eventi misurabili: vendite, preventivi, ore di cantiere) con chiavi verso le DIMENSIONI (chi, cosa, quando, dove: clienti, servizi, date, cantieri). Semplicita' che rende le query intuitive e veloci.

IL PENSIERO DIMENSIONALE:
- FATTI: numeri e chiavi. 'Il 12/3, cliente Rossi, preventivo bagno, importo 8500, stato inviato'.
- DIMENSIONI: gli attributi descrittivi. Il cliente ha regione e canale; la data ha mese e trimestre; il servizio ha categoria e margine standard.
- GRAIN (grana): la decisione piu' importante: una riga dei fatti = un cosa esattamente? Una voce di preventivo? Un giorno-uomo di cantiere? La grana sbagliata rende alcune domande impossibili.

CONCETTI CHE SERVONO:
- SCD (slowly changing dimensions): come tracciare che il cliente Rossi era nella regione Nord fino a marzo e poi Sud — storia invece di sovrascrittura.
- AGGREGAZIONI: tabelle pre-calcolate per le domande frequenti ('fatturato per mese e regione'): i report istantanei costano piu' spazio, zero attesa.
- SEMANTICA UNICA: una sola definizione ufficiale di 'fatturato' e 'margine', in un solo file dbt, usata da tutti i report.

ERRORE CLASSICO: l'analisi sui dati operazionali diretti (il gestionale): query lente, definizioni divergenti, storico perso. Il warehouse esiste per questo: copia separata, modellata per domande, storia preservata."""),

rec("DAE-003","data_ai","ml_engineering","MACHINE LEARNING ENGINEERING: DAL MODELLO AL SISTEMA",
"""Il modello ML e' il 20% di un sistema ML: il resto e' ingegneria.

IL CICLO DI VITA:
1. DEFINIZIONE: quale decisione migliora? 'Prioritizzare i lead piu' probabili da chiudere' — non 'usare l'AI'.
2. DATI: raccolta, pulizia, etichetatura. Il lavoro vero. Le etichette sporche rendono il modello sporco (garbage in, garbage out).
3. TRAINING: scelta del modello semplice PRIMA (una regressione logistica come baseline): il modello sofisticato deve GUADAGNARSI il posto contro la baseline. Metriche giuste per il problema (precision/recall per classi sbilanciate, MAE per stime continue).
4. VALUTAZIONE su dati MAI visti (test set), con attenzione alla distribuzione reale: un modello allenato sui dati di gennaio degradra' a luglio (drift).
5. SERVING: il modello in produzione come API con versionamento: v1 e v2 confrontabili.
6. MONITORAGGIO: le performance si misurano in produzione nel tempo; drift di dati = riallenamento programmato.

ERRORI TIPICI: leakage (informazioni future nei dati di training che in produzione non si hanno), ottimizzare l'accuratezza quando il costo degli errori e' asimmetrico (meglio chiamare 10 lead in piu' che perderne 1 buono), fidarsi del leaderboard del training invece dei dati reali.

L'ANALOGIA EDILE: il modello e' la gru — imponente e necessaria — ma il cantiere funziona per fondamenta (dati), viabilita' (pipeline), collaudi (valutazione) e manutenzione (monitoraggio). Comprare la gru prima di scavare e' il fallimento tipico."""),

rec("DAE-004","data_ai","finetuning_llm","FINE-TUNING E VALUTAZIONE DI LLM: QUANDO E COME SPECIALIZZARE",
"""Auratrix stesso e' il caso d'uso: quando e come specializzare un LLM oltre il prompt.

LA GERARCHIA DELLE SOLUZIONI (dalla piu' economica):
1. PROMPT ENGINEERING: costo zero, niente infrastruttura. Copre piu' di quanto si pensi.
2. RAG: il modello generale + i tuoi documenti nel contesto (corpus del progetto). Primo passo per conoscenza aziendale: sempre aggiornata senza riallenamenti.
3. FINE-TUNING: si riallena il modello su esempi di comportamento desiderato (risposte nello stile aziendale, formati di documenti, terminologia). Serve quando vuoi cambiare COMPORTAMENTO/stile, non aggiungere fatti (per i fatti: RAG).
4. MODELLO PROPRIETARIO DA ZERO: solo a scale industriali.

COME FUNZIONA IL FINE-TUNING PRATICO:
- FORMATO: coppie (istruzione, risposta ideale) — migliaia di esempi di qualita', non milioni di riga mediocre. La qualita' degli esempi batte la quantita'.
- METODI: LoRA/QLoRA — addestrano piccoli adapter invece di tutti i pesi: fattibile su una singola GPU, costi accessibili.
- BASE: partire da un modello open (Llama, Mistral, Qwen) con licenza compatibile, valutato sui propri compiti.

LA VALUTAZIONE (il collaudo):
- Dataset di valutazione separato, rappresentativo, NON visto in training;
- Giudici automatici per i compiti strutturati (esattezza del JSON prodotto, presenza delle voci obbligatorie);
- Giudizio umano campionato per la qualita' libera;
- Confronto A/B contro la versione precedente su task reali.

REGOLA DECISIVA: prima si misura cosa NON riesce con prompt + RAG; il fine-tuning si fa sull'ultimo miglio che quei due non coprono."""),

rec("DAE-005","data_ai","llmops","LLMOPS: FARE FUNZIONARE L'AI IN PRODUZIONE",
"""Un LLM in produzione e' un servizio software come gli altri, con tre esigenze extra: costi a consumo, output non deterministici, rischi di contenuto.

ARCHITETTURA DI SERVIZIO:
- CACHING SEMANTICA: domande simili -> risposta in cache: riduce costi e latenza del 30-60% sui carichi ripetitivi.
- GUARDIE DI INPUT/OUTPUT: classificatori che bloccano prompt injection, dati sensibili in uscita, contenuti vietati. La validazione dell'output e' obbligatoria prima di usarlo (JSON schema, voci attese).
- FALLBACK: se il modello principale e' giu' o lento: modello piu' piccolo, risposta cached, o coda di retry. L'utente non deve mai vedere l'errore grezzo.

COSTI E LATENZA:
- Il costo si misura per token: prompt lunghi = costo e latenza. Ottimizzare il contesto (RAG selettivo invece di tutto il manuale incollato).
- Streaming della risposta: l'utente vede subito l'inizio mentre il modello scrive.
- Modelli piccoli per i task semplici (classificare un'email non serve GPT), grandi solo dove servono.

OSSERVABILITA' AI: loggare prompt, risposta, modello, versione, costo, latenza, feedback utente. Le regressioni si vedono dai dati: se dal 14 ottobre le risposte sui preventivi peggiorano, si vuole poterlo dimostrare e risalire al cambiamento.

TEST PER L'AI: dataset di casi di test con risposte attese, eseguiti a ogni cambio di modello/prompt/versione — il CI/CD vale anche per l'AI.

PRINCIPIO: l'AI in produzione si tratta come un servizio critico: SLO, allarmi, runbook di fallback. L'unica differenza: il servizio talvolta improvvisa."""),
]

rete = [
rec("NET-001","rete_sistemi","networking_dev","NETWORKING PER SVILUPPATORI: TCP, DNS, TLS IN PRATICA",
"""Chi sviluppa software che viaggia in rete deve sapere cosa succede tra il click e la risposta.

IL VIAGGIO DI UNA RICHIESTA:
1. DNS: il dominio diventa un indirizzo IP. Attenzione: TTL troppo lunghi rendono dolorose le migrazioni; record giusti (A per server, CNAME per alias, MX per posta).
2. TCP: la connessione affidabile — handshake a 3 vie, ritrasmissione dei pacchetti persi, ordinamento. Le connessioni TCP che 'restano appese' sono dietro i timeout misteriosi: i timeout devono essere configurati SEMPRE.
3. TLS: la crittografia (gia' nel corpus sicurezza): il TLS 1.3 negozia in una round-trip, certificato valido e rinnovato automaticamente.
4. HTTP: la richiesta/risposta: metodi, header, status code (corpus base).

FENOMENI CHE BISOGNA RICONOSCERE:
- LATENZA vs BANDA: un sito leggero ma con 40 richieste sequentiali soffre la latenza, non la banda. HTTP/2 e HTTP/3 mitigano con multiplexing e QUIC (UDP).
- CONNECTION POOL: riusare le connessioni invece di rifare handshake a ogni chiamata — il database e le API esterne vanno in pool, mai connessioni a piacimento.
- TIMEOUT A STRATI: ogni chiamata esterna con timeout; il timeout totale < somma dei timeout interni, altrimenti il chiamante muore prima delle risposte.

DIAGNOSI: ping/traceroute (percorso), dig (DNS), curl -v (la conversazione HTTP esatta), ss/netstat (connessioni aperte). Quattro strumenti che risolvono l'80% dei misteri di rete."""),

rec("NET-002","rete_sistemi","http_caching","HTTP AVANZATO E CACHING WEB: IL PROTOCOLLO COME CONTRATTO",
"""HTTP sembra semplice ma ha un contratto preciso: header che trasformano completamente il comportamento.

HEADER CHE DECIDONO:
- Cache-Control: la policy di caching ('max-age=3600, immutable' per gli asset versionati; 'no-store' per i dati sensibili).
- ETag / If-None-Match: 'ho la versione X, e' cambiata?' — risposta 304 senza corpo: risparmio di banda e tempo.
- Vary: quali header influenzano la cache (Accept-Encoding per la compressione).
- CORS: chi puo' chiamare l'API dal browser — configurare esplicitamente origini, metodi, header, mai '*' con credenziali.

COOKIES E SESSIONI: Secure, HttpOnly (invisibili a JavaScript: anti-XSS), SameSite=Lax/Strict (anti-CSRF). Il trio attivo sempre sulle sessioni.

COMPRESSIONE: gzip/brotli sui testi (HTML/JSON/CSS), mai sulle immagini gia' compresse.

REDIRECT: 301 (permanente: i motori aggiornano), 302 (temporaneo), 307/308 (il metodo si conserva — il POST resta POST). Le catene di redirect rubano latenza: mai A->B->C->D.

API DI STREAMING: SSE (server-sent events) per dati in push testuali semplici; WebSocket per comunicazione bidirezionale real-time (chat, presenza); webhooks per eventi tra server.

REGOLA: ogni header HTTP ha un motivo d'esistere e un default che a volte tradisce: leggere la specifica una volta per i dieci header che si usano di piu' cambia la qualita' del software."""),

rec("NET-003","rete_sistemi","transazioni","TRANSAZIONI E LIVELLI DI ISOLAMENTO: LA CORRETTEZZA DEI DATI",
"""La transazione e' l'unita' indivisibile di lavoro sul database: ACID e' la garanzia che il denaro non sparisce nel mezzo.

ACID:
- ATOMICITA': tutto o niente — se il preventivo si salva ma le voci falliscono, si annulla tutto.
- CONSISTENZA: i vincoli restano veri (importi non negativi, chiavi presenti).
- ISOLAMENTO: le transazioni concorrenti non si sporcano a vicenda.
- DURABILITA': scritto = scritto (anche se il server cade dopo il commit).

I LIVELLI DI ISOLAMENTO (dal piu' debole al piu' forte):
- READ UNCOMMITTED: si leggono anche i dati non ancora confermati — quasi mai giusto.
- READ COMMITTED: solo dati committati. Possibile lettura non ripetibile (tra due SELECT cambia qualcosa).
- REPEATABLE READ: la stessa SELECT dara' lo stesso risultato. Previene la lettura sporca.
- SERIALIZABLE: come se le transazioni girassero una alla volta. Massima sicurezza, piu' conflitti.

FENOMENI DA CONOSCERE:
- RACE CONDITION: due utenti comprano l'ultimo pezzo contemporaneamente — si risolve con UPDATE ... WHERE stock > 0 e controllo delle righe toccate, o locking pessimista/ottimista (version column).
- DEADLOCK: due transazioni che si aspettano a vicenda: il database ne uccide una; il codice deve gestire il retry.
- N+1 e transaction boundary: le transazioni corte (la connessione e' risorsa condivisa), mai chiamate esterne dentro una transazione (rete lenta = lock tenuti per minuti = disastro).

REGOLA: la transazione racchiude SOLO le scritture correlate; ogni altro lavoro (email, chiamate API) va dopo il commit."""),

rec("NET-004","rete_sistemi","replicazione_dr","REPLICAZIONE, BACKUP E DISASTER RECOVERY: QUANDO IL DISCO MUORE",
"""I dischi muoiono, i data center vanno giu', gli operatori cancellano la tabella sbagliata: la domanda e' quanto velocemente si torna.

LE FORME DI REPLICAZIONE:
- PRIMARIO/SECONDARIO (replica): le scritture vanno al primario, le letture possono andare ai secondari. Leggere dalla replica = scalare le letture. Costo: lag (il secondario e' indietro di qualche secondo): l'utente che salva e ricarica potrebbe non vedere i suoi dati — 'read your own writes' va al primario.
- SINCRONA vs ASINCOLA: sincrona = zero perdita, piu' latenza; asincrona = veloce, perdi gli ultimi secondi in caso di morte del primario. Scelta consapevole, mai default inconsapevole.

BACKUP: la regola 3-2-1 (tre copie, due supporti, una fuori sede) — automatizzato e con VERIFICA: un backup mai ripristinato tecnicamente non esiste. Test di ripristino programmato (una volta al trimestre minimo).

DISASTER RECOVERY — LE DUE CIFRE DA DEFINIRE:
- RPO (Recovery Point Objective): quanti dati si possono permettere di perdere? 'Al massimo 5 minuti' -> backup/replica ogni 5 minuti.
- RTO (Recovery Time Objective): quanto tempo per tornare operativi? 'Entro 1 ora' -> procedure pronte, documentate, provate.
Questi numeri guidano l'investimento: RPO/RTO di zero costano un capitale; accettare 1 ora di perdità cambia completamente la progettazione.

ALTA DISPONIBILITA': eliminare i single point of failure: due istanze dietro load balancer, database con failover automatico, healthcheck veri (che verificano dipendenze, non solo 'sono vivo').

PRINCIPIO: la disponibilita' non si compra: si costruisce eliminando i punti singoli di rottura, uno per volta."""),

rec("NET-005","rete_sistemi","performance_systems","PERFORMANCE DI SISTEMA: PROFILING, FLAME GRAPH E IL METODO SCIENTIFICO",
"""Quando il sistema e' lento, il metodo scientifico batte l'intuizione ogni volta.

IL CICLO: ipotesi -> misura -> modifica -> verifica. Senza misura si ottimizza la parte sbagliata nel 90% dei casi.

GLI STRUMENTI:
- PROFILING CPU: dove passa il tempo di calcolo? I flame graph (un rettangolo per funzione, larghezza = tempo) mostrano la torre: spesso il 70% del tempo vive in due funzioni ignorate.
- PROFILING MEMORIA: chi alloca? Leak (cresce all'infinito) e allocazioni superflue (GC sotto pressione).
- TRACING DISTRIBUITO: dove va il tempo di una richiesta che attraversa 5 servizi? (corpus osservabilita': la colonna tracing).
- APM (Application Performance Monitoring): dati di produzione continui, per richiesta: il punto dove i problemi reali si vedono.

LE CLASSICHE CAUSE TROVATE DALLA MISURA:
1. N+1 query (il campione assoluto): 1 query + 400 query figlie. La fix e' una JOIN o una batch: da 4 secondi a 40ms.
2. Chiamate seriali che potrebbero essere parallele (Promise.all).
3. Algoritmo quadratico su dati cresciuti (corpus complessita').
4. Mancanza di indice apparso solo con la dimensione reale dei dati.
5. Lock di database tenuti troppo a lungo.

BENCHMARK ONESTI: misurare su dati realistici (1000 righe di test nascondono i problemi da 10 milioni), piu' run (media e varianza, non il singolo run fortunato), ambiente stabile.

REGOLA FINALE: 'premature optimization is the root of all evil' — ma la misura prematura e' il root di tutto il bene. Si misura sempre, si ottimizza solo cio' che la misura accusa."""),
]

craft = [
rec("CRF-001","craft","legacy_code","LAVORARE SU CODICE LEGACY: LA MINIERA SENZA MAPPE",
"""Il codice legacy e' il lavoro quotidiano della maggior parte degli sviluppatori: va trattato come un cantiere occupato — non si demolisce tutto, si rinnova stanza per stanza.

IL METODO DELLO STRANGLER FIG (fico strangolatore):
1. Metti un proxy davanti al sistema vecchio (una nuova interfaccia/API).
2. Implementa UNA funzionalita' nuova nel sistema nuovo, dietro lo stesso proxy.
3. Una funzionalita' alla volta, il nuovo sistema 'strangola' il vecchio: alla fine il vecchio e' un guscio vuoto e si spegne.
Vantaggio: mai il grande riscrittura (che fallisce nel 70% dei casi e intanto il business ferma), sempre valore consegnato.

LE REGOLE DI SOPRAVVIVENZA:
- CARATTERIZZAZIONE prima del cambiamento: scrivere test che documentano il comportamento ATTUALE (anche se sbagliato) — il comportamento e' un contratto con gli utenti: si cambia solo consapevolmente.
- Cambiamenti piccoli, verificabili, reversibili.
- Le 'seam' (cuciture): i punti dove il codice puo' essere modificato senza toccare tutto — trovarli e usarli; i punti senza cuciture vanno creati prima con piccoli refactor.
- Il Boy Scout Rule applicato al legacy: ogni file toccato esce un po' migliore.

MINDSET: il codice legacy e' un documento storico: ogni struttura strana e' probabilmente la cicatrice di un requisito dimenticato. Prima di giudicare, capire COSA risolveva.

QUANDO INVECE RISCRivere: tecnologia al capolinea di supporto, costo di cambiamento misurato superiore al rifacimento, requisiti cambiati radicalmente. E anche allora: per pezzi."""),

rec("CRF-002","craft","stime_pianificazione","STIME E PIANIFICAZIONE TECNICA: PROMETTERE SENZA MENTIRE",
"""La stima e' il contratto tra sviluppo e business: la tecnica conta quanto il codice.

LE TECNICHE:
1. DECOMPOSIZIONE FINO ALL'ORA: stimare 'il modulo fatturazione' e' astrologia; stimare 'tabella + API + form + test' e' ingegneria. Le stime valide nascono da task da 0,5-2 giorni, mai da settimane intere.
2. STIME A RANGE CON CONFIDENZA: '2-4 giorni, confidenza media' onesta batte '3 giorni' sperata. La regola empirica: la stima ottimistica succede con il 10% di probabilita', quella pessimistica con il 90%.
3. PIANIFICAZIONE A PUNTI STORICA: i punti (story points) misurano la VELOCITA' del team nel tempo, non l'ore dell'uomo: la media delle ultime iterazioni e' il miglior predittore delle prossime.
4. IL BUFFER ESPLICITO: l'incertezza si nomina ('il 30% di rischio su questa integrazione'), non si nasconde nel task.

LE TRAPPOLE PSICOLOGICHE:
- ANCORA: la prima cifra detta condiziona tutto — buttare giu' la propria stima PRIMA di sentire quella altrui.
- OTTIMISMO DEL VENDITORE: chi stima e' spesso chi vorrebbe dire di si': separare chi stima da chi commercia.
- EFFETTO PIANIFICAZIONE: aggiungere persone a un progetto in ritardo lo rallenta (Brooks): la stima non scala linearmente con il team.

GESTIONE DEI CAMBIAMENTI: il requisito che cambia a cantiere aperto e' normale: si tratta con la stessa disciplina del sopraggiunto edile — impatto valutato, prezzo/tempo rinegoziati, mai assorbito in silenzio.

PRINCIPIO: una stima e' una previsione con livello di confidenza: dire anche il livello e' parte della competenza."""),

rec("CRF-003","craft","regex_parsing","ESPRESSIONI REGOLARI E PARSING: LEGGERE E SCRIVERE LINGUAGGI",
"""Le regex sono un linguaggio nel linguaggio: potentissime per i testi, pericolosissime usate male.

REGOLE D'ORO DELLE REGEX:
1. SI usano per: validare formati (email, CAP, P.IVA), estrarre pattern (date, codici), sostituizioni puntuali.
2. NON si usano per: parsing HTML/XML/JSON strutturati (ci sono parser dedicati: BeautifulSoup, DOM — la regex su HTML e' fragile per definizione), logica annidata profonda.
3. LEGGIBILITA': flag verbose, gruppi nominati ('(?P<anno>\\d{4})'), commenti: una regex illeggibile e' codice illeggibile.
4. PERFORMANCE: catastrofic backtracking — pattern con quantificatori annidati ('(a+)+') su input ostili bloccano la CPU per ore. Sintomo: regex che 'gira' senza finire. Catastrophic backtracking si previene con possessive quantifiers o atomic groups.
5. TESTARE su casi reali: edge case con input vuoti, unicode, newline.

IL PARSING OLTRE LA REGEX: quando il formato e' un vero linguaggio (espressioni, config, mini-linguaggi di dominio), la strada e' il parser: tokenizer (spezza in token) + parser (ricostruisce la struttura secondo la grammatica). I parser combinators (in molti linguaggi) rendono scrivere parser piccoli un lavoro da un pomeriggio — apre a DSL edili ('linguaggio' per descrivere voci di computo?).

CASO D'USO EDILE: estrarre le voci da un testo di capitolato grezzo, validare i codici articolo del listino, normalizzare i CSV dei fornitori: regex + parser ben usati automatizzano ore di copia-incolla.

REGOLA FINALE: 'ora hai due problemi' scherza sulle regex: vero solo quando la regex diventa il problema invece dello strumento."""),

rec("CRF-004","craft","shell_automazione","SHELL SCRIPTING E AUTOMAZIONE: IL CANTIERE DIGITALE",
"""La shell e' il cantiere dove il professionista automatizza il ripetitivo: chi la padroneggia guadagna ore ogni settimana.

LE BASI CHE CAMBIANO LA GIORNATA:
- PIPE E COMPOSIZIONE: comandi piccoli che si concatenano ('cat log | grep ERRORE | awk '{print $5}' | sort | uniq -c | sort -rn') — ogni problema di testo e' cinque comandi lontano.
- REDIREZIONE: '>' sovrascrive, '>>' aggiunge, '2>' l'errore, '| tee' vede e salva.
- VARIABILI, CICLI, CONDITION: il minimo per gli script di automazione.
- EXIT CODE e set -euo pipefail: ogni comando ritorna successo/fallimento: gli script seri falliscono rumorosi al primo problema, non continuano nel caos.
- CRON/SYSTEMD TIMERS: l'automazione che gira da sola (backup, export, report): output sempre loggato, email/alert su errore.

QUANDO LO SCRIPT BASTA E QUANDO NO: script per sequenze di comandi, trasformazioni, orchestrazione di tool. Quando servono test, strutture dati complesse, gestione errori ricca: meglio Python (che e' sulla macchina di chiunque). La soglia: 50-100 righe di bash = candidato a diventare Python.

AUTOMAZIONI TIPO PER UNA REALTA' EDILE/DIGITALE: export giornalieri dal gestionale, rinomina e archiviazione fatture, controllo scadenze documenti con alert, report settimanale automatico, sincronizzazione listini fornitori.

SICUREZZA DEGLI SCRIPT: mai comandi con input non quotato ($VAR va tra virgolette sempre: il path con spazio altrimenti esplode), permessi minimi, segreti mai negli script versionati (variabili d'ambiente).

PRINCIPIO: se lo fai due volte, automatizzalo al terzo: l'investimento e' di minuti e rende per sempre."""),

rec("CRF-005","craft","lettura_codice","LEGGERE IL CODICE: LA COMPETENZA NASCOSTA DEI MIGLIORI",
"""I migliori sviluppatori leggono piu' codice di quanto ne scrivano: la lettura e' un'abilita' allenabile con metodo.

IL METODO DI LETTURA STRATEGICA:
1. DAL CONTRATTO: prima i tipi/le interfacce/le firme: cosa il modulo promette? Poi l'implementazione: come lo mantiene?
2. TOP-DOWN: entry point -> chiamate principali -> dettagli solo dove serve. Non leggere riga per riga: e' come studiare una citta' parola per parola invece che dalla mappa.
3. SEGUI LA DOMANDA: arrivare al codice con una domanda ('come viene calcolato lo sconto?') e lasciare che la domanda guidi il percorso.
4. IL GRAFO DELLE DIPENDENZE: chi chiama chi: strumenti come il 'go to reference' dell'IDE sono il GPS.

LEGGERE CODICE ALTRUI (open source): scegliere progetti di qualita' nota (il codice dei tool che usi: git, Django, requests) e leggerli come si leggono i classici: come sono organizzati i moduli, come gestiscono gli errori, come commentano.

COSA CERCARE NEL CODICE BUONO:
- come si entra e si esce dalle risorse (file, connessioni);\n- come si valida l'input esterno;\n- come si nomina e si struttura;\n- come si testa;\n- come si documenta il perche'.\n
LEGGERE CODICE CATTIVO (legacy): la tecnica della 'caratterizzazione': annotare cosa fa realmente (non cosa dice di fare), poi ragionare sul perche'. Il codice cattivo e' spesso codice buono invecchiato male: la storia spiega.

ESERCIZIO SETTIMANALE: leggere un modulo open source alla settimana, 30 minuti, prendendo appunti sulle tecniche viste. In un anno: cinquanta architetture diverse nella testa — il bagaglio che separa i livelli."""),
]

progetti = [
rec("PRG-001","progetti","cli_tool","PROGETTO GUIDATO: COSTRUIRE UN CLI PROFESSIONALE",
"""Il CLI (command line interface) e' il progetto perfetto per imparare: ambito chiuso, risultati verificabili, utilita' reale.

SPECIFICA: un tool 'preventivo-cli' che legge un file voci (JSON/YAML) e genera il preventivo: calcolo voci, subtotali, IVA, sconto, output testo e PDF.

ARCHITETTURA:
- ENTRY POINT: argomenti con una libreria (argparse/click/commander): 'preventivo-cli genera voci.yaml --iva 22 --sconto 5'.
- CORE PURO: le funzioni di calcolo senza I/O — testabilissime: calcola_subtotale(voci), applica_sconto(totale, pct), arrotonda_euro(importo) (banker's rounding: le regole contabili esistono — Decimal invece di float!).
- I/O PERIFERICO: lettura file, output PDF in funzioni separate dal core.
- ERRORI: file mancante, YAML malformato, voci senza prezzo — messaggi che dicono cosa correggere.

DISCIPLINE CHE SI IMPARANO:
- DECIMAL per i soldi: i float binari fanno 0.1+0.2=0.30000000004: i centesimi contano.
- TEST: ogni regola di calcolo con i suoi casi (sconto 0%, arrotondamenti, voci vuote).
- PACKAGING: installabile con pip/npm, versione, README con esempi.
- PUBBLICAZIONE: su PyPI/npm registry.

ESTENSIONI PROGRESSIVE: templati PDF diversi per cliente, lettura diretta da CSV listino, comando 'confronta' tra due versioni del preventivo (diff dei prezzi: l'evoluzione naturale verso il configuratore del corpus base).

CRITERIO DI FINE: un collega che non ha mai visto il progetto lo installa e lo usa seguendo solo il README."""),

rec("PRG-002","progetti","api_completa","PROGETTO GUIDATO: UNA REST API COMPLETA E PRODUTTIVA",
"""Progetto: 'cantiere-api' — la spina dorsale del gestionale: clienti, cantieri, voci preventivo, con autenticazione e test.

STACK: FastAPI (Python) o NestJS (TypeScript) + PostgreSQL + Docker + pytest.

LE FASI (ognuna con i suoi deliverable):
1. FONDAMENTA: struttura a layer (routers -> services -> repositories -> models), configurazione per ambiente (env vars), connessione DB con pool, migrazioni (Alembic).
2. AUTENTICAZIONE: registrazione/login con bcrypt, JWT con scadenza, ruoli (admin/site_manager/viewer) — dal corpus sicurezza: mai inventare, mai salvare password in chiaro.
3. CRUD COMPLETO: clienti e cantieri con validazione (Pydantic/zod), paginazione, filtri, ordinamento — il 90% delle API e' questo fatto bene.
4. TEST: unitari sulle regole (il calcolo dello stato avanzamento), di integrazione sugli endpoint (testcontainer: database vero nei test), copertura dei percorsi felici E degli errori (401, 403, 404, 409, 422).
5. PRODUZIONE: Dockerfile, CI/CD (lint+test+build+deploy), healthcheck endpoint, logging strutturato, rate limiting.

LE DECISIONI DIDATTICHE CHIAVE:
- errore HTTP giusto per ogni caso (409 quando esiste gia', 422 per validazione, 404 con messaggio utile);\n- transazioni sulle operazioni multi-tabella;\n- indici sulla colonna piu' cercata (cliente_id);\n- OpenAPI auto-generato come documentazione.\n
CRITERIO DI FINE: un front-end esterno puo' integrarsi usando solo l'OpenAPI, e una modifica futura (aggiungere la tabella 'materiali') richiede mezza giornata — segno che l'architettura tiene."""),

rec("PRG-003","progetti","rag_system","PROGETTO GUIDATO: SISTEMA RAG SUI DOCUMENTI AZIENDALI",
"""Progetto: 'manuale-ai' — chiedi in italiano ai documenti aziendali (capitolati, norme, listini) e ottieni risposte con la fonte.

ARCHITETTURA MINIMA (ogni componente e' un modulo di studio):
1. INGESTIONE: caricamento documenti (PDF/DOCX/markdown), pulizia, spezzettamento in chunk (400-800 token, con sovrapposizione: un concetto non deve spezzarsi a meta').
2. EMBEDDING: ogni chunk diventa un vettore numerico (modelli open come bge-m3 o API). La similarita' coseno misura la vicinanza semantica.
3. DATABASE VETTORIALE: pgvector su Postgres e' sufficiente fino a milioni di chunk — niente servizio extra.
4. RETRIEVAL: la domanda dell'utente diventa vettore -> top-5 chunk piu' simili.
5. GENERAZIONE: i chunk + la domanda nel prompt del LLM, con istruzione di citare la fonte; risposta con riferimento al documento e pagina.
6. INTERFACCIA: chat web minima (streamlit/gradio va benissimo).

I PROBLEMI VERI CHE SI IMPARANO A RISOLVERE:
- chunk sbagliati = risposte sbagliate: titoli ripetuti nei chunk, metadati (documento, sezione) allegati;\n- domande fuori dominio: il sistema deve dire 'non lo so' invece di inventare — prompt di istruzione + soglia di similarita';\n- valutazione: 20 domande di test con risposte attese, ri-eseguite a ogni modifica.\n
ESTENSIONI: hybrid search (vettoriale + keyword), reranking, accessi per utente (un cliente non vede i documenti di altri).

CRITERIO DI FINE: sui 20 casi di test, il sistema risponde correttamente con fonte nella stragrande maggioranza — ed e' misurabile."""),

rec("PRG-004","progetti","chatbot_tool","PROGETTO GUIDATO: CHATBOT CON STRUMENTI (AGENTE MINIMO)",
"""Progetto: 'assistente-cantiere' — il bot Telegram/WhatsApp che risponde ai collaboratori: 'a che ora iniziamo domani?', 'registra nota: serramenti consegnati', 'quanto e' il preventivo Rossi?'.

ARCHITETTURA (dal corpus AI coding):
1. L'LLM riceve il messaggio + la lista degli STRUMENTI disponibili (function calling): cerca_cantiere(data), registra_nota(testo), cerca_preventivo(cliente).
2. Il bot (il tuo codice) intercetta la richiesta di chiamata, VALIDA i parametri e esegue davvero la query sul database.
3. Il risultato torna all'LLM che compone la risposta naturale.
4. La memoria conversazionale: i messaggi recenti nel contesto (finestra limitata: ultimi 10 turn).

GUARDIE (ciò che separa il giocattolo dallo strumento):
- validazione parametri prima di eseguire ('registra nota' accetta testo < 500 caratteri);\n- conferma per le azioni distruttive ('vuoi davvero cancellare la nota 12? conferma con si');\n- log di ogni azione (chi, cosa, quando);\n- il bot dice 'non posso' per le richieste fuori dagli strumenti — niente improvvisazione libera sui dati.\n
STACK REALE: n8n o Python (aiogram + chiamate API LLM), database SQLite/Postgres, deploy su una VPS piccola.

DISCIPLINE APPRESE: function calling, gestione contesto, sicurezza dei bot (non eseguire mai comandi arbitrari che l'LLM propone), UX conversazionale (risposte brevi, bottone di conferma, gestione del 'non ho capito').

CRITERIO DI FINE: tre collaboratori reali lo usano per due settimane senza che il titolare debba intervenire."""),

rec("PRG-005","progetti","parser_dsl","PROGETTO GUIDATO: MINI-LINGUAGGIO PER VOCI DI COMPUTO",
"""Progetto avanzato: un parser per un linguaggio mini di descrizione voci — dove il software diventa linguaggio, il livello piu' alto del craft.

L'IDEA: descrivere voci di computo in testo quasi naturale strutturato:
'voce Muratura perimetrale\n mq 45\n prezzo 85.50\n categoria Murature\n cantiere ViaRoma'
e ottenere oggetti validati con calcoli.

LE FASI:
1. GRAMMATICA: definire la sintassi esplicita (EBNF): quali parole chiave, quali campi obbligatori, formato dei numeri.
2. TOKENIZER: spezzare il testo in token (parola chiave, numero, identificatore, newline) — 50 righe con una regex mirata o una libreria.
3. PARSER: ricostruire la struttura secondo la grammatica — ricorsione per le sezioni annidate ('voce' contiene 'attivita'?). Errori con riga e spiegazione ('riga 7: atteso 'prezzo', trovato 'prezzzo'').
4. SEMANTICA: validazione incrociata (la categoria esiste nel database? il prezzo e' positivo?), costruzione degli oggetti di dominio.
5. GENERAZIONE: export verso il computo (JSON/CSV/PDF) — ora il linguaggio e' una porta d'ingresso umana al gestionale.

PERCHE' E' IL PROGETTO PIU' FORMATIVO: unisce lexer/parser (corpus regex/parsing), design dei linguaggi, domain modeling (DDD), errori di dominio, API. E insegna la lezione piu' profonda: i linguaggi migliori rendono il semplice facile e il complesso possibile.

VARIANTE RAGGIUNGIBILE: invece di inventare la grammatica, usare l'LLM come PARSER NATURALE: il testo libero -> JSON validato dallo schema -> stesso percorso. La versione 'AI-first' dello stesso progetto — confrontarle e' un esercizio da senior.

CRITERIO DI FINE: il progettista digita le voci in un editor e vede il computo aggiornarsi: il ciclo completo dal linguaggio al dato."""),
]

corpora = [
    ("devops_infrastruttura.jsonl", devops),
    ("frontend_master.jsonl", frontend),
    ("data_ai_engineering.jsonl", data_ai),
    ("rete_sistemi.jsonl", rete),
    ("craft_avanzato.jsonl", craft),
    ("progetti_guidati.jsonl", progetti),
]

total = 0
for fname, recs in corpora:
    path = os.path.join(BASE, fname)
    with open(path, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    total += len(recs)
    print(f"{fname}: {len(recs)} schede")
print(f"TOTALE: {total} schede")
