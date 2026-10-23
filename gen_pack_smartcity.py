# -*- coding: utf-8 -*-
import json, io, os

BASE = r'UNIVERSITA_EDILIZIA/SMART_CITY_PACK'
os.makedirs(os.path.join(BASE, 'schede'), exist_ok=True)

KEYS = ['categoria','nome','descrizione','tecnologia','applicazioni','vantaggi','limiti',
        'costi_e_economia','casi_real_world','normative','note_cantiere']

S = []
def add(**kw):
    assert list(kw.keys()) == KEYS, list(kw.keys())
    assert kw['costi_e_economia'].startswith('Ordini di grandezza indicativi: '), kw['nome']
    S.append(kw)

add(
 categoria="Architettura",
 nome="La smart city: architettura a livelli e cosa significa davvero",
 descrizione="Smart city non e' uno slogan ma un'architettura tecnica: sensori sul territorio, reti di comunicazione, una piattaforma dati, applicazioni per i servizi. Chi progetta o gestisce edilizia pubblica ci lavora dentro: l'edificio scolastico, l'illuminazione, la rete idrica sono nodi del sistema.",
 tecnologia="Livelli: (1) percezione: sensori e contatori (illuminazione, traffico, qualita' aria, reti idriche, edifici); (2) connettivita': reti a basso consumo per IoT (LoRaWAN, NB-IoT), fibra e 5G per i flussi grandi; (3) piattaforma dati: raccolta, storicizzazione, API e cruscotti; (4) applicazioni: gestione illuminazione, manutenzione predittiva, servizi ai cittadini. Regola d'oro: ogni livello deve poter vivere senza gli altri (il lampione smart resta un lampione anche a piattaforma ferma); standard aperti per evitare lock-in del fornitore.",
 applicazioni="Programmi di rigenerazione urbana; gestione del patrimonio pubblico comunale; gare per servizi energetici e tecnologici; integrazione degli edifici pubblici nel monitoraggio cittadino.",
 vantaggi="I dati continui riducono costi di gestione (energia, manutenzione) e rendono misurabili i servizi; la piattaforma comune evita acquisti ripetuti di sensori ridondanti; un patrimonio pubblico monitorato si valorizza anche in sede di finanziamento.",
 limiti="Il rischio 'vetrina': progetti fatti di pochi sensori scenografici senza gestione dei dati; ogni sensore installato e' un oggetto da manutenere e alimentare per anni; la frammentazione tra uffici comunali (lavori pubblici, ambiente, sistemi informativi) e' l'ostacolo vero, non la tecnologia.",
 costi_e_economia="Ordini di grandezza indicativi: progetto di smart city per comune medio (10.000-50.000 abitanti) con illuminazione, sensoristica base e piattaforma: 0,5-3 M€ secondo perimetro; piattaforma dati comunale 50-200 k€ piu' canoni; sensore ambientale installato 300-1.500 euro/cad; i costi di gestione annui (connettivita', licenze, manutenzione) valgono tipicamente il 8-15% dell'investimento iniziale.",
 casi_real_world="Caso tipo: comune medio che unifica in un'unica gara illuminazione LED con telegestione, sensori parcheggi e monitoraggio qualita' aria su una piattaforma comune, invece di tre acquisti separati: un solo punto di raccolta dati, un solo contratto di manutenzione.",
 normative="GDPR (Reg. UE 2016/679) per i dati raccolti in spazi pubblici; D.Lgs 138/2024 (recepimento direttiva NIS2) per la cybersecurity dei servizi essenziali; D.Lgs 36/2023 per gli appalti di servizi tecnologici; AGID per interoperabilita' delle piattaforme pubbliche.",
 note_cantiere="Prima di comprare sensori, scrivi chi li legge: se nessun ufficio comunale e' titolare del dato, il sensore sara' un soprammobile. Assegna la titolarita' del dato nell'atto di gara, non a collaudo."
)

