# -*- coding: utf-8 -*-
"""Giro AY (2026-11-13): EDILIZIA_CARCERARIA_PACK - 13 schede."""
import json, os

KEYS = ["categoria","nome","descrizione","tecnologia","applicazioni","vantaggi","limiti",
        "costi_e_economia","casi_real_world","normative","note_cantiere"]

S = []

S.append({
"categoria": "Quadro normativo",
"nome": "Edilizia penitenziaria: ordinamento, standard e attori",
"descrizione": "L'edilizia carceraria e' regolata dall'ordinamento penitenziario (L. 26 luglio 1975 n. 354 e regolamento di esecuzione DPR 30 giugno 2000 n. 230), dalle sentenze della Corte EDU sul sovraffollamento (in particolare il giudicato pilota Torreggiani c. Italia, 2013, che ha fissato il parametro dei 3 mq per detenuto come soglia di trattamento inumano) e dagli standard del CPT (Comitato europeo per la prevenzione della tortura): 6 mq per la cella singola, 4 mq per detenuto nelle celle a occupazione multipla, esclusi i servizi. Il D.Lgs 2 ottobre 2018 n. 123 ha rafforzato la sorveglianza dinamica, che cambia la progettazione degli spazi comuni. Gli attori: Dipartimento dell'amministrazione penitenziaria (DAP) e provveditorati regionali per la committenza, MIBACT per i vincoli su immobili storici, Regioni e enti locali per i nuovi insediamenti.",
"tecnologia": "Parametri di progetto: densita' abitativa regolamentare, rapporto tra posti letto regolamentari e capienza effettiva, ore di aria (spazi esterni) per detenuto, separazione dei circuiti (alta sicurezza, media sicurezza, custodia attenuata, lavoro all'esterno), spazi trattamentali per sezione. La pianificazione nazionale e' affidata a piani di edilizia penitenziaria adottati con atti del Ministro della giustizia (verificare l'atto vigente su giustizia.it).",
"applicazioni": "Case circondariali, case di reclusione, istituti per l'esecuzione delle misure di sicurezza, istituti a custodia attenuata (ICAM per madri con figli), sezioni per semiliberi, strutture di espansione di istituti esistenti.",
"vantaggi": "Normativa di settore chiara sui diritti minimi; parametri CPT/CEDU danno al progettista numeri certi; la domanda di nuova edilizia penitenziaria e' strutturale (sovraffollamento cronico) e finanziata da piani nazionali.",
"limiti": "Committenza unica e complessa (DAP); iter decisionali lunghi e soggetti a revisioni di piano; alto rischio di contenzioso sulle varianti; sensibilita' mediatica e politica elevata su ogni scelta.",
"costi_e_economia": "Ordini di grandezza indicativi: studi di fattibilita' e masterplan di istituto 200-800 k€; progettazione completa di un nuovo istituto medio 1,5-4 milioni; due diligence su istituto esistente 50-200 k€.",
"casi_real_world": "Caso reale noto: dopo Torreggiani (2013) l'Italia ha avviato piani di nuovi posti letto e misure deflattive; i provveditorati hanno attivato programmi pluriennali di ammodernamento con verifica puntuale dei mq per detenuto in ogni sezione.",
"normative": "L. 354/1975; DPR 230/2000; D.Lgs 123/2018 (sorveglianza dinamica); sentenza CEDU Torreggiani c. Italia (2013); standard CPT (Cooperazione: 6 mq cella singola, 4 mq/detenuto in multipla); D.Lgs 42/2004 per gli istituti storici.",
"note_cantiere": "Alla prima riunione con il provveditorato chiedi il dato sui posti REGOLAMENTARI e su quelli EFFETTIVI di ogni sezione: il progetto parte dalla differenza tra i due numeri, non dal rendering."})

S.append({
"categoria": "Progettazione",
"nome": "Tipologie di istituto e organizzazione in circuiti e sezioni",
"descrizione": "L'istituto penitenziario si organizza per circuiti (alta sicurezza, media sicurezza, custodia attenuata) e sezioni detentive autosufficienti: ogni sezione ha celle, spazi comuni (sala socialita', docce, cucinetta), accesso diretto o controllato alle aree passeggio e ai servizi. La logica progettuale moderna riduce il numero di detenuti per sezione (indicativamente 20-60) per consentire sorveglianza dinamica e attivita' trattamentali. Le tipologie edilizie: istituto a padiglioni radiali (Ottocento), a blocchi paralleli, a campus con edifici separati per funzione. Il perimetro separa il dentro dal fuori con cinta, spazi di rispetto e accessi filtrati (cancello d'ingresso con doppia porta interbloccata, il cosiddetto 'sacco' di sicurezza).",
"tecnologia": "Dimensionamento: superficie per detenuto (standard CPT), spazi comuni per sezione 1,5-3 mq/posto, aree passeggio con copertura minima e affaccio sull'esterno; percorsi separati per detenuti, operatori, merci e visitatori (colloqui); centrale di controllo con ridondanza; corpi di fabbrica con compartimentazione per sezione.",
"applicazioni": "Nuovi istituti; riorganizzazione di sezioni in istituti storici; realizzazione di reparti speciali (art. 41-bis, semiliberta', salute mentale).",
"vantaggi": "Sezioni piccole = meno tensioni e gestione piu' sicura; percorsi separati riducono i movimenti scortati e il personale impiegato; il modello a campus consente cantieri per lotti senza fermare l'istituto.",
"limiti": "Gli istituti storici radiali sono difficili da adattare agli standard moderni senza demolizioni interne; la separazione dei circuiti moltiplica gli spazi e i costi; ogni deroga agli standard va motivata e approvata dal DAP.",
"costi_e_economia": "Ordini di grandezza indicativi: costruzione nuovo istituto 2.500-4.500 €/mq; costo per posto detentivo nuovo 150-400 k€; riorganizzazione di una sezione esistente 0,5-2 milioni.",
"casi_real_world": "Caso tipo: riorganizzazione di una casa circondariale degli anni Trenta: riduzione della capienza regolamentare del 30%, creazione di spazi comuni per sezione ricavati da celle accorpate, nuovo percorso colloqui con parlatori senza contatto diretto per i colloqui visuali.",
"normative": "DPR 230/2000 (spazi e servizi degli istituti); L. 354/1975; standard CPT; atti di indirizzo del DAP su tipologie e parametri (verificare la versione vigente su giustizia.it).",
"note_cantiere": "In fase di layout, disegna prima il percorso del detenuto e poi quello delle merci: se i due si incrociano in un punto non presidiabile, hai progettato un problema di sicurezza, non un corridoio."})

