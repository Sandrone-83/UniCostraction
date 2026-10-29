# -*- coding: utf-8 -*-
"""Giro AK (29/10/2026): genera IDROELETTRICO_PICCOLA_TAGLIA_PACK (12 schede, L2-L3,
FACOLTA_IMPIANTI_ENERGIA). Tema: mini/micro/pico idroelettrico — fisica, idrologia,
DMV, opere civili, turbine, generatore, connessione rete, autorizzazioni, economia,
recuperi su reti esistenti, cantiere, esercizio e manutenzione.
NON ridondante con RINNOVABILI_IDRO_BIOMASSA_GEOTERMIA_PACK (2 schede di panorama)
ne' con DIGHE_E_SISTEMAZIONI_IDRAULICHE_PACK (opere idrauliche civili, non impianti).
Norme solo di consolidata certezza; incentivi rimandati a verifica su GSE/ARERA.
"""
import json, os

BASE = os.path.join('UNIVERSITA_EDILIZIA', 'IDROELETTRICO_PICCOLA_TAGLIA_PACK')
KEYS = ["categoria","nome","descrizione","tecnologia","applicazioni","vantaggi","limiti",
        "costi_e_economia","casi_real_world","normative","note_cantiere"]

S = []
def add(**kw):
    assert list(kw.keys()) == KEYS, f"chiavi errate: {list(kw.keys())}"
    assert kw['costi_e_economia'].startswith('Ordini di grandezza indicativi: ')
    S.append(kw)

add(
categoria="Fondamenti",
nome="Fisica del piccolo idroelettrico: portata, salto, potenza e classificazione di taglia",
descrizione=("La potenza di un impianto idroelettrico e' sempre il prodotto di tre termini: portata turbinata Q "
    "(m3/s), salto lordo H (m) e rendimento complessivo. La formula pratica e' P(kW) = 9,81 x Q x H x eta, con "
    "9,81 = peso specifico dell'acqua in kN/m3. L'eta complessivo (turbina x moltiplicatore x generatore x "
    "trasformatore x perdite condotta) vale 0,70-0,85 nel piccolo idro: un sito con Q = 0,5 m3/s e H = 40 m "
    "da' dunque 150-165 kW elettrici, non i 196 kW teorici. La classificazione di taglia e' convenzionale "
    "(non fissata da una norma unica): pico sotto 5 kW, micro 5-100 kW, mini 100 kW-1 MW, piccolo 1-10 MW; "
    "le soglie amministrative italiane per concessioni e procedure semplificate sono definite a livello "
    "nazionale e regionale e vanno verificate caso per caso. La potenza installata non dice nulla sulla "
    "produzione: conta l'energia annua (kWh/anno), cioe' la potenza media effettiva per 8.760 ore."),
tecnologia=("Calcolo idraulico di base: salto netto = salto lordo meno perdite di condotta e di presa; portata "
    "turbinabile = portata disponibile meno deflusso ecologico e altri usi preesistenti. Strumenti: misura "
    "topografica del salto (stazione totale/GNSS, tolleranza centimetrica: un errore di 1 m su 30 m vale il "
    "3% di energia), stima della portata su curva di durata, simulazione mensile o giornaliera di "
    "producibilita' con foglio di calcolo o software dedicato."),
applicazioni=("Valutazione preliminare di un sito (sopralluogo con carta IGM 1:25.000 e DEM); confronto tra "
    "schemi alternativi (salto concentrato su condotta lunga vs piu' prese in cascata); dimensionamento di "
    "massima della turbina; stima del fatturato prima di investire in rilievi e concessione."),
vantaggi=("Formula semplice e trasparente: permette di scartare in un giorno i siti senza senso economico. "
    "Errori di valutazione evidenti fin da subito: il salto si misura, la portata si puo' stimare con metodi "
    "standard, il rendimento e' noto entro bande strette."),
limiti=("Il rendimento dichiarato dai costruttori vale al punto di funzionamento ottimale: lontano da quello "
    "punto cala rapidamente. La portata 'media' non esiste in natura: il torrente appenninico puo' passare da "
    "10 volte la media in inverno a quasi zero in agosto. La potenza nominale da sola e' un numero di marketing."),
costi_e_economia=("Ordini di grandezza indicativi: Studio di fattibilita' completo (rilievi, idrologia, schema "
    "d'impianto, business plan): 8-25 k€ per mini-idro, 3-8 k€ per micro; misura di portata con mulinello o "
    "tracciante: 300-1.500 € a campagna; rilievo topografico di presa-condotta-centrale: 2-6 k€."),
casi_real_world=("Caso tipo: condotto su torrente prealpino, presa a 812 m s.l.m., centrale a 748 m: salto "
    "lordo 64 m, portata media 0,32 m3/s, curva di durata con 6 mesi sopra 0,45 m3/s; scelta turbina da "
    "0,40 m3/s nominali: potenza installata 215 kW, produzione attesa 760 MWh/anno (3.530 ore equivalenti)."),
normative=("Nessuna norma tecnica cogente per la formula fisica; la classificazione amministrativa degli "
    "impianti e' nei decreti attuativi delle fonti rinnovabili e nelle norme regionali sulle concessioni "
    "(riferimento generale: D.Lgs 79/1999 e D.Lgs 28/2011): verificare le soglie vigenti presso la regione "
    "competente."),
note_cantiere=("Prima di firmare qualsiasi cosa, fai due misure vere: il salto con strumento topografico e la "
    "portata in almeno tre stagioni diverse. Chi compra un sito 'sulla carta' scopre dopo che il salto era "
    "al lordo di 800 m di condotta che mangia 6 m di perdite e che la portata estiva e' un decimo di quella "
    "dichiarata."),
)

