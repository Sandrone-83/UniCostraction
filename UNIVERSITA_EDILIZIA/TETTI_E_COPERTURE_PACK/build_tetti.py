# -*- coding: utf-8 -*-
"""TETTI_E_COPERTURE_PACK: falda, tegole, guaine, gronde, manutenzione."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Falda", "La copertura a falda: struttura, manto, ventilazione",
 "La copertura a falda (inclinazione minima 15-20° per tegole) protegge l'edificio dalla pioggia con il principio della sovrapposizione: ogni elemento copre il giunto di quello sotto; sotto il manto: struttura portante (capriate, orditure), manto di copertura (tegole, lastre), sottotetto (ventilato o no).",
 "Stratigrafia tipo: capriate o orditure in legno/acciaio, tavellone o pannello portante, guaina di sottocopertura (freno al vapore + barriera), controfascia e calmi? le tegole portanti su listelli (controgronda e gronda), grondaia a bordo; la pendenza: le tegole portano acqua per gravità, ogni tipo ha la sua pendenza minima (tegole marsigliesi 25-30%, portoghesi 20-25%, lastre metalliche 5-15%); la ventilazione del sottotetto: aria che entra in gronda ed esce in colmo (capezzali? camini di ventilazione) evita condensa e caldo estivo.",
 "Case, villette, coperture di pregio, edilizia residenziale con sottotetto abitabile.",
 "La falda ben fatta dura 50+ anni: il manto si sostituisce, la struttura resta.",
 "I punti deboli sono i dettagli: ricorsi (colmo), gronde, attraversamenti (camini, antenne), dove l'acqua si ferma o risale.",
 "Costo copertura a falda completa: 120-250 €/m² (manto e struttura accessoria); la sola sostituzione manto: 60-120 €/m².",
 "Copertura rifatta con sottotetto ventilato: l'estate il sottotetto misura 8-10 °C in meno rispetto alla falda soleggiata; i 40 anni della copertura precedente (non ventilata) erano finiti in 25 per marciume delle orditure.",
 "Normativa tetti (NTC per carichi neve/vento); UNI sulle tegole e sulle costruzioni in legno; regolamenti edilizi (altezze, pendenze).",
 "La prima legge del tetto: l'acqua scende, non sale — ma risale per capillarità e per vento nei dettagli mal chiusi."),
s("Manti", "I manti di copertura: tegole, lastre metalliche, membrane",
 "La scelta del manto coprente definisce vita e aspetto: tegole in laterizio (marsigliesi, portoghesi, coppi: durano 50+ anni, pesanti ~40-50 kg/m²), lastre metalliche (alluminio, zinco-titanio, acciaio: leggere, per pendenze basse, 30-50 anni), membrane bituminose ardesiate (per pendenze basse), scandole di legno (pregio, manutenzione).",
 "Caratteristiche: le tegole laterizio richiedono pendenza e struttura portante; le lastre metalliche coprono con pochi elementi (saldature o giunti a maschio-femmina), eccellenti su geometrie complesse; il zinco-titanio si piega a freddo (gronde e raccordi senza saldature); le membrane ardesiate per falde basse (5-15°) con giunti saldati alla fiamma; tutti i manti vanno fissati contro il vento (ganci, viti, chiodi secondo zona e pendenza).",
 "Coperture residenziali, coperture tecniche, pensiline, campanili e strutture speciali.",
 "Il laterizio è eterno e 'italiano': il metallo è moderno e leggero; la scelta corretta dipende da pendenza, peso, budget e vincoli paesaggistici.",
 "I manti leggeri soffrono il grandine e la dilatazione termica (il metallo 'lavora' con 30 °C di escursione); le tegole rompono se calpestate male.",
 "Costi: tegole laterizio 25-60 €/m² materiale, lastre metalliche 40-120 €/m², membrane 15-35 €/m², posa inclusa nel computo copertura.",
 "Copertura di una villa con lastre di zinco-titanio su falde complesse: le piegature a freddo hanno eliminato giunti e saldature; dopo 12 anni zero manutenzione e un invecchiamento uniforme elegante.",
 "Norme sui prodotti (marcatura CE tegole e lastre); specifiche produttori su fissaggi e pendenze.",
 "Regole d'oro: pendenza ≥ minima del manto, fissaggi contro il vento, dettagli piegati (non siliconati) su gronde e ricorsi."),
s("Guaine", "L'impermeabilizzazione: guaine, membrane liquide, coperture piane",
 "Le coperture piane e le terrazze si impermeabilizzano: guaine bituminose (ardegiate o autoaderenti, con giunti saldati), membrane sintetiche (PVC, TPO, EPDM: saldate a caldo o con nastro), membrane liquide (poliuretaniche, applicate a pennello, senza giunti); la pendenza minima 1-1,5% verso i pluviali è il primo requisito.",
 "Sistemi: la guaina armata sotto il massetto (o sopra), le membrane PVC/TPO saldate ad aria calda (tenuta perfetta, ispezionabili con prova), il liquido per geometrie impossibili; la protezione: la guaina va protetta (massetto, lastricato, ghiaia, verde) dai raggi UV e dai danni meccanici; i pluviali e i pozzetti (sempre almeno due per superficie) dimensionati per la pioggia di progetto.",
 "Terrazze, tetti piani, coperture tecniche, lastrici solari, piscine tecniche, fondazioni orizzontali (impermeabilizzazione).",
 "La copertura piana impermeabilizzata bene dura 25-30 anni e diventa terrazza: spazio guadagnato a parità di costruzione.",
 "È la copertura più delicata: l'acqua ristagnante e i dettagli (salti, camini, paracolpi) concentrano l'80% dei guasti.",
 "Costi: guaina bituminosa 20-40 €/m², PVC/TPO 30-60 €/m², liquide 25-50 €/m², posa inclusa; la protezione: extra.",
 "Terrazza impermeabilizzata con membrana PVC saldata e prova di tenuta in fase di posa: dopo 10 anni e due rifacimenti dei massetti 'gemelli' in bitume, zero infiltrazioni; la prova in cantiere ha pagato tutto.",
 "Norme sui prodotti e la posa (marcatura CE, istruzioni); UNI 11493? No: riferimento: specifiche e linee guida produttori; normativa antincendio delle coperture.",
 "La frase chiave: la copertura piana non deve mai vedere l'acqua ferma: pendenza, drenaggio, prova."),
s("Gronde", "Gronde e pluviali: l'acqua che si porta via",
 "Il sistema di raccolta (gronde per falde, pluviali per piani) dimensiona e convoglia l'acqua piovana verso lo scarico o il recupero; il dimensionamento dipende dalla superficie di raccolta e dalla pioggia intensa di zona.",
 "Regole: le gronde con pendenza 0,5-1% verso i pluviali, i pluviali uno ogni 10-15 m di gronda tipici, le caditoie dimensionate (una ogni 100-150 m² di superficie coperta nelle zone piovose), i pluviali esterni con fissaggi anti-sgrana? anti-sganciamento, lo scarico a 1 metro dal suolo (salpicamento contro i muri) o diretto in rete; il recupero: la prima pioggia (acqua sporca) si scarta, il resto va in cisterna per irrigazione.",
 "Ogni edificio: case, condomini, capannoni, per la gestione dell'acqua piovana.",
 "Il sistema di raccolta ben dimensionato elimina il rischio principale delle coperture: l'acqua che trabocca o ristagna ai bordi.",
 "Le gronde strette e i pluviali sottodimensionati traboccano nei temporali forti: bagnano le facciate e i davanzali.",
 "Costi: gronda in alluminio 15-35 €/m, pluviali 20-50 €/m, il sistema completo di un'abitazione: 1.000-3.000 €.",
 "Villa con gronde rifatte larghe e pluviali dimensionati al nuovo volume ricavato in sottotetto: dopo il temporale 'del secolo', zero traboccamenti; la casa identica del vicino ha bagnato tutti i davanzali del lato ovest.",
 "Nessuna norma cogente specifica; buona pratica edilizia; regole igieniche per gli scarichi.",
 "La verifica rapida in cantiere: il temporale forte è il collaudo del sistema — se l'acqua scende dai pluviali e non dalle gronde, il dimensionamento è giusto."),
s("Camini", "Camini, finestre da tetto e attraversamenti: i punti deboli",
 "Ogni attraversamento della copertura è un potenziale punto di infiltrazione: camini, finestre da tetto (velux e simili), antenne, pannelli solari, lucernari; il dettaglio corretto usa le pezze speciali (lastrine, collari, guaine sagomate) che portano l'acqua sopra il manto e mai dentro.",
 "Dettagli: il camino va 'guainato' fin sopra il manto con fascia di risalita (almeno 25-30 cm sopra il manto), le finestre da tetto con collare integrato alla sottocopertura e pendenza regolare attorno, i fissaggi dei pannelli FV con staffe che non forano il manto (o fori sigillati a regola), i lucernari con spallette alzate; la regola universale: l'acqua deve sempre trovare il percorso continuo sopra gli elementi, mai una 'falda inversa' non protetta.",
 "Coperture con camini e velux (sottotetti abitabili), impianti fotovoltaici su falda, lucernari su coperture piane.",
 "Gli attraversamenti ben dettagliati sono invisibili e secchi per decenni: sono il 20% della copertura e l'80% dei problemi.",
 "Il foro 'sistemato col silicone' nel manto di copertura è un conto alla rovescia: il silicone muore in 5-10 anni.",
 "Costo dettagli: la pezza speciale costa poco (50-200 €), rifare l'interno di una stanza dopo l'infiltrazione costa migliaia.",
 "Sottotetto con 6 velux posati con collari integrati: dopo 8 anni zero infiltrazioni; il sottotetto gemello con finestre 'adattate' dal posatore ha chiuso 4 finestre per infiltrazioni dopo 3 inverni.",
 "Buona pratica costruttiva e istruzioni produttori; le verifiche in collaudo copertura.",
 "La domanda di cantiere: 'da dove passa l'acqua se batte qui?' — se la risposta è il silicone, fermare il lavoro."),
s("Isolamento copertura", "L'isolamento della copertura: sopra, sotto, ventilato",
 "La copertura è la superficie che perde e guadagna più calore (fino al 30% delle dispersioni dell'edificio): si isola con lana o polistirofe sopra la struttura (sotto il manto, falda ventilata), sotto la struttura (controsoffitto, se il sottotetto non serve), o integrato (pannelli isolanti con struttura portante).",
 "Sistemi: il tetto ventilato (il più performante: l'aria che scorre sotto il manto porta via il caldo estivo e la condensa, l'isolante tra le orditure o sopra), il tetto non ventilato (isolante sopra la struttura continua, freno vapore rigoroso), il tetto 'freddo' (sottotetto non isolato, controsoffitto isolato: l'isolamento protegge il piano abitato sottostante); l'isolante: lana di roccia o fibra di legno in falda, XPS o poliuretano dove serve impermeabilità.",
 "Retrofit energetici (conto termico, detrazioni), nuove costruzioni, recupero sottotetti.",
 "Il tetto isolato bene cambia la casa: inverno caldo senza sprechi, estate fresca senza climatizzazione forsennata.",
 "L'isolamento mal posato (ponti termici sulle orditure, freno vapore mancante) condensa e marcisce la struttura in pochi anni.",
 "Costi: isolamento copertura in falda 40-90 €/m²; l'intervento su un 100 m² di copertura: 4.000-9.000 €.",
 "Sottotetto isolato con fibra di legno tra le orditure e 12 cm continui sopra (tetto ventilato): i consumi invernali sono calati del 35%; l'estate il sottotetto resta fresco senza aria condizionata.",
 "Normativa energetica (D.Lgs 192/2005, requisiti); UNI 11484? No: riferimento: prassi e certificazioni isolanti (marcatura CE).",
 "La copertura è il primo posto dove intervenire in un retrofit: rendimento massimo, invasività contenuta."),
s("Manutenzione tetto", "La manutenzione del tetto: ispezioni, pulizie, riparazioni",
 "Il tetto va ispezionato ogni anno (o dopo eventi eccezionali): lo smaltimento del fogliame dalle gronde, il controllo dei fissaggi e delle guaine, la verifica dei pluviali, la pulizia delle zone 'fredde'; la manutenzione programmata costa poco e raddoppia la vita del manto.",
 "Programma: primavera (pulizia gronde e caditoie, controllo guaine e fissaggi, verifica velux e camini), dopo i temporali forti (controllo danni e infiltrazioni), inverno (rimozione neve se carichi eccessivi, mai con strumenti taglienti), la verifica decennale delle guaine (microfessurazioni, alzature); le riparazioni immediate: il piccolo danno riparato subito costa poco, ignorato diventa struttura marcia.",
 "Case, condomini, patrimoni gestiti, capannoni.",
 "Il tetto mantenuto dura il doppio: la manutenzione è la polizza assicurativa più economica dell'edificio.",
 "L'ispezione 'da terra col binocolo' non vede i problemi veri: serve salire (o drone) una volta l'anno.",
 "Costi: ispezione professionale 100-300 €; pulizia gronde 2-5 €/m; riparazioni piccole 100-500 €; il conto del tetto ignorato: migliaia.",
 "Condominio con tetto ispezionato ogni anno: scoperta e riparata una alzatura di guaina da 40 cm per 180 €; il condominio vicino con la stessa guaina non ispezionata ha rifatto tre stanze per infiltrazioni: 12.000 €.",
 "Nessuna norma cogente; prassi assicurative (le polizze richiedono manutenzione).",
 "Da insegnare: il tetto non si vede dalla stanza, per questo si dimentica — finché piove dentro."),
]

README = """# TETTI_E_COPERTURE_PACK — Coperture a falda, manti, guaine, gronde, manutenzione

**Facoltà:** FACOLTA_TECNOLOGIA_E_COSTRUZIONE · **Livello:** L1-L2 · **Schede:** {n}

## Contenuto
Il mondo della copertura tradizionale: falde e pendenze minime dei manti
(tegole, lastre metalliche, membrane), l'impermeabilizzazione delle coperture
piane (guaine, PVC/TPO, membrane liquide), gronde e pluviali dimensionati,
camini e velux come punti deboli, l'isolamento della copertura (tetto ventilato,
freno vapore, retrofit) e la manutenzione programmata annuale.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: artigiani e imprese di copertura, verifica lavori, consulenza su
retrofit, dialogo con manutentori. I dettagli (ricorsi, gronde, attraversamenti)
sono il cuore del corso: l'acqua perde sempre nei dettagli, mai nel campo.
""".format(n=len(DATA))

COURSE = """corso: "Tetti e coperture"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L1-L2"
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