S.append({
"categoria": "Progettazione",
"nome": "La cella: dimensioni, servizi, arredi e qualita' ambientale",
"descrizione": "La cella e' l'unita' abitativa coatta: deve garantire dignita' (standard CPT: 6 mq singola, 4 mq per detenuto in multipla, escluso il bagno), sicurezza (niente appigli, spigoli o parti smontabili utilizzabili come arma o per autolesionismo) e vivibilita' (luce naturale diretta, ventilazione, temperatura). Il bagno in cella e' ormai standard irrinunciabile: vano separato con porta o parete schermata, sanitari in acciaio inox o resina rinforzata, rubinetteria a comando pneumatico o elettronico antivandalico. Arredi fissi ancorati (brande, tavolino, sgabello), prese elettriche protette con alimentazione controllabile dalla centrale, intercom di chiamata, finestre con affaccio libero verso l'esterno (no muri a distanza ravvicinata) e schermi anti-lancio.",
"tecnologia": "Pareti interne con finiture lavabili e antigraffio; pavimenti in resina o gres con posa senza fughe larghe; serramenti di sicurezza con vetri stratificati e grate integrate nel telaio; comando luci centralizzato con luce notturna di cortesia; ventilazione meccanica controllata dove la finestra non basta; sensori di presenza fumo con rete dedicata.",
"applicazioni": "Celle ordinarie, celle di isolamento sanitario, celle attrezzate per detenuti disabili (bagno accessibile, arredi ribassati), camere di pernottamento per semiliberi.",
"vantaggi": "Il bagno in cella risolve la gran parte dei problemi igienici e di ordine notturni; gli arredi fissi riducono incidenti e manutenzione; la luce naturale diretta riduce l'aggressivita' e i costi di illuminazione diurna.",
"limiti": "Riqualificare le celle di istituti ottocenteschi (spesso sotto i 4 mq/detenuto in tripla) richiede l'accorpamento: si riducono i posti e serve l'accordo con l'amministrazione; i sanitari antivandalici costano 3-5 volte i normali.",
"costi_e_economia": "Ordini di grandezza indicativi: riqualificazione completa di una cella con nuovo bagno 15-40 k€; serramento di sicurezza con vetro stratificato e grata 3-8 k€ cad.; sanitario antivandalico inox 800-2.500 € cad.; arredo fisso cella 1,5-4 k€.",
"casi_real_world": "Caso tipo: programma pluriennale di installazione del bagno in cella in un istituto storico: cantiere per sezioni a rotazione, celle accoppiate a due a due, posa dei sanitari inox con tubazioni in cavedii tecnici ispezionabili per impedire occlusioni intenzionali.",
"normative": "Standard CPT; DPR 230/2000 (igiene e dotazioni); D.M. 236/1989 per le celle accessibili; UNI EN 1627 per la classificazione antieffrazione dei serramenti di sicurezza.",
"note_cantiere": "Ogni vite visibile in una cella e' un problema futuro: usa solo fissaggi antimanomissione (torx con perno, rivetti strutturali) e collauda ogni arredo con il tentativo di strappo, non con lo sguardo."})

S.append({
"categoria": "Sicurezza passiva",
"nome": "Serramenti, grate e chiusure di sicurezza: la pelle dell'istituto",
"descrizione": "Le chiusure di sicurezza in un istituto penitenziario lavorano su tre livelli: perimetro (cinta, portoni, recinzioni), edificio (facciate con grate e serramenti certificati) e locale (porte di cella e di sezione). Le porte di cella moderne sono blindate con elettroserratura a doppia tecnologia (comando centralizzato + chiave meccanica di emergenza), spioncino e cerniere interne; le finestre integrano grata di sicurezza nel telaio e vetro stratificato anti-sfondamento. La classificazione di riferimento per l'antieffrazione e' la UNI EN 1627 (classi RC): per i serramenti penitenziari si adottano classi elevate con resistenza anche dall'interno (fuga) e non solo dall'esterno (effrazione).",
"tecnologia": "Elettroserrature con monitoraggio di stato (porta aperta/chiusa/non bloccata) riportato in centrale; alimentazione ridondata con UPS; cilindri meccanici con profili riservati e duplicazione controllata; grate in tondi pieni o piatti sagomati saldati con continuita' certificata; vetri stratificati con pellicole multiple; canalizzazioni elettriche delle porte in cavidotti protetti.",
"applicazioni": "Celle, cancellate di sezione, parlatori, infermerie, archivi atti, armerie, cucine (coltelleria sotto controllo), laboratori con attrezzi.",
"vantaggi": "Il monitoraggio centralizzato dello stato delle porte riduce i giri di controllo fisici e i tempi di reazione; i serramenti certificati RC con vetro stratificato eliminano la doppia barriera grata+vetro tradizionale, migliorando luce e manutenzione.",
"limiti": "Le elettroserrature richiedono manutenzione specialistica e ricambi dedicati: un guasto senza ricambio blocca una sezione; i sistemi meccanici puri sono piu' lenti ma non si guastano mai: la ridondanza dei due sistemi e' la regola d'oro.",
"costi_e_economia": "Ordini di grandezza indicativi: porta di cella blindata con elettroserratura e controllo 4-10 k€ cad.; grata integrata in serramento 1,5-4 k€/mq; cancellata di sezione motorizzata 8-20 k€; centrale di controllo porte per sezione 30-100 k€.",
"casi_real_world": "Caso tipo: sostituzione delle porte di cella in un istituto anni Sessanta: fase 1 campione su 5 celle con prova di funzionamento in continuo per 30 giorni, poi estensione a 200 porte con collaudo porta per porta e consegna delle chiavi meccaniche di emergenza in busta sigillata alla direzione.",
"normative": "UNI EN 1627 (classi RC antieffrazione); UNI EN 1522/1523 (resistenza balistica) per i locali speciali; capitolati DAP per le chiusure penitenziarie (verificare la versione vigente); DPR 230/2000.",
"note_cantiere": "Collauda OGNI porta singolarmente con il comando centrale E con la chiave: l'elettroserratura che funziona in centrale ma non si apre di emergenza e' un rischio di vita, non un difetto di collaudo."})

