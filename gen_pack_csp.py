# -*- coding: utf-8 -*-
import json, io, os

BASE = r'UNIVERSITA_EDILIZIA/SOLARE_TERMODINAMICO_CSP_PACK'
os.makedirs(os.path.join(BASE, 'schede'), exist_ok=True)

KEYS = ['categoria','nome','descrizione','tecnologia','applicazioni','vantaggi','limiti',
        'costi_e_economia','casi_real_world','normative','note_cantiere']

S = []
def add(**kw):
    assert list(kw.keys()) == KEYS, list(kw.keys())
    assert kw['costi_e_economia'].startswith('Ordini di grandezza indicativi: '), kw['nome']
    S.append(kw)

add(
 categoria="Fondamenti",
 nome="Il solare a concentrazione (CSP): principio e famiglie di impianto",
 descrizione="Il solare termodinamico concentra la radiazione diretta del sole con specchi per riscaldare un fluido a alta temperatura e produrre elettricita' con un ciclo termodinamico. A differenza del fotovoltaico usa solo la componente diretta (DNI) e puo' accumulare calore: e' una centrale termoelettrica alimentata dal sole.",
 tecnologia="Principio: specchi concentrano la radiazione diretta normale (DNI) su un ricevitore dove un fluido termovettore (olio diatermico, sali fusi, aria o vapore) raggiunge 290-565 gradi C secondo la tecnologia; il calore alimenta un ciclo Rankine a vapore (o cicli avanzati). Famiglie: collettori parabolici lineari (tecnologia matura), torri solari a ricevitore centrale, linear Fresnel, dish-Stirling (nicchia). Requisito di sito: DNI annua tipicamente superiore a 1.800-2.000 kWh/m2 per impianti elettrici competitivi; l'accumulo termico (sali fusi) permette produzione differibile di 3-15 ore.",
 applicazioni="Produzione elettrica utility-scale nelle regioni a alta DNI (Sud Italia, isole maggiori); calore di processo industriale a media temperatura; impianti ibridi con accumulo per coprire le ore serali; desalinizzazione accoppiata.",
 vantaggi="Energia rinnovabile programmabile grazie all'accumulo termico (valore sistemico superiore al fotovoltaico puro); componentistica meccanica convenzionale nel blocco di potenza; in Italia filiera e competenze reali maturate su impianti dimostrativi e di prima generazione; sinergia con l'industria esistente (componenti, specchi, caldereria).",
 limiti="Richiede DNI elevata: al Centro-Nord la resa crolla rispetto al Sud; taglie economiche grandi (decine di MW) e CAPEX elevato; complessita' di cantiere e di esercizio superiore al fotovoltaico; competizione di prezzo con FV+batterie che si e' mossa molto velocemente.",
 costi_e_economia="Ordini di grandezza indicativi: CAPEX di impianti a collettori parabolici con accumulo 4.000-7.000 euro/kW installato; costo livellato dell'energia (LCOE) di letteratura 0,12-0,20 euro/kWh secondo sito e ore di accumulo; superficie del campo solare 2-4 ettari per MW; i sistemi a media temperatura per calore di processo hanno CAPEX piu' contenuti (300-700 euro/m2 di collettore).",
 casi_real_world="Caso reale: in Sicilia e' in esercizio dal 2010 il primo impianto al mondo a collettori parabolici che usa i sali fusi sia come fluido termovettore sia come accumulo (circa 5 MW elettrici), dimostrando la produzione solare anche nelle ore notturne; in Spagna impianti da 50 MW con 7,5 ore di accumulo hanno mostrato produzione continua 24 ore in estate.",
 normative="D.Lgs 28/2011 (fonti rinnovabili: il CSP e' FER elettrica); D.Lgs 387/2003 (autorizzazione unica per impianti FER); D.Lgs 152/2006 (VIA per grandi impianti); decreti incentivi FER (D.M. 4/7/2019 e successivi, verificare il vigente per i nuovi impianti).",
 note_cantiere="Se ti propongono un CSP in un sito senza una misura DNI di almeno un anno solare (stazione meteo dedicata, non mappe), fermati: la differenza tra mappa e misura si paga in produzione per vent'anni."
)

