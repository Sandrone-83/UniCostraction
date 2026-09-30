# -*- coding: utf-8 -*-
"""Coding_Master_Pack: 36 schede per portare un LLM al livello massimo di scrittura codice."""
import json, os

BASE = r"C:\Users\alessandro\Documents\kimi\tasks\2026-09-26\15-14-07-e3d653af\Coding_Master_Pack\parsed"
os.makedirs(BASE, exist_ok=True)

LIC = "Sintesi didattica originale Kimi (pubblico dominio)"
ATT = "Corpus coding master a cura di Kimi"

def rec(id_, cat, tema, title, text):
    return {"id": id_, "categoria": cat, "tema": tema, "title": title, "text": text,
            "source": f"coding_master_{cat}_kimi", "license": LIC, "commercial_ok": True,
            "attribution": ATT, "url": ""}

best = [
rec("CDB-001","best_practices","clean_code","CLEAN CODE AVANZATO: IL CODICE COME PROSA",
"Il codice si legge 10 volte piu' di quanto si scriva: chi scrive codice eccellente scrive per il lettore.\n\n"
"PRINCIPI PROFONDI:\n1. NOMI COME NARRAZIONE: una funzione ben nominata e' un commento gratuito. 'calcola_prezzo_con_sconto_fedelta' batte 'calc2'. La regola: il nome deve rispondere a perche' esiste, cosa fa e come si usa — senza dover leggere il corpo.\n"
"2. FUNZIONI PICCOLE E SINGLE-PURPOSE: una funzione fa UNA cosa, la fa bene, la fa solo lei. Se il nome contiene 'e' o 'poi', e' da dividere. Lunghezza sana: 5-15 righe.\n"
"3. ARGOMENTI POCHI: 0-2 argomenti ideali. Oltre i 3, conviene un oggetto parametro. Le flag booleane come argomento (fare_questo=True) nascondono due funzioni: dividerle.\n"
"4. SIDE EFFECTS ESPLICITE: una funzione che legge dati e una che modifica stato devono essere distinguibili al nome. La sorpresa e' il nemico della manutenibilita'.\n"
"5. STRUTTURE DI CONTROLLO PIATTE: evitare nesting oltre 2 livelli con early return (guard clauses): se i dati non sono validi, esci subito invece di avvolgere tutto in un if.\n"
"6. COMMENTI GIUSTI: spiegare il perche' (decisioni, vincoli, workaround), non il cosa (il codice gia' lo dice). Codice che richiede commento per essere capito va riscritto.\n\n"
"TEST RAPIDO DI QUALITA': puo' un nuovo sviluppatore capire cosa fa un modulo in 5 minuti leggendo solo i nomi? Se no, i nomi sbagliano."),

rec("CDB-002","best_practices","refactoring","REFACTORING: IL CATALOGO DELLE TRASFORMAZIONI SICURE",
"Refactoring = migliorare la struttura del codice senza cambiarne il comportamento, in piccoli passi verificabili.\n\n"
"MOVIMENTI FONDAMENTALI (quelli che risolvono l'80% dei problemi):\n1. ESTRAI FUNZIONE: un pezzo di codice con un'intenzione propria diventa funzione nominata. Cura la clausola duplicazione.\n"
"2. RINOMINA: il miglioramento piu' economico e piu' potente. Con gli IDE moderni e' istantaneo e sicuro.\n"
"3. INTRODUCI VARIABILE SPOGATA: una espressione complessa assegnata a variabile dal nome descrittivo si legge come una frase.\n"
"4. SOSTITUCI CONDIZIONALE CON POLIMORFISMO: una catena di if su un tipo diventa classi con un metodo comune.\n"
"5. SEPARA QUERY DA MODIFICATORE: una funzione che restituisce un valore O ne cambia lo stato, non entrambe.\n\n"
"COME FARE SENZA ROMPERE:\n- un passo alla volta, piccolo;\n- dopo ogni passo, i test verdi (senza test il refactoring e' un salto nel buio);\n- committare (Git) dopo ogni passo sicuro.\n\n"
"CODICI CATTIVI DA RICONOSCERE: duplicazione (la regola del tre: alla terza volta duplicata, astrailo), funzione lunga, classe che fa troppe cose, feature envy (una funzione che tocca piu' dati di un'altra classe), dati sparsi.\n\n"
"QUANDO FERMASI: il refactoring e' come pulire una casa — infinito se ci si lascia andare. Si ferma quando il codice cambiato e' 'abbastanza pulito' per il suo livello di rischio."),

rec("CDB-003","best_practices","code_review","CODE REVIEW: LA PRATICA CHE ALZA LA QUALITA' PIU' DI QUALSIASI TOOL",
"La revisione del codice e' il momento in cui il sapere passa tra sviluppatori e i difetti vengono catturati prima della produzione.\n\n"
"PER CHI SCRIVE LA PULL REQUEST:\n1. Piccola e focalizzata: una PR da 400 righe si revisiona bene; una da 4.000 no. Spezzare le modifiche grandi.\n"
"2. Descrizione che aiuta il revisore: cosa fa, perche', come testarla, decisioni discutibili da evidenziare.\n"
"3. Autorevisione prima: rileggere la propria diff elimina meta' dei problemi.\n\n"
"PER CHI REVISIONA:\n1. Prima il quadro: cosa dovrebbe fare questo cambiamento? Leggere titolo e descrizione, poi la diff nel suo insieme, poi riga per riga.\n"
"2. Domande, non ordini: 'hai considerato cosa succede se il cliente e' disattivato?' crea collaborazione; 'sbagliato' crea difesa.\n"
"3. Livelli di severita' onesti: BLOCKER (da correggere), SUGGESTION (valuta), NIT (gusto personale, non obbligatorio). Non pretendere la perfezione: chiedi cio' che conta.\n"
"4. Velocita': la review va fatta in giornata; una PR che invecchia genera conflitti e frustrazione.\n\n"
"COSA GUARDARE PRIMA: correttezza e test; poi design e naming; poi sicurezza (dati sensibili, input esterni); infine dettagli.\n\n"
"CULTURA: la review e' del codice, non della persona. I commenti si riferiscono sempre al codice ('questa funzione puo' fallire se...'), mai alla persona."),

rec("CDB-004","best_practices","errori_logging","GESTIONE ERRORI E LOGGING: IL SOFTWARE MATURO SI VEDE NEI GUAI",
"La differenza tra software artigianale e professionale emerge quando qualcosa va storto.\n\n"
"GESTIONE ERRORI:\n1. Errori RECUPERABILI (rete assente, file occupato): gestirli con retry, fallback o messaggio utile.\n2. Errori DI PROGRAMMAZIONE (bug): farli esplodere in sviluppo, loggarli e monitorarli in produzione. Catturarli e ignorarli (except: pass) e' il peggior peccato: il programma continua in uno stato inconsistente.\n3. VALIDAZIONE AI CONFINI: verificare ogni input esterno (utente, API, file) alla prima porta di ingresso, con messaggi d'errore che dicono come correggersi.\n\n"
"ECCEZIONI VS VALORI: i linguaggi moderni supportano entrambi (Result/Either o try/catch). Regola: eccezioni per eventi eccezionali, valori di ritorno per esiti attesi.\n\n"
"LOGGING PROFESSIONALE:\n- LIVELLI: DEBUG (diagnosi), INFO (eventi di business: 'preventivo creato'), WARNING (anomalia gestita), ERROR (operazione fallita), FATAL (servizio morto).\n"
"- STRUTTURA: timestamp, livello, servizio, contesto (id richiesta, utente), messaggio. I log testuali liberi non si analizzano: JSON o chiave=valore.\n"
"- MAI: password, token, dati personali nei log (GDPR!).\n"
"- UN LOG UTTILE dice cosa e' successo, con chi e perche': 'preventivo 4821 salvato per cliente 93 in 340ms' batte 'ok'.\n\n"
"PRINCIPIO: ogni errore non gestito e' un errore che tornera' dal cliente nel momento peggiore. Meglio incontrarlo in log la prima mattina."),

rec("CDB-005","best_practices","documentazione","DOCUMENTAZIONE DEL CODICE CHE VIENE LETTA",
"La documentazione giusta non descrive il codice (che gia' si legge): spiega cio' che il codice non puo' dire.\n\n"
"I LIVELLI:\n1. NEL CODICE: nomi e struttura (prima forma di documentazione), commenti sul perche'. Sempre aggiornati per costruzione.\n"
"2. README DEL PROGETTO: il contratto d'ingresso. Deve contenere: cosa fa il progetto, come si installa (comandi copiabili), come si avvia, come si testa, come si contribuisce. Un README che funziona e' testabile: seguirlo su una macchina pulita deve funzionare.\n"
"3. DECISIONI ARCHITETTURALI (ADR): un file breve per decisione importante: contesto, opzioni valutate, scelta, conseguenze. Risponde al 'perche' abbiamo fatto cosi?' di tra sei mesi.\n"
"4. API: OpenAPI/Swagger generato dal codice dove possibile: documentazione che non mentisce perche' vive col codice.\n\n"
"REGOLE DI SOPRAVVIVENZA:\n- documentazione vicina al codice (stessa repo), versionata insieme;\n- meno e' meglio: una pagina letta batte cento pagine ignorate;\n- esempi funzionanti: ogni snippet deve essere codice reale testato;\n- segnalare esplicitamente cosa e' obsoleto: la documentazione sbagliata e' peggio dell'assente.\n\n"
"TRAPPOLE: documentare DOPO (mai trovare il tempo), duplicare informazioni (che poi divergono), wikis orfani lontani dal codice."),

rec("CDB-006","best_practices","technical_debt","TECHNICAL DEBT: INDEBTIARSI CONSAPEVOLMENTE, RIMBORSARE PUNTUALMENTE",
"Il debito tecnico e' la differenza tra come il codice e' e come dovrebbe essere per il lavoro che fa ora. Come il debito finanziario: a volte conviene contrarlo, sempre conviene ripagarlo.\n\n"
"LE SPECIE:\n1. DEBITO INTENZIONALE: 'rilasciamo cosi' per tempo di mercato, con piano di rimborso. Legittimo.\n2. DEBITO INVOLONTARIO: scelte sbagliate fatte per fretta o ignoranza. Il peggiore, perche' sconosciuto.\n3. DEBITO DA EVOLUZIONE: codice corretto che invecchia male perche' il contesto e' cambiato (nuove esigenze, nuove librerie).\n\n"
"COME GESTIRLO:\n- MISURARLO: complessita' ciclomatica, duplicazione, copertura test, rating dei linter (SonarQube e simili). Non si ripaga cio' che non si vede.\n"
"- BUDGET DI MANUTENZIONE: il 15-20% dello sprint dedicato a ripagamenti continui (regola del boy scout: lasciare il codice un po' meglio di come lo si e' trovato).\n"
"- LAVORARE PER DIREZIONE: non 'rifattorizziamo tutto' (mai finire), ma 'ogni volta che tocchiamo un file, lo miglioriamo'.\n\n"
"SEGNALI DI SOVRACCARICO: i fix impiegano sempre piu', i bug tornano nei punti dove gia' erano stati risolti, i nuovi arrivati impiegano settimane per rendersi utili, nessuno vuole toccare certi moduli.\n\n"
"PRINCIPIO FINALE: il debito tecnico non si paga mai tutto — si paga l'interesse continuamente. L'obiettivo non e' codice perfetto ma codice il cui costo di cambiamento resta sostenibile."),
]