S.append({
"categoria": "Spazi comuni",
"nome": "Spazi trattamentali, colloqui e aree passeggio: l'istituto oltre la cella",
"descrizione": "La funzione rieducativa della pena (art. 27 Cost.) si traduce in spazi: scuola e aule, biblioteca, laboratori di lavoro, sale sociali e attivita' per sezione, cappella/luoghi di culto, palestra e campo sportivo, sale colloqui con i familiari (ambienti normalizzati, non gabbie), colloqui visivi con i difensori, parlatori senza contatto diretto dove richiesto. Le aree passeggio (cortili esterni delle sezioni) devono garantire il tempo all'aperto previsto dall'ordinamento, con copertura parziale, affaccio visivo verso l'esterno, sedute e attrezzature fisse ancorate. Con la sorveglianza dinamica (D.Lgs 123/2018) questi spazi diventano il cuore della giornata detentiva e vanno progettati per l'uso prolungato, non come depositi.",
"tecnologia": "Sale colloqui familiari con finiture domestiche e percorsi separati; parlatori con divisorio vetrato stratificato e sistemi interfonici ridondati; laboratori con attrezzi inventariati e stoccati in armadi con conteggio; aree passeggio con superfici drenanti e illuminazione notturna; spazi verdi trattamentali dove il vincolo di sicurezza lo consente.",
"applicazioni": "Istituti di ogni circuito; in custodia attenuata gli spazi trattamentali sono la maggioranza del costruito; nelle sezioni di alta sicurezza i parlatori senza contatto sono lo standard.",
"vantaggi": "Spazi trattamentali adeguati riducono conflittualita' e atti di autolesionismo (evidenza consolidata nella letteratura penitenziaria); le sale colloqui dignitose migliorano il clima dell'intero istituto e il lavoro del personale.",
"limiti": "Negli istituti storici lo spazio per i servizi si ricava solo riducendo i posti letto o ampliando con nuovi corpi: entrambe le scelte sono politiche oltre che tecniche; i laboratori richiedono gestione rigorosa degli attrezzi (doppia firma in entrata/uscita).",
"costi_e_economia": "Ordini di grandezza indicativi: riqualificazione sala colloqui familiari 20-60 k€/sala; parlatorio senza contatto (postazione vetrata completa) 8-25 k€/posto; area passeggio attrezzata 300-700 €/mq; laboratorio produttivo allestito 50-150 k€.",
"casi_real_world": "Caso reale noto: i nuovi padiglioni realizzati con i piani carceri degli anni Duemiladieci hanno introdotto sale colloqui familiari normalizzate e aree passeggio con verde, con riduzione misurata degli eventi critici nelle sezioni interessate.",
"normative": "L. 354/1975 e DPR 230/2000 (attivita' trattamentali, colloqui, tempo all'aperto); D.Lgs 123/2018 (sorveglianza dinamica); D.M. 236/1989 (accessibilita' degli spazi comuni).",
"note_cantiere": "In una sala colloqui familiari non usare mai finiture 'da caserma': laminati caldi, colori chiari, una parete attrezzata per i giochi dei bambini. Costano come quelle tristi e lavorano il doppio sul clima dell'istituto."})