add(
categoria="Fondamenti",
nome="Idrologia per il piccolo idroelettrico: curve di durata, dati e siti non misurati",
descrizione=("La portata di un corso d'acqua e' la variabile che decide tutto e quella piu' difficile da "
    "conoscere. Lo strumento di base e' la curva di durata delle portate: per ogni valore Q dice per quanti "
    "giorni all'anno quel valore e' superato. Le portate caratteristiche si chiamano Q355, Q300, Q275, Q95: "
    "Q275 e' superata 275 giorni/anno ed e' l'ordine di grandezza con cui si sceglie la portata nominale "
    "della turbina nel piccolo idro a lama d'acqua (di regola tra Q270 e Q300: turbinare portate piu' alte "
    "significa macchina piu' grossa che lavora poche centinaia di ore). I dati vengono dalle stazioni "
    "idrometriche ARPA regionali e dagli Annali idrologici storici del ex Servizio Idrografico e Mareografico "
    "Nazionale: serie lunghe 30-70 anni ma stazioni spesso lontane dal sito e in parte dismesse."),
tecnologia=("Metodi di lavoro: (1) sito misurato: elaborazione diretta della serie giornaliera, controllo "
    "omogeneita', costruzione curva di durata; (2) sito vicino a stazione misurata: trasposizione in ragione "
    "delle superfici di bacino e delle piogge medie; (3) sito non misurato: metodi regionali di stima "
    "regionale delle portate (approcci tipo VAPI per piene; per le magre, modelli di bilancio idrologico "
    "pioggia-deflusso con parametri da letteratura regionale), validati con misure puntuali in asta "
    "(mulinello, tracciante salino, stazioni ADCP) in almeno 6-8 campagne distribuite sull'anno; (4) analisi "
    "di sensibilita': produzione calcolata con serie umida, media e secca."),
applicazioni=("Definizione della portata nominale di turbina; stima della producibilita' attesa (P50) e "
    "prudenziale (P90) richiesta dalle banche; valutazione dell'effetto del deflusso ecologico; verifica di "
    "trend pluriennali (riduzione delle portate estive in molti bacini italiani negli ultimi decenni)."),
vantaggi=("Metodi consolidati e difendibili davanti a banche ed enti; la curva di durata integra tutta "
    "l'informazione e rende immediato il confronto tra scenari di turbinamento."),
limiti=("Le serie storiche non garantiscono il futuro: uso idrico del bacino (prelievi irrigui, potabili) e "
    "clima cambiano; un impianto dimensionato su dati 1960-1990 puo' risultare sovradimensionato oggi. Su "
    "bacini piccoli non misurati l'incertezza sulla portata media puo' superare il 30-40%: va dichiarata nel "
    "business plan, non nascosta."),
costi_e_economia=("Ordini di grandezza indicativi: Elaborazione curva di durata da dati ARPA disponibili: "
    "1.500-5.000 €; campagna misure in asta con mulinello/ADCP: 300-1.500 € a uscita (consigliate 6-8 "
    "uscite); installazione stazione limnimetrica dedicata con datalogger: 3-8 k€ piu' gestione annua."),
casi_real_world=("Caso tipo: bacino appenninico di 18 km2 senza stazioni; stima con metodo regionale "
    "validata da 8 misure in asta in un anno: portata media 0,28 m3/s (incertezza ±25%), Q275 = 0,34 m3/s, "
    "Q95 = 0,10 m3/s; turbina scelta su 0,32 m3/s nominali anziche' sui 0,40 del progetto preliminare: "
    "producibilita' attesa ridotta del 12% ma macchina piu' piccola e sempre ben caricata."),
normative=("Dati pubblici: ARPA regionali e ISPRA (eredità del Servizio Idrografico Nazionale); il quadro di "
    "gestione delle acque e' la Direttiva 2000/60/CE recepita dal D.Lgs 152/2006 (piani di gestione dei "
    "distretti idrografici). Nessuna norma UNI cogente per la stima idrologica di progetto: valgono metodi di "
    "letteratura consolidata."),
note_cantiere=("Non fidarti mai della portata 'vista a occhio' in un sopralluogo di primavera: e' il momento "
    "di massima. Chiedi sempre al concessionario uscente o agli enti le serie storiche, e se non esistono "
    "metti in conto un anno di misure vere prima di dimensionare la macchina: costa poche migliaia di euro e "
    "salva centinaia di migliaia."),
)

add(
categoria="Ambiente",
nome="Deflusso ecologico (DMV/DEC): rilascio continuo, misura e compatibilita' col fiume",
descrizione=("Ogni derivazione lascia nel tratto fluviale sottratto un deflusso minimo che deve garantire la "
    "funzionalita' dell'ecosistema acquatico: storicamente chiamato DMV (deflusso minimo vitale), oggi "
    "deflusso ecologico (DEC) nel quadro della Direttiva 2000/60/CE e del D.Lgs 152/2006. Il valore non e' "
    "fisso: e' definito dai piani di gestione distrettuali e dalle discipline regionali con metodi diversi "
    "(percentuali della portata media naturale, metodi idrologici o olologici piu' raffinati); ordini di "
    "grandezza frequenti sono il 5-15% della portata media naturale, ma il valore reale e' quello scritto nel "
    "provvedimento di concessione. Il DEC deve essere rilasciato in continuo, misurato e teletrasmesso "
    "all'autorita' di distretto secondo le modalita' prescritte: il misuratore e' parte dell'impianto, non un "
    "accessorio."),
tecnologia=("Opere tipiche di rilascio: apertura dedicata in opera di presa (luce calibrata, paratoia a "
    "settore, valvola) dimensionata per garantire il DEC anche al variare del livello di monte; misura con "
    "stramazzo in sezione controllata, canale Venturi/Parshall o misuratore elettromagnetico su by-pass; "
    "centralina di acquisizione con trasmissione dati. Nel dimensionamento energetico il DEC si sottrae "
    "sempre dalla portata turbinabile: in magra estiva puo' azzerare la produzione; alcune concessioni "
    "permettono riduzioni del rilascio quando la produzione e' gia' nulla (recuperi parziali): dipende dal "
    "provvedimento."),
applicazioni=("Ogni nuova concessione e rinnovo; progetto dell'opera di presa e della centralina di misura; "
    "valutazione della producibilita' reale in magra; verifica di conformita' in esercizio (i controlli "
    "dell'autorita' sono sul rilascio continuo, non su valori medi)."),
vantaggi=("Un DEC ben progettato e' compatibile con un impianto redditizio: la perdita di energia e' "
    "concentrata nei mesi di magra, quando la produzione sarebbe comunque bassa. Opere di rilascio semplici "
    "(luci calibrate) sono robuste e quasi esenti da manutenzione."),
limiti=("Con DEC elevati o metodi olologici stagionali la perdita di producibilita' puo' superare il 20-30%: "
    "va calcolata prima dell'acquisto del sito. La strumentazione di misura in alveo e' esposta a piene e "
    "detriti: richiede manutenzione e tarature periodiche; un guasto non giustifica il mancato rilascio."),
costi_e_economia=("Ordini di grandezza indicativi: Opera di rilascio con luce calibrata e stramazzo di "
    "misura: 8-30 k€; misuratore elettromagnetico su by-pass con teletrasmissione: 6-15 k€; perdita di "
    "producibilita' da DEC: tipicamente 5-25% dell'energia annua, da valutare sul provvedimento specifico."),
casi_real_world=("Caso tipo: torrente appenninico, concessione con DEC stagionale (piu' alto in primavera "
    "per la riproduzione ittica): progetto con luce calibrata doppia e stramazzo triangolare in derivazione "
    "laterale; producibilita' persa 14% rispetto all'ipotesi senza DEC; la centralina teletrasmette ogni "
    "15 minuti al portale regionale."),
normative=("Direttiva 2000/60/CE (quadro acque); D.Lgs 152/2006 parte III (tutela delle acque) e piani di "
    "gestione dei distretti idrografici; discipline regionali di calcolo e monitoraggio del deflusso: "
    "verificare quella vigente nella regione dell'intervento; prescrizioni specifiche nel provvedimento di "
    "concessione."),
note_cantiere=("Progetta l'opera di rilascio per funzionare anche con il fiume in piena e con detriti: bocche "
    "piccole si intasano. E metti la misura dove puoi arrivarci con i mezzi anche d'inverno: quando la "
    "centralina si guasta a gennaio e non ci arrivi per due settimane, la contestazione arriva lo stesso."),
)

