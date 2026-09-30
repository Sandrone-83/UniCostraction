# -*- coding: utf-8 -*-
"""Coding_Master_Pack_4: quattro nicchie finali — 20 schede."""
import json, os

BASE = r"C:\Users\alessandro\Documents\kimi\tasks\2026-09-26\15-14-07-e3d653af\Coding_Master_Pack_4\parsed"
os.makedirs(BASE, exist_ok=True)

LIC = "Sintesi didattica originale Kimi (pubblico dominio)"
ATT = "Corpus coding master 4 a cura di Kimi"

def rec(id_, cat, tema, title, text):
    return {"id": id_, "categoria": cat, "tema": tema, "title": title, "text": text,
            "source": f"coding_master_4_{cat}_kimi", "license": LIC, "commercial_ok": True,
            "attribution": ATT, "url": ""}

consensus = [
rec("CST-001","consensus","raft","CONSENSO DISTRIBUITO E RAFT: METTERSI D'ACCORDO TRA MACCHINE",
"""Il problema del consenso: piu' server che devono concordare un unico ordine di operazioni, con guasti e rete instabile. E' il cuore di etcd, Consul, TiKV, CockroachDB.

IL CONSENSO: i server eleggono un LEADER che propone l'ordine delle operazioni; gli altri (followers) votano. Se il leader muore, nuova elezione. Le garanzie: safety (mai due leader con lo stesso mandato) e liveness (se la maggioranza e' viva, si elegge).

RAFT (comprensibile):
1. TERMINI: ogni elezione incrementa il termine (contatore logico di epoca).
2. ELEZIONE: timeout casuali di attesa; chi scade primo vota per se' e chiede i voti: chi vota controlla che il candidato abbia dati almeno aggiornati.
3. REPLICAZIONE: il leader accetta le scritture, le appende al log, le replica; il commit avviene quando la MAGGIORANZA le ha scritte — da quel momento la scrittura e' garantita anche in caso di guasti (su qualsiasi maggioranza futura).
4. REGOLE DI SICUREZZA: si vota solo per chi e' almeno aggiornati; un leader non puo' sovrascrivere voci committate.

PAXOS: il predecessore teorico piu' generale (e meno leggibile); Raft e' stato disegnato per essere comprensibile — nella pratica i sistemi moderni usano Raft o sue varianti.

COSA COMPRA IL CONSENSO: strongly consistent metadata (chi e' il leader, configurazioni, lock distribuiti, schema del database). Quando serve davvero: sistemi distribuiti con scritture su piu' nodi; mai la scelta di default — prima replica semplice o leader single.

CONNESSIONE CON I CORPUS: e' la risposta tecnica alla domanda del corpus affidabilita' ('che succede se due nodi decidono insieme?')."""),

rec("CST-002","consensus","storage_engines","STORAGE ENGINES: COME IL DATABASE SCRIVE SU DISCO",
"""Sotto ogni database relazionale c'e' una struttura dati su disco: B-Tree o LSM-Tree. Capire le due filosofie spiega la meta' dei comportamenti dei DB.

B-TREE (PostgreSQL, MySQL InnoDB, SQLite):
- ALBERO BILANCIATO SU DISCO: i nodi sono pagine da 4-16KB; la ricerca e' O(log n) con 3-4 letture anche su miliardi di righe.\n- LE LETTURE VELOCI: il dato e' ordinato, range query e ordinamenti naturali;\n- LE SCRITTURE COSTOSE: ogni insert/update tocca le pagine giuste e mantiene l'ordine (split dei nodi quando pieni);\n- INDICE CLUSTERED: l'indice primario E' la tabella (InnoDB) o separato (Postgres) — influenza costi di query e storage.\n\n"
"LSM-TREE (RocksDB, Cassandra, Scylla, LevelDB):\n- WRITE-OPTIMIZED: le scritture vanno in memoria (memtable) e su un log append-only: scrivere e' SEMPRE sequenziale e veloce;\n- COMPACTION: di tanto in tanto i file ordinati su disco (SSTable) vengono fusi e compattati — il lavoro di manutenzione che si paga in lettura/write amplification;\n- LETTURE CHE COSTANO: piu' livelli da controllare + bloom filters per saltare i file che non contengono la chiave.\n\n"
"LE CONSEGUENZE PRATICHE:\n- scrittura massiva (time-series, eventi, logging): LSM;\n- letture complesse, transazioni, SQL: B-Tree;\n- 'perche' l'update di una riga e' lento?': B-Tree, chiave grande = piu' pagine;\n- 'perche' il database si ingrossa dopo cancellazioni?': LSM, le compaction sono asincrone.\n\n"
"REGOLA: la scelta del database e' anche la scelta del suo storage engine — le performance si capiscono dal di sotto."""),

rec("CST-003","consensus","event_sourcing_crdt","EVENT SOURCING E CRDT: DUE STRADE ALLA CONSISTENZA",
"""Quando la coerenza immediata tra nodi e' impossibile (rete partizionata), esistono due architetture mature.

EVENT SOURCING:
- LO STATO DERIVA DAGLI EVENTI: invece di salvare 'saldo = 100', si salvano i fatti: 'versato 50', 'prelevato 30', 'versato 80'. Lo stato attuale si RICALCOLA riproducendo gli eventi (o mantenendo una proiezione aggiornata).
- VANTAGGI: audit trail completo gratis (chi ha fatto cosa e quando — oro in ambiti regolati come l'edilizia documentale), time travel (lo stato a una data qualsiasi), riproducibilita' dei bug.
- COSTI: lo schema evolutivo degli eventi (un evento vecchio deve restare leggibile: upcasting, versioning), la gestione delle proiezioni, la complessita' mentale.
- USO TIPO: ledger finanziari, audit, sistemi con requisiti di tracciabilita' — 'ogni modifica al preventivo e' un evento con autore e timestamp' e' event sourcing applicato al dominio edile.

CRDT (Conflict-free Replicated Data Types):
- STRUTTURE CHE SI FONDONO DA SOLE: contatori, set, map, testi collaborativi che possono essere modificati su piu' nodi in contemporanea e fusi senza conflitti (matematicamente garantito).
- LA REGOLA DI MERGE: ogni aggiornamento e' un operazione che commuta/associa: 'unione di set' non ha conflitti — 'ultimo scrive vince' si', ma e' una CRDT banale (LWW).
- USO TIPO: editing collaborativo (Google Docs, Figma), app offline-first, sistemi edge dove la rete non e' garantita — un tablet da cantiere offline che sincronizza al rientro in ufficio.
- COSTO: certi domini non si esprimono come CRDT: quando servono invarianti globali (stock unico), il compromesso cambia (sistemi con reconciliazione esplicita).

QUANDO USARE COSA: audit e riproducibilita' -> event sourcing; collaborazione offline e fusione automatica -> CRDT; semplicita' -> database classico."""),

rec("CST-004","consensus","distributed_transactions","TRANSAZIONI DISTRIBUITE: 2PC, SAGA E OUTBOX",
"""Quando una transazione attraversa piu' servizi, il CAP vieta la perfezione: restano compromessi consci.

2PC (TWO-PHASE COMMIT): il coordinatore chiede a tutti i partecipanti 'puoi committare?' (prepare); se tutti dicono si', ordina il commit a tutti. E' corretto ma fragile: il coordinatore e' single point of failure; i lock restano tenuti durante la fase di attesa (blocco del sistema); in presenza di partizioni qualcuno resta bloccato. Da evitare su architetture a servizi; ancora usato dentro i database stessi.

SAGA (gia' introdotto nel corpus affidabilita'): sequenza di transazioni locali con COMPENSAZIONI: 'se il passo 3 fallisce, esegui le inverse dei passi 1-2'. La regolarizzazione:
- orchestrazione: un orchestratore decide i passi (esplicito, debuggabile);\n- coreografia: ogni servizio reagisce agli eventi degli altri (disaccoppiato ma difficile da seguire);\n- ogni passo e' IDEMPOTENTE (i retry sono garantiti in un sistema distribuito).\n\n"
"OUTBOX PATTERN: il problema 'salva nel database E pubblica evento' non e' atomico tra DB e message broker. Soluzione: nella stessa transazione del dato si salva anche la riga 'outbox'; un processo legge l'outbox e pubblica (con retry): esattly-once effetto garantito dall'idempotenza dei consumer.\n\n"
"IL RUOLO DEI TEOREMI: CAP vieta coerenza+disponibilita' durante le partizioni; PACELC aggiunge che anche SENZA partizioni c'e' un trade-off latenza/coerenza (la replica sincrona costa). Le scelte concrete: read-your-writes via primario, coerenza eventuale accettata sui report, compensazioni sui flussi business.\n\n"
"REGOLA DECISIVA: prima si riduce lo stato condiviso (un servizio = un database), poi si scelgono i compromessi dove il business li accetta — mai globalmente."""),

rec("CST-005","consensus","tempo_ordine","TEMPO, ORDINE E OROLOGI IN SISTEMI DISTRIBUITI",
"""In un sistema distribuito non esiste 'ora' e non esiste 'ordine globale': due idee sottovalutate che spiegano meta' dei bug.

PERCHE' L'OROLOGIO DI SISTEMA NON BASTA:
- NTP tiene gli orologi vicini (millisecondi) ma non esatti: due eventi possono avere timestamp invertiti rispetto all'ordine reale;\n- gli orologi di sistema possono tornare INDIETRO (correzioni NTP, leap second): mai usarli per ordinare o per id univoci;\n- su macchine diverse, 'prima' e 'dopo' non sono confrontabili senza comunicazione.\n\n"
"L'ORDINE LOGICO: quello che conta e' l'ordine CAUSALE (A ha causato B? allora A prima di B).\n- CLOCK LOGICI (Lamport): ogni nodo incrementa un contatore; ogni messaggio porta il contatore; alla ricezione si aggiorna al massimo. Dato un timestamp di Lamport, chi e' minore e' 'prima' (ma non il viceversa: minore non implica causale).\n- VECTOR CLOCKS: un vettore di contatori (uno per nodo) cattura la causalita' completa: si puo' rispondere 'concorrenti' oltre a 'prima/dopo' — alla base dei sistemi con CRDT e dei database tipo Dynamo.\n\n"
"CASI D'USO REALI:\n- id univoci distribuiti: non timestamp ma ID generati localmente con unicità statistica (UUID v4, ULID, Snowflake — timestamp + nodo + sequenza);\n- ordinamento dei log distribuiti: si aggiunge il vector clock o si accetta l'ordinamento parziale;\n- deduplica di eventi: l'identita' dell'evento (id deterministico) invece del timestamp;\n- versioning ottimistico: ogni riga ha un numero di versione: chi scrive controlla che la versione sia ancora quella letta — il conflitto si rileva, non si suppone.\n\n"
"LEZIONE PRATICA: ogni volta che il codice dice 'ordina per timestamp', chiedersi: 'chi ha scritto questi timestamp? da quante macchine?'. Se la risposta e' piu' di una, servono id logici o vettori."""),
]