add(
 categoria="Servizi urbani",
 nome="Illuminazione pubblica intelligente: LED, telegestione e punto luce come nodo",
 descrizione="La riqualificazione LED con telegestione e' il progetto smart city piu' maturo: ogni punto luce diventa un nodo indirizzabile che si accende, dimezza e segnala guasti da solo. Il palo diventa poi infrastruttura per sensori e connettivita'.",
 tecnologia="Componenti: apparecchi LED con driver programmabile; nodo di telegestione punto-punto (power line o radio) o centralizzato a quadro; profili di dimming (riduzione notturna 30-50% del flusso nelle ore a basso traffico); telediagnostica guasti e misura dei consumi per punto luce; il palo come ospite: sensori ambientali, videocamere, piccole celle radio, colonnine EV (con verifiche di carico e di alimentazione); convenzione e contabilizzazione dei risparmi con la ESCo nel project financing o nel partenariato.",
 applicazioni="Riqualificazione energetica dell'illuminazione comunale; adeguamento normativo e di sicurezza stradale; predisposizione di infrastrutture per servizi smart futuri; contratti di rendimento energetico.",
 vantaggi="Risparmio energetico reale del 50-70% rispetto a scarica/ad alogenuri, misurabile punto per punto; guasti segnalati dal sistema invece che dai cittadini; il palo esistente evita nuove opere civili per sensori e antenne; intervento tra i piu' bancabili per ESCo e finanza di progetto.",
 limiti="La qualita' ottica non si improvvisa: apparecchi scadenti danno abbagliamento e luce dispersa verso il cielo (inquinamento luminoso, prescrizioni regionali); la telegestione power line soffre su reti vecchie; il canone di gestione e manutenzione va messo in gara o decade tutto in pochi anni.",
 costi_e_economia="Ordini di grandezza indicativi: sostituzione punto luce con LED e telegestione 350-700 euro/punto luce installato; progetto su 3.000 punti luce: 1-2 M€; risparmio energetico documentabile 50-70% sui consumi pregressi; tempi di rientro tipici 5-9 anni secondo il profilo di dimming e il prezzo dell'energia.",
 casi_real_world="Caso tipo diffuso: comune che sostituisce 4.000 punti luce a vapori con LED telegestito in partenariato, con dimming notturno e tabellone consumi pubblico: bolletta elettrica dell'illuminazione dimezzata e guasti gestiti entro 48 ore da allarme automatico.",
 normative="Leggi regionali sull'inquinamento luminoso (da verificare localmente); D.Lgs 152/2006 e normativa ambientale per lo smaltimento degli apparecchi dismessi; D.Lgs 36/2023 e disciplina del partenariato pubblico-privato per i contratti con ESCo; norme CEI sugli impianti di illuminazione pubblica.",
 note_cantiere="In sostituzione, verifica i punti luce su mappa e su sopralluogo: gli inventari comunali sbagliano regolarmente del 5-15% e l'ERRORE lo paghi tu in fase di rendicontazione dei risparmi, che si misurano sul censimento, non sul progetto."
)

add(
 categoria="Architettura",
 nome="Sensoristica urbana e reti IoT: LoRaWAN, NB-IoT e la scelta della connettivita'",
 descrizione="I sensori urbani (aria, rumore, livelli idraulici, parcheggi, cassonetti) parlano con reti a basso consumo: la scelta tra LoRaWAN proprietario comunale e NB-IoT dell'operatore decide costi, autonomia e governance per dieci anni.",
 tecnologia="Opzioni: LoRaWAN (rete propria del comune: gateway su edifici pubblici, copertura chilometrica, sensori a batteria 5-10 anni, nessun canone per dato ma gestione della rete a carico); NB-IoT/LTE-M (rete dell'operatore: canone per SIM, copertura gia' esistente, niente manutenzione di rete ma dipendenza dal contratto); 5G e fibra per i flussi video e i dati grandi; i sensori tipici: qualita' aria (PM, NO2), livello cassonetti, presenza parcheggio, rumore, livelli di tombini e corsi d'acqua, contatori acqua/energia degli edifici pubblici.",
 applicazioni="Monitoraggio ambientale comunale; gestione parcheggi e mobilita'; servizi idrici e drenaggio; telecontrollo degli edifici pubblici; raccolta dati per bandi e rendicontazioni.",
 vantaggi="Batterie pluriennali e nessun cablaggio: si installa un sensore in un'ora; LoRaWAN comunale elimina i canoni e tiene i dati in casa; NB-IoT elimina la gestione della rete e scala subito; i dati ambientali continui hanno valore anche verso cittadini e ARPA.",
 limiti="Nessuna delle due reti e' gratis sul lungo periodo: LoRaWAN richiede un ufficio capace di gestirla, NB-IoT vincola ai canoni e al fornitore; i sensori ambientali economici vanno tarati e sostituiti (deriva dei sensori PM in 1-3 anni); la copertura reale va misurata, non dichiarata: edifici e orografia schermano.",
 costi_e_economia="Ordini di grandezza indicativi: gateway LoRaWAN installato su edificio pubblico 500-1.500 euro/cad; sensore qualita' aria di fascia media installato 800-2.500 euro/cad; sensore parcheggio 100-300 euro/cad; SIM NB-IoT 1-3 euro/mese per sensore; sostituzione/taratura sensori ambientali ogni 1-3 anni come voce di gestione.",
 casi_real_world="Caso tipo: comune che copre il territorio con 6 gateway LoRaWAN su scuole e uffici pubblici e installa 40 sensori (aria, parcheggi, livello fiume) alimentati a batteria: nessun canone connettivita', dati su piattaforma comunale, manutenzione affidata con contratto triennale.",
 normative="Normativa europea sulle radiofrequenze e marcatura CE dei dispositivi; GDPR per i dati eventualmente riferibili a persone (parcheggi, flussi); D.Lgs 138/2024 (NIS2) se i sensori alimentano servizi essenziali; accordi quadro e convenzioni Consip/centrale acquisti per le forniture pubbliche.",
 note_cantiere="Prima di scegliere la rete, fai un giro con un sensore di prova nei punti peggiori (piani interrati, valli, capannoni): la copertura da brochure e quella reale non coincidono mai, e lo scopri gratis solo prima dell'acquisto."
)