add(
categoria="Opere civili",
nome="Opere di presa, adduzione e condotte forzate: il 50% del costo e dei guai",
descrizione=("Nel piccolo idroelettrico le opere civili pesano per il 40-60% dell'investimento e concentrano "
    "quasi tutti i rischi di cantiere. Lo schema tipo: opera di presa sul corso d'acqua (soglia o boccata "
    "laterale con griglia grossolana, sgrigliatore, paratoie di regolazione e di fondo), opera di adduzione "
    "(canale in quota o condotta a bassa pressione), vasca di carico/calma con griglia fine, troppopieno e "
    "scarico di fondo, condotta forzata in pressione fino a centrale, vasca di scarico e canale di "
    "restituzione. La griglia fine ha passata tipica 10-40 mm (piu' stretta per Pelton, piu' larga per "
    "coclee); la condotta forzata si dimensiona per velocita' economica 1,5-3 m/s: sotto si spreca diametro, "
    "sopra si brucia salto in perdite."),
tecnologia=("Materiali condotte: acciaio saldato (ogni salto, saldabile in sito, sensibile a corrosione), "
    "PRFV/vetroresina (leggera, liscia, attenzione a raggi UV e colpi), polietilene PE100 PN10-16 (fino a "
    "diametri medi, giunzioni elettrosaldabili, ottima per montagna); perdite: formule standard di moto in "
    "pressione, obiettivo perdite totali 3-7% del salto lordo; colpo d'ariete: manovre di chiusura lente "
    "(tempi di manovra progettati), sfiati e camere d'aria dove serve; opere interrate con copertura "
    "0,8-1,0 m minima per gelo e mezzi agricoli, giunti di dilatazione sui tratti a vista, ancoraggi ai "
    "cambi di direzione spinti."),
applicazioni=("Impianti ad acqua fluente su torrenti (presa + condotta corta), impianti su canali esistenti, "
    "rifacimento di opere vetuste in riattivazioni di vecchi mulini e centrali dismesse."),
vantaggi=("Opere semplici e leggibili: un canale o una condotta ben costruiti durano 50-70 anni con "
    "manutenzione minima. La vasca di carico ben fatta risolve mezza gestione: sedimenta, sgriglia e salva "
    "l'impianto nelle piene (troppopieno)."),
limiti=("I costi di sterro, di accesso e di ripristino in montagna crescono in fretta: una condotta di 2 km "
    "in versante ripido puo' costare piu' della centrale. Le opere in alveo sono soggette a piene: una "
    "presa sottodimensionata al trasporto solido si riempie di ghiaia alla prima piena seria."),
costi_e_economia=("Ordini di grandezza indicativi: Condotta forzata posata in montagna: 250-600 €/m a "
    "seconda di diametro (DN400-DN1000) e accessibilita'; opera di presa completa con sgrigliatore: 60-250 "
    "k€; vasca di carico in c.a.: 30-100 k€; quota opere civili sul totale impianto: 40-60%."),
casi_real_world=("Caso tipo: mini-idro appenninico 800 kW: presa a boccata con griglia grossolana e "
    "sgrigliatore a nastro, 1.150 m di condotta DN900 in acciaio interrata, vasca di carico da 400 m3 con "
    "troppopieno laterale e scarico di fondo comandato; opere civili 54% del CAPEX; prima piena autunnale "
    "smaltita senza danni grazie al troppopieno e alla paratoia di guardia chiusa da telecontrollo."),
normative=("Concessione di derivazione (quadro nazionale: T.U. R.D. 1775/1933 e D.Lgs 79/1999; gestione "
    "regionale); opere in alveo e su demanio idrico soggette a parere/autorizzazione dell'autorita' di "
    "bacino o regionale secondo D.Lgs 152/2006; stabilita' delle opere secondo NTC (D.M. 17/1/2018) per le "
    "parti strutturali; scavi e sicurezza: D.Lgs 81/2008 Titolo IV."),
note_cantiere=("Le piene non perdonano: non ridurre mai griglie e troppopieni per risparmiare calcestruzzo, "
    "e prevedi SEMPRE come ci arrivi a pulire la griglia con l'escavatore dopo una piena. Sulle condotte "
    "interrate il collaudo di tenuta si fa per tronchi prima della ricopertura: dopo e' troppo tardi."),
)

add(
categoria="Macchine",
nome="Turbine idrauliche di piccola taglia: Pelton, Francis, Kaplan, Banki-Michell, coclea e PAT",
descrizione=("La scelta della turbina e' dettata da salto e portata, e dentro la coppia giusta dal campo di "
    "parzializzazione. Pelton (azione): salti da 40-50 m a oltre 500 m, portate piccole-medie; rendimento di "
    "picco 88-92% e curva piatta: lavora bene dal 20% al 100% della portata nominale. Francis (reazione): "
    "25-350 m, rendimenti di picco fino a 90-93% (in piccola taglia 85-90%), ma sotto il 40-50% del carico "
    "il rendimento crolla: vuole portata costante. Kaplan ed elica (reazione assiale): 2-25 m e grandi "
    "portate; la Kaplan a doppia regolazione tiene rendimenti alti su campo ampio, l'elica a pale fisse "
    "costa meno ma parzializza male. Banki-Michell (cross-flow): 3-100 m, picco 82-86%, eccellente "
    "parzializzazione (utile gia' dal 15-20% della portata), macchina semplice e robusta: per questo ha "
    "colonizzato il piccolo idro italiano. Coclea idrodinamica (vite di Archimede rovesciata): 1-10 m e "
    "0,1-6 m3/s per stadio, rendimento 75-85%, fish-friendly, tollera detriti senza griglia fine. PAT "
    "(pompa centrifuga usata come turbina): recuperi in pressione 10-100 m, rendimento 65-80%, costo "
    "contenuto, senza regolazione: produce quello che passa."),
tecnologia=("Numero di giri e generatore: Pelton e Francis girano a 500-1.500 rpm (accoppiamento diretto o "
    "moltiplicatore); coclea 20-60 rpm (riduttore obbligatorio); Banki 100-600 rpm. Parzializzazione come "
    "criterio di scelta: con curva di durata ripida (torrente) serve macchina che rende bene a carichi "
    "parziali (Pelton, Banki, Kaplan); con portata costante (canale irriguo, scarico depuratore) Francis o "
    "elica danno il massimo. Sedimenti abrasivi: Pelton perde ugelli e spine, Francis e Kaplan perdono "
    "bordi e tenute: prevedere ricambi e riporti."),
applicazioni=("Pelton: torrenti montani con grande salto; Francis: salti medi e portata regolare, anche in "
    "centrali in caverna; Kaplan/elica e coclea: bassi salti di pianura, canali, salti su briglie e "
    "traversine esistenti; Banki: taglia piccola con portata variabile; PAT: recupero energetico su reti "
    "in pressione di acquedotti e industriali."),
vantaggi=("Parco tecnologico maturo e standardizzato: per quasi ogni coppia salto-portata esiste una "
    "macchina collaudata da decenni. Coclea e Banki hanno manutenzione semplice eseguibile da personale "
    "locale; la PAT usa componenti di largo consumo (pompe di catalogo)."),
limiti=("Nessuna turbina rende bene su tutto il campo: la scelta sbagliata rispetto alla curva di durata "
    "costa il 10-20% di produzione ogni anno. Le macchine 'speciali' su misura hanno tempi di consegna "
    "lunghi e ricambi vincolati al costruttore; la PAT non regola: se la rete a monte cambia portata, la "
    "produzione la subisce."),
costi_e_economia=("Ordini di grandezza indicativi: Gruppo turbina-generatore completo, mini-idro (100 kW-1 "
    "MW): 400-900 €/kW elettromeccanico installato; coclee: 700-1.400 €/kW ma con opere civili semplici; "
    "PAT su recupero esistente: 150-400 €/kW; revisione generale turbina (ogni 8-15 anni secondo "
    "abrasione): 5-15% del costo della macchina."),
casi_real_world=("Caso tipo 1: torrente appenninico, H = 85 m, curva di durata ripida: scelta Banki-Michell "
    "a due settori (1/3-2/3): produzione +9% rispetto a Francis di pari taglia sulla stessa idrologia. Caso "
    "tipo 2: scalo di 3,2 m su canale irriguo con portata 2,4 m3/s per 7 mesi/anno: coclea singola da 62 kW, "
    "passaggio pesci integrato, nessuna griglia fine."),
normative=("Nessuna norma cogente sulla scelta della macchina; marcatura e documentazione secondo "
    "Direttiva Macchine 2006/42/CE; prove e rendimenti secondo norme CEI EN/IEC di settore (riferimento "
    "generale alla serie IEC 60193 per le prove di accettazione dei modelli): verificare edizione vigente "
    "col costruttore; connessione elettrica secondo CEI 0-21/CEI 0-16 (vedi scheda dedicata)."),
note_cantiere=("Fai sempre vedere al costruttore la curva di durata e i sedimenti, non solo salto e portata "
    "nominale: un Pelton su acqua sabbiosa senza vasca di decantazione efficace si mangia gli ugelli in due "
    "stagioni. E chiedi i punti di rendimento garantiti in parzializzazione per iscritto, nel contratto."),
)