add(
 categoria="Tecnologie di campo solare",
 nome="Collettori parabolici lineari: la tecnologia matura del CSP",
 descrizione="I collettori parabolici (parabolic trough) sono la tecnologia CSP piu' installata al mondo: file di specchi cilindro-parabolici inseguono il sole su un asse e concentrano la radiazione su un tubo ricevitore posto nel fuoco.",
 tecnologia="Struttura: modulo di specchi parabolici (apertura tipica 5-6 m, lunghezza modulo 12 m, loop da 100-150 m) montati su struttura metallica con inseguimento monoassiale nord-sud; tubo ricevitore in acciaio con trattamento selettivo dentro campana di vetro sotto vuoto; fluido termovettore: olio diatermico (limite circa 390-400 gradi C) oppure sali fusi (fino a circa 550 gradi C, come nell'impianto dimostrativo italiano); il campo solare alimenta scambiatori che producono vapore surriscaldato per la turbina; controllo di allineamento critico: errore di puntamento oltre pochi milliradianti degrada la resa ottica.",
 applicazioni="Impianti elettrici utility-scale 5-100 MW; impianti ibridi FER; repowering con accumulo a sali fusi; calore di processo a 250-400 gradi C per industrie (con taglie ridotte).",
 vantaggi="Tecnologia provata su gigawatt installati e decenni di esercizio; componenti industriali reperibili; l'inseguimento monoassiale semplifica struttura e controllo; integrazione diretta con accumulo a sali fusi a due serbatoi.",
 limiti="Peso e vento: le strutture devono resistere a raffiche con superfici esposte grandi (fondazioni dimensionate al vento); il vuoto dei tubi ricevitori si degrada nel tempo (sostituzioni programmate); l'olio diatermico limita la temperatura e richiede gestione antincendio; pulizia specchi con acqua in siti spesso aridi: serve logica di lavaggio (demineralizzata, notturna).",
 costi_e_economia="Ordini di grandezza indicativi: campo solare a trough 250-450 euro/m2 di apertura installato (struttura, specchi, ricevitori, fluido, controllo); tubo ricevitore sotto vuoto 800-1.500 euro/m lineare sostituito; manutenzione annua campo solare 1-3% del CAPEX del campo; lavaggio specchi: voce ricorrente da pianificare con risorsa idrica dedicata.",
 casi_real_world="Caso tipo: repowering di un impianto a olio diatermico con sostituzione del fluido in sali fusi e aggiunta di accumulo a due serbatoi: la temperatura di mandata sale da 390 a oltre 500 gradi C, migliorando il rendimento del ciclo e la capacita' di accumulo senza rifare il campo specchi.",
 normative="D.Lgs 28/2011 e decreti FER applicabili; D.Lgs 152/2006 (VIA); norme antincendio per depositi e circuiti di olio diatermico (prevenzione incendi, da verificare con il progetto antincendio); marcatura CE e direttive macchine/pressione per i componenti.",
 note_cantiere="In montaggio dei trough il collaudo ottico non si improvvisa: misura l'allineamento con target e teodolite o sistemi fotogrammetrici modulo per modulo, perche' un campo 'quasi dritto' perde punti di resa che nessun collaudo finale ti ridara'."
)

add(
 categoria="Tecnologie di campo solare",
 nome="Torri solari a ricevitore centrale",
 descrizione="Nella torre solare centinaia o migliaia di eliostati (specchi piani inseguitori a due assi) concentrano la radiazione su un ricevitore in cima a una torre: si raggiungono temperature oltre i 565 gradi C e concentrazioni di centinaia di soli, con rendimenti del ciclo piu' alti.",
 tecnologia="Struttura: campo di eliostati a inseguimento biassiale controllati da un algoritmo di puntamento; torre in cls o acciaio (50-150 m) con ricevitore esterno o a cavita'; fluidi: sali fusi (fino a 565 gradi C, accumulo diretto), vapore diretto o aria/particelle per le generazioni avanzate; il fattore di concentrazione elevato consente temperature e rendimenti termodinamici superiori ai trough; criticita': puntamento e spillage (radiazione che manca il ricevitore), degradazione ottica, sicurezza del fascio (zone di esclusione per avifauna e traffico aereo).",
 applicazioni="Impianti utility-scale con accumulo lungo (8-15 ore) per produzione serale; progetti dimostrativi su cicli avanzati (supercritici, aria); abbinamento a processi industriali ad alta temperatura.",
 vantaggi="Temperature piu' alte significano rendimento del ciclo e densita' di accumulo maggiori; niente circuito di fluido distribuito nel campo (il fluido sta in torre); adatta a accumuli lunghi, il valore sistemico piu' richiesto dalle reti con molto fotovoltaico.",
 limiti="Tecnologia meno standard dei trough: ogni impianto e' quasi prototipale nella pratica contrattuale; precisione di puntamento e software di campo critici; permessi piu' complessi (impatto visivo della torre, sicurezza del fascio, avifauna); esperienza di esercizio italiana molto limitata.",
 costi_e_economia="Ordini di grandezza indicativi: CAPEX di impianti a torre con accumulo 5.000-9.000 euro/kW (letteratura internazionale, forte dipendenza da scala e contenuto locale); eliostato installato 100-200 euro/m2 di specchio; torre e ricevitore: quota singola piu' onerosa del progetto (ordine 10-20% del CAPEX); LCOE in riduzione ma superiore al fotovoltaico puro.",
 casi_real_world="Caso reale estero: impianti a torre da 10-20 MW con accumulo a sali fusi in Spagna hanno dimostrato produzione estiva continuata di 24 ore; progetti successivi in America e Asia hanno scalato la taglia oltre i 100 MW con accumuli di 10-15 ore.",
 normative="D.Lgs 28/2011; D.Lgs 387/2003 (autorizzazione unica); D.Lgs 152/2006 (VIA obbligatoria sopra le soglie di potenza FER); valutazioni specifiche su avifauna e sicurezza aerea (ENAC/ente competente) per il fascio concentrato.",
 note_cantiere="Se il progetto prevede una torre, verifica subito i vincoli di traffico aereo e le procedure di valutazione ambientale specifiche: sono le due autorizzazioni che piu' spesso fermano i progetti a ricevitore centrale in Europa."
)