add(
 categoria="Dati e piattaforme",
 nome="La piattaforma dati urbana e la control room: dove i dati diventano servizio",
 descrizione="Sensori senza piattaforma sono numeri persi: la piattaforma dati comunale raccoglie, storicizza e rende leggibili i dati del territorio. La control room e' il suo volto operativo: cruscotti, allarmi, stato dei servizi in tempo reale.",
 tecnologia="Componenti: broker e data lake per la raccolta multi-sorgente (IoT, contatori, sistemi gestionali, open data); standard di interoperabilita' e API aperte; cruscotti per servizio (energia edifici, illuminazione, mobilita', ambiente); allarmi e ticket automatici verso la manutenzione; pubblicazione open data verso i cittadini; integrazione con il catasto, il GIS comunale e i sistemi informativi esistenti; requisito chiave: il comune deve possedere i dati e poter cambiare fornitore della piattaforma senza perdere lo storico.",
 applicazioni="Gestione energetica del patrimonio pubblico; sala operativa per eventi ed emergenze; rendicontazione di bandi e finanziamenti; trasparenza e open data; supporto alle decisioni di bilancio.",
 vantaggi="Un dato solo, raccolto una volta, serve a dieci uffici; gli allarmi automatici trasformano la manutenzione da passiva a programmata; gli open data alimentano servizi di terzi senza costi aggiuntivi; la rendicontazione ai finanziatori diventa un'esportazione, non un progetto.",
 limiti="La piattaforma senza processi e' un costo fisso inutile: serve qualcuno che legga i cruscotti; l'integrazione con i gestionali esistenti e' sempre piu' costosa del preventivo; il rischio lock-in del fornitore e' reale se i dati non sono esportabili in formati aperti.",
 costi_e_economia="Ordini di grandezza indicativi: piattaforma dati comunale di taglia media 50-200 k€ di avvio piu' 15-50 k€/anno di gestione; allestimento control room (videowall, postazioni, rete) 30-150 k€; integrazione con un gestionale esistente 5-30 k€ a flusso; un addetto formato alla piattaforma e' la voce piu' dimenticata e piu' decisiva.",
 casi_real_world="Caso tipo: unione di comuni che condivide una piattaforma unica per energia delle scuole, illuminazione e qualita' aria: costi di licenza e gestione ripartiti, un solo cruscotto per il direttore dei lavori pubblici, open data pubblicati per i cittadini.",
 normative="AGID: linee guida su interoperabilita' e open data delle pubbliche amministrazioni; GDPR per i dati personali; D.Lgs 138/2024 (NIS2) per la sicurezza della piattaforma; CAD (D.Lgs 82/2005) per i servizi digitali pubblici.",
 note_cantiere="Metti nel contratto la clausola di esportazione completa dei dati in formato aperto a fine rapporto, con prova pratica annuale: il giorno che cambi fornitore ringrazierai te stesso, e costa zero scriverla oggi."
)

add(
 categoria="Dati e piattaforme",
 nome="Digital twin urbano: quando il modello digitale della citta' serve davvero",
 descrizione="Il digital twin urbano e' il modello digitale aggiornato della citta': edifici, reti, strade, sensori. Serve quando si devono simulare scenari (piani di traffico, rischio idraulico, piano energetico) e non solo 'guardare' i dati.",
 tecnologia="Costruzione: base GIS 3D della citta' (rilievi, fotogrammetria, cartografia); integrazione BIM degli edifici pubblici principali; collegamento dei dati in tempo reale dai sensori; motori di simulazione (idraulica urbana, traffico, energia, esposizione al rischio); il twin si mantiene: un modello non aggiornato diventa un plastico, non un twin; livelli di dettaglio diversi per usi diversi (LOD del territorio vs LOD degli edifici).",
 applicazioni="Piani di gestione del rischio idrogeologico urbano; pianificazione energetica di quartiere; simulazione di scenari di traffico e cantieri; gestione coordinata delle emergenze; presentazione pubblica dei progetti.",
 vantaggi="Le decisioni si testano sul modello prima che sul territorio; un unico riferimento 3D riduce gli errori di sovrapposizione delle reti in scavo; la comunicazione con cittadini e amministratori migliora drasticamente; i finanziamenti europei premiano progetti con base dati digitale.",
 limiti="Costo di costruzione e soprattutto di mantenimento: senza budget annuale il twin muore in due anni; la qualita' dipende dai rilievi di partenza (reti interrate mal censite restano mal censite anche in 3D); rischio di acquisto 'a scatola chiusa' di piattaforme spettacolari e vuote.",
 costi_e_economia="Ordini di grandezza indicativi: rilievo fotogrammetrico/LiDAR di un centro urbano medio 30-150 k€ secondo estensione e dettaglio; piattaforma di digital twin con integrazioni 100-500 k€ per un comune medio-grande; aggiornamento annuale 10-20% del costo iniziale; il censimento accurato delle reti interrate e' spesso la voce piu' lunga e piu' utile del progetto.",
 casi_real_world="Caso tipo: citta' media che costruisce il twin partendo dal rischio alluvione: modello idraulico urbano calibrato sui dati dei tombini sensorizzati, scenari di pioggia simulati, piano di intervento sulle caditoie con priorita' misurata invece che stimata.",
 normative="D.M. 312/2021 (metodi e strumenti digitali BIM negli appalti pubblici) per la parte edilizia; AGID e CAD (D.Lgs 82/2005) per i dati pubblici; GDPR per dati e immagini del territorio; normativa sul rilievo e sulla cartografia ufficiale.",
 note_cantiere="Non partire dal software: parti da UN caso d'uso che il comune ha gia' (alluvioni, energia delle scuole, cantieri) e costruisci il twin per quello. Chi compra il twin 'generico' ha comprato un problema, non uno strumento."
)