game = [
rec("GME-001","game_dev","game_loop_ecs","GAME LOOP, ECS E ARCHITETTURA DI UN ENGINE",
"""Il videogioco e' il software piu' esigente esistente: 60 frame al secondo, milioni di oggetti, zero tolleranza — e le sue architetture insegnano disciplina al software comune.

IL GAME LOOP: il cuore: while(vivo): input -> update(logica) -> render(disegna) -> attendi il prossimo frame. Il delta time (tempo tra i frame) rende il movimento indipendente dal framerate (su 120Hz e 30Hz la velocita' percepita deve essere identica). Il fixed timestep per la fisica: aggiornamenti a intervalli costanti per stabilita' numerica.

L'ARCHITETTURA ECS (Entity-Component-System):
- ENTITY: un id puro (l'entita' 'e' solo un numero);\n- COMPONENT: dati puri (posizione, velocita', sprite) senza logica;\n- SYSTEM: la logica che elabora TUTTI i componenti di un tipo insieme ('muovi tutte le velocita').\n- IL GUADAGNO: i dati di un tipo vivono CONTIGUI in memoria: il processore li legge in cache come una pila — migliaia di entita' processate in microsecondi. E' la stessa logica del columnar storage dei database analitici.\n\n"
"ALTRE COMPONENTI DELL'ENGINE:\n- SCENE GRAPH: la gerarchia di nodi (corpus graphics);\n- RESOURCE MANAGER: caricamento asincrono degli asset, streaming dei mondi aperti;\n- EVENT SYSTEM: comunicazione disaccoppiata tra sistemi (il pattern observer a regime);\n- SCRIPTING: la logica di gameplay in linguaggio interpretato (Lua, C#) per iterare veloci senza ricompilare l'engine.\n\n"
"LEZIONI TRASFERIBILI: i pattern performance-first (data-oriented design), il delta time come concetto di determinismo temporale, l'event-driven disaccoppiato — tutto nato dove i vincoli erano impossibili."""),

rec("GME-002","game_dev","fisica","FISICA PER GIOCHI E SIMULAZIONE: INTEGRATORI E COLLISIONI",
"""La fisica dei giochi e' una fisica utile, non esatta: si integra il moto a passi discreti e si trovano le collisioni con strutture spaziali.

L'INTEGRAZIONE DEL MOTO:
- EQUAZIONE: posizione += velocita' * dt; velocita' += accelerazione * dt. Semplice, ma l'errore si accumula;\n- EULER ESPLICITO: il metodo sopra — veloce ma instabile con passi grandi;\n- SEMI-IMPLICITO (SYMPLECTIC) EULER: aggiornare prima la velocita' poi la posizione: stabile ed e' quello usato nella maggior parte dei giochi;\n- VERLET/RUNGE-KUTTA: piu' precisi per simulazioni (tessuti, ragdoll) — scelti dove la stabilita' conta piu' del costo.\n\n"
"LE COLLISIONI:\n- FASE LAMPLIGHT (BROAD PHASE): quali coppie POSSONO collidere? Con migliaia di oggetti non si confronta tutto con tutto: strutture spaziali (AABB tree, quadtree/octree, spatial hash) riducono i candidati da O(n^2) a O(n log n);\n- FASE NARROW: sui candidati, il test preciso (cerchio-cerchio, OBB sat, mesh-mesh semplificata);\n- RISPOSTA: separare i corpi, calcolare l'impulso, gestire attrito e rimbalzo.\n\n"
"IL MOTORE FISICO: Box2D (2D), Bullet/Havok/PhysX (3D): integratori stabili, constraint solver, sleeping (i corpi fermi smettono di essere simulati — la piu' grande ottimizzazione).\n\n"
"LEZIONI TRASFERIBILI AI SIMULATORI EDILI: i BIM e i simulatori di cantiere usano gli stessi integratori e le stesse strutture spaziali; la differenza e' il dominio (travi invece di proiettili). E la regola e' identica: la simulazione e' credibile quando e' stabile nel tempo, non quando e' perfetta in un singolo frame."""),

rec("GME-003","game_dev","netplay","NETWORKING DEI GIOCHI: IL REAL-TIME SULLA RETE INSTABILE",
"""Il netcode e' il problema piu' duro del multiplayer: la luce e' lenta e la rete perde pacchetti. Le soluzioni inventate qui hanno ispirato molti sistemi real-time.

LE SFIDE: latenza (30-200ms fisiologici), jitter (la latenza balla), pacchetti persi, ordine non garantito. Il giocatore non accetta niente di tutto questo.

LE ARCHITETTURE:
1. LOCKSTEP: tutti i client eseguono la stessa simulazione con gli stessi input: quasi zero traffico, ma non tollera giocatori con latenze diverse (RTS classici). Il determinismo della simulazione e' un requisito durissimo.\n2. STATE SYNC con INTERPOLAZIONE: ogni client invia il proprio stato 20-30 volte/sec; gli altri INTERPOLANO tra gli ultimi due stati ricevuti: si vede il passato di 50-100ms ma tutto e' fluido. Il prezzo: l'input del giocatore stesso appare con ritardo.\n3. CLIENT-SIDE PREDICTION + SERVER RECONCILIATION (il modello FPS moderno): il client simula il PROPRIO movimento istantaneamente; il server e' autorita'; quando arriva la risposta del server, il client confronta: se diverge, RICONCILIA ri-simulando dalla posizione corretta. Il lag esiste ma non lo senti.\n4. LAG COMPENSATION (rewind): il server, per valutare un colpo, riavvolge gli avversari di X ms (la latenza dello sparatore): il colpo conta dove il tiratore VEDEVA il bersaglio.\n\n"
"LEZIONI TRASFERIBILI: l'interpolazione (lisciare dati ritardati invece di mostrarli grezzi), la prediction/reconciliation (rendere ottimista l'interfaccia e correggere dopo), il rewind per le decisioni su stato storico — usati in dashboard collaborative, editing condiviso, robotica teleoperata.\n\n"
"REGOLA: nel real-time si disegna sempre il presente del locale e il passato (interpolato) degli altri — non esiste altra scelta fisica."""),

rec("GME-004","game_dev","procedural","GENERAZIONE PROCEDURALE: MONDI DA ALGORITMI",
"""La generazione procedurale crea contenuti da regole e semi casuali: il principio dietro Minecraft, No Man's Sky e gli strumenti di progettazione assistita.

LE TECNICHE FONDAMENTALI:
1. NOISE (PERLIN/SIMPLEX): il rumore correlato — a differenza del random puro, i valori vicini sono simili: base di terreni, nuvole, materiali. Si combinano ottave (frattali) per dettaglio a piu' scale.\n2. GENERAZIONE BASATA SU GRAMMATICHE: regole di sostituzione (grammatiche di Lindenmayer per piante e vegetazione): 'ogni ramo si divide in due piu' corti'); nelle citta' procedurali: 'ogni isolato ha edifici, ogni edificio ha facciate, ogni facciata ha finestre'.\n3. WAVE FUNCTION COLLAPSE: si parte dai vincoli (quali pezzi possono stare vicini) e si collassano le possibilita' fino a una soluzione coerente: tilemap, dungeon, texture.\n4. ALGORITMI SPAZIALI: Voronoi per biomi e distretti, diagrammi di Delaunay per reti stradali, random walk per caverne.\n\n"
"IL SEME (SEED): lo stesso seme genera lo stesso mondo: riproducibilita' totale — debuggare un mondo generato significa salvare il seme.\n\n"
"APPLICAZIONI FUORI DAI GIOCHI:\n- architettura parametrica (Grasshopper): facciate, reticoli, planivolumetrie esplorative generate da vincoli;\n- ottimizzazione di layout: generare 50 varianti di disposizione di vani valutate da funzioni di merito (luce, flussi);\n- test data: generare dataset sintetici realistici per testare software.\n\n"
"IL PRINCIPIO: la generazione procedurale non sostituisce il progettista — gli da' 50 bozze tra cui scegliere, come il quantity surveying computazionale."""),

rec("GME-005","game_dev","game_architettura","PROGETTARE UN GIOCO COMPLETO: DAL PROTOTIPO AL RILASCIO",
"""Il game development come disciplina di progetto: scope, prototipi, iterazione — lezioni che valgono per ogni software creativo.

LA REGOLA N.1: IL PROTOTIPO PRIMA DI TUTTO. Prima settimana: il 'core loop' giocabile con rettangoli grigi. Se non e' divertente/funzionale con i rettangoli, la grafica non lo salvera. Il prototipo risponde a UNA domanda ('il salto e' soddisfacente? il combattimento funziona?').

LO SCOPE: la causa di morte n.1 dei giochi indie (e dei progetti software): si pianifica il triplo di cio' che si riesce a fare. La disciplina: vertical slice (una sezione piccola ma completa di tutto: meccanica, grafica, audio, UI) prima di estendere — dimostra la qualita' prima dell'estensione.

L'ARCHITETTURA DI PROGETTO:
- GAME DESIGN DOCUMENT: vivo, breve, che descrive il 'cosa' non il 'come implementare';\n- DIREZIONE TECNICA: le decisioni irreversibili prese presto (engine, linguaggio, pipeline degli asset);\n- CONTENT PIPELINE: dal file dell'artista al gioco: gli strumenti di import, conversione e validazione sono meta' del lavoro;\n- SAVE SYSTEM e VERSIONING DEI DATI: i salvataggi devono sopravvivere agli aggiornamenti (versione del formato, migrazione).\n\n"
"IL RILASCIO E DOPO: il day-one patch, la telemetria (come si muovono i giocatori: dati reali per bilanciare), il live-ops (contenuti continui), la community. Il gioco rilasciato e' l'inizio del servizio.\n\n"
"LEZIONI TRASFERIBILI: prototipo -> vertical slice -> estensione; scope aggressivamente piccolo all'inizio; strumenti prima di contenuti; i dati dei reali utenti guidano le iterazioni. La stessa sequenza che vorrebbero seguire tutti i progetti software e pochi fanno."""),
]