add(
 categoria="Tecnologie di campo solare",
 nome="Linear Fresnel e i concentratori a specchi piani",
 descrizione="Il linear Fresnel usa file di specchi quasi piani vicino al suolo che puntano su un ricevitore lineare sospeso: struttura semplice, costruzione quasi edile, concentrazione e temperature inferiori ai trough ma costi di campo potenzialmente piu' bassi.",
 tecnologia="Struttura: specchi piani o leggermente curvi su inseguitori monoassiali, ricevitore fisso lineare a 8-15 m di altezza con tubo assorbitore e riflettore secondario; produzione diretta di vapore (fino a circa 250-500 gradi C secondo il progetto) senza olio diatermico; il campo richiede superfici piane estese e manutenzione semplice; rendimenti ottici inferiori ai trough (radiazione obliqua e ombreggiamenti tra file), compensati da costi di struttura e fondazioni contenuti.",
 applicazioni="Calore di processo industriale e vapore fino a media temperatura; piccoli impianti elettrici; teleriscaldamento solare di grande superficie; integrazione su capannoni e terreni industriali pianeggianti.",
 vantaggi="Componenti di derivazione edile e meccanica semplice: specchi piani, carpenteria leggera, assenza di circuito olio; posa rapida con squadre edili ordinarie; buona resistenza al vento per la bassa altezza; sito adatto anche a terreni industriali di risulta.",
 limiti="Rendimento ottico ed elettrico inferiore alle altre tecnologie CSP; meno riferimenti di esercizio di lunga durata; la produzione diretta di vapore complica l'accumulo (serve separazione con accumulo a vapore o sali indiretti); banche finanziatrici meno familiari: piu' lavoro di due diligence.",
 costi_e_economia="Ordini di grandezza indicativi: campo Fresnel per calore di processo 200-350 euro/m2 di specchio installato; costo del calore solare di processo competitivo rispetto al gas in siti a DNI medio-alta con prezzi del gas elevati (dipende dal contesto: valutare con modello orario); impianti elettrici Fresnel: nicchia, CAPEX comparabile ai trough ma con rendimenti inferiori.",
 casi_real_world="Caso tipo europeo: campo linear Fresnel su terreno industriale fornisce vapore di processo a 12 bar a uno stabilimento alimentare, riducendo l'acquisto di gas; il cantiere e' durato pochi mesi con carpenteria locale e senza opere speciali.",
 normative="D.Lgs 28/2011; D.M. 37/2008 e normativa sugli apparecchi a pressione per i circuiti vapore; autorizzazioni edilizie e paesaggistiche ordinarie per i campi a bassa altezza (da verificare localmente).",
 note_cantiere="Il punto debole di un Fresnel non sono gli specchi ma il ricevitore sospeso: verifica in cantiere la rigidezza dei sostegni del ricevitore al vento prima dell'allineamento finale, altrimenti insegui vibrazioni per mesi."
)

add(
 categoria="Tecnologie di campo solare",
 nome="Dish-Stirling: il solare a concentrazione di piccola taglia e il suo stato reale",
 descrizione="Il dish-Stirling e' un concentratore parabolico puntuale (dish) con un motore Stirling nel fuoco: converte direttamente in elettricita' senza ciclo a vapore, in taglie unitarie di pochi kW. Tecnologia elegante, mai decollata commercialmente: conoscerla serve a non proporla nel contesto sbagliato.",
 tecnologia="Struttura: paraboloide a specchi (diametro tipico 5-10 m) su inseguitore biassiale, ricevitore nel fuoco che riscalda il gas di lavoro del motore Stirling; rendimenti di conversione solare-elettrica tra i piu' alti mai misurati su prototipi (oltre il 25% in condizioni di prova); nessun fluido termovettore, nessun ciclo Rankine; criticita': motore Stirling di precisione (tenuta gas, pistoni a lunga corsa, manutenzione specialistica), costo unitario elevato senza economie di scala, produttori storici usciti dal mercato.",
 applicazioni="Nicchie: siti isolati con alta DNI e manutenzione disponibile; ricerca e dimostratori; didattica. NON adatta a edilizia ordinaria ne' a produzione commerciale diffusa nello stato attuale.",
 vantaggi="Rendimento di picco elevato; nessun consumo idrico; modularita' unitaria; impatto paesaggistico limitato rispetto a grandi campi.",
 limiti="Affidabilita' del motore nel tempo il vero punto debole (ore di funzionamento tra manutenzioni limitate rispetto a turbomacchine); catena di fornitura quasi inesistente; costo per kW installato di gran lunga superiore a fotovoltaico e CSP utility; difficolta' di accumulo diretto.",
 costi_e_economia="Ordini di grandezza indicativi: costi unitari storici sui prototipi dell'ordine di 3.000-10.000 euro/kW senza economie di serie (letteratura); la manutenzione specialistica del motore e' la voce che affonda il piano economico; oggi il confronto con FV+accumulo e' improponibile in edilizia.",
 casi_real_world="Caso reale storico: dimostratori dish-Stirling da 10-25 kW installati in programmi di ricerca europei e americani hanno raggiunto record di rendimento solare-elettrico, ma i progetti commerciali annunciati negli anni 2000 non sono stati portati a termine per costi e affidabilita'.",
 normative="Marcatura CE e direttive macchine per il gruppo motore; connessione alla rete secondo CEI 0-21 (bassa tensione) per le taglie unitarie; per il resto nessuna disciplina specifica FER dedicata: segue le regole generali dei piccoli impianti FER.",
 note_cantiere="Se un fornitore ti propone un dish-Stirling per un cliente, chiedi il nome del manutentore del motore entro 100 km e le ore di funzionamento garantite: se la risposta e' vaga, il progetto finisce li'."
)