add(
 categoria="Servizi urbani",
 nome="Mobilita' smart: parcheggi sensorizzati, traffico e ricarica dei veicoli elettrici",
 descrizione="La mobilita' e' il servizio smart piu' visibile: sensori sui parcheggi, conteggi di traffico, colonnine di ricarica, pannelli informativi. Funziona quando i dati alimentano decisioni (prezzi, varchi, manutenzione), non quando decorano.",
 tecnologia="Parcheggi: sensori di occupazione (magnetici o ottici) con app di disponibilita'; traffico: spire, telecamere con analisi video (attenzione al GDPR: anonimizzazione a bordo), conteggi ciclabili; ricarica EV: colonnine da 7-22 kW AC in parcheggi e 50-350 kW DC su assi principali, con gestione dei carichi e tariffe; pannelli a messaggio variabile e infomobilita'; integrazione con i permessi ZTL e la sosta a pagamento.",
 applicazioni="Gestione della sosta in centro; piani urbani della mobilita' con dati misurati; infrastruttura di ricarica pubblica e condominiale; monitoraggio delle ZTL e dei cantieri stradali.",
 vantaggi="La sosta misurata riduce il traffico di ricerca (quota rilevante del traffico centrale); le colonnine ben posizionate usano la rete esistente senza riforzare le cabine; i dati di traffico continui sostituiscono le campagne di conteggio annuali; la ricarica condominiale coordinata evita il fai-da-te pericoloso.",
 limiti="Sensori di parcheggio: la manutenzione su pavimentazione stradale e' continua (asfaltature coprono i sensori); le colonnine pubbliche senza gestione dei carichi fanno saltare la fornitura nei momenti di punta; i dati video in spazi pubblici richiedono valutazione d'impatto privacy; la tariffa e i parcheggi sono scelte politiche: il sensore non decide nulla da solo.",
 costi_e_economia="Ordini di grandezza indicativi: sensore di parcheggio installato 100-300 euro/cad; colonnina AC 22 kW installata 3-8 k€/cad; fast DC 50-120 kW 40-100 k€/cad compresa la connessione; sistema di pannelli e infomobilita' per un centro medio 100-400 k€; gestione e connettivita' delle colonnine 50-150 euro/mese per punto.",
 casi_real_world="Caso tipo: comune che sensorizza 800 stalli centrali e collega i dati all'app e ai pannelli di accesso: tempo medio di ricerca parcheggio ridotto e misurato, tariffazione dinamica introdotta solo dopo un anno di dati pubblicati.",
 normative="Codice della strada e regolamenti di sosta comunali; GDPR e provvedimenti del Garante per la videosorveglianza urbana; normativa sulle colonnine e sui punti di ricarica pubblici (CEI, regole tecniche MIMS; da verificare le versioni vigenti); D.Lgs 36/2023 per le concessioni di servizio.",
 note_cantiere="Posa i sensori di parcheggio insieme all'asfaltatura, mai dopo: il sensore murato nell'asfalto nuovo vive anni, quello corredato dopo vive mesi. Coordina la gara sensori con il piano strade, o li compri due volte."
)

add(
 categoria="Servizi urbani",
 nome="Gestione idrica smart: perdite, drenaggio urbano e monitoraggio delle reti",
 descrizione="L'acqua e' il servizio dove la sensoristica ripaga di piu': distrettualizzazione e contatori smart riducono le perdite delle reti idriche, i sensori di livello su tombini e corsi d'acqua alimentano la protezione civile, il drenaggio misurato previene le alluvioni urbane.",
 tecnologia="Rete idrica: distrettualizzazione (DMA) con misuratori di portata e pressione, contatori smart con lettura remota, ricerca perdite guidata dai dati (minime notturne); drenaggio: sensori di livello nei nodi critici, pluviometri in rete, modelli idraulici urbani calibrati sui dati reali; corsi d'acqua: idrometri collegati alla sala di protezione civile comunale; qualita': sensori su vasche e scarichi; integrazione con il gestore idrico (che spesso non e' il comune: accordi sui dati necessari).",
 applicazioni="Piani di riduzione delle perdite (in Italia quote di rete perse elevate e misurate dai bilanci); pre-allarme alluvione urbana; gestione degli eventi di piena dei corsi minori; monitoraggio delle vasche di laminazione.",
 vantaggi="La riduzione perdite e' misurabile e finanziabile (meno acqua prelevata, meno energia di pompaggio); i pre-allarmi idraulici salvano beni e talvolta vite; i contatori smart eliminano letture stimate e contestazioni; i dati meteo-idraulici locali calibrano i modelli per il piano del territorio.",
 limiti="Le reti vecchie perdono da mille punti: i sensori indicano dove, ma la riparazione resta il costo vero; la distrettualizzazione mal progettata crea colli di bottiglia e pressioni insufficienti; la gestione e' del gestore idrico: il comune che installa sensori senza accordo raccoglie dati che nessuno usa.",
 costi_e_economia="Ordini di grandezza indicativi: distrettualizzazione con misura di una rete comunale media 100-500 k€ secondo estensione; contatore smart utenza installato 150-300 euro/cad; sensore di livello tombino/idrometro con teletrasmissione 500-2.000 euro/cad; ogni punto percentuale di perdite recuperato su una rete media vale decine di k€/anno di acqua non prelevata e pompata.",
 casi_real_world="Caso tipo: gestore idrico e comune che distrettualizzano la rete del centro storico e installano idrometri sui due fossi urbani: le minime notturne guidano la ricerca perdite (due tratti sostituiti) e la sala operativa riceve il pre-allarme di piena con 40-60 minuti di anticipo.",
 normative="Regolazione ARERA del servizio idrico (metriche di perdita e obblighi di misura); D.Lgs 152/2006 (acque e difesa del suolo); direttiva alluvioni recepita a livello nazionale per i piani di rischio; accordi comune-gestore secondo il quadro del servizio idrico integrato.",
 note_cantiere="Se installi idrometri per la protezione civile, scrivi e prova la procedura di allarme (chi riceve, chi decide, chi chiude le strade): un sensore che allerta un numero non presidiato e' peggio di niente, perche' da' falsa sicurezza."
)

