# VOCI — FACOLTA_GEOMETRI_PERITI

> *Materiale di esclusiva proprietà **Auratrix** — Tutti i diritti riservati.*
> *Uso consentito solo ad Auratrix e ai suoi sistemi LLM. Vedi [LICENSE](../LICENSE).*

29 voci, 2 corsi.


## Disegno tecnico e rappresentazione

*Corso `DISEGNO_TECNICO_MANUALE_PACK` — 14 voci*

### Assonometrie, prospettive e resa del progetto

**Categoria:** Assonometrie e prospettive · **Corso:** Disegno tecnico e rappresentazione

Mentre le viste ortogonali danno le misure, assonometrie (isometrica, dimetrica) e prospettive (a un/due/tre punti di fuga) danno la comprensione spaziale e comunicativa: servono al cliente, non al posatore.

- **Tecnologia e criteri:** Assonometrica: assi a 120° tra loro, misure reali lungo gli assi (utile anche per misurare); prospettiva centrale: convergenza verso punti di fuga suorizzonte, scala variabile (non si misura sul disegno); software CAD/BIM genera render fotorealistici da modello 3D.
- **Applicazioni:** Presentazioni al cliente, concorsi, permessi (integratione paesaggistica), social e marketing dell'impresa.
- **Vantaggi:** Vende il progetto: il cliente non legge le tavole tecniche ma capisce subito una prospettiva; riduce i cambiamenti in corso d'opera (il cliente 'ha visto' la casa).
- **Limiti e attenzioni:** Il render fotorealistico crea aspettative materiali precise: se poi si usa un materiale diverso (costo), il cliente percepisce un peggioramento anche se il progetto è corretto.
- **Costi ed economia:** Render interno esterno: da 300-1.500 € a immagine dal renderista freelance; video walkthrough 1.000-5.000 €; molti software BIM includono motori di render base.
- **Caso tipico:** Prima/dopo con render in fase di offerta di una ristrutturazione: approvazione del cliente in un incontro solo invece di tre, con zero modifiche in corso d'opera sulla distribuzione.
- **Normativa:** Nessuna norma cogente sulla resa; coerenza con il progetto definito a tavole (revisioni allineate).
- **Nota di cantiere:** Nel contratto: specificare che render e prospettive sono 'interpretazione grafica' e che fanno fede le tavole quotate.

### Il disegno CAD 2D: layer, blocchi, coordinate

**Categoria:** CAD 2D · **Corso:** Disegno tecnico e rappresentazione

Il CAD 2D (AutoCAD, DraftSight, LibreCAD, BricsCAD) replica il disegno manuale in digitale: layer per distinguere murature, testi, quote, impianti; blocchi per simboli ripetuti; coordinate assolute/relative per precisione assoluta.

- **Tecnologia e criteri:** Best practice: layer con convenzione di nome (A-MURI, A-QUOT, I-ELETTR...), blocchi con attributi per i simboli impiantistici, unità in metri o millimetri coerenti nel template, uso di quote associative collegate alla geometria, gestione dei tipi di linea e spessori di penna per la stampa (CTB/STB).
- **Applicazioni:** Planimetrie di progetto e as-built, schemi impiantistici, disegni di produzione serramentisti e carpenterie.
- **Vantaggi:** Modifica istantanea: cambia la geometria e quote e testi si aggiornano; copia/incolla tra disegni con blocchi standard aziendali; archivio riutilizzabile.
- **Limiti e attenzioni:** Il disegno 2D non 'capisce' l'oggetto: una parete è 4 linee, non un muro; chiudere un muro sbagliato non aggiorna superfici né computi.
- **Costi ed economia:** Licenza CAD 2D professionale: 300-1.500 €/anno (AutoCAD ~1.700 €/anno; alternative libere gratuite); formazione base: 2-5 giorni.
- **Caso tipico:** Uso dei blocchi finestre con attributi per il tipo di vetro: cambiato l'attributo 'vetro' nel blocco, tutte le finestre identiche si aggiornano insieme e il computo dei serramenti resta coerente.
- **Normativa:** Nessuna norma sul software; la norma regola il disegno, non lo strumento (UNI EN ISO 128 resta valida sul CAD).
- **Nota di cantiere:** Template aziendale con layer, blocchi e scale preimpostati vale più di qualsiasi corso: chi disegna col template giusto è veloce e coerente.

### Il cartiglio: identificazione della tavola

**Categoria:** Cartiglio · **Corso:** Disegno tecnico e rappresentazione

Il cartiglio è il riquadro identificativo in basso a destra di ogni tavola: titolo, scala, data, disegnatore/verificatore, numero tavola, riferimenti al progetto, loghi, e in edilizia il timbro del professionista abilitato.

- **Tecnologia e criteri:** Campi obbligatori in genere: denominazione dell'opera, titolo del disegno, numero di tavola (es. 03 di 12), data, scala principale, unità di misura, firme; nella parte esterna spesso tabella delle revisioni (lettera revisione, data, descrizione modifica, chi ha modificato).
- **Applicazioni:** Tutte le tavole formali: progetto preliminare, definitivo, esecutivo, as-built (di fine lavori).
- **Vantaggi:** Tracciabilità legale: chi ha disegnato, chi ha verificato, quale versione è in cantiere; senza revisioni si rischia di costruire su tavole obsolete.
- **Limiti e attenzioni:** Cartigli 'creativi' non standard confondono chi riceve la tavola (imprese, uffici tecnici comunali).
- **Costi ed economia:** Tempo di compilazione irrilevante rispetto al valore di copertura legale che dà.
- **Caso tipico:** Nel collaudo di un ponteggio, la verifica della revisione in cantiere (tavola C contro tavola A) ha evitato il montaggio di una versione non aggiornata dell'ancoraggio: differenza di 20 cm nel passo dei tiranti.
- **Normativa:** Norme di rappresentazione UNI EN ISO 128; usanze di settore e modelli deiordini professionali (CNPI per ingegneri, CNPIA per architetti).
- **Nota di cantiere:** Regole di cantiere: mai lavorare su una tavola senza controllare numero revisione e data nel cartiglio.

