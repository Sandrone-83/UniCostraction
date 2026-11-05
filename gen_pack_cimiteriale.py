# -*- coding: utf-8 -*-
"""Giro AQ: genera EDILIZIA_CIMITERIALE_PACK (12 schede)."""
import json, os

PACK = 'EDILIZIA_CIMITERIALE_PACK'
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

S('Quadro normativo', 'Quadro normativo e pianificazione cimiteriale',
  'Il cimitero e\u0300 un\u2019opera pubblica con disciplina propria: la costruzione, l\u2019ampliamento e la gestione sono regolati dal Regolamento di Polizia Mortuaria e dalle leggi regionali, con piani cimiteriali comunali che dimensionano la capacita\u0300 sul tasso di mortalita\u0300 e sul turn-over delle concessioni. Chi progetta deve conoscere i vincoli di localizzazione, le autorizzazioni sanitarie e i rapporti con la pianificazione urbanistica: un cimitero sbagliato non si sposta.',
  'Piano cimiteriale comunale: analisi demografica (tasso di mortalita\u0300 locale, proiezione 30-50 anni), riparto tra sepolture in terra, loculi e ceneri secondo la domanda locale; vincolo di distanza: il Regolamento di Polizia Mortuaria fissa la distanza minima dai centri abitati (orientativamente 200 m, con possibilita\u0300 di deroghe motivate dall\u2019autorita\u0300 sanitaria — verificare il testo vigente e le leggi regionali); verifica geologico-idrogeologica propedeutica; autorizzazione sanitaria e procedura urbanistica (variante di PRG o piano attuativo secondo la regione).',
  'Nuovi cimiteri e ampliamenti, verifica di saturazione dei campi esistenti, piani cimiteriali intercomunali, insediamento di forni crematori e nuove aree cinerarie.',
  'Pianificazione demografica seria evita saturazioni improvvise (emergenza salute pubblica) e sovradimensionamenti costosi; il vincolo sanitario chiaro semplifica il dialogo con ASL e regione.',
  'Iter autorizzativo lungo (sanitario + urbanistico + spesso paesaggistico); le distanze dai centri abitati rendono difficile trovare aree idonee in comuni densi; i piani cimiteriali invecchiano male se non rivisti ogni 10-15 anni.',
  'Ordini di grandezza indicativi: piano cimiteriale con indagini geologiche 20-60 k€; studio idrogeologico con piezometri 10-40 k€; iter autorizzativo nuovo cimitero 2-5 anni.',
  'Caso tipo: unione di comuni montani che fonde i piani cimiteriali e concentra l\u2019ampliamento nel sito geologicamente migliore, dotandolo di forno crematorio intercomunale; i comuni minori mantengono solo i campi esistenti in manutenzione.',
  'DPR 285/1990 (Regolamento di Polizia Mortuaria); leggi regionali cimiteriali (da verificare per la regione); DPR 380/2001 (titolo edilizio); normativa ASL su autorizzazioni sanitarie.',
  'Prima ancora di disegnare, chiedi all\u2019ufficio mortuorio i dati veri: sepolture/anno, mix terra-loculi-ceneri, concessioni in scadenza. Il piano fatto sulle tabelle nazionali senza i dati del comune dura una stagione.'),