add(
 categoria="Edifici pubblici",
 nome="L'edificio pubblico nella smart city: BEMS, scuole e il patrimonio misurato",
 descrizione="Scuole, uffici, palestre comunali sono i primi edifici della smart city: un sistema di gestione energetica (BEMS) che legge contatori e temperature li trasforma da bollette a dati, e la manutenzione da emergenza a programma.",
 tecnologia="Componenti: gateway su contatori elettrici/termici e sulle centrali termiche; sensori di temperatura e CO2 nelle aule; BEMS con cruscotti per edificio e allarmi (consumi anomali, deroghe, guasti); classi energetiche calcolate sui consumi misurati e non solo sull'APE; collegamento con la piattaforma comunale per la rendicontazione; integrazione con le prenotazioni degli spazi (palestre, sale) per accendere solo gli edifici usati; base per i contratti EPC e per le diagnosi energetiche obbligatorie.",
 applicazioni="Gestione energetica del patrimonio scolastico; verifica dei risultati delle riqualificazioni; priorita' di manutenzione basate sui dati; rendicontazione dei contributi energetici; qualita' dell'aria nelle aule (post-pandemia: monitoraggio CO2).",
 vantaggi="I consumi anomali si vedono in giorni invece che in bolletta dopo mesi; le scuole misurate scalano le classifiche dei finanziamenti (i bandi premiano i dati); il monitoraggio CO2 documenta la qualita' dell'aria verso famiglie e dipendenti; il BEMS ripaga con i primi guasti intercettati.",
 limiti="Le centrali termiche vecchie parlano lingue proprietarie o non parlano affatto (serve il gateway giusto o la sostituzione del modulo); i dati senza un referente energetico comunale si accumulano inutilizzati; i sensori nelle aule richiedono attenzione a privacy e percezione (documentare cosa si misura).",
 costi_e_economia="Ordini di grandezza indicativi: kit di monitoraggio per edificio scolastico (contatori, centralina, CO2) 2-6 k€ a edificio installato; BEMS comunale per 20-50 edifici 30-100 k€ piu' canone; risparmi documentabili dalla sola gestione (orari, set-point, guasti intercettati) 5-15% sui consumi; referente energetico: la voce che decide il successo, da internalizzare o affidare.",
 casi_real_world="Caso tipo: comune che monitora 30 scuole: nel primo inverno il BEMS individua caldaie in funzione h24 e modulazione assente in quattro plessi; regolazione e formazione dei custodi portano risparmi a doppia cifra senza alcun lavoro edile.",
 normative="D.Lgs 102/2014 e disciplina delle diagnosi energetiche; DPR 74/2013 (esercizio degli impianti termici); GDPR per i dati ambientali associabili a persone; D.M. 18/12/1975 e normativa scolastica per i parametri ambientali delle aule (da verificare nelle versioni vigenti).",
 note_cantiere="Prima di comprare il BEMS fai l'elenco delle centrali termiche con marca e protocollo: se meta' delle caldaie parla solo in seriale proprietario, lo sai a preventivo e non a cantiere aperto. Il sopralluogo impianti vale piu' della demo del software."
)