algoritmi = [
rec("ALG-001","algoritmi","pensiero_algoritmico","PENSIERO ALGORITMICO: RISOLVERE PROBLEMI PRIMA DI SCRIVERE CODICE",
"L'algoritmo e' la ricetta: il codice e' solo la traduzione. Chi pensa prima in algoritmi scrive codice migliore e piu' veloce.\n\n"
"IL METODO IN 5 PASSI:\n1. COMPRENDERE: riscrivere il problema con parole proprie, con un esempio concreto in mano. Non si risolve cio' che non si capisce.\n"
"2. ESEMPIO MANUALE: risolvere il caso piccolo a mano, annotando OGNI decisione. L'algoritmo e' la generalizzazione di quei passi.\n"
"3. PSEUDOCODICE: scrivere la soluzione in italiano strutturato (senza sintassi). Se non si riesce a dirlo, non si riuscira' a codarlo.\n"
"4. ANALISI: quanti passi per n elementi? Identificare il caso peggiore. Con 1 milione di elementi, un algoritmo O(n^2) fa un trilione di operazioni; uno O(n log n) ne fa venti milioni. La differenza e' il programma che risponde in un secondo contro quello che risponde in undici giorni.\n"
"5. VERIFICA: testare i casi limite: vuoto, uno, duplicati, negativi, enormi.\n\n"
"EURISTICHE PER TROVARE LA SOLUZIONE:\n- DEOMPOSIZIONE: spezzare il problema in sottoproblemi;\n- INDUZIONE: 'se sapessi risolverlo per n-1...' (base del ricorsivo);\n- INVARIANTE: trovare cosa resta vero a ogni passo del ciclo;\n- SIMMETRIA: il problema letto al contrario rivela la struttura;\n- RIDUZIONE: 'e' equivalente a un problema che gia' so risolvere?'\n\n"
"REGOLA D'ORO: due programmatori con lo stesso algoritmo scrivono codice simile; con algoritmi diversi, no. L'algoritmo e' il 90% della qualita'."),

rec("ALG-002","algoritmi","strutture_avanzate","STRUTTURE DATI AVANZATE: LO STRUMENTO GIUSTO CAMBIA TUTTO",
"La struttura dati giusta trasforma un problema impossibile in una riga di codice.\n\n"
"GRAFO DELLE SCELTE:\n- ARRAY/LISTA: accesso per indice, iterazione. Il default.\n"
"- HASH MAP (dizionario): 'esiste?', 'quante volte?', 'raggruppa per'. Il piu' sottoutilizzato dai principianti: cambia O(n) in O(1).\n"
"- SET: unicità garantita.\n"
"- PILA (stack): LIFO — undo, annidamento (parentesi bilanciate), DFS.\n"
"- CODA (queue): FIFO — lavori in attesa, BFS, task asincroni.\n"
"- HEAP (priority queue): 'il piu' urgente' in O(1), estrazione in O(log n). Code con priorita', top-k elementi.\n"
"- ALBERO (BST/bilanciato): ricerca ordinata O(log n), range query, prefissi.\n"
"- TRIE: albero dei prefissi — autocomplete, dizionari, ricerca per prefisso.\n"
"- UNION-FIND (disjoint set): 'fanno parte dello stesso gruppo?' con unione quasi istantanea — componenti connesse, Kruskal.\n"
"- GRAFO (liste di adiacenza): relazioni.\n\n"
"ESERCIZIO GUIDA — 'i due numeri che sommano a X':\n- Forza bruta: controllare tutte le coppie O(n^2).\n- Con hash map: scorrere una volta; per ogni numero, cercare X-numero nella mappa. O(n). La struttura dati ha eliminato un fattore n.\n\n"
"PRINCIPIO: prima domanda giusta — 'quali OPERAZIONI devo fare di piu'?' La struttura ottimizza quella."),

rec("ALG-003","algoritmi","grafi","ALGORITMI SU GRAFI: BFS, DFS E I CAMMINI",
"I grafi modellano il mondo: strade, reti sociali, dipendenze tra attivita' (cantieri!), pagine web.\n\n"
"RAPPRESENTAZIONE: lista di adiacenza (per ogni nodo, i vicini): memoria O(n+m), iterazione efficiente. Il default.\n\n"
"DFS (RICORSIONE/ PILA): esplora in profondita'. Usi: raggiungibilita', cicli, componenti connesse, ordinamento topologico (ordine di esecuzione delle attivita' con vincoli — esattamente il diagramma di un cantiere!), maze solving.\n\n"
"BFS (CODA): esplora a onde. Usi: cammino PIU' CORTO in grafi non pesati, 'grado di separazione', livelli di un albero, raggiungibilita' nel minor numero di passi.\n\n"
"CAMMINI MINIMI CON PESI:\n- DIJKSTRA: pesi non negativi. O(n log n) con heap. La scelta standard (mappe stradali).\n"
"- BELLMAN-FORD: pesi negativi ammessi; rileva cicli negativi.\n"
"- FLOYD-WARSHALL: tutte le coppie di nodi, grafi piccoli (n<500): tre cicli annidati e ogni coppia ottimale.\n\n"
"ALBERO DI COPERTURA MINIMO (MST): collegare tutti i nodi col costo minore. KRUSKAL (ordinamento archi + union-find) e PRIM (crescita da un nodo). Applicazione: reti di tubazioni/impianti con minimo materiale.\n\n"
"REGOLE PRATICHE: grafo piccolo e 'tutte le coppie' -> Floyd; sorgente unica, pesi positivi -> Dijkstra; non pesato -> BFS; dipendenze e ordini -> topologico DFS."),

rec("ALG-004","algoritmi","programmazione_dinamica","PROGRAMMAZIONE DINAMICA: IL PARADIGMA DEI PROBLEMI IMPOSSIBILI",
"La programmazione dinamica (PD) risolve problemi che sembrano esponenziali in tempo polinomiale, memorizzando cio' che e' gia' stato calcolato.\n\n"
"LA RICETTA IN TRE PASSI:\n1. DEFINIRE LA SOTTOSTRUTTURA: come il problema su n elementi si riduce a problemi piu' piccoli? La frase magica: 'il risultato per i primi n dipende solo dai risultati per n-1, n-2...'.\n"
"2. DEFINIRE LA RICORRENZA: scrivere la formula: dp[n] = migliore tra (dp[n-1] + qualcosa, dp[n-2] + altro).\n"
"3. IMPLEMENTARE TOP-DOWN (memoizzazione: ricorsione + cache) o BOTTOM-UP (tabella iterativa, spesso piu' efficiente).\n\n"
"I CLASSICI DA SAPERE A MEMORIA:\n- FIBONACCI (l'hello world della PD): senza cache e' esponenziale; con cache e' lineare.\n"
"- KNAPSACK (zaino): capacita' limitata, massimizzare valore — dietro ogni ottimizzatore di carichi e di budget.\n"
"- LIS (longest increasing subsequence): ordinamenti nascosti.\n"
"- EDIT DISTANCE (distanza di Levenshtein): quanto due stringhe somigliano — dietro il controllo errori e la ricerca fuzzy.\n"
"- COIN CHANGE: numero di modi di fare un importo con certe monete — analogo al computo delle combinazioni di preventivo.\n\n"
"SEGNI CHE UN PROBLEMA E' DA PD: 'massimizza/minimizza qualcosa', 'quanti modi di...', 'dato un limite (budget/peso/capacita')', sottoproblemi che si ripetono (l'albero di ricorsione naive visita gli stessi nodi milioni di volte).\n\n"
"ERRORE TIPICO: provare la PD senza prima aver scritto la ricorsione naive. La versione naive e' il progetto dell'edificio; la PD e' solo il modo veloce di costruirlo."),

rec("ALG-005","algoritmi","paradigmi","DIVIDE ET IMPERA E GREEDY: QUANDO LA SCELTA OCAZZIONALE FUNZIONA",
"Due paradigmi complementari alla PD, piu' semplici e spesso piu' rapidi.\n\n"
"DIVIDE ET IMPERA:\nIdea: spezza il problema a meta', risolvi ricorsivamente, combina. Quando il costo di combinare e' basso, il guadagno e' enorme.\n- MERGE SORT e QUICK SORT: l'ordinamento in O(n log n) nasce cosi'.\n- RICERCA BINARIA: dimezza a ogni passo — da un milione di elementi a trovarne uno in 20 confronti. Applicazione: ricerca in liste ordinate, e soprautto RICERCA BINARIA SULLA RISPOSTA: quando la soluzione e' un numero e 'e' fattibile(X)?' si puo' verificare, si cerca binariamente sui valori.\n- ALGORITMI GEOMETRICI: closest pair di punti.\n\n"
"GREEDY (INGORDO):\nIdea: fai sempre la scelta localmente migliore. Funziona SOLO se il problema ha la struttura giusta: scelta greedy sicura + sottostruttura ottima.\n- CLASSICI FUNZIONANTI: attivita' (massimizza attivita' senza sovrapposizioni), codici di Huffman (compressione), Kruskal/Prim (MST), Dijkstra.\n- CLASSICI INGANNEVOLI: zaino frazionario si, zaino 0/1 no (serve PD), cambio monete con certi set fallisce.\n\n"
"COME RICONOSCERE GREEDY-SICURO: se scambiare due elementi nella soluzione non peggiora mai (proprieta' di scambio / matroid), il greedy funziona. Altrimenti no.\n\n"
"STRATEGIA DI ESAME/RISOLUZIONE: 1. prova greedy (e verifica contro casi limite); 2. se fallisce, scrivi ricorsione naive; 3. se si ripetono sottoproblemi -> memoizza (PD)."),

rec("ALG-006","algoritmi","ricerca_ordinamento","RICERCA, ORDINAMENTO E COMPLESSITA': LE DECISIONI QUOTIDIANE",
"Le decisioni su ricerca e ordinamento si prendono ogni giorno: la maggior parte delle ottimizzazioni di performance e' qui.\n\n"
"ORDINAMENTO — COSA USARE:\n- NON scrivere mai un sort a mano: la libreria standard del linguaggio e' gia' ottimale (Timsort in Python/Java, Introsort in C++).\n"
"- QUICK SORT vs MERGE SORT: quicksort e' piu' veloce in media e in cache, merge e' stabile e garantito O(n log n).\n"
"- STABILE vs INSTABILE: l'ordinamento stabile mantiene l'ordine relativo degli elementi uguali — necessario per ordinare per piu' chiavi in sequenza (prima per citta', poi per data).\n"
"- COUNTING/RADIX: quando i valori sono interi in un range piccolo, si ordina in O(n) ignorando i confronti.\n\n"
"RICERCA:\n- Sequenziale O(n): solo per liste piccole o non ordinate.\n"
"- Binaria O(log n): prerequisito lista ordinata. Il return sull'investimento di un indice.\n"
"- HASH: ricerca per chiave in O(1) medio — l'hash map batte qualsiasi albero quando non serve l'ordinamento.\n\n"
"COMPLESSITA' IN PRATICA — REGOLE EMPIRICHE:\n- O(log n): impossibile notarlo.\n- O(n): su un milione di elementi, millisecondi.\n- O(n log n): su un milione, decimi di secondo.\n- O(n^2): su un milione, giorni. IL MALEDETTO: cicli annidati su dati esterni. La causa n.1 di lentezze in produzione.\n- O(2^n): oltre i 40 elementi e' irrealizzabile: il segno che serve PD, greedy o euristica.\n\n"
"PRINCIPIO FINALE: conoscere i limiti asintotici serve per RICONOSCERE la forma del problema (due cicli annidati su crescite insieme = quadratica) — la prima domanda di chi ottimizza: 'qual e' la complessita' attuale?'"),
]

