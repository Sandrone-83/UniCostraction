# -*- coding: utf-8 -*-
"""Coding_Master_Pack_5: 20 schede — cinque aree mai coperte (IR, query engines, architettura, build, knowledge graph)."""
import json, os

BASE = r"C:\Users\alessandro\Documents\kimi\tasks\2026-09-26\15-14-07-e3d653af\Coding_Master_Pack_5\parsed"
os.makedirs(BASE, exist_ok=True)

LIC = "Sintesi didattica originale Kimi (pubblico dominio)"
ATT = "Corpus coding master 5 a cura di Kimi"

def rec(id_, cat, tema, title, text):
    return {"id": id_, "categoria": cat, "tema": tema, "title": title, "text": text,
            "source": f"coding_master_5_{cat}_kimi", "license": LIC, "commercial_ok": True,
            "attribution": ATT, "url": ""}

ir = [
rec("IRS-001","information_retrieval","motori_ricerca","COME FUNZIONA UN MOTORE DI RICERCA: INDICE INVERTITO E BM25",
"""Ogni volta che cerchi in un sito, in Elasticsearch o in un archivio documenti, dietro c'e' un motore di ricerca informato: l'information retrieval e' la disciplina.

L'INDICE INVERTITO: la struttura dati fondamentale:
- INDICE DIRETTO: documento -> parole;\n- INDICE INVERTITO: parola -> lista dei documenti che la contengono (con posizioni). 'calcestruzzo' -> [doc3, doc7, doc12...]. La ricerca diventa unione/intersezione di liste: istantanea anche su milioni di documenti.\n\n"
"LA PIPELINE DI INDICIZZAZIONE:\n1. TOKENIZZAZIONE: spezzare il testo in token ('cantiere' -> 'cantiere'; attenzione a punteggiatura, apici, lingue);\n2. NORMALIZZAZIONE: lowercase, rimozione accenti, stopword (le parole vuote: 'il', 'di', 'che' — quasi sempre rimosse);\n3. STEMMING/LEMMAZZAZIONE: ridurre le parole alla radice ('costruzione', 'costruire' -> 'costru') — in italiano va fatta con cautela: il lemma spesso batte lo stem;\n4. INDICE: token -> documenti con posizioni e frequenze.\n\n"
"BM25 (IL RANKING CLASSICO): la formula standard per ordinare i risultati:\n- TERM FREQUENCY: piu' volte appare il termine, piu' e' rilevante (con saturazione: dopo un po' non conta piu');\n- INVERSE DOCUMENT FREQUENCY: termini rari ('armatura', 'pozzetto') pesano piu' di termini comuni;\n- LUNGHEZZA DEL DOCUMENTO: i documenti corti vincono a parita' di termini.\nBM25 e' il punto di partenza: Elasticsearch, OpenSearch, Solr lo usano.\n\n"
"QUERY LOGICHE: AND (intersezione, precisa), OR (unione, larga), frasi esatte ('cappotto termico' come sequenza), wildcard e fuzzy (edit distance: trova 'ponteggio' anche scritto male).\n\n"
"PERCHE' IMPORTA QUI: il corpus RAG costruisce sopra questi motori: chi capisce l'indice invertito capisce perche' un documento viene recuperato o perso."""),

rec("IRS-002","information_retrieval","valutazione_ricerca","VALUTARE UN MOTORE DI RICERCA: PRECISION, RECALL E RELEVANCE",
"""Un motore di ricerca si migliora solo se si misura: le metriche di information retrieval valgono per ogni sistema che recupera dati.

I CONCETTI BASE:
- RELEVANCE (rilevanza): un giudizio umano 'questo documento risponde a questa domanda?' — si costruisce un GROUND TRUTH: 50-100 query reali con i documenti rilevanti attesi.\n- PRECISION: tra i risultati restituiti, quanti erano rilevanti? ('ne ho mostrati 10, 7 utili = 0.7');\n- RECALL: tra tutti i documenti rilevanti che esistono, quanti ne ho trovati? ('ce n'erano 20, ho trovato 7 = 0.35');\n- IL TRADE-OFF: precision e recall si combattono: allargare la ricerca alza la recall e abbassa la precision. Il F1 score li combina.\n\n"
"LE METRICHE PER RANKING (l'ordine conta):\n- PRECISION@K: la precision sui primi K risultati ('i primi 5 sono tutti buoni?');\n- RECALL@K e NDCG: la posizione pesa: un documento rilevante al primo posto vale piu' che al decimo (graded relevance: 3=perfetto, 2=utile, 1=marginale).\n\n"
"IL METODO DI MIGLIORAMENTO:\n1. raccogli query REALI degli utenti (i log di ricerca sono oro);\n2. costruisci il ground truth;\n3. misura;\n4. intervieni sul punto debole specifico (tokenizzazione italiana? sinonimi? abbreviazioni edilizie?);\n5. rimisura: la regressione si vede subito.\n\n"
"SINONIMI E ONTOLOGIE: 'cappotto' = 'coibentazione esterna' = 'isolamento a parete': il lessico edilizia e' ricco di sinonimi e sigle (PSC, POS, SAL, CSE): i sinonimi vanno gestiti con liste controllate, query expansion o — meglio — il livello semantico vettoriale.\n\n"
"ERRORE TIPICO: migliorare 'a sentimento' senza ground truth: si ottimizza per i propri test, non per gli utenti."""),

rec("IRS-003","information_retrieval","vector_search","RICERCA VETTORIALE E ANN: HNSW E IL MOTORE DEI SISTEMI RAG",
"""La ricerca vettoriale (semantica) e' la seconda gamba dei sistemi RAG (corpus AI coding): qui la tecnologia in profondita'.

IL PRINCIPIO: ogni documento (o chunk) diventa un VETTORE numerico (embedding, tipicamente 384-3072 dimensioni) tale che documenti SIMILI per significato abbiano vettori VICINI (distanza coseno o euclidea). 'cappotto termico' e 'coibentazione della facciata' hanno vettori vicini anche senza parole in comune — cio' che la ricerca keyword non fa.

IL PROBLEMA: la ricerca esatta (k-NN) richiede di confrontare la query con OGNI vettore: su milioni di documenti e' troppo lento. La soluzione: ANN (Approximate Nearest Neighbor) — si sacrifica un po' di precisione per la velocita'.

L'ALGORITMO STANDARD (HNSW):
- HIERARCHICAL NAVIGABLE SMALL WORLD: un grafo a piu' livelli: in alto pochi nodi e salti lunghi; scendendo, sempre piu' nodi e passi corti. La ricerca: si salta in alto verso la zona giusta, si scende affinando. Risultato: ricerca su milioni di vettori in millisecondi con recall ~0.99.
- Le alternative: IVF (si divide lo spazio in regioni e si cerca solo nelle probabili), LSH (hashing locality-sensitive), product quantization (compressione dei vettori: 4x meno memoria).\n\n"
"I PARAMETRI CHE CONTANO: M (connessioni per nodo: piu' accuratezza, piu' memoria), ef (candidati esplorati: piu' recall, piu' lentezza), metrica di distanza (coseno per testi).\n\n"
"HYBRID SEARCH (LA PRATICA VINCENTE): vettoriale + keyword (BM25) combinati con RRF o pesi: la keyword garantisce le corrispondenze precise (sigle, codici, nomi propri — dove la semantica fallisce), la vettoriale copre i sinonimi. Poi il reranker (un modello cross-encoder) riordina i primi 20 risultati per precisione.\n\n"
"CASO RAG EDILE: 'cosa prevede il capitolato per le fondazioni?' — keyword trova i capitoli con 'fondazioni'; vettoriale trova anche le voci su 'platea', 'getto', 'pilotis'; insieme coprono il documento."""),

rec("IRS-004","information_retrieval","ir_rag_applicato","INFORMATION RETRIEVAL APPLICATO: MOTORI, OPENSEARCH E CICLO DI VITA",
"""L'IR dal laboratorio alla produzione: motori consolidati, schema di indicizzazione e operativita' nel tempo.

I MOTORI CONSOLIDATI:
- LUCENE: la libreria Java alla base di quasi tutto (indice invertito, BM25, query engine);\n- ELASTICSEARCH / OPENSEARCH: distribuiti, HTTP API, aggregazioni (il 'GROUP BY' dei motori di ricerca: 'quanti documenti per cantiere per anno'), sinonimi, highlight;\n- TYPESENSE / MEILIsearch: moderni, semplici, per app piu' piccole;\n- PG: la full-text search di Postgres (tsvector) copre il 70% dei casi semplici senza nuovo servizio — la scelta pragmatica di partenza.\n\n"
"LO SCHEMA DI INDICIZZAZIONE (il design che decide la qualita'):\n- CAMPI: titolo (peso alto), corpo (peso medio), tag/categoria (filtri esatti);\n- FILTRI (keyword non testuali): cantiere, anno, tipo documento — la combinazione testo+filtri e' il 90% delle query reali;\n- ANALYZER dedicati: italiano con elisioni e accenti;\n- SINONIMI: gestiti a indice (espansione) o a query.\n\n"
"IL CICLO DI VITA OPERATIVO:\n1. INDICIZZAZIONE INIZIALE: bulk con reindex dedicato;\n2. AGGIORNAMENTI INCREMENTALI: gli eventi di modifica (event sourcing del pack 4!) ri-indicizzano il documento: l'indice deve restare SINCRONO col database — pattern outbox applicato anche qui;\n3. MONITORAGGIO: query lente (slow query log), indice che cresce, shard mal bilanciati;\n4. EVOLUZIONE DELLO SCHEMA: la reindicizzazione completa e' il 'momento verita'' — pianificata, testata su copia.\n\n"
"REGOLA DI ARCHITETTURA: il database e' la fonte di verita', l'indice di ricerca e' una PROIEZIONE ricostruibile: si puo' sempre buttare e ricostruire — progettarlo cosi' fin dall'inizio toglie meta' dei rischi."""),
]