S.append({
"categoria": "Sicurezza perimetrale",
"nome": "Perimetro, cinta e recinzioni: il confine dell'istituto",
"descrizione": "Il perimetro penitenziario e' un sistema stratificato: cinta muraria (storica o in pannelli prefabbricati armati, altezza tipica 5-8 m), spazio di rispetto interno illuminato e videosorvegliato, seconda recinzione con rilevazione elettronica, camminamenti di ronda o torrette negli istituti storici, portone principale con sacca di sicurezza a due porte interbloccate. I sistemi di rilevazione perimetrale (microfoni su fibra, cavi piezoelettrici, radar, videosorveglianza analitica) segnalano scavalcamento, scavo e lancio; la gestione droni (consegne dal cielo) e' la voce piu' recente e in rapida evoluzione normativa e tecnologica.",
"tecnologia": "Pannelli di cinta prefabbricati con plinti e sopraelevazioni; fondazioni continue anti-scavo; illuminazione perimetrale schermata verso l'esterno (abbagliamento delle ronde interno); sensori di scavo e scavalcamento tarati sulle interferenze ambientali locali (fauna, vegetazione); cancelli carrai con blocco meccanico indipendente dall'automazione; percorsi di ronda protetti.",
"applicazioni": "Istituti di ogni tipologia; particolare attenzione agli istituti inseriti in tessuto urbano, dove il perimetro e' anche facciata sulla citta' e soggetto a vincolo paesaggistico.",
"vantaggi": "La stratificazione (fisico + elettronico + umano) rende l'evasione dal perimetro evento raro; la videosorveglianza analitica riduce i falsi allarmi e libera personale per la vigilanza diretta.",
"limiti": "La manutenzione del perimetro e' continua (vegetazione, corrosione, sensori degradati); i lanci con drone richiedono contromisure in evoluzione e non standardizzate; l'impatto urbano delle cinte storiche limita le modifiche possibili.",
"costi_e_economia": "Ordini di grandezza indicativi: cinta nuova in pannelli armati 800-2.000 €/m; rilevazione elettronica perimetrale 150-400 €/m; portone con sacca interbloccata 100-300 k€; videosorveglianza perimetrale analitica 50-150 k€ per istituto medio.",
"casi_real_world": "Caso tipo: adeguamento perimetrale di istituto urbano anni Cinquanta: sopraelevazione della cinta con pannelli prefabbricati rispettando il vincolo, nuova sacca d'ingresso con doppia porta interbloccata e magazzino merci filtrato, rilevazione anti-lancio sulla corte interna.",
"normative": "DPR 230/2000; capitolati DAP sulle opere di sicurezza perimetrale (verificare la versione vigente); D.Lgs 42/2004 per le cinte vincolate; normativa ENAC/ENAV per la gestione dei droni in prossimita' degli istituti.",
"note_cantiere": "La prima cosa da controllare in un sopralluogo di perimetro non sono i sensori: sono gli alberi a ridosso della cinta e i plinti sottosquadro. Il resto si aggiusta, quelli fanno evadere."})

S.append({
"categoria": "Impianti speciali",
"nome": "Impianti tecnologici di sicurezza: controllo centralizzato, video e comunicazioni",
"descrizione": "La centrale operativa di un istituto comanda: stato e comando delle porte (elettroserrature), videosorveglianza (centinaia di telecamere con registrazione certificata), interfonia di cella e di sezione, rilevazione intrusione e perimetrale, controllo accessi del personale e dei visitatori (registrazione, pass, conteggi metallici), gestione degli allarmi di aggressione del personale (radio portatili con localizzazione). Requisiti trasversali: ridondanza dei server, continuita' elettrica con UPS e gruppi elettrogeni, segregazione della rete di sicurezza dalla rete amministrativa, conservazione probatoria delle registrazioni.",
"tecnologia": "PLC di campo per i gruppi di porte con logica ridondata; supervisione SCADA con mappe sinottiche per sezione; telecamere antivandalo con copertura senza angoli ciechi nei punti critici; interfoni di cella a chiamata selettiva con registrazione; analitiche video (oggetti abbandonati, attraversamenti, assembramenti); gestione delle chiavi meccaniche con armadi elettronici a tracciamento.",
"applicazioni": "Ogni istituto; la complessita' cresce con i circuiti multipli e con le sezioni speciali (41-bis, sanitari).",
"vantaggi": "La centrale unica riduce il personale di sorveglianza statica e migliora i tempi di reazione; la tracciabilita' completa (chi ha aperto cosa e quando) e' la prima prova in ogni indagine interna.",
"limiti": "Obsolescenza rapida: i sistemi di 15 anni fa sono spesso non piu' supportati; il cablaggio storico in cavedii condivisi complica gli upgrade; cybersecurity: la rete di sicurezza va trattata come infrastruttura critica.",
"costi_e_economia": "Ordini di grandezza indicativi: centrale operativa completa per istituto medio 0,5-1,5 milioni; videosorveglianza 200-500 €/punto ripreso installato; interfonia di cella 150-400 €/cella; manutenzione annua impianti di sicurezza 5-10% del valore.",
"casi_real_world": "Caso tipo: rinnovo della centrale di controllo di un istituto da 400 posti: migrazione notturna per sezioni, doppio esercizio (vecchia+nuova) per 15 giorni, formazione del personale su banco prova prima del passaggio definitivo.",
"normative": "DPR 230/2000; capitolati DAP sugli impianti di sicurezza (verificare la versione vigente); GDPR e normativa sulla videosorveglianza nei luoghi di lavoro e di detenzione; CEI 64-8 per le parti elettriche.",
"note_cantiere": "Quando rinnovi la centrale, non smantellare mai la vecchia prima di due settimane di doppio esercizio: la notte in cui la nuova si blocca e' la notte in cui serve quella vecchia ancora accesa."})