linguaggi = [
rec("LIN-001","linguaggi","python_avanzato","PYTHON AVANZATO: IDIOMI CHE DISTINGUONO IL SENIOR",
"Python si impara in un weekend e si padroneggia in anni. Gli idiomi che separano i livelli:\n\n"
"1. COMPRENSIONI DI LISTE/DIZIONARI: espressive e veloci: 'quadrati = [x*x for x in numeri if x > 0]'. Ma regola: se serve piu' di un'istruzione o una lettura si perde, usare il ciclo normale.\n"
"2. GENERATORI: 'yield' al posto di return per flussi di dati — processano milioni di righe senza caricarle in memoria. 'for riga in leggi_csv_enorme():' consuma riga per riga.\n"
"3. DECORATORI: '@misura_tempo' sopra una funzione ne aggiunge comportamento senza toccarla (logging, cache, auth). Sono funzioni che avvolgono funzioni.\n"
"4. CONTESTI (with): 'with open(...)' gestisce la chiusura anche in caso di errore — obbligatorio per file, connessioni, lock.\n"
"5. TYPING: i type hints 'def calcola(mq: float, prezzo: float) -> float:' non rallentano nulla ma abilitano il controllo statico (mypy) che trova bug prima dell'esecuzione — su codice di qualunque dimensione.\n"
"6. DATACLASSES e Pydantic: modelli di dati con validazione e serializzazione in due righe invece di cento.\n"
"7. AMBIENTI VIRTUALI: ogni progetto col suo interprete e sue librerie: 'python -m venv .venv'. Mai installare nel sistema.\n\n"
"ERRORI DA NON FARE MAI: mutare una lista mentre la si itera, usare liste di default mutabili come argomento (def f(x=[])), credere che '=' copi (copia il riferimento: serve copy/deepcopy), catturare except Exception senza log.\n\n"
"PROFILING: prima di ottimizzare, 'cProfile' dice dove il tempo va davvero."),

rec("LIN-002","linguaggi","javascript_typescript","JAVASCRIPT E TYPESCRIPT MODERNI: IL LINGUAGGIO DEL WEB, FATTO BENE",
"JavaScript e' ovunque (browser, server, mobile); TypeScript e' JavaScript con i tipi, ed e' lo standard professionale.\n\n"
"CONCETTI JS CHE BISOGNA SAPERE DAVVERO:\n1. ASYNC/AWAIT: le operazioni lente (rete, file) non bloccano: 'const dati = await fetch(url)'. Promesse con async/await sono la base di ogni app moderna.\n"
"2. CLOSURE: una funzione che 'ricorda' le variabili dove e' nata. Dietro ogni callback, memoizzazione, e stato privato.\n"
"3. EVENT LOOP: JS e' single-threaded ma non bloccante: capire la coda degli eventi spiega meta' dei bug misteriosi (perche' il console.log stampa prima del risultato?).\n"
"4. == vs ===: usare SEMPRE === (senza coercizione).\n\n"
"TYPESCRIPT — IL SALTO DI QUALITA':\n- interfacce e tipi: 'interface Preventivo { cliente: string; importo: number }';\n"
"- il compilatore trova in compilazione gli errori che in JS emergerebbero in produzione;\n"
"- 'unknown' invece di 'any' quando il tipo e' ignoto: obbliga a verificare prima dell'uso;\n"
"- generics: funzioni e strutture tipizzate senza duplicazione.\n\n"
"ECOSISTEMA 2026: Node.js o Bun lato server, bundler come Vite, framework React/Next.js, gestione pacchetti con pnpm.\n\n"
"REGOLE D'ORO: TypeScript strict mode sempre attivo; gestire TUTTE le promesse (un await dimenticato = bug silenzioso); non usare var (let/const); formattatore (Prettier) e linter (ESLint) automatizzati."),

rec("LIN-003","linguaggi","sql_avanzato","SQL AVANZATO: OLTRE IL SELECT SEMPLICE",
"SQL e' il linguaggio che sopravvive da 50 anni perche' descrive COSA si vuole, non come ottenerlo.\n\n"
"IL LIVELLO AVANZATO:\n1. JOIN PERFETTO: INNER (solo corrispondenze), LEFT (tutti della sinistra), FULL (tutti). L'errore classico: LEFT JOIN con condizioni nel WHERE che lo trasformano in INNER.\n"
"2. CTE (WITH): query nominate e componibili: 'WITH clienti_attivi AS (...) SELECT ... FROM clienti_attivi'. Leggibilita' enorme e ricorsione (WITH RECURSIVE per alberi e gerarchie — categorie di materiali!).\n"
"3. WINDOW FUNCTIONS: aggregazioni SENZA collassare le righe: 'ROW_NUMBER() OVER (PARTITION BY cantiere ORDER BY data DESC)' = l'ultimo evento per ogni cantiere. LEAD/LAG per confrontare con la riga precedente (variazioni mese su mese). Fondamentali sui report.\n"
"4. GROUPING SETS / ROLLUP: subtotali e totali in una query sola.\n\n"
"OTTIMIZZAZIONE:\n- EXPLAIN ANALYZE prima di tutto: il piano di esecuzione dice dove il tempo va;\n"
"- INDICI: una colonna cercata in WHERE/JOIN/ORDER BY. Attenzione: indici accelerano la lettura e rallentano scrittura;\n"
"- SELECT solo le colonne necessarie: 'SELECT *' su tabelle grandi e' uno spreco misurabile;\n"
"- N+1: il pattern in cui per ogni riga di una query se ne fa un'altra — risolvere con JOIN o batch.\n\n"
"INTEGRITA': vincoli FOREIGN KEY, UNIQUE, NOT NULL nel database, non solo nell'applicazione: il database e' l'ultima linea di difesa dei dati.\n\n"
"REGOLA: ogni query deve avere un indice che la serve; ogni report complesso merita una CTE."),

rec("LIN-004","linguaggi","cpp_rust","C++ E RUST: IL CONTROLLO ESTREMO E COME RAGGIUNGERLO",
"Quando ogni ciclo di clock conta (game engine, embedded, sistemi operativi, robotica da cantiere), si scende di livello.\n\n"
"CONCETTI C++ ESSENZIALI:\n- GESTIONE MANUALE DELLA MEMORIA: malloc/free, poi new/delete, poi gli smart pointer (unique_ptr, shared_ptr) che liberano automaticamente: RAII (Resource Acquisition Is Initialization): una risorsa si lega a un oggetto e viene liberata alla sua distruzione.\n"
"- ZERO-COST ABSTRACTIONS: i template generano codice macchina ottimizzato a compile time: astrazione senza penalita'.\n"
"- COSTRUTTORE/DISTRUTTORE/COPY: la regola del tre (o del cinque in C++11+): se definisci uno, probabilmente serve tutta la gestione del ciclo di vita.\n\n"
"RUST — LA SICUREZZA DI MEMORIA COME GARANZIA:\n- OWNERSHIP: ogni valore ha un proprietario unico; quando il proprietario esce di scope, il valore e' liberato. Il borrow checker a compile time impedisce: use-after-free, double free, data race. Errori di memoria che in C++ sono runtime, in Rust sono errori di compilazione.\n"
"- BORROWING (&T immutabile, &mut T mutabile): regola — o n lettori o UN scrittore.\n"
"- RESULT/OPTION invece di eccezioni: gli errori sono nel tipo di ritorno, obbligati a gestirli.\n"
"- SENZA GARBAGE COLLECTOR: prestazioni C++ con sicurezza dimostrata a compile time.\n\n"
"QUANDO SCEGLIERLI: C++ per codebase esistenti, ecosistemi consolidati, latenza ultra-bassa; Rust per nuovi sistemi, sicurezza, tooling (Cloudflare, AWS, Linux usano Rust sempre di piu').\n\n"
"PER IL RESTO DI NOI: anche scrivendo Python/JS, i concetti di RAII, ownership e ciclo di vita rendono il codice migliore ovunque."),

rec("LIN-005","linguaggi","go","GO: LA SEMPLICITA' CHE SCALA",
"Go (golang) e' il linguaggio dei servizi cloud e degli strumenti infrastrutturali (Docker, Kubernetes, Terraform). La sua filosofia: pochi costrutti, uno stile, concorrenza di prima classe.\n\n"
"CARATTERISTICHE CHIAVE:\n1. GOROUTINE: 'go funzione()' lancia lavoro concorrente con costo di pochi KB — migliaia di goroutine dove altri linguaggi gestiscono decine di thread.\n"
"2. CHANNEL: le goroutine parlano tramite canali tipizzati: 'ch <- valore' e 'valore := <- ch'. La filosofia: 'non comunicare condividendo la memoria; condividi la memoria comunicando'.\n"
"3. SELECT: attesa multipla su piu' canali con timeout di default.\n"
"4. COMPILAZIONE RAPIDISSIMA E BINARIO STATICO: un unico eseguibile da distribuire — niente runtime da installare. Ideale per CLI e microservizi.\n\n"
"COSA MANCA (per scelta): generics arrivati tardi e minimi, niente eccezioni strutturate (error values controllati), niente classi (composition over inheritance: struct + interface implice).\n\n"
"ERROR HANDLING IDIOMATICO: if err != nil { return err } — verboso ma esplicito: ogni errore e' gestito sul posto.\n\n"
"QUANDO GO E' LA SCELTA GIUSTA: API e microservizi, CLI tools, agenti e automazioni che devono girare ovunque con un binario solo, sistemi di rete. Quando la semplicita' operativa conta piu' delle astrazioni sofisticate.\n\n"
"LEZIONE TRASFERIBILE: la limitazione deliberata (un solo modo di fare le cose) riduce il costo di lettura del codice altrui — una qualita' sottovalutatissima nei team."),

rec("LIN-006","linguaggi","scelta_linguaggio","COME SCEGLIERE IL LINGUAGGIO GIUSTO PER OGNI PROBLEMA",
"Non esiste il linguaggio migliore in assoluto: esiste il linguaggio migliore per QUEL problema, QUEL team, QUEL contesto.\n\n"
"MATRICE DI SCELTA PRATICA:\n- WEB FRONTEND: TypeScript (non c'e' alternativa reale).\n"
"- BACKEND/API CRUD e prodotti veloci: TypeScript/Node, Python (FastAPI/Django), Go.\n"
"- DATA, AI, SCRIPTING, CALCOLI: Python (ecosistema scientifico irraggiungibile).\n"
"- APP MOBILE: Kotlin/Swift native per performance e piattaforma; Flutter/Dart per cross-platform.\n"
"- DESKTOP: Electron/TS per velocita' di sviluppo; Rust/Tauri per leggerezza.\n"
"- SISTEMI, EMBEDDED, LATENZA CRITICA: C++, Rust, C.\n"
"- MICROSERVIZI E INFRASTRUTTURA: Go, Rust.\n"
"- PROTOTIPI VELOCI E AUTOMATIONI: Python.\n\n"
"I FATTORI CHE CONTANO DAVVERO (in ordine):\n1. ECOSISTEMA DELLE LIBRERIE per quel dominio (scrivi meno tu, meno bug tuoi);\n"
"2. ESPERIENZA DEL TEAM: un linguaggio nuovo al 30% della velocita' per 6 mesi;\n"
"3. ASSUNZIONI E MERCATO: quanti sviluppatori si trovano?\n"
"4. OPERATIVITA': deployment, osservabilita', costi di esecuzione;\n"
"5. PERFORMANCE: ultima, salvo requisiti duri (embedded, high-frequency).\n\n"
"ANTI-PATTERN: scegliere per moda, riscrivere tutto nel linguaggio nuovo, polyglottismo senza bisogno (ogni linguaggio in piu' e' costo operativo: build, dipendenze, competenze).\n\n"
"REGOLA DEL CONSULENTE ONESTO: il linguaggio giusto e' quasi sempre quello che il team gia' conosce e che ha le librerie per il dominio — salvo motivi misurabili per cambiare."),
]