query_engines = [
rec("QRE-001","query_engines","pipeline_query","LA PIPELINE DI ELABORAZIONE DI UNA QUERY SQL",
"""Cosa fa davvero il database quando riceve una SELECT: la pipeline in sei fasi.

1. PARSING: il testo SQL diventa albero di sintassi (come ogni linguaggio — corpus compilatori); validazione di tabelle e colonne (la catena degli scope).\n2. RISCRITTURA: regole logiche: viste espanse, subquery appiattite, predicati spinti dentro le UNION.\n3. PLANNING: il cuore: il generatore di piani produce CANDIDATI: quali indici, quali ordini di join, quali algoritmi.\n4. OPTIMIZZAZIONE (cost-based): il calcolo dei costi: per ogni piano candidato si stima il costo (righe lette, I/O, CPU) con le statistiche delle tabelle (cardinalita', distribuzioni — per questo le statistiche vanno aggiornate: ANALYZE);\n5. L'ESECUTORE: esegue il piano (corpus QRE-002/003);\n6. IL RISULTATO.\n\n"
"LA VISTA DECISIVA: 'EXPLAIN' (o EXPLAIN ANALYZE) mostra il piano scelto: leggere un EXPLAIN e' la competenza che separa chi scrive SQL da chi scrive SQL efficiente: i segnali: SEQ SCAN su tabelle grandi (manca l'indice), nested loop su migliaia di righe (manca un indice di join), sort su disco (la memoria e' troppo poca), rows estimate sbagliate di 100x (statistiche obsolete).\n\n"
"IL PREPARATO: i database PREPARANO le query (prepared statements): parsing e planning una volta sola, esecuzione molte: per le query ad alta frequenza il guadagno e' reale (oltre alla protezione da SQL injection).\n\n"
"REGOLA PRATICA: quando una query e' lenta, il percorso e' sempre: EXPLAIN -> capire il piano -> intervenire (indice, riformulazione, statistiche) -> EXPLAIN di nuovo. Mai ottimizzare a tentativi."""),

rec("QRE-002","query_engines","algoritmi_join","GLI ALGORITMI DI JOIN: NESTED LOOP, HASH E MERGE",
"""Il join e' l'operazione piu' costosa del SQL: tre algoritmi, tre mondi.

1. NESTED LOOP: per ogni riga della tabella A, cercare le corrispondenti in B. Costo: |A| x |B|. Va bene SOLO quando una delle due e' minuscola (poche righe) o quando esiste un indice su B per la ricerca: allora per ogni riga di A la ricerca in B e' O(log n) — nested loop CON INDICE e' spesso la scelta giusta su tabelle piccole/medie.\n2. HASH JOIN: si costruisce una tabella hash sui valori della colonna di join della tabella piu' piccola; poi si scorre la grande una volta sola, con lookup O(1): costo lineare O(A+B). La scelta standard per i join su grandi tabelle SENZA indice. Limiti: la tabella piccola deve entrare in memoria (altrimenti si partiziona in piu' passate).\n3. MERGE JOIN: entrambe le tabelle ordinate per la colonna di join si fondono scorrendole in parallelo come due deck di carte: O(A log A + B log B). La scelta quando le tabelle sono gia' ordinate (indice clustered) o quando serve comunque l'ordinamento.\n\n"
"COME SCEGLIE IL DATABASE: il cost-based optimizer confronta le stime dei costi: nested loop per pochi risultati, hash join per grandi, merge join con ordinamenti disponibili.\n\n"
"COSA PUO' ANDARE STORTO (i casi famosi):\n- l'optimizer sceglie nested loop perche' STIMA pochissime righe (statistiche obsolete: ANALYZE risolve);\n- l'hash join satura la memoria e va su disco: si vede nel profile;\n- il join su espressioni ('ON LOWER(a.nome) = LOWER(b.nome)') INVALIDA gli indici: la svolta e' indici funzionali o colonne normalizzate.\n\n"
"IL TEST DI MATURITA' SQL: guardare un EXPLAIN con hash join + sort e sapere PERCHE' e' quello e se puo' migliorare."""),

rec("QRE-003","query_engines","ottimizzazione","OTTIMIZZAZIONE BASATA SUI COSTI: STATISTICHE, CARDINALITA' E TRAPPOLE",
"""L'optimizer cost-based e' un estimatore: la sua bonta' dipende dalle statistiche e dalle assunzioni.

LE STATISTICHE: per ogni tabella e indice il database conserva: numero di righe, distribuzione dei valori (istogrammi: 'quanti valori tra 10 e 20, tra 20 e 30...'), nullita', cardinalita' delle colonne. Con queste stima: 'quante righe passera' questo WHERE?' (selectivity). La stima guida TUTTO: l'ordine dei join, l'algoritmo, l'uso degli indici.\n\n"
"QUANDO LE STIME SBAGLIANO (e le query esplodono):\n1. STATISTICHE OBSOLETE: tabella raddoppiata dopo un bulk load: l'optimizer pianifica per 10.000 righe e ne trova 2 milioni: ANALYZE/AUTOVACUUM risolve;\n2. PREDICATI CORRELATI: 'WHERE citta = X AND quartiere = Y' — citta' e quartiere non sono indipendenti (ogni quartiere e' in UNA citta'): l'indipendenza e' un'assunzione dell'optimizer: le stime si sballano; le estensioni statistiche (extended statistics) correggono;\n3. FUNZIONI SULLE COLONNE: 'WHERE DATE(created_at) = '2026-09-29'' invalida l'indice su created_at: si riscrive 'created_at >= ... AND created_at < ...' (range sull'indice);\n4. PARAMETRI DI TROPPO: prepared statement con parametro generico: il piano e' ottimizzato per il valore medio: per valori estremi e' sbagliato (le soluzioni esistono: plan freezing, hint, ricompilazione);\n5. LIKE CON WILDCARD INIZIALE: 'LIKE '%termico'' non usa l'indice (l'albero B e' ordinato per prefisso): trigram indexes (pg_trgm) o full-text.\n\n"
"GLI HINT: la maggior parte dei database permette di FORZARE il piano: usare SOLO come cerotto: se l'optimizer sbaglia sistematicamente, il problema sono le statistiche o il modello, non l'optimizer.\n\n"
"PRINCIPIO: l'optimizer e' un estimatore statistico: si tratta come un collega bravo ma che lavora con dati di ieri: gli si danno dati freschi (ANALYZE) e query scritte in modo che possa capirle."""),

rec("QRE-004","query_engines","modelli_esecuzione","MODELLI DI ESECUZIONE: VOLCANO, VECTORIZED E CODE GENERATION",
"""Come il database esegue fisicamente il piano: tre modelli, da quarant'anni di evoluzione.

1. IL MODELLO VOLCANO (iterator): ogni operatore (scan, join, filter) e' un oggetto con open()/next()/close(): il next() chiede la riga successiva all'operatore sottostante: la pipeline e' una catena di chiamate ricorsive. Vantaggi: elegante, componibile, supporta il pipelining (il risultato scorre senza materializzarsi). Svantaggio: overhead virtuale per riga: funzione, controlli, stato — milioni di chiamate per query.\n2. VECTORIZED (a blocchi): gli operatori processano BATCH di righe (migliaia per volta) come array: meno chiamate, SIMD (istruzioni vettoriali CPU), cache-friendly: il modello dei database analitici moderni (VectorWise, ClickHouse, DuckDB — DuckDB e' quello del runtime Python connesso all'AI). Il guadagno su query analitiche e' 10-100x.\n3. CODE GENERATION: si compila a runtime codice specializzato per la query specifica (senza il generale-indiretto del volcano): Spark (whole-stage codegen), Hyper: la query diventa un programma ottimizzato dal compilatore JIT.\n\n"
"LA DISTINZIONE OLTP vs OLAP:\n- OLTP (operazioni): poche righe per query, molte query: vince il row-store + volcano/index;\n- OLAP (analisi): milioni di righe per query, poche query: vince il column-store (si leggono SOLO le colonne richieste — il motivo dei database analitici) + vectorized.\nE' la stessa ragione delle differenze di modellazione operativa vs warehouse (corpus data warehouse).\n\n"
"LE CONSEGUENZE PRATICHE:\n- un database 'generale' (Postgres) e' ottimizzato per l'OLTP: per l'analisi seria si aggiunge un motore analitico (DuckDB in-process, ClickHouse, BigQuery);\n- il formato colonna comprime meglio (valori simili vicini) — i warehouse costano meno di quanto sembri;\n- capire il modello spiega i risultati dei benchmark 'strani'.\n\n"
"REGOLA: la domanda 'OLTP o OLAP?' viene PRIMA di quasi ogni decisione database: storage engine, modello di esecuzione, modellazione, indici."""),
]

