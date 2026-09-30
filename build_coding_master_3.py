# -*- coding: utf-8 -*-
"""Coding_Master_Pack_3: terzo livello — 30 schede su aree mai coperte."""
import json, os

BASE = r"C:\Users\alessandro\Documents\kimi\tasks\2026-09-26\15-14-07-e3d653af\Coding_Master_Pack_3\parsed"
os.makedirs(BASE, exist_ok=True)

LIC = "Sintesi didattica originale Kimi (pubblico dominio)"
ATT = "Corpus coding master 3 a cura di Kimi"

def rec(id_, cat, tema, title, text):
    return {"id": id_, "categoria": cat, "tema": tema, "title": title, "text": text,
            "source": f"coding_master_3_{cat}_kimi", "license": LIC, "commercial_ok": True,
            "attribution": ATT, "url": ""}

interview = [
rec("INT-001","interview","sliding_window","PATTERN ALGORITMICI 1: SLIDING WINDOW E TWO POINTERS",
"""Due pattern che risolvono decine di problemi da colloquio e, soprattutto, problemi reali di dati in sequenza.

SLIDING WINDOW (finestra scorrevole):
Idea: quando serve 'il migliore tra tutte le SOTTOSEQUENZE CONTIGUE di lunghezza k' (o variabile), non serve rigenerare il calcolo da zero a ogni posizione: si fa scorrere una finestra, si toglie l'elemento che esce e si aggiunge quello che entra. O(n) invece di O(n*k).
Riconoscimento: 'sottosequenza contigua', 'massimo/minimo di lunghezza k', 'somma di k elementi consecutivi'.
Caso base: somma massima di k elementi consecutivi. Variante: finestra variabile (allargare/restringere a due indici) per 'la piu' lunga sottosequenza con al massimo X elementi duplicati'.
Analogia edile: misurare il consumo di materiali ogni settimana mobile invece di ricalcolare da inizio cantiere ogni giorno.

TWO POINTERS (due puntatori):
Idea: due indici che scorrono la struttura in modo coordinato, evitando il doppio ciclo.
- Oposti: array ordinato, trovare la coppia che somma a X — uno da sinistra, uno da destra: O(n) invece di O(n^2).
- Stesso verso (fast/slow): trovare cicli in una lista concatenata (il coniglio e la tartaruga), trovare il punto medio, rilevare duplicati.
- Partizione (Lomuto/Hoare): la base di quicksort e la separazione 'stabile prima/instabile dopo'.

COME IMPARARLI: per ogni pattern, 5 problemi in ordine di difficolta' crescente; dopo i primi tre il pattern diventa riconoscibile a colpo d'occhio — ed e' il riconoscimento, non la scrittura, la competenza."""),

rec("INT-002","interview","intervalli_matrici","PATTERN ALGORITMICI 2: INTERVALLI, MATRICI E RICERCA SPECIALIZZATA",
"""Seconda famiglia di pattern: le strutture che sembrano semplici ma nascondono la trappola.

INTERVALLI:
I problemi su intervalli (riunioni sovrapposte, inserimento, minimizzazione di risorse) si risolvono ordinando e scorrendo:
- ORDINA per inizio (o fine, a seconda del problema): quasi sempre il primo passo.
- FONDI sovrapposti tenendo traccia del corrente: 'se il prossimo inizia prima che finisca il corrente -> fondi, altrimenti chiudi'.
Casi: numero minimo di aule per tutte le lezioni (greedy per fine piu' presto), somma di intervalli liberi, trovare buchi.
Analogia edile: il planning delle squadre tra cantieri e' un problema di intervalli — chi e' libero quando.

MATRICI:
- RICERCA IN MATRICE ORDINATA (righe e colonne crescenti): partire dall'angolo alto-destra: troppo grande -> sinistra; troppo piccolo -> giu'. O(m+n).
- TRAVERSATA A SPIRALE, ROTAZIONE IN PLACE, regioni connesse (flood fill con BFS/DFS — gia' nel corpus grafi: qui l'applicazione su griglia).
- PATHFINDING SU GRIGLIA: BFS per cammini minimi su griglia non pesata; A* con euristica (distanza di Manhattan) quando c'e' una destinazione — dietro i navigatori e le logiche di posa ottimale.

RICERCA SPECIALIZZATA:
- RICERCA BINARIA CON RISPOSTA: quando la soluzione e' un numero intero/reale e la funzione 'e' fattibile(x)' e' monotona ('minimo tempo sufficiente', 'massimo carico trasportabile').
- RICERCA SU RISPOSTA ROTATA: il classico 'array ruotato ordinato' — un'occhiata al mid dice quale meta' e' ordinata."""),

rec("INT-003","interview","backtracking","PATTERN ALGORITMICI 3: BACKTRACKING E COMBINATORICA",
"""Il backtracking e' il pattern dei problemi 'prova tutte le combinazioni ma con intelligenza': permutazioni, sottoinsiemi, sudoku, N-regine, partizioni.

IL MODELLO MENTALE: l'albero delle decisioni. A ogni livello si prende una decisione (inserire X / non inserirlo; mettere il numero k nella casella), si scende ricorsivamente, e se il ramo non puo' portare a soluzione si risale (prune).
Il template e' sempre lo stesso:
1. STATO: cosa ho deciso finora.
2. SCELTE: quali mosse sono legali ora.
3. PRUNING: scartare rami impossibili PRIMA di esplorarli (il 90% dell'efficienza sta qui).
4. CASO BASE: soluzione completa -> registrarla.

I CLASSICI:
- SOTTOINSIEMI (power set): per ogni elemento, prendi/non prendi: 2^n soluzioni.
- PERMUTAZIONI: scegli l'elemento da posizione i tra i rimanenti, marca usato, ricorri, smarca.
- COMBINAZIONI: permutazioni + vincolo di ordine non-decrescente per non duplicare.
- SUDOKU / N-REGINE: il pruning (vincoli di riga/colonna/diagonale) rende fattibile cio' che sarebbe 10^30 combinazioni.

COMPLESSITA': esponenziale per natura (i problemi combinatorici hanno soluzioni esponenziali): si misura il miglioramento del pruning come 'fattore di potatura'.
Analogia edile: la quantificazione delle varianti di preventivo (quali voci includere rispettando budget e vincoli) e' backtracking — e la programmazione a vincoli (constraint programming) e' il suo parente industriale, usata nei software di ottimizzazione di taglio e posa.

QUANDO NON USARLO: se una soluzione greedy o PD funziona, il backtracking e' spreco. Lo si usa quando il problema CHIEDE di esplorare lo spazio delle soluzioni."""),

rec("INT-004","interview","colloquio_tecnico","IL COLLOQUIO TECNICO: COME SI AFFRONTA E COME SI VALUTA",
"""Il colloquio tecnico misura come si ragiona sotto vincolo, non la conoscenza enciclopedica: si affronta con metodo.

IL METODO DURANTE IL PROBLEMA (parlare mentre si ragiona — il silenzio e' il peggior errore):
1. RIPETERE e chiedere: vincoli, dimensioni dei dati, esempi. 'Puo' essere vuoto? Ci sono duplicati? Quanto grande?' — tre domande che evitano meta' delle trappole.
2. SOLUZIONE NAIVE PRIMA: dire la soluzione forza-bruta ad alta voce ('potrei controllare tutte le coppie in O(n^2)...') dimostra comprensione e crea la base per l'ottimizzazione.
3. OTTIMIZZARE INSIEME: 'dove si perde tempo? ho bisogno di ricordare qualcosa? -> struttura dati' — la conversazione deve guidare verso la soluzione.
4. CODARE pulito, testare a voce su 2-3 esempi inclusi i limite.
5. ANALISI COMPLESSITA' alla fine: tempo e spazio, sempre.

COME CI SI VALUTA (l'altra faccia — utile anche a chi assume):
- segnali forti: domande prima di codare, discussione di alternative, test dei casi limite, codice leggibile a occhio;
- segnali deboli: saltare alla codice, ignorare i vincoli, 'funziona con questo esempio' come unica verifica, codice criptico;
- il falso positivo da evitare: chi ha imparato a memoria 300 problemi — cambiando un vincolo ('ora con k duplicati ammessi') si vede se ragiona o recita.

PREPARAZIONE REALISTICA: 6-8 settimane, 1-2 problemi al giorno con approfondimento (non raffica di 50), pattern prima dei singoli problemi (il corpus pattern di questo pack), simulazioni a voce alta. La velocita' arriva dalla riconoscibilita', non dalla scrittura veloce."""),

rec("INT-005","interview","system_interview","IL SYSTEM DESIGN INTERVIEW: ARCHITETTURA SOTTO PRESSIONE",
"""Il colloquio di system design (una scatola di requisiti aperti: 'progetta X') misura il giudizio architetturale, non la memoria. Struttura del corpus system design applicata in 45 minuti.

LE FASI GESTITE CON I NUMERI IN MANO:
1. 5 MIN — AMBITO: funzionalita' core vs fuori scope; utenti, QPS, dati/giorno, crescita. '1 milione di utenti attivi, 1000 richieste/sec di picco, 10 GB nuovi al giorno' — scritti, visibili.
2. 10 MIN — MODELLO DATI E API: entita' principali e le operazioni; la struttura guida tutto il resto.
3. 20 MIN — ARCHITETTURA: disegnare client -> load balancer -> app stateless -> cache -> database + code per i lavori asincroni; motivare OGNI freccia con un numero ('cache: 200 letture/1 scrittura').
4. 10 MIN — BOTTLENECK: 'a 10x cosa muore prima?' (sempre: database, poi la parte sincrona lenta). Soluzioni nominate con trade-off.
5. DIMOSTRARE MATURITA': menzionare osservabilita', deploy, failure mode ('se questo servizio muore...').

ERRORI CHE COSTANO IL COLOQUIO:
- saltare i numeri e disegnare scatole di moda (Kafka, Kubernetes) senza motivazione misurabile;\n- progettare per scala che non esiste ('sharding' per 1000 utenti);\n- monologo senza coinvolgere l'intervistatore — e' una conversazione, non un esame;\n- dimenticare i dati: architettura bellissima su un modello dati sbagliato.\n
LA VERITA' SUL VALORE: questi colloqui premiano chi ha COSTRUITO cose reali — chi ha visto un sistema cadere per un lock del database riconosce subito la risposta giusta. Anche qui: progetti verdi battono esercizi."""),
]