add(
 categoria="Accumulo e blocco di potenza",
 nome="Accumulo termico a sali fusi: la differenza tra sole e centrale solare",
 descrizione="L'accumulo termico e' cio' che distingue il CSP dal fotovoltaico: il calore raccolto di giorno si conserva in serbatoi di sali fusi e si restituisce alla sera, rendendo la produzione programmabile. E' la voce che giustifica l'intero investimento.",
 tecnologia="Sistema a due serbatoi: sale miscela nitrato di sodio e nitrato di potassio (60/40, 'sale solare'), serbatoio freddo a circa 290 gradi C e caldo a circa 565 gradi C negli impianti a torre (circa 385-390 gradi C con olio nei trough con accumulo indiretto); scambiatori sale-vapore alimentano il generatore di vapore; capacita' tipica 3-15 ore a pieno carico; criticita': congelamento del sale sotto circa 220-240 gradi C (tracciamento elettrico di tubazioni e valvole obbligatorio), tenute e valvolame ad alta temperatura, gestione termica dei serbatoi (fondazioni ventilate o isolate secondo il progetto).",
 applicazioni="Impianti CSP utility-scale con produzione serale; accumulo di calore di processo; retrofit di impianti a olio con passaggio a sali; prospettiva di accumulo termico stand-alone accoppiato a FV (riscaldo elettrico dei sali).",
 vantaggi="Tecnologia di accumulo con costo per kWh termico storicamente inferiore alle batterie elettrochimiche per grandi capacita' e durata di decenni; il calore accumulato alimenta il blocco convenzionale esistente; materia prima (sali) abbondante e riciclabile.",
 limiti="Gestione antigelo del sale vincolante: un congelamento in circuito e' un incidente serio; serbatoi e valvole ad alta temperatura richiedono manutenzione specializzata; il peso (migliaia di tonnellate di sale) impone fondazioni dedicate; avviamento e spegnimento quotidiano del ciclo accelerano la fatica termica dei componenti.",
 costi_e_economia="Ordini di grandezza indicativi: costo dell'accumulo a sali 20-60 euro/kWh termico installato (serbatoi, sale, scambiatori, tracciamento); il sale di impianto per ore di accumulo pesa migliaia di tonnellate (es. migliaia di t per 5-7 ore su 50 MW); il tracciamento elettrico antigelo e' una voce di esercizio permanente da non sottostimare.",
 casi_real_world="Caso reale: l'impianto dimostrativo italiano a sali fusi ha usato i sali come fluido termovettore e accumulo integrato fin dal 2010; gli impianti spagnoli da 50 MW con 7,5 ore di accumulo a due serbatoi hanno operato produzioni notturne complete, diventando il riferimento mondiale della tecnologia.",
 normative="Normativa apparecchi a pressione per serbatoi e circuiti (direttiva PED e recepimento nazionale); prevenzione incendi per grandi depositi caldi; D.Lgs 152/2006 per gli aspetti ambientali; disciplina FER per la qualificazione dell'energia accumulata.",
 note_cantiere="In costruzione di un accumulo a sali, il tracciamento elettrico si collauda prima del sale, non dopo: carica i circuiti riscaldanti, misura le correnti circuito per circuito e firma un verbale. Un sale congelato in una valvola non tracciata e' un fermo di settimane."
)