S('Sito e geologia', 'Vincolo idrogeologico e scelta del sito',
  'La sepoltura in terra impone requisiti geologici stringenti: il sito deve garantire che il fondo delle fosse resti sopra il massimo livello della falda acquifera con un franco di sicurezza, che il terreno sia sufficientemente permeabile ma non inquini gli acquiferi, e che non vi siano rischi di frana, allagamento o erosione. La verifica geologico-idrogeologica e\u0300 propedeutica a qualsiasi autorizzazione: non e\u0300 un adempimento formale.',
  'Indagini: fori geognostici e piezometri con monitoraggio stagionale della falda (almeno un ciclo idrologico se possibile), prove di permeabilita\u0300 (Lefranc/Lugeon secondo contesto), verifica della direzione di flusso verso eventuali pozzi e captazioni; il Regolamento di Polizia Mortuaria richiede che il fondo delle sepolture sia sopra il livello massimo di falda con un franco (orientativamente 2 m — verificare il testo vigente); in caso di falda alta: solo sepolture fuori terra (loculi) oppure rinuncia al sito.',
  'Selezione di nuovi siti cimiteriali, ampliamenti a valle di campi esistenti, conversione a soli loculi di aree con falda alta, verifiche richieste da ASL e ARPA.',
  'Indagine seria = autorizzazione sanitaria senza contenzioso e nessun rischio di inquinamento degli acquiferi; la conoscenza della falda guida il mix terra/loculi piu\u0300 economico.',
  'Monitoraggio di falda richiede mesi e costa; siti con falda alta o terreni troppo permeabili/impermeabili possono risultare inutilizzabili per sepolture in terra; vincoli idrogeologici (zone di tutela dei pozzi) escludono molte aree.',
  'Ordini di grandezza indicativi: campagna geognostica con 4-8 fori + piezometri e monitoraggio annuale 15-50 k€; relazione idrogeologica per autorizzazione 8-20 k€.',
  'Caso tipo: ampliamento cimiteriale in pianura alluvionale; i piezometri mostrano falda massima a 1,2 m dal p.c.: il progetto si converte integralmente a loculi fuori terra e campi in tumulazione su plateau impermeabilizzato, mantenendo l\u2019autorizzazione.',
  'DPR 285/1990 (requisiti del sito, verificare testo e aggiornamenti); D.Lgs 152/2006 (tutela acque sotterranee); leggi regionali cimiteriali e idrogeologiche (da verificare).',
  'Non promettere mai un ampliamento a sepolture in terra prima del monitoraggio di falda: se il fondo fossa finisce in acqua, il progetto si butta e la credibilita\u0300 del tecnico anche.'),

S('Organizzazione', 'Organizzazione funzionale: campi, servizi e flussi',
  'Un cimitero e\u0300 un organismo complesso: zone di sepoltura in terra (campi comuni e campi a rotazione), blocchi di loculi e colombari, tombe private e cappelle, servizi (ingresso con parco, uffici, obitorio, camere ardenti, laboratorio marmisti, servizi igienici, magazzini), viabilita\u0300 interna carrabile e pedonale. La progettazione deve separare i flussi: cortei funebri, visitatori, mezzi operativi e manutenzione hanno esigenze diverse e nei giorni di punta (commemorazione dei defunti) i carichi pedonali esplodono.',
  'Schema funzionale: ingresso principale con parco/foresteria e parcheggi (dimensionati per i picchi, non per il giorno medio), asse centrale di distribuzione, campi in terra a monte dei blocchi di loculi per gerarchia percettiva, area servizi in posizione baricentrica ma riservata, laboratori e piazzali di cantiere separati e schermati; percorso corteo funebre senza conflitti col flusso visitatori; recinzione perimetrale con chiusura e controllo accessi.',
  'Nuovi cimiteri, ampliamenti per lotti, riorganizzazioni funzionali di cimiteri storici, inserimento di forni crematori e aree cinerarie in impianti esistenti.',
  'Separazione dei flussi = decoro e sicurezza anche nei giorni di affollamento; servizi baricentrici riducono i costi di gestione; schema a lotti consente ampliamenti coerenti nel tempo.',
  'La dimensione dei picchi (2 novembre) viene regolarmente sottostimata: parcheggi e servizi vanno pensati per l\u2019evento, con gestione ordinaria diversa; i vincoli di recinzione e chiusura confliggono con l\u2019idea di parco aperto.',
  'Ordini di grandezza indicativi: sistemazioni esterne (viabilita\u0300, verde, illuminazione) 60-120 €/m2 di area trattata; edificio servizi (obitorio, uffici, camere ardenti) 1.500-2.500 €/m2.',
  'Caso tipo: ampliamento con nuovo ingresso e parco: il corteo arriva direttamente ai campi nuovi senza attraversare la parte storica; nei giorni di punta l\u2019asse centrale diventa solo pedonale con navetta per anziani.',
  'DPR 285/1990 (requisiti funzionali e sanitari); D.M. 236/1989 (accessibilita\u0300); normativa regionale cimiteriale (da verificare); D.Lgs 285/1992 per la viabilita\u0300 di accesso.',
  'Dimensiona parcheggi e servizi sul picco di inizio novembre e verifica il percorso carro funebre col tornante reale del mezzo: il progetto che funziona solo nel giorno medio e\u0300 un progetto fallito.'),

