# -*- coding: utf-8 -*-
"""COSTRUZIONI_SPECIALI_PACK: tensostrutture, ponti (cenni), opere marittime, prefabbricazione avanzata."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Tensostrutture", "Le tensostrutture: membrana tesa tra gli elementi portanti",
 "Le tensostrutture coprono grandi luci con materiale teso (membrane PVC o PTFE, cavi) ancorato a puntoni, anelli o contropesi: i carichi viaggiano solo per trazione, con sezioni minime e peso estremamente contenuto.",
 "Principi: la forma si trova 'a parametri di equilibrio' (l'architetto strutturale lavora sulla geometria), pretensione che mantiene la rigidità sotto vento e neve, bordi e nodi come zone critiche (cuciture, anelli, ancoraggi); le membrane: PVC-PVDF (economica, 15-25 anni), PTFE rivestito (nobile, 30-50 anni), ETFE (cuscini pneumatici per facciate e coperture trasparenti).",
 "Stadi, tensostrutture per eventi, coperture piscine e centri sportivi, pensiline, coperture industriali leggere.",
 "Il rapporto peso/luce è imbattibile: grandi coperture con fondamenta ridotte e tempi di montaggio rapidissimi.",
 "Le membrane hanno vita utile definita (sostituzione oce ogni 15-30 anni) e sono sensibili a tagli, fuochi dolci e vandalismi.",
 "Costo indicativo: 250-600 €/m² di copertura secondo complessità (ordine di grandezza); la manutenzione è la voce critica.",
 "Tensostruttura su centro sportivo: copertura di 60×90 m in 4 mesi di cantiere; la verifica della pretensione annuale ha mantenuto la forma perfetta dopo 8 anni e due nevicate eccezionali.",
 "Eurocodice 1 (azioni) e prassi per membrane; normativa antincendio delle membrane (reazione al fuoco certificata); specifiche produttori.",
 "Regola: in tensostruttura tutto sta nei dettagli di bordo e ancoraggio: il 90% dei guasti nasce lì."),
s("Coperture leggere", "Gusci, reticolari e coperture leggere a grande luce",
 "Oltre alle membrane, le grandi luci si coprono con gusci sottili (calcestruzzo, acciaio, compositi), reticolari spaziali (nodi tubolari) e pannelli sandwich autoportanti: ogni sistema ha il suo regime di luci e costi.",
 "Gusci: calcestruzzo a doppia curvatura (autoportante per forma, spessori 5-10 cm), acciaio corrugato (lamiere grecate a doppia curvatura); reticolari: tubi acciaio nodi sferici o a guscio, luci 20-100 m; pannelli: sandwich acciaio-PU/PIR o lana, luci fino a 3-4 m, rapidi da posare; il dimensionamento passa per: carichi neve/vento (zone climatiche), deformazioni frecce (L/200-L/300 tipiche), connessioni e controventi.",
 "Capannoni industriali, hangar, palazzetti, coperture di grandi superfici commerciali.",
 "Le coperture leggere riducono il peso permanente e quindi le strutture portanti e le fondazioni: risparmio strutturale a catena.",
 "La tenuta all'acqua delle grandi luci è critica: dilatazioni termiche, condensa e punti singoli (luci, camini) richiedono progetto attento.",
 "Costi indicativi: pannelli sandwich 30-70 €/m², reticolari 80-200 €/m², gusci su progetto; montaggio incluso nel computo.",
 "Capannone con reticolare 40×80: la verifica in fase di progetto del camino passante (solaio forato, anello di tenuta) ha evitato la classica infiltrazione camino che invece è emersa nel capannone 'gemello' progettato senza dettaglio.",
 "Eurocodice 3 (acciaio), Eurocodice 2 (calcestruzzo); normativa neve UNI EN 1991-1-3.",
 "Nelle coperture leggere il diavolo è nei dettagli: ogni foro, ogni attraversamento, ogni giunzione è un futuro punto di infiltrazione se non disegnato."),
s("Ponti cenni", "I ponti: tipologie e cenni di progetto",
 "Il ponte è la struttura per eccellenza: supera un ostacolo con luci variabili; le tipologie principali: travi in c.a. o acciaio (luci 10-50 m), travate reticolari (50-150 m), stralli (100-500 m), arco (60-300 m), sospeso (oltre 500 m); il progetto integra struttura, fondazioni, viabilità e durabilità.",
 "Elementi del progetto: schema statico (semplici, continue, cantilever), azioni (traffico da normativa, vento, sisma, urto, frenata), fondazioni (pozzi, pali, platee secondo terreno e corso d'acqua), durabilità (copriferri, calcestruzzi di classe esposizione), esecutività (cicli costruttivi, varo, centinatura); la sorveglianza e la manutenzione programmata sono parte del progetto (ispezionabilità, passerelle, giunti accessibili).",
 "Opere viarie e pedonali, sopraelevate, passerelle ciclopedonali, viadotti.",
 "Il ponte bene progettato dura un secolo: la durabilità è il vero business case (ponti con manutenzione programmata costano meno dei ponti 'a basso costo' nel ciclo di vita).",
 "Gli errori più costosi: sottovalutazione dei carichi speciali, dettagli non ispezionabili, giunti mal posizionati.",
 "Costi: da migliaia di euro al metro lineare per passerelle a decine di migliaia per viadotti (ordini di grandezza molto variabili).",
 "Passerella pedonale di 40 m: la scelta dell'arco con impalcato sospeso ha liberato il letto del torrente (idraulica) e ridotto le fondazioni; il confronto con la trave continua equivalente ha mostrato un risparmio del 18% complessivo.",
 "Eurocodici strutturali e norme applicative italiane; normativa ponte-specifica e direttive ANAS/RFI per le grandi opere.",
 "Per il LLM: nel ponte ogni disciplina si tocca (struttura, fondazioni, idraulica, viabilità, paesaggio): è il caso studio perfetto dell'integrazione."),
s("Serbatoi", "Serbatoi e opere di contenimento",
 "Serbatoi, vasche e bacini contengono liquidi: il progetto tratta la spinta idrostatica, la tenuta, la pulizia e la sicurezza; materiali: calcestruzzo (getto in opera o prefabbricato), acciaio, GRP (plastica rinforzata).",
 "Principi: spinta idrostatica crescente con la profondità (triangolare sulle pareti), la tenuta di struttura e giunzioni (giunti waterstop in PVC o metallo, malte elastiche), il nastro di galleggiamento? No: galleggianti e venting per i serbati coperti, scale di accesso, scarichi e troppopieni dimensionati (normativa), la verifica antisismica delle vasche piene (massa d'acqua che oscilla - verifica sloshing per grandi bacini).",
 "Acquedotti, serbatoi antincendio, vasche di depurazione, serbatoi industriali, vasche agricole, piscine tecniche.",
 "La tenuta è tutto: un serbatoio che perde è un costo permanente di gestione e un rischio idrogeologico.",
 "Le vasche interrate non ispezionabili degradano invisibilmente: la manutenzione preventiva richiede accessi e botole.",
 "Costi: serbatoio c.a. interrato 500-1.500 €/m³; GRP superficiale 150-400 €/m³ (ordini di grandezza).",
 "Serbatoio antincendio di un'industria: la verifica del troppopieno verso lo scarico di sicurezza (e non verso l'esterno del terreno) ha evitato un allagamento chimico in caso di guasto della galleggiante.",
 "Normativa idraulica (D.Lgs 152/2006); Eurocodice 8 per le vasche in sisma; specifiche settore acquedottistico.",
 "Domande da porre: cosa contiene? chi lo ispeziona e come? cosa succede se trabocca o si rompe? — tre risposte progettano il serbatoio."),
s("Opere marittime", "Le opere marittime: dighe, scafi, pontili",
 "Le opere marittime convivono con l'acqua di mare: dighe foranee e frangiflutti (proteggono i porti), moli e banchine (attracco), pontili e scafi (operatività); il nemico è la forza del mare: onde, moto ondoso, corrosione, sabbia in movimento.",
 "Principi: il moto ondoso si caratterizza per altezza, periodo, direzione (rilevamenti e modelli); le strutture rispondono in rilevato (ciottoli e quadroni in c.a., dissipazione per porosità) o verticali (paratie c.a. posate su cassoni); gli aggradimenti della corrente? No: i sedimenti si muovono (erosione e aggradimento): il progetto senza analisi dei sedimenti crea danni a terzi; la corrosione marina obbliga a copriferri maggiorati, acciai speciali, protezioni catodiche.",
 "Porti turistici, peschecci, difese costiere, banchine industriali, cantieri navali.",
 "Una buona opera marittime protegge un territorio per decenni: il valore è nel servizio continuo (porto operativo, spiaggia preservata).",
 "Il mare risponde in anni, non in giorni: le opere sbagliate degradano lentamente ma inesorabilmente e i danni a terzi (erosione della costa vicina) sono oggetto di contenziosi lunghissimi.",
 "Costi: molto variabili (opere marittime: migliaia di euro al metro lineare); la manutenzione è il 30-50% del costo del ciclo di vita.",
 "Porto turistico: il frangiflutti orientato seguendo l' analisi delle onde dominanti ha mantenuto la calma in banchina con mare forza 7; il porto 'gemello' con orientamento sbagliato richiede chiusura con mare forza 5.",
 "D.M. marina? Riferimento: specifiche tecniche per le opere marittime (direttive MIT), Eurocodice 7 e 8, norme corrosione.",
 "La prima legge dell'ingegneria marittima: rispettare il mare come un carico vivo che cambia — mai combatterlo con la rigidità dove serve la porosità."),
s("Prefabbricazione", "La prefabbricazione industriale avanzata",
 "La prefabbricazione sposta la produzione dal cantiere allo stabilimento: elementi in c.a. (travi, pilastri, lastre), scatolari, pannelli di facciata, moduli completi (volumi); i benefici sono industriali: qualità controllata, tempi rapidi, cantiere pulito; il limite è la rigidità progettuale (l'opera si 'compone' da cataloghi).",
 "Sistemi: strutturale (scheletro precast gettato in stabilimento e assemblato), pannello (facciate e pareti complete con finitura), modulare (volumi chiusi con impianti già montati); le connessioni sono il cuore: giunti a bicchiere, mensole, incollaggi e bullonati con tolleranze millimetriche; il montaggio richiede gru e squadre specializzate; la logistica (trasporti eccezionali) condiziona le dimensioni degli elementi.",
 "Edilizia residenziale di serie, uffici, scuole, ospedali modulari, capannoni.",
 "Il cantiere industriale è più veloce del 30-50% e con scarti ridotti: il tempo è denaro e la qualità di serie batte la posa artigianale su grandi numeri.",
 "Il progetto deve essere 'industriale' da subito: cambiare in corso d'opera costa come ridisegnare la fabbrica.",
 "Costi: elemento precast tipico 100-300 €/m³ posato (ordine di grandezza); il vantaggio cresce con la ripetizione (quantità).",
 "Edificio scolastico con 60% elementi prefabbricati: cantiere di 9 mesi invece di 14, con zero fessurazioni da ritiro e qualità superficiale superiore grazie allo stampo in stabilimento.",
 "Normativa precast (Eurocodice 2 parte precompresso e specifiche UNI); D.M. requisiti energetici (se involucro); specifiche produttori.",
 "La regola: il prefabbricato premia chi progetta per il sistema dall'inizio e punisce chi lo usa come 'scorciatoia' a progetto avviato."),
s("Strutture vetro", "Le strutture in vetro: la trasparenza strutturale",
 "Il vetro strutturale porta carichi: facciate a montanti e traversi, coperture reticolari in vetro, scale e pavimenti calpestabili; il vetro è fragile a urto e a tensioni concentrate: il progetto si gioca sui bordi, i fori e le connessioni.",
 "Principi: il vetro temperato (4-5 volte più resistente, si frantuma in granelli innocui) e stratificato (due lastre + film PVB/SGP che trattiene i frammenti); le connessioni: punteggiato (rotelle metalliche attraverso fori), incollato strutturale (silicone strutturale certificato), profili a contrasto (laminato profilato); il dimensionamento include il carico di pulizia/manutenzione e gli urti accidentali.",
 "Facciate trasparenti, coperture di atri, ponti e passerelle pedonali di pregio, scale interne, balaustre.",
 "La trasparenza strutturale è l'estetica massima: luce e leggerezza impossibili con altri materiali.",
 "Il vetro strutturale non perdona: un difetto di bordo o un foro mal posizionato è una rottura certa a mesi di distanza; la manutenzione (guarnizioni, silicone) è obbligatoria e specialistica.",
 "Costi: vetro strutturale temperato stratificato: 150-400 €/m² (ultra performante di più); il sistema completo di facciata strutturale: 500-1.200 €/m².",
 "Copertura atrio in vetro: la scelta del film SGP (rigido) invece del PVB standard ha permesso lastre più leggere con la stessa sicurezza; dopo 10 anni, zero fratture spontanee contro la media storica del 1% del PVB.",
 "Normativa vetro strutturale (UNI e linee guida nazionali; Eurocodice con documenti applicativi); norma sui prodotti vetro (EN 12150 temperato, EN 14449 stratificato).",
 "Le tre regole del vetro strutturale: bordi lavorati perfetti, fori solo dove il progettista li ha messi, nessuna concentrazione di tensione mai."),
s("Compositi avanzati", "Le strutture composte acciaio-calcestruzzo avanzate",
 "Le strutture miste sfruttano la collaborazione acciaio-calcestruzzo: travi con piattabanda (slim floor), solette collaboranti su lamiera grecata, colonne riempite (CFST: concrete-filled steel tubes); il vantaggio è l'altezza ridotta, la velocità e la resistenza al fuoco migliorata.",
 "Principi: la connessione acciaio-c.a. (connettori a chiodo Nelson, staffe, piegafili) trasferisce gli sforzi di taglio tra i due materiali; le solette collaboranti: lamiera grecata posata su travi acciaio, arature e getto in opera che lavora insieme; le colonne CFST: tubo acciaio riempito di calcestruzzo, eccellenti in sisma e fuoco; i vantaggi in fase costruttiva: impalcato di cantiere (la lamiera è cassaforma), rapidità.",
 "Edifici per uffici, scuole, ospedali, ampliamenti su edifici esistenti (l leggerezza), ponti in acciaio-calcestruzzo.",
 "L' altezza della struttura si riduce del 20-30% rispetto al c.a. puro: su edifici alti significano piani in più o costi di involucro ridotti.",
 "La collaborazione richiede controllo di posa (connettori saldati correttamente, getto senza vuoti): il difetto è nascosto.",
 "Costi: solette collaboranti complete 40-90 €/m²; il risparmio è nei tempi e nell'altezza più che nel solo costo materiale.",
 "Ampliamento di un edificio con solette collaboranti su struttura esistente: il carico aggiuntivo ridotto del 40% rispetto alla soluzione in c.a. ha permesso il rifacimento senza rinforzo delle fondazioni, con risparmio complessivo del 25%.",
 "Eurocodice 4 (strutture composte); norme sui connettori e sulle lamiere grecate collaborative.",
 "Domanda da porsi: 'dove il c.a. puro pesa troppo e l'acciaio puro costa troppo?' — lì vive il composito."),
s("Monitoraggio", "Il monitoraggio delle opere speciali: sensori e ispezioni",
 "Le opere speciali (ponti, tensostrutture, gusci, opere marittime) si affidano al monitoraggio: sensori (estensimetri, accelerometri, celle di carico, inclinometri), ispezioni programmate, prove non distruttive; il dato nel tempo racconta la salute dell'opera.",
 "Strumenti: monitoraggio statico (cedimenti, deformazioni con rilievi periodici), dinamico (vibrazioni, frequenze proprie: il cambio di frequenza segnala danni), innovativo (fibre ottiche distribuite lungo la struttura); la gestione: baseline in costruzione, soglie di allarme, piano di intervento; il costo del monitoraggio è una frazione del costo del crollo o della chiusura imprevista.",
 "Ponti esistenti, opere critiche, edifici monitorati post-sisma, strutture con vincoli assicurativi.",
 "Il monitoraggio trasforma la manutenzione da 'a guasto' a 'previsione': si interviene sul componente giusto prima che ceda.",
 "I sensori senza interpretazione sono numeri morti: serve il professionista che legge e decide.",
 "Costo: monitoraggio ponte medio 10.000-50.000 € iniziale + gestione annua; il confronto: chiusura imprevista di un viadotto: costi sociali enormi.",
 "Viadotto monitorato dopo un sisma: l'accelerometro ha registrato il superamento delle soglie su un appoggio; ispezione mirata entro 48 ore, sostituzione del dispositivo e riapertura in una settimana invece di mesi di verifiche generalizzate.",
 "Linee guida MIT per la classificazione e la sorveglianza dei ponti; norme sui controlli non distruttivi (UNI EN ISO).",
 "L'opera speciale moderna si consegna con il 'fascicolo della salute' come una persona: esami periodici, storia, previsioni."),
]

README = """# COSTRUZIONI_SPECIALI_PACK — Tensostrutture, ponti, opere marittime, prefabbricazione avanzata

**Facoltà:** FACOLTA_INGEGNERIA · **Livello:** L3 · **Schede:** {n}

## Contenuto
Le costruzioni oltre l'edificio ordinario: tensostrutture e membrane, coperture
leggere (gusci, reticolari, pannelli), cenni di progetto dei ponti, serbatoi e
opere di contenimento, opere marittime (dighe, banchine, pontili), prefabbricazione
industriale avanzata, strutture in vetro strutturale, strutture composte
acciaio-calcestruzzo avanzate e il monitoraggio strutturale delle opere speciali.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: cultura strutturale avanzata, dialogo con specialisti, scelta preliminare
di sistemi costruttivi, casi studio di integrazione disciplinare. I costi indicati
sono ordini di grandezza: le opere speciali richiedono sempre computi dedicati.
""".format(n=len(DATA))

COURSE = """corso: "Costruzioni speciali e opere d'ingegneria"
facolta: "FACOLTA_INGEGNERIA"
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