add(
 categoria="Accumulo e blocco di potenza",
 nome="Il blocco di potenza: generatore di vapore, turbina e bilancio di centrale",
 descrizione="Il blocco di potenza del CSP e' una piccola centrale termoelettrica convenzionale: generatore di vapore alimentato dal campo solare, turbina a vapore, condensatore, alternatore. Conoscerne i numeri evita di confondere la parte solare con quella termodinamica.",
 tecnologia="Schema: treno di scambiatori (preriscaldatore, evaporatore, surriscaldatore, risurriscaldatore) che producono vapore tipicamente a 100-140 bar e 380-540 gradi C secondo il fluido termovettore; turbina a vapore con rigenerazioni; condensazione ad acqua (torri evaporative: consumo idrico rilevante) o a secco (condensatori ad aria: niente acqua ma resa minore e costo maggiore, scelta tipica in siti aridi); alternatore e trasformatore di connessione MT; servizi ausiliari (pompe, tracciamenti, inseguitore) con consumo proprio dell'ordine del 8-12% della produzione lorda.",
 applicazioni="Dimensionamento e stima di produzione netta degli impianti CSP; valutazione del consumo idrico in fase autorizzativa; scelta tra condensazione umida e secca; integrazione con accumulo e con il campo solare.",
 vantaggi="Tecnologia convenzionale con fornitori e manutentori della filiera termoelettrica; produzione regolabile e partecipazione ai servizi di rete come una centrale tradizionale; vita utile del blocco superiore ai 30 anni con manutenzione ordinaria.",
 limiti="Il rendimento del ciclo a queste taglie e temperature e' modesto (ordine 28-38% dal calore all'eletticita' secondo la tecnologia); gli avviamenti quotidiani impongono materiali e gestione della fatica; il condensatore a secco riduce la resa proprio nei siti piu' soleggiati dove l'acqua manca.",
 costi_e_economia="Ordini di grandezza indicativi: blocco di potenza (turbina, generatore vapore, condensazione, BOP elettrico) 1.000-1.800 euro/kW nelle taglie 10-50 MW; condensazione a secco aggiunge circa il 5-10% al costo del blocco e riduce la produzione di alcuni punti percentuali; consumo idrico con torri evaporative: milioni di m3/anno per grandi taglie, voce decisiva in VIA.",
 casi_real_world="Caso tipo: impianto trough da 50 MW con condensazione ad aria in area arida: rinuncia a qualche punto di rendimento estivo ma elimina il fabbisogno idrico continuo, semplificando autorizzazione e gestione in un sito senza derivazioni d'acqua.",
 normative="Direttiva attrezzature a pressione (PED) e recepimento per generatori di vapore e tubazioni; normativa INAIL/ISPESL di derivazione per gli apparecchi a pressione in esercizio; CEI 0-16 per la connessione in media/alta tensione; D.Lgs 152/2006 per scarichi ed emissioni.",
 note_cantiere="Il numero che conta in collaudo e' la produzione NETTA: fai misurare i consumi ausiliari (pompe, tracciamenti, inseguitori) con lo stesso rigore della potenza lorda, perche' e' li' che i modelli di produzione sbagliano di piu'."
)

add(
 categoria="Integrazione edilizia",
 nome="Solare a media temperatura in edilizia e industria: calore, cooling e reti di calore",
 descrizione="Sotto la scala delle centrali, il solare termico a concentrazione di piccola taglia (trough compatti, Fresnel) produce calore a 100-250 gradi C per processi industriali, teleriscaldamento e raffrescamento ad assorbimento: il vero punto di contatto tra CSP ed edilizia.",
 tecnologia="Tecnologie: piccoli collettori parabolici e Fresnel su tetti piani industriali o terreni; produzione di acqua surriscaldata o vapore a bassa/media pressione; abbinamento con assorbitori (bromuro di litio, alimentati a 80-120 gradi C) per il raffrescamento solare (solar cooling); integrazione in reti di teleriscaldamento come integrazione solare stagionale con accumuli; in Italia la DNI limita la concentrazione spinta, ma la media temperatura resta praticabile nel Centro-Sud e nelle isole con collettori evoluti.",
 applicazioni="Calore di processo per industrie alimentari, tessili, cartarie nel Mezzogiorno; raffrescamento ad assorbimento di edifici terziari con carichi estivi allineati al sole; integrazione solare in reti di teleriscaldamento esistenti; distretti turistici e ospedalieri.",
 vantaggi="Il carico di raffrescamento estivo e' sincrono con la radiazione: il solar cooling usa il sole proprio quando serve; il calore solare di processo sostituisce gas con costi stabili per 20 anni; tetti e piazzali industriali offrono superfici gia' urbanizzate senza consumo di suolo.",
 limiti="In gran parte d'Italia la DNI e' modesta: i collettori a concentrazione rendono meno che nel Sud Europa, e spesso il confronto con collettori piani sottovuoto + pompa di calore elettrica non regge; assorbitori e caldaie di backup aggiungono complessita' impiantistica; mercato italiano piccolo: poche referenze e filiera sottile.",
 costi_e_economia="Ordini di grandezza indicativi: collettori a media temperatura installati 300-700 euro/m2; assorbitore a bromuro di litio per terziario 300-600 euro/kW frigoro; sistema di solar cooling completo per edificio terziario 1.200-2.500 euro/kW frigoro (due-tre volte un sistema elettrico, da giustificare con i carichi e gli incentivi); calore solare di processo: valutare il costo livellato rispetto al gas con modello orario.",
 casi_real_world="Caso tipo: stabilimento alimentare in Puglia con campo a piccoli trough su piazzale per preriscaldo dell'acqua di processo a 120 gradi C, integrato con la caldaia esistente; la quota solare copre una parte significativa del carico diurno estivo con rientro coerente con gli incentivi FER termici.",
 normative="D.Lgs 28/2011 e Conto Termico 3.0 (D.M. 7/8/2025) per gli incentivi del solare termico (verificare le regole applicative GSE vigenti per i collettori a concentrazione); D.M. 37/2008 per gli impianti; normativa apparecchi a pressione per il vapore; UNI EN 12975 e serie per i collettori solari termici.",
 note_cantiere="Prima di vendere solar cooling, guarda le bollette estive del cliente e il profilo orario: se l'edificio e' vuoto ad agosto o ha carichi serali, il sole non gli serve. E metti sempre la caldaia di backup nel computo: il cliente ti giudica a ferragosto, non ad aprile."
)