S('Sepolture in terra', 'Sepolture in terra e campi comuni',
  'La sepoltura in terra resta la forma piu\u0300 tradizionale: fosse singole in campi comuni, con periodo di sepoltura legato ai tempi di mineralizzazione delle salme (in Italia orientativamente 10 anni, secondo normativa mortuaria e regolamenti locali), poi esumazione e trasferimento in ossario o loculo. La progettazione riguarda drenaggio dei campi, stabilita\u0300 dei terreni di scavo, viabilita\u0300 di servizio e gestione della rotazione.',
  'Campi con parcelle ordinate e accessi carrabili per i mezzi di scavo; drenaggio sottosuperficiale dei campi (tubazioni forate e vespaio) dove il terreno lo richiede; profondita\u0300 e sezioni delle fosse secondo regolamento mortuario e sicurezza degli scavi; registro di campo con numerazione e piani di rotazione; terreno di risulta gestito come sottoprodotto o rifiuto secondo la caratterizzazione.',
  'Campi comuni di nuova formazione, riordino di campi esistenti, campi a rotazione accelerata (con terreni particolari), gestione post-esumazione.',
  'Costo unitario per sepoltura il piu\u0300 basso in assoluto; risposta alla domanda tradizionale; i campi a rotazione restituiscono capacita\u0300 nel tempo.',
  'Impatto al suolo elevato e vincoli di falda; tempi di mineralizzazione variabili col terreno (argille pesanti rallentano); gestione delle esumazioni delicata sotto il profilo organizzativo e umano; manodopera specializzata.',
  'Ordini di grandezza indicativi: sistemazione campo con drenaggio e viabilita\u0300 40-80 €/m2; costo complessivo per posto salma in terra (quota parte campo) 300-800 €, contro migliaia per il loculo.',
  'Caso tipo: comune che ripristina la rotazione dei campi comuni con drenaggio nuovo e registro informatico: la capacita\u0300 decennale raddoppia senza consumo di suolo aggiuntivo e senza nuovi blocchi di loculi.',
  'DPR 285/1990 (sepolture, esumazioni, verificare testo vigente); regolamenti comunali cimiteriali (tempi e modalita\u0300, da verificare); D.Lgs 152/2006 (gestione terre di scavo).',
  'Nei campi nuovi prevedi sempre il drenaggio e il passaggio dei mezzi: la fossa scavata a mano perche\u0300 la pala non ci passa costa il doppio e allaga alla prima pioggia.'),

S('Loculi e colombari', 'Loculi e colombari prefabbricati',
  'I blocchi di loculi (celle per feretri sovrapposte in file) e i colombari (celle per urne cinerarie) sono la risposta alla scarsita\u0300 di suolo: sistemi prefabbricati in calcestruzzo armato, modulari e impilabili, con telai portanti o a scatola, tamponati e finiti. Il progetto riguarda statica (sovrapposizione fino a 4-6 file), areazione delle celle, chiusura e sigillatura, accessibilita\u0300 alle file alte e durabilita\u0300: un blocco di loculi lavora per decenni con concessioni pluridecennali.',
  'Sistemi prefabbricati: moduli in c.a. vibrato con pareti e divisori, fondazione a platea o cordoli continui, file da 4 a 6 con scale di accesso o piattaforme; celle con areazione verso l\u2019esterno e chiusura a tenuta con lastra e sigillo; finiture in marmo/granito o pannelli; colombari con celle 40x40x60 cm circa; verifica sismica come struttura non convenzionale: masse in sommita\u0300 (feretri e lapidi) e collegamenti tra moduli.',
  'Blocchi di loculi in ampliamenti, colombari per ceneri, sopraelevazioni di blocchi esistenti (con verifica statica), rivestimenti e rifacimenti di facciate cimiteriali.',
  'Prefabbricazione = velocita\u0300, qualita\u0300 controllata, costo per posto prevedibile; flessibilita\u0300 a lotti (si costruisce quello che vende); durabilita\u0300 elevata con c.a. di qualita\u0300.',
  'Patologie note: cedimenti differenziali, fessurazioni, degrado dei copriferri, problemi di tenuta e odori se l\u2019areazione e\u0300 sbagliata; la statica delle sopraelevazioni su blocchi esistenti e\u0300 spesso critica; impatto visivo da mitigare.',
  'Ordini di grandezza indicativi: blocco prefabbricato finito 500-1.100 €/loculo (struttura e chiusura esclusi marmi pregiati); colombario 250-600 €/cella cineraria; platea e opere esterne a parte.',
  'Caso tipo: ampliamento con 1.200 loculi in blocchi a 5 file su platea unica; i moduli arrivano a lotti di 200 seguendo le concessioni vendute; accesso alle file alte con passerella fissa antisdrucciolo.',
  'DPR 285/1990 (requisiti igienici delle celle, verificare); NTC D.M. 17/1/2018 (verifiche statiche e sismiche); regolamenti comunali per durata concessioni (da verificare, tipicamente 25-99 anni).',
  'Pretendi i certificati di produzione del prefabbricato e controlla l\u2019areazione delle celle prima della consegna: una cella non areata e\u0300 un problema sanitario e un contenzioso certo. E mai sopraelevare senza indagine statica sul blocco esistente.'),