add(
categoria="Macchine",
nome="Generatore, regolazione e quadri: la parte elettrica dell'impianto a lama d'acqua",
descrizione=("Il gruppo elettrogeno converte la potenza meccanica in elettrica e tiene l'impianto in rete. "
    "Due scelte di macchina: generatore asincrono (gabbia di scoiattolo): semplice, robusto, economico, "
    "tipico fino a qualche centinaio di kW; non regola tensione ne' reattivi e in isola richiede batterie "
    "di condensatori; in rete segue la frequenza del distributore. Generatore sincrono: piu' costoso ma "
    "regola tensione e fattore di potenza, obbligatorio sopra certe taglie e dove il distributore chiede "
    "servizi di rete. La regolazione di un impianto a lama d'acqua segue la portata disponibile: un "
    "regolatore elettronico agisce sulla valvola di ammissione o sul distributore mantenendo il livello "
    "della vasca di carico entro banda; il PLC di centrale gestisce avvio, sincronizzazione, protezioni e "
    "telecontrollo."),
tecnologia=("Catena tipica: turbina — giunto (elastico o con volano dove serve inerzia) — moltiplicatore "
    "(cinghie dentate per piccole taglie, riduttore per coclee) — generatore IP23/IP54 — quadro di potenza "
    "con sezionatore, interruttore di macchina (DG) e quadro di parallelo — trasformatore MT/BT se "
    "connessione in media tensione — gruppo ausiliari propri (lubrificazione, comando oleodinamico "
    "valvole, UPS per telecontrollo e chiusura di emergenza). Protezioni: di macchina (sovravelocita', "
    "temperatura cuscinetti, vibrazione) e di rete (vedi scheda connessione)."),
applicazioni=("Tutti gli impianti grid-connected; impianti in isola (rifugi, baite, piccole utenze "
    "disperse) con gestione carichi dedicati; retrofit di centrali storiche con sostituzione del solo "
    "gruppo elettrogeno."),
vantaggi=("L'asincrono in BT rende gli impianti piccoli semplicissimi: niente regolatore di tensione, "
    "poche protezioni, manutenzione quasi nulla. Il telecontrollo moderno (PLC + VPN) riduce le visite in "
    "sito da quotidiane a settimanali."),
limiti=("L'asincrono assorbe reattivi dalla rete (rifasamento obbligatorio) e non puo' alimentare utenze "
    "in isola senza regolazione esterna. L'elettronica di regolazione in ambienti umidi e polverosi va "
    "protetta (quadri IP54, riscaldatori anticondensa): i guasti elettronici sono la prima causa di fermo "
    "impianto non meccanico."),
costi_e_economia=("Ordini di grandezza indicativi: Generatore asincrono 100-500 kW con quadro e "
    "rifasamento: 150-350 €/kW; generatore sincrono con regolatore: +30-60% rispetto all'asincrono; PLC di "
    "centrale con telecontrollo e videosorveglianza: 15-40 k€; trasformatore MT/BT con cella: 15-40 k€."),
casi_real_world=("Caso tipo: riattivazione centrale anni Cinquanta da 380 kW: mantenuta turbina Francis "
    "revisionata, sostituito generatore sincrono con asincrono 400 V, nuovo quadro con PLC, regolazione "
    "su valvola a farfalla motorizzata, telecontrollo completo: fermo cantiere 4 mesi, personale ridotto "
    "da presenza continua a due visite settimanali."),
normative=("DM 37/2008 (impianti elettrici: progetto e dichiarazione di conformita'); Direttiva Macchine "
    "2006/42/CE per il gruppo; marcatura CE dei quadri secondo Direttiva BT 2014/35/UE ed EMC 2014/30/UE; "
    "connessione: CEI 0-21/CEI 0-16 e delibere ARERA vigenti (vedi scheda dedicata); D.Lgs 81/2008 per "
    "sicurezza in esercizio e manutenzione."),
note_cantiere=("Metti sempre un volano o un'inerzia sufficiente se la rete e' debole (fine linea MT in "
    "montagna): i distacchi per sovrafrequenza nei vuoti di carico sono il guasto piu' frustrante del "
    "piccolo idro. E prevedi l'UPS seria sul PLC: quando salta la rete, l'impianto deve poter chiudere la "
    "valvola in sicurezza da solo."),
)