geometria = [
rec("GEO-001","geometria_computazionale","geometria_2d3d","GEOMETRIA COMPUTAZIONALE 2D/3D: IL CODICE CHE TOCCA IL FISICO",
"""La geometria computazionale e' il ponte tra software e mondo fisico: CAD, BIM, GIS, robotica, grafica.

LE FONDAMENTA 2D:
- RAPPRESENTAZIONE: punti, vettori, segmenti, polilinee, poligoni. Le operazioni base: distanza punto-retta, proiezione, prodotto scalare (angolo e proiezione) e vettoriale (area orientata, lato di un punto rispetto a una retta).
- ORIENTAMENTO: il cross product 2D dice se tre punti girano a sinistra o a destra: e' la base di: punto dentro poligono, intersezione segmenti, convessita'.
- POLIGONI: area (shoelace formula), punto interno (ray casting: conta quante volte un raggio dal punto attraversa i bordi), semplificazione Douglas-Peucker per le polilinee.

LE FONDAMENTA 3D:
- VETTORI E MATRICI: trasformazioni come matrici 4x4 (rotazione, traslazione, scala, proiezione) — una catena di trasformazioni si compone moltiplicando matrici.
- PIANI E NORMALI: equazione del piano, distanza punto-piano, normale come direzione perpendicolare (usata per l'illuminazione e le operazioni booleane).
- SISTEMI DI COORDINATE: locale -> mondo -> camera -> schermo: ogni salto e' una matrice.

ROBUSTEZZA NUMERICA: i floating point accumulano errore: test di quasi-uguaglianza con epsilon, e predicati geometrici robusti (predicati esatti) nei kernel CAD seri — un errore di 10^-15 su un test di intersezione crea poligoni sbagliati.

PERCHE' IMPORTA QUI: la tua CAD Library e' fatta di questi formati: chi li genera o li legge ragiona in questi termini."""),

rec("GEO-002","geometria_computazionale","mesh_brep","MESH, B-REP E RAPPRESENTAZIONE DELLE FORME",
"""Un solido 3D puo' essere descritto in due mondi: le mesh (approssimazione) e la B-Rep (geometria esatta). I formati CAD vivono in questa distinzione.

MESH (rappresentazione poligonale):
- VERTICI + FACCE: un solido come insieme di triangoli/quadrangoli. Formato OBJ, STL, PLY, 3DS (tuo corpus CAD!).
- STRUTTURE DATI: vertex buffer + index buffer; half-edge per attraversare i vicini di efficientemente (le operazioni locali: smussatura, suddivisione).
- QUALITA': mesh orientate consistentemente, normali per vertice (smooth shading), manifold-ness (nessun bordo spaiato) — le mesh non-manifold rompono le operazioni di stampa 3D e simulazione.
- OPERAZIONI: decimazione (meno triangoli, stessa forma), suddivisione (Catmull-Clark: superfici lisce dai pochi poligoni), remeshing.

B-REP (boundary representation):
- LA FRONTIERA COME DEFINIZIONE: un solido e' definito dalle sue superfici di confine: facce -> superfici matematiche (piani, cilindri, NURBS), spigoli -> curve (linee, archi, spline), vertici -> punti.
- I FORMATI STEP/IGES e le parti native dei CAD professionali sono B-Rep: la precisione e' esatta (un foro e' un cilindro perfetto, non una approssimazione a 32 facce).
- NURBS: le superfici freeform standard industriale: controllate da punti di controllo e pesi — dietro carrozzerie, carene, superfici architettoniche curve.
- TRADUZIONE: il kernel CAD (Open CASCADE — open source, Parasolid, ACIS) implementa le operazioni B-Rep.

QUANDO USARE COSA: mesh per visualizzazione, giochi, stampa 3D, scansione; B-Rep per progettazione di precisione, lavorazioni, tolleranze — STEP perche' viaggia tra CAD diversi."""),

rec("GEO-003","geometria_computazionale","booleane_kernel","OPERAZIONI BOOLEANE E KERNEL GEOMETRICI: L'ALGEBRA DEI SOLIDI",
"""Le operazioni booleane (unione, intersezione, sottrazione) sono l'operazione CAD per eccellenza: unione di muri, foro da un cilindro, tasca da un prisma.

COME FUNZIONANO (in breve):
1. CLASSIFICAZIONE: ogni porzione di superficie di entrambi i solidi viene classificata: dentro l'altro, fuori, o sul confine.
2. RICOSTRUZIONE: si tengono solo le porzioni richieste dall'operazione (unione = fuori+fuori; intersezione = dentro+entro; sottrazione = dentro il primo e fuori il secondo).
3. RIPARAZIONE: le intersezioni curve-superficie creano nuovi spigoli; il risultato deve restare un solido valido (chiuso, orientato).
Il punto critico e' la robustezza: intersezioni tangenziali, tolleranze, casi degeneri rendono le implementazioni naive instabili — il motivo per cui esistono pochi kernel CAD al mondo e sono decenni di ingegneria.

I KERNEL: Open CASCADE (open source, dietro FreeCAD e molti tool), Parasolid (Siemens), ACIS (Spatial), C3D. Un kernel e' una libreria C++ che implementa B-Rep, booleane, superfici, filettature, offset — il 'motore' sotto i CAD.

OPERAZIONI CORRELATE:
- OFFSET/SHELL: spessore uniforme (l'operazione che crea i muri cavi dal solido pieno);\n- FILLET/CHAMFER: raccordi e smussi con ricostruzione locale delle superfici;\n- SWEEP/LOFT: sezioni che viaggiano lungo traiettorie (estrusioni, scale rampe);\n- TESSELLAZIONE: conversione B-Rep -> mesh per la visualizzazione (controllata da angolo di deviazione).\n
COLLABORAZIONE CON L'AI: un LLM che capisce questi termini puo' generare script parametrici (OpenSCAD, FreeCAD Python) per costruire geometria per codice — il livello piu' alto: testo che diventa solido."""),

rec("GEO-004","geometria_computazionale","gis_spaziale","GIS E DATI SPAZIALI: LA GEOMETRIA CHE CAMMINA SUL TERRITORIO",
"""Il GIS (Geographic Information System) e' la geometria applicata al territorio: cantieri, rete idrica, vincoli urbanistici, catasto.

I CONCETTI BASE:
- GEOMETRIE: punto (un pozzo), linea (una condotta), poligono (un lotto, una zona vincolata). Coordinate in sistemi di riferimento: WGS84 (lat/lon GPS), sistemi proiettati locali (UTM, Gauss-Boaga in Italia) — LE PROIEZIONI contano: le distanze su lat/lon non sono metri!
- DATABASE SPAZIALI: PostGIS (estensione di PostgreSQL) aggiunge tipi geometry e indici spaziali (R-tree): 'tutti i cantieri entro 500 m da questa strada' e' una query SQL, non un programma.
- OPERAZIONI SPAZIALI: intersezione, buffer (zona tampon), within, contains, union/dissolve, voronoi.

LE ANALISI CHE VIVONO QUI:
- BUFFER ANALYSIS: zone di influenza (rumore, caduta gru, distanze da fognature);\n- INTERSEZIONE CATASTO/VINCOLI: il lotto tocca zona vincolata?\n- NETWORK ANALYSIS: percorsi ottimali (grafi su strade — corpus grafi incontra il territorio);\n- TIN E MODELLI DEL TERRENO: superfici da punti quotati (rilievi, curve di livello), calcolo dei volumi di scavo con metodo dei prismoidi.\n
DATI ITALIANI UTILI (pubblici): carte tecniche regionali, catastali (WFS/WMS dei geoportali), DTM nazionali, dati OpenStreetMap — la materia prima dei siting di cantiere e delle pratiche.
CASO D'USO AURATRIX: 'il terreno ha pendenza verso nord-est, il vincolo paesaggistico copre il 30% del lotto, la fogna piu' vicina e' a 40 m' — risposta da dati, non da memoria."""),

rec("GEO-005","geometria_computazionale","grafica_rendering","COMPUTER GRAPHICS E RENDERING: COME IL MODELLO DIVENTA IMMAGINE",
"""Dal modello 3D all'immagine fotorealistica: la pipeline della grafica che produce le tue renderizzazioni edili.

LA PIPELINE DI RENDERING (real-time):
1. TRASFORMAZIONI: vertici del modello -> mondo -> camera -> clip -> schermo (matrici del corpus GEO-001).
2. RASTERIZZAZIONE: quali pixel copre ogni triangolo.
3. SHADING: il colore di ogni pixel: modello di illuminazione (Lambert, Phong/PBR — physically based rendering: base color, roughness, metalness) piu' ombre (shadow mapping), riflessioni (reflection probes, screen-space).
4. POST-PROCESSING: bloom, antialiasing, tone mapping.

IL RAY TRACING (offline, fotorealistico): per ogni pixel si lancia un raggio che rimbalza sulla scena calcolando luce diretta, riflessa, rifratta — il metodo di V-Ray, Corona, Cycles. Costoso perche' simula la luce fisica: compromesso con path tracing e denoising.

LE RAPPRESENTAZIONI DI SCENA:
- SCENE GRAPH: gerarchia di nodi con trasformazioni (porta -> vano -> piano -> edificio): muovere il piano muove tutto;\n- Istanziamento: 1000 finestre identiche = 1 geometria disegnata 1000 volte (i motori ottimizzano cosi');\n- LOD (level of detail): lontano = meno poligoni.\n
MOTORI E FORMATI: Blender (open source, cicli/eevee), game engine (Unreal, Unity) per real-time architetturale (walkthrough), formati glTF/USD per scene interoperabili.
PER L'AI EDILE: generare buone immagini dei progetti (quando il testo non basta) richiede capire questa pipeline — anche solo per valutare cosa il modello 3D puo' promettere."""),
]

