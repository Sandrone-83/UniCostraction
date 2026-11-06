# -*- coding: utf-8 -*-
"""Giro AR: genera TEATRI_LOCALI_SPETTACOLO_PACK (12 schede)."""
import json, os

PACK = 'TEATRI_LOCALI_SPETTACOLO_PACK'
ROOT = os.path.join('UNIVERSITA_EDILIZIA', PACK)
K = ['categoria','nome','descrizione','tecnologia','applicazioni','vantaggi','limiti',
     'costi_e_economia','casi_real_world','normative','note_cantiere']

def S(categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti,
      costi_e_economia, casi_real_world, normative, note_cantiere):
    d = dict(zip(K, [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi,
                     limiti, costi_e_economia, casi_real_world, normative, note_cantiere]))
    assert d['costi_e_economia'].startswith('Ordini di grandezza indicativi: '), nome
    return d

SCHEDE = [

S('Quadro normativo', 'Agibilità e licenza dei locali di pubblico spettacolo',
  'Teatri, cinema, sale da concerto e locali di pubblico spettacolo sono attivita\u0300 sottoposte a licenza di pubblica sicurezza e ad agibilita\u0300 per l\u2019affollamento: oltre al titolo edilizio servono la conformita\u0300 al regolamento di costruzione specifico, il nulla osta antincendio e la licenza di esercizio con la capienza autorizzata. La commissione di vigilanza sui locali di pubblico spettacolo verifica periodicamente le condizioni: l\u2019agibilita\u0300 non e\u0300 un atto una tantum ma uno stato da mantenere.',
  'Iter tipico: titolo edilizio (PdC/SCIA) con destinazione d\u2019uso spettacolo, verifica al regolamento di costruzione dei locali di pubblico spettacolo (superfici minime, altezze, uscite, servizi), progetto antincendio e SCIA ai VVF per le attivita\u0300 soggette, richiesta di licenza al Comune (TULPS), sopralluogo della commissione di vigilanza e rilascio dell\u2019agibilita\u0300 con capienza massima (persone ammesse); verifiche periodiche e rinnovi; per sale storiche, deroghe motivate su parametri puntuali con misure compensative.',
  'Apertura di nuove sale, riapertura di teatri chiusi, cambi di destinazione d\u2019uso verso spettacolo (ex cinema, ex chiese, capannoni), verifiche periodiche e aumenti di capienza.',
  'Agibilita\u0300 e capienza formalizzate chiariscono le condizioni di esercizio e la responsabilita\u0300; la commissione di vigilanza e\u0300 un interlocutore unico per sicurezza e igiene.',
  'Iter multiplo (edilizio, antincendio, pubblica sicurezza) con tempi lunghi; le sale in edifici esistenti incontrano parametri difficili da rispettare senza opere; la capienza autorizzata puo\u0300 essere inferiore a quella fisica: il gestore pianifica su quella.',
  'Ordini di grandezza indicativi: pratiche di agibilita\u0300 e licenza per sala media 10-40 k€ di parcelle; adeguamenti per ottenere l\u2019agibilita\u0300 in edificio esistente da 50 k€ a oltre 500 k€ secondo lo stato.',
  'Caso tipo: riapertura di un cinema degli anni \u201950 come teatro: la commissione concede l\u2019agibilita\u0300 con capienza ridotta a 299 posti e prescrizione di due nuove uscite di emergenza e della revisione delle poltrone fisse.',
  'R.D. 773/1931 TULPS (licenza, artt. 68 e seguenti); D.M. 19/8/1996 (regolamento di costruzione dei locali di pubblico spettacolo); DPR 151/2011 (attivita\u0300 soggette VVF); DPR 380/2001 (titoli edilizi); regolamenti regionali e comunali (da verificare).',
  'Verifica sempre la capienza autorizzata prima di progettare palchi, gradinate o servizi: e\u0300 lei che comanda. E tieni i verbali della commissione di vigilanza come oro: sono la storia clinica della sala.'),

S('Tipologie e sala', 'Tipologie di sala e dimensionamento per spettatore',
  'La sala da spettacolo si dimensiona attorno al rapporto palcoscenico-pubblico: teatro all\u2019italiana (sala a ferro di cavallo con palchi), sala con platea e gallerie, anfiteatro e arena, black box flessibile, sala da concerto a vigna. Ogni tipologia ha indici di superficie per posto, distanze di visibilita\u0300 e requisiti acustici propri: la scelta tipologica e\u0300 la prima decisione strutturale, perche\u0300 fissa luci, altezze e impianti.',
  'Indici tipici: superficie sala 0,6-1,0 m2/posto in platea (poltrone) e oltre in black box; larghezza poltrona 0,50-0,60 m, passo tra file 0,80-1,05 m (1,00-1,05 dove serve l\u2019esodo tra file occupate secondo il regolamento); visibilita\u0300: alzata tra file 8-12 cm in platea, maggiore in galleria, con verifica grafica del cono visivo; distanza massima di visione 20-30 m per prosa, oltre per lirica e concerti; il regolamento D.M. 19/8/1996 fissa i minimi di legge.',
  'Progetto di nuove sale, riconfigurazione di platee, verifica della capienza in ristrutturazioni, conversione di cinema in teatri.',
  'Indici corretti = confort e visibilita\u0300 che giustificano il prezzo del biglietto; la black box massimizza la flessibilita\u0300 d\u2019uso; il teatro all\u2019italiana conserva acustica e gerarchia sociale dei posti.',
  'Aumentare i posti a scapito di passo file e visibilita\u0300 produce sale scomode e problemi in commissione; le gradinate ripide migliorano la vista ma complicano l\u2019esodo e l\u2019accessibilita\u0300; ogni tipologia vincola il macchinismo scenico.',
  'Ordini di grandezza indicativi: poltrona teatrale installata 250-700 €/posto; gradinata telescopica motorizzata per black box 1.500-3.000 €/posto; solo sala (finita, senza impianti scenici) 1.500-2.500 €/m2.',
  'Caso tipo: black box comunale da 250 posti con gradinate telescopiche: la stessa sala ospita prosa, concerti e convegni cambiando configurazione in mezza giornata; la capienza autorizzata varia per configurazione ed e\u0300 registrata in licenza.',
  'D.M. 19/8/1996 (dimensioni minime, passi, uscite); D.M. 236/1989 (posti per disabili); normativa regionale sullo spettacolo (da verificare).',
  'Disegna la visibilita\u0300 con la sezione vera e il punto di vista dell\u2019ultima fila, non a sentimento: il posto che vede meta\u0300 palco esiste per sempre. E misura il passo file con le poltrone vere: il campione da catalogo non basta.'),

S('Sicurezza antincendio', 'Esodo e prevenzione incendi nelle sale con affollamento',
  'La sala da spettacolo e\u0300 il caso scolastico di esodo in presenza di affollamento: centinaia o migliaia di persone, al buio, con attenzione altrove. Il progetto antincendio combina compartimentazione (palcoscenico verso sala), controllo dei fumi, larghezze di esodo dimensionate sulla capienza, illuminazione di sicurezza e gestione dell\u2019evacuazione: qui gli errori si pagano in vite, non in varianti.',
  'Elementi: separazione sala/palcoscenico con sipario tagliafuoco e compartimentazione EI secondo regolamento; uscite di sala dimensionate sul deflusso (moduli di uscita per unita\u0300 di larghezza secondo D.M. 19/8/1996 e Codice D.M. 3/8/2015), distribuite su piu\u0300 lati; vie di esodo sgombre e segnalate, illuminazione di emergenza e antipanico; porte con maniglioni antipanico aprenti nel senso dell\u2019esodo; EVAC e servizio di sicurezza con addetti formati; controllo fumi in sala secondo geometria.',
  'Sale di ogni dimensione, teatri storici con vincoli (misure compensative), spazi temporanei (tensostrutture per spettacolo, con normativa specifica), riaperture con aumento di capienza.',
  'Il regolamento specifico del settore offre parametri chiari; la separazione sala/palco contiene il rischio del lato piu\u0300 pericoloso (scena con materiali scenici); l\u2019approccio prestazionale del Codice aiuta le sale storiche.',
  'Nei teatri storici le larghezze di esodo sono il vincolo che fissa la capienza; i materiali scenici (legno, tessuti, gommapiuma) alimentano il carico d\u2019incendio: servono regole di gestione, non solo impianti; i costi di adeguamento possono superare quelli del restauro.',
  'Ordini di grandezza indicativi: adeguamento antincendio sala esistente (uscite, EVAC, sipario tagliafuoco, illuminazione) 100-500 k€; sipario tagliafuoco 30-100 k€; gestione sicurezza in esercizio: personale dedicato per serata.',
  'Caso tipo: teatro storico che ottiene l\u2019aumento di capienza da 400 a 520 posti con soluzione prestazionale: due nuove uscite laterali, sipario tagliafuoco revisionato e piano di evacuazione con addetti dedicati approvati dalla commissione.',
  'D.M. 19/8/1996 (esodo, separazioni); D.M. 3/8/2015 (Codice prevenzione incendi); DPR 151/2011 (soggezione VVF); UNI EN 12101 (controllo fumi); normativa sulle tensostrutture per spettacolo (da verificare).',
  'Non trattare mai l\u2019esodo come un disegno a posteriori: le uscite si contano in fase di pianta. E imponi al gestore il registro dei materiali scenici: la scenografia infiammabile vanifica il miglior progetto antincendio.'),

S('Acustica', 'Acustica della sala: riverbero, intelligibilità, isolamento',
  'L\u2019acustica e\u0300 la prestazione che definisce una sala da spettacolo: tempo di riverbero ottimale per la funzione (prosa, lirica, concerto), distribuzione uniforme del suono, assenza di echi e focalizzazioni, isolamento dai rumori esterni e dagli impianti. Si progetta con la geometria prima ancora che coi materiali: nessun pannello corregge una forma sbagliata.',
  'Parametri: tempo di riverbero medio ottimale orientativo 0,7-1,0 s per la prosa, 1,4-1,8 s per lirica e concerti sinfonici (volume dipendente); geometria: superfici laterali riflettenti vicino al proscenio, soffitto come riflettore, fondo assorbente; materiali fonoassorbenti calibrati (tendaggi, pannelli microforati, risuonatori); isolamento: box-in-box per le sale critiche, porte acustiche, soglia di rumore di fondo NR 20-25; impianti su supporti antivibranti con canalizzazioni insonorizzate.',
  'Nuove sale, risanamento acustico di sale esistenti, conversione di cinema (troppo \u2018sordi\u2019 per la prosa), contenimento del rumore verso il vicinato per live club.',
  'L\u2019acustica corretta si percepisce e vende biglietti; la progettazione geometrica precoce costa poco e rende molto; il box-in-box risolve il rapporto col vicinato.',
  'Correzioni a posteriori costano care e sono limitate; la multifunzione (prosa + musica amplificata) richiede acustica variabile costosa; il rumore degli impianti e\u0300 il difetto piu\u0300 comune e piu\u0300 trascurato.',
  'Ordini di grandezza indicativi: progetto acustico con misurazioni 15-60 k€; trattamenti acustici della sala 100-400 €/m2 di superficie trattata; box-in-box per live club 300-700 €/m2 di involucro interno.',
  'Caso tipo: ex cinema con riverbero di 0,5 s convertito in teatro di prosa: superfici laterali riflettenti al proscenio, soffitto parzialmente liberato dalle controsoffittature assorbenti, fondo con pannelli variabili: il riverbero sale a 0,9 s e la sala torna agibile acusticamente.',
  'UNI EN ISO 3382-1 (misurazione parametri acustici delle sale); L. 447/1995 e DPCM 5/12/1997 (limiti di rumore verso l\u2019esterno); D.M. 236/1989 per i percorsi; rinvio a ACUSTICA_EDILIZIA_PACK per i fondamenti.',
  'Fai misurare l\u2019acustica a sala vuota e a sala piena prima della consegna: le poltrone cambiano il riverbero. E ascolta la sala con gli impianti accesi al minimo sindacale: il ronzio che il progettista non sente, il pubblico si\u0300.'),

S('Palcoscenico', 'Palcoscenico e torre scenica: geometria e macchinismo',
  'Il palcoscenico e\u0300 la macchina produttiva del teatro: piano di lavoro, torre scenica per il volo delle scene, graticcia, ponti mobili, argani, proscenio con sipario e quinte. Le sue dimensioni e il suo macchinismo determinano cosa la sala puo\u0300 ospitare: una torre assente o bassa esclude l\u2019opera; un retropalo inesistente impedisce il montaggio delle produzioni in tournée.',
  'Dimensioni tipiche: boccascena 8-14 m per teatri medi; torre scenica con altezza libera 2-2,5 volte l\u2019altezza del boccascena; graticcia a carico distribuito (orientativamente 3-5 kN/m2 secondo uso — da verificare in progetto); argani motorizzati a fune con controllo di posizione e carico, ponti mobili e camminamenti di servizio; piano palco in assi di legno su travatura ispezionabile, con botole e carri scenici; retropalo e lateralita\u0300 dimensionate per le produzioni ospitate.',
  'Teatri di nuova costruzione, rifunzionalizzazione di sale con aggiunta di torre, ammodernamento del macchinismo (da argani manuali a motorizzati), adeguamento alla sicurezza macchine.',
  'Macchinismo moderno = tempi di allestimento dimezzati e sicurezza del personale; la torre ben dimensionata apre al cartellone lirico; l\u2019ispezionabilita\u0300 del piano palco previene i cedimenti.',
  'Il macchinismo scenico e\u0300 costoso e richiede manutenzione specialistica obbligatoria; la torre scenica e\u0300 un volume edilizio imponente con impatto urbanistico; sale senza torre restano limitate al repertorio leggero.',
  'Ordini di grandezza indicativi: macchinismo scenico completo per teatro medio 500 k€-2 M€; argano motorizzato 5-15 k€/cad.; piano palco ispezionabile 400-800 €/m2; volume di torre in muratura o acciaio 150-250 €/m3.',
  'Caso tipo: teatro comunale che sostituisce 40 argani manuali a verricello con 24 argani motorizzati a controllo numerico e graticcia nuova: gli allestimenti passano da due giorni a mezza giornata e gli infortuni di movimentazione si azzerano.',
  'Direttiva Macchine 2006/42/CE (argani e ponti come macchine); D.Lgs 81/2008 (lavoro in quota, attrezzature); D.M. 19/8/1996 (requisiti del palcoscenico); NTC D.M. 17/1/2018 (strutture della torre).',
  'Prevedi la manutenzione del macchinismo nel progetto: camminamenti di accesso, punti di ancoraggio, spazi per lo smontaggio degli argani. Un argano che non si puo\u0300 ispezionare in sicurezza e\u0300 un guasto annunciato.'),

S('Strutture', 'Strutture di sala e torre: grandi luci senza pilastri',
  'La sala da spettacolo impone spazi senza supporti intermedi: platea e palchi appoggiati a strutture perimetrali, copertura di grande luce, torre scenica alta e snella, gallerie a sbalzo. Le soluzioni classiche (muratura e capriate in legno o ferro) e quelle moderne (c.a., acciaio, strutture reticolari) devono integrare acustica (masse e isolamento), impianti (passaggi in copertura) e sicurezza (compartimentazione).',
  'Copertura sala: capriate metalliche o reticolari luce 15-35 m, o travi in c.a.; gallerie e palchi: strutture in c.a. gettato o acciaio con sbalzi 2-5 m; torre scenica: telai in c.a. o acciaio con controventi, carichi di graticcia e argani in sommita\u0300; fondazioni su terreni variabili con attenzione ai cedimenti differenziali tra corpi di fabbrica diversi; verifiche sismiche su edifici con grandi vuoti e masse in quota.',
  'Teatri di nuova costruzione, sopraelevazioni di torri sceniche, consolidamento di capriate storiche in legno, inserimento di gallerie in sale esistenti.',
  'Le strutture moderne liberano la sala da ogni vincolo di appoggio; l\u2019acciaio consente torri leggere e rapide; il consolidamento delle capriate storiche conserva il valore documentale.',
  'I cedimenti differenziali tra corpi (sala, torre, foyer) sono la patologia tipica; le grandi luci in copertura complicano l\u2019integrazione impiantistica; le gallerie a sbalzo richiedono verifiche rigorose di deformazione e vibrazione.',
  'Ordini di grandezza indicativi: struttura completa sala+torre 250-450 €/m2 di superficie coperta; capriata metallica di sala 100-180 €/m2; consolidamento di capriata storica in legno 30-80 k€/campata.',
  'Caso tipo: restauro di teatro ottocentesco: le capriate in legno, verificate con prove di carico locali e rinforzate con tiranti, restano in servizio; la nuova torre scenica in acciaio appoggia su fondazioni indipendenti per non caricare le murature storiche.',
  'NTC D.M. 17/1/2018 (azioni, sisma, edifici con grandi luci); UNI EN 1090 (acciaio); normativa sul consolidamento delle strutture storiche (Circolare NTC, da verificare).',
  'Separa staticamente i corpi nuovi da quelli storici e misura prima di fidarti dei disegni d\u2019epoca: il muro del proscenio non e\u0300 mai dove la pianta dice. Nei teatri storici prevedi sempre la campagna di indagini strutturali prima del progetto definitivo.'),

S('Impianti tecnici', 'Impianto elettrico scenico, reti e sicurezza',
  'La sala da spettacolo ha un impianto elettrico doppio: quello di servizio (illuminazione, prese, ausiliari) e quello scenico (potenze per dimmer e luci, reti dati DMX, audio, video). A questi si aggiungono gli impianti di sicurezza: illuminazione di emergenza, EVAC, rivelazione incendi, continuita\u0300 elettrica per i servizi essenziali. La separazione fisica e logica tra i sistemi e\u0300 la regola che evita i guasti in replica.',
  'Impianto scenico: quadri con potenze dedicate (centinaia di kW per sale medie), dimmer o relay, distribuzione a bacchetta e graticcia, prese di potenza normalizzate, rete DMX/ethernet scenico, ponti radio; servizio: illuminazione foyer e sala con scenografie, UPS e generatori per EVAC e emergenza, rivelazione e spegnimento selettivo; cablaggi con cavi resistenti al fuoco per i servizi di sicurezza; verifiche CEI e collaudi prima dell\u2019agibilita\u0300.',
  'Nuove sale, rifacimento impianti di teatri esistenti, adeguatezza delle potenze per produzioni moderne (LED wall, automazione scenica), messa a norma delle parti elettriche.',
  'Potenze e reti ben dimensionate ospitano qualsiasi produzione senza noleggi di gruppi; la separazione dei sistemi contiene i guasti; la continuita\u0300 dei servizi di sicurezza e\u0300 requisito di agibilita\u0300.',
  'Le potenze sceniche crescono (LED wall, motori): quadri sottodimensionati si saturano in pochi anni; i cavi scenici subiscono usura meccanica continua e vanno sostituiti a rotazione; il coordinamento con l\u2019acustica (rumore di dimmer e ventole) e\u0300 spesso dimenticato.',
  'Ordini di grandezza indicativi: impianto elettrico completo sala media (scenico + servizio) 80-200 €/m2; quadro dimmer/ridistribuzione scenica 100-400 k€; gruppo elettrogeno per emergenza 30-80 k€.',
  'Caso tipo: teatro che raddoppia la potenza scenica a 600 kW con nuovo quadro e dorsale dati in fibra: le produzioni con LED wall non richiedono piu\u0300 gruppi elettrogeni a noleggio e la sala entra nei circuiti delle tournée.',
  'CEI 64-8 (impianti elettrici, luoghi con affollamento); D.M. 19/8/1996 (requisiti impianti); normativa CEI per i luoghi di spettacolo (da verificare nelle parti specifiche); D.Lgs 81/2008 (manutenzione impianti scenici).',
  'Fai il collaudo dell\u2019impianto con la produzione piu\u0300 esigente prevista, non con le luci di casa: scopri i limiti del quadro in prova, non alla prima. E documenta ogni linea scenica: in replica il buio non ammette schemi approssimativi.'),

S('HVAC', 'Climatizzazione e qualità dell\u2019aria nelle sale',
  'Climatizzare una sala da spettacolo significa gestire carichi termici elevati e variabili (affollamento, luci sceniche) con requisiti acustici severissimi: l\u2019impianto deve essere potente e silenzioso (NR 20-25 in sala), con ricambi d\u2019aria adeguati alla capienza e nessun moto d\u2019aria percepibile sul pubblico e sulla scena (i costumi leggeri tradiscono ogni spiffero).',
  'Impianti ad aria primaria con grandi UTA a bassa velocita\u0300, condotte silenziate (silenziatori a setti, plenum), immissione dal basso (bocchette sotto-poltrona) o dall\u2019alto a induzione controllata, estrazione in sommita\u0300; controllo CO2 per modulare i ricambi sull\u2019affollamento reale; unita\u0300 su supporti antivibranti, isolate acusticamente dalla sala; regolazione a zone (sala, palco, foyer) per gestire le diverse occorrenze.',
  'Sale nuove ed esistenti, riqualificazione energetica dei teatri, adeguamento dei ricambi post-pandemia, contenimento del rumore impiantistico.',
  'Aria ben progettata = confort invisibile e acustica intatta; il controllo CO2 riduce i consumi nelle sale a mezzo servizio; l\u2019immissione dal basso usa la stratificazione a favore.',
  'I silenziatori e le basse velocita\u0300 richiedono condotte grandi: spazi tecnici da prevedere in struttura; la riqualificazione in sale storiche trova raramente i vani impianto adeguati; il controllo delle turbolenze in scena impone prove a regimi reali.',
  'Ordini di grandezza indicativi: HVAC sala con requisiti NR 25 120-250 €/m2 di sala; silenziatori e plenum 20-50 k€; controllo CO2 con sondaggio 5-15 k€.',
  'Caso tipo: riqualificazione di teatro con UTA in centrale lontana, condotte silenziate e immissione sotto-poltrona: il rumore di fondo scende sotto NR 25 e i consumi calano del 30% con il controllo a CO2.',
  'D.M. 19/8/1996 (aerazione); UNI EN ISO 7730 (confort); normativa sui ricambi per luoghi di pubblico spettacolo (da verificare); rinvio a ACUSTICA_EDILIZIA_PACK per i livelli NR.',
  'Prova l\u2019impianto a piena portata con la sala vuota e il tecnico acustico presente: il fischio della bocchetta si sente solo a teatro in silenzio. E metti le serrande motorizzate dove la manutenzione ci arriva davvero.'),

S('Front of house', 'Spazi per il pubblico: foyer, servizi, accessibilità',
  'Il front of house vende l\u2019esperienza: biglietteria, guardaroba, foyer, bar, servizi igienici dimensionati sull\u2019affollamento degli intervalli, percorsi accessibili a ogni posto riservato. Sono gli spazi che la commissione di vigilanza misura per prima e che il pubblico ricorda: un teatro con servizi insufficienti perde pubblico indipendentemente dal cartellone.',
  'Indici: foyer 0,3-0,6 m2/spettatore secondo livello; servizi igienici dimensionati sulla capienza con riparto e numero di apparecchi secondo regolamento (D.M. 19/8/1996 e normativa igienica); posti per spettatori con disabilita\u0300 in posizioni integrate (non solo in fondo), con percorsi dedicati dall\u2019ingresso, servizi accessibili e posti accompagnatori; segnaletica, illuminazione di accoglienza, spazi bar con sicurezza alimentare.',
  'Nuove sale, ampliamento foyer in teatri esistenti, adeguamento servizi igienici, inserimento dell\u2019accessibilita\u0300 completa in sale storiche.',
  'Foyer adeguati abilitano eventi collaterali (conferenze, ricevimenti) e ricavi accessori; l\u2019accessibilita\u0300 integrata e\u0300 requisito di legge e qualita\u0300 civile; servizi dimensionati sugli intervalli eliminano le code.',
  'Nei teatri storici il front of house e\u0300 quasi sempre sottodimensionato e l\u2019ampliamento urta i vincoli; i posti accessibili ricavati a posteriori sono spesso marginali; la gestione bar richiede requisiti igienici aggiuntivi.',
  'Ordini di grandezza indicativi: ristrutturazione foyer e servizi 1.000-2.000 €/m2; adeguamento servizi igienici a norma 30-100 k€; piattaforma elevatrice integrata 20-50 k€.',
  'Caso tipo: teatro storico che ricava il nuovo foyer nell\u2019atrio delle biglietterie e raddoppia i servizi con un corpo aggiunto in corte: gli intervalli tornano vivibili e i ricavi del bar coprono il nuovo personale di sala.',
  'D.M. 19/8/1996 (servizi e spazi); D.M. 236/1989 (accessibilita\u0300); normativa igienica per somministrazione (da verificare); regolamenti di igiene locali.',
  'Conta gli apparecchi igienici sull\u2019intervallo di 15 minuti, non sulla giornata: e\u0300 li\u0300 che la fila si forma. E collauda il percorso accessibile con una carrozzina vera dalla biglietteria alla poltrona: ogni barriera nascosta salta fuori.'),

S('Back of house', 'Back of house: camerini, produzione e logistica scenica',
  'Dietro il palco lavora la produzione: camerini, sartoria e costumeria, magazzini scene e costumi, officina, sala prove, carico e scarico delle scenografie con accesso al livello del palco. Il back of house ben progettato riduce i tempi di allestimento e i costi di produzione: quello sbagliato costringe le compagnie a lavorare per strada.',
  'Elementi: varco di carico al livello palco con portone dimensionato ai container scenici (orientativamente 3x4 m o piu\u0300), piazzale di manovra per mezzi pesanti, montacarichi scenico per i depositi fuori quota; camerini con servizi e docce (collettivi e di rappresentanza), sartoria con lavanderia, magazzini con controllo di umidita\u0300 per costumi e strumenti; sala prove con acustica e pavimento da danza; percorsi artisti separati dal pubblico.',
  'Teatri di produzione e di circuito, centri di residenza artistica, ampliamenti di sale esistenti, riuso di volumi adiacenti come depositi.',
  'Logistica scenica efficiente attira le produzioni (le tournée scelgono le sale dove si carica in sicurezza); depositi a norma conservano il patrimonio di scene e costumi; la sala prove moltiplica la redditivita\u0300 della struttura.',
  'Il varco di carico e\u0300 un vincolo geometrico rigido (altezze, raggi di manovra) che nei centri storici e\u0300 spesso impossibile da ricavare; i magazzini in teatro competono per lo spazio con tutto il resto; la sicurezza delle movimentazioni sceniche richiede procedure e formazione.',
  'Ordini di grandezza indicativi: varco di carico con portone e montacarichi 80-250 k€; camerini finiti 1.200-2.000 €/m2; magazzino scene con scaffalature e controllo climatico 600-1.000 €/m2.',
  'Caso tipo: teatro che ricava il carico scenico dal cortile posteriore con portone a tutta altezza e montacarichi da 3 t: le produzioni che prima scaricavano in strada con permessi eccezionali ora lavorano in coperto e la sala entra nel circuito nazionale.',
  'D.Lgs 81/2008 (movimentazione, lavoro in quota, camerini come luoghi di lavoro); D.M. 19/8/1996 (locali di servizio); normativa antincendio per i depositi (materiali scenici infiammabili); D.M. 236/1989 (accessibilita\u0300 anche per gli artisti).',
  'Progetta il percorso della scenografia dal camion al palco con le misure del container piu\u0300 grande previsto: ogni centimetro di strozzatura si paga a ogni allestimento. E non mettere il magazzino costumi sopra la caldaia: l\u2019umidita\u0300 e il calore rovinano il patrimonio.'),

S('Teatri storici', 'Adeguamento e riuso dei teatri storici',
  'Il patrimonio teatrale italiano e\u0300 fatto di sale storiche vincolate: l\u2019adeguamento alla sicurezza e alla funzionalita\u0300 contemporanea deve passare attraverso il rispetto del documento monumentale. Il progetto lavora su misure compensative, impianti reversibili, inserimenti leggibili e dialogo continuo con la Soprintendenza: l\u2019obiettivo e\u0300 una sala agibile e sicura che resti se stessa.',
  'Strategie: valutazione prestazionale antincendio con misure compensative dove i parametri del regolamento sono irraggiungibili; impianti reversibili e a secco (passaggi in controsoffitti tecnici ispezionabili, centrali remote); inserimento di corpi scala e uscite nuove in posizioni di rispetto; consolidamento strutturale compatibile (tiranti, rinforzi locali); acustica recuperata liberando le superfici storiche dai rivestimenti incongrui; documentazione con rilievo laser scan e HBIM.',
  'Teatri all\u2019italiana vincolati, sale in palazzi storici, cinema-teatro del Novecento, riaperture dopo lunghi abbandoni.',
  'Il valore culturale sostiene finanziamenti dedicati (pubblici e fondazioni); l\u2019approccio prestazionale consente l\u2019agibilita\u0300 senza snaturare; il restauro integrato (struttura, acustica, decoro) restituisce sale altrimenti perdute.',
  'Iter lungo con due autorita\u0300 (Soprintendenza e commissione di vigilanza) dai requisiti a volte confliggenti; costi imprevedibili (le sorprese dietro gli intonaci sono la regola); la capienza finale puo\u0300 restare limitata dalle geometrie storiche.',
  'Ordini di grandezza indicativi: restauro integrale di teatro storico medio 5-20 M€; rilievo laser scan e indagini preliminari 50-150 k€; percentuale di imprevisti da accantonare 15-25%.',
  'Caso tipo: riapertura di teatro chiuso dagli anni \u201990: HBIM completo, consolidamento dei palchi in legno con rinforzi nascosti, sipario tagliafuoco nuovo, impianti a secco sotto la platea smontabile: agibilita\u0300 per 350 posti con decoro integrale restaurato.',
  'D.Lgs 42/2004 (vincoli e autorizzazioni); D.M. 19/8/1996 e D.M. 3/8/2015 (con valutazione prestazionale); NTC D.M. 17/1/2018 (costruzioni esistenti); rinvio a RESTAURO_CONSERVAZIONE_PACK per le tecniche conservative.',
  'Prima di promettere tempi e costi su un teatro storico, apri i saggi: le capriate, i palchi e le murature raccontano la verita\u0300 solo a cantiere aperto. E porta in Soprintendenza le soluzioni, non i problemi: il dialogo tecnico anticipato dimezza l\u2019iter.'),

S('Economia', 'Economia e gestione della sala da spettacolo',
  'Una sala da spettacolo vive di ricavi da biglietteria, spazi accessori, convenzioni e contributi pubblici (lo spettacolo dal vivo e\u0300 sostenuto dal FUS e da fondi regionali): il progetto edilizio incide su tutti. Posti vendibili, costi di esercizio (energia, manutenzione macchinismo, personale di sicurezza) e capacita\u0300 di attrarre produzioni decidono la sostenibilita\u0300: il teatro progettato senza il piano di gestione e\u0300 un monumento ai costi.',
  'Voci economiche: costo di costruzione per posto (sala media finita 8.000-15.000 €/posto, fortemente variabile); esercizio: energia, manutenzione programmata del macchinismo (contratti full-service), personale tecnico e di sicurezza per serata; ricavi: biglietti, abbonamenti, affitto sala per eventi, bar e guardaroba, contributi pubblici legati a programmazione e accessibilita\u0300; piano capex per sostituzione poltrone, rinnovo impianti scenici, adeguamenti normativi.',
  'Studi di fattibilita\u0300 di nuove sale, piani di rilancio di teatri chiusi, valutazione di riuso di cinema e spazi dismessi, programmazione dei capex pluriennali.',
  'Il legame tra qualita\u0300 edilizia e ricavi e\u0300 diretto (confort, acustica, logistica attirano pubblico e produzioni); i fondi pubblici premiano accessibilita\u0300 e programmazione; gli spazi flessibili moltiplicano i giorni di apertura.',
  'I costi fissi di sicurezza e manutenzione gravano anche a sala chiusa; il pubblico pagante copre raramente tutto: serve il mix contributi-ricavi; gli adeguamenti normativi periodici sono capex non rinviabili.',
  'Ordini di grandezza indicativi: nuovo teatro medio 400-600 posti 8-25 M€; esercizio annuo sala media 300 k€-1 M€; manutenzione macchinismo scenico 20-60 k€/anno; ristrutturazione poltrone e platea 300-700 €/posto.',
  'Caso tipo: fondazione che gestisce un teatro riaperto con black box e foyer affittabile: i 220 giorni/anno di apertura (spettacoli + eventi) coprono i costi fissi e il fondo capex sostituisce le poltrone al decimo anno senza debiti.',
  'Normativa sullo spettacolo dal vivo e FUS (riferimenti ministeriali, da verificare); D.M. 19/8/1996 per gli standard che condizionano i costi; contratti di manutenzione e D.Lgs 81/2008 per il personale.',
  'Quando presenti il progetto, porta anche il conto economico di gestione: chi finanzia vuole sapere come la sala vive dopo l\u2019inaugurazione. E metti nel piano il fondo ricambi del macchinismo: l\u2019argano fermo il giorno della prima e\u0300 la fine della reputazione.'),
]

