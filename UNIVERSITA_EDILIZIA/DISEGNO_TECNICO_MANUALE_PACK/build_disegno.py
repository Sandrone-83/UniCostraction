# -*- coding: utf-8 -*-
"""Costruisce DISEGNO_TECNICO_MANUALE_PACK: norme di rappresentazione, tipi di disegno, tavole e cartigli."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Fondamenti", "Il linguaggio del disegno tecnico: perché esiste",
 "Il disegno tecnico è la lingua universale tra progettista, cliente, direzione lavori e produzione: un insieme di convenzioni grafiche che permettono di descrivere un oggetto in modo univoco, senza ambiguità, indipendente dalla lingua parlata.",
 "Basato su regole condivise (proiezioni ortogonali, quote, scale, sezioni) definite dalle norme UNI/ISO; ogni segno sul foglio ha un significato convenzionale: linee continue = bordi visibili, tratteggiate = spigoli nascosti, a catena = assi di simmetria, sottili continue = quote e riferimenti.",
 "Tavole di progetto, disegni di officina, planimetrie, documenti di gara, manuali di montaggio.",
 "Elimina gli equivoci: due tecnici di paesi diversi leggono la stessa tavola e vedono lo stesso oggetto; è la base legale del capitolato (chi costruisce DEVE consegnare quanto disegnato).",
 "Richiede disciplina: una convenzione sbagliata o mancante può costare errori in produzione di migliaia di euro.",
 "Il costo è solo tempo di produzione tavola (ora di tecnico); il costo di UN errore di disegno è invece sproporzionato.",
 "Un dettaglio costruttivo di un cappotto mal quotato (spessore non indicato) ha prodotto in un cantiere reale il montaggio di serramenti fuori sagoma con smontaggio e rifacimento a carico dell'appaltatore.",
 "UNI EN ISO 128 (regole generali della rappresentazione); UNI EN ISO 129 (quotatura).",
 "Prima regola d'oro: ogni tavola deve poter essere interpretata SENZA parlare con chi l'ha disegnata."),
s("Proiezioni", "Le proiezioni ortogonali: il metodo di Monge",
 "Il metodo delle proiezioni ortogonali (Monge, fine '700) rappresenta un oggetto 3D su piani paralleli alle sue facce principali: pianta (vista dall'alto), alzati/prospetti (viste frontali e laterali), spaccati (sezioni).",
 "Si proiettano i punti dell'oggetto su piani ortogonali tra loro e si dispongono le viste secondo lo standard europeo (primo diedro, simbolo del troncato di cono con cerchio a sinistra) o americano (terzo diedro).",
 "Qualsiasi disegno architettonico o meccanico: piante, sezioni, prospetti, disegni di parti in officina.",
 "Dà informazioni complete e misurabili dall'oggetto: ogni quota è vera in scala, cosa che le prospettive non garantiscono.",
 "Le viste singole non mostrano la profondità: servono almeno 2-3 viste coordinate; i principianti sbagliano spesso l'allineamento tra pianta e alzati.",
 "Nessun costo specifico: è il metodo base di ogni CAD 2D e 3D.",
 "Il classico esercizio accademico: disegnare un pezzo meccanico dalle tre viste (di fronte, di lato, dall'alto) e verificare che ogni spigolo corrisponda; errore tipico = linea mancante nel cambio di piano.",
 "UNI EN ISO 128-30 (viste); UNI EN ISO 5456 (proiezioni).",
 "In cantiere: la pianta e la sezione devono sempre essere allineate (stessa quota di riferimento) o chi esegue legge male i vani."),
s("Sezioni e spaccati", "Sezioni, spaccati e dettagli costruttivi",
 "La sezione è la vista dell'oggetto 'tagliato' lungo un piano di taglio: mostra ciò che le viste esterne nascondono (anime, stratigrafie, connessioni). Lo spaccato è una sezione applicata all'edificio; il dettaglio è un ingrandimento di una zona critica.",
 "Il piano di taglio si indica in pianta/alzato con una linea a catena grossa e le frecce di osservazione; la parte tagliata si tratteggia secondo il materiale (muratura, calcestruzzo, legno, metallo hanno tratteggi UNI diversi); le zone dietro il taglio si vedono proiettate.",
 "Stratigrafie di parete, connessioni solaio-muratura, fondazioni, carpenteria, particolari di giunzione tra materiali diversi.",
 "È l'unico modo di 'vedere' dentro i muri: senza sezione non esiste progetto eseguibile né verifica del cappotto o del cappotto-serramento.",
 "Una sezione mal scelta (taglio fuori dal punto critico) nasconde esattamente il nodo che serviva controllare.",
 "Tempo tecnico maggiorato rispetto alle viste semplici; i dettagli ingranditi sono ciò che differenzia un progetto serio da uno da operazione commerciale.",
 "La verifica termigrafica di un edificio mostra ponti termici proprio dove il dettaglio costruttivo era generico ('a completamento dell'impresa') invece di quotato: il risultato è muffa agli angoli.",
 "UNI EN ISO 128-40/50 (sezioni e tagli); UNI 3973 (tratteggi dei materiali, ancora molto usata in Italia).",
 "Regola pratica: TUTTI i nodi dove due materiali diversi si incontrano (finestra/muro, solaio/muro, copertura/muro) DEVONO avere il proprio dettaglio quotato."),
s("Quotatura", "La quotatura: regole, catene di quote, riferimenti",
 "La quotatura trasferisce le dimensioni reali sul disegno: quote in millimetri (edilizia italiana) scritte sopra linea di quota sottile, con frecce o spigoli che toccano gli estremi misurati.",
 "Catene di quote aperte o chiuse; quota funzionale (si quota ciò che serve per fabbricare/posare, NON ogni tratto); quote di riferimento (interasse di colonne, quote di imposta); si evitano quote duplicate o 'a catena' non controllate perché gli errori si sommano; quote fuori scala mai ammesse salvo indicazione 'NS' (non in scala).",
 "Planimetrie con quote d'asse, disegni di produzione serramenti e mobili, quote d'imposta di solai e coperture.",
 "La quota giusta al posto giusto permette la verifica in cantiere col metro: senza quota, chi esegue 'interpreta' e l'interpretazione costa.",
 "Quotare TUTTO rende la tavola illeggibile; quotare troppo poco rende il disegno ineseguibile: la mediazione è competenza del disegnatore.",
 "Zero costo diretto; errore tipico costoso: quota d'impresa mancante su una trave in carpenteria = trave rifatta da zero.",
 "Il classico contenzioso: serramento quotato 'luce murario -2 cm' senza specificare i due cm totali o per lato: fornitura sbagliata di 2 cm su ogni lato, 40 serramenti da sostituire.",
 "UNI EN ISO 129-1 (quotatura); UNI 11352 (documenti di cantiere, quote).",
 "In cantiere: prima domanda di ogni operaio è 'quanto è?'. Se la risposta non sta sul disegno, la tavola è incompleta."),
s("Scale e formati", "Scale di rappresentazione e formati dei fogli",
 "La scala è il rapporto tra disegno e realtà: edilizia usa soprattutto 1:50 e 1:100 (piante/sezioni), 1:20 o 1:10 (dettagli), 1:200 (schembi/ubicazione); i formati foglio seguono la serie A (A0 841×1189, A1 594×841, A2 420×594, A3 297×420, A4 210×297 mm).",
 "Rapporto di riduzione armonico: ogni formato A è metà di quello precedente, mantenendo le proporzioni (1:√2) così la scala rimane leggibile a ogni ingrandimento/riduzione; la scala si indica nel cartiglio (es. 1:50) e sul disegno si scrive sempre 'in scala' o si quotano le misure reali.",
 "Scelta formato tavola: A1/A0 per tavole di progetto, A3 per dettagli e disegni di produzione, A4 per relazioni.",
 "Formati standardizzati = stampa, archiviazione e consultazione uniformi in tutto il mondo; copisterie e plotter lavorano solo con questi formati.",
 "A scale troppo piccole (1:200 per dettagli) le spessori diventano invisibili: il disegnatore tende a esagerare i spessori 'a mano' creando disegni falsi.",
 "Costo copia A1 circa 3-6 €, plotter interno vs copisteria; archiviazione digitale (PDF/A) azzera il costo di conservazione.",
 "Dettaglio cappotto-serramento eseguito in scala 1:5 su A3: leggibile, quotato, consegnabile direttamente al posatore senza interpretazioni.",
 "UNI EN ISO 5455 (scale); UNI EN ISO 216 / 5457 (formati foglio e disposizione).",
 "Regola: se in scala 1:50 due linee si sovrappongono, servono il dettaglio ingrandito e la quota, non la 'linea più grossa'."),
s("Cartiglio", "Il cartiglio: identificazione della tavola",
 "Il cartiglio è il riquadro identificativo in basso a destra di ogni tavola: titolo, scala, data, disegnatore/verificatore, numero tavola, riferimenti al progetto, loghi, e in edilizia il timbro del professionista abilitato.",
 "Campi obbligatori in genere: denominazione dell'opera, titolo del disegno, numero di tavola (es. 03 di 12), data, scala principale, unità di misura, firme; nella parte esterna spesso tabella delle revisioni (lettera revisione, data, descrizione modifica, chi ha modificato).",
 "Tutte le tavole formali: progetto preliminare, definitivo, esecutivo, as-built (di fine lavori).",
 "Tracciabilità legale: chi ha disegnato, chi ha verificato, quale versione è in cantiere; senza revisioni si rischia di costruire su tavole obsolete.",
 "Cartigli 'creativi' non standard confondono chi riceve la tavola (imprese, uffici tecnici comunali).",
 "Tempo di compilazione irrilevante rispetto al valore di copertura legale che dà.",
 "Nel collaudo di un ponteggio, la verifica della revisione in cantiere (tavola C contro tavola A) ha evitato il montaggio di una versione non aggiornata dell'ancoraggio: differenza di 20 cm nel passo dei tiranti.",
 "Norme di rappresentazione UNI EN ISO 128; usanze di settore e modelli deiordini professionali (CNPI per ingegneri, CNPIA per architetti).",
 "Regole di cantiere: mai lavorare su una tavola senza controllare numero revisione e data nel cartiglio."),
s("Assonometrie e prospettive", "Assonometrie, prospettive e resa del progetto",
 "Mentre le viste ortogonali danno le misure, assonometrie (isometrica, dimetrica) e prospettive (a un/due/tre punti di fuga) danno la comprensione spaziale e comunicativa: servono al cliente, non al posatore.",
 "Assonometrica: assi a 120° tra loro, misure reali lungo gli assi (utile anche per misurare); prospettiva centrale: convergenza verso punti di fuga suorizzonte, scala variabile (non si misura sul disegno); software CAD/BIM genera render fotorealistici da modello 3D.",
 "Presentazioni al cliente, concorsi, permessi (integratione paesaggistica), social e marketing dell'impresa.",
 "Vende il progetto: il cliente non legge le tavole tecniche ma capisce subito una prospettiva; riduce i cambiamenti in corso d'opera (il cliente 'ha visto' la casa).",
 "Il render fotorealistico crea aspettative materiali precise: se poi si usa un materiale diverso (costo), il cliente percepisce un peggioramento anche se il progetto è corretto.",
 "Render interno esterno: da 300-1.500 € a immagine dal renderista freelance; video walkthrough 1.000-5.000 €; molti software BIM includono motori di render base.",
 "Prima/dopo con render in fase di offerta di una ristrutturazione: approvazione del cliente in un incontro solo invece di tre, con zero modifiche in corso d'opera sulla distribuzione.",
 "Nessuna norma cogente sulla resa; coerenza con il progetto definito a tavole (revisioni allineate).",
 "Nel contratto: specificare che render e prospettive sono 'interpretazione grafica' e che fanno fede le tavole quotate."),
s("Disegno manuale", "Il disegno a mano libera: dal righello alla tavoletta",
 "Il disegno manuale resta fondamentale: schizzi di concept, rilevamenti rapidi in cantiere, appunti grafici durante i sopralluoghi; strumenti: matite (gradazioni H/B), squadre, rulloig, carta millimetrata, tavoletta grafica per il digitale a mano libera.",
 "Schizzo proporzionato a mano alzata → ricalco a squadra su carta millimetrata → eventuale scansione e vettorializzazione in CAD; in cantiere: quaderno di rilevamento con misure annotate per ciascun ambiente, con croce di livello (+1,00 m) e quote architravi/spessori.",
 "Rilevamento di immobili esistenti, bozze di concept da discutere col cliente, annotazioni in direzione lavori.",
 "Velocità e pensiero: disegnando a mano il progettista ragiona; molti concept migliori nascono sul quaderno prima ancora di aprire il CAD.",
 "Precisione limitata: uno schizzo non è un documento di gara; il passaggio al CAD serve sempre per la restituzione quotata.",
 "Costo strumentale quasi zero (quaderno + matita + metro laser 40-100 €); valore enorme per la fase preliminare.",
 "Rilevamento di un appartamento anni '60: misure incrociate su due diagonali per vano hanno rivelato un muro non a 90° di 4 cm: senza diagonali il mobilificio avrebbe sbagliato la cassettiera su misura.",
 "Nessuna norma specifica; il rilievo quotato che alimenta il progetto deve rispettare la quotatura UNI EN ISO 129.",
 "Regola di rilevamento: mai meno di 2 misure per definire un punto, e sempre le diagonali dei vani per verificare la squadratura."),
s("Disegno architettonico", "Il disegno architettonico: piante, sezioni, prospetti e loro coerenza",
 "Il set base di un progetto architettonico: planimetrie (distribuzione, quotata), sezioni (altezze, stratigrafie), prospetti (finisage esterni), con gerarchia di tavole dalla scala urbana (1:500) al dettaglio (1:5).",
 "Coerenza obbligatoria tra tavole: la quota in pianta deve coincidere con quella in sezione; le finiture del prospetto devono corrispondere al capitolato; le superfici in planimetria alimentano il computo metrico; ogni tavola riferisce le altre (tav. correlata).",
 "Pratiche edilizie comunali, gare d'appalto, comunicazione con la direzione lavori e le imprese.",
 "Un set coerente elimina il 90% delle richieste di chiarimento (RdC) in cantiere: chi esegue trova tutto, allineato.",
 "La manutenzione dell'allineamento tra tavole è manuale in CAD 2D (in BIM è automatica): ogni modifica va propagata a mano su tutte le tavole.",
 "Set completo appartamento: 15-25 tavole; costo interno o onorario per tavola nella struttura dell'incarico professionale.",
 "Richiesta di chiarimento in cantiere su una scala interna: la sezione quotava alzata 2,80 m, la pianta 2,85 m: disallineamento di copiatura in CAD 2D, risolto con una sola tavola 'di revisione B'.",
 "Linee guida del Ministero per le tavole di progetto (schemi tipo); regolamenti edilizi comunali (contenuti minimi).",
 "Checklist prima di consegnare un set: pianta-sezione-prospetto sullo stesso asse, quote coincidenti, finiture coerenti col capitolato."),
s("Disegno meccanico", "Il disegno meccanico ed elettromeccanico in edilizia",
 "Oltre all'architettura, il progettista edile legge disegni meccanici: carpenterie metalliche, serramenti, opere in acciaio, componenti di impianto (quadri, centrali termiche), perni e staffe di connessione.",
 "Quote funzionali con tolleranze (ISO 2768 per tolleranze generali o quote con deviazioni esplicite: es. 45 +0,2/-0,1); rugosità superficiale (simbolo √ con valore Ra in micron); trattamenti e materiali indicati in nota (es. acciaio S275JR, zincatura a caldo 85 µm); disegno di saldatura con simboli ISO 2553.",
 " carpenterie di solai in acciaio, scale metalliche, strutture di copertura, telai serramenti, supporti impianti.",
 "La tolleranza esplicita evita il 'non entra': il carpentiere sa cosa aspettarsi e cosa consegnare; il collaudo ha un riferimento oggettivo.",
 "Confondere tolleranza dimensionale con tolleranza di posizionamento (GD&T) porta a pezzi buoni scartati o montaggi forzati.",
 "Disegno di produzione di una scala metallica: 400-1.200 € a seconda della complessità; pezzo meccanico singolo molto meno.",
 "Staffa di connessione tra trave acciaio e pilastro: disegno con tolleranze sui fori (+0,5 mm) ha permesso montaggio a secco senza rilavorazione di 120 staffe in un capannone logistico.",
 "UNI EN ISO 2768 (tolleranze generali); UNI EN ISO 1302 (rugosità); UNI EN ISO 2553 (saldature).",
 "Regola: in cantiere NON si 'adatta' mai un pezzo meccanico con la smerigliatrice senza aver avvisato il progettista: la tolleranza violata può essere strutturale."),
s("Rilievo laser scanner", "Il rilievo con laser scanner e fotogrammetria",
 "Il rilievo moderno dell'esistente: scanner laser terrestre (LiDAR) che misura milioni di punti (nuvola di punti) o fotogrammetria da drone/foto, restituiti in piante, sezioni e modelli 3D con precisione millimetrica.",
 "Scansione con target di riferimento, registrazione delle scansioni in un unico sistema di coordinate, pulizia della nuvola, estrazione di sezioni ortogonali e quotate in CAD; scanner terrestre: portata 50-300 m, precisione ±2-3 mm; fotogrammetria: precisione 1-3 volte la dimensione del pixel di volo (cm/dm a seconda dell'altitudine).",
 "Rilievo di fabbricati storici, verifica di deformazioni e saggi, as-built per retrofit, rilievo di facciate con telai e ponteggi difficili.",
 "Velocità e completezza: in giornata si rileva un intero edificio con dettaglio impossibile a mano; la nuvola è archivio permanente misurabile anche anni dopo.",
 "La nuvola di punti non è un disegno: serve la restituzione umana (interpretazione di cosa è muro, arredo, impalcatura); costo strumentale elevato.",
 "Scansione giornaliera servizio: 800-2.500 € a seconda della superficie; drone + fotogrammetria facciate: 500-1.500 €; software di gestione nuvole incluso in molti CAD.",
 "Rilievo laser scanner di una chiesa con volte: restituzione ha scoperto uno spostamento di 12 cm della chiave di volta rispetto ai disegni del '900, decisivo per il progetto di consolidamento.",
 "Riferimento tecnico UNI 11337 per l'informatizzazione (contesto BIM); specifiche IGM per i rilievi di precisione.",
 "Prima di ristrutturare senza disegni: il rilievo scanner paga sempre il suo costo alla prima muratura che 'non era dove sembrava'."),
s("Tavole esecutive", "Le tavole esecutive: il disegno che va in cantiere",
 "Le tavole esecutive traducono il progetto definitivo in istruzioni operative: posizioni, quote, materiali con riferimento al capitolato, dettagli costruttivi, lavorazioni connesse, con la precisione sufficiente a che ogni impresa esegua senza interpretazioni.",
 "Numero tavole per disciplina (architettonico, strutturale, impiantistico) con riferimenti incrociati; ogni tavola esecutiva riporta: lavorazione, quota d'impresa, materiale (richiamo capitolato), dettagli associati; aggiornamento tramite revisioni con tabella delle modifiche.",
 "Cantieri ordinari e grandi opere: sono il documento operativo quotidiano della direzione lavori e delle imprese.",
 "Minimizzano varianti e contenziosi: se è disegnato e quotato, è dovuto; se non è disegnato, l'impresa può legittimamente chiedere economie o eseguire a propria interpretazione.",
 "Produzione onerosa: un set esecutivo completo di una villa può richiedere 100-200 ore di tavolino; sottodimensionare questa fase è l'errore più pagato di tutto il settore.",
 "Set esecutivo medio: 3.000-15.000 € di onorario a seconda della complessità; il risparmio di un set esiguo si ripaga con liti da 10 volte tanto.",
 "Cantiere di una piscina: l'esecutivo quotava la pendenza di 1,5 cm/m verso i skimmer; l'impresa aveva 'sempre fatto 1 cm/m': la tavola ha chiuso la discussione in 5 minuti e la piscina funziona perfettamente.",
 "UNI 11352 (documenti di cantiere); capitolato speciale d'appalto (richiami incrociati).",
 "Il direttore dei lavori consegna in cantiere SOLO tavole con timbro e revisione corrente; le tavole senza firma sono bozze, non documenti."),
s("CAD 2D", "Il disegno CAD 2D: layer, blocchi, coordinate",
 "Il CAD 2D (AutoCAD, DraftSight, LibreCAD, BricsCAD) replica il disegno manuale in digitale: layer per distinguere murature, testi, quote, impianti; blocchi per simboli ripetuti; coordinate assolute/relative per precisione assoluta.",
 "Best practice: layer con convenzione di nome (A-MURI, A-QUOT, I-ELETTR...), blocchi con attributi per i simboli impiantistici, unità in metri o millimetri coerenti nel template, uso di quote associative collegate alla geometria, gestione dei tipi di linea e spessori di penna per la stampa (CTB/STB).",
 "Planimetrie di progetto e as-built, schemi impiantistici, disegni di produzione serramentisti e carpenterie.",
 "Modifica istantanea: cambia la geometria e quote e testi si aggiornano; copia/incolla tra disegni con blocchi standard aziendali; archivio riutilizzabile.",
 "Il disegno 2D non 'capisce' l'oggetto: una parete è 4 linee, non un muro; chiudere un muro sbagliato non aggiorna superfici né computi.",
 "Licenza CAD 2D professionale: 300-1.500 €/anno (AutoCAD ~1.700 €/anno; alternative libere gratuite); formazione base: 2-5 giorni.",
 "Uso dei blocchi finestre con attributi per il tipo di vetro: cambiato l'attributo 'vetro' nel blocco, tutte le finestre identiche si aggiornano insieme e il computo dei serramenti resta coerente.",
 "Nessuna norma sul software; la norma regola il disegno, non lo strumento (UNI EN ISO 128 resta valida sul CAD).",
 "Template aziendale con layer, blocchi e scale preimpostati vale più di qualsiasi corso: chi disegna col template giusto è veloce e coerente."),
s("Errori tipici", "Gli errori tipici del disegno tecnico e come evitarli",
 "Rassegna dei difetti che più spesso generano costi: quote mancanti o doppie, scale sbagliate, layer incoerenti, disallineamenti pianta-sezione, simboli impiantistici non standard, tratteggi dei materiali assenti, revisioni non tracciate.",
 "Controllo qualità di una tavola: checklist (cartiglio completo, scala dichiarata, quote chiuse, sezioni nei punti critici, richiami ai dettagli, tabella revisioni aggiornata); confronto incrociato tra tavole dello stesso asse; verifica finale a occhio 'da distanza' (la tavola si legge componendo?).",
 "Audit di set di tavole prima di gare e consegne, formazione dei disegnatori junior.",
 "Una checklist di 10 punti applicata a ogni tavola elimina la quasi totalità degli errori materiali.",
 "Nessuno: è pura disciplina; il rischio è trascurarla 'perché tanto è urgente'.",
 "Costo del controllo: minuti per tavola; costo tipico di un errore scoperto in cantiere: da centinaia a decine di migliaia di euro.",
 "Audit pre-gara di un set impiantistico: scoperto che le tavole elettriche usavano 3 simboli diversi per la stessa presa: unificati i simboli e il computo quadri ha smesso di avere voci 'a interpretazione'.",
 "Nessuna norma specifica; riferimento alla buona pratica UNI EN ISO 128 e ai manuali d'azienda.",
 "Cultura da instillare nel LLM: la tavola incompleta non è 'quasi finita', è un rischio economico espresso in euro."),
]

README = """# DISEGNO TECNICO MANUALE PACK — Corso di disegno tecnico e rappresentazione