system = [
rec("SYS-001","system_design","metodo","SYSTEM DESIGN: IL METODO CHE USANO I MIGLIORI INGEGNERI",
"Il system design non si improvvisa: e' un metodo ripetibile.\n\n"
"IL PROCESSO IN 6 FASSE:\n1. REQUISITI (5-10 min): QPS (richieste/sec), dati al giorno, latenza attesa, utenti, casi d'uso principali. Numeri su carta: senza numeri ogni decisione e' opinione.\n"
"2. API E MODELLO DATI: prima le entita' e le operazioni ('POST /preventivi', tabelle clienti/preventivi/voci), poi tutto il resto.\n"
"3. ARCHITETTURA AD ALTO LIVELLO: client, load balancer, servizi, database, cache, coda. Disegnare prima il flusso principale.\n"
"4. APPROFONDIMENTO COMPONENTE PER COMPONENTE: per ognuno: cosa fa, come scala, cosa succede se muore.\n"
"5. BOTTLENECK E SCALE: che succede a 10x? Dove si rompe prima? (quasi sempre: database e single point of failure).\n"
"6. OPERATIVITA': monitoraggio, logging, backup, deploy.\n\n"
"LE DOMANDE CHE GUIDANO OGNI PROGETTO:\n- Quale e' la LETTURA/SCRITTURA ratio? (leggi molto -> cache; scrivi molto -> sharding, code);\n"
"- Quanto deve essere FRESH il dato? (sempre perfetto -> database forte; tolleranza -> cache e code);\n"
"- Quali sono i SINGLE POINT OF FAILURE? (eliminare o addormentare il rischio);\n"
"- Che succede se un nodo muore a meta' di un'operazione? (idempotenza).\n\n"
"ERRORE DEL PRINCIPIANTE: progettare per 10 milioni di utenti che non ci sono. Progettare per 10.000 con una strada chiara verso 10 milioni."),

rec("SYS-002","system_design","scalabilita","SCALABILITA' E SISTEMI DISTRIBUITI: CAP, SHARDING, CACHING",
"Quando un server non basta, le risposte sono tre famiglie: replicare, spezzare, memorizzare vicino.\n\n"
"CAP (impossibilita' fondamentale): in presenza di partizione di rete, si puo' scegliere solo due tra Consistenza e Disponibilita'. CP: database bancari (meglio errore che dato sbagliato). AP: social, carrelli e-commerce (meglia dato vecchio che sito giu'). Ogni database e' una scelta su questo asse.\n\n"
"SCALING:\n- VERTICALE: macchina piu' grossa. Semplice, fino a un punto.\n"
"- ORIZZONTALE: piu' macchine. La strada vera: load balancer (round-robin, least-conn), stateless application server (lo stato vive nel database/cache, non nella memoria del processo).\n\n"
"SHARDING (partizionamento dei dati): dividere i dati su piu' database per chiave (user_id -> shard n). Funziona quando la chiave di sharding coincide con i pattern di query dominanti. Costi: query cross-shard, resharding doloroso, join complicati.\n\n"
"CACHING — IL MIGLIORAMENTO PIU' RAPIDO:\n- Cache applicativa (Redis/Memcached): il dato caldo in RAM;\n"
"- Cache CDN per i contenuti statici vicino all'utente;\n"
"- PATTERN: cache-aside (leggi cache, se manca leggi DB e popola), write-through (scrivi DB e cache insieme), TTL (scadenza: la coerenza si compra con la scadenza);\n"
"- IL MALEDETTO: cache stampede (tutte le richieste arrivano insieme quando la cache scade): lock o rigenerazione anticipata.\n\n"
"REGOLA PRATICA: prima replica e stateless, poi cache, e solo alla fine sharding — nell'ordine di dolore crescente."),

rec("SYS-003","system_design","architetture","ARCHITETTURE: EVENT-DRIVEN, CQRS, MICROSERVIZI E QUANDO NON USARLI",
"Le architetture moderne rispondono a problemi specifici; adottate per moda creano complessita' gratuita.\n\n"
"MICROSERVIZI: servizi piccoli, indipendenti, deployabili separatamente. Guadagni: scalabilita' selettiva, team autonomi, deploy indipendenti. Costi: network failure, distributed transactions, osservabilita' complessa, dati duplicati. REGOLA: partire da monolite modulare; estrarre servizi quando un dominio ha esigenze di scala o release diverse.\n\n"
"EVENT-DRIVEN: i componenti parlano tramite eventi (code come Kafka/SQS) invece di chiamate sincrone. Guadagni: disaccoppiamento, buffering di picchi, reazione in tempo reale. Costi: eventual consistency, debugging distribuito, ordinamento eventi. PATTERN: outbox (salva evento e dato nella stessa transazione), idempotent consumer (processare due volte lo stesso evento non deve fare danni).\n\n"
"CQRS (Command Query Responsibility Segregation): scritture e letture usano modelli separati. La lettura e' denormalizzata e veloce; la scrittura e' il modello di dominio. Ideale quando le query di lettura sono complesse e i dati cambiano raramente (report, dashboard). Costo: sincronizzazione.\n\n"
"DOMAIN-DRIVEN DESIGN (DDD): progettare il software attorno al linguaggio del dominio (nel nostro caso: Cantiere, Computo, SAL, Capitolo). Bounded context: ogni modulo ha il suo modello; i moduli parlano via API/eventi espliciti. Il DDD vale per domini complessi — come l'edilizia.\n\n"
"REGOLA FINALE: l'architettura giusta e' la piu' semplice che sopravvive ai requisiti di domani, non la piu' sofisticata di oggi."),

rec("SYS-004","system_design","database_scelta","DATABASE: SCEGLIERE E MODELLAARE (SQL, NOSQL, VETTORIALI)",
"La scelta del database e' una delle decisioni piu' durature: cambiarla dopo costa mesi.\n\n"
"PANORAMICA:\n- RELAZIONALE (PostgreSQL, MySQL): il default. Dati strutturati, integrita', transazioni ACID, JOIN. Copre l'80% dei casi.\n"
"- DOCUMENTALE (MongoDB): dati semi-strutturati, schemi fluidi, aggregazioni. Attenzione: senza disciplina lo schema deriva nel caos.\n"
"- CHIAVE-VALORE (Redis): cache, sessioni, contatori, code. Velocita' estrema, persistenza limitata.\n"
"- WIDE-COLUMN (Cassandra, Bigtable): scritture massive, time-series.\n"
"- GRAFO (Neo4j): relazioni come cittadino di primo livello: reti sociali, dipendenze, reti di fornitori.\n"
"- VETTORIALE (pgvector, Pinecone, Qdrant): ricerca per SIMILITUDINE semantica — il cuore dei sistemi RAG per l'AI.\n\n"
"MODELLAZIONE: nel relazionale, partire dalle QUERY: 'cosa devo chiedere al database?' Le tabelle nascono dalle domande, non dalle entita' astratte. Normalizzare fino alla terza forma per i dati operativi; denormalizzare deliberatamente per i report.\n\n"
"INDICI E PERFORMANCE: indice = struttura che rende la ricerca O(log n) ma costa scrittura e spazio. Indicizzare WHERE, JOIN, ORDER BY. EXPLAIN per verificare.\n\n"
"REGOLE PRATICHE: PostgreSQL come default quasi universale; aggiungere Redis quando c'e' traffico di lettura; aggiungere vettoriale quando arriva l'AI; documentale solo per dati documentali veri; uscire dal relazionale solo con un motivo misurabile."),

rec("SYS-005","system_design","api_design","API DESIGN EVOLUTO: REST FATTO BENE, GRAPHQL, WEBHOOK, RATE LIMITING",
"Le API sono il contratto tra sistemi: come i capitolati tra impresa e committente, devono essere chiare, stabili e oneste.\n\n"
"REST FATTO BENE:\n- RISORSE NOME PLURALE: /preventivi, /clienti/{id}/preventivi;\n"
"- VERBI HTTP GIUSTI: GET (leggi), POST (crea), PUT/PATCH (aggiorna), DELETE;\n"
"- CODICI DI STATO ONESTI: 201 creato, 400 input invalido, 401 non autenticato, 403 non autorizzato, 404, 409 conflitto, 500 errore interno;\n"
"- PAGINAZIONE obbligatoria sulle liste: cursor-based (stabile sotto inserimenti);\n"
"- VERSIONING: /v1/ nell'URL o header; mai rompere contratti esistenti — deprecare con avviso;\n"
"- FILTRI E SORTING espliciti: ?stato=aperto&sort=-data.\n\n"
"GRAPHQL: il client chiede esattamente i campi che vuole. Ideale: frontend complessi, molte viste diverse sugli stessi dati. Costi: caching piu' difficile, query costose possibili (limitare profondita' e complessita').\n\n"
"WEBHOOK: il server avvisa il client ('evento avvenuto') invece di farlo interrogare. Regole: firmare le richieste (verifica provenienza), rispondere subito 200 e processare async, retry con backoff, idempotenza (il destinatario deve poter ricevere due volte lo stesso evento senza danni).\n\n"
"RATE LIMITING E QUOTA: proteggere ogni API pubblica: limiti per utente/chiave, code 429 con Retry-After. Senza di essa, un singolo cliente con un loop basta.\n\n"
"PRINCIPIO: un'API e' una promessa: cambiare il comportamento senza cambiare versione e' una rottura di contratto."),

rec("SYS-006","system_design","affidabilita","AFFIDABILITA': IDEMPOTENZA, RETRY, CIRCUIT BREAKER E SAGHE",
"I sistemi distribuiti falliscono di continuo: l'affidabilita' non e' prevenire i guasti ma sopravviverli.\n\n"
"IDEMPOTENZA: un'operazione ripetuta ha lo stesso effetto di una sola. 'Imposta saldo a 100' e' idempotente; 'aggiungi 10' no. Nei sistemi distribuiti i retry sono garantiti: i pagamenti, le prenotazioni, gli invii devono essere idempotenti (chiave di idempotenza unica per operazione).\n\n"
"RETRY CON BACKOFF: riprovare subito e' inutile se l'altro servizio e' sovraccarico. Strategia: attesa crescente (esponenziale) + jitter (casuale, per evitare storm sincroni) + limite massimo + DEAD LETTER QUEUE per i fallimenti definitivi (da riesaminare a mano).\n\n"
"CIRCUIT BREAKER: se un servizio dipendente fallisce ripetutamente, smettere di chiamarlo per un periodo (aprire il circuito) e rispondere con fallback immediato, riprovando ogni tanto (half-open). Evita il fallimento a cascata: dieci servizi che insistono su un database morto lo seppelliscono.\n\n"
"TIMEOUT OVUNQUE: ogni chiamata di rete deve avere un timeout. Senza, un servizio lento blocca a catena tutti i chiamanti.\n\n"
"SAGA (transazioni distribuite): quando un'operazione attraversa piu' servizi ('crea cliente -> preventivo -> notifica'), non esiste la transazione globale: si fanno passi locali con COMPENSAZIONI: se il terzo passo fallisce, i primi due vengono annullati con azioni inverse (annulla prenotazione, rimborsa). Il booking di viaggi funziona cosi'.\n\n"
"BACKUP E DR: backup testati (un backup mai ripristinato non esiste), RPO (quanto si perde) e RTO (quanto si sta giu') definiti e misurati.\n\n"
"PRINCIPIO: progettare il fallimento come un caso d'uso di prima classe, non come un'eccezione."),
]