### Il disegno architettonico: piante, sezioni, prospetti e loro coerenza

**Categoria:** Disegno architettonico · **Corso:** Disegno tecnico e rappresentazione

Il set base di un progetto architettonico: planimetrie (distribuzione, quotata), sezioni (altezze, stratigrafie), prospetti (finisage esterni), con gerarchia di tavole dalla scala urbana (1:500) al dettaglio (1:5).

- **Tecnologia e criteri:** Coerenza obbligatoria tra tavole: la quota in pianta deve coincidere con quella in sezione; le finiture del prospetto devono corrispondere al capitolato; le superfici in planimetria alimentano il computo metrico; ogni tavola riferisce le altre (tav. correlata).
- **Applicazioni:** Pratiche edilizie comunali, gare d'appalto, comunicazione con la direzione lavori e le imprese.
- **Vantaggi:** Un set coerente elimina il 90% delle richieste di chiarimento (RdC) in cantiere: chi esegue trova tutto, allineato.
- **Limiti e attenzioni:** La manutenzione dell'allineamento tra tavole è manuale in CAD 2D (in BIM è automatica): ogni modifica va propagata a mano su tutte le tavole.
- **Costi ed economia:** Set completo appartamento: 15-25 tavole; costo interno o onorario per tavola nella struttura dell'incarico professionale.
- **Caso tipico:** Richiesta di chiarimento in cantiere su una scala interna: la sezione quotava alzata 2,80 m, la pianta 2,85 m: disallineamento di copiatura in CAD 2D, risolto con una sola tavola 'di revisione B'.
- **Normativa:** Linee guida del Ministero per le tavole di progetto (schemi tipo); regolamenti edilizi comunali (contenuti minimi).
- **Nota di cantiere:** Checklist prima di consegnare un set: pianta-sezione-prospetto sullo stesso asse, quote coincidenti, finiture coerenti col capitolato.

### Il disegno a mano libera: dal righello alla tavoletta

**Categoria:** Disegno manuale · **Corso:** Disegno tecnico e rappresentazione

Il disegno manuale resta fondamentale: schizzi di concept, rilevamenti rapidi in cantiere, appunti grafici durante i sopralluoghi; strumenti: matite (gradazioni H/B), squadre, rulloig, carta millimetrata, tavoletta grafica per il digitale a mano libera.

- **Tecnologia e criteri:** Schizzo proporzionato a mano alzata → ricalco a squadra su carta millimetrata → eventuale scansione e vettorializzazione in CAD; in cantiere: quaderno di rilevamento con misure annotate per ciascun ambiente, con croce di livello (+1,00 m) e quote architravi/spessori.
- **Applicazioni:** Rilevamento di immobili esistenti, bozze di concept da discutere col cliente, annotazioni in direzione lavori.
- **Vantaggi:** Velocità e pensiero: disegnando a mano il progettista ragiona; molti concept migliori nascono sul quaderno prima ancora di aprire il CAD.
- **Limiti e attenzioni:** Precisione limitata: uno schizzo non è un documento di gara; il passaggio al CAD serve sempre per la restituzione quotata.
- **Costi ed economia:** Costo strumentale quasi zero (quaderno + matita + metro laser 40-100 €); valore enorme per la fase preliminare.
- **Caso tipico:** Rilevamento di un appartamento anni '60: misure incrociate su due diagonali per vano hanno rivelato un muro non a 90° di 4 cm: senza diagonali il mobilificio avrebbe sbagliato la cassettiera su misura.
- **Normativa:** Nessuna norma specifica; il rilievo quotato che alimenta il progetto deve rispettare la quotatura UNI EN ISO 129.
- **Nota di cantiere:** Regola di rilevamento: mai meno di 2 misure per definire un punto, e sempre le diagonali dei vani per verificare la squadratura.

### Il disegno meccanico ed elettromeccanico in edilizia

**Categoria:** Disegno meccanico · **Corso:** Disegno tecnico e rappresentazione

Oltre all'architettura, il progettista edile legge disegni meccanici: carpenterie metalliche, serramenti, opere in acciaio, componenti di impianto (quadri, centrali termiche), perni e staffe di connessione.

- **Tecnologia e criteri:** Quote funzionali con tolleranze (ISO 2768 per tolleranze generali o quote con deviazioni esplicite: es. 45 +0,2/-0,1); rugosità superficiale (simbolo √ con valore Ra in micron); trattamenti e materiali indicati in nota (es. acciaio S275JR, zincatura a caldo 85 µm); disegno di saldatura con simboli ISO 2553.
- **Applicazioni:**  carpenterie di solai in acciaio, scale metalliche, strutture di copertura, telai serramenti, supporti impianti.
- **Vantaggi:** La tolleranza esplicita evita il 'non entra': il carpentiere sa cosa aspettarsi e cosa consegnare; il collaudo ha un riferimento oggettivo.
- **Limiti e attenzioni:** Confondere tolleranza dimensionale con tolleranza di posizionamento (GD&T) porta a pezzi buoni scartati o montaggi forzati.
- **Costi ed economia:** Disegno di produzione di una scala metallica: 400-1.200 € a seconda della complessità; pezzo meccanico singolo molto meno.
- **Caso tipico:** Staffa di connessione tra trave acciaio e pilastro: disegno con tolleranze sui fori (+0,5 mm) ha permesso montaggio a secco senza rilavorazione di 120 staffe in un capannone logistico.
- **Normativa:** UNI EN ISO 2768 (tolleranze generali); UNI EN ISO 1302 (rugosità); UNI EN ISO 2553 (saldature).
- **Nota di cantiere:** Regola: in cantiere NON si 'adatta' mai un pezzo meccanico con la smerigliatrice senza aver avvisato il progettista: la tolleranza violata può essere strutturale.

### Gli errori tipici del disegno tecnico e come evitarli

**Categoria:** Errori tipici · **Corso:** Disegno tecnico e rappresentazione