architettura = [
rec("ARC-001","architettura_hw","cpu_programmatori","L'ARCHITETTURA CPU PER CHI PROGRAMMA: PIPELINE E PREDIZIONE",
"""Il processore non esegue le istruzioni una alla volta come il codice sorgente suggerisce: conoscere la CPU cambia il modo di scrivere codice.

LA PIPELINE: la CPU scompone l'esecuzione in stadi (fetch, decode, execute, memory, writeback) e li sovrappone come una catena di montaggio: mentre un'istruzione esegue, la successiva decodifica, la terza fetcha: il throughput e' di piu' istruzioni per ciclo.\n- I BRANCH (if/else) rompono la catena: la CPU non sa quale strada prendere: PREDICE (branch predictor: si ricorda dei pattern passati) e prosegue SPECULATIVAMENTE; se la previsione e' sbagliata, si SVUOTA la pipeline (branch misprediction: 10-20 cicli persi). Codice con branching imprevedibile (dipendente dai dati) e' piu' lento di quanto sembri.\n- IL COSTO DELLE ECCEZIONI/ERRORI: nei linguaggi con eccezioni a costo zero finche' non lanciano (C++, Rust): proprio perche' il lancio rompe tutte le previsioni.\n\n"
"L'IPC (ISTRUZIONI PER CICLO): il parametro di salute: un loop che va a 0.5 IPC sta sprecando meta' del processore: cause: dipendenze tra istruzioni, branch miss, cache miss (corpus ARC-002).\n\n"
"ISTRUZIONI COSTOSE DA CONOSCERE:\n- divisione e floating point lenti rispetto a interi/shift;\n- la moltiplicazione per potenze di 2 e' uno shift (i compilatori lo fanno);\n- i bound-check degli array eliminabili quando il compilatore puo' dimostrare la sicurezza.\n\n"
"LEZIONE PRATICA: il profilo (corpus performance systems) dice DOVE; questa scheda dice PERCHE': 'il loop e' lento perche' imprevedibile nel branching o perche' salta in giro per la memoria' — domande diverse, cure diverse."""),

rec("ARC-002","architettura_hw","memoria_cache","MEMORIA E LOCALITA': IL VERO COLLO DI BOTTIGLIA",
"""La RAM e' 100 volte piu' lenta della CPU: le cache (L1/L2/L3) coprono il divario — ma solo per chi le usa.

LA GERARCHIA: registri < L1 (KB, 1 ciclo) < L2 < L3 < RAM (~200 cicli) < disco (milioni di cicli). Ogni livello e' 10-100x piu' capace e 10-100x piu' lento. La cache carica LINEE di 64 byte: leggere 1 byte porta 63 vicini gratis.\n\n"
"IL PRINCIPIO DELLA LOCALITA':\n- SPAZIALE: si accede a cose vicine in memoria (array sequenziali, struct compatte);\n- TEMPORALE: si riusa cio' che si e' appena usato (variabili calde).\nIl codice veloce massimizza entrambi.\n\n"
"L'ARRAY DI STRUCT vs STRUCT DI ARRAY (il caso didattico):\n- Array di struct: [{x,y,z},{x,y,z}...] — accedere a tutte le x richiede di saltare (stride 12 byte): ogni accesso e' un cache miss;\n- Struct di array: {xs[], ys[], zs[]} — le x sono contigue: la cache lavora. E' ESATTAMENTE il columnar storage dei database (corpus QRE-004) e l'ECS dei game engine (corpus GME-001): stesso principio fisico.\n\n"
"FALSE SHARING: due thread che scrivono variabili diverse MA nella stessa linea di cache si invalidano a vicenda la cache (la linea e' la grana di coerenza): il parallelismo che rallenta: si separano le variabili per-thread su linee diverse.\n\n"
"NUMA: su server multi-socket, la RAM e' 'piu' vicina' a un processore: un thread che accede alla RAM dell'altro nodo paga il doppio: i database seri (e i loro tuning) tengono conto dell'affinita'.\n\n"
"REGOLA D'ORO: 'i dati che si usano insieme vanno vicini': prima domanda di chi ottimizza la memoria."""),

rec("ARC-003","architettura_hw","gpu_simt","GPU E COMPUTAZIONE PARALLELA DI MASSA: IL MODELLO SIMT",
"""La GPU e' un'altra macchina: non piu' veloce per il codice seriale, ma capace di migliaia di calcoli in parallelo — e ora centrali per AI e grafica.

IL MODELLO SIMT (Single Instruction, Multiple Threads): migliaia di 'thread' eseguono la STESSA istruzione su dati diversi: pensare a un'istruzione che opera su un vettore di 1024 elementi contemporaneamente. Le unita' si chiamano shader core/CUDA core/NPU a seconda del vendor.\n\n"
"COME PROGRAMMARLA:\n- I KERNEL: si scrive la funzione che gira 'per ogni elemento' ('ogni thread somma il suo elemento');\n- LA MEMORIA: gerarchia esplicita (registri per thread, shared memory per blocco, global per tutti): chi controlla la memoria controlla la velocita';\n- LE DIVERGENZE: i branch dentro un kernel dove i thread dello stesso gruppo prendono strade diverse SERIALIZZANO: il parallelismo premia la regolarita'.\n\n"
"CUDA (NVIDIA) E LE ALTERNATIVE: CUDA e' l'ecosistema dominante; le alternative aperte: ROCm (AMD), SYCL/oneAPI, OpenCL; le astrazioni: PyTorch/TensorFlow (il GPU viene dietro alle tensor operations), Triton (kernel pythonici), WebGPU/WGSL (grafica e compute nel browser).\n\n"
"LE APU E L'AI LOCALE: il confine GPU/CPU si sfuma (le APU integrano entrambe) e le NPU (neural processing unit) accelerano l'inferenza AI a basso consumo: l'AI on-device dei laptop moderni. Per i workload AI: la GPU regge il training e l'inferenza seria; la NPU l'inferenza leggera continua.\n\n"
"CASI D'USO EDILI: render fotorealistici (corpus graphics), simulazioni termiche/strutturali, elaborazione point cloud, training dei modelli di visione per il cantiere."""),

rec("ARC-004","architettura_hw","acceleratori_sistemi","ACCELERATORI E SISTEMI SPECIALIZZATI: TPU, FPGA E QUANTO BASTA",
"""Oltre CPU e GPU: l'hardware specializzato dove le prestazioni contano davvero — e la competenza per riconoscerne il momento.

TPU E ACCELERATORI AI: unita' progettate per una sola operazione (moltiplicazione di matrici — il cuore delle reti neurali): Google TPU, AWS Trainium/Inferentia, le NPU dei laptop: il training AI a scala e' economico solo su acceleratori: il costo del calcolo AI si e' crollato proprio grazie a loro.\n\n"
"FPGA (FIELD-PROGRAMMABLE GATE ARRAY): hardware riconfigurabile via software: si 'compila' il circuito: latenza estrema, parallelismo su misura, consumi bassissimi: usate in trading ad alta frequenza, telecom, automazione industriale, edge AI. Il costo: sviluppo lungo e competenze rare (HDL come VHDL/Verilog).\n\n"
"ASIC E SISTEMI EMBEDDED DI CALCOLO: chip su misura (il chip dell'auto, del telefono, del sensore): la flessibilita' zero in cambio di costo/performance/watt ottimali. L'Internet delle Cose vive qui: il microcontrollore a 2 euro che campiona un sensore ogni ora non ha bisogno di una CPU generale.\n\n"
"LE DECISIONI PRATICHE (quando l'hardware specializzato si paga):\n- throughput AI > qualche query/secondo -> GPU/acceleratori;\n- latenza o consumo estremi su task fisso -> FPGA/ASIC;\n- tutto il resto -> CPU: ricordando che la CPU moderna con SIMD (AVX-512) fa molto piu' di quanto si pensi, e che l'80% dei problemi si risolve con codice migliore, non hardware migliore.\n\n"
"L'ANALOGIA EDILE: CPU = squadra edile versatile; GPU = getto continuo su cassaforme (volume enorme di operazioni identiche); FPGA = cassaforma su misura per quel pilastro; ASIC = la linea di produzione del prefabbricato. La scelta giusta dipende dalla ripetizione e dal volume — mai dal prestigio."""),
]