S.append({
"categoria": "Antincendio ed emergenze",
"nome": "Antincendio in istituto penitenziario: evacuare chi non puo' fuggire",
"descrizione": "La strategia antincendio negli istituti penitenziari non puo' contare sull'esodo immediato: le persone detenute sono fisicamente vincolate. Il progetto si basa su: compartimentazione spinta per sezione (porte REI, tagliafuoco sulle vie di collegamento), protezione attiva estesa (rilevazione in ogni cella con rete dedicata e tamper, idranti interni sotto controllo del personale, sprinkler ove compatibile), procedure di evacuazione assistita verso aree di raccolta protette interne (cortili di sezione) prima ancora che verso l'esterno, gestione fumi nelle gallerie di distribuzione. La prevenzione incendi degli istituti e' soggetta ai controlli dei VVF secondo la classificazione delle attivita' (categoria di attivita' da verificare sull'elenco del DPR 151/2011 e s.m.i. per la specifica realta').",
"tecnologia": "Rilevazione fumi di cella con segnalazione indirizzata in centrale; estintori e naspi nelle posizioni accessibili solo al personale; porte REI con elettroserratura svincolabile su allarme con ridondanza; piani di emergenza con evacuazione orizzontale per compartimenti; esercitazioni con personale e (ove previsto) con detenuti formati; gestione dei presidi medici di sezione per l'evacuazione di detenuti non deambulanti.",
"applicazioni": "Tutti gli istituti; criticita' massima nelle sezioni di alta sicurezza e nei piani alti degli istituti storici multipiano.",
"vantaggi": "La compartimentazione per sezione allinea antincendio e sicurezza detentiva (stesso perimetro); la rilevazione indirizzata in ogni cella abbatte i tempi di intervento sui focolai piu' frequenti (materassi, piccoli focolai dolosi).",
"limiti": "L'evacuazione assistita richiede personale numeroso e formato: i turni notturni sono il punto debole; i focolai intenzionali sono piu' frequenti che altrove e i dispositivi vanno protetti dalla manomissione; l'adeguamento degli istituti storici e' costoso e lento.",
"costi_e_economia": "Ordini di grandezza indicativi: adeguamento antincendio di sezione storica 150-500 k€; rilevazione indirizzata per cella 300-700 €/cella; porta REI con svincolo e monitoraggio 2-5 k€; piano di emergenza ed esercitazioni 20-60 k€/anno.",
"casi_real_world": "Caso tipo: incendio doloso di materasso in cella notturna: rilevazione indirizzata, intervento del personale di sezione in 4 minuti, compartimento chiuso, nessuna evacuazione generale necessaria; il verbale VVF ha registrato la conformita' della procedura.",
"normative": "DPR 151/2011 e s.m.i. (classificazione attivita' da verificare); Codice di prevenzione incendi (D.M. 3/8/2015 e s.m.i.) per gli approcci prestazionali; DPR 230/2000; D.Lgs 81/2008 per il personale.",
"note_cantiere": "Ogni rivelatore di cella lo installi e poi provi a raggiungerlo come farebbe un detenuto con un asciugamano bagnato: se lo copri o lo stacchi con un gesto, cambia modello o posizione prima del collaudo."})

S.append({
"categoria": "Sanita' penitenziaria",
"nome": "Aree sanitarie, REMS e salute in istituto: progettare per la cura in custodia",
"descrizione": "L'istituto ospita un presidio sanitario: ambulatori, infermeria con camere di degenza osservata, servizio odontoiatrico, spazi per la salute mentale, farmacia con stoccaggio controllato. Le REMS (residenze per l'esecuzione delle misure di sicurezza) sono strutture sanitarie con custodia: piccole (fino a 20-30 posti), organizzate come residenze protette, con doppia committenza sanitaria-regionale e penitenziaria. Le esigenze architettoniche: percorsi separati per i detenuti pazienti, sale d'attesa schermate, camere di osservazione con controllo visivo continuo e arredi anti-autolesionismo, accesso diretto e filtrato per le ambulanze.",
"tecnologia": "Camere di degenza con vetri di osservazione stratificati e arredi ancorati; porte con apertura centralizzata e sblocco sanitario di emergenza; stoccaggio farmaci con armadi doppia firma e tracciamento; impianti a norma sanitaria (ventilazione, finiture lavabili) integrati con i vincoli di sicurezza; percorsi ambulanza con cancello dedicato.",
"applicazioni": "Presidi sanitari di istituto; sezioni di medicina protetta negli ospedali (camere blindate per detenuti ricoverati); REMS; centri di salute mentale penitenziaria.",
"vantaggi": "Un presidio ben progettato riduce i trasferimenti esterni (costi, rischi di sicurezza, code sanitarie); le camere di osservazione ben fatte riducono gli eventi di autolesionismo; la doppia logica sanitaria+sicurezza risolta in progetto evita i conflitti quotidiani tra medici e polizia penitenziaria.",
"limiti": "Doppia committenza = doppio tavolo decisionale su ogni finitura; i costi al mq sono i piu' alti dell'istituto; il personale sanitario lavora con vincoli di sicurezza che richiedono formazione specifica continua.",
"costi_e_economia": "Ordini di grandezza indicativi: presidio sanitario di istituto medio 0,5-1,5 milioni; camera di osservazione attrezzata 40-100 k€; REMS di nuova costruzione 3.500-5.500 €/mq; riqualificazione ambulatorio 100-300 k€.",
"casi_real_world": "Caso reale noto: la chiusura degli ospedali psichiatrici giudiziari (avviata con la L. 9/2012 e completata negli anni successivi) ha trasferito la casistica alle REMS, con programma nazionale di nuove residenze di piccola taglia diffuse sul territorio.",
"normative": "L. 9/2012 (superamento OPG); DPR 230/2000 (assistenza sanitaria); standard CPT; normativa sanitaria regionale per l'accreditamento dei presidi; D.M. 236/1989.",
"note_cantiere": "Nelle camere di osservazione conta quello che NON c'e': niente appigli, niente spigoli, niente elementi smontabili, niente punti ciechi. Fai il giro della stanza finita con l'infermiere capo, non solo con il collaudatore."})