formal = [
rec("FRM-001","formal","cosa_sono","METODI FORMALI: LA MATEMATICA CHE CONTROLLA IL SOFTWARE",
"""I metodi formali usano matematica per specificare e verificare il comportamento del software: costosi, potenti, e piu' accessibili di quanto si pensi.

LO SPETTRO DELLA RIGOROSA':
- TESTING: mostra la presenza di bug, non l'assenza (Dijkstra);\n- TYPE CHECKING (il piu' diffuso dei metodi formali): il compilatore verifica proprieta' su TUTTI i possibili input — e' la verifica formale che usi ogni giorno senza chiamarla cosi';\n- MODEL CHECKING: si esplora matematicamente TUTTI gli stati raggiungibili di un sistema (finito) e si verificano proprieta' ('mai due treni sullo stesso binario', 'il sistema non va in deadlock');\n- PROVE DI CORRETTEZZA: si dimostra con logica formale che il codice soddisfa la specifica — il livello piu' alto, usato sui sistemi critici (software aerospaziale, nucleari, crittografici).\n\n"
"DOVE SONO GIA' OGGI: i protocolli crittografici (verificati formalmente), i chip (verifica hardware — un chip sbagliato costa milioni), Amazon e Microsoft usano TLA+ per i protocolli distribuiti (AWS ha trovato bug subdoli nei suoi sistemi di replica PRIMA di implementarli), i compilatori (CompCert, compilatore C verificato — usato nell'aeronautica).\n\n"
"IL COSTO E IL GUADAGNO: la specifica formale obbliga a pensare CHIARAMENTE — il valore maggiore e' spesso nella chiarezza, prima ancora della verifica. Il costo e' la formazione e il tempo: giustificato su codice critico, inutile su un CRUD.\n\n"
"POSIZIONE PRAGMATICA: il 99% dei team non usera' mai le prove; ma SPECIFICARE con precisione (stati, transizioni, invarianti) e' gia' metodo formale applicato col pennello — e migliora ogni design."""),

rec("FRM-002","formal","specifica_invarianti","SPECIFICA, STATI E INVARIANTI: PENSARE IL SISTEMA COME AUTOMAT",
"""L'abilita' fondamentale dei metodi formali — pensare a stati e transizioni — e' gratuita e migliora ogni codice.

LA MACCHINA A STATI FINITI: lo strumento mentale piu' sottoutilizzato del software: ogni entita' del dominio ha STATI ammessi e TRANSIZIONI lecite. Il preventivo: Bozza -> Inviato -> Accettato/Rifiutato/Scaduto. Il cantiere: NonAvviato -> InCorso -> Sospeso -> Concluso -> Chiuso.

LE INVARIANTI: le condizioni che DEVONO restare vere in ogni stato valido: 'il preventivo accettato non ha voci modificate dopo la firma', 'il cantiere concluso non riceve materiali'. Scritte esplicitamente (anche solo come commento o assert), le invarianti trasformano i bug da sorprese a violazioni rilevabili.

LE TECNICHE PRATICHE:
- ENUM PER GLI STATI (mai booleani multipli incoerenti — 'isInviato && isAccettato' simultanei e' impossibile con un enum);\n- PATTERN MATCHING ESUSTIVO: il compilatore avvisa se manca una transizione;\n- TRANSIZIONI COME FUNZIONI ESPLICITE: 'accetta(preventivo)' invece di 'preventivo.stato = Accettato' sparso nel codice: in un punto solo si valida che la transizione sia lecita;\n- ASSERZIONI IN CODICE: assert(invariante) nei punti critici: falliscono in test, documentano in lettura.\n\n"
"L'ANALOGIA EDILE: gli stati e le transizioni sono il PROGRAMMA DEI LAVORI del software: chiare le fasi, chiari i passaggi, chiari i collaudi tra una fase e l'altra. Un cantiere senza programma dei lavori va come un software senza stati espliciti: avanti e indietro nel caos.\n\n"
"ESERCIZIO: prendere l'entita' piu' importante del dominio e disegnarne il diagramma stati/transizioni con invarianti: mezz'ora di lavoro che paga per anni."""),

rec("FRM-003","formal","model_checking","MODEL CHECKING: ESPLORARE TUTTI GLI STATI PRIMA DI SCRIVERE CODICE",
"""Il model checking e' la verifica automatica di proprieta' su un modello: il tool esplora TUTTI gli scenari possibili e trova i controesempi.

IL FLUSSO:
1. MODELLO: si descrive il sistema in un linguaggio formale (TLA+, PlusCal, Promela/Spin, Alloy): gli stati, le azioni, i vincoli. Non codice — un modello astratto piu' piccolo del sistema reale (si modella la PARTE critica: il protocollo di lock distribuito, non tutta l'app).\n2. PROPRIETA': si scrivono le cose da garantire: safety ('non succede mai X') e liveness ('prima o poi succede Y').\n3. ESECUZIONE: il checker esplora l'albero degli stati (con simmetrie e riduzioni per renderlo fattibile) e, se una proprieta' fallisce, restituisce LA TRACCIA ESATTA: la sequenza di passi che porta al guasto — un test case automatico.\n\n"
"IL VALORE CONCRETO (i casi famosi):\n- Amazon ha usato TLA+ sui protocolli di replicazione S3 e DynamoDB: trovati bug di coerenza PRIMA dell'implementazione — bug che i test probabilistici avrebbero mostrato dopo mesi in produzione;\n- i protocolli di consenso (Raft e altri) sono stati verificati e alcuni bug teorici scoperti cosi';\n- l'harware: i chip moderni sono verificati con model checking.\n\n"
"LIMITI REALI: esplosione combinatoria degli stati (il modello va astratto — la bravura e' nel modellare il giusto livello); non scala all'intero sistema; la proprieta' sbagliata verificata con successo vale zero.\n\n"
"QUANDO VALE LA PENA: protocolli distribuiti, sistemi concorrenti, algoritmi con invarianti critici — esattamente dove i test tradizionali sono piu' deboli (i bug concorrenti sono non deterministici: il checker e' deterministico per costruzione)."""),

rec("FRM-004","formal","tipi_prove","TIPI COME PROVE E PROGRAMMAZIONE TOTALE",
"""Nel confine tra tipi e logica: linguaggi dove 'se compila, e' corretto' e' quasi letterale.

L'IDEA (corrispondenza di Curry-Howard): i tipi sono enunciati, i programmi sono dimostrazioni. Un valore di tipo 'A -> B' e' una funzione che data una prova di A produce una prova di B. Conseguenze pratiche:
- I TIPI DIPENDENTI (Idris, Agda, Coq, F*): il TIPO dipende dal VALORE: 'una lista lunga esattamente n' o 'un importo in centesimi non negativo': alcuni bug diventano errori di compilazione impossibili;\n- TIPO OPTION/Maybe come unione disgiunta: 'valore o niente' nel tipo — la gestione del null obbligata dal compilatore (gia' visto in Kotlin/Rust: e' la versione pratica di questa filosofia);\n- PROGRAMMAZIONE TOTALE: vietato il non-terminare e il caso non gestito: ogni funzione copre tutti gli input — nella pratica si ottengono le funzioni totali tranne i punti espliciti marcati.\n\n"
"STRUMENTI PRATICI CHE ESISTONO GIA':\n- RUST: il borrow checker e' una forma di verifica formale sulla memoria usata da milioni di sviluppatori;\n- COQ/ISABELLE: dimostratori interattivi — compilatori verificati, kernel di sistema operativi (seL4, il microkernel con prove di correttezza funzionale usato in ambiti critici);\n- SAT/SMT SOLVER (Z3): motori di verifica logica usabili via API: si modellano vincoli (il planning dei turni del cantiere! le regole di magazzino!) e il solver dice se esiste soluzione e quale — risolutori di problemi di vincoli industriali.\n\n"
"POSIZIONE PRAGMATICA: non serve scrivere in Coq; serve SAPERE che questi strumenti esistono: quando un problema e' 'trovare una configurazione che rispetti 40 vincoli', la risposta e' un SMT solver, non mille if."""),

rec("FRM-005","formal","pragmatica","QUANDO USARE I METODI FORMALI: LA SCALA DELLA NECESSITA'",
"""Il senso pratico della verifica formale e' saperla dosare: piu' rigore dove il costo dell'errore cresce, meno dove il feedback e' veloce.

LA SCALA DELLA NECESSITA':
1. SOFTWARE CON FEEDBACK VELOCE (siti, app, gestionali): il costo del bug e' un fix di giorni — il testing abituale basta, la specifica formale e' lusso.\n2. SOFTWARE COSTOSO DA SBAGLIARE (pagamenti, dati personali, edilizia documentale): specifica esplicita di stati e invarianti, testing di proprieta', code review rigorosa — il livello 'pensare come un matematico senza strumenti'.\n3. SOFTWARE CRITICO PER SICUREZZA (impianti, ascensori, strutture controllate da software, automazione industriale): verifica formale vera (model checking sulle parti critiche, possibilmente certificazioni di processo come le norme IEC 61508/EN 50128).\n\n"
"LE DOMANDE CHE DECIDONO IL LIVELLO:\n- qual e' il costo peggiore di un bug non rilevato?\n- quanto e' lento il feedback loop (quanto tempo passa prima che l'errore si manifesti)?\n- il comportamento e' ricostruibile (stati espliciti) o emergente?\n\n"
"LE ABITUDINI FORMALI GRATUITE (per ogni livello):\n- stati come enum e transizioni come funzioni;\n- invarianti scritte e assertite;\n- funzioni pure per la logica di dominio: la testabilita' e' la porta d'ingresso alla verificabilita';\n- code review che chiede 'qual e' l'invariante di questa struttura?'.\n\n"
"L'ERRORE OPPOSTO: applicare la formalita' pesante dove non serve — paralizza il team e fa abbandonare la disciplina. La scienza della costruzione insegna la stessa scala: collaudi diversi per una tettoia e per un ponte, ma collaudi."""),
]