add(
categoria="Connessione",
nome="Connessione alla rete elettrica: CEI 0-21, CEI 0-16, SPI e iter col distributore",
descrizione=("Vendere energia richiede la connessione alla rete pubblica secondo le regole tecniche del "
    "distributore. In bassa tensione (tipicamente fino a 100 kW) vale la norma CEI 0-21; in media tensione "
    "la CEI 0-16: definiscono protezioni, regolazioni e documentazione. Il cuore e' il Sistema di "
    "Protezione di Interfaccia (SPI o DDI): relè che sorveglia tensione e frequenza di rete e comanda il "
    "Dispositivo di Interfaccia (DDI) che separa l'impianto quando la rete esce dai limiti; in MT i "
    "settaggi li impone il distributore e vanno certificati con verbale di prova. L'iter: richiesta di "
    "connessione con dati di impianto, preventivo TICA del distributore (tempi e costi definiti dalle "
    "delibere ARERA), accettazione, realizzazione opere, regolamento di esercizio, prova finale e messa in "
    "servizio."),
tecnologia=("Schema tipico BT: DG (dispositivo generale) + SPI integrato o esterno secondo taglia, "
    "rifasamento, misura fiscale dell'energia prodotta (contatore M1) e scambiata; schema MT: cabina "
    "utente con sezionatore di manovra-sezionatore, celle di misura, DG, SPI a relè certificato con "
    "settaggi da lettera del distributore, prove con strumento tarato e verbale. Servizi richiesti oltre "
    "certe soglie: regolazione di potenza reattiva, teledistacco, derating su segnale: verificare con la "
    "lettera di connessione specifica."),
applicazioni=("Ogni impianto grid-connected; adeguamento di connessioni esistenti in rifacimenti; "
    "configurazioni con autoconsumo parziale (impianto su acquedotto o industria: parte dell'energia "
    "autoconsumata, il resto in rete)."),
vantaggi=("Procedure standardizzate: tempi e costi del preventivo sono regolati; le norme CEI danno "
    "criteri certi per il collaudo. La connessione MT ben progettata abilita servizi (telegestione, "
    "mercati) che nel lungo periodo valorizzano l'impianto."),
limiti=("I tempi reali dell'iter superano spesso quelli regolari (mesi, a volte oltre un anno nelle zone "
    "con rete satura): la connessione va richiesta prestissimo, meglio in fase di concessione. Nelle reti "
    "deboli di montagna il distributore puo' imporre limitazioni di immissione o lavori di rinforzo a "
    "carico del produttore: costi che il business plan iniziale spesso ignora."),
costi_e_economia=("Ordini di grandezza indicativi: Connessione BT semplice: 5-20 k€; cabina MT e opere di "
    "connessione su rete esistente vicina: 30-120 k€; se servono km di linea nuova o rinforzi: da 100 k€ a "
    "salire (verificare preventivo TICA); prove SPI e pratiche distributore: 2-6 k€."),
casi_real_world=("Caso tipo: mini-idro 450 kW in valle alpina: preventivo TICA con 2,3 km di linea MT "
    "interrata lungo strada comunale; concordato con il Comune lo scavo congiunto con altri sottoservizi "
    "per ridurre i costi; verbale prova SPI con settaggi del distributore eseguito a collaudo; messa in "
    "servizio 14 mesi dopo la richiesta."),
normative=("Norma CEI 0-21 (BT) e CEI 0-16 (MT) nelle edizioni vigenti; Testo Integrato Connessioni Attive "
    "(TICA) e delibere ARERA di settore: verificare versione corrente; D.Lgs 28/2011 per il quadro FER; "
    "censimento obbligatorio dell'impianto sul sistema GAUDI' di Terna secondo le soglie vigenti; "
    "adempimenti fiscali di officina elettrica (Agenzia delle Dogane e Monopoli) se applicabili alla "
    "taglia: verificare."),
note_cantiere=("Fai la richiesta di connessione appena hai il salto e la portata credibili, NON a macchina "
    "ordinata: la connessione e' il collo di bottiglia dei tempi. E conserva tutti i verbali delle prove "
    "SPI: alla prima verifica del distributore, senza verbale firmato l'impianto rischia il distacco."),
)

add(
categoria="Iter",
nome="Iter autorizzativo: concessione di derivazione, autorizzazione unica, VIA e vincoli",
descrizione=("Un impianto idroelettrico ha bisogno di due titoli distinti: il titolo idrico (concessione di "
    "derivazione di acqua pubblica per uso idroelettrico) e il titolo edilizio-impiantistico "
    "(autorizzazione alla costruzione ed esercizio). Il quadro nazionale: T.U. R.D. 1775/1933 per le acque "
    "pubbliche, D.Lgs 79/1999 per gli impianti di produzione elettrica, D.Lgs 28/2011 che per gli impianti "
    "FER prevede l'autorizzazione unica regionale (e procedure semplificate per interventi minori); la "
    "gestione concreta e' delle Regioni e Province autonome, con disciplina di dettaglio nelle leggi "
    "regionali sulle concessioni e sui canoni demaniali. Sopra certe soglie o in aree sensibili serve la "
    "verifica o il procedimento di VIA (D.Lgs 152/2006 parte II); in siti Natura 2000 la valutazione di "
    "incidenza (Direttiva 92/43/CEE e s.m.i.); con vincolo paesaggistico (D.Lgs 42/2004) l'autorizzazione "
    "paesaggistica, spesso semplificata per le FER ma non automatica."),
tecnologia=("Sequenza pratica tipica: istanza di concessione con progetto preliminare e relazione "
    "idrologica — istruttoria con pareri (ARPA, genio civile, enti pesca/parc, soprintendenza se vincolata) "
    "— pubblicazione e contraddittorio con usi preesistenti — decreto di concessione con durata, canone e "
    "prescrizioni (DEC, monitoraggi) — autorizzazione unica/procedura edilizia con progetto definitivo — "
    "realizzazione — collaudi e concessione a esercizio. Tempi realistici complessivi: 2-5 anni per un "
    "mini-idro nuovo su corso non problematico; piu' lunghi con opposizioni o VIA."),
applicazioni=("Nuovi impianti; rinnovi di concessioni in scadenza; ricostruzioni e potenziamenti di "
    "impianti esistenti (attenzione: il potenziamento puo' richiedere nuova istruttoria piena); passaggi "
    "di proprieta' con voltura dei titoli."),
vantaggi=("Concessionaria chiara e titolo pluriennale danno bancabilita': una concessione ventennale con "
    "canone definito e' un asset finanziabile. Le procedure semplificate per interventi minori accorciano "
    "molto i tempi sui recuperi di esistente."),
limiti=("Iter lungo e incerto: pareri non vincolanti possono bloccare mesi; il rinnovo delle concessioni "
    "storiche e' materia in evoluzione normativa e contenziosa (verificare lo stato della disciplina "
    "regionale e nazionale al momento dell'operazione); canoni e sovra-canoni regionali possono cambiare "
    "nel tempo e pesare sensibilmente sull'economia."),
costi_e_economia=("Ordini di grandezza indicativi: Progettazione preliminare per istanza di concessione "
    "(idrologia, opere, relazioni ambientali): 20-60 k€ per mini-idro; istruttoria e pareri (diritti, "
    "relazioni integrative, integrazioni richieste): 10-40 k€; canone demaniale: definito da legge "
    "regionale, da verificare (spesso parametrato a kW o kWh); complessivo iter autorizzativo: 3-8% del "
    "CAPEX."),
casi_real_world=("Caso tipo: riattivazione mulino storico con salto 6 m su roggia: concessione esistente "
    "da rinnovare + procedura semplificata per l'impianto da 90 kW con coclea; parere favorevole "
    "dell'ente pesca condizionato a scala di risalita; iter completo 26 mesi; opere 8 mesi."),
normative=("R.D. 1775/1933 (T.U. acque e impianti elettrici); D.Lgs 79/1999; D.Lgs 28/2011 (autorizzazione "
    "unica FER e procedure); D.Lgs 152/2006 (VIA e tutela acque); D.Lgs 42/2004 (paesaggio); Direttiva "
    "92/43/CEE (Natura 2000); leggi regionali su concessioni e canoni: da verificare nella regione "
    "dell'intervento."),
note_cantiere=("Mai iniziare i lavori con la concessione 'in istruttoria avanzata': o hai il decreto in "
    "mano o sei abusivo, e l'abuso su demanio idrico e' penale. E leggi TUTTE le prescrizioni del decreto "
    "prima di firmare il contratto d'appalto: le penali del concessionario nascono li', non in cantiere."),
)

