# -*- coding: utf-8 -*-
"""INFRASTRUTTURE_VIARIE_PACK: strade, pavimentazioni, reti esterne, parcheggi, illuminazione pubblica."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Strade", "Le strade: classificazione e geometria",
 "Le strade si classificano per funzione (autostrade, strade extraurbane principali/secondarie/locali, strade urbane) e ogni classe ha la sua geometria: larghezza carreggiata, raggio minimo delle curve, pendenze longitudinali e trasversali, visibilità.",
 "Parametri chiave: larghezza corsie (3,50-3,75 m in sede extraurbana), banchine, pendenze max (8% tipico montagna, 6-7% pianura), raggio minimo in curva (in funzione della velocità di progetto), sagoma limite (ingombro verticale e laterale); la velocità di progetto guida tutto: strada da 50 km/h ha curve e pendenze diverse da una da 90 km/h.",
 "Progettazione di strade nuove, varianti, accessi, interventi di sicurezza.",
 "La geometria giusta è la prima sicurezza stradale: la maggior parte degli incidenti in curva nasce da raggi sotto standard.",
 "Lo standard costa spazio e terreno: nelle zone montane la geometria piena non è sempre raggiungibile e si accettano compromessi segnalati.",
 "Costi: nuova strada extraurbana: 300-1.000 €/m lineare (ordini di grandezza molto variabili secondo terreno e opere d'arte).",
 "Variante di una strada comunale con raggio in curva portato dallo standard di 30 a 80 km/h: gli incidenti in curva si sono azzerati nei 3 anni successivi (dati comunali).",
 "Normativa geometrica stradale (D.M. 5 novembre 2001 e ss.); norme ANAS e locali.",
 "La prima domanda di progetto: 'a che velocità deve andare qui in sicurezza?' — la risposta decide curve, pendenze e visibilità."),
s("Pavimentazioni", "Le pavimentazioni stradali: flessibili e rigide",
 "Le pavimentazioni sono a struttura flessibile (sottofondi granulari + conglomerati bituminosi) o rigida (cemento alleggerito? No: calcestruzzo, 'bianco'); il dimensionamento usa il traffico (assi equivalenti) e il sottosuolo (CBR).",
 "Flessibile: struttura con strato di fondo (fondazione in pietrisco legato o stabilizzato), base (bituminosa), legante (asfalto), usura (microlastrici o manto d'usura); rigida: lastre in calcestruzzo con giunti, eccellente durata (30-40 anni) ma costosa e rumorosa; manutenzione: flessibile = manutenzione frequente e rapida (microtappeti, rattoppi), rigida = interventi rari ma onerosi; il drenaggio della pavimentazione è metà della vita.",
 "Strade urbane ed extraurbane, parcheggi, piste ciclabili, aree industriali.",
 "La pavimentazione giusta per il traffico giusto: il sovradimensionamento spreca, il sottodimensionamento diventa colata continua di rattoppi.",
 "Il difetto più comune: il drenaggio trascurato: l'acqua che resta nel pacchetto stradale distrugge ogni struttura in pochi inverni.",
 "Costi: asfaltatura nuova 25-60 €/m²; rifacimento completo struttura 60-120 €/m²; il cemento rigido 20-40% in più iniziale.",
 "Strada comunale rifatta con drenaggio longitudinale corretto e manto d'usura a drenaggio rapido: dopo 6 anni e 4 inverni pesanti, zero buche; la strada parallela fatta nello stesso periodo senza drenaggio: rattoppata ogni primavera.",
 "Norme pavimentazioni (specifiche MIT e ANAS; UNI per i conglomerati bituminosi).",
 "La vita di una pavimentazione si decide nel progetto idraulico, non nella scelta del bitume."),
s("Traffico", "L'ingegneria del traffico: segnaletica e sicurezza stradale",
 "L'ingegneria del traffico regola il flusso: segnaletica orizzontale e verticale, semafori, rotatorie, attraversamenti pedonali; la logica è gerarchica: prima la geometria, poi la segnaletica, infine l'illuminazione e i dispositivi di sicurezza passiva (barriere, cuscini? No: guard rail, new jersey).",
 "Strumenti: studi di traffico (conteggi, matrici), capacità delle intersezioni (rotatorie di piccole dimensioni calmano il traffico), segnaletica conforme al Codice della Strada (segnali, marcature, delineatori), sicurezza passiva (barriere di sicurezza per contenere i veicoli in uscita, terminazioni corrette); l'auditoria di sicurezza: la revisione sistematica di un tratto per eliminare gli 'incidenti ripetuti'.",
 "Comuni e province per la gestione viaria, cantieri che impattano sulla viabilità.",
 "L'intervento mirato (rotatoria, attraversamento rialzato, delineatore) costa poco e salva vite: la sicurezza stradale è il miglior investimento pubblico per rapporto costo/beneficio.",
 "La segnaletica eccessiva o incoerente confonde e degrada la sicurezza invece di aumentarla.",
 "Costi: attraversamento pedonale rialzato 3.000-8.000 €; rotatoria 30.000-150.000 €; barriera guardrail 30-60 €/m.",
 "Rotatoria in un incrocio rurale 'pericoloso': gli incidenti con lesioni si sono ridotti del 70% (prima/dopo a 3 anni); il costo dell'opera si è ripagato con i costi sociali evitati in meno di 2 anni.",
 "Codice della Strada (D.Lgs 285/1992); normativa segnaletica (regolamento esecuzione); linee guida sicurezza MIT.",
 "Domanda da tecnico: 'dove accade la maggior parte degli incidenti di questo tratto?' — i dati degli incidenti guidano gli investimenti meglio di ogni opinione."),
s("Marciapiedi", "Marciapiedi, piste ciclabili e la città a 30 km/h",
 "La viabilità dolce è la nuova frontiera urbana: marciapiedi continui e accessibili, piste ciclabili di qualità (protette, continue), zone 30 e isole ambientali; il principio è la gerarchia delle velocità: dove ci sono persone fuori dai veicoli, la velocità scende.",
 "Standard: marciapiedi con larghezze minime (1,50-2,00 m dove possibile), scivoli e rampe per carrozzine e passeggini, piste ciclabili con larghezza minima (1,50 m per senso, da verificare su normativa locale), continuità obbligatoria (un cantiere che interrompe la pista la devia, non la chiude), attraversamenti corti e protetti, superfici drenanti per ridurre acqua e ghiaccio.",
 "Riqualificazioni urbane, mobilità sostenibile, cantieri in centro.",
 "La città a velocità umana vende e vive meglio: commerci, immobili e sicurezza traggono beneficio dai percorsi pedonali di qualità.",
 "La pista ciclabile 'simbolica' (segni sulla carreggiata) non la usa nessuno: la sicurezza percepita decide l'uso reale.",
 "Costi: pista ciclabile protetta 80-200 €/m; marciapiede nuovo 50-120 €/m; la segnaletica orizzontale a costo quasi nullo.",
 "Zona 30 con piste ciclabili continua in una città media: gli spostamenti in bici sono raddoppiati in 2 anni (rilevazione comunale) e gli incidenti ciclo-pedonali sono scesi di un terzo.",
 "Codice della Strada; linee guida MIT sulla mobilità ciclistica; normative accessibilità.",
 "La regola: le persone non usano la pista ciclabile che si interrompe; progettare la continuità prima della larghezza."),
s("Reti esterne", "Le reti tecnologiche esterne: acqua, gas, elettricità, fibra",
 "L'edificio esiste grazie alle reti esterne: acquedotto, fognatura, gas, elettricità, telecomunicazioni (fibra FTTH); ognuna ha il suo tracciato, la sua profondità, le sue distanze di sicurezza reciproche e dai fabbricati.",
 "Regole tipiche: distanze minime tra condotte (es. acqua e fognatura: la fognatura sempre sotto e discosta, per evitare contaminazioni in caso di rottura), profondità di posa (sotto il gelo, tipicamente 60-80 cm per acqua), camere di ispezione sui cambi di direzione delle fognature (raggiungibili!), i pozzetti sifonati? No: i pozzetti di raccolta pluviale, i ripartitori gas, i pozzetti elettrici e le canalizzazioni; il coordinamento (coordinato dello scavo): una sola trincea per tutte le reti quando possibile.",
 "Urbanizzazioni di lotti, ristrutturazioni con aumento di carico (allacci nuovi o potenziati), cantieri.",
 "Le reti ben progettate in fase di urbanizzazione evitano il disastro dello scavo successivo: ogni rete dimenticata è un cantiere aperto sull'asfalto nuovo.",
 "Il sottoservizio 'dimenticato' poi si paga il triplo: la trincea aperta dopo mesi rovina la pavimentazione e la fiducia del cliente.",
 "Costi: allacciamenti completi per una villetta: 3.000-15.000 € a seconda delle distanze e delle reti; l'urbanizzazione completa di reti: quote importanti del computo di lottizzazione.",
 "Lottizzazione con il coordinato di scavo: una sola trincea per tutte le reti ha risparmiato il 30% dei costi di scavo rispetto alle trincee separate previste inizialmente.",
 "Norme tecniche delle reti (UNI per acquedotti, gas UNI 7129 e norme del gas, norme elettriche CEI, specifiche gestori).",
 "La carta delle reti aggiornata è la mappa del tesoro del cantiere: chi la ha evita il 90% delle rotture accidentali."),
s("Parcheggi", "I parcheggi: progettare l'auto senza rovinare il quartiere",
 "Il parcheggio è spazio urbano critico: box interrati (costosi ma salvano superficie), parcheggi a raso (economici ma divorano territorio), parcheggi scambiatori e parcheggi di quartiere; la normativa chiede minimi (posti auto per abitazione/attività) che ogni comune aggiorna (molti li stanno riducendo per favorire la mobilità dolce).",
 "Dimensioni standard: posto auto 2,50×5,00 m (2,40×4,80 minimi in alcune normative), vialetti di scorrimento 6 m a senso unico, 7 m a doppio senso (valori tipici da verificare localmente), rampe con pendenza max 15-17% per garage, altezze minime (2,20-2,40 m), ventilazione forzata per i box chiusi (CO e NOx), l'impermeabilizzazione e il primo soccorso antincendio per gli interrati; il parcheggio verde (superfici drenanti + alberi) mitiga isola di calore.",
 "Residenze, uffici, centri commerciali, cantieri di urbanizzazione.",
 "Il parcheggio interrato libera superficie vendibile o verde: il costo del box si ripaga nel valore dell'immobile.",
 "Il garage fatto male (rampe impossibili, colonne nei posti) genera liti decennali tra condomini.",
 "Costo box interrato: 8.000-20.000 € a posto; parcheggio a raso: 500-2.000 € a posto (massetto e segnaletica).",
 "Palazzina con garage interrato ben proporzionato: le rampe dolci e i posti larghi hanno eliminato le lamentele e i danni auto dei primi anni: il condominio 'gemello' dello stesso costruttore, con garage 'compresso', ha avuto 2 assemblee litigiose e richieste di risarcimento.",
 "Normativa antincendio parcheggi (D.M. 2015); regolamenti edilizi locali (standard parcheggio).",
 "Prova del nove del garage: 'una famiglia normale con bambini e spesa riesce a scendere, parcheggiare e salire senza acrobazie?'"),
s("Illuminazione pubblica", "L'illuminazione pubblica: sicurezza, risparmio, cielo stellato",
 "L'illuminazione pubblica serve la sicurezza stradale e urbana: lampioni con altezze e passi regolari, luce a LED (risparmio 50-70% sui corpi incandescenti), regolazione di flusso (si abbassa a notte fonda), il rispetto del cielo stellato (luce verso il basso, temperatura colore controllata) sempre più richiesto.",
 "Parametri: classe di illuminazione (dalla M1 alla M6 per strade, lux medi e uniformità da normativa UNI 11248), altezza apparecchi (4-10 m), passo (3-5 volte l'altezza), lampade LED 3000-4000K, schermatura per non invadere le finestre; la gestione: impianti con telecontrollo (rilevano guasti e regolano l'intensità) che riducono i costi di esercizio.",
 "Strade, piazze, percorsi pedonali, parcheggi, aree industriali.",
 "L'illuminazione giusta riduce incidenti notturni e degrado percepito: la luce è la prima sicurezza urbana.",
 "L'illuminazione eccessiva o mal orientata costa denaro, inquina (luce verso il cielo) e infastidisce i residenti.",
 "Costi: apparecchio LED pubblico 150-400 €; impianto completo stradale: 1.500-3.000 €/punto luce installato; il risparmio LED: il 50-70% sulla bolletta.",
 "Comune che ha sostituito 1.200 punti luce con LED e telecontrollo: bolletta dimezzata, guasti rilevati in ore invece che settimane, e richieste di intervento azzerate.",
 "UNI 11248 (illuminazione stradale); norme CEI; linee guida risparmio energetico MIT.",
 "Il principio moderno: la luce giusta, dove serve, quando serve, al livello giusto — il resto è spreco."),
s("Viabilità cantiere", "La viabilità in cantiere: il cantiere che non strangola la colla",
 "Il cantiere in strada o in centro deve convivere con la viabilità: il piano di traffico (PdT) definisce deviazioni, restringimenti, segnaletica temporanea, presidi; in Italia la gestione del traffico in deroga è regolata (approvazione della local police/competente).",
 "Elementi: il POS (Piano operativo di sicurezza? No: piano operativo di sicurezza è sicurezza cantieri) — per la viabilità: il progetto della segnaletica temporanea (coni, transenne, pannelli) conforme alle norme, la comunicazione all'ente gestore prima dell'occupazione suolo pubblico (OSU), i cantieri a fasi per mantenere sempre un percorso, la protezione degli spigoli e dei pozzetti durante i getti, la pulizia quotidiana della carreggiata (le gomme sporche portano detriti e incidenti).",
 "Lavori stradali, posa reti, ristrutturazioni su fronte strada.",
 "Il piano traffico ben fatto evita multe, sospensioni e incidenti: il cantiere che rispetta la strada lavora senza intoppi amministrativi.",
 "La 'deroga' non richiesta o il cantiere improvvisato causano sospensioni dei lavori e danni alla reputazione.",
 "Costo: piano e segnaletiva temporanea 1.000-5.000 €; l'OSU: diritti comunali; i ritardi da sospensione: incalcolabili.",
 "Lavori su via principale con piano traffico approvato e cantiere a fasi: zero sospensioni e una segnaletazione che i residenti hanno apprezzato; il cantiere 'gemello' senza piano: sospeso 3 volte in un mese, ritardo complessivo di 6 settimane.",
 "Codice della Strada (artt. 211 e ss. per la circolazione in presenza di lavori); norme segnaletica temporanea; regolamenti OSU comunali.",
 "Regole ferree: mai chiudere una strada senza deroga approvata, mai lasciare materiale oltre i coni, mai lavorare sul fronte strada senza protezione degli operai."),
s("Drenaggio", "Il drenaggio stradale: l'acqua nemica numero uno",
 "L'acqua è il nemico primario delle strade: il drenaggio raccoglie (bordi e cunette), allontana (caditoie e tombini), convoglia (tubi e canalette) e smaltisce (fossi e corpi idrici); il dimensionamento dipende dalla pioggia di progetto e dall'area servita.",
 "Elementi: il profilo trasversale che convoglia verso le cunette (pendenza trasversale 1,5-2,5%), le caditoie a griglia o fessurata (intervalli regolari in rettilineo, ravvicinati in curva dove l'acqua tende all'esterno), le condotte sotto la strada, le soglie e i rigagnoli nelle zone rurali; la manutenzione (pulizia autunnale) è metà dell'efficienza: una caditoia ostruita fa straripare l'acqua sulla carreggiata.",
 "Strade, piazzali, parcheggi, muri di contenimento (i drenaggi dietro i muri salvano le strutture).",
 "Il drenaggio funzionante raddoppia la vita della pavimentazione: l'acqua che resta o penetra è il primo degrado.",
 "I drenaggi sono invisibili finché funzionano: nessuno li manutiene finché non è troppo tardi.",
 "Costo: la componente drenaggio è il 5-10% del costo stradale; la pulizia programmata: irrisoria rispetto ai guasti.",
 "Curva che si allagava ogni temporale forte: aggiunti due pozzetti e una condotta di scarico di 15 m: costo 2.800 €; gli incidenti in quella curva (frequenti sul bagnato) si sono azzerati nell'anno successivo.",
 "Normativa idraulica (legge drenaggi locali); prassi MIT; standard comunali.",
 "La regola del manutentore: le caditoie si puliscono PRIORA dell'autunno, non dopo il primo allagamento."),
s("Manutenzione", "La manutenzione delle infrastrutture viarie: il valore del preservare",
 "La manutenzione programmata delle strade costa una frazzione della ricostruzione: il ciclo preserva (sigillature, microtappeti), mantiene (rattoppi, ripristini), riabilita (risurfacing) e ricostruisce; la logica è intervenire presto, quando il costo è minimo.",
 "Il piano di manutenzione: censimento dello stato (indici di danneggiamento visivi o strumentali), priorità per traffico e stato, cicli di intervento (le sigillature ogni 3-5 anni sulle flessibili evitano l'infiltrazione), monitoraggio dopo gli inverni; il ritorno: ogni euro di manutenzione programmata ne risparmia 4-10 in ricostruzioni (stima ricorrente in letteratura di settore).",
 "Comuni, province, gestori di strade, grandi piazzali industriali.",
 "La strada mantenuta è sicura, dura il doppio e costa meno: la manutenzione è il miglior investimento di bilancio.",
 "La cultura della manutenzione è debole: si preferisce la 'inaugurazione' alla cura — e poi le buche diventano cronaca.",
 "Costi: sigillatura 3-8 €/m²; microtappeto 8-15 €/m²; rifacimento completo 60-120 €/m².",
 "Comune con piano di manutenzione stradale programmata: spesa annua costante e dimezzata nel decennio; il comune vicino con politica 'a guasto': spesa doppia e strade percepite 'distruzione' dai cittadini.",
 "Linee guida MIT sulla manutenzione; norme sui programmi di manutenzione stradale.",
 "La lezione per il LLM: le infrastrutture, come gli edifici, si mantengono — il 'costruire' senza 'mantenere' è il fallimento italiano classico."),
]

README = """# INFRASTRUTTURE_VIARIE_PACK — Strade, reti esterne, parcheggi, illuminazione pubblica

**Facoltà:** FACOLTA_INGEGNERIA · **Livello:** L2 · **Schede:** {n}

## Contenuto
Il mondo dell'urbanizzazione scavo e della viabilità: classificazione e geometria
delle strade, pavimentazioni flessibili e rigide, ingegneria del traffico e
sicurezza stradale, marciapiedi e piste ciclabili, reti tecnologiche esterne
(acqua, gas, elettricità, fibra), progettazione dei parcheggi, illuminazione
pubblica moderna, gestione della viabilità in cantiere, drenaggio stradale e
manutenzione programmata.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: urbanizzazioni, lottizzazioni, dialogo con enti e gestori di reti,
cultura della manutenzione. I valori geometrici e di costo sono tipici (2025)
e vanno verificati con le normative locali vigenti.
""".format(n=len(DATA))

COURSE = """corso: "Infrastrutture viarie e urbanizzazioni"
facolta: "FACOLTA_INGEGNERIA"
livello: "L2"
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