S('Tombe private', 'Tombe private, cappelle gentilizie ed edicole',
  'Le tombe private e le cappelle gentilizie sono piccole costruzioni a tutti gli effetti: fondazioni, elevazioni, coperture, finiture lapidee, serramenti. Ricadono nel perimetro cimiteriale con concessione di area e vincoli di regolamento (altezze, materiali, arretramenti), ma la responsabilita\u0300 statica e di manutenzione resta del concessionario: il comune deve verificare i progetti e lo stato di conservazione.',
  'Strutture in muratura armata, c.a. o miste con fondazioni su terreno dei campi privati; rivestimenti lapidei ancorati (tasselli, staffe, non solo colla); coperture piane o a falda con impermeabilizzazione; interazione con le reti e i drenaggi dei campi; dimensioni secondo lotti concessi; verifica statica richiesta dal regolamento oltre certe dimensioni.',
  'Cappelle gentilizie di famiglia, edicole funerarie, tombe private plurime, ristrutturazioni di sepolture storiche con vincoli.',
  'Domanda stabile e margini di costruzione interessanti; possibilita\u0300 di qualita\u0300 architettonica; i lotti privati finanziano la gestione del cimitero.',
  'Responsabilita\u0300 frammentata: il degrado di una cappella privata e\u0300 rischio per tutti (caduta lapidi, instabilita\u0300); regolamenti permissivi del passato hanno prodotto mostri statici; manutenzione a carico del concessionario spesso disattesa.',
  'Ordini di grandezza indicativi: cappella gentilizia 15-30 m2: 60-180 k€ chiavi in mano; edicola semplice 15-50 k€; rivestimento lapideo con ancoraggio meccanico 300-800 €/m2.',
  'Caso tipo: campagna di verifica su cappelle anni \u201960: un terzo presenta distacchi di lastre con sola colla; il comune impone ripristino con ancoraggi meccanici entro 12 mesi, con schede di censimento per ogni concessione.',
  'Regolamenti comunali cimiteriali (vincoli e verifiche, da verificare); NTC D.M. 17/1/2018 per le verifiche statiche; normativa su ancoraggio dei rivestimenti lapidei (buone pratiche e linee guida, da verificare).',
  'In ogni rivestimento lapideo nuovo o rifatto esigi ancoraggio meccanico documentato: la lastra incollata cade, e quando cade fa danni seri. Verbalizza lo stato esistente prima dei lavori vicini.'),

S('Ossari e ceneri', 'Ossari, cinerari e gestione delle esumazioni',
  'Il ciclo cimiteriale si chiude con le esumazioni: a fine periodo le salme non mineralizzate vanno all\u2019ossario comune, le ossa raccolte in ossari individuali o comuni, e le ceneri in cinerari/columbari. La normativa sulla cremazione e sulla destinazione delle ceneri ha profondamente cambiato la domanda: i nuovi impianti devono prevedere aree cinerarie, giardini di dispersione e spazi per la tumulazione delle urne.',
  'Ossari comuni in calcestruzzo interrati o fuori terra con accessi controllati; cinerari con celle per urne (dimensioni standard delle urne circa 25x25x35 cm — verificare regolamenti); giardini di dispersione delle ceneri con aree dedicate e registrazione; procedure di esumazione con personale formato, attrezzature dedicate e protocolli igienici; registro informatizzato collegato all\u2019anagrafe cimiteriale.',
  'Ossari e cinerari di nuova realizzazione, ampliamenti per crescita della cremazione (in molte aree oltre la meta\u0300 delle scelte), riordino di ossari storici saturi, giardini di dispersione.',
  'Risposta alla crescita della domanda di cremazione; costi di gestione bassi rispetto ai loculi; i giardini di dispersione richiedono poco consumo di suolo.',
  'La crescita delle ceneri rende obsoleti i piani cimiteriali tarati sulle sepolture; gli ossari storici sono spesso saturi e fuori norma igienica; la dispersione richiede regolamento e gestione attenta (registro, aree dedicate).',
  'Ordini di grandezza indicativi: cinerario prefabbricato 250-600 €/cella; ossario comune interrato 40-100 k€ secondo capacita\u0300; giardino di dispersione con percorso e verde 30-80 k€.',
  'Caso tipo: comune con cremazioni oltre il 60% che riconverte un campo storico saturo in giardino cinerario con columbario centrale e area dispersione: capacita\u0300 trentennale senza nuovo consumo di suolo.',
  'DPR 285/1990 (esumazioni, ossari); L. 130/2001 (cremazione e destinazione delle ceneri); leggi regionali e regolamenti comunali (dispersione, da verificare).',
  'La dispersione ceneri senza registro e aree dedicate e\u0300 un problema giuridico e di decoro: prevedi sempre la tracciabilita\u0300. E forma il personale delle esumazioni: e\u0300 il momento piu\u0300 delicato di tutta la gestione.'),