embedded = [
rec("EMB-001","embedded_iot","elettronica_base","ELETTRONICA E MICROCONTROLLORI: IL SOFTWARE CHE TOCCA L'ARIA",
"""L'embedded e' il software dentro le cose: sensori, attuatori, automazioni — e nell'edilizia: cantieri intelligenti, impianti connessi, sensoristica strutturale.

LE BASI CHE SERVONO:
- TENSIONE, CORRENTE, RESISTENZA: le grandezze elettriche (Ohm: V=RI). Livelli logici: 3.3V/5V — collegare un sensore da 5V a un pin da 3.3V brucia l'ingresso.
- DIGITALE vs ANALOGICO: i pin digitali leggono 0/1; gli ADC leggono tensioni continue (0-3.3V -> numero 0-4095): un sensore di temperatura e' analogico.
- BUS DI COMUNICAZIONE: I2C e SPI (corto raggio, tra chip sullo stesso circuito), UART/seriale (punto-punto), CAN bus (automotive/industriale, robusto), RS-485 (lunghe distanze, multipunto — usato in edilizia/impiantistica).
- MICROCONTROLLORI: ESP32 (WiFi+BLE integrato, il re dell'IoT economico), STM32 (professionale), Arduino (didattico). Si programmano in C/C++ con librerie hardware astratte.

I CONCETTI SOFTWARE EMBEDDED:
- REAL-TIME: i tempi contano al millisecondo: un watchdog riavvia se il loop si blocca; niente garbage collector, gestione manuale della memoria spesso.
- INTERRUPT: il codice si interrompe per eventi hardware (un pulsante, un dato arrivato) — la concorrenza piu' primitiva e piu' pericolosa.
- BASSO CONSUMO: deep sleep e wakeup timer: un sensore a batteria che vive 5 anni dorme il 99.9% del tempo.

QUANDO SERVE: mai per un sito web; sempre quando il dato nasce fisicamente: umidita' muro, vibrazione, apertura porta, consumo elettrico."""),

rec("EMB-002","embedded_iot","protocolli_iot","PROTOCOLLI IOT E EDGE: I DATI DEL CANTIERE CHE VIAGGIANO",
"""L'IoT industriale e' una questione di protocolli: come i sensori parlano con il mondo.

MQTT (IL PROTOCOLLO DELL'IOT):
- PUBBLISHER/SUBSCRIBER tramite BROKER: i sensori pubblicano su 'topic' ('cantiere/viaroma/temp'); chi si iscrive riceve. Leggerissimo, progettato per reti instabili e dispositivi deboli.
- TOPIC gerarchici: organizzare per cantiere/impianto/sensore — la stessa logica delle cartelle.
- QUALITY OF SERVICE: QoS 0 (al massimo una volta), 1 (almeno una), 2 (esattamente una) — scegliere in base a cosa costa perdere un messaggio.

OPC UA: lo standard industriale (fabbriche, impianti): tipizzato, sicuro, serve ai PLC e ai sistemi di supervisione (SCADA).

L'ARCHITETTURA EDGE:
- LIVELLO PERIFERIA: i sensori raccolgono e pre-processano (filtrano, aggregano) vicino alla fonte — perche' inviare 10 letture/sec quando basta la media ogni 5 minuti? Edge = meno traffico, meno costi cloud, resilienza se la rete cade.\n- LIVELLO GATEWAY: il concentratore locale (un Raspberry/PC industriale) che normalizza i protocolli e parla col cloud.\n- LIVELLO CLOUD: storage, dashboard, allarmi, analisi.\n\n"
"SICUREZZA IOT (il punto debole storico): credenziali default mai cambiate, firmware mai aggiornato, rete piatta. Minimo: credenziali uniche per dispositivo, rete segmentata, aggiornamenti OTA firmati.\n\n"
"CASO D'USO CANTIERE: sensori polvere/umidita'/rumore con soglie di allerta MQTT, centralina che gira i dati ogni 10 minuti, dashboard per il CSE — conformita' e sicurezza documentate in automatico."""),

rec("EMB-003","embedded_iot","sensoristica_cantiere","SENSORISTICA PER L'EDILIZIA: MISURARE PER COSTRUIRE",
"""La sensoristica trasforma il cantiere in dati: qualita', sicurezza, efficienza.

LE GRANDEZZE E I SENSORI:
- TEMPERATURA/UMIDITA' (igrometro per getti e maturazione del calcestruzzo: il calcestruzzo matura male sotto i 5 gradi e troppo in fretta col caldo — la CURVA DI MATURAZIONE si monitora con sonda e datalogger);
- PRESSIONE (impianti idraulici, caldaie);
- VIBRAZIONE (macchine, ponteggi: accelerometri per la manutenzione predittiva — lo spettro di vibrazione dice come sta un motore);
- LIVELLI (cisterne, serbatoi: ultrasuoni o pressione idrostatica);
- GAS (CO, CO2, metano: sicurezza ambientale e dei locali);
- PESO (celle di carico per ponti, gru: il sovraccarico e' la causa n.1 dei crolli di sollevamento);
- POSIZIONE/GNSS (georeferenziazione di mezzi e rilievi);
- STRUMENTAZIONE STRUTTURALE: estensimetri (deformazione), celle di carico nei puntoni, inclinometri (edifici e scavi — il monitoraggio dei cedimenti in fase di scavo e' spesso obbligatorio per legge: oscillazioni entro soglie prefissate, allarmi).

L'ANALISI DEI DATI: raw data -> medie mobili -> soglie -> allarme; trend nel tempo per la manutenzione predittiva ('la pompa vibra +30% rispetto al mese scorso').

INTEGRAZIONE CON L'AI: un LLM che legge i dati della sensoristica in linguaggio naturale ('ieri la temperatura del getto e' scesa sotto soglia per 3 ore — cosa comporta?') richiede che i dati siano accessibili via API — architettura MQTT -> database -> query per l'AI.

COSTI REALI: un sensore ESP32 + sonda = 10-30 euro; un sistema di monitoraggio cedimenti professionale = migliaia. Sapere la differenza e' gia' competenza."""),

rec("EMB-004","embedded_iot","automazione_impianti","AUTOMAZIONE E CONTROLLO: DAL SENSORE ALL'AZIONE",
"""Il controllo automatico chiude il cerchio: misurare -> decidere -> agire. Il cuore degli impianti intelligenti.

IL CONTROLLO ON/OFF (il termostato di casa):
- soglia con isteresi: accendi sotto 19, spegni sopra 21 — senza isteresi il relais starnutisce ogni 10 secondi (usura elettrica e meccanica). Il concetto piu' importante e' il piu' semplice.

IL CONTROLLO PID (proporzionale-integrale-derivativo):
- P: reagisci all'ERRORE attuale (lontano dalla temperatura target = piu' potenza);\n- I: correggi l'ERRORE ACCUMULATO NEL TEMPO (una deriva lenta sistematica);\n- D: anticipa in base alla VELOCITA' di avvicinamento (frena prima del sorpasso).\n- REGOLAZIONE: i tre guadagni si tarano empiricamente (metodo Ziegler-Nichols come partenza) — la taratura sbagliata = oscillazioni continue o lentezza.\n\n"
"LOGICA A SCALE (PLC): l'automazione industriale classica (ladder logic: i diagrammi a contatti elettrici diventano programmi) — dietro ascensori, cancelli, impianti di produzione. Gli standard IEC 61131 definiscono i linguaggi (ladder, structured text).\n\n"
"SUPERVISIONE (SCADA): il livello sopra i PLC: visuale grafica dello stato impianto, allarmi, storici, comandi manuali — i grandi impianti termotecnici ed edilizi ne fanno uso.\n\n"
"CASO D'USO: pompa di calore con climatica invernale (temperatura di mandata in funzione della temperatura esterna): curva tarabile, valvole di zona, integrazione domotica (corpus domotica del pack edilizia incontra il controllo).\n\n"
"PRINCIPIO: il miglior sistema di controllo e' quello che non si accorge mai di usare: stabile, tarato, con fallback manuali."""),

rec("EMB-005","embedded_iot","progetto_iot_edile","PROGETTO GUIDATO: SISTEMA DI MONITORAGGIO CANTIERE CONNESSO",
"""Progetto integrativo: 'site-sense' — il sistema IoT completo per un cantiere medio, dal sensore alla dashboard.

L'ARCHITETTURA:
1. SENSORI (fascia 10-40 euro): ESP32 + sensore temperatura/umidita'/polveri sui ponteggi e nei getti; GNSS per mezzi; pulsanti/manutentori per gli eventi manuali.
2. GATEWAY LOCALE (Raspberry o mini-PC): broker MQTT locale (Mosquitto) + Node-RED per la logica di raccolta: cosi' il sistema funziona ANCHE se internet cade — resilienza di cantiere.
3. DATABASE: InfluxDB (time-series: i dati di sensori sono serie temporali — compressione e query temporali ottimali) o Postgres con hypertable.
4. DASHBOARD: Grafana (open source): pannelli temperatura, umidita', eventi, soglie di allarme con notifica Telegram/email.
5. ALLARMI: regole esplicite ('getto collocato, temperatura < 5 gradi per 3 ore -> allerta CSE').

IL SOFTWARE EMBEDDED (firmware ESP32):
- deep sleep con wakeup ogni 5 minuti: lettura, publish MQTT, riposo — batteria di mesi;\n- retry e buffer locale (SPIFFS) per i periodi senza rete;\n- watchdog e auto-recovery.\n\n"
"LE SFIDE REALI:\n- AMBIENTE OSTILE: polvere, umidita', urti: contenitori IP65, connettori stag;\n- ALIMENTAZIONE: prese in cantiere instabili: batterie + pannellini solari per i punti lontani;\n- RETE: copertura mobile variabile: il gateway locale bufferizza.\n\n"
"VALORE DOCUMENTALE: i dati registrati diventano parte del fascicolo di cantiere (tracciabilita' getti, conformita' rumore/polveri) — e alimentano l'AI (Auratrix che legge 'il cantiere ha rispettato le soglie acustiche per tutta la durata').\n\n"
"CRITERIO DI FINE: 30 giorni di dati continui senza intervento manuale, e una persona non tecnica capisce la dashboard in 5 minuti."""),
]