add(
categoria="Economia",
nome="Economia del piccolo idroelettrico: CAPEX, producibilita', ricavi e O&M",
descrizione=("Il piccolo idroelettrico e' un investimento capital-intensive a vita lunghissima: CAPEX "
    "tipico 2.500-6.000 €/kW installato per mini-idro (sotto i 100 kW anche 5.000-12.000 €/kW), con opere "
    "civili 40-60%, elettromeccanico 25-35%, progettazione/iter/connessione 15-25%. I ricavi dipendono "
    "dalla producibilita': le ore equivalenti (kWh annui / kW installati) valgono 2.500-5.500 h/a secondo "
    "idrologia e regolazione dell'impianto; la media del piccolo idro italiano ben fatto e' attorno a "
    "3.500-4.000 h. Ricavi: vendita dell'energia al GSE in Ritiro Dedicato (prezzi minimi garantiti per "
    "impianti FER entro soglie definite dalla disciplina ARERA vigente: verificare valori aggiornati sul "
    "sito GSE) o sul mercato/PPA; eventuali incentivi vanno verificati caso per caso su fonti ufficiali "
    "perche' la disciplina cambia. O&M: 1,5-3% del CAPEX all'anno; vita attesa: opere civili 50-70 anni, "
    "elettromeccanica 30-40 anni con revisioni."),
tecnologia=("Indicatori: costo livellato dell'energia (LCOE) tipico 80-150 €/MWh per impianti ben "
    "progettati con buona idrologia; payback semplice 8-15 anni; VAN sensibile soprattutto a producibilita' "
    "P50/P90, prezzo energia e durata residua della concessione. Bancabilita': gli istituti finanziano su "
    "P90 prudenziale, contratto di O&M, assicurazione all-risk e concessione con durata residua adeguata "
    "al piano."),
applicazioni=("Valutazione di acquisto siti e concessioni; business plan per finanziamento; confronto tra "
    "scenario 'vendi tutto' e 'autoconsumo parziale' (industrie, acquedotti, consorzi irrigui); valutazione "
    "di rifacimenti (nuova turbina su opere esistenti: CAPEX ridotto del 40-60%)."),
vantaggi=("Fonte programmabile e stabile nel lungo periodo: nessuna aleatorieta' giornaliera paragonabile "
    "a FV/eolico sulle medie stagionali; vita utile doppia rispetto ad altre FER: l'impianto produce per "
    "decenni dopo il payback; costi O&M contenuti e prevedibili."),
limiti=("Rischio idrologico (annate secche riducono i ricavi del 20-40%), rischio regolatorio (canoni, "
    "rinnovi, DEC), rischio rete (limitazioni di immissione): tutti difficili da assicurare. Il piccolo "
    "idro non scala: un impianto da 80 kW con 400 k€ di opere civili ha economia fragile qualunque sia il "
    "prezzo dell'energia."),
costi_e_economia=("Ordini di grandezza indicativi: CAPEX mini-idro 100 kW-1 MW: 2.500-6.000 €/kW; micro "
    "(<100 kW): 5.000-12.000 €/kW; O&M: 1,5-3% CAPEX/anno; assicurazione e gestione amministrativa: "
    "8-25 k€/anno; revisione generale elettromeccanica ogni 8-15 anni: 5-15% del valore macchina."),
casi_real_world=("Caso tipo: impianto 620 kW, CAPEX 2,9 M€ (4.680 €/kW), producibilita' P50 2.350 MWh/a "
    "(3.790 h), vendita in RID con prezzo minimo garantito vigente + eccedenze a prezzo zonale; O&M 62 "
    "k€/anno; payback 11 anni; durata concessione residua al finanziamento: 24 anni."),
normative=("RID e prezzi minimi garantiti: disciplina ARERA/GSE (delibere di settore, aggiornamenti "
    "annuali dei prezzi minimi): verificare sul portale GSE la versione vigente; quadro FER: D.Lgs "
    "28/2011; contratti e contabilizzazione: regole tecniche GSE; nessun incentivo specifico da assumere "
    "senza verifica su bando/decreto vigente."),
note_cantiere=("Fai sempre il conto con P90 e con la durata RESIDUA della concessione: un bell'impianto "
    "con 6 anni di concessione residua non vale quasi nulla. E metti nel business plan una riga 'piena "
    "eccezionale' ogni 10-15 anni: prima o poi arriva, e chi non l'ha prevista la paga due volte."),
)

add(
categoria="Recuperi",
nome="Idroelettrico senza nuova derivazione: recuperi su acquedotti, depuratori, canali e dighe esistenti",
descrizione=("La meta' piu' sostenibile (e spesso piu' rapida) del piccolo idro e' quella che non deriva "
    "acqua nuova: recupera energia dove l'acqua scende gia'. Campi tipici: nodi di riduzione della "
    "pressione negli acquedotti (al posto delle valvole riduttrici si installa una turbina o una PAT che "
    "dissipa producendo); scarichi di depuratori e portate di processo industriali; scali di quota su "
    "canali irrigui e consortili (gocciolatoi, briglie); rilasci da dighe e traversine esistenti "
    "(compreso il rilascio del deflusso ecologico: energia oggi buttata); recuperi in impianti "
    "potabilizzatori e serbatoi. Potenze tipiche 5-500 kW, spesso in BT o MT semplice, con iter "
    "autorizzativo alleggerito perche' non si tocca il regime idrologico."),
tecnologia=("Macchine: PAT per recuperi in pressione (nessuna regolazione, costo minimo); Banki o coclea "
    "per salti a pelo libero su canali; Kaplan S o eliche sommerse per rilasci di fondo. Integrazione col "
    "processo esistente e' il punto critico: la macchina non deve MAI mettere a rischio il servizio "
    "primario (pressostati di emergenza, by-pass automatici, valvola riduttrice di riserva in parallelo "
    "alla PAT)."),
applicazioni=("Gestori idrici e consorzi (autoconsumo della stazione di pompaggio o vendita); industrie "
    "con circuiti idraulici in pressione; enti gestori di dighe che devono comunque rilasciare DEC; "
    "amministrazioni con rogge e mulini storici da riattivare."),
vantaggi=("Iter piu' breve (spesso senza nuova concessione piena, con provvedimenti semplificati: "
    "verificare la disciplina regionale); impatto ambientale minimo; opere civili limitate (vasca o "
    "locale macchina su esistente); autoconsumo diretto che vale piu' della vendita in rete."),
limiti=("Portata e salto sono quelli del processo: non si scelgono e non crescono; la continuita' di "
    "esercizio dipende dal servizio primario (se l'acquedotto ferma il ramo, la turbina si ferma); le "
    "potenze sono piccole e il costo unitario puo' salire: conta l'autoconsumo, non il prezzo di vendita."),
costi_e_economia=("Ordini di grandezza indicativi: Recupero con PAT su acquedotto (20-200 kW): "
    "1.500-4.000 €/kW chiavi in mano; coclea su scalo di canale esistente: 2.000-5.000 €/kW; payback con "
    "autoconsumo pieno: 4-8 anni; con vendita in rete: 8-14 anni."),
casi_real_world=("Caso tipo: serbatoio di carico acquedotto montano con salto dissipato su valvola: PAT "
    "da 45 kW in parallelo con by-pass, energia autoconsumata dalla stazione di potabilizzazione a "
    "valle; nessuna nuova derivazione; pratica edilizia semplificata; payback 5 anni e mezzo."),
normative=("Se non si modifica la derivazione esistente: intervento interno alla concessione del gestore "
    "(verificare il provvedimento); quadro FER D.Lgs 28/2011 (procedure semplificate per interventi "
    "minori); connessione CEI 0-21/0-16 e delibere ARERA; DM 37/2008 per gli impianti; disciplina "
    "specifica da verificare col gestore della rete e la regione."),
note_cantiere=("Il patto col gestore del servizio primario va scritto prima del progetto: chi comanda la "
    "valvola, chi ferma per manutenzione, chi paga i danni se la turbina blocca la rete idrica. Senza "
    "questo accordo, il miglior progetto del mondo resta sulla scrivania."),
)