S.append({
"categoria": "Recupero",
"nome": "Ex carceri: dismissione, restauro e riconversione degli edifici penitenziari storici",
"descrizione": "Il patrimonio penitenziario storico (panopticon ottocenteschi, ex conventi e fortezze convertiti) si dismette lentamente e si riconverte con fatica: vincolo culturale (D.Lgs 42/2004), strutture pensate per il controllo (spessori murari enormi, grate, celle) e storia scomoda da raccontare. Le riconversioni riuscite: musei e memoriale, universita', residenze, alberghi, spazi culturali. Il progetto di riconversione parte dalla documentazione (rilievo, analisi storica, carte dei vincoli) e decide cosa conservare come memoria (una sezione con celle originali, il percorso di ronda) e cosa trasformare radicalmente.",
"tecnologia": "Rilievo laser scanner e HBIM per le strutture complesse; indagini su murature e volte prima di ogni apertura; conservazione programmata degli elementi identitari (grate, porte, scritte delle celle come palinsesto storico); adeguamento sismico e antincendio con tecniche compatibili (fibre, rinforzi locali); gestione dell'amianto e delle vernici al piombo tipiche dei cantieri di recupero novecenteschi.",
"applicazioni": "Musei della memoria e dell'ordinamento penitenziario; campus universitari e scuole; residenze e studentati; hospitality culturale; spazi per la giustizia riparativa.",
"vantaggi": "Ubicazioni centrali e complessi monumentali; la memoria conservata da' valore culturale e turistico alla riconversione; finanziamenti disponibili sui bandi culturali e di rigenerazione urbana.",
"limiti": "Vincoli stringenti su ogni modifica delle parti storiche; costi di adeguamento normativo (sismico, antincendio, accessibilita') alti su edifici pensati per non essere attraversabili; bonifiche da amianto quasi sempre presenti.",
"costi_e_economia": "Ordini di grandezza indicativi: riconversione culturale/museale 1.500-3.500 €/mq; riconversione residenziale/alberghiera 1.800-4.000 €/mq; solo messa in sicurezza e conservazione 300-800 €/mq; rilievo e HBIM di complesso medio 50-150 k€.",
"casi_real_world": "Casi reali noti: l'ex carcere delle Murate a Firenze riconvertito a residenze, commerciale e spazi culturali conservando il cortile e parti delle celle; altre ex case circondariali riconvertite a sedi universitarie e musei della memoria in diverse citta' italiane.",
"normative": "D.Lgs 42/2004; NTC D.M. 17/1/2018 (cap. 8 costruzioni esistenti); D.Lgs 81/2008 Titolo IX (amianto in bonifica); linee guida MIBACT per la conservazione (riferimento generale).",
"note_cantiere": "Prima del primo getto in un ex carcere, mappa TUTTE le aperture murate e i passaggi segreti: ogni ex istituto ne ha, e scoprirli a struttura finita costa dieci volte tanto."})

S.append({
"categoria": "Nuove costruzioni",
"nome": "Progettare il nuovo istituto: tipologie moderne e cantiere da zero",
"descrizione": "Il nuovo istituto penitenziario moderno abbandona il panopticon per il modello a campus: edifici separati per funzione (sezioni detentive, servizi, lavoro, sanita', amministrazione), perimetro compatto, sezioni piccole con spazi comuni dignitosi, verde interno controllato. Il progetto integra fin dal concept: sicurezza passiva (geometrie senza angoli ciechi, facciate con serramenti certificati), sostenibilita' (CAM edilizia, D.M. 11 ottobre 2017, obbligatoria per la committenza pubblica), manutenibilita' (cavedii ispezionabili, materiali durevoli), flessibilita' (sezioni riconvertibili tra circuiti). La committenza (DAP/provveditorati) lavora per piani e lotti con finanziamenti pluriennali.",
"tecnologia": "Strutture in c.a. o prefabbricate con finiture antivandalo; involucro ad alta efficienza (NZEB per la PA); impianti centralizzati con ridondanza; BIM obbligatorio per le soglie di appalto pubblico; cantiere organizzato per lotti funzionali con collaudi parziali; arredi e serramenti di sicurezza a capitolato DAP.",
"applicazioni": "Nuovi istituti su aree libere; espansioni con nuovi padiglioni in aree di pertinenza; sostituzione completa di istituti obsoleti.",
"vantaggi": "Il modello a campus riduce i costi di gestione (percorsi corti, sezioni autosufficienti); i CAM impongono materiali durevoli che abbattono la manutenzione; la nuova costruzione consente standard CPT pieni dal primo giorno.",
"limiti": "Iter autorizzativi e finanziari lunghi (5-10 anni dalla decisione all'apertura); contestazione locale sugli insediamenti (sindrome NIMBY rovesciata: nessuno vuole il carcere, tutti vogliono i posti di lavoro); costi fissi di gestione da sostenere a regime.",
"costi_e_economia": "Ordini di grandezza indicativi: nuovo istituto medio (300-600 posti) 60-200 milioni complessivi; costo per posto 150-400 k€; opere esterne e perimetro 10-20% del totale; progettazione BIM completa 3-6% dell'importo lavori.",
"casi_real_world": "Caso tipo: nuovo istituto a campus da 500 posti su area libera: 6 padiglioni detentivi da 80 posti, edificio servizi centrale, perimetro compatto con doppia recinzione; finanziamento a lotti su piano pluriennale, apertura per sezioni progressive con collaudi separati.",
"normative": "DPR 230/2000; standard CPT; D.M. 11/10/2017 (CAM edilizia); D.Lgs 50/2016 (codice appalti, ora D.Lgs 36/2023: verificare il riferimento vigente); D.Lgs 81/2008 per il cantiere.",
"note_cantiere": "Nel concept del nuovo istituto, la prima domanda al committente e' sempre: quanti posti per sezione e quale circuito prevalente? La risposta decide la forma di tutto il resto."})