compilatori = [
rec("CMP-001","compilatori","pipeline_compilatore","COME FUNZIONA UN COMPILATORE: DAL TESTO ALL'ESEGUIBILE",
"""Capire il compilatore rende migliori programmatori in qualunque linguaggio: e' l'interprete tra il tuo codice e la macchina.

LE FASI (la pipeline classica):
1. LEXING (tokenizzazione): la sorgente testuale diventa token: 'if', '(', 'x', '>', '3', ')'. Gli errori di sintassi si rilevano qui (caratteri inattesi).
2. PARSING: i token diventano ALBERO DI SINTASSI (AST): 'espressione if con condizione binaria >'. Gli errori di grammatica qui ('manca una parentesi').
3. ANALISI SEMANTICA: nomi risolti (a cosa si riferisce 'x'?), tipi controllati ('non puoi sommare stringa e intero'), scope. L'errore 'variabile non definita' viene da qui.
4. OTTIMIZZAZIONE: l'albero/il codice intermedio viene trasformato per essere piu' veloce (eliminare codice morto, spostare calcoli fuori dai cicli, inline delle funzioni piccole) — decine di passi, tutti corretti per costruzione.
5. CODE GENERATION: l'output finale: machine code della CPU, oppure bytecode per una VM (Java, Python, .NET), oppure sorgente di un altro linguaggio (transpiling TypeScript -> JavaScript).

INTERPRETI, JIT, AOT:
- INTERPRETE: esegue l'AST riga per riga (Python classico) — lento ma immediato.
- JIT: compila a runtime le parti calde (Java HotSpot, V8) — il meglio dei due mondi, con costo di avvio.
- AOT: compilato prima (C, Go, Rust) — massime prestazioni e prevedibilita'.

PERCHE' IMPORTA A CHI NON SCRIVE COMPILATORI: i messaggi d'errore moderni (Rust e' famoso per questo) derivano da compilatori che si sforzano di spiegare la semantica: chi capisce le fasi legge gli errori piu' velocemente e capisce perche' certi costrutti costano piu' di altri."""),

rec("CMP-002","compilatori","parser_approfondito","PARSER E GRAMMATICHE: LA TEORIA DI DIETRO AL TESTO",
"""Dietro ogni linguaggio (di programmazione, config, query) c'e' una grammatica formale: sapere la teoria rende il parsing di progetto invece che di tentativo.

LA GERARCHIA DI CHOMSKY (il panorama, semplificato):
- REGOLARI: espresse dalle regex — il livello piu' debole;\n- LIBERE DAL CONTESTO: i linguaggi di programmazione — grammatiche con produzioni ricorsive ('espressione = espressione + termine');\n- I linguaggi naturali (italiano) non sono nemmeno liberi dal contesto — per questo gli LLM e non i parser.\n\n"
"GRAMMATICHE: la definizione formale (terminali, non-terminali, produzioni, simbolo iniziale). Una grammatica AMBIGUA permette due alberi per la stessa frase ('2+3*4' con due priorita') — le grammatiche dei linguaggi reali sono progettate per essere non ambigue, e dove non lo sono (il dangling else) si aggiungono convenzioni.\n\n"
"ALGORITMI DI PARSING:\n- LL (top-down, ricorsivo discendente): ogni non-terminale e' una funzione che chiama le altre — il metodo manuale piu' leggibile, alla base di parser artigianali;\n- LR (bottom-up, tabellare): i generatori automatici (yacc, bison, ANTLR) costruiscono tabelle da una grammatica e riconoscono una classe piu' ampia di linguaggi;\n- PEG/PACKRAT: le moderne grammatiche con priorita' (usate da molti linguaggi recenti).\n\n"
"ERROR RECOVERY: un parser che muore al primo errore e' inutile negli IDE: la tecnica del panic mode (saltare fino al punto di sincronizzazione) permette di segnalare PIU' errori in un colpo.\n\n"
"APPLICAZIONE PRATICA: quando incontri un file config strano, un mini-linguaggio di dominio (corpus progetti), o vuoi validare rigorosamente input: la domanda 'qual e' la grammatica?' trasforma il problema."""),

rec("CMP-003","compilatori","bytecode_vm","BYTECODE, VM E RUNTIME: DOVE VIVE IL CODICE CHE ESEGUI",
"""Tra il codice sorgente e il silicio c'e' spesso uno strato intermedio: il bytecode e la sua macchina virtuale.

IL MODELLO: il compilatore genera bytecode (un linguaggio macchina ipotetico, compatto); una VM lo esegue. Esempi: JVM (Java/Kotlin/Scala), CLR (.NET/C#), CPython, JavaScript V8, WebAssembly (il bytecode del web).

PERCHE' IL BYTECODE:
- PORTABILITA': 'write once, run anywhere' — la VM si porta, il bytecode no;\n- VELOCITA' DI AVVIO: il bytecode si genera/carica piu' in fretta del machine code nativo;\n- SICUREZZA: la VM controlla i tipi e gli accessi a runtime;\n- STRUMENTAZIONE: debug, profiling, garbage collection sono piu' facili sulla VM.\n\n"
"LA VM: un ciclo fetch-decode-execute su istruzioni numerate: stack machine (i valori vivono su una pila: JVM, CPython) o register machine (Dalvik). Il garbage collector (mark-and-sweep, generational) vive qui: perche' Java/Go/Python non chiedono di liberare la memoria.\n\n"
"JIT E TIERED COMPILATION: la VM moderna (V8, HotSpot) osserva quali funzioni girano tanto e le compila in nativo ottimizzato a runtime, speculando sui tipi osservati — se la speculazione fallisce, de-ottimizza. E' la ragione per cui JavaScript e' passato da 'linguaggio lento' a fondamenta del web.\n\n"
"WEBASSEMBLY (WASM): il bytecode universale moderno: linguaggi come Rust, C, Go compilano a WASM e girano nel browser e su server (Wasmtime) quasi a velocita' nativa — sandboxed, veloce, portabile. La direzione del futuro per plugin e computazione sicura.\n\n"
"PER IL PRATICO: capire la VM spiega i costi reali (perche' i loop Java erano lenti e ora no), i messaggi d'errore di runtime, e le scelte di deployment (JVM in produzione = ops consolidate)."""),

rec("CMP-004","compilatori","tipi_semantica","TIPI, TYPE SYSTEMS E PERCHE' ESISTONO",
"""Il sistema dei tipi e' il primo linter del programma: la sua storia spiega TypeScript, Rust e tutti i moderni.

COSA FA UN TYPE SYSTEM:
- RIFIUTA programmi con certi errori PRIMA dell'esecuzione (sommare un intero a una stringa, chiamare un metodo inesistente);\n- DOCUMENTA: la firma 'fun calcola(mq: float, prezzo: float) -> float' e' un contratto leggibile;\n- ABILITA' STRUMENTI: autocomplete, refactoring sicuri, navigazione del codice — impossibili senza tipi.\n\n"
"LA TASSONOMIA:\n- STATICO vs DINAMICO: i tipi si controllano a compile time (Java, Rust, TypeScript) o a runtime (Python, JS);\n- FORTE vs DEBOLE: quanto il linguaggio impedisce implicitamente di mischiare tipi (forte: Python, Rust; debole: PHP storico, JavaScript con le coercizioni);\n- INFERENZA: il compilatore deduce i tipi senza dichiararli (Haskell, Rust, TypeScript moderato, Python col mypy);\n- NULL SAFETY: i moderni (Kotlin, Rust, Swift, TypeScript strict) distinguono 'valore' e 'forse valore' nel TIPO — il famoso 'bilione di dollari' di Tony Hoare per i null pointer.\n\n"
"I TIPI AVANZATI CHE CONTANO:\n- GENERICS: parametrizzare i tipi (una lista di T, non di 'qualsiasi cosa') senza perdere la sicurezza;\n- ALGEBRAIC DATA TYPES (Rust enum, Haskell): modellare 'questo OPPURE quello' nel tipo — lo stato impossibile diventa irrapresentabile: 'Preventivo = Bozza | Inviato | Accettato | Rifiutato' — non serve un booleano 'isInviato' incoerente;\n- PATTERN MATCHING: smontare i tipi con exhaustiveness check ('hai dimenticato il caso Rifiutato').\n\n"
"LA LEZIONE ARCHITETTONICA: i type system buoni si usano per RENDERE IMPOSSIBILI gli stati sbagliati, non per correggerli dopo."""),

rec("CMP-005","compilatori","costruire_linguaggio","COSTRUIRE UN MINI-LINGUAGGIO: IL PROGETTO CHE INSEGNA TUTTO",
"""Progetto integrativo del corpus: un linguaggio di scripting mini — 'calc-script' per espressioni di computo con variabili.

PERCHE' QUESTO PROGETTO: costruire un linguaggio insegna lexer, parser, semantica, interpreti, scope, garbage collection — l'intero corpus compilatori in un solo esercizio. Chi ha scritto un interprete capisce per sempre come i linguaggi si comportano.

LE FASI (ognuna un weekend):
1. LEXER: da testo a token. Un pomeriggio con una tabella di regex ordinate.
2. PARSER RICORSIVO DISCENDENTE: grammatica piccola: espressione -> termine (('+'|'-') termine)*; termine -> fattore (('*'|'/') fattore)*; la ricorsione per le parentesi. AST come classi/enum.
3. INTERPRETE TREE-WALKING: visita l'AST e calcola — l'interprete piu' semplice del mondo.
4. VARIABILI E SCOPE: 'let x = 5'; ambiente come mappa nidificata (scope lessicale: una catena di mappe).
5. FUNZIONI (se si vuole il livello avanzato): chiusure (le funzioni ricordano il loro ambiente — il concetto che illumina JavaScript).
6. ERRORI CON STILE: riga/colonna nei messaggi ('alla riga 3: variabile sconosciuta x') — la qualita' percepita di un linguaggio e' la qualita' dei suoi errori.

VARIANTE PER L'EDILIZIA: il linguaggio legge variabili da un file voci ('mq_cappotto = 120') ed espressioni di costo ('costo = mq_cappotto * prezzo_mq + costo_fisso') — un mini-computo dichiarativo: il progetto fine a se stesso e utile.

ESTENSIONE INDUSTRIALE: trasformare l'interprete in un COMPILATORE verso bytecode proprio (stack machine con 20 istruzioni) — si capisce la VM dal di dentro.

CRITERIO DI FINE: un file di 20 righe del tuo linguaggio viene letto, eseguito, e produce il risultato atteso — con un messaggio d'errore comprensibile quando sbagli."""),
]