add(
categoria="Cantiere",
nome="Cantiere idroelettrico: lavori in alveo, finestre stagionali, sicurezza e collaudo",
descrizione=("Il cantiere idroelettrico convive con l'acqua viva: le opere in alveo si fanno in finestre "
    "stagionali ristrette (magra estivo-autunnale, e spesso ulteriori limitazioni per la fauna ittica "
    "definite dagli enti), con by-pass provvisori del flusso e piano piene sempre attivo. Sequenza tipo: "
    "recinti e accessi — by-pass e scolmatori provvisori — scavo e getti della presa — posa condotta "
    "(tronchi, prove di tenuta parziali, ricoprimenti) — scavo e getti centrale — montaggio macchine e "
    "quadri — prove a secco — allagamento controllato — prima accensione e collaudo. La sicurezza segue "
    "il D.Lgs 81/2008 Titolo IV: lavori sopra o presso acqua (PPI contro annegamento, mezzi di "
    "recupero), spazi confinati (condotte, vasche, pozzi: Titolo XI, qualifiche e attrezzature "
    "specifiche), scavi profondi, sollevamenti dei gruppi macchina."),
tecnologia=("Gestione del rischio piena: allerta meteo operativa collegata al piano di sicurezza, soglie "
    "idrometriche di evacuazione del cantiere di alveo, materiali e mezzi sempre rimovibili in poche ore; "
    "by-pass dimensionato almeno sulla portata di magra stagionale con margine; prove condotta: riempimento "
    "lento controllato, verifica giunti, prova di tenuta a pressione di esercizio per tronchi; collaudo "
    "macchina: prove a secco (senso rotazione, protezioni, chiusura di emergenza), allagamento, avvio a "
    "vuoto, carico graduale, prova di sincronizzazione e distacco, prova SPI col distributore, prova di "
    "rigetto del carico (load rejection) dove richiesta."),
applicazioni=("Nuovi impianti; rifacimenti con impianto fermo a finestra; opere di presa su fiumi vivi con "
    "scorrimento continuo da mantenere (DEC anche in costruzione, se prescritto)."),
vantaggi=("Lavori ben pianificati in magra si completano in una stagione; le prove per tronchi riducono il "
    "rischio collaudo; il collaudo documentato (tenuta, protezioni, sincronizzazione) e' la base della "
    "garanzia e dell'assicurabilita'."),
limiti=("Una piena fuori stagione nel momento sbagliato puo' distruggere mesi di lavoro in alveo: il "
    "rischio non si elimina, si gestisce; le finestre ittiche possono spezzare il cantiere in due "
    "stagioni con costi di mobilitazione doppi; spazi confinati e lavori sott'acqua richiedono imprese "
    "qualificate: non sono cantieri improvvisabili."),
costi_e_economia=("Ordini di grandezza indicativi: Costi di mobilitazione/allestimento cantiere in sito "
    "montano: 5-10% del valore lavori; by-pass provvisori e scolmatori: 10-60 k€ secondo portata; "
    "assicurazione CAR cantiere: 1-2,5% del valore assicurato; collaudi e prove con strumentazione: "
    "8-30 k€."),
casi_real_world=("Caso tipo: rifacimento presa su torrente prealpino: finestra luglio-ottobre, by-pass "
    "con pompe e canaletta provvisoria, soglia idrometrica di allerta a 15 m3/s con evacuazione mezzi in "
    "2 ore; piena improvvisa di settembre gestita senza danni; getti ripresi dopo 9 giorni; consegna con "
    "collaudo statico e funzionale documentato."),
normative=("D.Lgs 81/2008 (Titolo IV cantieri, Titolo XI spazi confinati, attrezzature e PPI); prescrizioni "
    "del decreto di concessione e degli enti (finestre, DEC in costruzione); NTC D.M. 17/1/2018 per le "
    "opere strutturali; DM 37/2008 per la dichiarazione di conformita' degli impianti; collaudi secondo "
    "prescrizioni della concessione e regole dell'arte."),
note_cantiere=("Il cantiere in alveo si apre solo con il piano piene firmato e condiviso: soglie, chi "
    "decide, dove vanno i mezzi. E la prima cosa che costruisci e' la via di fuga, non la cassaforma: se "
    "arriva la piena di notte, i mezzi si ricomprano, le persone no."),
)