add(
 categoria="Rigenerazione",
 nome="Smart district e rigenerazione urbana: il quartiere come unita' di progetto",
 descrizione="Il livello giusto della smart city spesso non e' la citta' intera ma il quartiere: ex aree industriali, comparti scolastici, distretti fieristici. Nel distretto si integrano energia, mobilita', verde e servizi con numeri che si misurano.",
 tecnologia="Elementi del distretto smart: rete di calore o solare di quartiere; ricarica EV e mobilita' condivisa; illuminazione e sicurezza integrate; verde urbano sensorizzato (irrigazione a richiesta, monitoraggio alberature); edifici con BEMS collegati; piattaforma di distretto con indicatori pubblici (energia, aria, presenze); governance: un soggetto gestore del distretto (pubblico o misto) con obblighi misurabili; iter: masterplan con indicatori, gare per i servizi, fasi a misura con verifica annuale pubblica degli indicatori.",
 applicazioni="Rigenerazione di ex aree industriali e militari; nuovi insediamenti universitari e ospedalieri; quartieri fieristici e direzionali; programmi di riqualificazione con finanziamenti nazionali ed europei.",
 vantaggi="La scala del quartiere rende gli investimenti dimensionabili e i risultati misurabili in anni, non decenni; l'integrazione tra servizi (calore+EV+verde) genera economie vere; gli indicatori pubblici creano fiducia e attraggono operatori; e' la scala preferita dai bandi di rigenerazione.",
 limiti="Il rischio 'quartiere vetrina' con servizi che decadono dopo l'inaugurazione: senza gestore e piano di gestione i sensori muoiono; i tempi delle opere edili e quelli dei servizi digitali non coincidono mai: serve un direttore unico; i vincoli tra pubblico e privato nel distretto sono il punto legale piu' delicato.",
 costi_e_economia="Ordini di grandezza indicativi: dotazione digitale di un quartiere di rigenerazione (sensoristica, piattaforma, illuminazione smart, ricarica) 1-5% del valore complessivo dell'intervento edilizio; gestione dei servizi smart 50-200 k€/anno secondo perimetro; gli indicatori ben scelti (10-20, non 200) costano poco e decidono i finanziamenti successivi.",
 casi_real_world="Caso tipo: trasformazione di un'ex area produttiva con masterplan a indicatori: rete di calore alimentata da recupero industriale, 60 punti di ricarica, verde sensorizzato e cruscotto pubblico trimestrale; i bandi successivi sono stati vinti mostrando i dati del primo anno.",
 normative="D.Lgs 36/2023 (concessioni e partenariati); D.Lgs 42/2004 e strumenti urbanistici comunali per la rigenerazione; normativa europea e nazionale dei programmi di finanziamento della rigenerazione (da verificare bando per bando); GDPR per i dati di quartiere.",
 note_cantiere="Scrivi nel capitolato chi accende e chi spegne: ogni servizio smart del distretto deve avere un titolare di gestione con budget, dalla prima lampadina. I quartieri smart falliti falliscono tutti sullo stesso foglio: la gestione."
)

add(
 categoria="Governance",
 nome="Privacy, cybersecurity e governance dei dati urbani",
 descrizione="La smart city raccoglie dati in spazi pubblici: telecamere, flussi, consumi, spostamenti. Il perimetro legale (GDPR, NIS2) non e' un ostacolo ma il progetto: chi non lo progetta prima lo subisce dopo, con sanzioni e servizi fermi.",
 tecnologia="Regole tecniche: minimizzazione (raccogliere solo il dato necessario al servizio); anonimizzazione a bordo per video e flussi (i volti non escono dalla telecamera); DPIA (valutazione d'impatto) obbligatoria per il trattamento sistematico in spazi pubblici; sicurezza by design: reti separate per IoT e uffici, aggiornamenti dei dispositivi, inventario degli asset; NIS2 (D.Lgs 138/2024): i comuni e i gestori di servizi essenziali rientrano nel perimetro con obblighi di gestione del rischio, incident reporting e misure tecniche; ruoli: titolare del dato, DPO, responsabile sicurezza, fornitori con clausole specifiche.",
 applicazioni="Videosorveglianza e analisi video urbane; piattaforme dati comunali; servizi essenziali digitali (idrico, energia, mobilita'); gare di servizi tecnologici con clausole di sicurezza.",
 vantaggi="La compliance progettata prima accelera le gare e i collaudi invece di bloccarli; l'anonimizzazione a bordo permette analisi video utili senza trattare dati personali; la rete IoT separata limita gli incidenti ai dispositivi, senza toccare gli uffici; la fiducia dei cittadini e' un asset del servizio.",
 limiti="Gli obblighi NIS2 richiedono competenze che i piccoli comuni non hanno: serve supporto intercomunale o esterno; i dispositivi IoT economici non sono aggiornabili: diventano il punto debole della rete; ogni sanzione o incidente pubblico brucia anni di fiducia sul progetto.",
 costi_e_economia="Ordini di grandezza indicativi: DPIA e impianto privacy per un programma smart comunale 5-20 k€ di consulenza; adeguamento NIS2 per un ente medio (assessment, misure, procedure) 20-80 k€ iniziali piu' gestione; il costo di un incidente (fermo servizio, sanzioni, comunicazione) supera regolarmente il costo della prevenzione di un ordine di grandezza.",
 casi_real_world="Caso tipo: comune che installa analisi video sui varchi con anonimizzazione a bordo e DPIA pubblicata: il progetto passa la verifica preliminare senza rilievi e i dati aggregati alimentano il piano traffico senza alcun trattamento di volti o targhe.",
 normative="Reg. UE 2016/679 (GDPR) e provvedimenti del Garante privacy su videosorveglianza e smart city; D.Lgs 138/2024 (NIS2: obblighi per PA e servizi essenziali); CAD (D.Lgs 82/2005); linee guida AGID sulla sicurezza delle PA.",
 note_cantiere="In gara chiedi sempre: il dispositivo riceve aggiornamenti di sicurezza? Per quanti anni? Se la risposta e' 'non previsto', quel sensore economico ti costera' caro: in NIS2 un dispositivo abbandonato e' una vulnerabilita' tua, non del fornitore."
)

