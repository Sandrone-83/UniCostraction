# -*- coding: utf-8 -*-
"""Giro P: crea MEZZI_SOLLEVAMENTO_MOVIMENTAZIONE_PACK (12 schede)."""
import json, os

KEYS = ['categoria','nome','descrizione','tecnologia','applicazioni','vantaggi','limiti','costi_e_economia','casi_real_world','normative','note_cantiere']
P = 'UNIVERSITA_EDILIZIA/MEZZI_SOLLEVAMENTO_MOVIMENTAZIONE_PACK'
os.makedirs(P + '/schede', exist_ok=True)

S = [
("Fondamenti","Il sistema dei mezzi di sollevamento in cantiere: classificazione e scelta",
 "Sollevare e movimentare e' meta' del lavoro di un cantiere: materiali, prefabbricati, casseforme, attrezzature. Scegliere il mezzo giusto significa dimensionarlo su tre variabili: peso, raggio orizzontale e altezza di sollevamento.",
 "Mezzi a scelta: gru a torre per cantieri edili di media e grande estensione; autogru e camion-gru per interventi rapidi e sagomati; piattaforme di lavoro elevabili (PLE) per lavori in quota su facciate; ponteggi come sistema di accesso prolungato; paranchi, verricelli, montacarichi per il sollevamento verticale; carriponte e portali negli stabilimenti. La scelta parte dalla scheda di sollevamento: peso al gancio, raggi di lavoro, altezze, tempi di utilizzo.",
 "Organizzazione di cantiere, preventivi dei lavori di movimentazione, scelta tra noleggio e acquisto, pianificazione delle fasi critiche.",
 "Nessun cantiere moderno va avanti senza questi mezzi: pianificarli bene evita fermi macchina che bruciano migliaia di euro al giorno.",
 "Il mezzo giusto al momento sbagliato resta inutile: le fasi di cantiere vanno sincronizzate con la disponibilita' dei mezzi, specie quelli noleggiati.",
 "Ordini di grandezza indicativi: noleggio autogru 60-150 €/ora con minimo giornaliero; gru a torre 2.500-6.000 €/mese piu' montaggio 8.000-20.000 €; PLE 150-400 €/giorno; ponteggio 15-35 €/m² installato.",
 "Cantiere residenziale: camion-gru per posa tetti di legno in una giornata, poi smontaggio, invece di una settimana di ponteggio dedicato.",
 "D.Lgs 81/2008 e s.m.i. (attrezzature di lavoro, formazione degli operatori); UNI EN 13000 (gru mobili, criteri generali di progetto citati per cultura di settore).",
 "Prima di noleggiare, fare la scheda di sollevamento con pesi reali (non stimati): il sovraccarico al gancio e' la prima causa di incidente grave."),
("Gru a torre","Gru a torre: componenti, fondazioni, ancoraggi e cantiere",
 "La gru a torre e' il mezzo simbolo del cantiere edile: alta, potente, presente per mesi. Funziona solo se base, ancoraggi e interferenze sono stati progettati, non improvvisati.",
 "Componenti: basamento su zavorra o su plinti di fondazione gettati ex novo, traliccio, braccio orizzontale (o a punta) con carrello, contrappeso, argano e gancio. La capacita' massima e' al carrello vicino alla torre e cresce a mano a mano che il carrello si allontana: il diagramma di carico regola ogni manovra. Ancoraggi intermedi a edificio ogni certo numero di tralicci secondo progetto del costruttore.",
 "Cantieri edili di media e grande dimensione, posa di prefabbricati, movimentazione continua di materiali su piu' piani.",
 "Copre tutta l'area del cantiere da un punto solo; altezze e portate elevatissime; con il carrello a radio comando la manovra e' precisa anche a grande distanza.",
 "Costi fissi pesanti: fondazioni, montaggio con autogru grande, smontaggio, permessi per interferenze con vie e linee elettriche; altezza libera limitata da ostacoli e norme aeronautiche locali.",
 "Ordini di grandezza indicativi: gru a torre da cantiere residenziale 40.000-90.000 € usata e 120.000-250.000 € nuova; fondazioni dedicate 5.000-15.000 €; viaggio di montaggio 3.000-8.000 €.",
 "Quartiere residenziale: gru a torre su plinti gettati, ancoraggi intermedi al fabbricato a ogni tre piani, posa di 120 prefabbricati in 20 giorni.",
 "D.Lgs 81/2008 (attrezzature di lavoro e verifiche); prescrizioni del costruttore del mezzo per fondazioni, ancoraggi e sovrapposizioni.",
 "Le interferenze tra due gru dello stesso cantiere si gestiscono con piano di costruzione: mai far lavorare i bracci allo stesso piano senza zone vietate."),
("Autogru","Autogru e camion-gru: diagrammi di carico, slancio e contrappesi",
 "L'autogru e' la soluzione flessibile: arriva, starga, solleva e riparte. Ma la sua capacita' crolla con la distanza: il diagramma di carico e' la sua carta d'identita'.",
 "Struttura: cabina di comando, braccio telescopico o reticolare, argano, braccetti di stabilizzazione (staffe) che scaricano il peso su tamponi. Il diagramma di carico riporta portata in funzione del raggio (distanza orizzontale dal centro di rotazione) e dell'altezza di gancio: a braccio tutto esteso e in piano la portata residua puo' essere un decimo di quella minima. I contrappesi aumentano la stabilita' ma non cambiano il diagramma.",
 "Posa di manufatti leggeri, scarico materiali, lavori di manutenzione industriale, cantieri poco estesi o brevi.",
 "Rapidita': si sposta da solo, non serve fondazione, e copre interventi impossibili per la gru a torre.",
 "Il diagramma di carico e' tabella sacra: ignorarlo, anche per pochi metri di slancio in piu', porta al ribaltamento; il suolo sotto le staffe va verificato (tamponi su soletta, non su terreno sconosciuto).",
 "Ordini di grandezza indicativi: noleggio 60-150 €/ora con minimo; trasporto del mezzo 200-600 €; tamponi e cunei 100-400 €; aumento contrappesi dedicato da preventivo.",
 "Scarico carico di laterizi in centro storico: camion-gru con staffe su protezioni, raggio minimo e posa diretta su ponteggio di carico.",
 "D.Lgs 81/2008 (uso in sicurezza); UNI EN 13000 (requisiti per gru mobili); manuale del costruttore con diagrammi di carico.",
 "Stampare il diagramma e tenerlo in cabina: il segnalatore a terra deve conoscere il raggio esatto prima di dare il via alla manovra."),
("PLE","Piattaforme di lavoro elevabili (PLE): tipi, stabilizzatori e uso corretto",
 "La PLE (piattaforma di lavoro elevabile) sostituisce scala e impalcatura per lavori brevi in quota: pulizia facciate, manutenzione impianti, tinteggiatura. E' veloce ma va usata dentro i suoi limiti.",
 "Tipi: a pantografo (verticali, per interni e pavimentazioni regolari), a braccio articolato e telescopico (per aggirare ostacoli), a ragno (leggere, fuoristrada leggere e cortili). Sistema di comando da basket con selettori di emergenza a terra, allarme di inclinazione e dispositivi di blocco in caso di perdita di stabilita'. Stabilizzazione su zattere o ruote con bloccaggio prima dell'alzata.",
 "Edilizia di manutenzione, pulizia e verniciatura di facciate, lavori elettrici e idraulici in quota, allestimento eventi e luci.",
 "Montaggio in pochi minuti senza ponteggio; raggiunge quote che un ponteggio raggiungerebbe solo in giorni; occupa poco spazio a terra.",
 "Non e' un mezzo di sollevamento materiali: il cestello e' per persone; il vento sopra certe velocita' vieta l'uso delle versioni leggere; il suolo sconnesso richiede la versione a ragno o lo spianamento.",
 "Ordini di grandezza indicativi: noleggio giornaliero 150-400 €; settimanale 500-1.200 €; corso abilitante per operatori 200-500 €; trasporto con bisarca 150-350 €.",
 "Manutenzione ordinaria condominiale: PLE a pantografo in corte interna per rifacimento pluviali e tinteggiatura cornicioni in tre giorni.",
 "UNI EN 280 (progettazione e calcolo delle PLE); D.Lgs 81/2008 (formazione degli operatori e verifiche periodiche).",
 "Leggere la targhetta: ogni PLE ha portata nominale persone e carichi; mai superarla con attrezzature, il cestello non e' un montacarichi."),
("Ponteggi a telai","Ponteggi metallici a telai: montaggio, vincoli e carichi ammissibili",
 "Il ponteggio a telai e' la spina dorsale dei lavori su facciata: una struttura temporanea metallica che deve reggere persone, materiali e talvolta gru a piattaforma. Va montata da personale abilitato secondo progetto.",
 "Elementi: telai standard (portanti), traverse, correnti di piano di calpestio, catenarie e paraoli, paravento, basi regolabili su piastre o cunei, ancoraggi a parete distanziati secondo progetto (scarpata, tiranti, cavalletti). Classi di carico: ponti di servizio leggeri (2 kN/m²) fino a ponti di carico con gru a piattaforma; la classe detta passo dei telai, doppiatura degli appoggi e dimensionamento.",
 "Restauri, tinteggiature, rifacimenti di facciata, lavori su edifici esistenti di ogni epoca.",
 "Permette lavori prolungati e organizzati su tutta la facciata con deposito materiali a piano; protegge il marciapiede con canopi; integra coperture e reti di cantiere.",
 "Invade suolo pubblico con concessione; il montaggio e' lento e costoso su fronti brevi; vincola finestre e accessi per mesi.",
 "Ordini di grandezza indicativi: noleggio e montaggio 15-35 €/m² di facciata; canopio su marciapiede 10-25 €/m.l.; tirafondi e ancoraggi 5-15 €/cad.",
 "Restauro palazzo storico: ponteggio multidirezionale su androne, canopio su marciapiede, reti anti-detriti e passerella carrabile.",
 "UNI EN 12810 (metodo del telaio, ponteggi di facciata); UNI EN 12811 (requisiti prestazionali e carichi); D.Lgs 81/2008 (montaggio da ditte abilitate e verifiche).",
 "L'ancoraggio a parete e' il punto debole: su murature antiche verificare la resistenza prima di caricare, mai ancorare su intonaco o laterizio cavo senza dispositivi dedicati."),
("Ponteggi speciali","Ponteggi multidirezionali, sospesi e strutture speciali",
 "Quando la facciata e' complessa — cupole, torri, ponti, fronti in quota su roccia — il ponteggio a telai non basta: entrano i sistemi multidirezionali (fermate su ogni direzione) o i ponteggi sospesi.",
 "Multidirezionale: tubi con calettatori omni-direzionali che realizzano qualsiasi geometria, coperture di cantiere, torri di sostegno, passerelle. Ponteggio sospeso: piattaforme appese a cavi o bracci a sbalzo per facciate alte (grattacieli, silos) senza appoggio a terra. Strutture speciali: coperture provvisorie, torri di sostegno per varo, banchine di montaggio prefabbricati.",
 "Ponti e viadotti, cupole e chiese, torri, facciate di grande altezza, cantieri con interferenze a terra intense.",
 "Adattabile a qualsiasi geometria; sospeso lavora dove a terra non c'e' spazio; riduce al minimo l'ingombro su suolo pubblico.",
 "Progettazione specifica obbligatoria: niente schemi standard; costi di studio e montaggio alti; il sospeso dipende da ancoraggi in quota di altissima affidabilita'.",
 "Ordini di grandezza indicativi: ponteggio multidirezionale 20-45 €/m²; progettazione strutturale temporanea 1.500-6.000 €; piattaforma sospesa 250-600 €/giorno installata.",
 "Cupola di chiesa: ponteggio multidirezionale interno a ferro di cavallo per mosaici, con passerelle inclinate e illuminazione integrata.",
 "UNI EN 12811 (requisiti per ponteggi di tipo diverso dal telaio); D.Lgs 81/2008 (progetto di strutture provvisorie e verifiche); DPR 177/2011 (requisiti ditte ponteggi).",
 "Le strutture temporanee che durano mesi vanno verificate dopo ogni evento atmosferico eccezionale: pioggia, neve e vento lavorano su di esse come su quelle definitive."),
("Sollevamento verticale","Paranchi, verricelli, montacarichi e mini-gru da cantiere",
 "Per muovere carichi in verticale dentro il cantiere — sacchi, casseforme, attrezzature — esistono macchine piccole ma decisive: paranchi a fune o catena, verricelli, montacarichi a cremagliera e mini-gru autocarrate.",
 "Paranco: argano a fune o catena con gancio, portate da 0,5 a 10 t, azionamento elettrico o manuale; i paranchi elettrici a catena hanno limitatore di sovraccarico. Vernicello: argano orizzontale o inclinato per trascinare carichi. Montacarichi: torretta a cremagliera con cabina per persone e materiali, con finecorsa e dispositivi anti-caduta. Mini-gru: gru cingolata compatta che passa da portone e solleva sui piani con braccio articolato.",
 "Cantieri edili in corpo esistente, movimentazione tra piani, alimentazione ponteggi, cantieri di restauro con accessi ridotti.",
 "Portano il sollevamento dentro l'edificio senza gru esterne; il montacarichi copre tutta la durata del cantiere; la mini-gru entra dove un mezzo grande non passa.",
 "Piccole ma non innocue: un paranco sovraccarico che cede e' un proiettile; i montacarichi richiedono manutenzione della cremagliera e verifiche periodiche senza scuse.",
 "Ordini di grandezza indicativi: paranco elettrico a catena 300-2.500 €; noleggio mini-gru 100-250 €/giorno; montacarichi noleggio 800-1.800 €/mese piu' installazione; verricello 150-600 €.",
 "Restauro in centro storico: mini-gru in corte interna che alimenta il ponteggio, montacarichi per gli operai, zero gru a torre in vista.",
 "D.Lgs 81/2008 (attrezzature di sollevamento, verifiche periodiche); UNI EN 14492-2 (apparecchi di sollevamento a fune o catena, requisiti); prescrizioni del costruttore.",
 "Ispezionare la fune o la catena prima di ogni turno: un filo spezzato o una maglia deformata giustifica la sostituzione immediata, non la speranza."),
("Industria","Carriponte, portali e sistemi di movimentazione industriale",
 "Nelle officine, nei magazzini e nelle prefabbricazioni la movimentazione e' industriale: carriponte su rotaie, portali semi-automatici e sistemi di stoccaggio che lavorano migliaia di cicli l'anno.",
 "Carriponte: ponte orizzontale su due carrelli di estremita' che viaggiano su rotaie aeree, con paranco centrale; portate da poche tonnellate a centinaia. Portali: struttura a portale su rotaie a terra o su pneumatici per esterni e depositi. Sistemi correlati: sollevatori a forche, nastri, transpallet elettrici, scaffalature con stoccatori. Ogni sistema ha il suo piano di manutenzione e le verifiche di legge.",
 "Capannoni industriali, officine meccaniche, depositi di prefabbricazione, logistica pesante.",
 "Movimenta carichi che nessun mezzo da cantiere regge in continuita'; integra la produzione: la linea non si ferma se il carroponte e' affidabile.",
 "Richiede opere civili serie (rotaie, fondazioni, armadi di comando); un guasto ferma l'intera produzione; gli incollaggi su binari vanno tenuti puliti.",
 "Ordini di grandezza indicativi: carroponte monotrave 8.000-25.000 € installato; bitrave 15.000-60.000 €; portale 10.000-40.000 €; contratto manutenzione 1.500-6.000 €/anno.",
 "Prefabbricazione: carriponte bitrave da 20 t con benna magnetica per magazzino ferri, cicli continui con operatore in cabina radiocomandata.",
 "D.Lgs 81/2008 (attrezzature con obbligo di verifiche periodiche); UNI EN ISO 4309 (funi, criteri di sostituzione); manuale costruttore per le scadenze.",
 "Le rotaie del carroponte vanno allineate e lubrificate: il 50% dei guasti costosi nasce da binari trascurati, non dal motore."),
("Sotto il gancio","Imbragature, stralli e attrezzature di sollevamento accessorie",
 "Il carico viaggia appeso a funi, catene, stralli e ganci: e' la parte meno appariscente e piu' pericolosa di tutto il sistema. Il fattore di utilizzo e la geometria dell'imbragatura decidono se il carico arriva o cade.",
 "Attrezzature: funi metalliche (funi a trefoli, con morsetti e ganci), catene a maglia con ganci di sicurezza, stralli sintetici a telaio (cinghie), grillo a omega, bilancieri e spalmatoi per carichi lunghi. Fattore di utilizzo: rapporto tra portata dell'attrezzatura e carico reale; le norme impongono margini diversi per sollevamento persone e materiali. Angoli di imbragatura: piu' il ventre e' aperto, piu' ciascuna fune lavora.",
 "Ogni sollevamento di carichi sagomati, prefabbricati, macchinari, casseforme e silos.",
 "Attrezzature leggere e versatili: un set di stralli e grilli risolve sollevamenti che il gancio nudo non puo' fare; sintetici proteggono le superfici verniciate.",
 "La fune danneggiata non avverte: trefoli spezzati, schiacciamenti e corrosione interna riducono la portata invisibilmente; gli angoli sbagliati raddoppiano lo sforzo sulle branche.",
 "Ordini di grandezza indicativi: fune metallica con ganci 20-80 €/metro; strallo sintetico 15-60 €; grillo 5-30 €; bilanciere per carichi lunghi 200-800 €; rinnovo certificato periodico secondo uso.",
 "Posa di prefabbricati sagomati: bilanciere a quattro branche con stralli regolabili, imbragatura calcolata sull'angolo reale di lavoro.",
 "UNI EN ISO 4309 (funi metalliche: abbandono e sostituzione); UNI EN 818 (catene di sollevamento, componenti); UNI EN 1492-1/-2 (imbragature sintetiche).",
 "Mai raccorciare una fune con nodi improvisati ne' saldare attrezzature di sollevamento: la certificazione vale finche' l'attrezzatura resta originale e ispezionabile."),
("Piani di manovra","Piani di sollevamento, segnali e direzione delle manovre",
 "Ogni sollevamento delicato si progetta prima di muovere il gancio: piano di sollevamento, zona di esclusione, segnalatore dedicato e comunicazioni chiare tra cabina e terra.",
 "Il piano di sollevamento (lift plan) riporta: peso e baricentro del carico, mezzo e configurazione (braccio, contrappesi), raggio e altezza di lavoro, percorso del carico, zone di esclusione a terra, ruoli (operatore macchina, segnalatore, imbragatore). Segnali standard a gesti o radio: quota, abbassa, sposta, stop immediato. Il segnalatore e' l'unico che parla con l'operatore.",
 "Sollevamenti di prefabbricati pesanti, macchinari, lavori vicino a linee elettriche, interventi con piu' mezzi contemporanei.",
 "Il 90% degli incidenti di sollevamento muore nel caos di comunicazione: un piano scritto e un solo segnalatore li azzerano quasi del tutto.",
 "I piani non scritti restano desideri: se cambia qualcosa (vento, ostacolo, peso diverso dal previsto) il piano va fermato e riscritto, non adattato al volo.",
 "Ordini di grandezza indicativi: redazione piano di sollevamento 300-1.500 € secondo complessita'; riunione pre-lavoro (safety briefing) inclusa nella gestione di cantiere.",
 "Posa cassaforme 12 t in stazione ferroviaria in esercizio: piano con finestra notturna, zona di esclusione con nastri e vigilanza, segnalatore unico collegato in radio alla cabina.",
 "D.Lgs 81/2008 (organizzazione delle manovre e figure dedicate); manuale del costruttore del mezzo per i limiti operativi.",
 "Stop assoluto: chiunque sul cantiere vede un pericolo alza le braccia incrociate e la manovra si ferma senza discussione, poi si riparte solo dopo verifica."),
("Adempimenti","Verifiche, manutenzione e adempimenti degli apparecchi di sollevamento",
 "Le attrezzature di sollevamento sono tra i pochi oggetti del cantiere con obblighi di legge scritti nel sangue: verifiche iniziali, periodiche e straordinarie, libretti e personale formato. Mancarli e' reato e disgrazia insieme.",
 "D.Lgs 81/2008: attrezzature di lavoro con verifica iniziale prima dell'uso, verifica periodica (scadenze secondo il tipo di attrezzatura e il decreto), verifica straordinaria dopo riparazioni o modifiche. Documentazione: libretto con dichiarazione CE, verbali di verifica, manutenzione programmata registrata. Persone: operatori formati per ciascuna tipologia di mezzo; montaggio ponteggi solo da ditte con requisiti specifici.",
 "Gestione della sicurezza in cantiere, uffici tecnici delle imprese, conduttori di mezzi, direzione lavori in verifica documentale.",
 "Tutto cio' che serve a dimostrare di aver operato correttamente e' gia' previsto: basta farlo e registrarlo.",
 "La documentazione scade senza suonare: il libretto dimenticato in ufficio ferma il cantiere al controllo piu' scomodo; le verifiche fatte ma non registrate valgono zero.",
 "Ordini di grandezza indicativi: verifica periodica mezzo 100-400 € a seconda di tipo; corso aggiornamento operatori 150-400 €; software di scadenziario mezzi 200-800 €/anno.",
 "Impresa edile media: scadenziario unico con tutti i mezzi, verifiche raggruppate in soste programmate, zero fermi imprevisti a cantiere aperto.",
 "D.Lgs 81/2008 (Allegato XXX elenco attrezzature soggette a verifica periodica); DPR 177/2011 (requisiti ditte montaggio ponteggi).",
 "Associare a ogni mezzo un fascicolo digitale con scadenze: la verifica si prenota con 30 giorni di anticipo, non il giorno prima del sequestro."),
]