S('Forni crematori', 'Forni crematori: tecnologia, emissioni e inserimento',
  'Il forno crematorio e\u0300 l\u2019impianto tecnologicamente piu\u0300 complesso del sistema cimiteriale: camera di combustione a ~800-1.000 \u00b0C, post-combustione, sistema di abbattimento fumi (filtrazione, adsorbimento), gestione dei residui e controllo continuo delle emissioni. Richiede autorizzazioni ambientali e sanitarie, un bacino di utenza che giustifichi l\u2019investimento e un inserimento architettonico e paesaggistico delicato.',
  'Impianto: camera primaria e secondaria di post-combustione (850 \u00b0C minimo con tempi di permanenza definiti), bruciatori a gas metano o GPL, linea fumi con scambiatore, filtro a maniche, adsorbimento a carboni attivi e calce idrata, camino con monitoraggio continuo (polveri, CO, TOC, HCl, SO2, NOx, HF, metalli, diossine secondo limiti di legge); parte edilizia: sala commiato, sala di consegna, area tecnica, spogliatoi; bacino di dimensionamento: 1 linea per ~3.000-4.000 cremazioni/anno potenziali.',
  'Nuovi impianti crematori comunali o intercomunali, ammodernamento di forni esistenti con adeguamento emissivo, integrazione con sale del commiato e servizi.',
  'Risponde alla crescita strutturale della cremazione; economia di scala intercomunale; gli impianti moderni hanno emissioni controllate e monitorate.',
  'Investimento elevato e gestione tecnica specializzata (personale formato, manutenzione, controlli); iter autorizzativo ambientale e sanitario lungo; opposizione locale frequente (NIMBY) da gestire con comunicazione e monitoraggi pubblici.',
  'Ordini di grandezza indicativi: forno a 1 linea con edificio e sala commiato 2,5-5 M€; adeguamento emissivo di forno esistente 300-800 k€; costi di esercizio per cremazione 150-400 €.',
  'Caso tipo: consorzio di 12 comuni che realizza un impianto a due linee con sala del commiato affacciata sul parco; il monitoraggio emissivo continuo e\u0300 pubblicato online: le opposizioni iniziali si spengono in due anni.',
  'DPR 285/1990 e L. 130/2001 (cremazione); D.Lgs 152/2006 (emissioni in atmosfera, limiti specifici per crematori secondo testo vigente — da verificare); autorizzazione ambientale e sanitaria regionale; normativa antincendio per gli impianti a gas.',
  'Il camino con monitoraggio continuo non e\u0300 un optional: prevedi da subito pubblicazione dei dati e contratto di manutenzione full-service col costruttore. Un forno fermo per guasto blocca un servizio essenziale.'),