add(
 categoria="Economia",
 nome="L'economia della smart city: CAPEX, OPEX, bandi e modelli di partenariato",
 descrizione="I progetti smart falliscono piu' spesso sui numeri di gestione che sulla tecnologia: ogni sensore ha un OPEX per dieci anni. Il modello economico (bando, partenariato, gara di servizio) decide cosa sopravvive dopo l'inaugurazione.",
 tecnologia="Struttura dei costi: CAPEX (sensori, rete, piattaforma, integrazioni) e OPEX (connettivita', licenze, manutenzione, energia, personale: tipicamente 8-15% del CAPEX ogni anno); fonti: bandi nazionali ed europei di rigenerazione (verificare i bandi aperti: quelli PNRR sono chiusi), fondi regionali, partenariato pubblico-privato con ESCo per i servizi energetici, gare di servizio con canoni legati a indicatori; la regola: nessun CAPEX senza il suo OPEX finanziato; contratti con livelli di servizio misurabili (uptime piattaforma, tempi di riparazione, accuratezza dei dati).",
 applicazioni="Piani triennali comunali dei servizi digitali; gare di illuminazione e servizi energetici; candidature a bandi di rigenerazione; valutazione di proposte in partenariato.",
 vantaggi="I bandi coprono il CAPEX ma quasi mai l'OPEX: chi lo sa scrive progetti sostenibili e vince piu' spesso; il partenariato con ESCo sposta il rischio energetico su chi lo gestisce; i livelli di servizio contrattuali rendono misurabile la qualita' del fornitore.",
 limiti="Il finanziamento a bando crea il 'peccato originale': servizi nati senza copertura di gestione; i canoni cloud crescono con i dati raccolti (il successo costa); il partenariato mal scritto lascia al comune i rischi e al privato i margini; la mancanza di personale comunale formato rende l'ente dipendente dal fornitore per ogni variazione.",
 costi_e_economia="Ordini di grandezza indicativi: programma smart triennale di un comune medio 1-5 M€ di CAPEX con 0,1-0,6 M€/anno di OPEX; gara di servizio illuminazione+energia in partenariato: investimento del privato 1-10 M€ ripagato dai risparmi condivisi in 8-15 anni; formazione e presidio interno 30-80 k€/anno: la voce che decide se il programma sopravvive al cambio di giunta.",
 casi_real_world="Caso tipo: comune che candida a un bando di rigenerazione solo i servizi con OPEX coperto da bilancio o da canone di servizio, rinunciando a due linee scenografiche non gestibili: progetto finanziato, servizi ancora attivi a cinque anni di distanza.",
 normative="D.Lgs 36/2023 (appalti e concessioni di servizi); disciplina del partenariato pubblico-privato; regole dei programmi di finanziamento nazionali ed europei (da verificare bando per bando); D.Lgs 118/2011 e armonizzazione contabile per l'iscrizione a bilancio degli OPEX.",
 note_cantiere="Quando valuti un progetto smart, chiedi il piano di gestione a dieci anni prima del rendering: chi paga, chi ripara, chi aggiorna. Se il piano non c'e', non e' un progetto: e' un gadget con la data di scadenza."
)