add(
 categoria="Contesto italiano",
 nome="CSP in Italia: radiazione diretta, siti idonei e l'esperienza nazionale",
 descrizione="L'Italia ha DNI buona solo in aree limitate (Sicilia, Sardegna, Puglia ionica, zone costiere del Sud) e un'esperienza industriale reale: l'impianto a sali fusi in Sicilia e' stato il primo al mondo con accumulo integrato. Capire dove ha senso e' la prima competenza.",
 tecnologia="Valutazione del sito: DNI annua da misura in sito (stazioni con pireliometro, almeno un anno) o serie satellitari validate; soglia indicativa di convenienza per CSP elettrico 1.800-2.000 kWh/m2 anno (in Italia raggiunta solo in aree del Sud e isole); vincoli: superfici piane estese (2-4 ettari/MW), connessione elettrica vicina, acqua se condensazione umida, paesaggio e vincoli ambientali; l'esperienza italiana: impianto dimostrativo a sali fusi da circa 5 MW entrato in esercizio nel 2010 in Sicilia, filiera nazionale di specchi e componenti maturata sui progetti esteri, studi su repowering e nuovi impianti nel Mezzogiorno.",
 applicazioni="Screening di siti per impianti CSP o per calore solare di processo; due diligence su progetti proposti; programmazione energetica regionale nel Mezzogiorno; valutazione di riconversione di siti industriali dismessi.",
 vantaggi="Le aree idonee italiane hanno tra le migliori DNI d'Europa insieme alla Spagna meridionale; siti industriali dismessi del Sud offrono superfici piane, connessioni e autorizzazioni piu' semplici; la filiera nazionale esiste e puo' competere sui componenti.",
 limiti="La DNI italiana resta inferiore a Spagna del Sud e Nord Africa: i margini economici sono sottili e dipendono dagli incentivi; il consumo di suolo e' alto e incontra opposizioni locali; le connessioni elettriche nelle aree idonee sono spesso sature di richieste FER.",
 costi_e_economia="Ordini di grandezza indicativi: campagna di misura DNI in sito (stazione pireliometrica, un anno, gestione e validazione dati) 15-40 k€; studio di fattibilita' completo per impianto medio 100-300 k€; il prezzo del terreno non e' mai il problema: lo sono connessione e autorizzazioni, i cui tempi valgono piu' del CAPEX di superficie.",
 casi_real_world="Caso reale: il primo impianto CSP a sali fusi del mondo e' entrato in esercizio nel 2010 in un sito industriale siciliano (circa 5 MW), integrato con la centrale esistente: ha dimostrato l'accumulo diretto in sali e formato la filiera nazionale che ha poi lavorato su impianti esteri.",
 normative="D.Lgs 28/2011; D.Lgs 387/2003 (autorizzazione unica FER); D.Lgs 152/2006 (VIA); decreti FER per l'accesso agli incentivi (verificare il decreto vigente e i registri/aste applicabili alla tecnologia).",
 note_cantiere="Mai accettare un progetto CSP presentato con la sola mappa DNI atlante: chiedi la serie satellitare ventennale del punto esatto e, se il progetto e' serio, la stazione di misura gia' installata. Chi non misura, indovina."
)

add(
 categoria="Iter autorizzativo",
 nome="Iter autorizzativo e connessione: VIA, autorizzazione unica e incentivi",
 descrizione="Un impianto CSP e' un progetto industriale: VIA, autorizzazione unica, connessione alla rete, eventuale accesso agli incentivi FER. L'iter dura anni e determina la fattibilita' piu' della tecnologia.",
 tecnologia="Passaggi: screening e verifica di assoggettabilita' a VIA (impianti FER sopra le soglie di potenza del D.Lgs 152/2006); istanza di connessione al gestore di rete con soluzione tecnica (TICA) e relativo corrispettivo; autorizzazione unica presso la regione/provincia con conferenza di servizi; vincoli paesaggistici, idrogeologici, acustici, avifauna (per torri e campi estesi); accesso agli incentivi: registri o aste dei decreti FER secondo la potenza, con tempi di realizzazione vincolanti e penali di decadenza; collaudi, officina elettrica e qualificazione dell'impianto presso il GSE.",
 applicazioni="Sviluppo di nuovi impianti; acquisizione di progetti autorizzati (due diligence autorizzativa); revamping e repowering con variazioni sostanziali; integrazione di accumulo su impianti esistenti.",
 vantaggi="L'autorizzazione unica concentra in un provvedimento il consenso degli enti; i decreti FER danno percorsi definiti per gli incentivi; i progetti autorizzati hanno valore di mercato anche prima della costruzione.",
 limiti="Tempi: 3-6 anni tra sviluppo e autorizzazione sono la norma per grandi impianti; i corrispettivi di connessione sono onerosi e perfezionano vincoli finanziari con il gestore; il mancato rispetto dei termini di entrata in esercizio fa decadere l'incentivo; il paesaggistico su campi estesi e' il punto piu' imprevedibile.",
 costi_e_economia="Ordini di grandezza indicativi: costi di sviluppo e autorizzazione di un impianto medio-grande 1-3 M€ (studi, VIA, istanze, progettazione); corrispettivi di connessione per taglie da decine di MW: centinaia di k€ fino a milioni di euro secondo la soluzione tecnica; la decadenza da incentivo per ritardo vale piu' di qualunque penale contrattuale: e' il rischio numero uno del cronoprogramma.",
 casi_real_world="Caso tipo: progetto CSP su sito industriale dismesso nel Sud: VIA superata in sede regionale con prescrizioni su paesaggio e specchi, connessione ottenuta su cabina primaria esistente del sito, autorizzazione unica in circa tre anni dalla prima istanza.",
 normative="D.Lgs 152/2006 (VIA, allegati e soglie per impianti FER); D.Lgs 387/2003 (autorizzazione unica); D.Lgs 28/2011 e decreti FER vigenti (registri/aste, verificare il quadro attuale); CEI 0-16 per la connessione; regolamento GSE per la qualificazione IAFR.",
 note_cantiere="Il cronoprogramma autorizzativo lo scrivi a ritroso dalla data di decadenza dell'incentivo, non in avanti da oggi: se i conti non tornano con i tempi di VIA e connessione, il progetto non parte, qualunque sia la tecnologia."
)