**Facoltà:** FACOLTA_GEOMETRI_PERITI · **Livello:** L1 (base universitaria) · **Schede:** {n}

## Contenuto
Il linguaggio grafico universale delle costruzioni: proiezioni ortogonali (metodo di Monge),
sezioni e spaccati con tratteggi dei materiali, quotatura UNI, scale e formati ISO,
cartigli e revisioni, assonometrie e prospettive, disegno manuale di rilevamento,
disegno architettonico e meccanico (tolleranze e rugosità), rilievo laser scanner,
tavole esecutive, CAD 2D e controllo qualità delle tavole.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi: categoria, nome, descrizione,
  tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: interpretazione e produzione di tavole, comprensione di convenzioni UNI/ISO,
verifica di coerenza tra piante/sezioni/prospetti, dialogo tra progettista e cantiere.
I casi real world sono episodi tipici di contenzioso o buona pratica, non riferimenti a cantieri identificabili.
Le fasce di costo sono indicative (2025) e vanno verificate sul mercato locale.
""".format(n=len(DATA))

COURSE = """corso: "Disegno tecnico e rappresentazione"
facolta: "FACOLTA_GEOMETRI_PERITI"
livello: "L1"
schede: {n}
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
""".format(n=len(DATA))

os.makedirs(os.path.join(ROOT, "schede"), exist_ok=True)
with open(os.path.join(ROOT, "schede", "schede.jsonl"), "w", encoding="utf-8") as f:
    for d in DATA:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
    f.write(README)
with open(os.path.join(ROOT, "COURSE.yaml"), "w", encoding="utf-8") as f:
    f.write(COURSE)
print("OK", len(DATA), "schede")