add(
 categoria="Servizi urbani",
 nome="Rifiuti urbani smart: cassonetti sensorizzati, raccolta a misura e tariffazione puntuale",
 descrizione="La raccolta dei rifiuti e' il servizio dove i sensori cambiano i conti: cassonetti che dicono quando sono pieni, raccolte pianificate sul riempimento reale invece che sul calendario, tariffe calcolate su quanto si conferisce davvero.",
 tecnologia="Componenti: sensori di livello a ultrasuoni nei cassonetti (batteria 3-7 anni, rete LoRaWAN o NB-IoT); piattaforma di ottimizzazione dei giri di raccolta (meno km, meno mezzi); sistemi di accesso con riconoscimento utenza (tessera, transponder) per la tariffazione puntuale: il conferimento si pesa e si addebita all'utente; isole ecologiche presidiate con telecamere e prenotazione; integrazione con il gestore della raccolta e con la bollettazione TARI; per la raccolta porta a porta: tag RFID sui contenitori e lettura sui mezzi.",
 applicazioni="Cestini e cassonetti stradali nei centri e nei parchi; raccolta domiciliare con tariffazione puntuale (premio per chi differenzia e riduce); gestione delle isole ecologiche; controllo degli abbandoni nei punti critici; piani comunali di riduzione dei rifiuti con dati misurati.",
 vantaggi="I giri di raccolta sul riempimento reale riducono chilometri e mezzi del 20-40% secondo la letteratura di settore e le esperienze documentate; la tariffazione puntuale e' l'unica leva che fa differenziare davvero (riduzioni del secco misurabili in un anno); meno straripamenti: il decoro si misura in foto prima/dopo; i dati di conferimento rendono la TARI equa e difendibile.",
 limiti="I sensori nei cassonetti subiscono vandalismo e sporco: la manutenzione e' una voce continua, non un optional; la tariffazione puntuale richiede mesi di comunicazione e una fase transitoria: introdurla d'imperio genera abbandoni selvaggi; l'integrazione con il gestore e' il punto vero: sensori del comune e mezzi del gestore devono parlarsi contrattualmente; sui piccoli numeri (pochi cassonetti) il risparmio non copre la piattaforma.",
 costi_e_economia="Ordini di grandezza indicativi: sensore di livello installato su cassonetto 150-400 euro/cad; piattaforma di ottimizzazione raccolta per un servizio comunale 20-80 k€ piu' canoni; sistema di accesso con riconoscimento e pesatura per centro di raccolta 15-50 k€/cad; la tariffazione puntuale ripaga in equita' e in riduzione del secco piu' che in risparmio diretto di raccolta.",
 casi_real_world="Caso tipo: comune collinare che sensorizza 350 cassonetti stradali e passa i giri da calendario a riempimento: mezzi in strada ridotti di un terzo, straripamenti quasi azzerati nei weekend, e dopo un anno di dati avvia la tariffazione puntuale sul porta a porta con una campagna pubblica trimestrale.",
 normative="D.Lgs 152/2006 (disciplina dei rifiuti) per le modalita' di raccolta e conferimento; regolazione ARERA del ciclo dei rifiuti urbani (metodo tariffario e obblighi di misura) per la TARI puntuale; GDPR per i dati di conferimento associati alle utenze; regolamento comunale di igiene urbana.",
 note_cantiere="Prima della tariffazione puntuale fai tre mesi di misura 'a secco': pesi e volumi registrati senza addebito, pubblicati per quartiere. Quando la tariffa parte, i numeri li conoscono gia' tutti e le contestazioni crollano: chi salta la misura preliminare la paga in ricorsi."
)

# --- scrittura schede.jsonl ---
p_jsonl = os.path.join(BASE, 'schede', 'schede.jsonl')
out = io.open(p_jsonl, 'w', encoding='utf-8', newline='\n')
for s in S:
    out.write(json.dumps(s, ensure_ascii=False) + '\n')
out.close()

# --- COURSE.yaml ---
course = """corso: "Smart city: sensoristica, piattaforme e servizi urbani"
facolta: "FACOLTA_GESTIONE_SISTEMA"
livello: "L2-L3"
schede: 12
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "Reg. UE 2016/679 (GDPR), D.Lgs 138/2024 (NIS2), D.Lgs 82/2005 (CAD), D.Lgs 36/2023 (appalti), D.M. 312/2021 (BIM), D.Lgs 152/2006, ARERA (servizio idrico), AGID (interoperabilita' e sicurezza PA), DPR 74/2013, D.Lgs 102/2014; bandi e programmi di finanziamento marcati da verificare"
nota_metodologica: "Architettura smart city, illuminazione pubblica intelligente, reti IoT (LoRaWAN/NB-IoT), piattaforma dati e control room, digital twin, mobilita' e ricarica EV, gestione idrica smart, edifici pubblici e BEMS, smart district, privacy e cybersecurity, economia (CAPEX/OPEX, partenariati). Distinta da domotica (scala edificio) e CAD/BIM (scala progetto): qui la scala urbana. Prezzi come fasce indicative; bandi chiusi segnalati come tali; nessun nome di azienda."
"""
open(os.path.join(BASE, 'COURSE.yaml'), 'w', encoding='utf-8').write(course)

# --- README.md ---
readme = """# Smart city: sensoristica, piattaforme e servizi urbani

Corso di livello L2-L3 (FACOLTA_GESTIONE_SISTEMA) sulla città intelligente a scala urbana: architettura a livelli (sensori, reti, piattaforma, applicazioni), illuminazione pubblica telegestita, reti IoT LoRaWAN e NB-IoT, piattaforma dati comunale e control room, digital twin urbano, mobilità smart e ricarica EV, gestione idrica (perdite, drenaggio, pre-allarmi), edifici pubblici e BEMS, smart district e rigenerazione, privacy/cybersecurity (GDPR, NIS2), economia dei progetti (CAPEX/OPEX, bandi, partenariati). Il filo conduttore: ogni servizio smart vive solo se ha titolare del dato, OPEX finanziato e livelli di servizio misurabili.

**Schede: 12** — formato JSONL con le 11 chiavi standard dell'Università dell'Edilizia.

Regola metodologica: scala urbana (distinta da domotica a scala edificio e da CAD/BIM a scala progetto); prezzi come fasce indicative con unità; bandi di finanziamento marcati «da verificare»; nessun nome di aziende.
"""
open(os.path.join(BASE, 'README.md'), 'w', encoding='utf-8').write(readme)

# --- verifica finale ---
rows = [json.loads(l) for l in open(p_jsonl, encoding='utf-8') if l.strip()]
assert len(rows) == 12, len(rows)
for r in rows:
    assert list(r.keys()) == KEYS, r['nome']
    assert 'aplicazioni' not in r and 'tegnologia' not in r
print('OK:', p_jsonl, '-', len(rows), 'schede, chiavi e ordine corretti')