S('Impianti e servizi', 'Impianti e servizi: acqua, scarichi, luce, obitorio',
  'Il cimitero ha una dotazione impiantistica specifica: rete idrica con fontanelle distribuite per i fiori e l\u2019irrigazione del verde, scarichi separati, illuminazione funzionale e di sicurezza, obitorio con celle mortuarie e camere ardenti, laboratorio marmisti con aspirazione polveri, videosorveglianza e controllo accessi. Sono impianti semplici ma con vincoli igienici e di decoro che li distinguono da un parco.',
  'Rete idrica con rubinetterie antivandaliche e pozzetti; scarichi con separazione acque meteoriche e di lavaggio; obitorio: celle frigorifere positive, sala tanatoestetica, camere ardenti con arredi dedicati; laboratorio marmisti: aspirazione localizzata delle polveri di marmo (silice cristallina), compressori, lavelli; illuminazione a LED con fotocellule e telegestione; gruppo elettrogeno per celle e servizi essenziali.',
  'Dotazioni di nuovi cimiteri, ammodernamento igienico di obitori esistenti, adeguamento dei laboratori marmisti alla normativa su polveri, efficientamento illuminazione.',
  'Impianti semplici e robusti = bassa manutenzione; obitorio a norma migliora il servizio e la dignita\u0300; aspirazione polveri tutela gli operatori.',
  'Le fontanelle e i pozzetti soffrono gelo e vandalismo: servono materiali e dettagli robusti; gli obitori esistenti sono spesso sotto standard e richiedono opere murarie oltre che impianti; la gestione idrica invernale (svuotamento reti) e\u0300 un costo ricorrente.',
  'Ordini di grandezza indicativi: rete idrica con fontanelle 15-30 €/m lineare; obitorio con 6-12 celle e camere ardenti 250-600 k€; laboratorio marmisti con aspirazione 60-150 k€.',
  'Caso tipo: adeguamento di un obitorio anni \u201970: nuove celle modulari, sala del commiato ridisegnata, aspirazione del laboratorio marmisti e svuotamento automatico invernale della rete idrica.',
  'DPR 285/1990 (requisiti obitorio); D.Lgs 81/2008 (polveri di silice cristallina, laboratori); norme CEI per gli impianti elettrici; D.Lgs 152/2006 per gli scarichi.',
  'Progetta la rete idrica per lo svuotamento invernale rapido (pendenze e valvole di scarico in basso): la gelata di gennaio che spacca le fontanelle e\u0300 il guasto classico. E separa davvero i flussi dell\u2019obitorio: publico e operatori non devono incrociarsi.'),

S('Sicurezza e manutenzione', 'Sicurezza statica e manutenzione programmata',
  'I cimiteri concentrano rischi statici spesso sottovalutati: blocchi di loculi vetusti, cappelle private con rivestimenti pericolanti, muri di sostegno, alberi ad alto fusto vicino alle strutture. I crolli di loculi avvenuti in Italia hanno imposto campagne di verifica: il gestore deve censire, verificare e manutenere, con piani pluriennali e responsabilita\u0300 chiare tra comune e concessionari.',
  'Censimento strutturale: schede per blocco/cappella con stato di conservazione, vincoli e criticita\u0300; verifiche statiche su strutture sospette (NTC: azioni, sisma, durabilita\u0300); monitoraggio di lesioni e distacchi; piano di messa in sicurezza con priorita\u0300 (puntellamenti, reti di contenimento, chiusure temporanee); manutenzione programmata di coperture, giunti, impermeabilizzazioni e ancoraggi lapidei; gestione del verde con valutazione di stabilita\u0300 degli alberi.',
  'Campagne di verifica dopo eventi (sisma, maltempo), piani di manutenzione pluriennali, messa in sicurezza di blocchi fatiscenti, verifiche pre-sopraelevazione.',
  'Il censimento previene gli eventi improvvisi e il contenzioso; la manutenzione programmata costa una frazione dell\u2019emergenza; le priorita\u0300 oggettive rendono spendibili i bilanci.',
  'Il patrimonio cimiteriale e\u0300 frammentato (migliaia di concessionari) e vetusto: i costi di messa in sicurezza superano spesso i bilanci; le chiusure per pericolo creano pressione sociale; manca spesso personale tecnico interno.',
  'Ordini di grandezza indicativi: censimento con schede 5-20 €/struttura; verifica statica su blocco di loculi 3-10 k€; puntellamento e messa in sicurezza provvisoria 200-600 €/m lineare di fronte; piano manutentivo quinquennale 10-40 k€ di redazione.',
  'Caso tipo: dopo un cedimento parziale di un blocco anni \u201960, il comune censice tutte le strutture, chiude un\u2019ala e finanzia il ripristino con le somme delle nuove concessioni; il registro dei controlli diventa annuale.',
  'NTC D.M. 17/1/2018 (verifiche); D.Lgs 81/2008 (lavori in cimitero, scavi e fosse); normativa regionale cimiteriale su controlli (da verificare); responsabilita\u0300 del custode e del proprietario (c.c.).',
  'Fai un giro con gli occhi del perito, non del gestore: distacchi di lastre, lesioni ai cordoli, alberi radicati nei giunti. Fotografa, verbalizza, dai priorita\u0300: il primo che segnala per iscritto si tutela; l\u2019ultimo che interviene paga.'),