with open(P + '/schede/schede.jsonl', 'w', encoding='utf-8') as f:
    for row in S:
        d = dict(zip(KEYS, row))
        assert list(d.keys()) == KEYS
        f.write(json.dumps(d, ensure_ascii=False) + '\n')

course = '''corso: "Mezzi di sollevamento e movimentazione"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L1-L2"
schede: 12
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "D.Lgs 81/2008, UNI EN 12810, UNI EN 12811, UNI EN 280, UNI EN 13000, UNI EN 14492-2, UNI EN 818, UNI EN ISO 4309, UNI EN 1492, DPR 177/2011"
nota_metodologica: "Mezzi di sollevamento e movimentazione di cantiere: scelta, uso e adempimenti. Norme e decreti citati solo dove consolidati; le scadenze precise delle verifiche periodiche vanno lette nell'Allegato XXX del D.Lgs 81/2008 vigente."
'''
open(P + '/COURSE.yaml', 'w', encoding='utf-8').write(course)

readme = '''# Mezzi di sollevamento e movimentazione — Pack

Dodici schede operative sui mezzi che sollevano e movimentano in cantiere e
in industria: gru a torre, autogru, piattaforme di lavoro elevabili (PLE),
ponteggi a telai e multidirezionali, paranchi e montacarichi, carriponte e
portali, attrezzature di sotto il gancio, piani di sollevamento e
adempimenti di legge (verifiche periodiche, personale formato, libretti).

Struttura dati: `schede/schede.jsonl`, una scheda JSON per riga, con le 11
chiavi standard della repository (categoria, nome, descrizione, tecnologia,
applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world,
normative, note_cantiere). I costi sono ordini di grandezza indicativi.

Fonte principale: D.Lgs 81/2008 (attrezzature di lavoro) e norme europee
adottate in Italia (UNI EN) citate per esteso nelle schede.
'''
open(P + '/README.md', 'w', encoding='utf-8').write(readme)
print('MEZZI_SOLLEVAMENTO_MOVIMENTAZIONE_PACK creata:', len(S), 'schede')