vision = [
rec("CVS-001","computer_vision","immagini_tensori","IMMAGINI COME NUMERI: PIXEL, CANALI E OPERAZIONI",
"""La computer vision e' il software che guarda: per capirla, partire da cosa e' un'immagine per una macchina.

LA RAPPRESENTAZIONE:
- GRIGLIA DI NUMERI: un'immagine e' un tensore: altezza x larghezza x canali (RGB = 3). Bianco e nero: 1 canale. Un'immagine 1080p e' un tensore 1080x1920x3 = 6,2 milioni di numeri.\n- OPERAZIONI BASE: luminosita' (somma), contrasto (scalatura), sfocatura (media dei vicini), edge detection (differenza dei vicini — il kernel Sobel, matrice 3x3 che convolve l'immagine).\n\n"
"LA CONVOLUZIONE: l'operazione madre: una piccola matrice (kernel) scorre l'immagine moltiplicando e sommando: ogni kernel estrae un pattern (bordi verticali, diagonali, texture). Le reti neurali convoluzionali NON sono altro che kernel IMPARATI dai dati: la prima riconosce bordi, la seconda angoli, la terza oggetti parziali, la quarta oggetti interi.\n\n"
"LE TRASFORMAZIONI GEOMETRICHE (connesse col corpus geometria): resize, crop, rotazione, prospettiva (omografia: da un'immine prospettica si stira verso la vista dall'alto — la base del document scanning: fotografa la tavola di cantiere e la appiattisci).\n\n"
"PREPROCESSING PER L'AI: normalizzazione dei valori (0-255 -> 0-1), ridimensionamento standard per il modello, aumentazione (rotazioni/tagli casuali per ingrandire il training set).\n\n"
"LIBRERIE: OpenCV (il coltello svizzero, open source), Pillow/PIL, scikit-image. Per ogni problema visivo, prima si chiede: 'questo lo risolvo con operazioni classiche o serve l'AI?' — i metodi classici su vincoli controllati sono piu' rapidi, esatti e spiegabili."""),

rec("CVS-002","computer_vision","vision_classica","VISIONE ARTIFICIALE CLASSICA: FEATURE E GEOMETRIA",
"""Prima del deep learning (e ancora oggi dove servono precisione e spiegabilita'): la visione classica risolve problemi misurabili.

LE TECNICHE CHE FUNZIONANO:
1. SOGLIA E MORFOLOGIA: binarizzazione (Otsu per scegliere la soglia automaticamente), poi operazioni morfologiche (erosione/dilatazione) per pulire: conteggio oggetti, rilevamento difetti su superfici uniformi, misura di aree.\n2. EDGE E CONTOURI: Canny (il rilevatore di bordi standard) -> contorni -> poligoni approssimati: misurare perimetri, forme, allineamenti.\n3. FEATURE CLASSICHE: SIFT/SURF/ORB — punti di interesse invarianti a scala e rotazione: il matching tra due immagini (la stessa facciata fotografata da due angoli) si fa abbinando i descrittori: base del photogrammetry e del rilievo da foto.\n4. CAMERA MODEL E CALIBRAZIONE: la proiezione 3D->2D con parametri intrinseci (focale, centro) ed estrinseci (posa): conoscerli permette di MISURARE dal mondo reale: 'questa foto contiene una quota di riferimento: misuriamo tutto il resto in scala'.\n\n"
"FOTOGRAMMETRIA E RILIEVO (il caso edile): serie di foto sovrapposte -> punti chiave abbinati -> nuvola di punti 3D -> mesh del monumento o del cantiere: il metodo del rilievo architettonico moderno (scanner laser a parte). Strumenti: COLMAP (open source), RealityCapture, i software dei droni.\n\n"
"DOCUMENT AI CLASSICO: rilevamento pagina -> rettifica -> binarizzazione -> OCR (Tesseract open source): la pipeline di digitalizzazione dei documenti di cantiere.\n\n"
"REGOLA DI SCELTA: visione classica dove il problema e' geometrico e controllato (misura, controllo qualita', allineamento); deep learning dove la variabilita' e' alta (oggetti diversi, scene complesse)."""),

rec("CVS-003","computer_vision","deep_vision","DEEP LEARNING PER LA VISIONE: DALLE CNN AI FOUNDATION MODEL",
"""La rivoluzione: le reti imparano le feature dai dati. Il panorama in cinque schede di progresso.

1. CNN (ALEXNET 2012, RESNET 2015): la convoluzione impara feature gerarchiche; ResNet introduce le connessioni residue (saltare un livello) che permettono reti profondissime: la profondita' e' diventata fattibile.\n2. DETECTION E SEGMENTAZIONE: non solo 'cosa c'e'' ma DOVE: YOLO (una sola passata, velocita' da video live), Faster R-CNN (accuratezza), U-Net e Mask R-CNN (segmentazione: pixel per pixel — contorni esatti degli oggetti).\n3. VIOLTURA SEMANTICA E ISTANZA: in cantiere: detection = 'ci sono 3 caschi', segmentation = 'questi pixel sono il casco di Rossi': la base dei controlli automatici di sicurezza (EPI rilevato/non rilevato).\n4. SELF-SUPERVISED E TRANSFER LEARNING: non serve milioni di etichette: si pre-allena su milioni di immagini non etichettate, poi si ADATTA al dominio con poche centinaia di esempi (fine-tuning): la pratica standard — 'pochi dati? parti da un modello pre-allenato'.\n5. I FOUNDATION MODEL DI VISIONE (CLIP 2021, SAM 2023, modelli visione-linguaggio): CLIP capisce immagini e testo insieme ('trova le foto del cantiere con ponteggio non ancorato' — ricerca semantica su archivi di foto); SAM segmenta QUALUNQUE cosa con un click/zero shot: la segmentazione e' diventata un servizio di base. I modelli multimodali recenti ragionano su immagini e testo insieme.\n\n"
"IL FLUSSO PRATICO DI UN PROGETTO: definire il compito (classificazione/detection/segmentazione) -> raccogliere e etichettare dati (il collo di bottiglia) -> partire da un modello pre-allenato -> fine-tuning -> valutazione su dati mai visti -> serving.\n\n"
"STRUMENTI: PyTorch/TensorFlow, Ultralytics YOLO (pronto all'uso), Hugging Face (modelli pre-allenati scaricabili), Roboflow/Label Studio (etichettatura)."""),

rec("CVS-004","computer_vision","vision_3d_industriale","VISIONE 3D INDUSTRIALE: DALLA FOTO ALL'OGGETTO",
"""La visione che misura il mondo: scanner, depth camera, ricostruzione 3D — il ponte con la geometria computazionale e la CAD library.

LE SORGENTI DI PROFONDITA':
- STEREOVISIONE: due camere come gli occhi: il DISPARITY (lo scarto tra le due immagini) diventa profondita' (triangolazione): economica ma fragile su superfici uniformi;\n- SENSORI ATTIVI: LiDAR (impulsi laser e tempo di ritorno: precisione millimetrica, usato in scanner da cantiere e droni), structured light (pattern proiettato: le deformazioni danno la forma — Kinect, FaceID), ToF (time of flight compatto);\n- DEPTH FROM MONOCAMERA: i modelli moderni stimano la profondita' da una sola immagine con reti neurali: utile ma assoluta (non metrica) — va calibrata.\n\n"
"NUVOLA DI PUNTI -> MESH -> MODELLO: la pipeline della scansione 3D: acquisizione -> allineamento delle scansioni (ICP, iterative closest point) -> fusione in nuvola densa -> ricostruzione di superficie (Poisson, marching cubes) -> mesh -> eventualmente conversione B-Rep per il CAD.\n\n"
"APPLICAZIONI EDILI:\n- SCAN-TO-BIM: scansione laser dell'esistente -> point cloud -> modellazione BIM dei fabbricati reali (lo stato di fatto per la ristrutturazione);\n- CONTROLLO GEOMETRICO: confronto automatico tra il modello nominale (BIM) e lo stato reale (point cloud): il 'deviazione heatmap' che colora dove la parete e' fuori tolleranza;\n- PROGRESS REPORTING: foto/scan periodiche -> confronto col programma dei lavori: l'avanzamento si misura invece di dichiararsi;\n- MISURA DA FOTO con un riferimento noto (metro, targhetta ArUco: i marcatori quadrati che le camere riconoscono e che danno scala e orientamento).\n\n"
"STRUMENTI: Open3D (open source), CloudCompare, Potree (visualizzatore web di point cloud), PCL."""),

rec("CVS-005","computer_vision","vision_ai_applicata","AI VISIONE APPLICATA AL CANTIERE: DALL'IMMAGINE ALLA DECISIONE",
"""Chiudere il cerchio: la visione artificiale che produce dati di business, dal controllo sicurezza al monitoraggio avanzamento.

I CASI D'USO CONCRETI:
1. SICUREZZA (EPI DETECTION): telecamere di cantiere + modello detection addestrato su caschi/gilet/sicurezza -> alert real-time quando un operaio entra in zona senza DPI. Note operative: privacy (non riconoscere PERSONE, riconoscere OGGETTI e zone; informativa e DPIA), falsi positivi gestiti con soglie e zone, il sistema AVVISA ma la responsabilita' resta umana.\n2. AVANZAMENTO LAVORI (IMAGE PROGRESS MONITORING): foto periodiche dagli stessi punti fissi (o droni) -> confronto con il modello: 'il cappotto e' stato posato al 60% della facciata nord': dati oggettivi per i SAL.\n3. CONTROLLO QUALITA': difetti di superficie (crepe, sfaldature, corrosione): detection/segmentazione su dataset addestrati col proprio archivio fotografico — il valore cresce con gli anni di foto documentate.\n4. DOCUMENTAZIONE INTELLIGENTE: foto di cantiere georeferenziate e timestampate -> collegate automaticamente alla voce di computo/capitolato (il retaggio: 'foto del getto del 12/3 nel fascicolo della platea').\n\n"
"L'ARCHITETTURA TIPO: edge (camera + box che gira il modello: latenza zero, privacy migliore — i video non escono dal cantiere) oppure cloud (piu' potenza, piu' costi dati). La scelta dipende da latenza, rete e privacy.\n\n"
"LE TRAPPOLE REALI:\n- il dataset non rappresenta la realta' (sole/pioggia/angolazioni diverse): la robustezza si ALLENA con varieta', non con quantita';\n- drift: il cantiere cambia, il modello resta fermo: monitoraggio continuo e riallenamento periodico;\n- il 'fatto a mano' prima del modello: molte regole di business si codificano in tre giorni di logica classica — il modello si usa per cio' che la logica non copre.\n\n"
"L'INTEGRAZIONE CON AURATRIX: la visione produce fatti ('zone ponteggio: 2 accessi senza casco tra le 14:00 e 15:00') che entrano nel registro — e l'LLM li riassume, confronta con i verbali, segnala i trend."""),
]

corpora = [
    ("consensus_storage.jsonl", consensus),
    ("game_development.jsonl", game),
    ("metodi_formali.jsonl", formal),
    ("computer_vision.jsonl", vision),
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