build = [
rec("BLD-001","build_systems","build_fondamenti","BUILD SYSTEM: COSA FANNO DAVVERO E PERCHE'",
"""Il build system e' il primo tool di ogni progetto: compila, testa, impacchetta. La sua storia spiega i problemi che risolve.

LE FASI DI UN BUILD:
1. DIPENDENZE: quali pezzi servono (librerie, artefatti interni);\n2. COMPILAZIONE: sorgente -> artefatti;\n3. TEST: l'esecuzione dei test e' parte del build (CI/CD: il build e' il gate);\n4. PACKAGING: il distributivo (jar, wheel, docker image, apk);\n5. PUBBLICAZIONE: nel registry interno/esterno.\n\n"
"IL PRINCIPIO FONDAMENTALE: INCREMENTALITA' E CORRETTEZZA:\n- si ricompila SOLO cio' che e' cambiato (dependency graph: si parte dal grafo delle dipendenze tra moduli);\n- la correttezza: se cambia un header/dipendenza transitiva, TUTTO cio' che dipende si ricostruisce (i build seri tracciano i content hash, non solo i timestamp);\n- L'EREDITA': Make (1976): regole file->file con timestamp: sufficiente per i progetti C piccoli, fragile sui grandi (i timestamp mentono su checkout freschi); i successori moderni: Bazel/Buck/Pants (hermetic: ambiente controllato, cache remote — sui monorepo grandi), Gradle/Maven (Java), Cargo (Rust — il migliore della categoria: veloce, corretto, ergonomico), CMake + Ninja (C/C++).\n\n"
"ERMITICITA' E REPRODUCIBILITY: i build moderni mirano a: stesso input -> stesso output, sempre, ovunque (ambienti isolati, versioni pinnate, niente 'funziona solo sulla mia macchina'): la base della supply chain security (SBOM del corpus sicurezza).\n\n"
"REGOLA PRATICA: il tempo di build e' il tempo del team: oltre i 10 minuti si investe nella velocita' (parallelismo, caching, modularizzazione). Il build lento non e' un fastidio: e' una tassa su ogni decisione."""),

rec("BLD-002","build_systems","package_managers","PACKAGE MANAGER E RISOLUZIONE DELLE DIPENDENZE: IL SAT SOLVER SOTTO npm",
"""Dietro ogni 'npm install' o 'pip install' c'e' un problema NP-completo risoltto in millisecondi.

IL PROBLEMA: dare a ogni pacchetto le versioni che richiede ('A vuole X>=2, B vuole X<3') trovando una combinazione coerente — con centinaia di pacchetti. E' un problema di soddisfacimento di vincoli (SAT/CP-SAT: i solver del corpus formale).\n\n"
"LE STRATEGIE:\n- NESTED (npm classico): ogni pacchetto porta le proprie versioni nidificate: semplicita', duplicazione (la famosa cartella node_modules da 400MB);\n- FLAT (pip classico): una sola versione per pacchetto nel virtualenv: conflitti esposti subito;\n- LOCKFILE: la soluzione trovata viene CONGELATA (package-lock.json, poetry.lock, Cargo.lock): reinstallazioni identiche per sempre: la riproducibilita' in pratica (corpus supply chain).\n\n"
"I PROBLEMI NOTI:\n- dependency hell: vincoli in conflitto irrisolvibili: si risolve aggiornando o allentando vincoli;\n- version pinning: pinnare TUTTO (lockfile) vs range semantici: la pratica matura: range in development, lockfile in produzione;\n- dependency confusion: un pacchetto interno senza namespace pubblico puo' essere 'ombreggiato' da uno pubblico con lo stesso nome: si usano scope/namespace privati;\n- i peer dependencies (librerie che vanno fornite dall'applicazione: i plugin di React).\n\n"
"SEMVER NELLA PRATICA: MAJOR.MINOR.PATCH: i major bump rompono i contratti: il problema culturale: troppi pacchetti rompono il MINOR invece del MAJOR (il dibattito Hyrum: 'con abbastanza utenti, OGNI cambiamento e' un breaking change': anche correggere un bug rompe chi ci si appoggiava).\n\n"
"REGOLA: il package manager e' il gestionale delle dipendenze: si rispetta (lockfile committato, audit regolari, upgrade piccoli e continui)."""),

rec("BLD-003","build_systems","monorepo_dx","MONOREPO E DEVELOPER EXPERIENCE: SCALARE I TEAM, NON SOLO IL CODICE",
"""Quando il codice cresce, il problema diventa organizzativo: il monorepo e la developer experience sono le risposte moderne.

MONOREPO vs POLIREPO:
- POLIREPO: un repository per servizio/pacchetto: indipendenza, ma coordinamento difficile (cambiamenti che attraversano piu' repo: PR multiple, versioni da allineare, CI disallineate);\n- MONOREPO: tutto in un repository: un commit atomico cambia client e server insieme: refactoring su scala (rinominare un tipo usato ovunque in un colpo solo), CI unificata. Costi: il tooling deve reggere la scala (i build system Bazel/Pants nascono per questo: affected detection — si testa solo cio' che il cambiamento tocca).\n- LE VARIANTI: monorepo con publishing (ogni pacchetto esce versionato) vs trunk-based: la direzione moderna dei grandi player (Google, Meta).\n\n"
"LA DEVELOPER EXPERIENCE (DX): il 'cantiere' dello sviluppatore: ogni attrito si moltiplica:\n- setup in un comando ('git clone && make setup' deve bastare: il documento di setup che funziona verificato in CI);\n- feedback loop veloce (build locale < 1 minuto per il ciclo edit-test);\n- i tool che decidono al posto dello sviluppatore (formatter, linter, codegen);\n- la documentazione nel repo (README per modulo, ADR per le decisioni).\n\n"
"L'AFFECTED DETECTION E LA CI SUL MONOREPO: il grafo delle dipendenze permette: 'questo PR tocca 3 pacchetti -> si testano quelli e i dipendenti': la CI resta veloce a qualunque scala.\n\n"
"LEZIONE GENERALE: la velocita' del team e' il prodotto delle sue macro-piu' lente (build, CI, deploy): investire nella DX e' investimento nella throughput del team, non in comodita'."""),

rec("BLD-004","build_systems","release_engineering","RELEASE ENGINEERING: VERSIONARE, FIRMARE, DISTRIBUIRE",
"""Dopo il build: la disciplina della release — versionamento, changelog, artefatti firmati, rollout.

IL VERSIONAMENTO SEMANTICO APPLICATO:
- MAJOR: rotture di contratto (si comunica con anticipo e path di migrazione);\n- MINOR: funzionalita' additive retrocompatibili;\n- PATCH: correzioni.\n- Il CHANGELOG mantenuto a mano (Keep a Changelog): gli utenti leggono quello, non i commit.\n\n"
"LA CATENA DI FORNITURA DELLA RELEASE (sicurezza applicata):\n1. BUILD ERMETICO: ambiente pulito, dipendenze pinnate;\n2. FIRMA: l'artefatto viene firmato (GPG, cosign per le immagini container): chi installa VERIFICA la provenienza;\n3. SBOM: la lista delle componenti (corpus supply chain);\n4. PROVENANCE (SLSA): le attestazioni di come e' stato costruito (da cosa, da chi, in quale ambiente);\n5. DISTRIBUZIONE: registry con controlli di accesso, immutabilita' (le versioni pubblicate non si sovrascrivono MAI — una versione rilasciata e' permanente).\n\n"
"LE STRATEGIE DI ROLLOUT (dal corpus CI/CD): canary, blue/green, feature flag: la release e' un processo controllato, non un evento.\n\n"
"RELEASE TRAIN VS CONTINUOUS:\n- RELEASE TRAIN: rilasci a calendario (ogni 2 settimane): prevedibilita' per chi integra;\n- CONTINUOUS DELIVERY: ogni commit e' rilasciabile (la decisione separata dal lavoro): il default moderno dei SaaS;\n- I LONG-TERM SUPPORT (LTS): i rami di manutenzione pluriennali per chi non puo' aggiornare spesso.\n\n"
"LA REGOLA FINALE: la release e' un contratto con gli utenti: versioni oneste, changelog curati, artefatti verificabili — la fiducia si costruisce release dopo release, come i SAL di un cantiere."""),
]