add(
categoria="Esercizio",
nome="Esercizio e manutenzione: griglie, sedimenti, usura turbine e telecontrollo",
descrizione=("Un piccolo impianto idroelettrico ben costruito produce per decenni, ma solo se gestito: la "
    "manutenzione ordinaria e' poca cosa fatta con costanza. Attivita' tipiche: pulizia griglie (da "
    "quotidiana in autunno con fogliame a settimanale in stagione pulita; lo sgrigliatore automatico si "
    "ripaga da solo sopra certe portate), vuotatura periodica della vasca di carico (sedimenti), ispezione "
    "condotta e giunti, ingrassaggio cuscinetti, controllo allineamenti e tensione cinghie, taratura "
    "protezioni. Le turbine si usurano per abrasione da sedimenti (Pelton: ugelli, spine, cucchiai; "
    "Francis/Kaplan: bordi, tenute, distributori) e per cavitazione (controllare i segni sulle pale a ogni "
    "fermata: picchiettatura = cavitazione). Il telecontrollo (PLC + router VPN) gestisce avvio/arresto, "
    "allarmi, livelli, produzione e archivia i dati per la garanzia e per l'autorita'."),
tecnologia=("Piano di manutenzione tipico: visite settimanali leggere (o continue via telecontrollo), "
    "manutenzione annuale meccanica (cuscinetti, giunti, tenute, tarature), revisione approfondita ogni "
    "8-15 anni secondo abrasione; monitoraggi che pagano: vibrometria periodica sui gruppi, analisi olio, "
    "termografia quadri; disponibilita' attesa di un impianto ben tenuto: 92-97%. Gestione dati: portata "
    "turbinata, DEC rilasciato, ore e kWh: archivio minimo decennale per concessione, garanzie e vendita "
    "dell'asset."),
applicazioni=("Ogni impianto in esercizio; contratti di O&M full-service o a chiamata; gestione "
    "multi-impianto di piccoli portafogli (un tecnico, piu' centrali, tutto telecontrollato)."),
vantaggi=("Costi di gestione bassi e prevedibili; il telecontrollo riduce drasticamente le trasferte; una "
    "manutenzione programmata seria allunga la vita della macchina oltre i 30 anni e mantiene alta la "
    "disponibilita'."),
limiti=("L'usura da sedimenti e' una tassa nascosta: bacini con trasporto solido elevato impongono "
    "revisioni ravvicinate e ricambi (ugelli Pelton in metallo duro, riporti); il guasto elettronico in "
    "siti remoti puo' significare giorni di fermo se i ricambi non sono a scaffale; la manutenzione "
    "'quando ho tempo' si paga con fermate nelle settimane di portata migliore."),
costi_e_economia=("Ordini di grandezza indicativi: O&M ordinario: 1,5-3% del CAPEX/anno (inclusi canoni "
    "di telecontrollo e ricambi correnti); sgrigliatore automatico: 25-80 k€ ma risparmio di 100-300 ore/"
    "anno di lavoro; kit ricambi strategici a scaffale (cuscinetti, tenute, scheda PLC): 5-20 k€; "
    "revisione generale: 5-15% del valore macchina ogni 8-15 anni."),
casi_real_world=("Caso tipo: portafoglio di 4 mini-centrali appenniniche gestite da due tecnici: "
    "telecontrollo unico, pulizia griglie programmata con sgrigliatori sui due siti piu' sporchi, "
    "vibrometria semestrale; disponibilita' media 95,4%; fermata piu' lunga dell'anno: 3 giorni per "
    "sostituzione cuscinetto con ricambio a scaffale."),
normative=("Prescrizioni della concessione (DEC, monitoraggi, comunicazioni all'autorita'); D.Lgs "
    "81/2008 per le attivita' di manutenzione (spazi confinati, lavori elettrici: formazione PES/PAV "
    "secondo CEI 11-27 per il personale elettrico); documentazione impianti secondo DM 37/2008; regole "
    "dell'arte e manuali del costruttore per la manutenzione macchine."),
note_cantiere=("Tieni a scaffale il cuscinetto, la tenuta e la scheda elettronica critica: costano poco "
    "e valgono settimane di produzione. E non rimandare la pulizia della griglia 'a domani' in ottobre: "
    "la differenza tra griglia pulita e sporca, in una notte di foglie, e' una giornata di produzione "
    "persa."),
)

os.makedirs(os.path.join(BASE, 'schede'), exist_ok=True)
with open(os.path.join(BASE, 'schede', 'schede.jsonl'), 'w', encoding='utf-8', newline='\n') as f:
    for r in S:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

course = '''corso: "Idroelettrico di piccola taglia avanzato: siti, idrologia, DMV, opere, turbine, rete, autorizzazioni, economia, recuperi, cantiere, esercizio"
facolta: "FACOLTA_IMPIANTI_ENERGIA"
livello: "L2-L3"
schede: 12
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "D.Lgs 79/1999, D.Lgs 28/2011, D.Lgs 152/2006, D.Lgs 42/2004, R.D. 1775/1933 (T.U. acque), Direttiva 2000/60/CE, Direttiva 92/43/CEE, DM 37/2008, D.Lgs 81/2008, NTC D.M. 17/1/2018, norme CEI 0-21 e CEI 0-16, Direttiva Macchine 2006/42/CE, Direttiva BT 2014/35/UE ed EMC 2014/30/UE, serie IEC 60193 (prove turbine, riferimento generale), delibere ARERA/TICA e disciplina GSE RID citate come da verificare nella versione vigente; leggi regionali su concessioni e canoni citate come da verificare"
nota_metodologica: "Corso completo sul mini/micro/pico idroelettrico con taglio operativo: fisica (P=9,81*Q*H*eta), idrologia e curve di durata, deflusso ecologico, opere civili di presa e condotte, parco turbine (Pelton, Francis, Kaplan/elica, Banki-Michell, coclea, PAT) con campi di applicazione e rendimenti tipici di letteratura, generatore e regolazione, connessione rete (CEI 0-21/0-16, SPI, TICA), iter autorizzativo (concessione, autorizzazione unica, VIA, paesaggio), economia (CAPEX, ore equivalenti, RID con prezzi da verificare), recuperi su reti esistenti, cantiere in alveo e collaudo, esercizio e manutenzione. NON ridondante con RINNOVABILI_IDRO_BIOMASSA_GEOTERMIA_PACK (2 schede di panorama: qui il corso completo) ne' con DIGHE_E_SISTEMAZIONI_IDRAULICHE_PACK (opere idrauliche civili, non impianti di produzione). Prezzi come fasce indicative; norme solo di consolidata certezza; nessun nome di azienda."
'''
with open(os.path.join(BASE, 'COURSE.yaml'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(course)

readme = ('# Idroelettrico di piccola taglia avanzato\n\n'
    'Corso L2-L3 della Facolta di Impianti ed Energia: progettazione, autorizzazione, costruzione ed '
    'esercizio di impianti mini/micro/pico idroelettrici. Dalla fisica del sito (portata, salto, '
    'rendimento) all\'idrologia (curve di durata, siti non misurati), dal deflusso ecologico alle opere '
    'civili (presa, condotte forzate), dal parco turbine (Pelton, Francis, Kaplan, Banki-Michell, coclea, '
    'PAT) alla connessione in rete (CEI 0-21/0-16, SPI, TICA), dall\'iter autorizzativo (concessione, '
    'autorizzazione unica, VIA, paesaggio) all\'economia (CAPEX, ore equivalenti, RID), fino ai recuperi '
    'su reti esistenti, al cantiere in alveo e alla manutenzione pluriennale.\n\n'
    '**Schede: 12**\n\n'
    'Non ridondante con RINNOVABILI_IDRO_BIOMASSA_GEOTERMIA_PACK (schede di panorama) e '
    'DIGHE_E_SISTEMAZIONI_IDRAULICHE_PACK (opere idrauliche civili).\n')
with open(os.path.join(BASE, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(readme)

# assert finali
with open(os.path.join(BASE, 'schede', 'schede.jsonl'), encoding='utf-8') as f:
    rows = [json.loads(l) for l in f if l.strip()]
assert len(rows) == 12, f"attese 12 schede, trovate {len(rows)}"
for r in rows:
    assert list(r.keys()) == KEYS
    assert r['costi_e_economia'].startswith('Ordini di grandezza indicativi: ')
    blob = json.dumps(r, ensure_ascii=False)
    assert 'aplicazioni' not in blob and 'tegnologia' not in blob
print(f"OK: {os.path.join(BASE, 'schede', 'schede.jsonl')} - {len(rows)} schede, chiavi e ordine corretti")