Rassegna dei difetti che più spesso generano costi: quote mancanti o doppie, scale sbagliate, layer incoerenti, disallineamenti pianta-sezione, simboli impiantistici non standard, tratteggi dei materiali assenti, revisioni non tracciate.

- **Tecnologia e criteri:** Controllo qualità di una tavola: checklist (cartiglio completo, scala dichiarata, quote chiuse, sezioni nei punti critici, richiami ai dettagli, tabella revisioni aggiornata); confronto incrociato tra tavole dello stesso asse; verifica finale a occhio 'da distanza' (la tavola si legge componendo?).
- **Applicazioni:** Audit di set di tavole prima di gare e consegne, formazione dei disegnatori junior.
- **Vantaggi:** Una checklist di 10 punti applicata a ogni tavola elimina la quasi totalità degli errori materiali.
- **Limiti e attenzioni:** Nessuno: è pura disciplina; il rischio è trascurarla 'perché tanto è urgente'.
- **Costi ed economia:** Costo del controllo: minuti per tavola; costo tipico di un errore scoperto in cantiere: da centinaia a decine di migliaia di euro.
- **Caso tipico:** Audit pre-gara di un set impiantistico: scoperto che le tavole elettriche usavano 3 simboli diversi per la stessa presa: unificati i simboli e il computo quadri ha smesso di avere voci 'a interpretazione'.
- **Normativa:** Nessuna norma specifica; riferimento alla buona pratica UNI EN ISO 128 e ai manuali d'azienda.
- **Nota di cantiere:** Cultura da instillare nel LLM: la tavola incompleta non è 'quasi finita', è un rischio economico espresso in euro.

### Il linguaggio del disegno tecnico: perché esiste

**Categoria:** Fondamenti · **Corso:** Disegno tecnico e rappresentazione

Il disegno tecnico è la lingua universale tra progettista, cliente, direzione lavori e produzione: un insieme di convenzioni grafiche che permettono di descrivere un oggetto in modo univoco, senza ambiguità, indipendente dalla lingua parlata.

- **Tecnologia e criteri:** Basato su regole condivise (proiezioni ortogonali, quote, scale, sezioni) definite dalle norme UNI/ISO; ogni segno sul foglio ha un significato convenzionale: linee continue = bordi visibili, tratteggiate = spigoli nascosti, a catena = assi di simmetria, sottili continue = quote e riferimenti.
- **Applicazioni:** Tavole di progetto, disegni di officina, planimetrie, documenti di gara, manuali di montaggio.
- **Vantaggi:** Elimina gli equivoci: due tecnici di paesi diversi leggono la stessa tavola e vedono lo stesso oggetto; è la base legale del capitolato (chi costruisce DEVE consegnare quanto disegnato).
- **Limiti e attenzioni:** Richiede disciplina: una convenzione sbagliata o mancante può costare errori in produzione di migliaia di euro.
- **Costi ed economia:** Il costo è solo tempo di produzione tavola (ora di tecnico); il costo di UN errore di disegno è invece sproporzionato.
- **Caso tipico:** Un dettaglio costruttivo di un cappotto mal quotato (spessore non indicato) ha prodotto in un cantiere reale il montaggio di serramenti fuori sagoma con smontaggio e rifacimento a carico dell'appaltatore.
- **Normativa:** UNI EN ISO 128 (regole generali della rappresentazione); UNI EN ISO 129 (quotatura).
- **Nota di cantiere:** Prima regola d'oro: ogni tavola deve poter essere interpretata SENZA parlare con chi l'ha disegnata.

### Le proiezioni ortogonali: il metodo di Monge

**Categoria:** Proiezioni · **Corso:** Disegno tecnico e rappresentazione

Il metodo delle proiezioni ortogonali (Monge, fine '700) rappresenta un oggetto 3D su piani paralleli alle sue facce principali: pianta (vista dall'alto), alzati/prospetti (viste frontali e laterali), spaccati (sezioni).