add(
 categoria="Cantiere",
 nome="Il cantiere CSP: fondazioni degli specchi, montaggio del campo e commissioning",
 descrizione="Costruire un campo solare a concentrazione e' un cantiere di carpenteria di precisione su scala industriale: migliaia di fondazioni puntuali, montaggio di specchi a tolleranze millimetriche, collaudo ottico. La parte edile e' semplice, la parte ottica no.",
 tecnologia="Fasi: preparazione del piano di campagna (livellamenti, drenaggi, viabilita' interna); fondazioni puntuali degli inseguitori (micropali battuti o plinti, secondo la pull-out test iniziale: la prova di estrazione sul terreno decide la fondazione); montaggio di strutture e specchi con controllo geometrico continuo; posa del circuito del fluido termovettore con tracciamenti; collaudo ottico (allineamento, puntamento, fattore di intercettazione) e poi idraulico (tenute, portate, bilanciamento dei loop); commissioning con avviamenti progressivi e prova di produzione garantita (performance ratio termico).",
 applicazioni="Costruzione di impianti CSP nuovi; repowering di campi esistenti; manutenzione straordinaria con sostituzione di moduli; audit di cantiere per finanziatori (monitoring dei milestone).",
 vantaggi="La serialita' premia: squadre addestrate montano decine di moduli al giorno con qualita' costante; la prova di estrazione iniziale ottimizza migliaia di fondazioni con un solo test; il collaudo ottico strumentale da' un riferimento oggettivo di fine lavori.",
 limiti="Le tolleranze ottiche non si recuperano con varianti in corsa: un modulo fuori allineamento va smontato; il vento ferma il montaggio degli specchi piu' delle lavorazioni edili; la logistica dei componenti fragili (specchi, ricevitori) richiede stoccaggi coperti e movimentazione dedicata.",
 costi_e_economia="Ordini di grandezza indicativi: opere civili e fondazioni di un campo CSP 15-25% del costo del campo solare; montaggio meccanico e ottico 20-30%; commissioning completo con prove di produzione: mesi, da pianificare nella stagione a DNI adeguata; le penali di ritardo verso l'EPC su impianti medi valgono decine di k€ a settimana.",
 casi_real_world="Caso tipo: cantiere di un campo trough nel Sud: pull-out test iniziale su tre tipi di micropalo, scelta della sezione piu' leggera conforme, montaggio a ritmo di un loop al giorno con squadre locali formate dal fornitore, collaudo ottico con target laser e consegna per loop firmati.",
 normative="D.Lgs 81/2008, Titolo IV (cantiere: lavori in quota su strutture, mezzi di sollevamento, lavori elettrici); normativa sulle prove di carico delle fondazioni; direttiva macchine per gli inseguitori; disciplina contrattuale di collaudo (prove su criterio, prestazioni garantite) secondo il contratto EPC.",
 note_cantiere="Prima del primo micropalo fai la pull-out test sul terreno reale, non sulla relazione geologica di un altro sito: la fondazione degli inseguitori e' l'unica voce che moltiplichi per migliaia, e un errore li' non lo ammortizzi mai."
)