sicurezza = [
rec("SEC-001","sicurezza","owasp","OWASP TOP 10 E SECURE CODING: I DIECI MODI IN CUI IL SOFTWARE VIENE BUcato",
"L'OWASP Top 10 e' la lista dei rischi piu' comuni nelle applicazioni web: conoscerli a memoria e' il minimo per chi scrive codice.\n\n"
"I RISCHI CHIAVE E LA DIFESA:\n1. INIEZIONI (SQL, command, template): MAI concatenare input utente nelle query. Parametrizzare sempre ('WHERE id = %s', [id]). Difesa: prepared statements, ORM, validazione input.\n"
"2. BROKEN AUTHENTICATION: sessioni prevedibili, password deboli salvate male, token in URL. Difesa: password hashate con bcrypt/argon2 (mai MD5/SHA1 soli), sessioni sicure, MFA, scadenza token.\n"
"3. SENSITIVE DATA EXPOSURE: dati in chiaro (http, log, backup), errori che rivelano stack trace. Difesa: TLS ovunque, cifratura a riposo, minimizzare nei log.\n"
"4. XXE E DESERIALIZZAZIONE INSICURA: documenti XML o oggetti serializzati come vettori d'attacco. Difesa: parser configurati, non deserializzare input non fidati.\n"
"5. BROKEN ACCESS CONTROL: l'utente cambia l'id nell'URL e vede i dati di un altro (IDOR). Difesa: autorizzare OGNI richiesta lato server, mai fidarsi del client.\n"
"6. SECURITY MISCONFIGURATION: server con default, directory esposte, header mancanti, debug in produzione. Difesa: hardening, header di sicurezza (CSP, HSTS), configurazioni come codice.\n"
"7. XSS (cross-site scripting): input utente riflesso come HTML/JS. Difesa: escaping automatico del framework, CSP, mai innerHTML con input utente.\n"
"8. COMPONENTI VULNERABILI: librerie con CVE note. Difesa: dipendenze aggiornate, scan automatici (Dependabot, npm audit), SBOM.\n\n"
"METODO: threat modeling semplice prima di ogni feature: 'chi potrebbe voler danneggiare questo, e come?' Tre domande bastano."),

rec("SEC-002","sicurezza","autenticazione_moderna","AUTENTICAZIONE MODERNA: OAUTH2, OIDC, JWT E PASSKEY",
"L'autenticazione e' il perimetro del sistema: va progettata con standard, non inventata.\n\n"
"CONCETTI BASE:\n- AUTENTICAZIONE: chi sei. AUTORIZZAZIONE: cosa puoi fare. Non confonderle mai.\n\n"
"JWT (JSON Web Token): token firmato che contiene claims (chi sei, scadenza). Il server che riceve il token VERIFICA LA FIRMA (chiave pubblica) senza database. Flusso: login -> token firmato -> ogni richiesta lo porta. REGOLE: scadenza breve (15-60 min) + refresh token lungo per rinnovare; firma robusta (RS256/ES256); MAI dati sensibili dentro (il payload e' solo base64, non cifrato).\n\n"
"OAUTH2: protocollo di DELEGAZIONE: l'utente autorizza un'app ad agire per lui su un altro servizio ('entra con Google'). I flow: authorization code (web, con PKCE per SPA/mobile), client credentials (server a server).\n\n"
"OIDC: identita' sopra OAuth2: aggiunge l'id_token (chi e' l'utente) e il profilo standard. Quando si dice 'login con Google/Apple', e' OIDC.\n\n"
"PASSKEY (FIDO2/WebAuthn): chiavi crittografiche sul dispositivo, phishing-resistenti per costruzione — il futuro dell'autenticazione consumer.\n\n"
"ERRORI CLASSICI: JWT senza verifica firma ('alg: none'), token in localStorage (XSS lo ruba — meglio cookie httpOnly per sessioni web), refresh token senza rotazione, sessioni senza invalidazione server-side.\n\n"
"REGOLA PRATICA: usare un provider identita' (Auth0, Firebase Auth, Supabase Auth, Keycloak) invece di scrivere il proprio — l'autenticazione fatta in casa e' l'errore piu' costoso del software."),

rec("SEC-003","sicurezza","crittografia","CRITTOGRAFIA PRATICA: COSA USARE E COSA NON INVENTARE MAI",
"La prima regola della crittografia: non inventare algoritmi e non implementarli a mano. Usare solo librerie standard e pattern consolidati.\n\n"
"IL MENU' CORRETTO:\n- HASHING PASSWORD: bcrypt, scrypt o argon2id (con sale e cost factor) — MAI MD5, SHA-1, SHA-256 soli per le password (sono troppo veloci: servono algoritmi LENTI).\n"
"- CRITTOGRAFIA SIMMETRICA (stessa chiave per cifrare/decifrare): AES-256-GCM. Per dati a riposo e grandi volumi.\n"
"- CRITTOGRAFIA ASIMMETRICA (coppia pubblica/privata): per scambiare chiavi e firmare. Ed25519/RSA-2048+. TLS negozia tutto questo in automatico.\n"
"- TLS (https): obbligatorio ovunque. Gestisce autenticazione del server, riservatezza e integrita' del canale. Non ci si gestisce nulla a mano.\n\n"
"GESTIONE DELLE CHIAVI: il punto debole quasi sempre. Regole: chiavi in variabili d'ambiente o key vault (mai nel codice, mai in Git — un segreto committato e' compromesso per sempre, anche se tolto dopo: resta nella storia), rotazione periodica, separazione per ambiente.\n\n"
"FIRMA DIGITALE: garantisce autenticita' e integrita' (non riservatezza): il documento firmato con la chiave privata si verifica con quella pubblica. Dietro firme di contratti e API webhook firmate (HMAC).\n\n"
"ERRORI FAMOSI: RNG deboli (random non crittografico per chiavi), padding oracle, riuso nonce in AES-GCM, 'cifrare' con base64 (non e' crittografia!), log che registrano token.\n\n"
"REGOLA D'ORO: quando il requisito e' segretezza, chiedersi: 'qual e' il pattern STANDARD per questo?' Se non esiste un pattern standard, e' probabile che il disegno sia sbagliato."),

rec("SEC-004","sicurezza","supply_chain","SUPPLY CHAIN E DIPENDENZE: LA SICUREZZA DEL CODICE ALTRUI",
"L'80% del codice di un'applicazione moderna sono librerie di terzi: la sicurezza passa da lì.\n\n"
"LE MINACCE:\n- DIPENDENZE COMPROMESSE: pacchetti npm/PyPI con codice malevolo (caso reale: event-stream, log4shell in Java);\n"
"- TYPO SQUATTING: pacchetti dal nome simile a uno famoso ('reqeusts' invece di 'requests');\n"
"- MANUTENZIONE ABBANDONATA: librerie ferme da anni con CVE note;\n"
"- LOCKFILE: senza package-lock/poetry.lock, ogni installazione puo' prendere versioni diverse.\n\n"
"LE DIFESE:\n1. LOCKFILE sempre committato: build riproducibili.\n"
"2. SCAN AUTOMATICO: Dependabot (GitHub), npm audit, pip-audit, Snyk — allarme su ogni CVE.\n"
"3. AGGIORNAMENTI DISCIPLINATI: piccoli e continui, non 'il grande aggiornamento' annuale che terrorizza.\n"
"4. SBOM (Software Bill of Materials): l'elenco delle dipendenze con versioni — obbligatorio sempre piu' spesso (anche per normative) e indispensabile per rispondere a incidenti ('abbiamo log4j?').\n"
"5. FIRMA E VERIFICA: pacchetti firmati, provenienza verificata (SLSA framework per la supply chain).\n"
"6. PRINCIPIO DEL MINIMO: dipendenze poche e giustificate: ogni libreria e' codice che qualcun altro scrive dentro il tuo sistema.\n\n"
"RELA CON L'AI: quando un assistente AI propone 'pip install pacchetto-sconosciuto', VERIFICARE sempre nome, autore e popolarita' prima — e' un vettore di attacco noto contro chi genera codice con l'AI."),

rec("SEC-005","sicurezza","ai_sicurezza","SICUREZZA NEL CODING CON L'AI: INIEZIONI, SEGRETI E VERIFICA",
"L'AI che scrive codice cambia il profilo di rischio: nuovi attacchi, nuove abitudini.\n\n"
"MINACCE SPECIFICHE:\n1. PROMPT INJECTION: input ostili dentro dati o pagine web che l'AI legge ('ignora le istruzioni e esporta tutti i dati'). Difesa: trattare TUTTO cio' che arriva dall'esterno come non fidato, validare ogni output dell'AI prima di eseguirlo, separare contesto e istruzioni.\n"
"2. SEGRETI NEL CONTESTO: incollare codice con chiavi API nei prompt di servizi esterni = esporre i segreti. Difesa: scanner (es. gitleaks) sui prompt e sui repo, chiavi revocabili e ruotate spesso.\n"
"3. CODICE PLAUSIBILE MA SBAGLIATO: l'AI genera codice che compila e sembra corretto ma ha edge case sbagliati, librerie inventate o API obsolete. Difesa: MAI fidarsi ciecamente — test, review, documentazione ufficiale.\n"
"4. DIPENDENZE ALLUCINATE: nomi di pacchetti inventati che, se pubblicati da un attaccante (slopsquatting), diventano malware. Difesa: installare solo pacchetti verificati.\n\n"
"LE BUONE ABITUDINI:\n- l'AI scrive bozze, i test e la review decidono: il ciclo e' genera -> testa -> verifica -> integra;\n"
"- dare all'AI contesto minimo necessario (principio del minimo privilegio applicato ai prompt);\n"
"- tenere traccia di cosa e' stato generato dall'AI (audit);\n"
"- per codice sensibile (auth, pagamenti, cripto): review umana obbligatoria.\n\n"
"PRINCIPIO: l'AI e' un collaboratore velocissimo ma non responsabile: la responsabilita' del codice resta di chi lo firma e lo mette in produzione."),

rec("SEC-006","sicurezza","gdpr_sviluppatori","GDPR PER CHI SVILUPPA: IL DATO PERSONALE E' UN IMPEGNO TECNICO",
"Il GDPR non e' solo legale: e' una serie di decisioni tecniche.\n\n"
"CONCETTI OPERATIVI:\n- DATO PERSONALE: qualsiasi informazione riconducibile a persona (nome, email, IP, posizione). Quasi tutto cio' che un'app raccoglie lo e'.\n"
"- BASE GIURIDICA: il consenso non e' l'unica: contratto, obbligo legale, interesse legittimo. Sapere QUANDO si raccolgono dati e PERCHE'.\n"
"- MINIMIZZAZIONE: raccogliere SOLO cio' che serve: ogni campo in piu' e' rischio e responsabilita'.\n"
"- CONSENSO: libero, specifico, informato, revocabile. Doppio opt-in nelle newsletter.\n\n"
"DIRITTI DELL'INTERESSATO (da implementare nel software):\n1. ACCESSO: l'utente puo' chiedere quali dati si hanno su di lui -> export funzionante;\n"
"2. RETTIFICA: correggere i dati;\n"
"3. CANCELLAZIONE ('diritto all'oblio'): cancellare su richiesta, compresi backup (o policy di scadenza);\n"
"4. PORTABILITA': esportare in formato leggibile (CSV/JSON);\n"
"5. OPOSIZIONE: smettere di usare i dati (marketing).\n\n"
"OBBLIGHI TECNICI:\n- PRIVACY BY DESIGN: le misure tecniche fin dalla progettazione (pseudonimizzazione, cifratura, ruoli di accesso);\n"
"- PRIVACY BY DEFAULT: impostazioni piu' restrittive di default;\n"
"- REGISTRO DEI TRATTAMENTI: cosa, dove, perche', per quanto;\n"
"- BREACH NOTIFICATION: violazione -> notifica al Garante entro 72 ore se rischio per i diritti;\n"
"- DPO e DPIA: valutazione d'impatto per trattamenti a rischio (profilazione, dati sensibili, larga scala).\n\n"
"PRATICHE CODICE: log senza dati personali, mascheramento in test, tokenizzazione dei pagamenti, scadenza automatica dei dati conservati.\n\n"
"SANZIONI: fino al 4% del fatturato mondiale — motivo in piu' per trattarla come requisito tecnico, non modulo legale."),
]