S('Accessibilità e paesaggio', 'Accessibilità, accoglienza e progetto del paesaggio',
  'Il cimitero e\u0300 un luogo pubblico di prossimita\u0300 quotidiana: deve essere accessibile a anziani e disabili (D.M. 236/1989), leggibile nei percorsi, dotato di sedute e ombra, e inserito nel paesaggio con cura: recinzioni mitigate, verde strutturale, gestione delle visuali. La qualita\u0300 dello spazio non e\u0300 decoro accessorio: e\u0300 la misura del rispetto verso chi lo frequenta.',
  'Accessibilita\u0300: percorsi senza barriere tra ingresso, campi e servizi, rampe con pendenze a norma, accesso alle file alte dei loculi con mezzi idonei (piattaforme, passerelle), servizi igienici accessibili; paesaggio: alberature di pompaggio ombra, siepi di mitigazione perimetrali, pavimentazioni drenanti, panchine e punti di sosta, segnaletica leggibile; gestione dei picchi con percorsi temporanei.',
  'Adeguamenti di accessibilita\u0300 in cimiteri esistenti, progetto paesaggistico di nuovi ampliamenti, mitigazione di recinzioni e volumi tecnici, sistemazione delle aree di accoglienza.',
  'Accessibilita\u0300 vera allarga l\u2019utenza e riduce i reclami; il verde ben progettato migliora microclima e percezione; i costi sono modesti rispetto al beneficio collettivo.',
  'I cimiteri storici in pendenza rendono l\u2019adeguamento costoso (rampe, percorsi alternativi); il verde vicino alle strutture va gestito (radici e cadute); la manutenzione del paesaggio e\u0300 un costo ricorrente spesso tagliato.',
  'Ordini di grandezza indicativi: adeguamento accessibile di un asse principale 30-80 k€; piantumazione e sistemi di ombra 15-40 €/m2; pavimentazioni drenanti pedonali 40-90 €/m2.',
  'Caso tipo: ampliamento con percorso anulare accessibile, panchine ombreggiate ogni 40 m e fontane lungo il giro; nei giorni di punta la navetta elettrica collega parcheggi e campi alti.',
  'D.M. 236/1989 (accessibilita\u0300); D.Lgs 42/2004 (vincoli paesaggistici ove presenti); regolamenti comunali del verde; DPR 285/1990 per i requisiti generali.',
  'Prova il percorso con una persona anziana vera prima di consegnare: la rampa a norma che nessuno riesce a fare perche\u0300 troppo lunga senza soste e\u0300 conforme e inutile. Panchine e ombra non sono un extra: sono il progetto.'),

S('Economia e gestione', 'Economia e gestione: concessioni, costi e investimenti',
  'Il cimitero si autofinanzia in parte con le concessioni (loculi, tombe private, cinerari) e in parte con il bilancio comunale: la tariffa della concessione dovrebbe coprire costruzione, manutenzione del periodo concesso e quota di gestione. Il progettista deve conoscere questa economia: il dimensionamento dei lotti segue la vendita delle concessioni, e gli investimenti (forni, blocchi nuovi) si ripagano con la domanda reale.',
  'Conto economico: tariffa concessione loculo (25-99 anni secondo regolamenti) da confrontare con costo di costruzione 500-1.100 €/loculo piu\u0300 manutenzione e gestione; canoni e servizi accessori (esumazioni, tumulazioni, servizi funebri); investimenti a lotti seguendo l\u2019assorbimento; gestione diretta, in house o concessione a terzi con capitolato; PPP per forni crematori e grandi ampliamenti.',
  'Piani economici cimiteriali, determinazione delle tariffe di concessione, valutazione di nuovi lotti e forni, affidamenti in concessione con capitolato di manutenzione.',
  'Il lotto progressivo allinea investimento e domanda; tariffe ben costruite finanziano la manutenzione senza aggravi sul bilancio; i forni intercomunali hanno economie di scala.',
  'Tariffe storicamente basse creano deficit di manutenzione che esplodono dopo decenni; la domanda varia rapidamente (cremazioni) e sballa i piani; le concessioni a terzi senza capitolato manutentivo generano contenziosi.',
  'Ordini di grandezza indicativi: concessione loculo comunale 800-3.000 € per 30-50 anni (fortemente variabile per comune); tariffa cremazione 200-600 €; piano economico cimiteriale con tariffario 10-30 k€.',
  'Caso tipo: revisione del tariffario dopo 20 anni: la nuova tariffa loculi copre costruzione del lotto successivo e fondo manutenzione; le concessioni vendute finanziano il colombario senza mutuo.',
  'Regolamenti comunali cimiteriali e tariffari (da verificare); D.Lgs 36/2023 (concessioni, ove applicabili); normativa sui servizi pubblici locali per la gestione.',
  'Quando dimensioni un lotto, chiedi il dato vero di assorbimento (loculi venduti/anno) e scrivi nel progetto che le tariffe devono coprire anche la manutenzione: il blocco costruito sotto costo e\u0300 un debito dilazionato.'),
]

