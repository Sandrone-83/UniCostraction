# -*- coding: utf-8 -*-
"""COSTRUIRE_IN_LEGNO_PACK: strutture in legno, X-Lam, telaio, connessioni, protezione."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Fondamenti", "Perché costruire in legno: il materiale che respira",
 "Il legno è il più antico dei materiali da costruzione e il più moderno: rinnovabile (cresce), sequestra CO2 (un m³ di legno stocca ~1 tonnellata di CO2), leggero (5 volte più del calcestruzzo), isolante naturale, lavorabile in officina; le costruzioni in legno moderno (telaio, X-Lam) sono industriali: precise, rapide, leggere.",
 "Le proprietà: resistenza a trazione e compressione paragonabile all'acciaio a parità di peso, il comportamento sismico eccellente (leggero e duttile), la conducibilità bassa (λ 0,13-0,18 W/mK nel senso della fibra); il difetto storico: sensibilità a fuoco e umidità — oggi gestite con protezioni e dettagli.",
 "Case unifamiliari, edilizia residenziale, scuole, edifici a elevata sostenibilità, sopralzi e ampliamenti.",
 "Il legno ben progettato dura come il calcestruzzo: con la metà del peso, la metà del tempo di cantiere e la CO2 sequestrata.",
 "Il pregiudizio 'il legno brucia e marcisce' è superato tecnicamente ma vivo nel mercato: serve comunicazione e dettagli corretti.",
 "Costo struttura in legno: 250-450 €/m² di superficie (ordini di grandezza); il gap si chiude nei tempi e nei consumi energetici.",
 "Casa in X-Lam di 180 m²: cantiere di 4 mesi contro i 10 della muratura equivalente; i consumi invernali misurati sono un terzo inferiori alla casa di confine in calcestruzzo.",
 "NTC (Eurocodice 5 in Italia); UNI EN 1995 (progettazione legno); marcatura CE dei prodotti strutturali.",
 "La prima battaglia del progettista in legno è culturale: il cliente chiede 'sicurezza contro fuoco e umidità' — le risposte esistono e sono normate."),
s("X-Lam", "L'X-Lam (CLT): il legno che fa da muro e da solaio",
 "L'X-Lam (cross laminated timber) è il pannello di legno incrociato: listelli sovrapposti a strati incrociati (3-7 strati), incollati, che danno un pannello bidirezionale: porta carichi nelle due direzioni, fa pareti portanti, solai e coperture; è la 'lastra di legno' che ha rivoluzionato l'edilizia in legno.",
 "Produzione: pannelli da 3 a 9 strati, spessori 60-300 mm, formati fino a 3×12 m; le pareti X-Lam portano verticalmente e orizzontalmente (pannelli a disco); i solai in X-Lam lavorano a piastra o su travi; le connessioni: viti, piastre metalliche e chiodi speciali che uniscono i pannelli (il 'nodo' è il cuore della struttura); la finitura naturale interna (il legno a vista) è un valore estetico immediato.",
 "Edifici residenziali multi-piano, scuole, uffici, edilizia con struttura a vista.",
 "Il cantiere X-Lam è un cantiere industriale: i pannelli arrivano tagliati, forati e numerati, si montano in giorni con gru e squadre piccole.",
 "Il costo al metro quadro è più alto della muratura tradizionale (ordine +20-40%); il gap si recupera in tempi, precisione e consumi.",
 "Costi: pannello X-Lam 40-90 €/m² (spessori standard); struttura completa 250-450 €/m².",
 "Edificio scolastico in X-Lam a tre piani: montaggio della struttura in 3 settimane; il legno a vista nelle aule ha migliorato la percezione dello spazio e la qualità dell'ambiente dichiarata da studenti e insegnanti.",
 "Eurocodice 5 / NTC; marcatura CE EN 13986 (X-Lam); specifiche produttori (hub? no: Holz, Stora Enso,Mayr-Melnhof come riferimenti europei).",
 "La regola: l'X-Lam si progetta CON il produttore (sistemi, connessioni, trasporti): il modello 3D nasce già costruibile."),
s("Telaio", "Il telaio in legno: travi, pilastri e la costruzione tradizionale",
 "Il telaio in legno (platform framing, balloon) è il sistema a intelaiatura: telai di travi e montanti riempiti di pannelli (OSB, fibra, laterizio leggero); è il sistema più diffuso al mondo (USA, Scandinavia) e il più economico in legno.",
 "Costruzione: il telaio poggia sul solaio interrato o su fondazioni, i montanti verticali (sezione 45×95-145 mm tipiche) portano i carichi, i pannelli di tamponamento (OSB 12-18 mm) irrigidiscono contro il vento e il sisma; i ritocchi? No: i nodi: angolari, piastre e chiodi; il tamponamento termico: lana minerale o fibra di legno tra i montanti + lastra interna; la posa è artigianale ma veloce, con tolleranze da carpenteria.",
 "Villette, case unifamiliari, piccoli edifici residenziali, sopralzi leggeri.",
 "Il telaio è il legno più accessibile: costi contenuti, posa con squadre locali, adattabilità totale alla geometria.",
 "La precisione artigianale è il limite: il telaio mal posato (fuori squadra, pannelli storti) perde le prestazioni teoriche.",
 "Costi: struttura telaio 180-350 €/m²; la posa richiede carpenteria qualificata.",
 "Sopralzo in telaio leggero su edificio esistente: il peso ridotto del 70% ha evitato il rinforzo della struttura esistente; i tempi di cantiere sono stati un terzo della soluzione in acciaio-valutata.",
 "Eurocodice 5; norme sulle costruzioni in legno (UNI); marcatura CE pannelli OSB (EN 300).",
 "Il telaio vive di precisione: il montante dritto e il pannello ben fissato valgono più di ogni altra cosa."),
s("Connessioni", "Le connessioni in legno: dove le strutture si incontrano",
 "Nel legno tutto avviene nelle connessioni: il legno è anisotropo (forte nella fibra, debole traverso) e le giunzioni concentrano gli sforzi; le connessioni moderne usano viti filettate, piastelle, angolari metallici, chiodi speciali, incastri tradizionali; la regola: la connessione è progettata, mai improvvisata.",
 "Tipi: viti e chiodi (a taglio, precaricati), piastine e angolari (collegamenti a trazione), incastri e coda di rondine (tradizione), connettori a disco (Holz) per giunzioni tra elementi; i problemi: il legno si asciuga e si muove (i fissaggi devono permettere il movimento senza allentarsi), la corrosione dei metalli in ambiente umido (acciaio zincato o inox), il fuoco (le connessioni vanno protette come gli elementi).",
 "Ogni struttura in legno: telai, X-Lam, coperture, capriate.",
 "La connessione giusta è invisibile e dura quanto la struttura: i collassi del legno avvengono quasi sempre nei nodi, non negli elementi.",
 "La connessione 'a occhio' del carpentiere tradizionale è il rischio maggiore in cantiere: ogni giunzione va disegnata.",
 "Costo delle connessioni: 10-20% del costo strutturale; il risparmio sulle connessioni è il peggior risparmio possibile.",
 "Verifica post-tempesta di un capannone in legno: tutti gli elementi integri, caduto per il distacco di una piastra mal fissata con viti troppo corte: la struttura era a posto, il nodo no.",
 "Eurocodice 5 (capo connessioni); ETA dei sistemi di fissaggio; marcatura CE viti strutturali (EN 14592).",
 "La regola d'oro: in cantiere, ogni connessione deve corrispondere a un disegno; se non c'è il disegno, non si fa."),
s("Fuoco", "Il legno e il fuoco: la protezione che funziona",
 "Il legno brucia in superficie ma ha un superpotere: carbonizza a velocità nota (0,5-0,7 mm/min) e il carbone isolante protegge il cuoro sano: una sezione in legno dimensionata 'al fuoco' mantiene la resistenza più a lungo di un acciaio non protetto (che collassa a 500 °C).",
 "Protezione: il dimensionamento 'al fuoco' aumenta le sezioni (la carbonizzazione consuma il coprifuoco), i rivestimenti (intonaci, lastre, vernici intumescenti) rallentano la carbonizzazione, i nodi vanno protetti (il punto debole), le grandi superfici X-Lam carbonizzano in modo prevedibile e certificato; la reazione al fuoco (superficiale) si migliora con trattamenti ignifughi (classe C-s2,d0 o migliore).",
 "Ogni edificio in legno: residenziale, pubblico, industriale.",
 "Il legno non è più 'il materiale che brucia' ma 'il materiale che resiste al fuoco in modo calcolabile': il grattacielo in legno (18 piani, Mjøstårnet in Norvegia) esiste e ha superato le verifiche al fuoco.",
 "La comunicazione resta difficile: dire 'il legno resiste al fuoco' senza spiegare il meccanismo non convince nessuno.",
 "Costo protezione: il dimensionamento al fuoco è già nel progetto; i rivestimenti aggiungono 10-30 €/m² dove richiesti.",
 "Ufficio in X-Lam con pareti a vista trattate: la certificazione REI 60 ottenuta con il calcolo della carbonizzazione, senza intonaci; il cliente ha accettato il legno 'perché il progettista ha spiegato il fuoco'.",
 "Eurocodice 5 parte fuoco; UNI EN 13501 (classi); normativa prevenzione incendi.",
 "La formula da insegnare: 'il legno brucia il suo coprifuoco, l'acciaio cede improvvisamente: il legno al fuoco è prevedibile, l'acciaio no (se non protetto)'."),
s("Umidità", "Il legno e l'umidità: protezione dalla pioggia e dalla condensa",
 "L'umidità è il nemico silenzioso del legno: gonfia, ritrae (fino all'8% in larghezza), marcisce ai ristagni; la protezione è nei dettagli: il legno strutturale resta in classe di umidità 1-2 (interno protetto o sotto copertura), le basi stanno isolate dal suolo (zoccolo in calcestruzzo, piede d'appoggio), i dettagli scolano l'acqua (gocciolatoi, sporgenze), i telai sotto la pioggia devono avere lo scarico del vapore.",
 "Classi di umidità (EN 335): 1 (interno asciutto), 2 (coperto, non esposto), 3 (esposto alla pioggia senza ristagno); il legno strutturale va scelto per classe; la protezione superficiale (impregnanti, vernici) rinnova ma non sostituisce il dettaglio scorrevole; la ventilazione: il sottotetto in legno si costruisce ventilato, le facciate a telaio hanno la cavità ventilata e il freno vapore interno.",
 "Tetti, strutture esterne, basamenti, facciate in legno, case al mare o in montagna.",
 "Il dettaglio giusto protegge meglio di qualsiasi vernice: l'acqua che scorre via non marcisce nulla.",
 "La 'tignola' perenne: la colonna di legno piantata nel terreno o appoggiata sul piano senza zoccolo: marcisce in 5-10 anni.",
 "Costo protezioni e dettagli: inclusi nel progetto corretto; l'errore costa la sostituzione degli elementi.",
 "Villa al mare con struttura in telaio: il dettaglio del zoccolo rialzato (40 cm) e le sporgenze dei tetti hanno mantenuto il legno perfetto dopo 15 anni di salsedine; la casa vicina 'identica' con basamenti a terra ha sostituito le colonne di portico a 8 anni.",
 "EN 335 (classi umidità); Eurocodice 5; prassi costruttive e dettagli tipo.",
 "La frase chiave: nel legno l'acqua non deve mai fermarsi: ogni orizzontale scolante, ogni base rialzata, ogni sporgenza è un anno di vita in più."),
s("Sismica", "Il legno in sisma: la leggerezza che protegge",
 "Il legno è il materiale con il miglior rapporto resistenza/peso: nelle scosse, le forze sismiche sono proporzionali alla massa — un edificio in legno pesa 4-5 volte meno di uno in calcestruzzo, quindi subisce forze 4-5 volte minori; con le connessioni duttili (viti e piastre che si deformano plasticamente) l'energia si dissipa senza crolli.",
 "Meccanismo: la struttura a telaio o X-Lam con pannelli (che irrigidiscono) e connessioni dissipative (giunti a viti calcolati per snervarsi controllatamente) forma un sistema 'a muro controventato' equivalente agli edifici in c.a. controventati; la normativa (NTC) fornisce i metodi di calcolo e i fattori di comportamento q per il legno (simili al c.a.); la leggerezza elimina il rischio di crollo per peso proprio, il rischio resta il ribaltamento dei pannelli fuori piano (i collegamenti orizzontali contano).",
 "Edilizia residenziale in zone sismiche, scuole, edifici pubblici in zona 1-2.",
 "Il legno in sisma protegge per fisica: meno massa, meno forze; i danni restano riparabili (le connessioni si sostituiscono, gli elementi no).",
 "La leggerezza non perdona gli ancoraggi: il legno ben costruito vola via dalle fondazioni se i collegamenti sono deboli.",
 "Costo: nessun sovrapprezzo 'sismico' rispetto al legno standard (la norma è già nel progetto).",
 "Edificio in X-Lam in zona sismica: dopo una scossa forte (M5.9) le ispezioni hanno trovato fessurazioni solo in due giunti a vite (riparabili in giorni); l'edificio in c.a. confinante ha avuto danni strutturali significativi.",
 "NTC (Eurocodice 8 per le verifiche sismiche); linee guida per le costruzioni in legno in zona sismica.",
 "La domanda: 'come si comporta al sisma?' — risposta: 'pesa un quinto, si muove con la scossa e si ripara in giorni'."),
s("Costruzione", "Il cantiere del legno: montaggio, sequenze, precisione",
 "Il cantiere in legno è un montaggio, non una costruzione: gli elementi arrivano prefabbricati (tagliati, forati, numerati), la gru li posa, le squadre avvitano le connessioni; il tempo si dimezza, il cantiere resta pulito (niente getti, niente ponteggi per mesi), i vicini soffrono meno.",
 "Sequenza: fondazioni (identiche alle altre costruzioni) + zoccoli di partenza, posa del primo solaio X-Lam o del primo anello di telaio, montaggio dei pannelli parete (una casa a un piano in 2-4 giorni), solai successivi, copertura, chiusura immediata (il legno va protetto dal bagnato durante il montaggio: teli, programmazione), le connessioni di cantiere con avvitatori a coppia controllata (ogni vite tracciata), il controllo qualità con verbali di posa.",
 "Case, edilizia residenziale, ampliamenti, sopralzi.",
 "Il cantiere asciutto è un vantaggio doppio: tempi rapidi e qualità (il legno non ama bagnarsi mentre lo monti).",
 "La logistica è critica: i pannelli grandi richiedono gru e spazi; un cantiere senza gru giusta blocca tutto.",
 "Costo cantiere: il montaggio è il 20-30% del costo struttura; il risparmio di tempo porta via ponteggi, sicurezza e gestione.",
 "Casa unifamiliare: montaggio della struttura in 6 giorni lavorativi, chiusa al tetto in 3 settimane; la casa 'gemella' in muratura dello stesso costruttore: 5 mesi alla stessa fase.",
 "Piano di montaggio del produttore; controllo qualità interno; sicurezza cantieri (più leggero, meno rischi).",
 "La regola d'oro del cantiere legno: il telo copre tutto ciò che non è ancora coperto, e ogni vite va a coppia controllata con segno a matita."),
s("Economia", "L'economia del legno: costi, tempi, mercato",
 "Il legno strutturale costa più del c.a. 'a metro quadro di struttura' ma compete sul totale: i tempi di cantiere ridotti (ponteggi, sicurezza, gestione), i consumi energetici inferiori (l'involucro spesso integrato), la CO2 sequestrata (crediti ambientali nei bandi pubblici), la qualità industriale (meno imprevisti); il mercato italiano cresce ma resta al 5-8% dell'edilizia residenziale (dati settore).",
 "Conto economico: struttura +20-40% rispetto al c.a., cantiere -30-50% di tempo, involucro integrato (lastra + isolante) a parità di prestazione, manutenzione programmata annuale; la catena del valore: progettista specializzato, produttore (centro di lavorazione), carpentiere certificato; il prezzo del legno materia prima ha avuto forti oscillazioni (2021-2023) da gestire in contratto.",
 "Imprese che valutano il passaggio al legno, investitori, committenti pubblici con vincoli ambientali.",
 "Il totale costo d'opera del legno è competitivo: chi guarda solo il prezzo della struttura sbaglia il confronto.",
 "La filiera è più corta e meno 'blindabile': i forti del legno in produzione sono pochi, i prezzi volatili.",
 "Costi: casa in legno chiavi in mano: 1.800-2.800 €/m² (comparabile alla muratura di qualità); la struttura sola: voci precedenti.",
 "Confronto trasparente presentato a un committente (tabella costi-tempi-consumi legno vs c.a.): la scelta è caduta sul legno non per 'green' ma per il totale costo d'opera inferiore del 8%.",
 "Nessuna norma cogente; dati di mercato (piazze borsa legno, studi settore).",
 "Insegnare al LLM il confronto 'totale costo d'opera': chi vende il legno sul solo prezzo struttura perde, chi lo vende su tempi + consumi + ambiente vince."),
]

README = """# COSTRUIRE_IN_LEGNO_PACK — Strutture in legno: X-Lam, telaio, connessioni, protezioni

**Facoltà:** FACOLTA_INGEGNERIA · **Livello:** L2 · **Schede:** {n}

## Contenuto
La costruzione in legno moderna: perché il legno (CO2 sequestrata, leggerezza,
sismica), l'X-Lam/CLT come pannello strutturale, il telaio platform framing,
le connessioni (viti, piastre, nodi progettati), la protezione al fuoco
(carbonizzazione calcolabile), la protezione dall'umidità (classi EN 335,
dettagli scolanti), la sismica della leggerezza, il cantiere di montaggio
industriale e l'economia comparata sul totale costo d'opera.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza su scelta strutturale, dialogo con produttori e
carpentieri, superamento dei pregiudizi su fuoco e umidità con dati tecnici,
confronti economici corretti. Il tema cardine: nel legno vince chi progetta
il dettaglio (nodo, scolo, coprifuoco), non chi discute il materiale.
""".format(n=len(DATA))

COURSE = """corso: "Costruire in legno"
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