add(
 categoria="Economia e prospettive",
 nome="Economia del CSP: CAPEX, LCOE, confronto con il fotovoltaico e quando ha senso",
 descrizione="Il giudizio economico sul CSP oggi parte da un dato: il fotovoltaico con batterie ha cambiato il riferimento di prezzo. Il CSP resta competitivo dove serve energia rinnovabile programmabile di lunga durata e dove la filiera termica ha valore industriale.",
 tecnologia="Numeri di riferimento: CAPEX trough con accumulo 4.000-7.000 euro/kW, torri 5.000-9.000 euro/kW (letteratura internazionale); LCOE 0,12-0,20 euro/kWh secondo DNI e ore di accumulo; il fotovoltaico utility costa una frazione (e il confronto va fatto a parita' di servizio: produzione programmabile serale); il valore del CSP cresce con la quota di FV in rete (copre le ore in cui il FV non c'e'), con l'accumulo lungo (8-15 ore, dove le batterie costano di piu' per kWh) e con usi termici diretti; incentivi FER e meccanismi di capacita' possono chiudere il piano economico nei siti migliori.",
 applicazioni="Valutazione preliminare di progetti; confronto tecnologico per piani energetici regionali; scelta tra FV+batterie, CSP e ibridi; argomentazione in sede di VIA e di concertazione locale.",
 vantaggi="Energia rinnovabile dispacciabile senza dipendenza dalle filiere delle batterie; vita utile lunga con costi di esercizio prevedibili; contenuto nazionale di componenti e cantieri elevato; complementare (non concorrente) al fotovoltaico nelle ore serali.",
 limiti="Senza incentivo o meccanismo di capacita' il business case italiano e' fragile; il finanziamento bancario richiede referenze e controparti solide; il confronto con FV+storage si muove ogni anno a favore del FV: un piano fatto nel 2024 va riverificato oggi; i tempi autorizzativi lunghi aumentano il rischio di obsolescenza del piano.",
 costi_e_economia="Ordini di grandezza indicativi: per un impianto da 20 MW con 8 ore di accumulo in sito a buona DNI, CAPEX complessivo dell'ordine di 100-160 M€ e produzione annua dipendente dal sito; il valore dell'energia serale programmabile, piu' gli incentivi, determina il rientro: non esiste un numero unico, esiste un modello orario da costruire per il sito.",
 casi_real_world="Caso tipo: piano energetico regionale del Mezzogiorno che confronta tre scenari per la copertura serale: FV+batterie 4 ore, CSP con accumulo 10 ore su sito industriale, mix; lo scenario CSP vince su durata dell'accumulo e contenuto industriale locale, perde su CAPEX unitario: la scelta finale dipende dagli incentivi disponibili.",
 normative="Decreti FER e meccanismi di accesso agli incentivi (verificare il quadro vigente presso GSE/MASE); disciplina del mercato della capacita' (verificare le regole vigenti); D.Lgs 28/2011 per la qualificazione dell'energia da fonte solare termodinamica.",
 note_cantiere="Quando confronti CSP e FV+batterie, esigi lo stesso perimetro: produzione serale garantita, ore di accumulo, vita utile, decommissioning. I confronti 'a costo del kWh di giorno' sono il modo piu' comune di sbagliare la scelta."
)

# --- scrittura schede.jsonl ---
p_jsonl = os.path.join(BASE, 'schede', 'schede.jsonl')
out = io.open(p_jsonl, 'w', encoding='utf-8', newline='\n')
for s in S:
    out.write(json.dumps(s, ensure_ascii=False) + '\n')
out.close()

# --- COURSE.yaml ---
course = """corso: "Solare termodinamico (CSP) e solare a concentrazione"
facolta: "FACOLTA_IMPIANTI_ENERGIA"
livello: "L2-L3"
schede: 12
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "D.Lgs 28/2011, D.Lgs 387/2003 (autorizzazione unica FER), D.Lgs 152/2006 (VIA), D.M. 7/8/2025 (Conto Termico 3.0) e regole applicative GSE, D.M. 37/2008, CEI 0-16/0-21, direttiva PED (apparecchi a pressione), UNI EN 12975 (collettori solari termici), D.Lgs 81/2008 (Titolo IV), letteratura tecnica internazionale su CSP (LCOE, CAPEX, rendimenti come ordini di grandezza)"
nota_metodologica: "Principio CSP e famiglie, collettori parabolici, torri, linear Fresnel, dish-Stirling (stato reale), accumulo a sali fusi, blocco di potenza, integrazione edilizia (calore di processo, solar cooling), contesto italiano (DNI, siti, esperienza a sali fusi), iter autorizzativo e connessione, cantiere e commissioning, economia e confronto con FV. Prezzi e rendimenti come fasce di letteratura; decreti FER marcati da verificare nel quadro vigente; nessun nome di azienda, casi reali descritti in forma anonima."
"""
open(os.path.join(BASE, 'COURSE.yaml'), 'w', encoding='utf-8').write(course)

# --- README.md ---
readme = """# Solare termodinamico (CSP) e solare a concentrazione

Corso di livello L2-L3 (FACOLTA_IMPIANTI_ENERGIA) sul solare a concentrazione: principio e requisito di radiazione diretta (DNI), collettori parabolici lineari, torri solari a ricevitore centrale, linear Fresnel, dish-Stirling e il suo stato reale, accumulo termico a sali fusi, blocco di potenza a vapore, integrazione in edilizia e industria (calore di processo, solar cooling, reti di calore), il contesto italiano (DNI, siti idonei, l'impianto dimostrativo a sali fusi del 2010), iter autorizzativo (VIA, autorizzazione unica, incentivi FER), cantiere e commissioning del campo solare, economia (CAPEX, LCOE) e confronto onesto con fotovoltaico e batterie.

**Schede: 12** — formato JSONL con le 11 chiavi standard dell'Università dell'Edilizia.

Regola metodologica: prezzi e rendimenti come fasce di letteratura tecnica, mai come quotazioni; decreti FER e regole applicative marcati «da verificare nel quadro vigente»; casi reali descritti senza nomi di aziende.
"""
open(os.path.join(BASE, 'README.md'), 'w', encoding='utf-8').write(readme)

# --- verifica finale ---
rows = [json.loads(l) for l in open(p_jsonl, encoding='utf-8') if l.strip()]
assert len(rows) == 12, len(rows)
for r in rows:
    assert list(r.keys()) == KEYS, r['nome']
    assert 'aplicazioni' not in r and 'tegnologia' not in r
print('OK:', p_jsonl, '-', len(rows), 'schede, chiavi e ordine corretti')