def main():
    os.makedirs(os.path.join(ROOT, 'schede'), exist_ok=True)
    with open(os.path.join(ROOT, 'schede', 'schede.jsonl'), 'w', encoding='utf-8', newline='\n') as f:
        for d in SCHEDE:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

    course = f'''corso: "Edilizia cimiteriale: quadro normativo e piani cimiteriali (DPR 285/1990, distanze), vincolo idrogeologico e scelta del sito, organizzazione funzionale e flussi, sepolture in terra e campi comuni, loculi e colombari prefabbricati, tombe private e cappelle gentilizie, ossari cinerari e dispersione ceneri (L. 130/2001), forni crematori (emissioni, autorizzazioni), impianti e servizi (obitorio, laboratorio marmisti), sicurezza statica e manutenzione programmata, accessibilita' e paesaggio, economia e gestione (concessioni, tariffe)"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L1-L2"
schede: {len(SCHEDE)}
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "DPR 285/1990 (Regolamento di Polizia Mortuaria), L. 130/2001 (cremazione e ceneri), D.Lgs 152/2006 (acque, terre, emissioni), NTC D.M. 17/1/2018, D.M. 236/1989 (accessibilita'), D.Lgs 81/2008 (sicurezza, silice), D.Lgs 42/2004 (paesaggio), DPR 380/2001 (titoli), D.Lgs 36/2023 (concessioni); leggi regionali e regolamenti comunali citati come da verificare"
nota_metodologica: "Corso tipologico sull'edilizia cimiteriale: pianificazione (piani cimiteriali, distanze dai centri abitati, autorizzazioni sanitarie), sito (falda, geologia, piezometri), organizzazione (campi, servizi, flussi e picchi), sepolture in terra (drenaggi, rotazione, esumazioni), loculi e colombari prefabbricati (statica, areazione, concessioni), tombe private (ancoraggio lapidei, responsabilita'), ossari e cinerari (L. 130/2001, dispersione), forni crematori (post-combustione, emissioni, bacino), impianti (obitorio, fontanelle, laboratorio marmisti), sicurezza e manutenzione (censimenti, crolli noti, priorita'), accessibilita' e paesaggio, economia (concessioni, tariffe, lotti). NON ridondante: nessun pack esistente tratta la tipologia cimiteriale (grep su titoli: solo Colosseo storico). Norme: solo DPR 285/1990, L. 130/2001, D.Lgs 152/2006, NTC e le altre di consolidata certezza; distanze e franchi con invito alla verifica del testo vigente; prezzi come fasce indicative; nessun nome di azienda."
'''
    with open(os.path.join(ROOT, 'COURSE.yaml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(course)

    readme = f'''# Edilizia cimiteriale

Corso L1-L2 della Facolta di Tecnologia e Costruzione: il cimitero come tipologia edilizia e impiantistica completa — quadro normativo e piani cimiteriali (DPR 285/1990 Regolamento di Polizia Mortuaria, distanze, autorizzazioni sanitarie), vincolo idrogeologico e scelta del sito (falda, piezometri, permeabilita'), organizzazione funzionale (campi, servizi, flussi e picchi della commemorazione), sepolture in terra e campi comuni (drenaggio, rotazione, esumazioni), loculi e colombari prefabbricati (statica, areazione delle celle, concessioni), tombe private e cappelle gentilizie (ancoraggio dei lapidei, responsabilita'), ossari, cinerari e dispersione delle ceneri (L. 130/2001), forni crematori (post-combustione, emissioni, bacino di utenza), impianti e servizi (obitorio, rete idrica, laboratorio marmisti), sicurezza statica e manutenzione programmata (censimenti, priorita'), accessibilita' e progetto del paesaggio, economia e gestione (concessioni, tariffe, investimenti a lotti).

**Schede: {len(SCHEDE)}**

Non ridondante: nessun pack esistente tratta la tipologia cimiteriale. I riferimenti a distanze, franchi di falda e durate concessorie riportano gli orientamenti consolidati con invito alla verifica del testo vigente e dei regolamenti comunali.
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