def main():
    os.makedirs(os.path.join(ROOT, 'schede'), exist_ok=True)
    with open(os.path.join(ROOT, 'schede', 'schede.jsonl'), 'w', encoding='utf-8', newline='\n') as f:
        for d in SCHEDE:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

    course = f'''corso: "Teatri e locali di pubblico spettacolo: agibilita' e licenza (TULPS, D.M. 19/8/1996, commissione di vigilanza), tipologie di sala e dimensionamento per spettatore, esodo e prevenzione incendi con affollamento, acustica di sala (riverbero, NR, box-in-box), palcoscenico e torre scenica (macchinismo, graticcia, argani), strutture di grande luce, impianto elettrico scenico e sicurezza, HVAC a bassa rumorosita', front of house (foyer, servizi, accessibilita'), back of house (carico scenico, camerini, depositi), adeguamento dei teatri storici, economia e gestione della sala"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L1-L2"
schede: {len(SCHEDE)}
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "R.D. 773/1931 TULPS (artt. 68 ss.), D.M. 19/8/1996 (regolamento costruzione locali di pubblico spettacolo), DPR 151/2011, D.M. 3/8/2015, UNI EN 12101, D.M. 236/1989, UNI EN ISO 3382-1, L. 447/1995, DPCM 5/12/1997, Direttiva Macchine 2006/42/CE, D.Lgs 81/2008, NTC D.M. 17/1/2018, UNI EN 1090, CEI 64-8, D.Lgs 42/2004; normativa spettacolo dal vivo (FUS) e regolamenti citati come da verificare"
nota_metodologica: "Corso tipologico su teatri e locali di pubblico spettacolo: agibilita' e licenza (TULPS, D.M. 19/8/1996, capienza autorizzata, commissione di vigilanza), tipologie di sala (all'italiana, black box, arena; indici m2/posto, passi file, visibilita'), esodo e antincendio (sipario tagliafuoco, moduli di uscita, EVAC), acustica (Tr 0,7-1,8 s per funzione, NR 20-25, box-in-box), palcoscenico e torre scenica (boccascena 8-14 m, graticcia, argani motorizzati, Direttiva Macchine), strutture di grande luce (capriate, gallerie a sbalzo, cedimenti differenziali), impianti (scenico vs servizio, dimmer, DMX, continuita' sicurezza), HVAC silenziato (immissione sotto-poltrona, controllo CO2), front of house (foyer, servizi per intervallo, accessibilita' integrata), back of house (varco di carico, camerini, depositi), teatri storici (misure compensative, impianti reversibili, Soprintendenza), economia (costo per posto, FUS, capex). NON ridondante: nessun pack tratta lo spettacolo dal vivo (solo Colosseo storico nei titoli); acustica e illuminotecnica solo di rinvio ai pack dedicati. Norme di consolidata certezza; parametri regolamentari con rinvio al D.M. 19/8/1996; prezzi come fasce indicative; nessun nome di azienda."
'''
    with open(os.path.join(ROOT, 'COURSE.yaml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(course)

    readme = f'''# Teatri e locali di pubblico spettacolo

Corso L1-L2 della Facolta di Tecnologia e Costruzione: la sala da spettacolo come tipologia edilizia completa — agibilita' e licenza (TULPS R.D. 773/1931, regolamento di costruzione D.M. 19/8/1996, commissione di vigilanza e capienza autorizzata), tipologie di sala e dimensionamento per spettatore (indici, passi file, visibilita'), esodo e prevenzione incendi con grande affollamento (sipario tagliafuoco, moduli di uscita, EVAC), acustica di sala (tempo di riverbero per funzione, NR 20-25, box-in-box), palcoscenico e torre scenica (geometria, graticcia, argani motorizzati e Direttiva Macchine), strutture di grande luce senza pilastri (capriate, gallerie a sbalzo, torri), impianto elettrico scenico e di sicurezza (potenze, dimmer, reti DMX, continuita'), climatizzazione a bassa rumorosita' (immissione sotto-poltrona, controllo CO2), front of house (foyer, servizi igienici per l'intervallo, accessibilita' integrata), back of house (varco di carico scenico, camerini, depositi), adeguamento e riuso dei teatri storici (misure compensative, impianti reversibili, dialogo con Soprintendenza) ed economia e gestione della sala (costo per posto, FUS, capex pluriennali).

**Schede: {len(SCHEDE)}**

Non ridondante: nessun pack esistente tratta lo spettacolo dal vivo. ACUSTICA_EDILIZIA_PACK e ILLUMINAZIONE_TECNICA_PACK restano i riferimenti per i fondamenti acustici e illuminotecnici; qui la tipologia edilizia completa — autorizzativa, strutturale, impiantistica, scenotecnica ed economica.
'''
    with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(readme)

    for d in SCHEDE:
        assert list(d.keys()) == K
        s = json.dumps(d, ensure_ascii=False)
        assert 'aplicazioni' not in s and 'tegnologia' not in s
    print('OK', PACK, len(SCHEDE), 'schede')

if __name__ == '__main__':
    main()