S.append({
"categoria": "Cantiere in istituto",
"nome": "Lavorare dentro un istituto in esercizio: logistica, scorte e regole del cantiere protetto",
"descrizione": "Il cantiere in istituto operativo e' un cantiere dentro un organismo che non si ferma mai: le aree di lavoro sono separate con recinzioni fisiche presidiate; il personale e' soggetto a verifiche di ingresso (documenti, controlli, talvolta veto su parentele con detenuti); attrezzi e materiali entrano ed escono contati (registro attrezzi, doppia firma); gli oggetti pericolosi (lame, solventi, corde, pile) sono inventariati e stoccati sotto chiave; i contatti tra operai e detenuti sono vietati e presidiati; le emergenze seguono procedure dedicate (allarme istituto = stop lavori e raccolta in punti definiti). Il coordinatore per la sicurezza lavora fianco a fianco con la sicurezza penitenziaria: due piani, un solo cantiere.",
"tecnologia": "Registro attrezzi con conteggio giornaliero entrata/uscita; ponte radio dedicato con il comando; casseforti per lame e sostanze pericolose; badge e passaggi filtrati con controllo biometrico o visivo; separazione fisica delle aree con barriere piene; piani di emergenza integrati (cantiere + istituto); formazione specifica del personale prima dell'ingresso (regole, divieti, comportamenti).",
"applicazioni": "Riqualificazioni di sezioni, manutenzioni straordinarie, nuovi corpi in aree interne, lavori su impianti tecnologici in esercizio.",
"vantaggi": "Regole chiare e presidio costante riducono i furti e le interferenze rispetto a un cantiere urbano aperto; il conteggio attrezzi, fatto bene, e' anche un ottimo controllo di avanzamento materiali.",
"limiti": "Produttivita' ridotta (stimata 10-25% in meno per ingressi, controlli e vincoli di orario); ingressi e uscite consumano ore uomo; ogni oggetto dimenticato e' un evento di sicurezza; pochi impresi hanno esperienza specifica: la formazione del personale e' la prima voce di costo nascosta.",
"costi_e_economia": "Ordini di grandezza indicativi: maggiorazione dei costi di cantiere in istituto 10-25% rispetto al cantiere libero; formazione e iter autorizzativi del personale 100-300 €/operaio; recinzioni presidiate e magazzino attrezzi 20-80 k€ per cantiere medio.",
"casi_real_world": "Caso tipo: sostituzione delle finestre di una sezione in esercizio: cantiere di 4 mesi con 2 operai dedicati ai conteggi attrezzi, lavori cella per cella con trasferimento temporaneo dei detenuti in sezione satellite, consegna quotidiana firmata delle lame e dei solventi.",
"normative": "D.Lgs 81/2008 (PSC, POS, CSP/CSE); DPR 230/2000 (regole dell'istituto applicate al cantiere); accordi cantiere-provveditorato (documento di cantiere specifico, verificare il modulo in uso presso il provveditorato competente).",
"note_cantiere": "Il martello dimenticato sul ponteggio chiude il cantiere una settimana: fai il conteggio attrezzi a pranzo e a sera, sempre, con due firme, anche quando hai fretta. Specialmente quando hai fretta."})

S.append({
"categoria": "Economia e gestione",
"nome": "Costi, appalti e manutenzione dell'edilizia penitenziaria",
"descrizione": "L'edilizia penitenziaria costa piu' dell'edilizia ordinaria: sicurezza passiva, impianti speciali, materiali antivandalo e cantieri protetti portano i costi al mq a 1,5-2,5 volte quelli di una scuola. La committenza e' pubblica (DAP, provveditorati) con appalti secondo il codice dei contratti; i lavori di sicurezza possono avere vincoli di riservatezza sulle tavole sensibili (planimetrie di porte e impianti). La manutenzione programmata e' critica: un istituto degradato genera costi di gestione crescenti (personale in piu' per supplire ai guasti, contenziosi, emergenze). Il facility management penitenziario e' un mercato specialistico con contratti integrati (manutenzione + servizi).",
"tecnologia": "Computi metrici con voci specifiche (porte blindate, grate, elettroserrature, controllo centralizzato); piani di manutenzione per sottosistemi (serramenti, impianti di sicurezza, sanita'); contratti di global service con SLA sui tempi di ripristino dei dispositivi di sicurezza; gestione documentale riservata per le tavole sensibili; banche dati prezzi DAP per i lavori ricorrenti.",
"applicazioni": "Nuove costruzioni; programmi di manutenzione straordinaria; contratti di facility; adeguamenti normativi programmati.",
"vantaggi": "Domanda stabile e finanziata da piani nazionali; specializzazione difendibile (pochi concorrenti qualificati); la manutenzione programmata riduce i costi totali di gestione del 15-30% rispetto alla gestione a guasto.",
"limiti": "Pagamenti e iter amministrativi lenti; varianti in corso d'opera soggette a controlli stringenti; la riservatezza sulle tavole complica subappalti e forniture; il mercato e' concentrato su pochi committenti.",
"costi_e_economia": "Ordini di grandezza indicativi: costruzione 2.500-4.500 €/mq; manutenzione ordinaria programmata 25-60 €/mq/anno; contratto di facility integrato per istituto medio 0,5-2 milioni/anno; costo di gestione per posto detentivo 3-8 k€/anno (quota immobiliare).",
"casi_real_world": "Caso tipo: provveditorato che passa dalla manutenzione a chiamata al contratto di facility con SLA: tempi di ripristino porte di sicurezza da 72 a 8 ore, costi annuali scesi del 18% in tre anni, verbali VVF e CPT piu' ordinati.",
"normative": "D.Lgs 36/2023 (codice appalti: verificare il testo vigente e le soglie); DPR 230/2000; D.M. 11/10/2017 (CAM) per la committenza pubblica; normativa sulla riservatezza degli atti per le tavole sensibili (riferimento generale).",
"note_cantiere": "In un appalto penitenziario metti in computo una voce 'controlli e doppie firme' con le ore vere: chi la dimentica lavora gratis un giorno alla settimana."})