concorrenza = [
rec("CON-001","concorrenza","modelli","MODELLI DI CONCORRENZA: THREAD, PROCESSI, EVENTI E ATTORI",
"""La concorrenza ha quattro famiglie di soluzione: scegliere quella giusta e' una decisione architetturale.

I MODELLI:
1. PROCESSI: programmi separati con memoria separata — sicuri (nessun dato condiviso da corrompere) ma costosi da creare; comunicazione via pipe/socket. Il modello 'Unix'.
2. THREAD (CONDIVISIONE DELLA MEMORIA): piu' esecutori nello stesso processo, stessa memoria: veloci, ma il caos e' dietro l'angolo — due thread che toccano lo stesso dato contemporaneamente corrompono tutto. Sincronizzazione: lock, semafori, condition variable. Potente e pericoloso: il modello di Java, C++, Rust.
3. EVENT LOOP (SINGLE-THREAD ASYNC): un solo esecutore che gestisce eventi/callback (JavaScript, asyncio): niente race condition sulla memoria (single thread!) ma attenzione ai blocchi (un calcolo lungo blocca TUTTO — 'mai fare CPU-bound nel loop').
4. ATTORI/CSP: il modello dei messaggi (Akka, Erlang/OTP, Go channels): ogni attore ha la sua mailbox e il suo stato privato — comunicano solo messaggi. Niente memoria condivisa = niente lock. Il modello piu' robusto per sistemi distribuiti concorrenti.

COME SCEGLIERE:
- CPU-bound parallelo (calcoli su molti core): thread/process pool;\n- I/O-bound ad alto volume (10.000 connessioni): event loop;\n- sistemi distribuiti affidabili: attori;\n- scripts e pipelines: processi.\n\n"
"L'ERRORE CLASSICO: scegliere i thread perche' familiari e poi scoprire che il 70% del codice e' sincronizzazione — quando i message passing bastavano.\n\n"
"PER L'AI: capire il modello del linguaggio che stai usando e' il prerequisito per scrivere codice concorrente corretto al primo colpo — e per capire perche' il codice dell'AI talvolta e' sbagliato sotto concorrenza."""),

rec("CON-002","concorrenza","lock_deadlock","LOCK, RACE CONDITION E DEADLOCK: I TRE FANTASMI",
"""La concorrenza con memoria condivisa ha tre mostri: riconoscerli e disinnescarli e' la competenza.

1. RACE CONDITION: il risultato dipende dall'ordine imprevedibile di esecuzione. Classico: 'check-then-act' — 'se il conto ha fondi, ritira': tra il controllo e il ritiro un altro thread ritira: conto negativo. La regola: ogni invariante va protetta atomicamente, non in due passi.
2. DATA RACE: accesso concorrente alla stessa memoria con almeno una scrittura, senza sincronizzazione — undefined behavior in C/C++, fonte di bug impossibili da riprodurre.
3. DEADLOCK: due thread si aspettano a vicenda (A tiene lock 1, vuole 2; B tiene 2, vuole 1) — entrambi fermi per sempre.

LE REGOLE DI PREVENZIONE:
- MINIMIZZARE LO STATO CONDIVISO: meno dati condivisi = meno lock; preferire immutabilita' (strutture dati immutabili: si copia invece di mutare — costa memoria, compra correttezza);\n- GERARCHIA DEI LOCK: acquisire i lock SEMPRE nello stesso ordine globale: niente deadlock;\n- LOCK A GRANA FINE/GROSSA: lock grande = semplice ma lento (tutto aspetta); lock fine = veloce ma deadlock dietro l'angolo: si parte dal grande;\n- TIMEOUT E STRUMENTI: i lock con timeout rivelano i deadlock invece di congelare; i detector (Go, ThreadSanitizer) li trovano in test.\n\n"
"DEBUGGING: i bug concorrenti sono non deterministici ('mai successo sul mio pc') — si riproducono con stress test dedicati e i tool sanitizers, non con il debugger classico.\n\n"
"REGOLA FINALE: la soluzione migliore al problema dei lock e' architetturale — non avere bisogno del lock (message passing, immutabilita')."""),

rec("CON-003","concorrenza","lockfree_atomics","LOCK-FREE, ATOMICHE E STRUTTURE CONCORRENTI",
"""Al di la' dei lock: la programmazione lock-free con operazioni atomiche — la frontiera per le performance estreme.

LE OPERAZIONI ATOMICHE: istruzioni hardware indivisibili: fetch-and-add, compare-and-swap (CAS) — 'se il valore e' ancora X, scrivi Y'. Sono la base di tutto il resto.

COSTRUIRE SOPRA LE ATOMICHE:
- CONTATORI ATOMICI: incrementi senza lock: il 90% dei casi d'uso reale;\n- SPINLOCK: attesa attiva invece di dormire — giusto per attese brevissime (microsecondi), altrimenti si brucia CPU;\n- LOCK-FREE QUEUE: producer e consumer che si incrociano senza mai bloccarsi (algoritmo di Michael-Scott): le code ad alta frequenza (logging, task dispatch) girano cosi'.\n\n"
"IL PROBLEMA ABA: con CAS, tra la lettura di X e lo scambio, il valore puo' diventare Y e tornare X (ABA): il CAS ha successo ma lo stato e' cambiato due volte — soluzione: puntatori con contatore (tagged pointers) o double-width atomics.\n\n"
"L'ORDINAMENTO DELLA MEMORIA (memory ordering): le CPU riordinano le istruzioni per performance: 'sequentially consistent' (il default sicuro), 'acquire/release' (il compromesso giusto per i sistemi reali). Usare i default sicuri finche' il profiler non dice il contrario.\n\n"
"QUANDO SERVE DAVVERO: contatori ad altissima frequenza, code tra thread, engine di giochi, database. Per il 95% delle applicazioni: i lock di alto livello (mutex) o i channel bastano — e sono piu' semplici da ragionare.\n\n"
"AVVERTENZA ONesta: il codice lock-free e' tra i piu' difficili da scrivere e da verificare: si adotta da librerie consolidate (crossbeam, java.util.concurrent), mai artigianalmente, salvo necessita' misurata."""),

rec("CON-004","concorrenza","strutture_concorrenti","STRUTTURE DATI CONCORRENTI E POOL: LA CASSA DEGLI ATTREZZI",
"""Le strutture dati concorrenti pronte all'uso risolvono il 95% dei problemi: conoscerle evita di reinventarle male.

IL MENU':
- CONCURRENT HASH MAP: letture concorrenti veloci, scritture sincronizzate a grana fine (Java ConcurrentHashMap, Rust dashmap) — la struttura piu' usata: cache, registri, tabelle condivise;\n- CONCURRENT QUEUE: LinkedBlockingQueue, ArrayBlockingQueue, channel Go — handoff tra thread: il pattern produttore/consumatore fatto bene;\n- READ-WRITE LOCK: molti lettori O uno scrittore — per dati letti molto piu' che scritti;\n- SEMAFORI E BARRIERE: limitare l'accesso a N risorse, sincronizzare fasi di calcolo;\n- ATOMIC REFERENCES: aggiornamenti atomici di oggetti interi (la base dell'immutabilita' concorrente).\n\n"
"I PATTERN CHE RISOLVONO I PROBLEMI REALI:\n1. PRODUCER-CONSUMER: una coda come 'ponte' tra chi produce e chi consuma: disaccoppia i ritmi (il parser butta in coda, il writer scrive — chi va piu' veloce non aspetta);\n2. OBJECT POOL: riuso di risorse costose (connessioni DB, thread): meno allocazione = meno pressione GC;\n3. BATCHING: accumulare e processare a blocchi — il throughput batte la latenza per i lavori bulk;\n4. BACKPRESSURE: quando il consumatore e' lento, il produttore DEVE rallentare (coda limitata: 'se e' piena, aspetta o butta') — altrimenti la memoria esplode.\n\n"
"LA REGOLA D'ORO: prima struttura concorrente pronta, lock semplice solo se serve, lock-free mai salvo misurato. La complessita' concorrente va comprata solo quando i numeri la giustificano."""),

rec("CON-005","concorrenza","async_moderno","ASYNC/AWAIT E PROGRAMMAZIONE ASINCRONA MODERNA",
"""L'async/await e' il modello dominante della concorrenza I/O (Python asyncio, JS, Rust tokio, C#, Kotlin): potente ma con le sue trappole.

IL MODELLO MENTALE: la funzione async restituisce subito una 'promessa' (coroutine/task) e il runtime la riprende quando il risultato e' pronto. Un solo thread gestisce migliaia di operazioni I/O perche' mentre una aspetta, le altre girano. Il guadagno: niente blocchi = niente thread in attesa.

LE REGOLE DI SOPRAVVIVENZA:
1. NON BLOCCARE IL LOOP: dentro una funzione async, MAI operazioni bloccanti (sleep sincrono, CPU-bound lungo, chiamate sync): bloccheresti TUTTO. Il CPU-bound va in executor/pool separato.\n2. GESTIRE SEMPRE LE ECCEZIONI: un task il cui errore non viene atteso ('fire and forget') muore in silenzio e perdi l'eccezione: si raccolgono i task e si verificano.\n3. TIMEOUT OVUNQUE: ogni await potenzialmente infinito va dentro un timeout.\n4. CONCORRENZA DI PIU' OPERAZIONI: Promise.all / asyncio.gather: le chiamate indipendenti vanno INSIEME, non in sequenza: da 3 chiamate da 1s a 1s totale invece che 3s.\n5. STATO CONDIVISO: in single-threaded async i dati condivisi non fanno data race MA fanno race logiche (un await a meta' funzione interrompe il flusso: lo stato puo' cambiare dopo ogni await — il 'check-then-act' ritorna).\n\n"
"QUANDO NON USARLO: il codice async complica il flusso (stack trace spezzati, debug piu' duro): se il servizio e' semplice e sincrono va benissimo essere sincroni. L'async si paga solo dove il numero di connessioni/contesti lo giustifica.\n\n"
"PER L'AI: il codice generato dall'AI manca spesso di timeout e gestione errori nei task — primo controllo da fare sul codice async proposto."""),
]

