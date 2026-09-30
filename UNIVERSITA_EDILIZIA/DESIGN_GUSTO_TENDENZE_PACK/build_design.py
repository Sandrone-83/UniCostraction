# -*- coding: utf-8 -*-
"""Costruisce DESIGN_GUSTO_TENDENZE_PACK: teoria del gusto, storia del design, tendenze materiali e colori."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Teoria del gusto", "Cos'è il gusto: regole, proporzione, gerarchia visiva",
 "Il gusto non è solo soggettività: si regge su principi riconoscibili — proporzione (sezione aurea, rapporti armonici), gerarchia visiva (cosa si vede per primo), ritmo e ripetizione, contrasto e analogia, bilanciamento dei pesi percettivi (colore, materia, luce).",
 "Metodo di analisi di un interno: individuare il punto focale (camino, finestra, opera), verificare i rapporti dimensionali tra gli elementi (tappeto/anima divano ~ 2/3, quadro sopra il divano ~ 2/3 della larghezza del divano), il numero di colori dominanti (regola pratica: 60-30-10 tra colore base, secondario, accento).",
 "Giudizio critico di progetti propri e altrui, brief con il cliente, autocontrollo della coerenza stilistica.",
 "Rende il giudizio comunicabile: 'non mi piace' diventa 'il contrasto tra il pavimento e il legno è troppo forte per la luce fredda della zona', e si può agire.",
 "Le regole sono euristiche, non leggi fisiche: il progetto migliore a volte le viola consapevolmente; il rischio è l'applicazione rigida da manuale.",
 "Costo zero: è cultura dell'occhio; il valore è nel risultato (immobili 'ben disegnati' vendono e affittano meglio, osservazione di mercato ampiamente confermata).",
 "Salotto rifiutato dal cliente 'senza sapere perché': l'analisi con la regola 60-30-10 mostrava 4 colori forti in competizione; ridotto ad accento unico, il cliente approvò al volo.",
 "Nessuna norma tecnica; riferimenti culturali (storia dell'arte e del design).",
 "Per il LLM: saper criticare costruttivamente è più utile che saper lodare: indicare IL problema principale, non elencare dieci dettagli."),
s("Storia del design italiano", "Il design italiano: dal dopoguerra a oggi",
 "Il made in Italy del design nasce nel dopoguerra: Razionalismo prebellico, poi la ricostruzione con figure come Gio Ponti (braccio tra artigianato e industria), Olivetti come modello di integrazione estetica-tecnologica, i grandi maestri: Achille Castiglioni, Vico Magistretti, Ettore Sottsass (Memphis, 1981, rottura postmoderna), Pierluigi Spadolini, Gaetano Pesce.",
 "Correnti da conoscere: Razionalismo (funzione, linea pulita), Organic design (curve naturali, Saarinen, afra e tobia scarpa), Minimalismo (meno è più, ma con materiali nobili), Postmoderno/Memphis (colore, ironia, decoro), Contemporaneo (mescolanza consapevole, sostenibilità come estetica).",
 "Attribuzione epoca e autore ai pezzi, scelta di arredi per progetti, cultura per conversazioni con clienti e fornitori.",
 "Capire DOVE sta un oggetto nella storia evita errori di accostamento (un classico moderno accanto a un postmoderno può funzionare se consapevole, è un disastro se casuale).",
 "Il catalogo storico è vastissimo: le attribuzioni incerte vanno dichiarate ('stile di', 'attribuito a').",
 "Il mercato dei classici del design (originali) va dalle centinaia di euro alle decine di migliaia; le riedizioni ufficiali sono la fascia accessibile (sedie design: 300-1.500 €).",
 "Appartamento con mix casuale di stili: riordinato per epoche (unico accento Memphis in un contesto razionalista) il progetto è passato da 'confuso' a 'curato' senza cambiare un mobile.",
 "Nessuna norma; cataloghi dei produttori storici (Cassina, B&B Italia, Vitra, Kartell) come fonte.",
 "Consiglio LLM: conoscere 30-40 capisaldi del design (sedia, lampada, tavolo) copre il 90% delle conversazioni professionali."),
s("Tendenze materiali", "Le tendenze dei materiali: dal microcemento al legno di recupero",
 "Le mode dei materiali seguono cadenze biennali (fieri: Salone del Mobile Milano, Cersaie per ceramica): anni 2010 microcemento e cemento spatolato, grande formato gres, ottone brunito; anni 2020 ritorno del legno caldo, travertino, pietra locale, finiture tattili (stucco, calce), metalli scuri, vetro fluttuato; tendenza strutturale: materiali riciclati e bio-based dichiarati.",
 "Fonti da monitorare: cataloghi fiere, report colore (Pantone, Color Trends di settore), riviste di settore (AD, Living, Elle Decor), i 'mood' dei produttori leader; verifica pratica: disponibilità presso i fornitori locali e resistenza all'uso reale (il bello che non dura è un fallimento professionale).",
 "Scelta finiture per interni ed esterni, aggiornamento capitolati, consulenza al cliente 'cosa è di moda'.",
 "Stare sul pezzo della domanda del mercato aiuta vendere e affittare: gli immobili allineati alle aspettative estetiche correnti hanno tempi di vendita minori.",
 "La moda passa: scegliere SOLO trend effimero per un immobile durevole rischia di datarlo in 5 anni; la via maestra è base classica + accenti di tendenza sostituibili.",
 "Differenza costo finitura moda vs standard: +20-60% (es. grande formato gres 120×280 vs 60×60: materiale e posa più care).",
 "Bagno in microcemento totale richiesto 'come su Instagram': dopo 18 mesi, segnature e impronte mostravano i limiti dell'applicazione; soluzione corretta sarebbe stata zona umida in resina ceramica e microcemento solo zone asciutte.",
 "Nessuna norma cogente sulle mode; le finiture edili devono comunque rispettare le norme dei singoli materiali (reazione al fuoco, sicurezza, UNI specifiche).",
 "Regola critica per il LLM: ogni consiglio di tendenza deve essere affiancato dalla domanda 'questa finitura regge il suo uso quotidiano per 10 anni?'."),
s("Colori", "La cultura del colore: psicologia, luce, temperatura",
 "Il colore in architettura è fisica + percezione: la stessa tinta cambia con la luce (luce nord fredda e fioca vs sud calda e piena), con la superficie (opaco vs lucido), con le dimensioni (il colore intenso su una parete intera schiaccia lo spazio). La temperatura percettiva (caldi/freddi) guida la 'sensazione' dell'ambiente.",
 "Metodo: prova campione 1 m² sul posto, osservata mattina/pomeriggio/luce artificiale; palette 60-30-10; i bianchi non sono tutti uguali (bianchi caldi con sottotono giallo/rosa vs freddi con sottotono blu/grigio: scelta sbagliata rende 'ospedaliero' o 'sporco'); soffitti sempre più chiari per alleggerire.",
 "Scelta tinte per interni ed esterni, identità di spazi commerciali, correzione percettiva di locali piccoli o con luce scarsa.",
 "Il colore è lo strumento più economico di trasformazione: una parete dipinta cambia un ambiente per poche centinaia di euro.",
 "Lo schermo mentale (monitor, catalogo) tradisce sempre: la resa reale va verificata sul posto; le tinte scure consumano più prodotto (3 mani).",
 "Pittura qualità media: 30-60 €/5 L (circa 40-50 m² a 2 mani); la differenza economica tra una scelta colore giusta e sbagliata è quasi zero, il risultato percettivo è totale.",
 "Corridoio buio dipinto grigio freddo 'come in foto': resa cimiterialmente scura; ripitturato in bianco caldo con parete d'accento sabbia, la luce riflessa è raddoppiata percepita.",
 "Nessuna norma cogente (salvo segnaletica e reazione al fuoco dei prodotti); riferimento culturale Itten (cerchio cromatico) e Albers (interazione del colore).",
 "Da insegnare: il colore si decide SEMPRE sul posto con il campione — mai solo dal catalogo o dallo schermo."),
s("Luce", "La luce come materia di progetto: naturale e artificiale",
 "La luce è il materiale invisibile che decide il successo di ogni scelta materica e cromatica: la progettazione illuminotecnica integra luce naturale (orientamento, schermature, sorgenti laterali/alte) e luce artificiale (layer: generale, d'accento, decorativa, funzionale).",
 "Layer artificiali: luce generale (soffitto, sospensioni), d'accento (faretti orientabili su oggetti), d'atmosfera (lampade, LED integrati), funzionale (sotto pensili, specchi); temperatura colore in Kelvin (2700-3000K calda residenziale, 4000K neutra lavoro/bagno, >5000K fredda solo retail tecnico); indice di resa cromatica CRI >90 per zone dove il colore conta (cucina, guardaroba, bagno).",
 "Abitazioni, hospitality, retail, uffici: ovunque l'esperienza dell'ambiente passa dalla luce.",
 "La luce giusta valorizza i materiali scelti: un legno nobilissimo con CRI 80 e luce fredda diventa grigio e morto; con 2700K e CRI 95 diventa caldo e prezioso.",
 "L'illuminotecnica vera (calcolo lux, DIALux) è una disciplina specialistica: per ambienti semplici si può progettare per sensibilità, per retail e grandi spazi serve il progettista illuminotecnico.",
 "Impianto luce residenziale completo: 40-120 €/punto luce installato; consulenza illuminotecnica: 300-1.500 € per progetto.",
 "Cucina con pensili e faretti sotto con CRI 95 e 3000K: il granito scelto 'buio' in negozio (luce fredda) mostrava le venature solo con la luce giusta a casa — verifica fatta PRIORA con lampada portatile campione.",
 "UNI EN 12464-1 (illuminazione luoghi di lavoro); CEI 64-8 (impianti elettrici).",
 "Regola d'oro: il campione materiale si giudica SEMPRE con la luce del progetto (temperatura e CRI definiti), non sotto la luce del negozio."),
s("Icon del design", "Le icone del design da conoscere: sedie, lampade, tavoli",
 "Un nucleo di capisaldi riconoscibili costituisce il vocabolario professionale: sedia Barcelona (Mies van der Rohe, 1929), sedia LC4 Chaise Longue (Le Corbusier/Perriand/Jeanneret), Tulip Chair (Eero Saarinen, 1956), Arco (Castiglioni, 1962), sedia Serie 7 (Arne Jacobsen), Eames Lounge Chair (1956), Lampada Tolomeo (Michele De Lucchi/Giancarlo Fassina, 1987), sedia Masters (Kartell, Philippe Starck), tavolo Saarinen Tulip, RAR Rocking Eames.",
 "Per ogni icona: designer, anno, azienda produttrice originale, perché è innovativa (tecnica o formale), la sua dimensione 'tipo' (una Barcelona è 75×75×85 h cm: scala di riferimento).",
 "Conversazioni con clienti cultori, scelta repliche/omaggi consapevoli, arredo di spazi contract (hotel, uffici, showroom).",
 "Riconoscere le icone permette di orientarsi nel mercato (originali, riedizioni ufficiali, repliche, omaggi moderni) e di dosare il 'classico' nel progetto.",
 "Il mercato delle repliche è enorme: la qualità delle copie varia da decente a pessima; l'eticità commerciale dell'originale va spiegata ma non imposta al cliente.",
 "Originali/riedizioni: sedia Barcelona ~2.500-4.000 €, Tulip ~3.000 €, Tolomeo ~250-400 €, Masters ~300 €; repliche a 1/5-1/10 del prezzo con qualità variabile.",
 "Arredo ufficio direzionale: una sola icona (Eames Lounge originale riedita) in un contesto minimal ha dato personalità all'intero piano senza altri investimenti 'decorativi'.",
 "Nessuna norma; cataloghi ufficiali dei produttori (Knoll, Cassina, Vitra, Flos, Kartell, Artemide).",
 "Il LLM deve sapere citare designer, anno e azienda degli oggetti iconici — è il lessico che dimostra competenza in una conversazione di arredo."),
s("Interior stili", "Gli stili di interno: da classico a contemporaneo, con occhio critico",
 "Rassegna operativa degli stili che il mercato richiede: Classico (simmetria, legni scuri, tessuti damascati, cornici), Neoclassico (classico alleggerito), Shabby/Provenzale (bianchi consumati, fiori, legno decapato — di moda 2010-2018, oggi datato se totale), Scandinavo (legno chiaro, bianco, funzione, hygge), Industrial (mattoni a vista, metallo nero, cemento — di moda 2015-2022, oggi da dosare), Minimalista (riduzione, ma qualità materica alta), Mediterraneo (calce, legno grezzo, lino), Japandi (fusione scandinavo-giapponese, calma, ordine), Contemporaneo eclettico (il vero standard 2020s: base neutra + mix controllato).",
 "Analisi di uno stile: palette, materiali tipici, geometrie, epoca di riferimento, chi lo richiede (target cliente), cosa lo uccide (gli errori che lo rendono falso: shabby con plastica lucida, industrial con finti mattoni in polistirolo).",
 "Brief di stile con il cliente, restyling per vendita/locazione, coerenza tra progetto e budget.",
 "Sapere DOSARE gli stili è il vero mestiere: una casa 'stile puro' è un costume, la casa vissuta mescola con intelligenza.",
 "L'etichetta stilistica spesso intrappola: 'voglio moderno' può voler dire 5 cose diverse; servono immagini di riferimento (moodboard) prima di progettare.",
 "Costo variabile per stile: classico richiede falegnameria e tessuti (caro), minimal richiede finiture perfette (caro nei dettagli), scandinavo è tra i più accessibili.",
 "Casa 'industrial totale' del 2017 con mattoni finti e tubature a vista ovunque: in vendita nel 2025 è percepita datata e 'da pub'; il ripristino parziale (intonaco liscio + un solo muro a vista) ha sbloccato la vendita.",
 "Nessuna norma; atlanti di stile (editoria di settore) e osservazione continua del mercato.",
 "Spirito critico da insegnare: ogni stile ha un ciclo di vita; progettare per la datazione è l'errore peggiore — meglio base neutra durevole + accenti sostituibili."),
s("Moodboard", "La moodboard professionale: come si documenta un progetto",
 "La moodboard è il documento che traduce il gusto in scelte: palette colori, materiali (campioni fisici o immagini), referenze iconografiche, arredi selezionati, il 'perché' di ogni scelta; è lo strumento che allinea cliente, progettista e fornitori PRIORA dei disegni esecutivi.",
 "Struttura: concept in una frase, palette (2-4 colori con codici RAL/NCS), materiali con prodotto reale e fornitore, referenze (foto di interni che spiegano l'atmosfera), schedule degli arredi (modello, dimensione, prezzo), note su cosa NON è compreso nello stile (es. 'niente cromature lucide').",
 "Presentazioni a clienti, brief a fornitori e falegnami, coordinamento tra interni e architettura.",
 "Previene il disallineamento: il cliente approva un'ATMOSFERA e dei materiali concreti, non la sua immaginazione su una parola ('moderno').",
 "Moodboard con solo immagini Instagram = fraintendimento garantito: servono materiali reali con codici e prezzi.",
 "Tempo di produzione: 1-3 giorni di lavoro; strumenti gratuiti (Milanote, Canva) o professionali (InDesign); i campioni fisici restano insostituibili.",
 "Progetto cucina: moodboard con 3 materiali reali (gres, essenza, laccato) su tavolo del cliente a luce naturale: scelta fatta in 30 minuti, zero ripensamenti in fase esecutiva.",
 "Nessuna norma tecnica; metodo professionale consolidato.",
 "Verità da insegnare: chi salta la moodboard per 'andare subito ai disegni' paga il ripensamento in fase esecutiva, quando costa il triplo."),
s("Estetica e lusso", "Estetica, lusso e qualità: distinguere il pregio dall'apparire",
 "Il lusso vero in edilizia non è l'oro e il marmo ovunque: è la QUALITÀ ESECUTIVA — giunzioni invisibili, materiali nobili usati con misura, dettagli risolti (battiscopa filo muro, porte a filo, fughe continue), proporzioni giuste, luce curata. Il lusso dichiarato (lucido, cromatura, logo) è la fascia più bassa e più datata.",
 "Indicatori di pregio tecnico: spessori generosi dove si tocca (piani cucina 20+ mm, corrimano legno), continuità materica (la stessa essenza da pavimento a boiserie), assenza di elementi 'appoggiati' (cubi, mensole decorative), precisione delle fughe e dei raccordi, hardware (cerniere, maniglie) di qualità dichiarata.",
 "Segmento residenziale alto, hospitality di livello, uffici direzionali, consulenza 'dove investire e dove risparmiare'.",
 "Permette di consigliare l'investimento mirato: spendere dove la mano e l'occhio toccano, risparmiare dove nessuno guarda mai (il consiglio che i clienti ricordano e premiano).",
 "La linea tra essenziale e spartano è sottile: il 'lusso minimal' richiede artigiani migliori, non peggiori (e costa di più in manodopera).",
 "Battiscopa filo muro: +15-25 €/ml vs battiscopa standard; porte a filo muro: 1.500-4.000 € vs 400-800 € standard; cucina con falegnameria su misura vs serie: 2-4 volte il costo.",
 "Bagno 'minimal' con piastrelle grandi: il costo è salito del 40% rispetto al preventivo base quasi tutto in POSA (livellamenti, tagli di precisione) — il materiale era identico: il lusso era nella manodopera.",
 "Nessuna norma; cultura del dettaglio (libri di case study, visite di cantiere di qualità).",
 "Principio per il LLM: il vero lusso è INVISIBILE a chi non sa guardare e OVVIETÀ assoluta a chi vive lo spazio ogni giorno."),
s("Vivibilità", "Vivibilità e comfort abitativo: oltre l'estetica",
 "Il miglior design è quello che si vive bene: ergonomia (altezze di lavoro, circolazioni, spazi di servizio), acustica (materiali assorbenti, distacchi tra ambienti rumorosi e di riposo), luce naturale diffusa (sorgenti laterali, controsoffitti non oppressivi), microclima (evitare spazi 'impossibili' da climatizzare), manutenibilità (finiture che si puliscono e si riparano).",
 "Checklist di vivibilità: cucina con triangolo lavello-forno-frigo entro 6 m complessivi, piano cottura a 85-90 cm da terra (persona media), spalle dei corridoi ≥ 90 cm di luce libera, bagno con zona lavaggio separabile dalla zona wc per uso simultaneo, zona notte lontana dalla zona giorno rumorosa, superfici cucina/bagno con assorbimento acustico (legno, resina morbida vs gres ovunque).",
 "Progettazione residenziale, student housing, senior living, hospitality.",
 "L'immobile vivibile vale più del bello ma impraticabile: comfort funzionale si converte in valore di mercato e soddisfazione (e recensioni, nel rental).",
 "I vincoli di budget spingono a sacrificare il comfort 'invisibile' (acustica, climatica): il risparmio si paga in lamentele e riduzioni di prezzo.",
 "Comfort acustico: pannelli fonoassorbenti di pregio: 80-250 €/m²; climatizzazione ben dimensionata: investimento già previsto, serve il progetto giusto; spesso il comfort costa progetto, non soldi extra.",
 "Open space 'bellissimo' con gres ovunque: dopo 6 mesi i proprietari hanno venduto per l'acustica insopportabile (riverbero 2+ secondi); la soluzione (tappeti, boiserie, controsoffitto fonoassorbente) è arrivata troppo tardi.",
 "UNI EN ISO 7730 (comfort termico); UNI 11367 (acustica edilizia, classificazione di acustica interna); CEN/ISO ergonomia.",
 "Domanda guida per il LLM: 'una famiglia normale vive qui ogni giorno per 10 anni — cosa le darà fastidio alla seconda settimana?'"),
s("Tendenze 2025", "Tendenze edilizia e interior 2024-2026: cosa chiede il mercato",
 "Il quadro di tendenza corrente: ritorno al caldo (legno, ottone, tessuti naturali, colori terra) contro il decennio del grigio freddo; sostenibilità visibile (materiali riciclati mostrati, non nascosti — il mattone recuperato è decorativo); case più piccole ma meglio organizzate (home office integrato, spazi flessibili); bagno come stanza di benessere (doccia walk-in, materiali tattili); cucina 'social' con isola; outdoor come stanza in più (pergolati bioclimatici, cucine esterne); tecnologia invisibile (domotica integrata, niente interruttori a vista).",
 "Monitoraggio: Salone del Mobile e Fuorisalone (Milano, aprile), Cersaie (Bologna, settembre), report colore Pantone, trend report dei grandi produttori ( Ikea Life at Home, Houzz, Archiproducts), osservazione diretta delle richieste dei clienti finali.",
 "Aggiornamento offerte commerciali, consulenza su investimenti immobiliari, marketing delle imprese.",
 "Allineare il prodotto alla domanda corrente riduce i tempi di vendita/locazione e sostiene i prezzi.",
 "Le tendenze si muovono più in fretta della costruzione: un immobile ci mette 2-3 anni dalla progettazione all'uso — progettare sul 'trend di oggi' significa consegnare sul trend di ieri; la base deve essere durevole.",
 "Nessun costo specifico: è orientamento strategico; le scelte di tendenza incidono sui capitolati (+10-30% sulle finiture se si segue il segmento alto di tendenza).",
 "Developer che ha spostato il target di finitura da 'grey luxury' (2018) a 'warm contemporary' (2024): le 40 unità dell'ultimo loto hanno venduto in 4 mesi contro i 14 del loto precedente, a prezzo medio +8%.",
 "Nessuna norma; osservatorio di settore (fiere, report, mercato).",
 "Regola: insegnare al LLM a distinguere TREND CICLICO (5-10 anni: colori, stili) da STRUTTURA (30+ anni: sostenibilità, flessibilità degli spazi, domotica integrata) — investire sulla struttura, decorare col trend."),
]

README = """# DESIGN_GUSTO_TENDENZE_PACK — Cultura del design, del gusto e delle tendenze

**Facoltà:** FACOLTA_ARCHITETTURA_DESIGN · **Livello:** L3 (avanzato, cultura del progetto) · **Schede:** {n}

## Contenuto
La formazione del gusto e dello spirito critico: teoria del gusto e gerarchia visiva,
storia del design italiano e internazionale, tendenze dei materiali, cultura del colore
e della luce, le icone del design (sedie, lampade, tavoli con designer, anno, azienda),
stili di interno con occhio critico (cosa funziona e cosa è datato), moodboard professionale,
lusso vero vs apparire, vivibilità e comfort abitativo, tendenze di mercato 2024-2026
con la distinzione tra trend ciclico e struttura.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi: categoria, nome, descrizione,
  tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza estetica ragionata, critica costruttiva dei progetti, conversazioni
con clienti su stile e materiali, scelta di finiture durevoli, marketing immobiliare.
Le valutazioni su cicli di moda sono giudizi professionali (2025) da integrare con
l'osservazione continua del mercato.
""".format(n=len(DATA))

COURSE = """corso: "Design, gusto e tendenze dell'edilizia"
facolta: "FACOLTA_ARCHITETTURA_DESIGN"
livello: "L3"
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