knowledge_graph = [
rec("KNG-001","knowledge_graph","modellare_conoscenza","GRAFI DI CONOSCENZA: MODELLARE IL MONDO COME RELAZIONI",
"""Il grafo di conoscenza rappresenta entita' e relazioni esplicitamente: la struttura dati piu' naturale per conoscenza complessa — ed e' il complemento ideale dei documenti per un LLM.

L'IDEA: invece di testo libero ('il preventivo 12 riguarda il cantiere di via Roma del cliente Rossi'), FATTI strutturati: (Preventivo:12) -[riguarda]-> (Cantiere:ViaRoma); (Cantiere:ViaRoma) -[di]-> (Cliente:Rossi). La conoscenza diventa NAVIGABILE: 'tutti i preventivi del cliente Rossi', 'tutti i cantieri con cappotto termico', 'quali fornitori lavorano su cantieri con lo stesso tipo di impianto'.\n\n"
"VANTAGGI RISPETTO AI DOCUMENTI:\n- PRECISIONE: i fatti sono esatti, non interpretabili;\n- NAVIGAZIONE: il grafo si attraversa (chiave: le query a piu' salti — 'i subappaltatori dei cantieri del cliente X');\n- INFERENZA: regole semplici ('se A e' parte di B e B e' parte di C -> A e' parte di C') derivano fatti nuovi.\n\n"
"IL MODELLO DATI: NODI (entita': tipate — Cantiere, Cliente, VoceComputo), RELAZIONI (tipate e dirette: 'riguarda', 'comprende', 'fornisce'), PROPRIETA' (attributi scalari: data, importo, stato).\n\n"
"CASO EDILE MODELLAto: Cliente <-[ordina]- Preventivo -[comprende]-> Voce -[utilizza]-> Materiale -[fornito_da]-> Fornitore; Cantiere -[ha_fase]-> Fase -[richiede]-> Certificazione. Il grafo diventa il 'cervello' operativo: dall'ordine alla filiera.\n\n"
"STRUMENTI: Neo4j (il principale, Cypher), Memgraph, Amazon Neptune, oppure PostgreSQL con Apache AGE per iniziare.\n\n"
"QUANDO USARLO: relazioni complesse da interrogare in molti modi, conoscenza di dominio strutturata, integrazione con l'AI (la prossima scheda)."""),

rec("KNG-002","knowledge_graph","rdf_owl_ontologie","RDF, OWL E ONTOLOGIE: LA VERSIONE FORMALE DELLA CONOSCENZA",
"""Il web semantico ha prodotto gli strumenti formali per la conoscenza: RDF, OWL, SPARQL — tecnologia matura dietro la ricerca biomedica e i cataloghi culturali.

RDF (RESOURCE DESCRIPTION FRAMEWORK): il modello a tripla: SOGGETTO - PREDICATO - OGGETTO, con tutto identificato da URI ('urn:preventivo:12', 'urn:riguarda', 'urn:cantiere:viaroma'). Grafo globale, distribuito, fondamentale: chiunque puo' dichiarare fatti su qualunque cosa. Serializzazioni: Turtle (leggibile), JSON-LD (il web).\n\n"
"ONTOLOGIE (OWL): si definiscono le CLASSI e le loro proprieta' formali:\n- 'Cantiere e' una sottoclasse di Progetto' (ereditarieta' delle proprieta');\n- 'ogni VoceComputo appartiene a esattamente un Preventivo' (vincoli di cardinalita');\n- 'il fornitore di X non puo' essere il cliente di X' (vincoli di disgiunzione).\nCon l'ontologia si fa INFERENZA: dal fatto che 'ViaRoma e' un Cantiere' e 'Cantiere e' Progetto', il sistema deduce che ViaRoma e' un Progetto — ragionamento automatico sui dati.\n\n"
"SPARQL: il linguaggio di query RDF (il 'SQL del grafo'): pattern matching su triple: 'tutti i cantieri il cui cliente ha sede in Lombardia'.\n\n"
"PERCHE' E' IMPORTANTE PER L'AI: un LLM con un'ontologia del dominio edile risponde entro una struttura formale condivisa: i termini hanno DEFINIZIONI formali (uri) — si riducono ambiguita' e allucinazioni sui concetti. I grandi grafi di conoscenza pubblici (Wikidata!) funzionano cosi'.\n\n"
"IL CASO PRATICO: si parte SEMPLICE (proprieta' grafo: nodi e relazioni), si aggiunge formalita' SOLO dove serve (i vincoli di dominio che contano): l'ontologia totale e' un progetto infinito — la regola e' la stessa dei metodi formali (corpus FRM): dosare."""),

rec("KNG-003","knowledge_graph","graph_queries","QUERY SU GRAFI: CYPHER, PATTERN MATCHING E PERCORSI",
"""Le query su grafi ragionano sui PATTERN di relazioni: la competenza chiave per usarli.

CYPHER (il linguaggio di Neo4j, il piu' diffuso): si DISEGNA il pattern cercato:\n- MATCH (c:Cantiere)-[:HA_FASE]->(f:Fase {stato:'in_corso'}) RETURN c, f;\n- trovare i PERCORSI: MATCH path = (a:Cliente)-[*1..4]->(b:Fornitore): tutti i percorsi di 1-4 salti tra cliente e fornitore: 'come siamo collegati?'.\n\n"
"LE OPERAZIONI CARATTERISTICHE:\n1. PATTERN MATCHING: 'trovami tutte le configurazioni dove X collega a Y con certi vincoli' — la query base;\n2. PERCORSI E RAGGIUNGIBILITA': shortest path, tutti i percorsi (con limite: esplosione combinatoria), all-pairs shortest (algoritmi grafi del corpus ALG applicati);\n3. VARIABILITA' DELLO SCHEMA: i grafi sono 'schema-flexible': si aggiungono relazioni nuove senza migrazioni — vantaggio e rischio (la disciplina arriva dai tipi di nodo/relazione);\n4. AGGREGAZIONI GRAFICHE: pagerank, community detection (algoritmi sui grafi: quali fornitori formano un cluster?), centralita'.\n\n"
"LE TRAPPOLE:\n- il modello sbagliato: le relazioni a doppio senso (si modella una volta, le query seguono la direzione o si usa la freccia senza direzione);\n- la property explosion: attributi che dovevano essere nodi ('il materiale' come stringa invece che nodo: perdi le query sui materiali);\n- le query senza bound sui percorsi: esplodono sempre: si limita la profondita' e si filtra.\n\n"
"IL GRADO ZERO: importare i dati esistenti (clienti, cantieri, voci) come nodi e le FK del database come relazioni: la prima versione del grafo aziendale in un pomeriggio — il valore si vede alle prime query a 3 salti."""),

rec("KNG-004","knowledge_graph","kg_llm","GRAFO DI CONOSCENZA + LLM: GRAPH RAG E CONTESTO STRUTTURATO",
"""L'integrazione grafo + LLM (Graph RAG): il livello piu' avanzato dei sistemi RAG — e il piu' promettente per domini complessi come l'edilizia.

I LIMITI DEL RAG VETTORIALE (corpus IRS): recupera CHUNKS di testo simili, ma:\n- non ragiona sulle RELAZIONI ('i cantieri dello stesso cliente con lo stesso difetto di posa');\n- non e' preciso sui FATTI ('l'importo del preventivo 12': il testo puo' dirlo male o non dirlo);\n- perde il CONTESTO GLOBALE (come le entita' si collegano).\n\n"
"GRAPH RAG: LA PIPELINE:\n1. LA DOMANDA si analizza: quali ENTITA' cita? ('quanto ha speso Rossi per i bagni?');\n2. SI INTERROGA IL GRAFO: i fatti precisi (spese, importi, date, stati) via Cypher;\n3. SI INTERROGA IL VETTORIALE: il contesto testuale (normativa, capitolati, note);\n4. L'LLM COMBINA: 'Rossi ha speso 12.400 euro su 3 bagni (grafo); i capitolati richiedono la guaina sotto la doccia (vettoriale); il cantiere di Via Verdi presenta lo stesso schema (grafo)'.\n\n"
"LE TECNICHE SPECIFICHE:\n- TEXT-TO-CYPHER: l'LLM traduce la domanda in query (con validazione!): 'mostrami i cantieri in ritardo' -> Cypher sui dati reali: la risposta e' ESATTA, non generata;\n- ENTITY LINKING: collegare le menzioni nel testo ai nodi del grafo (la pipeline di indicizzazione che costruisce entrambi);\n- HYBRID RETRIEVAL: vettoriale + grafo + keyword (corpus IRS-003): la pratica consolidata.\n\n"
"PER AURATRIX: un assistente che conosce l'azienda non da documenti soli ma da un grafo operativo (clienti, cantieri, voci, materiali, fornitori) puo' rispondere con PRECISIONE contabile alle domande del titolare ('a quanto ammontano i lavori in corso con acconti superiori al 40%?') — il tipo di domanda dove l'allucinazione non e' tollerabile.\n\n"
"LA REGOLA FINALE: i grafi danno i fatti, i vettori danno il contesto, l'LLM fa da collante: tre strumenti, un sistema."""),
]

corpora = [
    ("information_retrieval.jsonl", ir),
    ("query_engines.jsonl", query_engines),
    ("architettura_calcolatori.jsonl", architettura),
    ("build_systems_tooling.jsonl", build),
    ("knowledge_graphs.jsonl", knowledge_graph),
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