testing = [
rec("TST-001","testing_avanzato","property_based","PROPERTY-BASED TESTING: VERIFICARE LE PROPRIETA', NON GLI ESEMPI",
"""Oltre l'unit test con esempi fissi: il property-based testing genera centinaia di casi automaticamente e verifica le PROPRIETA' invarianti.

IL CONCETTO: invece di 'f(2)=4', si dichiara la proprieta': 'per OGNI x: ordinare due volte = ordinare una volta' (idempotenza), 'per OGNI lista: somma degli elementi = somma ordinati', 'per OGNI preventivo: il totale >= 0'. La libreria (Hypothesis per Python, fast-check per JS, QuickCheck per Haskell) genera casi casuali mirati, trova il controesempio MINIMO (shrinking) e lo riporta.

DOVE BRILLA:
- FUNZIONI PURE: parsing, calcolo, trasformazioni dati — tutto cio' dove gli esempi a mano non coprono lo spazio degli input;\n- REGOLE DI BUSINESS: 'sconto mai negativo', 'le voci del preventivo restano coerenti dopo ogni operazione';\n- SERIALIZZAZIONE/ROTAZIONE: 'encode(decode(x)) == x' per qualunque x valido.\n\n"
"L'ANALOGIA EDILE: collaudare un muro su 3 punti a mano vs collaudare la PROPRIETA' 'ogni punto del muro ha resistenza >= R' con strumento che scansiona — la copertura non e' paragonabile.\n\n"
"IL WORKFLOW: 1. scrivere le proprieta' insieme alle funzioni; 2. lasciare che il generatore trovi i casi limite (stringhe vuote, unicode, numeri enormi, liste nil); 3. quando trova un fallimento, aggiungere il caso MINIMO ai test di regressione.\n\n"
"CASO D'USO CONCRETO: un parser di voci di computo — property: 'per ogni testo valido, il parse produce voci con importi >= 0 e la somma coincide col totale dichiarato'. Centinaia di input generati trovano in 10 secondi i casi che 50 esempi a mano avrebbero perso.\n\n"
"LIMITI: serve pensare alle proprieta' (piu' difficile che scrivere esempi); non sostituisce i test di integrazione e i casi di business specifici."""),

rec("TST-002","testing_avanzato","mutation_fuzzing","MUTATION TESTING E FUZZING: STRESSARE I TEST, STRESSARE IL CODICE",
"""Due tecniche che misurano e forzano la qualita' oltre il 'tutto verde'.

MUTATION TESTING: i test verdi sono davvero buoni? Si muta il codice di produzione (si cambia '>' in '>=', si cancella una riga) e si controlla che ALMENO UN TEST fallisca. Se i test restano verdi con il codice sbagliato, non stanno testando niente. Tool: mutmut (Python), Stryker (JS/Java), PIT (Java). Metrica: mutation score. Usi: sul codice critico (calcoli, auth) dove 'copertura 100%' non basta — copre le RIGHE, non le DECISIONI.

IL FUZZING: inondare il programma con input semi-casali (e non: fuzzing coverage-guided come AFL/libFuzzer) alla ricerca di crash, memory bug, eccezioni non gestite. Categorie:
- FUZZING DI PARSER E API: input malformati, payload casuali su ogni endpoint — la sicurezza moderna (OSS-Fuzz di Google trova migliaia di bug cosi');\n- FUZZING DI PROPRIETA': combinato col property-based testing (Hypothesis fa gia' fuzzing casuale mirato);\n- CHAOS ENGINEERING (la categoria grande): in produzione controllata, si rompe DI PROPOSITO — si uccidono istanze, si rallenta la rete, si riempiono i dischi — per verificare che il sistema sopravviva (Chaos Monkey di Netflix). La regola: prima la resilienza si progetta (corpus affidabilita'), poi si dimostra col caos.\n\n"
"QUANDO ADOTTARLE: mutation testing sui moduli piu' critici (una passata a sprint); fuzzing continuo su parser, API pubbliche, deserializzatori; chaos dopo che l'osservabilita' e' pronta (altrimenti si rompe e non si vede).\n\n"
"IL PRINCIPIO: i test si verificano come il codice — e la robustezza si dimostra rompendo le cose in condizioni controllate, non sperando che reggano."""),

rec("TST-003","testing_avanzato","load_testing","LOAD TESTING E PERFORMANCE TESTING: SAPERE QUANTO REGGE",
"""Quanto traffico regge il sistema? La risposta si misura con i test di carico, non si spera.

LE FASI DEL CARICO:
1. BASELINE: il sistema a riposo — latenza e throughput di riferimento.
2. LOAD TEST: il traffico atteso normale (o 2x): il sistema deve reggere con le performance accettabili. Metrica: p95/p99 della latenza (la media nascode code).
3. STRESS TEST: si aumenta finche' ROMPE — per trovare il punto di rottura e come si rompe (degrada o crolla? errori puliti o timeouts a catena?).
4. SOAK TEST (endurance): carico costante per ore/giorni — rivela leak di memoria, degradazioni lente, connessioni che non tornano al pool.
5. SPIKE TEST: un picco improvviso 10x per 30 secondi — come un preventore che va virale o il rientro delle ferie: la capacita' di assorbire gli spike dipende da code, cache e autoscalig.

GLI STRUMENTI: k6, Gatling, Locust (open source): script di scenario (simulano comportamenti utente reali: login -> cerca -> compra), distribuiti da piu' nodi per la scala.

CIO' CHE SI IMPARA DAI NUMERI:
- la legge di Little (concorrenza = throughput x latenza): quanti utenti simultanei regge davvero;\n- i colli di bottiglia reali: quasi sempre database e code esterne (corpus performance);\n- le soglie da dichiarare: 'regge 500 utenti concorrenti con p95 < 300ms' e' un requisito misurabile, 'e' veloce' no.\n\n"
"ERRORE CLASSICO: testare solo il backend: la CDN, il frontend pesante, il mobile su rete 4G scarsa sono metà dell'esperienza.\n\n"
"REGOLA: il load test entra nella CI solo per i controlli di regressione di performance (un ordine di grandezza), le campagne complete restano periodiche."""),

rec("TST-004","testing_avanzato","integration_infra","TEST DI INTEGRAZIONE CON INFRASTRUTTURA REALE",
"""L'unit test con i mock va bene per la logica; ma a un certo punto bisogna testare contro la REALTA': database veri, API vere, code vere.

I PRINCIPI:
1. TESTCONTAINER (il pattern vincente): i test di integrazione alzano veri database/Redis/MQTT in container Docker, li popolano, verificano, li buttano. Ogni test ha la sua istanza isolata: niente 'test che dipendono dall'ordine', niente ambiente condiviso instabile. Supporti: testcontainers (Java, Python, JS, Go, .NET).
2. COSA TESTARE CONTRO INFRASTRUTTURA REALE:
   - le QUERY (l'ORM genera SQL giusto? gli indici esistono? la transazione fa quello che credi?);\n   - le MIGRAZIONI (la migrazione su uno schema popolato funziona e torna indietro?);\n   - le CODE (il messaggio pubblicato arriva? il consumer e' idempotente? il DLQ funziona?);\n   - le API ESTERNE con contract test (Pact): il provider e il consumatore rispettano il contratto — quando l'API esterna cambia, si scopre in CI, non in produzione.\n3. LE REGOLE DI ORO: i test di integrazione sono lenti (secondi/minuti): pochi, mirati ai confini; i mock restano per la logica pura; il CI li gira in parallelo su runner separati.\n\n"
"IL PROBLEMA DEI MOCK ECESSIVI: quando tutto e' mockato, i test passano e la produzione e' rotta — il classico 'i test erano verdi'. I confini da NON mockare: il database (testcontainer), i protocolli complessi, i sistemi di cui NON controlli il contratto.\n\n"
"L'ANALOGIA EDILE: i mock sono il plastico, i test di integrazione sono la struttura di prova: prima di consegnare si collauda il materiale VERO.\n\n"
"METRICA DI MATURITA': il tempo tra 'un cambiamento rompe il confine con X' e 'ci accorgiamo in CI': minuti, non giorni."""),

rec("TST-005","testing_avanzato","qualita_processo","QUALITA' COME PROCESSO: COVERAGE, QUALITA' E CULTURA DEI TEST",
"""La qualita' non e' uno sprint finale: e' un processo con metriche oneste e una cultura di team.

LE METRICHE (usate bene):
- COVERAGE (copertura): percentuale di righe/rami eseguiti dai test. Regola sana: 80%+ sul codice di dominio; 100% sul codice critico; NON inseguire il 100% ovunque (i getter testati non aggiungono valore — la coverage misura cio' che ESEGUE, non cio' che VERIFICA: si combina col mutation testing).\n- DEFECT ESCAPE RATE: quanti bug arrivano in produzione vs trovati prima — la metrica che conta davvero: si misura il PROCESSO, non il codice;\n- FLAKY TEST RATE: i test che falliscono a caso (timing, ordine, dipendenze esterne) distruggono la fiducia: si perseguono con test deterministici, orologi controllati, retry SOLO su cause note — un test flaky va disattivato e riparato, non rieseguito.\n- TEMPO DI FEEDBACK: da commit a verdetto: sotto i 10 minuti o si aggira.\n\n"
"LA PIRAMIDE DEI TEST (la si rispetta?): 70% unit (veloci, numerosi), 20% integrazione (confini), 10% end-to-end (pochi, sui flussi critici). Il anti-pattern: l'ice cream cone — tutto e2e, tutto lento, tutto fragile.\n\n"
"LA CULTURA:\n- chi rompe i test, li aggiusta (subito, non 'dopo');\n- il 'test prima o subito dopo' nelle definition of done;\n- i test vanno trattati come codice di produzione: revisionati, refactorizzati, cancellati quando obsoleti;\n- il code review include i test: un'implementazione senza test di comportamento nuovo e' incompleta.\n\n"
"L'ERRORE STRATEGICO N.1: trattare i test come costo. I test sono il PREZZO pagato per la VELOCITA' futura: il codice ben testato si modifica in ore, quello no in settimane di paura."""),
]

corpora = [
    ("interview_algoritmi.jsonl", interview),
    ("geometria_computazionale.jsonl", geometria),
    ("embedded_iot.jsonl", embedded),
    ("compilatori_linguaggi.jsonl", compilatori),
    ("concorrenza_avanzata.jsonl", concorrenza),
    ("testing_avanzato.jsonl", testing),
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