S.append({
"categoria": "Prospettive",
"nome": "Diritti, standard europei e futuro dell'edilizia penitenziaria",
"descrizione": "L'edilizia carceraria si muove dove si muovono i diritti: gli standard CPT e le sentenze CEDU spingono verso spazi minimi garantiti, normalizzazione degli ambienti, eliminazione delle condizioni degradanti. Le prospettive tecniche: istituti piu' piccoli e diffusi (vicinanza ai territori e alle famiglie), tecnologie di sicurezza meno visibili e piu' integrata (sensori al posto delle sbarre dove possibile), sostenibilita' energetica obbligatoria per la committenza pubblica, spazi trattamentali come parte strutturale del programma. La progettazione penitenziaria e' sempre piu' un lavoro di equilibrio tra sicurezza, dignita' e costi di gestione: chi progetta una cella progetta un pezzo di giustizia.",
"tecnologia": "Modelli abitativi normalizzati (celle come camere con servizi); sicurezza basata su sensori e geometrie invece che su barriere visibili; edifici NZEB con monitoraggio dei consumi; spazi modulari riconvertibili tra circuiti; verde terapeutico e aree esterne qualificate.",
"applicazioni": "Nuovi piani di edilizia penitenziaria; programmi di riduzione del sovraffollamento; riconversione di edifici pubblici dismessi a custodia attenuata; progettazione europea comparata.",
"vantaggi": "Gli standard europei danno al progettista parametri certi e difendibili; gli istituti piccoli riducono i costi di gestione e migliorano gli esiti trattamentali (evidenza comparata consolidata).",
"limiti": "I vincoli di bilancio spingono verso grandi numeri e grandi istituti, in tensione con gli standard; l'innovazione tecnologica in ambiente penitenziario richiede validazioni lunghe; la dimensione etica del progetto non e' delegabile a nessun capitolato.",
"costi_e_economia": "Ordini di grandezza indicativi: progettazione e consulenza per studi di standard europei 30-150 k€; audit CPT-style su istituto esistente 20-80 k€; masterplan di riduzione sovraffollamento per provveditorato 100-400 k€.",
"casi_real_world": "Caso tipo: audit su istituto storico con matrice CPT: misurazione reale dei mq per detenuto per sezione, verifica bagni in cella e ore di aria effettive, piano di interventi in tre lotti con obiettivo conformita' in 36 mesi.",
"normative": "Standard CPT (Consiglio d'Europa); sentenze CEDU (Torreggiani 2013 e successiva giurisprudenza); L. 354/1975 e DPR 230/2000; art. 27 Cost.",
"note_cantiere": "Quando misuri una cella per l'audit, misura il pavimento libero e non quello disegnato: gli armadi e i muri fuori squadro mangiano sempre mezzo metro, e quel mezzo metro puo' essere la differenza tra conforme e non conforme."})

assert len(S) == 14, len(S)
for r in S:
    assert list(r.keys()) == KEYS, list(r.keys())
    assert r["costi_e_economia"].startswith("Ordini di grandezza indicativi: ")
    txt = json.dumps(r, ensure_ascii=False)
    assert "aplicazioni" not in txt and "tegnologia" not in txt

base = os.path.join("UNIVERSITA_EDILIZIA", "EDILIZIA_CARCERARIA_PACK")
os.makedirs(os.path.join(base, "schede"), exist_ok=True)
with open(os.path.join(base, "schede", "schede.jsonl"), "w", encoding="utf-8", newline="") as f:
    for r in S:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

with open(os.path.join(base, "COURSE.yaml"), "w", encoding="utf-8", newline="") as f:
    f.write(
"nome: Edilizia Carceraria e Penitenziaria\n"
"codice: EDILIZIA_CARCERARIA\n"
"pack: EDILIZIA_CARCERARIA_PACK\n"
"livello: L1-L2\n"
"schede: 14\n"
"facolta: FACOLTA_TECNOLOGIA_E_COSTRUZIONE\n"
"prerequisiti: [FONDAMENTI, SICUREZZA_ANTINCENDIO_ACCESSIBILITA, RESTAURO_E_CONSERVAZIONE_OPERE]\n"
"giro: AY\n"
"data: 2026-11-13\n")

with open(os.path.join(base, "README.md"), "w", encoding="utf-8", newline="") as f:
    f.write(
"# EDILIZIA_CARCERARIA_PACK — Edilizia Carceraria e Penitenziaria\n\n"
"Pack dedicato alla progettazione, costruzione e gestione degli istituti di pena:\n"
"quadro normativo (L. 354/1975, DPR 230/2000, D.Lgs 123/2018, standard CPT e\n"
"giurisprudenza CEDU Torreggiani), tipologie e circuiti, progettazione della cella\n"
"(standard 6/4 mq, bagno in cella, arredi anti-autolesionismo), serramenti e\n"
"chiusure di sicurezza (UNI EN 1627), spazi trattamentali e colloqui, perimetro e\n"
"cinta, impianti tecnologici di sicurezza (controllo centralizzato porte, video),\n"
"antincendio per persone non libere, sanita' penitenziaria e REMS, riconversione\n"
"degli ex carceri storici, nuove costruzioni a campus, cantiere in istituto in\n"
"esercizio, economia e facility, prospettive europee.\n\n"
"**Schede:** 14 | **Livello:** L1-L2 | **Facolta':** FACOLTA_TECNOLOGIA_E_COSTRUZIONE\n"
"**Esame:** ESAMI/EDILIZIA_CARCERARIA (250 domande)\n\n"
"Aggiunto nel Giro AY (2026-11-13).\n")

print(f"OK: {len(S)} schede scritte in {os.path.abspath(os.path.join(base,'schede','schede.jsonl'))}")