- **Tecnologia e criteri:** Si proiettano i punti dell'oggetto su piani ortogonali tra loro e si dispongono le viste secondo lo standard europeo (primo diedro, simbolo del troncato di cono con cerchio a sinistra) o americano (terzo diedro).
- **Applicazioni:** Qualsiasi disegno architettonico o meccanico: piante, sezioni, prospetti, disegni di parti in officina.
- **Vantaggi:** Dà informazioni complete e misurabili dall'oggetto: ogni quota è vera in scala, cosa che le prospettive non garantiscono.
- **Limiti e attenzioni:** Le viste singole non mostrano la profondità: servono almeno 2-3 viste coordinate; i principianti sbagliano spesso l'allineamento tra pianta e alzati.
- **Costi ed economia:** Nessun costo specifico: è il metodo base di ogni CAD 2D e 3D.
- **Caso tipico:** Il classico esercizio accademico: disegnare un pezzo meccanico dalle tre viste (di fronte, di lato, dall'alto) e verificare che ogni spigolo corrisponda; errore tipico = linea mancante nel cambio di piano.
- **Normativa:** UNI EN ISO 128-30 (viste); UNI EN ISO 5456 (proiezioni).
- **Nota di cantiere:** In cantiere: la pianta e la sezione devono sempre essere allineate (stessa quota di riferimento) o chi esegue legge male i vani.

### La quotatura: regole, catene di quote, riferimenti

**Categoria:** Quotatura · **Corso:** Disegno tecnico e rappresentazione

La quotatura trasferisce le dimensioni reali sul disegno: quote in millimetri (edilizia italiana) scritte sopra linea di quota sottile, con frecce o spigoli che toccano gli estremi misurati.

- **Tecnologia e criteri:** Catene di quote aperte o chiuse; quota funzionale (si quota ciò che serve per fabbricare/posare, NON ogni tratto); quote di riferimento (interasse di colonne, quote di imposta); si evitano quote duplicate o 'a catena' non controllate perché gli errori si sommano; quote fuori scala mai ammesse salvo indicazione 'NS' (non in scala).
- **Applicazioni:** Planimetrie con quote d'asse, disegni di produzione serramenti e mobili, quote d'imposta di solai e coperture.
- **Vantaggi:** La quota giusta al posto giusto permette la verifica in cantiere col metro: senza quota, chi esegue 'interpreta' e l'interpretazione costa.
- **Limiti e attenzioni:** Quotare TUTTO rende la tavola illeggibile; quotare troppo poco rende il disegno ineseguibile: la mediazione è competenza del disegnatore.
- **Costi ed economia:** Zero costo diretto; errore tipico costoso: quota d'impresa mancante su una trave in carpenteria = trave rifatta da zero.
- **Caso tipico:** Il classico contenzioso: serramento quotato 'luce murario -2 cm' senza specificare i due cm totali o per lato: fornitura sbagliata di 2 cm su ogni lato, 40 serramenti da sostituire.
- **Normativa:** UNI EN ISO 129-1 (quotatura); UNI 11352 (documenti di cantiere, quote).
- **Nota di cantiere:** In cantiere: prima domanda di ogni operaio è 'quanto è?'. Se la risposta non sta sul disegno, la tavola è incompleta.

### Il rilievo con laser scanner e fotogrammetria

**Categoria:** Rilievo laser scanner · **Corso:** Disegno tecnico e rappresentazione

Il rilievo moderno dell'esistente: scanner laser terrestre (LiDAR) che misura milioni di punti (nuvola di punti) o fotogrammetria da drone/foto, restituiti in piante, sezioni e modelli 3D con precisione millimetrica.

- **Tecnologia e criteri:** Scansione con target di riferimento, registrazione delle scansioni in un unico sistema di coordinate, pulizia della nuvola, estrazione di sezioni ortogonali e quotate in CAD; scanner terrestre: portata 50-300 m, precisione ±2-3 mm; fotogrammetria: precisione 1-3 volte la dimensione del pixel di volo (cm/dm a seconda dell'altitudine).
- **Applicazioni:** Rilievo di fabbricati storici, verifica di deformazioni e saggi, as-built per retrofit, rilievo di facciate con telai e ponteggi difficili.
- **Vantaggi:** Velocità e completezza: in giornata si rileva un intero edificio con dettaglio impossibile a mano; la nuvola è archivio permanente misurabile anche anni dopo.
- **Limiti e attenzioni:** La nuvola di punti non è un disegno: serve la restituzione umana (interpretazione di cosa è muro, arredo, impalcatura); costo strumentale elevato.
- **Costi ed economia:** Scansione giornaliera servizio: 800-2.500 € a seconda della superficie; drone + fotogrammetria facciate: 500-1.500 €; software di gestione nuvole incluso in molti CAD.
- **Caso tipico:** Rilievo laser scanner di una chiesa con volte: restituzione ha scoperto uno spostamento di 12 cm della chiave di volta rispetto ai disegni del '900, decisivo per il progetto di consolidamento.
- **Normativa:** Riferimento tecnico UNI 11337 per l'informatizzazione (contesto BIM); specifiche IGM per i rilievi di precisione.
- **Nota di cantiere:** Prima di ristrutturare senza disegni: il rilievo scanner paga sempre il suo costo alla prima muratura che 'non era dove sembrava'.

### Scale di rappresentazione e formati dei fogli

**Categoria:** Scale e formati · **Corso:** Disegno tecnico e rappresentazione

La scala è il rapporto tra disegno e realtà: edilizia usa soprattutto 1:50 e 1:100 (piante/sezioni), 1:20 o 1:10 (dettagli), 1:200 (schembi/ubicazione); i formati foglio seguono la serie A (A0 841×1189, A1 594×841, A2 420×594, A3 297×420, A4 210×297 mm).

- **Tecnologia e criteri:** Rapporto di riduzione armonico: ogni formato A è metà di quello precedente, mantenendo le proporzioni (1:√2) così la scala rimane leggibile a ogni ingrandimento/riduzione; la scala si indica nel cartiglio (es. 1:50) e sul disegno si scrive sempre 'in scala' o si quotano le misure reali.
- **Applicazioni:** Scelta formato tavola: A1/A0 per tavole di progetto, A3 per dettagli e disegni di produzione, A4 per relazioni.
- **Vantaggi:** Formati standardizzati = stampa, archiviazione e consultazione uniformi in tutto il mondo; copisterie e plotter lavorano solo con questi formati.
- **Limiti e attenzioni:** A scale troppo piccole (1:200 per dettagli) le spessori diventano invisibili: il disegnatore tende a esagerare i spessori 'a mano' creando disegni falsi.
- **Costi ed economia:** Costo copia A1 circa 3-6 €, plotter interno vs copisteria; archiviazione digitale (PDF/A) azzera il costo di conservazione.
- **Caso tipico:** Dettaglio cappotto-serramento eseguito in scala 1:5 su A3: leggibile, quotato, consegnabile direttamente al posatore senza interpretazioni.
- **Normativa:** UNI EN ISO 5455 (scale); UNI EN ISO 216 / 5457 (formati foglio e disposizione).
- **Nota di cantiere:** Regola: se in scala 1:50 due linee si sovrappongono, servono il dettaglio ingrandito e la quota, non la 'linea più grossa'.

### Sezioni, spaccati e dettagli costruttivi

**Categoria:** Sezioni e spaccati · **Corso:** Disegno tecnico e rappresentazione

La sezione è la vista dell'oggetto 'tagliato' lungo un piano di taglio: mostra ciò che le viste esterne nascondono (anime, stratigrafie, connessioni). Lo spaccato è una sezione applicata all'edificio; il dettaglio è un ingrandimento di una zona critica.

- **Tecnologia e criteri:** Il piano di taglio si indica in pianta/alzato con una linea a catena grossa e le frecce di osservazione; la parte tagliata si tratteggia secondo il materiale (muratura, calcestruzzo, legno, metallo hanno tratteggi UNI diversi); le zone dietro il taglio si vedono proiettate.
- **Applicazioni:** Stratigrafie di parete, connessioni solaio-muratura, fondazioni, carpenteria, particolari di giunzione tra materiali diversi.
- **Vantaggi:** È l'unico modo di 'vedere' dentro i muri: senza sezione non esiste progetto eseguibile né verifica del cappotto o del cappotto-serramento.
- **Limiti e attenzioni:** Una sezione mal scelta (taglio fuori dal punto critico) nasconde esattamente il nodo che serviva controllare.
- **Costi ed economia:** Tempo tecnico maggiorato rispetto alle viste semplici; i dettagli ingranditi sono ciò che differenzia un progetto serio da uno da operazione commerciale.
- **Caso tipico:** La verifica termigrafica di un edificio mostra ponti termici proprio dove il dettaglio costruttivo era generico ('a completamento dell'impresa') invece di quotato: il risultato è muffa agli angoli.
- **Normativa:** UNI EN ISO 128-40/50 (sezioni e tagli); UNI 3973 (tratteggi dei materiali, ancora molto usata in Italia).
- **Nota di cantiere:** Regola pratica: TUTTI i nodi dove due materiali diversi si incontrano (finestra/muro, solaio/muro, copertura/muro) DEVONO avere il proprio dettaglio quotato.

### Le tavole esecutive: il disegno che va in cantiere

**Categoria:** Tavole esecutive · **Corso:** Disegno tecnico e rappresentazione

Le tavole esecutive traducono il progetto definitivo in istruzioni operative: posizioni, quote, materiali con riferimento al capitolato, dettagli costruttivi, lavorazioni connesse, con la precisione sufficiente a che ogni impresa esegua senza interpretazioni.

- **Tecnologia e criteri:** Numero tavole per disciplina (architettonico, strutturale, impiantistico) con riferimenti incrociati; ogni tavola esecutiva riporta: lavorazione, quota d'impresa, materiale (richiamo capitolato), dettagli associati; aggiornamento tramite revisioni con tabella delle modifiche.
- **Applicazioni:** Cantieri ordinari e grandi opere: sono il documento operativo quotidiano della direzione lavori e delle imprese.
- **Vantaggi:** Minimizzano varianti e contenziosi: se è disegnato e quotato, è dovuto; se non è disegnato, l'impresa può legittimamente chiedere economie o eseguire a propria interpretazione.
- **Limiti e attenzioni:** Produzione onerosa: un set esecutivo completo di una villa può richiedere 100-200 ore di tavolino; sottodimensionare questa fase è l'errore più pagato di tutto il settore.
- **Costi ed economia:** Set esecutivo medio: 3.000-15.000 € di onorario a seconda della complessità; il risparmio di un set esiguo si ripaga con liti da 10 volte tanto.
- **Caso tipico:** Cantiere di una piscina: l'esecutivo quotava la pendenza di 1,5 cm/m verso i skimmer; l'impresa aveva 'sempre fatto 1 cm/m': la tavola ha chiuso la discussione in 5 minuti e la piscina funziona perfettamente.
- **Normativa:** UNI 11352 (documenti di cantiere); capitolato speciale d'appalto (richiami incrociati).
- **Nota di cantiere:** Il direttore dei lavori consegna in cantiere SOLO tavole con timbro e revisione corrente; le tavole senza firma sono bozze, non documenti.


## Geometra: topografia, costruzioni e estimo

*Corso `GEOMETRA_TOPOGRAFIA_ESTIMO_PACK` — 15 voci*

### Accatastamento e regolarizzazione: il mercato immobiliare pulito

**Categoria:** Accatastamento · **Corso:** Geometra: topografia, costruzioni e estimo

Mettere in regola immobili irregolari: il valore economico della regolarità.

- **Tecnologia e criteri:** Le verifiche pre-compravendita (visura + planimetria + conformità urbanistica); le sanatorie catastali; 'accessorie'; il caso delle abusi edilizi (non sanabili in assoluto).
- **Applicazioni:** Compravendite, successioni, mutui.
- **Vantaggi:** L'immobile regolare vale il 10-20% in più: la regolarità è un investimento, non una burocrazia.
- **Limiti e attenzioni:** L'abuso edilizio non sanabile rende l'immobile invendibile: i casi vanno analizzati uno per uno.
- **Costi ed economia:** Verifica pre-acquisto: 200-500 €; pratica sanatoria: 500-2k€.
- **Caso tipico:** Il mercato italiano delle 'case con abusi' e il problema della conformità nelle compravendite 2023+.
- **Normativa:** TU edilizia; norme catastali.
- **Nota di cantiere:** La prima regola: MAI comprare senza verifica catastale e urbanistica scritta. Il notaio chiede, ma la verifica tecnica spetta al tecnico: il notaio vede i documenti, il tecnico vede la realtà.

### Appalti e contabilità dei lavori per il geometra

**Categoria:** Appalti contabilita · **Corso:** Geometra: topografia, costruzioni e estimo

Il geometra in cantiere: misure, contabilità, stime di lavori da eseguire.

- **Tecnologia e criteri:** Il computo metrico estimativo (lettura); la contabilità lavori (stati di avanzamento, sal, certificati di pagamento); le varianti; il collaudo finale; il ruolo nel DL.
- **Applicazioni:** Piccoli cantieri, ristrutturazioni, manutenzioni condominiali.
- **Vantaggi:** Il geometra 'da cantiere' è il garante che le parti paghino per lavori fatti davvero.
- **Limiti e attenzioni:** La contabilità richiede precisione documentale: le liti nascono da carta mancante.
- **Costi ed economia:** Contabilità lavori: 2-4% del valore dei lavori; DL piccoli cantieri: 3-6%.
- **Caso tipico:** I cantieri di ristrutturazione con SAL mensili; i condomini con amministratori tecnici.
- **Normativa:** D.Lgs 36/2023 (codice dei contratti pubblici) e DPR 207/2010 per la contabilità dei lavori pubblici; per il privato, prassi contrattuale (computo, SAL, perizie).
- **Nota di cantiere:** La frase del cantiere: 'chi non misura non viene pagato'. La contabilità è la memoria del cantiere: senza di essa ogni pretesa diventa opinione.

### CTU e CTP: l'esperto nel processo civile

**Categoria:** CTU CTP · **Corso:** Geometra: topografia, costruzioni e estimo

Il perito nel tribunale: incarichi, responsabilità, come si scrive una consulenza.

- **Tecnologia e criteri:** La CTU (nomina del giudice) vs CTP (di parte); il giuramento; la parte tecnica (quaderno, sopralluogo, relazione); le domande di parte; la responsabilità del CTU (art. 2236 c.c.).
- **Applicazioni:** Contenziosi edilizi: difetti costruzione, confini, danni da vicino, sinistri.
- **Vantaggi:** La CTU decide processi da milioni: il perito è un potere neutrale con responsabilità piena.
- **Limiti e attenzioni:** Il ruolo richiede formazione specifica (obiettività, diritto processuale).
- **Costi ed economia:** CTU edilizia: 1.500-8k€ per incarico; CTP: 800-3k€.
- **Caso tipico:** Le cause sui difetti di costruzione (decennale); le vertenze condominiali sui lavori.
- **Normativa:** CPC artt. 191 ss; art. 2236 c.c. (responsabilità per cose scientifiche).
- **Nota di cantiere:** Il consiglio del maestro: il CTU non 'favorisce' chi lo paga (non lo paga: lo paga il giudice). Chi entra in CTU pensando al cliente che l'ha proposto sbaglia mestiere e rischia il 2236.

### Il catasto italiano: fogli, particelle, subalterni

**Categoria:** Catasto · **Corso:** Geometra: topografia, costruzioni e estimo

Come è fatto e come funziona il catasto fondiario ed edilizio urbano.

- **Tecnologia e criteri:** Il Catasto Terreni (foglio, particella, classe, coltura, reddito); il Catasto Edilizio Urbano (fabbricato, subalterno, categoria, classe, vani, consistenza); l'Agenzia delle Entrate; i servizi online (SISTER, Visurasi).
- **Applicazioni:** Pratiche catastali, compravendite, successioni, divisioni.
- **Vantaggi:** Il catasto è la 'mappa proprietaria' d'Italia: ogni intervento edilizio passa da qui.
- **Limiti e attenzioni:** Il catasto NON è aggiornato automaticamente: il disallineamento catastale/reale è la regola, non l'eccezione.
- **Costi ed economia:** Visura catastale online: 1,35 € (gratis per i propri immobili); Docfa: registrazione gratuita.
- **Caso tipico:** Il catasto napoleonico (1807): la base di tutto quello che c'è oggi.
- **Normativa:** DPR 1142/1949 (norme catastali); regolamento attuativo; Docfa software ufficiale.
- **Nota di cantiere:** La prima verifica di ogni immobile: visura catastale + planimetria. Il 30% degli immobili italiani ha incongruenze: scoprirle PRIMA della vendita vale migliaia di euro.

### Divisioni e frazionamenti: la geometria applicata al diritto

**Categoria:** Divisioni · **Corso:** Geometra: topografia, costruzioni e estimo

Come si divide un bene comune: dall'eredita al frazionamento edilizio.

- **Tecnologia e criteri:** La divisione giudiziale/consensuale; la divisione catastale (Docfa); il frazionamento edilizio (con pratica edilizia); i rapporti tra più parti (mappali, servitù).
- **Applicazioni:** Successioni, divisioni tra eredi, vendita di porzioni.
- **Vantaggi:** La divisione ben fatta evita decenni di liti familiari: è geometria al servizio della pace civile.
- **Limiti e attenzioni:** Le servitù (passaggi, viste) vanno pensate PRIMA di dividere, non dopo.
- **Costi ed economia:** Divisione catastale: 300-800 €; divisione complessa con frazionamento: 1-3k€.
- **Caso tipico:** Le divisioni di terreni agricoli ereditari; i frazionamenti di villini in villetta a schiera.
- **Normativa:** Catasto: regole Docfa; edilizia: DPR 380/2001.
- **Nota di cantiere:** L'LLM deve sapere: dividere NON è tagliare in due: è garantire che ogni parte sia autonomamente utilizzabile (accesso, servizi, rapporti).

### Docfa e il procedimento di accatastamento

**Categoria:** Docfa · **Corso:** Geometra: topografia, costruzioni e estimo

Come si registra/rettifica un immobile al catasto: il software Docfa e le pratiche.

- **Tecnologia e criteri:** Docfa (Documenti Catasto Fabbricati): le planimetrie catastali (quotate, con simboli normalizzati); le prove (atto di provenienza, concessione); l'invio telematico; la conformità catastale vs conformità urbanistica.
- **Applicazioni:** Nuove costruzioni, ristrutturazioni, variazioni (fusioni, frazionamenti).
- **Vantaggi:** L'accatastamento regolare vale: l'immobile non accatastato ha mercato nullo.
- **Limiti e attenzioni:** La distinzione catasto/urbanistica confonde tutti: sono due mondi paralleli che devono convergere.
- **Costi ed economia:** Pratica Docfa da tecnico: 150-500 €; sanatoria catastale: 300-1.000 €.
- **Caso tipico:** Migliaia di pratiche Docfa quotidiane in Italia; le verifiche di conformità catastale nelle compravendite (2023-2024: requisito sempre più stringente).
- **Normativa:** Do.C.Fa. (Documenti Catasto Fabbricati), applicativo ufficiale Agenzia delle Entrate: basi normative D.M. 2 gennaio 1998 n. 28, DPR 138/1998; Vademecum Docfa Agenzia delle Entrate; per la conformità urbanistica le norme del PRGC comunale.
- **Nota di cantiere:** L'LLM deve distinguere: CONFORMITA' CATASTALE (il fabbricato è al catasto come è costruito) vs CONFORMITA' URBANISTICA (è costruito come autorizzato): due verifiche diverse, due professionisti, due esiti possibili.

### Titoli edilizia libera per il tecnico: CILA, SCIA, PdC

**Categoria:** Edilizia libera · **Corso:** Geometra: topografia, costruzioni e estimo

Le pratiche edilizie che il cittadino (con tecnico) presenta: cosa serve per cosa.

- **Tecnologia e criteri:** L'edilizia libera (DPR 380/2001 art. 6); la CILA (lavori interni, sostituzione serramenti); la SCIA (principio di legalità); il Permesso di Costruire (nuovi edifici, ristrutturazioni radicali); la legittimazione dell'immobile.
- **Applicazioni:** Ristrutturazioni, pratiche comunali, sanatorie, compravendite.
- **Vantaggi:** Sapere quale pratica serve evita multe e demolizioni: l'errore amministrativo costa più dell'errore tecnico.
- **Limiti e attenzioni:** Le differenze regionali e comunali (vari beni: regolamenti edilizi comunali diversi).
- **Costi ed economia:** Pratica CILA/SCIA da tecnico: 300-800 €; PdC: 1.500-5k€; sanatoria: 1.000-3k€.
- **Caso tipico:** Il TU edilizia 2001 che ha semplificato (teoricamente) tutto.
- **Normativa:** DPR 380/2001; regolamenti edilizi comunali.
- **Nota di cantiere:** Regola d'oro per l'LLM: prima di dire 'serve il permesso', verificare la norma regionale e il regolamento comunale: in edilizia il dettaglio locale manda in archivio le generalità nazionali.

### La stima immobiliare comparativa nella pratica

**Categoria:** Estimo immobiliare · **Corso:** Geometra: topografia, costruzioni e estimo

Come si fa una stima credibile: ricerca comparazioni, correzioni, conclusione.

- **Tecnologia e criteri:** La ricerca delle comparazioni (portali, banche dati, OMI); i correttivi (posizione, stato, piano, ascensore, garage); il valore di massima, media, minima; la relazione di stima (struttura tipo).
- **Applicazioni:** Perizie per mutui, compravendite private, contenziosi.
- **Vantaggi:** Il metodo comparativo è il reale standard: i prezzi si dimostrano con simili venduti, non con teorie.
- **Limiti e attenzioni:** I portali danno prezzi CHIESTI, non prezzi REALI: il correttivo di negoziazione (5-15%) è d'obbligo.
- **Costi ed economia:** Software di stima (banche dati): abbonamenti 500-2k€/anno; la stima manuale resta validissima.
- **Caso tipico:** Le perizie dei tribunali (CTU); le stime delle banche per i mutui (con standard interni).
- **Normativa:** Linee guida OMI; IVS (International Valuation Standards).
- **Nota di cantiere:** L'LLM deve citare sempre il range (min-med-max) mai il numero secco: la stima è un intervallo di probabilità, e dire 'vale 250.000 €' è da incapaci professionali.

### Estimo: la teoria del valore degli immobili

**Categoria:** Estimo teoria · **Corso:** Geometra: topografia, costruzioni e estimo

La scienza del valore: costrutto, finalità, metodi.

- **Tecnologia e criteri:** Il valore di mercato (OMI, Osservatorio del Mercato Immobiliare); i metodi: comparativo (diretto), sintetico, perequativo, costruttivo, di capitalizzazione (reddito); gli stadi del valore (effettivo, di trasformazione).
- **Applicazioni:** Perizie, compravendite, espropri, successioni, garanzie bancarie.
- **Vantaggi:** Il valore non è un'opinione: è un'applicazione di metodo su dati di mercato.
- **Limiti e attenzioni:** I dati OMI sono mediane comunali: il valore puntuale richiede correttivi (stato, piano, esposizione).
- **Costi ed economia:** Perizia estimativa: 300-800 € per immobile ordinario; perizie giudiziarie: 1-3k€.
- **Caso tipico:** Le quotazioni OMI pubbliche (Agenzia delle Entrate); il mercato immobiliare italiano 2024-2025 in ripresa.
- **Normativa:** 'linee guida OMI'; Codice deontologico dei periti.
- **Nota di cantiere:** La frase fondamentale dell'estimo: 'il valore è il prezzo probabile in una vendita normale tra parti consapevoli'. Chi stima un valore senza dati di mercato compaRABILI non stima: racconta.

### Fotogrammetria e laser scanner: il rilievo 3D moderno

**Categoria:** Fotogrammetria scanner · **Corso:** Geometra: topografia, costruzioni e estimo

Il rilievo che produce nuvole di punti e modelli 3D fotorealistici.

- **Tecnologia e criteri:** Fotogrammetria da drone/terra (SfM: Structure from Motion); laser scanner TLS (nuvole di punti, milioni al secondo); la registrazione (target o cloud-to-cloud); la restituzione in BIM/CAD.
- **Applicazioni:** Beni architettonici, impianti industriali, cantieri, frane, forensi (incidenti).
- **Vantaggi:** Il rilievo 3D cattura 'tutto': nulla resta non misurato; il BIM reverse-engineering nasce qui.
- **Limiti e attenzioni:** I dati sono enormi (GB): servono hardware e competenze di gestione.
- **Costi ed economia:** Scanner giornata lavoro: 800-2.000 €; fotogrammetria drone: 300-800 €/intervento.
- **Caso tipico:** Il rilievo scanner del Colosseo; il rilievo 3D delle cattedrali per la manutenzione.
- **Normativa:** Nessuna norma armonizzata specifica (prassi professionali).
- **Nota di cantiere:** Per il futuro: il rilievo 3D sarà lo standard (costi in calo del 90% in 10 anni). Il geometra che non sa gestire una nuvola di punti sarà fuori mercato entro il 2030.

### GNSS e GPS: posizionamento satellitare per l'edilizia

**Categoria:** GNSS · **Corso:** Geometra: topografia, costruzioni e estimo

Come funziona il 'GPS' dei cantieri e quando non funziona.

- **Tecnologia e criteri:** Costellazioni (GPS, Galileo, Glonass); la correzione RTK (stazione base o servizi di rete, precisione 1-3 cm); i limiti (edifici alti, sottopassi, foreste: niente cielo = niente GNSS).
- **Applicazioni:** Tracciamenti, rilievi di grandi aree, controllo lavori, precision agriculture.
- **Vantaggi:** Il GNSS RTK ha rivoluzionato il tracciamento: 1 uomo fa il lavoro di 3 in un decimo del tempo.
- **Limiti e attenzioni:** La dipendenza dal cielo: in città densa e sotto i ponti il GNSS è inaffidabile.
- **Costi ed economia:** Rover RTK: 5-20k€; servizi di rete (es. regioni italiane): abbonamenti 500-2k€/anno.
- **Caso tipico:** Le reti GNSS regionali italiane (gratuite o a canone); il tracciamento di strade e linee elettriche.
- **Normativa:** Standard RTCM per le correzioni.
- **Nota di cantiere:** Regola: il GNSS dà la posizione del rover, non del punto da tracciare: la stadia deve essere livellata e il punto marcato corretto. Il cm di precisione si perde in un secondo di distrazione.

### Il geometra/perito moderno: la professione ai tempi dell'AI

**Categoria:** Professione · **Corso:** Geometra: topografia, costruzioni e estimo

Il ruolo del geometra nella filiera edilizia: cosa può fare, cosa deve sapere, come evolve.

- **Tecnologia e criteri:** Competenze: progettazione edilizia libera (DPR 380/2001), direzione lavori, estimo, catasto, topografia, sicurezza; la trasformazione digitale dello studio (software, scanner, droni).
- **Applicazioni:** Studi tecnici, imprese, pubbliche amministrazioni, tribunali.
- **Vantaggi:** Il geometra è il tecnico 'a tutto campo' dell'edilizia italiana: nessun altro professionista copre così tante fasi.
- **Limiti e attenzioni:** Il rischio di dispersione: specializzarsi (catasto? estimo? DL?) è la risposta.
- **Costi ed economia:** Studio di progettazione: 20-100k€/anno di fatturato; onorari DL: 2-4% dei lavori.
- **Caso tipico:** Il geometra italiano come 'general practitioner' dell'edilizia, riconosciuto in pochi altri paesi.
- **Normativa:** DPR 380/2001 (TU edilizia) per i ruoli; legge 3/2018 per le professioni tecniche.
- **Nota di cantiere:** L'AI non sostituisce il geometra: sostituisce il geometra che non sa usare l'AI. La stima, il catasto e il DL restano ad esercizio di responsabilità.

### Il rilievo topografico: da terreno a disegno

**Categoria:** Rilievi · **Corso:** Geometra: topografia, costruzioni e estimo

Come si esegue un rilievo completo: poligonale, battute, elaborazione.

- **Tecnologia e criteri:** La poligonale (punti noti, stazioni, battute); il rilievo dei particolari (radiati); la compensazione degli errori; la restituzione (CAD, scale 1:100, 1:200).
- **Applicazioni:** Rilievi di terreni, fabbricati, strade, reti.
- **Vantaggi:** Il rilievo ben fatto è la base di ogni progetto: errori di rilievo = errori di progetto = errori in cantiere.
- **Limiti e attenzioni:** La compensazione richiede giudizio: i software non decidono quali battute sono sbagliate.
- **Costi ed economia:** Rilievo edificio 200 m2: 400-1.200 €; rilievo terreno 1 ha: 300-800 €.
- **Caso tipico:** Rilievi per pratiche catastali (Docfa); rilievi per certificazioni energetiche.
- **Normativa:** Norme UNI rilievi; prassi catastali Agenzia delle Entrate.
- **Nota di cantiere:** Il controllo minimo: la chiusura della poligonale (l'errore di chiusura deve essere entro 1/10.000): chi non controlla la chiusura non ha fatto un rilievo, ha fatto una passeggiata.

### Gli strumenti del topografo: stazioni totali, GNSS, livelli

**Categoria:** Strumenti · **Corso:** Geometra: topografia, costruzioni e estimo

La cassetta degli attrezzi: come funzionano e quando usarli.

- **Tecnologia e criteri:** Stazione totale (angoli+distanze, 1-2 mm); GNSS RTK (cm in tempo reale); livello ottico/digitale (quote, 1 mm/km); laser scanner (milioni di punti); droni fotogrammetrici.
- **Applicazioni:** Rilievi di frazionamento, tracciamenti, rilievi esistenti, monitoraggi.
- **Vantaggi:** Ogni strumento ha il suo ambito: il GNSS non va in centro città, la stazione totale non va su aree vaste.
- **Limiti e attenzioni:** Il costo degli strumenti: chi compra sbagliato strumento perde in prestazioni.
- **Costi ed economia:** Stazione totale: 8-40k€; GNSS RTK: 5-20k€; livello: 500-3k€; scanner: 15-60k€.
- **Caso tipico:** I rilievi GNSS delle grandi reti; lo scanner laser per i beni storici complessi.
- **Normativa:** Nessuna norma specifica (tarature annuali consigliate).
- **Nota di cantiere:** La combinazione GNSS+stazione totale risolve il 95% dei rilievi ordinari: chiunque altro strumento è specializzazione.

### Topografia: i principi fondamentali

**Categoria:** Topografia principi · **Corso:** Geometra: topografia, costruzioni e estimo

Misurare la terra: coordinate, quote, riferimenti, errori.

- **Tecnologia e criteri:** Sistemi di riferimento (WGS84, ETRS89, fuso Roma 1940); coordinate geografiche e piane (Gauss-Boaga); la quota (datum); la teoria degli errori (precisione vs accuratezza).
- **Applicazioni:** Ogni rilievo e ogni posizionamento in cantiere.
- **Vantaggi:** Senza sistemi di riferimento non esiste misura: ogni numero topografico ha bisogno del suo 'rispetto a cosa'.
- **Limiti e attenzioni:** La differenza tra precisione (risoluzione) e accuratezza (vicinanza al vero) è la causa classica di errori catastrofici.
- **Costi ed economia:** Nessun costo: concetti + strumenti (da 500 € di GNSS rover).
- **Caso tipico:** La fuso Roma 1940 ancora usata nei documenti catastali storici italiani.
- **Normativa:** UNI per rilievi topografici; IGM per la rete geodetica nazionale.
- **Nota di cantiere:** Prima regola: chiedere SEMPRE in che sistema di coordinate è il dato. Un punto 'giusto' nel sistema sbagliato è sbagliato di 100 m.