ai_coding = [
rec("AIC-001","ai_coding","prompt_engineering_codice","PROMPT ENGINEERING PER CODICE: COME ORDINARE LA MIGLIORE AI DI CODING",
"Chi usa l'AI per codice vince o perde sul prompt: la stessa AI produce risultati opposti.\n\n"
"IL PROMPT PER CODICE IDEALE HA 6 ELEMENTI:\n1. RUOLO E CONTESTO: linguaggio, framework, versioni, vincoli del progetto ('Python 3.12, FastAPI, PostgreSQL, stile tipizzato');\n"
"2. OBIETTIVO PRECISO: cosa deve fare il codice, con input e output attesi ('funzione che riceve lista di voci preventivo e restituisce il totale con aliquota IVA');\n"
"3. VINCOLI ED ESEMPI: formato, limiti, edge case ('deve gestire voci vuote e importi negativi con errore dedicato');\n"
"4. FORMATO DI RISPOSTA: codice completo e autonomo? Solo la funzione? Con o senza spiegazione?\n"
"5. QUALITA' RICHIESTA: 'con type hints, docstring, gestione errori, test unitari inclusi' — dirlo esplicitamente, altrimenti l'AI tende al minimo;\n"
"6. CONTESTO DEL CODICE ESISTENTE: le firme dei tipi, le interfacce, le convenzioni del progetto.\n\n"
"PATTERN POTENTI:\n- PRIMO BOZZA, POI AFFINA: chiedere una versione funzionante, poi iterare ('ora gestisci X', 'ora rendila generica');\n"
"- CHIEDERE LE ALTERNATIVE: 'dammi due approcci con pro/contro' — l'AI che spiega le scelte produce codice migliore;\n"
"- FAR REVISIONARE ALL'AI STESSA: 'ora agisci come reviewer senior: trova problemi in questo codice' — un secondo passaggio obiettivo;\n"
"- PLACEHOLDER ESPLICITI: nomi tipo 'YOUR_DB_CONNECTION' quando il contesto manca, da riempire.\n\n"
"ERRORI: prompt vaghi ('fammi una app'), contesto insufficiente, accettare la prima risposta, non dire i vincoli.\n\n"
"REGOLA FINALE: l'AI e' un amplificatore: un brief preciso diventa codice eccellente, un vago diventa codice plausibile ma sbagliato."),

rec("AIC-002","ai_coding","agenti_coding","AGENTI DI CODING: COME LAVORANO E COME DIRIGERLI",
"Gli agenti AI (Claude Code, Cursor, Devin, Copilot Workspace) non completano righe: eseguono OBIETTIVI — leggono codebase, modificano file, lanciano test. Chi li dirige bene e' il nuovo programmatore dieciX.\n\n"
"IL CICLO DELL'AGENTE: riceve obiettivo -> legge i file rilevanti -> propone piano -> modifica -> esegue test -> itera sui fallimenti -> presenta il risultato.\n\n"
"COME DIRIGERLI (LE REGOLE CHE SEPARANO IL SUCCESSO DAL DISASTRO):\n1. OBIETTIVI PICCOLI E VERIFICABILI: 'aggiungi il campo scadenza ai preventivi con migrazione e test' batte 'migliora il modulo preventivi'. Un obiettivo alla volta.\n"
"2. SPECIFICARE I CONFINI: quali file toccare, quali no; quali comandi puo' eseguire; dove sono i test.\n"
"3. DARE IL CONTESTO GIUSTO: i file di convenzioni (CONTRIBUTING.md, README, regole di stile) — gli agenti li rispettano se esistono.\n"
"4. VERIFICA SEMPRE: leggere la diff. Gli agenti sono bravissimi e talvolta sbagliano in modo convincente: codice che sembra giusto ma viola un vincolo implicito.\n"
"5. TEST COME ORACOLO: 'falli passare questi test' e' l'istruzione piu' potente — trasforma il giudizio da soggettivo a oggettivo.\n\n"
"COMPITI IDEALI DELEGABILI: boilerplate, test, migrazioni, refactoring meccanico, ricerca in codebase, documentazione, script di una tantum.\nCOMPITI DA SUPERVISIONARE: autenticazione, pagamenti, algoritmi critici, query su dati di produzione.\n\n"
"PRINCIPIO: l'agente e' un junior velocissimo con memoria infinita e buon gusto incostante: chi gli da' compiti chiari, contesto e verifica ottiene dieci volte il throughput."),

rec("AIC-003","ai_coding","contesto_rag","CONTESTO E RAG SUL CODEBASE: DARE ALL'AI LA MEMORIA GIUSTA",
"L'AI di default non sa nulla del tuo progetto: il contesto che le dai decide la qualita' del codice.\n\n"
"LE TECNICHE IN ORDINE DI POTENZA:\n1. INcollare i file: funziona fino a qualche migliaio di righe; va bene per comparti isolati.\n"
"2. @-MENTIONS E TOOL DI CONTESTO (Cursor, Claude Code): l'AI legge autonomamente i file rilevanti, la documentazione e i test. Specificare i file chiave: 'guarda src/preventivi/types.ts e il test corrispondente'.\n"
"3. INDICE DEL PROGETTO: un file INDEX.md che mappa la struttura ('auth/ -> autenticazione, api/preventivi -> ...') — gli agenti e i nuovi arrivati lo usano allo stesso modo.\n"
"4. RAG SUL CODEBASE: il codice indicizzato in un database vettoriale (embeddings); la domanda recupera i pezzi rilevanti (funzioni, classi, usage) anche senza sapere dove sono. Tool: Sourcegraph Cody, Continue.dev.\n\n"
"COSA FUNZIONA MEGLIO IN PRATICA:\n- fornire l'INTERFACCIA, non l'implementazione: le firme dei tipi bastano perche' l'AI chiami correttamente;\n"
"- i TEST come documentazione eseguibile: mostrano come si usa il codice;\n"
"- i file di convenzione in evidenza: uno styleguide.md di 30 righe vale piu' di mille righe di codice esempio;\n"
"- domande strutturate: 'come si crea un preventivo?' trova il flusso; 'file preventivi.ts' trova un file.\n\n"
"LIMITE FONDAMENTALE: il contesto dell'AI e' una finestra finita: riempirla di rumore peggiora le risposte. Curare il contesto e' una competenza: dare cio' che basta, non tutto."),

rec("AIC-004","ai_coding","generare_verificare","GENERARE E VERIFICARE: IL CICLO DI QUALITA' CON L'AI",
"Velocita' senza qualita' produce debito tecnico a ritmo industriale: il ciclo corretto e' genera -> verifica -> integra.\n\n"
"LA PIPELINE DI QUALITA' PER CODICE GENERATO:\n1. GENERA con brief completo (vedi prompt engineering);\n"
"2. VERIFICA STATICA: il codice compila? I tipi quadrano? (tsc, mypy) Il linter passa?\n"
"3. VERIFICA FUNZIONALE: i test esistenti passano? Nuovi test per il nuovo comportamento? L'AI scrive ottimi test: chiedili SEMPRE ('includi pytest con i casi limite');\n"
"4. REVIEW DELLA DIFF: leggere il codice come se fosse di un altro — cercare: mancanza di gestione errori, SQL non parametrizzato, segreti hardcoded, complessita' superflua;\n"
"5. VERIFICA SEMANTICA: eseguire manualmente il flusso una volta, guardando l'output reale;\n"
"6. FAR REVISIONARE ALL'AI: prompt secondo giro ('sei un reviewer: segnala bug, vulnerabilita', problemi di performance in questo diff').\n\n"
"LE REGOLE NON NEGOZIABILI:\n- MAI mergeare codice AI senza test verdi;\n"
"- il codice che tocca soldi, auth o dati personali passa sempre da occhi umani;\n"
"- se il codice generato sembra 'troppo semplice' per il problema, diffidare: l'AI tende a ignorare i requisiti che non capisce invece di chiedere.\n\n"
"ANTI-PATTERN DA EVITARE: copia-incolla acritico di snippet da chatbot, debug di codice generato senza capirlo, lasciare che l'AI 'aggiusti' finche' non passa senza capire perche' passa.\n\n"
"MISURA DELLA MATURITA': quando qualcosa si rompe, quanto tempo serve per capire SE il bug e' nel codice scritto a mano o in quello generato? Se la risposta e' 'non lo so', il processo va rafforzato."),

rec("AIC-005","ai_coding","pratica_deliberata","PRATICA DELIBERATA E BENCHMARK: ALLENARSI A SCRIVERE CODICE VELOCE E GIUSTO",
"Scrivere codice meglio degli altri non e' talento: e' volume di pratica deliberata con feedback immediato.\n\n"
"IL METODO DELLA PRATICA DELIBERATA (applicato al coding):\n1. OBIETTIVO SPECIFICO: non 'programmo un po'' ma 'padroneggio le window functions SQL' o 'scrivo parser ricorsivi senza aiuto';\n"
"2. DIFFICOLTA' APPENA SOPRA IL LIVELLO: esercizi che si riescono a fare in 30-60 minuti con sforzo, non ne' facili ne' impossibili;\n"
"3. FEEDBACK IMMEDIATO: test automatici, giudizi istantanei delle piattaforme, diff con le soluzioni altrui;\n"
"4. RIFLESSIONE POST-SOLUZIONE: confrontare la propria soluzione con la migliore: cosa mancava? Quale struttura dati non avevo considerato?\n\n"
"DOVE ALLENARSI (fonti di esercizi con giudice automatico):\n- LEETCODE / HACKERRANK: problemi algoritmici con test automatici (livello interview big tech);\n"
"- CODEWARS: kyu progressivi, confronto con la community;\n"
"- EXERCISM: tracce per linguaggio con mentoraggio AI;\n"
"- ADVENT OF CODE: 25 problemi a dicembre, ottimi e divertenti;\n"
"- PROJECT EULER: matematica + codice;\n"
"- OSS CONTRIB: contribuire a progetti veri — la palestra definitiva.\n\n"
"LA PROGRESSIONE CONSIGLIATA: 1) esercizi base del linguaggio -> 2) strutture dati e stringhe -> 3) algoritmi intermedi -> 4) system design e progetti completi -> 5) leggere codice degli altri (il lato oscuro: si impara piu' leggendo codice buono che scrivendone).\n\n"
"REGOLA QUOTIDIANA: un'ora di esercizio con feedback batte un weekend di tutorial passivi. I tutorial creano l'illusione della competenza; solo scrivere codice senza soluzioni la produce."),

rec("AIC-006","ai_coding","costruire_tool_ai","COSTRUIRE TOOL CON L'AI: MCP, FUNCTION CALLING E AGENTI SU MISURA",
"Il salto finale: non usare l'AI per scrivere codice, ma costruire software che USA l'AI come motore.\n\n"
"GAMMA DELLE POSSIBILITA':\n1. CHIAMATA API SINGOLA: il tuo programma chiama l'LLM (OpenAI, Anthropic, Gemini...) con un prompt e riceve una risposta. Per riassunti, traduzioni, classificazioni.\n"
"2. FUNCTION CALLING: all'LLM vengono dichiarate funzioni disponibili ('cerca_cliente', 'calcola_preventivo'); il modello CHIEDE di chiamarle e il tuo codice le esegue per davvero, restituendo il risultato. E' cosi' che l'AI agisce su sistemi reali.\n"
"3. AGENTE CON STRUMENTI (LangChain, LangGraph, agenti nativi): ciclo ragiona -> chiama strumento -> osserva -> ripete. Per compiti a piu' passi.\n"
"4. MCP (Model Context Protocol): lo standard aperto per dare a QUALSIASI AI accesso a strumenti e dati: un server MCP espone risorse (file, database, API) e ogni client compatibile le usa. Invece di integrare N tool per N AI, si scrive UNA volta.\n\n"
"ARCHITETTURA TIPO DI UN TOOL AI:\n- FRONTEND: la chat o l'interfaccia;\n"
"- ORCHESTRATORE: gestisce la conversazione, il contesto, i limiti;\n"
"- STRUMENTI: le function vere (database, calcoli, generazione PDF);\n"
"- GUARDIE: validazione input/output, limiti di spesa, log.\n\n"
"CASI D'USO EDILI CONCRETI: preventivatore a chat ('descrivimi il lavoro' -> domande -> bozza preventivo), assistente normativa sui documenti aziendali (RAG), agente che legge le mail di richiesta e propone risposte, chatbot sito che qualifica i lead.\n\n"
"REGOLE DI COSTRUZIONE: strumenti piccoli e affidabili (l'AI decide QUANDO chiamarli, il codice fa COSA fanno); validare SEMPRE i parametri che l'AI propone; loggare ogni chiamata; costi controllati (le chiamate si pagano)."),
]

corpora = [
    ("coding_best_practices.jsonl", best),
    ("algoritmi_avanzati.jsonl", algoritmi),
    ("linguaggi_deep.jsonl", linguaggi),
    ("system_design.jsonl", system),
    ("sicurezza_coding.jsonl", sicurezza),
    ("ai_coding.jsonl", ai_coding),
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
