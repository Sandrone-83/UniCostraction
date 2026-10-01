# -*- coding: utf-8 -*-
"""Giro K: 3 corsi nuovi — Ferrovie e stazioni, Rinnovabili idro-biomasse-geotermia,
Carpenteria metallica. Contenuti classici verificabili; nessuna norma inventata."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

KEYS = ["categoria", "nome", "descrizione", "tecnologia", "applicazioni", "vantaggi",
        "limiti", "costi_e_economia", "casi_real_world", "normative", "note_cantiere"]

def write_pack(dirname, corso, facolta, livello, descrizione_yaml, readme, schede):
    p = os.path.join(ROOT, dirname)
    os.makedirs(os.path.join(p, "schede"), exist_ok=True)
    assert all(list(s.keys()) == KEYS for s in schede)
    with open(os.path.join(p, "schede", "schede.jsonl"), "w", encoding="utf-8") as f:
        for s in schede:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    with open(os.path.join(p, "COURSE.yaml"), "w", encoding="utf-8") as f:
        f.write(f'corso: "{corso}"\nfacolta: "{facolta}"\nschede: {len(schede)}\n'
                f'livello: "{livello}"\ndescrizione: "{descrizione_yaml}"\nformato: "JSONL/MD"\nlingua: "it"\n')
    with open(os.path.join(p, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    print(dirname, len(schede), "schede")

# =====================================================================
# PACK 1 — FERROVIE E STAZIONI
# =====================================================================
ferrovie = [
dict(categoria="Armamento tradizionale", nome="Armamento ferroviario con massicciata",
 descrizione="Sistema rotaia-traversina-massicciata (ballasted track) della rete ferroviaria convenzionale.",
 tecnologia="Rotaia Vignoles tipo 60E1 (UIC60) e 60E2 da 60 kg/m; traverse in legno (2,60 m, classe portanza) o in cemento armato precompresso (2,40-2,60 m, 240-300 kg); massicciata in pietrisco di gneiss/basalto granulometria 31,5-63 mm, spessore sotto la battuta della traversina 25-30 cm; lastrico in pietrisco o sabbia; dispositivi di fissaggio (clip elastiche, pattini, bulloni); controbinario per soppressione del controrottaio nelle curve fino a una soglia di raggio.",
 applicazioni="Linee convenzionali, linee ad alta velocità in superficie, fasci di stazione e ricoveri.",
 vantaggi="Smorzamento delle vibrazioni, facile regolazione della quota del binario con spintarola, drenaggio naturale, manutenzione possibile con mezzi semplici.",
 limiti="Richiede rinnovo periodico della massicciata (fresatura, sostituzione pietrisco), sedimentazione differenziale, limitazione di velocità in curva, volume e peso maggiori rispetto al ballastless.",
 costi_e_economia="Ordini di grandezza indicativi: rinnovo completo armamento 300-600 €/m di binario; massicciata fresata/integrata 20-50 €/m.",
 casi_real_world="Rete RFI: binario semplice su linee secondarie, binari paralleli su direttrici; armamento 60E1 diffusissimo anche in gallerie corte.",
 normative="Norme tecniche RFI (Manuale dell'armamento, norme tecniche per l'armamento ferroviario); prescrizioni UIC per rotaie e traverse.",
 note_cantiere="Il rilascio e il ripristino dell'armamento avvengono solo con occupazione binari concordata con l'esercente; la continuità del traffico impone finestre di lavoro notturne."),

dict(categoria="Armamento avanzato", nome="Armamento senza massicciata (slab track)",
 descrizione="Sopraelevato continuo in cls su cui sono ancorate rotaie o traverse bloccate, senza pietrisco.",
 tecnologia="Sistemi prefabbricati (Rheda 2000, Max Bögl, Getrac) con traverse in cls annegate in getto; sistemi gettati in opera (ipsometrici con guida formale); colatoio in cls C30/37 o superiore posato su strato portante regolarizzato (spesso invert con funzione di stagna); tirafondi tipo W14/Vossloh avvitati nella struttura.",
 applicazioni="Alta velocità, gallerie, viadotti e ponti (riduzione dei carichi), metropolitane e stazioni sotterranee.",
 vantaggi="Stabilità dimensionale e geometrica nel tempo, manutenzione quasi nulla sulla geometria del binario, vita utile 50-60 anni, adatto a basi cedevoli e a ponti.",
 limiti="Costo iniziale elevato, riparazioni locali complesse, richiede fondazione di precisione e controllo stretto della planarità.",
 costi_e_economia="Ordini di grandezza indicativi: 2-4 volte il costo dell'armamento con massicciata; convenienza sul ciclo di vita per traffico pesante o >250 km/h.",
 casi_real_world="Direttrici AV italiane (Torino-Milano, Milano-Bologna, Bologna-Firenze, Roma-Napoli) in galleria e su viadotto; metropolitane di Milano, Torino, Brescia.",
 normative="Specifiche RFI per armamento a struttura continua; norme UIC per rotaie e componenti di fissaggio.",
 note_cantiere="Nelle gallerie il posamento slab track precede l'ultima fase degli impianti (aerazione, SCADA); i giunti tra campate richiedono dettagli anti-ribaltamento."),

dict(categoria="Manutenzione linea", nome="Manutenzione dell'armamento",
 descrizione="Preservazione della geometria del binario e rinnovo programmato degli elementi usurabili.",
 tecnologia="Interventi di levigatura e rettifica del profilo della rotaia (grinding train), rinnovo traversine su macchina operatrice, spurgo e integrazione massicciata (fresatura, sostituzione selettiva), tecnopolimero per fissaggi, controllo geometrico con mezzi diagnostici (carrello di registrazione, laser scanner, veicolo per prove non distruttive delle rotaie USU).",
 applicazioni="Tutta la rete ferroviaria in esercizio, con programmi pluriennali di rinnovo.",
 vantaggi="Previene il degrado accelerato, riduce il rumore, mantiene i parametri di qualità di marcia, posticipa i rinnovi integrali.",
 limiti="Interferisce con l'esercizio (occupazione binari), richiede mezzi dedicati costosi, scarti di rotaia e traversine da smaltire come rifiuti.",
 costi_e_economia="Ordini di grandezza indicativi: rettifica profili 10-30 €/m di binario; rinnovo traversine su macchina 15-40 €/m; costo annuo di manutenzione ordinaria 10-30 k€/km a seconda del traffico.",
 casi_real_world="Programmi pluriennali RFI di rinnovo armamento e rettifica sulle direttrici di collegamento; veicoli diagnostici per la registrazione della geometria del binario.",
 normative="Norme tecniche RFI per manutenzione e accettazione degli interventi; standard UIC per le rotaie e i profili di usura.",
 note_cantiere="Ogni intervento vicino al binario richiede protezioni di cantiere e coordinamento con la centrale operativa; i sagristi operano con divieto di avvicinamento mezzi."),

dict(categoria="Segnalamento", nome="Segnalamento ferroviario: ETCS/ERTMS e SCMT",
 descrizione="Sistemi di controllo e protezione automatica della marcia dei treni e distanziamento.",
 tecnologia="SCMT (Sistema Controllo Marcia Treno) sovrapposto alla tradizionale protezione automatica a max quattro codici, con ripetizione segnali in cabina; ETCS Livello 1 (puntiforme) e Livello 2 (radio, segnalazione solo in cabina) su rete dati radio GSM-R in migrazione verso FRMCS; gestione comandi da centrale di comando; sistemi silenziosi per circolazione simultanea AV/DC.",
 applicazioni="Tutta la rete RFI, con ETCS L2 in espansione sulle direttrici AV e merci; interoperabilità transfrontaliera europea.",
 vantaggi="Aumento della capacità di linea, standardizzazione europea (ERTMS), riduzione dei segnali di linea e dei cavidotti, diagnostica avanzata.",
 limiti="Investimenti su bordo e terra, complessità della migrazione dai sistemi nazionali, necessità di equipaggiare il parco rotabili.",
 costi_e_economia="Ordini di grandezza indicativi: impiantistica di segnalamento e TLC 1-4 M€/km sulle linee AV; upgrade radio e centri di comando a contratto quadro.",
 casi_real_world="Direttrici AV italiane con ETCS L2; piano di estensione ETCS sulla rete convenzionale avviato con bandi RFI; interoperabilità Brennero con Austria/Germania.",
 normative="Regolamento (CE) n. 352/2009 (CSM — gestione sicurezza comune applicata al sistema); D.Lgs 264/2008 (sicurezza ferroviaria); specifiche tecniche di interoperabilità (TSI); serie UNI EN 50126/50128/50129 (RAMS, software, sistemi di sicurezza).",
 note_cantiere="Lavori su segnalamento e TLC in prossimità della linea richiedono piani di sicurezza condivisi con l'esercente e distacchi di linea documentati."),

dict(categoria="Elettrificazione", nome="Elettrificazione ferroviaria: 3 kV DC e 25 kV AC",
 descrizione="Sistemi di alimentazione elettrica dei treni sulla rete italiana e sulle linee AV.",
 tecnologia="Rete convenzionale a corrente continua 3 kV con sottostazioni elettriche a 50 km circa e sezionamenti ogni 2-4 km; linee AV a corrente alternata 25 kV 50 Hz con sottostazioni ognitempo (BT/MT) e autotrasformatori in parallelo; catenaria composta da filo di contatto (Cu-Ag 120-150 mm²), messaggero, pendini, stralli di ancoraggio; caditoie di alimentazione e parascintille; ricircolo e dispersione controllata.",
 applicazioni="Linee convenzionali elettrificate, direttrici AV, raccordi industriali e portuali elettrificati.",
 vantaggi="Trazione elettrica efficiente, nessuna emissione locale, potenze elevate disponibili per treni merci pesanti.",
 limiti="Interferenze indotte su reti metalliche vicine, necessità di coordinamento con reti di distribuzione, limiti di sagoma in galleria per la catenaria.",
 costi_e_economia="Ordini di grandezza indicativi: elettrificazione ex novo 1-2 M€/km; rifacimento catenaria su viadotto/galleria molto superiore al tratto in superficie.",
 casi_real_world="Sistema misto italiano: 3 kV DC su convenzionale, 25 kV AC sulle AV; collegamenti con reti estere a sistemi diversi con sistemi di trazione multisistema.",
 normative="Norme tecniche RFI per impianti elettrici e di segnalamento; regolamenti CEI per installazioni elettriche; accordi di interfaccia con i gestori di rete (Terna, distributori).",
 note_cantiere="Vicino alla catenaria vigono distanze di sicurezza che impongono lavori sotto distacco elettrico, messa a terra e verbale di messa in sicurezza."),

dict(categoria="Opere sotterranee", nome="Gallerie ferroviarie",
 descrizione="Costruzione e adeguamento delle gallerie ferroviarie, dal raddoppio sezionale alla nuova linea.",
 tecnologia="Scavo meccanizzato in piena sezione con TBM a doppio scudo o EPB per gallerie lunghe; tradizionale ad avanzamento ridotto o ciclo completo su tratti brevi; rivestimento in cls con falsa volta, spallette, spalla di galleria e pavimentazione con cordolo; dispositivi di sicurezza (piazzole di sfogo, fontane antincendio, sistemi SCADA, illuminazione di emergenza, ventilazione forzata nelle gallerie superiori a 1 km).",
 applicazioni="Attraversamenti appenninici e alpini, direttrici AV, raddoppi e ammodernamenti della rete convenzionale.",
 vantaggi="Pendenze contenute e tracciato rettilineo, indipendenza dal fondo superficiale, riduzione impatto paesaggistico rispetto al tracciato in superficie.",
 limiti="Investimenti elevati (decenni di progettazione e costruzione), gestione della sicurezza in esercizio, interferenze con reti idriche e sismicità.",
 costi_e_galleria="",
 costi_e_economia="Ordini di grandezza indicativi: costruzione in galleria 30-80 M€/km a seconda di lunghezza, geologia e sistemi; adeguamento di galleria esistente 5-20 M€/km.",
 casi_real_world="Trafori storici ammodernati (Giovi, Frejus per il trasporto combinato) e grandi gallerie AV degli anni 2000-2010; gallerie base del valico alpino in corso (Lyon-Torino) come riferimento europeo.",
 normative="Prescrizioni tecniche RFI per gallerie e sicurezza in esercizio; specifiche TSI 'sicurezza in galleria'; norme UNI per materiali e cls.",
 note_cantiere="In galleria il cantiere è lineare e sequenziale: previa, scavo, rivestimento, posa binario e impianti; le interferenze tra squadre impongono piani di occupazione rigidi."),

dict(categoria="Opere d'arte", nome="Viadotti e ponti ferroviari",
 descrizione="Opere di attraversamento per linee ferroviarie: viadotti continui, ponti ad arco e impalcati.",
 tecnologia="Impalcati in cls precompresso con luci 30-60 m su pile, viadotti continui in cls cassero o prefabbricato, ponti ad arco in cls o acciaio per luci >100 m, attrezzature di cantiere per varo (carrelli, lancio di impalcato); verifiche a fatica per azioni cicliche del traffico, interazione dinamica carrello-ponte, cuscinetti antisismici e apparecchi di appoggio.",
 applicazioni="Attraversamenti di valli, fiumi e infrastrutture esistenti sulle direttrici AV e convenzionali.",
 vantaggi="Superamento di ostacoli senza dislivelli, soluzioni industrializzate per la prefabbricazione, qualità controllata.",
 limiti="Sensibilità alle cedimenti differenziali delle fondazioni, manutenzione di apparecchi di appoggio e giunti, vinci paesaggistici sui grandi luci.",
 costi_e_economia="Ordini di grandezza indicativi: viadotto ferroviario in cls 5-15 M€/km equivalente; ponte ad arco o grande luce da progetto a progetto, decine di milioni.",
 casi_real_world="Viadotti delle direttrici AV (es. viadotti sulla Roma-Napoli e Milano-Bologna); ponti storici a travata metallica mantenuti in esercizio dopo consolidamento.",
 normative="Norme tecniche RFI per opere d'arte; NTC 2018 (D.M. 17/1/2018) e Eurocodici strutturali per il calcolo; verifiche a fatica secondo Eurocodice per strutture ferroviarie.",
 note_cantiere="Il varo di grandi luci sopra linee in esercizio richiede fasi provvisorie certificate, finestre di blocco traffico e monitoraggio continuo delle deformazioni."),

dict(categoria="Architetture di stazione", nome="Piattaforme, banchine e pensiline ferroviarie",
 descrizione="Elementi edilizi delle stazioni di superficie: banchine viaggiatori, pensiline e percorsi di interconnessione.",
 tecnologia="Banchina viaggiatori (piattaforma) in cls gettato o prefabbricato con altezza da quota ferro (in genere 55 cm su rete RFI, fino a 76 cm su AV) e lunghezza da 250 m (regionale) a 400 m (AV); cordolo di sicurezza a 90 cm dalla banchina interna; pensiline reticolari o a struttura di acciaio/legno con tamponamento in pannelli o membrana; illuminazione di banchina su pali o integrate; sistemi di informazione e videosorveglianza; attraversamenti pedonali a raso con cancelli di sicurezza o sottopassi e sovrappassi.",
 applicazioni="Stazioni di superficie e stazioni AV, fermate regionali, interventi di adeguamento a norma di accessibilità.",
 vantaggi="Separazione viaggiatori/treni, capacità di stazionamento elevata, standardizzazione dei componenti in prefabbricato.",
 limiti="Interventi su banchine esistenti richiedono occupazione binari, vinci di sagoma ferroviaria e distanze di sicurezza, integrazione con impiantistica esistente.",
 costi_e_economia="Ordini di grandezza indicativi: costruzione banchina prefabbricata 300-800 €/m lineare; pensilina su banchina 500-1.500 €/m²; adeguamento accessibilità di una stazione da 0,5 a 5 M€.",
 casi_real_world="Interventi di adeguamento banchine e pensiline sulle stazioni della rete regionale; banchine AV a 400 m sulle direttrici ad alta velocità.",
 normative="Requisiti RFI per interventi sulle piattaforme; normativa di accessibilità (L. 13/1989, D.Lgs 198/2021) per percorsi e servizi; regolamenti di polizia ferroviaria per l'uso dei locali.",
 note_cantiere="I getti vicino al binario avvengono con casseri a perdere o prefabbricati e trasporti meccanizzati; le banchine devono essere consegnate con profili di quota certificati."),

dict(categoria="Lavori in esercizio", nome="Interventi edilizi in stazione e a ridosso dei binari",
 descrizione="Criteri per costruire o ristrutturare edifici di stazione mentre la circolazione continua.",
 tecnologia="Reparti di stazione coordinati dall'esercente (RFI) con piani di occupazione binari e distacchi impianti; barriere di protezione (cancelli di sicurezza, transenne certificate) ai margini della sagoma; getti in cassero a perdere o strutture prefabbricate a monte; sollevamento tramite gru con autorizzazioni per invaso; monitoraggio delle vibrazioni e spostamenti delle opere vicine; coordinamento con gestori degli impianti (elettrificazione, segnalamento, TLC).",
 applicazioni="Riqualificazioni di stazioni, nuovi sottopassi pedonali, fabbricati viaggiatori, depositi bagagli, servizi igienici, sale d'attesa.",
 vantaggi="Continuità dell'esercizio durante i lavori, trasformazione graduale degli spazi, possibilità di interventi a lotti.",
 limiti="Finestre di lavoro brevi e notturne, molteplici enti interessati (esercente, gestori impianti, comune), adempimenti autorizzativi complessi, sicurezza del personale viaggiante.",
 costi_e_economia="Ordini di grandezza indicativi: premio di cantiere in esercizio +20-50% rispetto a cantiere libero; ciascun distacco impianti e occupazione binari ha costi gestionali non ripetibili.",
 casi_real_world="Riqualificazioni programmate delle stazioni italiane con cantieri a ridosso binari; realizzazione di sottopassi pedonali con tecnica di spinta o a cielo aperto in notturna.",
 normative="D.Lgs 81/2008 (sicurezza nei cantieri, Titolo IV per i lavori con interferenze) applicato ai cantieri ferroviari; regolamenti di esercizio RFI; autorizzazioni dell'ente proprietario per occupazioni di suolo e sagoma.",
 note_cantiere="Prima regola del cantiere ferroviario: nessuna interferenza non pianificata. Ogni attraversamento del binario è un'operazione formale con protezione e nominativi al seguito."),

dict(categoria="Grandi opere", nome="Grandi stazioni e nodi intermodali",
 descrizione="Architetture delle grandi stazioni moderne: hall, gallerie di stazione, interscambi e coperture.",
 tecnologia="Gallerie di stazione (bypass) per attraversare il nodo senza fermata; coperture in acciaio e vetro a grandi luci con tamponamento ETFE o vetrata; piattaforme sotterranee multilivello; sistemi di interscambio verticale (scale mobili, ascensori, tapis roulant); gestione degli afflussi con simulazioni pedonali; integrazione con parcheggi di interscambio, fermate metro/tram e stazioni bus.",
 applicazioni="Nodi AV nazionali e regionali, stazioni di interscambio metropolitano, terminal internazionali.",
 vantaggi="Capacità di smistamento elevata, riduzione dei tempi di interscambio, valorizzazione urbana dell'area di stazione.",
 limiti="Costi molto elevati, complessità progettuale e realizzativa, gestione del cantiere in esercizio nel nodo, manutenzione di coperture speciali.",
 costi_e_economia="Ordini di grandezza indicativi: grande stazione o nodo AV da centinaia di milioni a oltre un miliardo di euro; copertura a grandi luci 1.500-4.000 €/m².",
 casi_real_world="Napoli Afragola (progetto Zaha Hadid Architects), Bologna AV e le stazioni del passante ferroviario metropolitano di Milano come esempi di nodi AV moderni.",
 normative="Prescrizioni RFI per opere in stazione; NTC 2018 per le strutture; normativa antincendio per locali di pubblico afflusso (D.M. 7 gennaio 2023? no — antincendio edifici: DM 03/09/2021 applicativo Codice prevenzione incendi D.Lgs 139/2006; prudent: 'Codice prevenzione incendi e DM applicativi').",
 note_cantiere="Nelle stazioni in esercizio i cantieri sono a lotti con mantenimento dei flussi viaggiatori; la progettazione degli interventi segue le simulazioni pedonali di evacuazione e interscambio."),

dict(categoria="Sicurezza del sistema", nome="Sicurezza ferroviaria: CSM, certificazione e Agenzia ERA",
 descrizione="Il quadro della sicurezza ferroviaria europea e nazionale: regole, certificazioni, indagini.",
 tecnologia="Applicazione del Regolamento (CE) n. 352/2009 sul Common Safety Method (CSM) per il risk assessment di ogni modifica significativa del sistema; certificazione di sicurezza dell'impresa ferroviaria e del gestore dell'infrastruttura; registrazione e notifica di occorrenze (reg. UE 1078/2012? prudente: regolamento sull'indagine sugli incidenti); ruolo dell'Agenzia dell'Unione Europea per le ferrovie (ERA) per l'interoperabilità; sistemi di gestione della sicurezza (SMS).",
 applicazioni="Tutti i soggetti del sistema ferroviario: gestori infrastruttura, imprese di trasporto, manutentori, progettisti e imprese appaltatrici di lavori significativi.",
 vantaggi="Uniformità europea dei livelli di sicurezza, cultura dell'analisi del rischio documentata, lezioni apprese condivise.",
 limiti="Adempimenti documentali pesanti, necessità di figure dedicate (responsabili SMS, risk assessor), scostamenti tra normativa nazionale ed europea in transizione.",
 costi_e_economia="Ordini di grandezza indicativi: la certificazione e il mantenimento del SMS incidono sull'organico amministrativo; i progetti significativi dedicano 1-5% degli oneri alla documentazione di sicurezza CSM.",
 casi_real_world="Adozione CSM nei progetti di ammodernamento della rete italiana; indagini formali sugli incidenti con rapporti pubblici dell'ANSF (Agenzia Nazionale per la Sicurezza delle Ferrovie).",
 normative="D.Lgs 264/2008 (riordino della sicurezza ferroviaria); reg. (CE) n. 352/2009 CSM; regolamento (UE) sull'indagine degli incidenti ferroviari; regolamenti TSI dell'Agenzia ERA.",
 note_cantiere="Le imprese che eseguono lavori significativi sul sistema forniscono input al risk assessment del committente: modifiche di sagoma, interferenze con segnalamento ed elettrificazione vanno sempre dichiarate."),

dict(categoria="Economia e programma", nome="Costi, contratti e programmazione dei lavori ferroviari",
 descrizione="Come si stima, appalta e programma un cantiere lineare ferroviario.",
 tecnologia="Stima per chilometro di linea con breakdown (terreni, armamento, opere d'arte, impianti, elettrificazione); contratti a corpo con prezzi unitari per interferenze e lavori in esercizio; programmi di cantiere con occupazioni binari certificate; gestione delle interferite (esercizio, terze imprese); collaudi funzionali con prove dinamiche a treno vuoto prima della riapertura.",
 applicazioni="Raddoppi, ammodernamenti, quadruplicazioni, nuove linee e bypass di stazione.",
 vantaggi="Prezzi unitari per le interferenze riducono le controversie, il programma di occupazione binari allinea cantiere ed esercizio, collaudi funzionali certificano la geometria finale.",
 limiti="Incidenza alta dei costi indiretti e delle notturne, sensibilità ai ritardi autorizzativi, rischio di varianti per interferenze non previste.",
 costi_e_economia="Ordini di grandezza indicativi: AV in superficie 10-20 M€/km, in galleria 30-80 M€/km; ammodernamento convenzionale 2-8 M€/km; premio notturno e interferenze +15-50% sul costo diretto.",
 casi_real_world="Programmi pluriennali di potenziamento della rete nazionale e regionale con cantieri in esercizio su più tratte simultanee.",
 normative="Codice dei contratti pubblici (D.Lgs 36/2023) per appalti e concessioni; norme tecniche RFI per collaudi e accettazione; disciplina delle occupazioni e distacchi secondo regolamenti dell'esercente.",
 note_cantiere="Il programma ferroviario è un contratto con l'esercente: le finestre perse vanno recuperate, e il costo di un binario bloccato supera di gran lunga il costo diretto del lavoro."),

dict(categoria="Integrazione urbana", nome="Ferrovie metropolitane e passanti urbani",
 descrizione="Le linee ferroviarie in ambito urbano: passanti, soppressioni dei passaggi a livello, cinturazioni.",
 tecnologia="Passanti ferroviari urbani in galleria o trincea coperta che attraversano il centro; soppressione dei passaggi a livello con sottopassi viari o sovrappassi, o cinturazione della linea; trincee foderate con copertura a giardino per recupero del suolo urbano; fermate metropolitane ferroviarie con banchine a 90-110 cm per varia orizzontale; dispositivi di varco (porte di banchina) nelle stazioni sotterranee senza personale.",
 applicazioni="Passanti di grandi città, cinturazioni di quartieri attraversati da linee storiche, potenziamento del servizio suburbano ferroviario.",
 vantaggi="Recupero di suolo urbano, eliminazione delle barriere di attraversamento a raso, integrazione con il trasporto metropolitano, riduzione del rumore e della frammentazione urbana.",
 limiti="Costi di mitigazione elevati, interferenze con reti urbane (idrico, fognario, elettrico, TLC), complessità dei cantieri in città densa, vincoli del costruito storico.",
 costi_e_economia="Ordini di grandezza indicativi: copertura di trincea 2-5 M€/km; sottopasso viario 1-4 M€ per attraversamento; passante urbano da centinaia di milioni a diversi miliardi.",
 casi_real_world="Passanti e cinturazioni realizzati nelle grandi città italiane e in corso su più nodi urbani; soppressioni di passaggi a livello nei programmi di sicurezza della rete.",
 normative="L. 47/1985 (disciplina dei passaggi a livello) e sue modificazioni; normativa di mitigazione acustica (DPCM 14/11/1997) per le linee; accordi di programma con i comuni interessati.",
 note_cantiere="In ambito urbano il cantiere vive per anni dentro la città: necessari pannelli fonoassorbenti, gestione dei cantieri di sito con accessi dedicati e comunicazione continua con i residenti."),
]
# rimuovo la chiave accidentale
for s in ferrovie:
    s.pop("costi_e_galleria", None)

write_pack("FERROVIE_E_STAZIONI_PACK",
 "Ferrovie e stazioni", "FACOLTA_INGEGNERIA", "L2-L3",
 "Armamento, segnalamento, elettrificazione, gallerie, ponti, stazioni, sicurezza, economia.",
 """# FERROVIE_E_STAZIONI_PACK

**Ferrovie e stazioni: tecnologia, opere edili e lavori in esercizio**

Armamento tradizionale e slab track, manutenzione, ETCS/SCMT, elettrificazione 3 kV/25 kV, gallerie, viadotti, piattaforme e pensiline, interventi in esercizio, grandi nodi, sicurezza CSM, economia e programmazione dei cantieri lineari, passanti urbani.

Schede: 12 (formato JSONL, un oggetto per riga).
""", ferrovie)

# =====================================================================
# PACK 2 — RINNOVABILI IDRO-BIOMASSA-GEOTERMIA
# =====================================================================
rinnovabili = [
dict(categoria="Mini-idro", nome="Mini-idroelettrico: schemi e turbine",
 descrizione="Produzione idroelettrica su piccola scala con turbine idrauliche adatte a portate e salti diversi.",
 tecnologia="Schemi a flusso (bacino presa, canale/gravità, centrale, scarico) o a derivazione; turbine Pelton per salti >250 m e portate modeste, Francis per salti 30-250 m, Kaplan ed eliche per bassi salti (<30 m) e portate elevate; alternatori sincroni o asincroni, rendimento complessivo 85-92%; portata minima vitale e deflussi biologici garantiti.",
 applicazioni="Torrenti e fiumi di montagna, derivazioni da acquedotti e scarichi industriali, potenze da pochi kW a 1 MW (micro <100 kW).",
 vantaggi="Fonte programmabile e flessibile, vita utile >40 anni, basso impatto visivo a scala ridotta, integrazione nelle reti rurali.",
 limiti="Dipendenza dalla portata stagionale, iter autorizzativo lungo per concessioni e vincoli ambientali, interferenze con usi irrigui e bacini.",
 costi_e_economia="Ordini di grandezza indicativi: costo impianto mini-idro 2.000-6.000 €/kW installato; produzione specifica da 1.500 a 4.500 kWh/kWp equivalente secondo salto e portata.",
 casi_real_world="Presenze diffuse di centrali storiche riammodernate nelle valli alpine; connessione di derivazioni agricole e acquedotti con concessione.",
 normative="D.Lgs 28/2011 (obiettivi FER e disciplina produzione da rinnovabili); disciplina delle acque e delle concessioni idroelettriche secondo il Testo Unico Ambiente; autorizzazione unica dove prevista.",
 note_cantiere="Prima della modifica di una derivazione occorre verificare i deflussi minimi e le interferenze con le opere di presa esistenti; la ripresa a valle va tenuta in funzione per le specie ittiche."),

dict(categoria="Accumulo idrico", nome="Pumped storage e accumulo idroelettrico",
 descrizione="Grandissime batterie idrauliche: si pompano acque verso un bacino alto per rigenerare in punta.",
 tecnologia="Due bacini a quota diversa collegati da condotta forzata; gruppo pompa-turbina reversibile (Francis reversibile o ternary set) e motore-generatore; ciclo pompaggio-turbinamento con resa 70-80%; avviamento in pochi minuti; funzioni di regolazione primaria, riserva e bilanciamento del FV/eolico.",
 applicazioni="Sistemi elettrici con forte penetrazione rinnovabile, integrazione eolico/FV di valle, servizi di rete.",
 vantaggi="Capacità di accumulo gigawattora, durata di scarica ore-giorni, vita >50 anni, unica tecnologia di accumulo stagionale.",
 limiti="Richiede siti con dislivello idoneo e autorizzazioni ambientali impegnative, efficienza di ciclo limitata, investimenti da centinaia di milioni.",
 costi_e_economia="Ordini di grandezza indicativi: 600-2.000 €/kW installato per potenza; il costo per kWh immagazzinato scende al crescere delle ore di bacino.",
 casi_real_world="Impianti di pompaggio storici in montagna riammodernati; valutazioni di nuovi bacini con dighe esistenti come riferimento europeo.",
 normative="Autorizzazioni ambientali e idroelettriche; regolamenti GSE per i servizi di flessibilità e il mercato della capacità; disciplina dighe (D.Lgs 152/2006 e norme di classifica delle dighe).",
 note_cantiere="Le dighe esistenti vanno sempre verificate per classifica e stato: un pompaggio aumenta i cicli di carico sul paramento e sulle opere di presa."),

dict(categoria="Biomasse legnose", nome="Caldaie a biomasse legnose: cippato e pellet",
 descrizione="Produzione di calore da legna in caldaie automatiche per edilizia civile, industriale e reti di calore.",
 tecnologia="Caldaie a cippato con caricamento a coclea da silos, caldaie a pellet con bruciatore a fiamma invertita o a letto, potenze 20 kW-5 MW termici; rendimento 85-95% sul PCI; canne fumarie coibentate; sistemi di caricamento stoccati giorni-settimane; pannelli di controllo con modulazione di fiamma.",
 applicazioni="Riscaldamento edifici civili grandi (condomini, scuole, uffici), produzione ACS, reti di teleriscaldamento, essiccazione industriale agricola.",
 vantaggi="Rinnovabile gestibile a comando, sostituzione del gasolio e del metano, catena corta del combustibile, incentivi (Conto Termico) su edilizia esistente.",
 limiti="Spazio per stoccaggio, manutenzione regolare dello scambiatore, qualità del combustibile decisiva, emissioni da gestire con camini idonei.",
 costi_e_economia="Ordini di grandezza indicativi: caldaia pellet 6-10 kW 4.000-9.000 € installata; centrale a cippato 200 kW 60.000-120.000 €; cippato 100-150 €/t e pellet 300-450 €/t con variazioni di mercato.",
 casi_real_world="Teleriscaldamenti a cippato nelle valli alpine e appenniniche; caldaie a pellet diffuse in edilizia residenziale centralizzata.",
 normative="Regolamenti Ecodesign per caldaie a biomassa (Reg. UE 813/2013); requisiti per emissioni locali secondo normativa regionale/ARPA; UNI EN 303-5 per caldaie a biomassa.",
 note_cantiere="La canna fumaria va dimensionata e isolata contro la condensa acida; il silos richiede vano antincendio con distanze dalle strutture e dalle reti."),

dict(categoria="Qualità combustibile", nome="Pellet, cippato e certificazione dei combustibili legnosi",
 descrizione="Classi di qualità del combustibile legnoso: il rendimento di una caldaia nasce dal legno.",
 tecnologia="Classificazione del pellet secondo UNI EN ISO 17225-2 (ex UNI EN 14961-2) in classi A1, A2 e B con parametri su ceneri (<0,5-1,2%), potere calorifico (16-19 MJ/kg), umidità (<10%), fini e additivi; cippato classificato per funzione (UNI EN ISO 17225-1); certificazioni di filiera (ENplus per pellet, certificazioni per cippato) che tracciano origine e scambiamento; umidità del cippato fresato 25-40% contro 10-15% del pellet essiccato.",
 applicazioni="Scelta del combustibile per caldaie residenziali, centrali di teleriscaldamento, stufe e termostufe.",
 vantaggi="Combustibile standardizzato garantisce rendimento e basse emissioni, filiera certificata tracciabile, maggiore potere calorifico per volume stoccato.",
 limiti="Qualità variabile del prodotto non certificato, sensibilità ai prezzi di mercato, stoccaggio del cippato con rischio di degradazione e autoaccensione.",
 costi_e_economia="Ordini di grandezza indicativi: pellet certificato A1 300-450 €/t; cippato 100-150 €/t; differenza di rendimento reale tra cippato ben essiccato e fresco 10-20%.",
 casi_real_world="Il mercato italiano del pellet è tra i maggiori d'Europa con forte importazione; certificazione ENplus adottata dalla gran parte dei produttori nazionali.",
 normative="UNI EN ISO 17225 (classi di qualità del pellet e del cippato); Reg. UE 813/2013 (etichettatura energetica e requisiti ecodesign); schemi di certificazione volontaria di filiera.",
 note_cantiere="Un pellet di classe B in una caldaia tarata per A1 sporca lo scambiatore e aumenta le emissioni: la scheda tecnica della caldaia indica le classi ammesse."),

dict(categoria="Biogas", nome="Biogas da digestione anaerobica",
 descrizione="Produzione di biogas da materie organiche (agro-industriali) e conversione in energia elettrica e termica.",
 tecnologia="Digestori anaerobici a media temperatura (mesofili 35-40 °C) con alimentazione letame e colture dedicate (miscanthus, sorgo, triticale) o scarti agroalimentari; permanenza 20-60 giorni; biogas composto da metano 50-65%, CO2 30-45%, H2S e vapore; cogenerazione CHP con rendimento elettrico 35-40% e termico 45-50%; digestato da spandere come ammendante.",
 applicazioni="Aziende agricole zootecniche e agroindustriali, impianti da 100 kW a 3 MW elettrici, produzione combinata di calore di processo.",
 vantaggi="Valorizza scarti e reflui, bilancia stagionalità delle fonti, digestato ricco di azoto, doppia produzione elettrica+termica.",
 limiti="Gestione tecnica continua, emissioni odorigene da contenere, variabilità del metano in base alla sostanza, mercato degli incentivi cambiato più volte nel tempo.",
 costi_e_economia="Ordini di grandezza indicativi: costo impianto 3.000-7.000 €/kW elettrico; produzione specifica 4.000-7.000 kWh/kW·anno per agro; incentivi da verificare di anno in anno sul GSE.",
 casi_real_world="Parco italiano di impianti a biogas agro realizzato nella prima ondata FER anni 2010, oggi orientato all'upgrading a biometano.",
 normative="D.Lgs 28/2011 per l'incentivazione delle rinnovabili; disciplina dello spandimento del digestato (normativa nitrati D.Lgs 152/2006); adempimenti autorizzativi ambientali (AUA).",
 note_cantiere="La tenuta del digestore e la gestione del biogas (H2S corrosivo) sono punti critici: sensori, ventilazioni e manutenzione dei gruppi CHP decidono la vita dell'impianto."),

dict(categoria="Biometano", nome="Biometano: upgrading e iniezione in rete",
 descrizione="Depurazione del biogas fino a qualità da gas naturale e immissione nelle reti di distribuzione.",
 tecnologia="Upgrading con lavaggio ad acqua (scrubbing), adsorbimento con oscillazione di pressione (PSA), membrane polimeriche o lavaggio chimico amminico; rimozione di CO2, H2S, silossani e umidità; biometano con 95-99% CH4 e potere calorifico conforme alle specifiche del gestore di rete; possibilità di uso automotive (BioGNL liquefatto) o industriale.",
 applicazioni="Aziende agricole e agroindustriali con connessione alla rete gas, sostituzione del gas fossile, filiere del trasporto pesante.",
 vantaggi="Stoccabilità nella rete esistente, valorizzazione del biogas senza vincoli di autoconsumo, contribuzione alla decarbonizzazione del gas.",
 limiti="CapEx di upgrading e connessione, accordo con il distributore e specifiche stringenti, variabilità di incentivazione nel tempo.",
 costi_e_economia="Ordini di grandezza indicativi: upgrading 300.000-800.000 € per impianti agro da 250-500 Nm³/h; tariffe di iniezione e premialità da verificare sugli schemi GSE vigenti.",
 casi_real_world="Crescita degli impianti a biometano in Italia tra i primi mercati europei; upgrade degli impianti a biogas esistenti verso l'iniezione in rete.",
 normative="Disciplina dell'iniezione di biometano nelle reti (requisiti di qualità e accordi con i distributori); schemi incentivanti GSE aggiornati di volta in volta; D.Lgs 28/2011 come quadro FER.",
 note_cantiere="Prima di progettare l'upgrading serve il pre-accordo col gestore di rete: portata, pressione, specifiche e punto di consegna definiscono l'impianto."),

dict(categoria="Geotermia bassa entalpia", nome="Geotermia a bassa entalpia: sonde e pompe di calore geotermiche",
 descrizione="Sfruttamento del calore del sottosuolo con sonde di scambio per alimentare pompe di calore.",
 tecnologia="Sonde verticali in HDPE a doppia U in fori da 100-150 m (fino a 400 m nei sistemi più profondi) riempiti di bentonite-cemento; scambiatori orizzontali a spirale o a sonde in falda per piccoli impianti; pompe di calore geotermiche (acqua-aria, acqua-acqua) con COP 3,5-5 e SCOP stagionali elevati; rigenerazione estiva del campo sonde con ricarica del calore (free-cooling raffrescamento).",
 applicazioni="Riscaldamento e raffrescamento di edilizia residenziale, terziaria, condomini, edilizia industriale leggera; integrazione con produzione ACS.",
 vantaggi="Rendimenti altissimi e stabili (il sottosuolo è a temperatura costante), bassa visibilità dell'impianto, combinazione ideale con FV per copertura elettrica.",
 limiti="Richiede terreno per il campo sonde o possibilità di trivellazione, iter autorizzativo per i fori, costo iniziale superiore alle altre pompe di calore.",
 costi_e_economia="Ordini di grandezza indicativi: trivellazione e sonda 40-80 €/m; PC geotermica domestica 12.000-25.000 € installata; copertura incentivi tramite Conto Termico da verificare sul bando vigente.",
 casi_real_world="Ampia diffusione in Europa centrale (Germania, Svezia, Svizzera) con decine di migliaia di sonde; crescita in Italia su edilizia residenziale e GDO.",
 normative="D.Lgs 145/2013 (attività geotermica: procedura semplificata per scambiatori fino a 400 m di profondità e 100 kW termici; oltre, procedura ordinaria con valutazioni ambientali); regole regionali sulle trivellazioni.",
 note_cantiere="Il campo sonde va dimensionato sul carico termico invernale e verificato per il bilancio annuo: la sovratemperatura estiva degrada il COP se non c'è ricarica."),

dict(categoria="Geotermia alta entalpia", nome="Geotermia ad alta entalpia",
 descrizione="La geotermia da fluidi caldi profondi per produzione elettrica e diretta.",
 tecnologia="Sorgenti naturali o pozzi profondi (1-3 km) con fluidi a 150-350 °C; impianti a flash (separazione vapore/acqua) o a ciclo binario (ORC — Organic Rankine Cycle) per temperature più basse; resa elettrica 5-20% a seconda della temperatura; possibilità di teleriscaldamento a cascata (uso diretto del calore).",
 applicazioni="Aree vulcaniche attive, produzione baseload rinnovabile, teleriscaldamento urbano geotermico.",
 vantaggi="Fonte continua non intermittente, basso costo marginale, combinazione elettricità+calore.",
 limiti="Localizzata in aree specifiche, rischio indotto da reiniezione gestito con protocolli, investimenti esplorativi iniziali.",
 costi_e_economia="Ordini di grandezza indicativi: costo di esplorazione e pozzi la voce dominante; LCOE dei campi maturi tra i più bassi delle rinnovabili.",
 casi_real_world="Larderello in Toscana (provincia di Pisa-Grosseto), il più antico campo geotermico del mondo in produzione continuativa, con potenza installata complessiva dell'ordine del GW nel distretto toscano.",
 normative="Autorizzazioni per ricerca e coltivazione geotermica; discipline ambientali per pozzi e reiniezione; D.Lgs 145/2013 per il quadro autorizzativo geotermico.",
 note_cantiere="Le aree geotermiche storiche convivono con vincoli paesaggistici e termali: la valutazione di impatto integra entrambi gli aspetti."),

dict(categoria="Reti di calore", nome="Teleriscaldamento e reti di calore",
 descrizione="Distribuzione centralizzata del calore prodotto da biomasse, geotermia, recupero o cogenerazione.",
 tecnologia="Reti a doppia tubazione con tubi preisolati in acciaio o polietilene (PE-RT) a circuito primario ad alta temperatura (90-130 °C) o basse temperature (50-70 °C per reti di 4ª generazione); cabine di sottostazione di utenza con scambiatori e contabilizzazione; fonti centralizzate: caldaie a biomassa, recupero energetico, inceneritori ottimizzati, geotermia; perdite di rete 5-15% da contenere con isolamento e controllo.",
 applicazioni="Quartieri residenziali, distretti industriali, città con campo geotermico o impianti di recupero.",
 vantaggi="Fonte centralizzata efficiente e monitorabile, sostituzione diffusa delle caldaie private, possibilità di miscela di fonti rinnovabili.",
 limiti="Investimento iniziale della rete proporzionale alla lunghezza, densità di carico minima richiesta, manutenzione delle sottostazioni condominiali.",
 costi_e_economia="Ordini di grandezza indicativi: rete primaria 300-800 €/m lineare a seconda del diametro; sottostazione utenza 3.000-8.000 €; tariffa calore competitiva con gas in densità buone.",
 casi_real_world="Reti di teleriscaldamento a biomassa nelle valli alpine e appenniniche; distretti geotermici toscani; bandi per reti di calore efficienti promossi a livello nazionale e regionale.",
 normative="Requisiti di contabilizzazione del calore negli edifici (direttiva UE 2012/27 e recepimento); UNI 10200 per i sistemi di contabilizzazione; bandi e decreti per reti di calore da verificare alla data di progetto.",
 note_cantiere="La fattibilità di una rete nasce dalla densità termica: chiavi in mano si valutano linee chilometriche per MWh fatturato prima di progettare la tracciato."),

dict(categoria="Integrazione FV-termica", nome="Power-to-Heat: sfruttare l'eccedenza fotovoltaica in calore",
 descrizione="Conversione dell'elettricità rinnovabile in eccedenza in calore utile, con o senza accumulo.",
 tecnologia="Resistenze elettriche a immersione (booster) su accumuli di acqua calda sanitaria da 1.000-5.000 L; pompe di calore con multi-sorgente (FV + tariffa) e avvio su eccedenza; sistemi ibridi caldaia-PdC con logica di priorità; scambiatori estraibili per la manutenzione; controlli con meter di flusso e gestione degli stati di carica dell'accumulo.",
 applicazioni="Case unifamiliari e condomini con FV esistente, produzione ACS a basso costo marginale, reti di piccola taglia e centri sportivi.",
 vantaggi="Aumenta autoconsumo FV da 30% a 60-80%, riduce il prelievo da rete per ACS, sfrutta l'energia a costo quasi nullo, prepara l'edificio al futuro elettrico.",
 limiti="Necessita accumulo dimensionato per 1-3 giorni di fabbisogno ACS, gestione tariffe e logica di controllo, rendimento della conversione diretta limitato rispetto alla PdC.",
 costi_e_economia="Ordini di grandezza indicativi: accumulo 1.000 L in acciaio inox 1.500-3.500 €; booster e controllo 500-1.500 €; payback tipico 4-8 anni su famiglia con FV.",
 casi_real_world="Retrofit diffusi di serbatoi ACS con resistenze e logica di autoconsumo su edilizia residenziale con FV anni 2010-2020.",
 normative="Norme CEI per impianti elettrici e protezioni; requisiti per il collegamento delle utenze (CEI 0-21); norme igieniche per ACS (L. 238/2004 e circolari per la prevenzione della legionella).",
 note_cantiere="L'accumulo ACS va mantenuto a temperatura di legionellosi (ricircolo periodico ≥60 °C): il booster programma i cicli quando c'è sole, non a caso."),

dict(categoria="Accumulo termico", nome="Accumulo termico: buffer, stratificazione e materiali a cambiamento di fase",
 descrizione="Conservare il calore per separare produzione e utilizzo: dal serbatoio in acciaio ai PCM.",
 tecnologia="Serbatoi di accumulo in acciaio carbonio/inox con coibentazione e serpentine; stratificazione termica con bocchette di laminazione che mantengono zone calde sopra e fredde sotto (efficienza di stratificazione 80-95%); accumulatori a cambiamento di fase (PCM) con sali idrati o paraffine per accumulare in poco volume; accumuli combinati con serpentina FV per ACS.",
 applicazioni="Sistemi con pompa di calore (riduzione dei cicli di avvio), impianti solari termici, reti di calore, integrazione P2H.",
 vantaggi="Migliora il COP della PdC lavorando a carichi stabili, aumenta l'autoconsumo, riduce potenze contrattuali elettriche e gas.",
 limiti="Ingombro e peso dei grandi volumi, dispersioni se mal coibentati, costo dei PCM ancora elevato, necessità di stratificazione ben progettata.",
 costi_e_economia="Ordini di grandezza indicativi: accumulo 500-1.000 L 700-2.500 € installato; PCM 3-10 volte il costo per kWh accumulato rispetto all'acqua.",
 casi_real_world="Accumuli combinati solare termico + caldaia di vecchia generazione ancora in esercizio; nuovi sistemi PdC + buffer standard in climatizzazione residenziale.",
 normative="Norme per recipienti a pressione dove applicabili; marcatura CE dei serbatoi; norme igieniche ACS per temperatura e ricircolo.",
 note_cantiere="L'accumulo si dimensiona sulle ore di funzionamento decoupled: PdC che lavora 4 ore al giorno richiede buffer per il resto del fabbisogno."),

dict(categoria="Economia rinnovabili", nome="Incentivi e conto economico delle rinnovabili termiche ed elettriche",
 descrizione="Mappa aggiornabile degli incentivi italiani per FER elettriche e termiche, con la regola d'oro della verifica.",
 tecnologia="Detrazioni fiscali per riqualificazione energetica e misure antisismiche (aliquote e massimali aggiornati con cadenza di legge); Conto Termico 3.0 per pompe di calore, solare termico, biomasse e reti di calore; Contratti di Acquisto Diretto (CAD) gestiti dal GSE per piccole rinnovabili elettriche; CER e configurazioni aggregate; Scambio sul Posto chiuso ai nuovi impianti e RID come alternativa; Tariffe Premio FER riconosciute ai moduli aggiornate periodicamente dal GSE.",
 applicazioni="Ogni progetto di impianto rinnovabile o riqualificazione energetica in Italia, dalla villetta al campo FV.",
 vantaggi="Incentivi stabili e certificati riducono i tempi di ritorno; la combinazione detrazione + CER + autoconsumo è la leva principale per l'edilizia privata.",
 limiti="Le regole cambiano a ogni manovra di bilancio: aliquote, massimali e aperture di bando vanno sempre verificati alla data di progetto; cumuli e divieti vanno letti nel testo vigente.",
 costi_e_economia="Ordini di grandezza indicativi: rientro tipico 5-10 anni per PdC con incentivi, 6-12 per biomasse, 8-15 per geotermia senza detrazione agevolata — sempre da ricalcolare sul bando vigente.",
 casi_real_world="Aggiornamento dei pacchetti di detrazioni e del Conto Termico tracciato nei pack ENERGETICA_INCENTIVI e FOTOVOLTAICO di questa repository con fonti verificate a ottobre 2026.",
 normative="D.Lgs 28/2011; decreti requisiti minimi CAM edilizia; decreti Conto Termico (D.M. 7 agosto 2025 per la terza edizione) e aggiornamenti successivi; regole GSE per CER, RID, CAD e Tariffa Premio.",
 note_cantiere="Regola d'oro: prima di scrivere un preventivo con incentivi, verificare su GSE/ENEA/Agenzia delle Entrate il testo vigente alla data di presentazione della pratica; questa repository registra gli aggiornamenti nel CHANGELOG."),
]

write_pack("RINNOVABILI_IDRO_BIOMASSA_GEOTERMIA_PACK",
 "Rinnovabili idro, biomasse e geotermia", "FACOLTA_IMPIANTI_ENERGIA", "L2-L3",
 "Mini-idro, pumped storage, biomasse, biogas/biometano, geotermia bassa e alta entalpia, reti di calore, P2H, incentivi.",
 """# RINNOVABILI_IDRO_BIOMASSA_GEOTERMIA_PACK

**Rinnovabili idriche, da biomassa e geotermiche**

Mini-idro e turbine, pumped storage, caldaie a biomassa e qualità del combustibile, biogas e biometano, geotermia bassa e alta entalpia, teleriscaldamento, power-to-heat, accumulo termico, economia e incentivi con la regola della verifica annuale.

Schede: 12 (formato JSONL, un oggetto per riga).
""", rinnovabili)

# =====================================================================
# PACK 3 — CARPENTERIA METALLICA E ACCIAIO
# =====================================================================
carpenteria = [
dict(categoria="Acciai", nome="Acciai strutturali: gradi, laminati e zincati",
 descrizione="Le famiglie di acciaio da costruzione: gradi strutturali, lamiere e nastri zincati.",
 tecnologia="Acciai strutturali non legati S235/S275/S355 (cedimento 235-355 MPa) secondo UNI EN 10025, con qualità JR (resilienza a 27 J a 20 °C), J0 (27 J a 0 °C), J2/K2 (27 J a -20 °C); acciai bonificati e temprabili per applicazioni speciali; lamiere e nastri zincati a caldo secondo UNI EN 10346 (es. DX51D zinco Z100-Z275, ~7-20 µm per faccia); lamiere zincate a freddo e aluzinc; scelta del grado in funzione di resistenza, saldabilità e clima d'impiego.",
 applicazioni="Strutture portanti, carpenterie di facciata, tamponamenti metallici, elementi zincati per serramenti e opere di finitura.",
 vantaggi="Resistenza nota e certificata, disponibilità immediata dei laminati, marcatura CE del prodotto siderurgico, riciclabilità completa.",
 limiti="Sensibilità alla corrosione degli acciai non protetti, sensibilità al calore in caso di incendio, limiti di snellezza per la stabilità.",
 costi_e_economia="Ordini di grandezza indicativi: acciaio laminato di base 0,7-1,3 €/kg; lamiera zincata 0,9-1,6 €/kg; fluttuano con il mercato delle materie prime.",
 casi_real_world="S355 diffuso per strutture snelle in Europa; qualità J2/K2 obbligatorie dove la normativa sismica richiede resilienza a temperatura più bassa.",
 normative="UNI EN 10025 (acciai strutturali); UNI EN 10346 (lamiere e nastri zincati a caldo); NTC 2018 per i requisiti delle strutture metalliche.",
 note_cantiere="La certificazione dei colatai (mill certificates 3.1) deve riportare grado e qualità reali: il grado inferiore al progetto è non conformità grave."),

dict(categoria="Profilati", nome="Profili laminati e profili cavi",
 descrizione="Il catalogo dei profili metallici: dalle travi IPE alle tubazioni strutturali.",
 tecnologia="Travi IPE (ali strette, peso/m contenuto), HEA/HEB/HEM (ali larghe, resistenza al carico di punta), profili a U (UPN/UPE) per arcarecci e cordoli, angolari (L) e T; profili cavi strutturali rettangolari/quadrati/circolari secondo UNI EN 10219 con spessori 2-12,5 mm; profili saldati su disegno per forme speciali; tabelle dei profili con caratteristiche geometriche e meccaniche per il calcolo.",
 applicazioni="Tetti e solai in acciaio, colonne, strutture di soppalchi, ponti, facciate e sottostrutture, carpenteria leggera.",
 vantaggi="Alta resistenza con peso contenuto, precisione dimensionale dei laminati, assemblaggio rapido con bulloni o saldature.",
 limiti="Costo superiore al cls per molte applicazioni, instabilità degli elementi snelli, rumore/vibrazioni se non progettati contro lo svergolamento.",
 costi_e_economia="Ordini di grandezza indicativi: profilato laminato 1,0-1,8 €/kg; profilo cavo 1,2-2,2 €/kg; taglio, foratura e zincatura aggiungono 15-40%.",
 casi_real_world="Profili HEA/HEB standard in tutta la carpenteria portante europea; sostituzione dei profili a U con UPE a ali parallele per facilitare i dettagli.",
 normative="UNI EN 10365 (dimensioni e caratteristiche dei profili laminati); UNI EN 10219 (profili cavi strutturali); Eurocodice 3 (UNI EN 1993) per il dimensionamento.",
 note_cantiere="Le tolleranze dei profili cavi saldati vanno specificate in fase di ordine: lo scostamento tra ali parallele e perpendicolarità influisce sul montaggio."),

dict(categoria="Carpenteria leggera", nome="Carpenteria metallica leggera per costruzioni a secco",
 descrizione="Profili sottili zincati per contropareti, contropavimenti, tetti e strutture leggere.",
 tecnologia="Profili in lamiera zincata piegata a freddo (C, Z, omega, montanti e guide) con spessori 0,5-3 mm; zincatura a caldo continua Z140-Z275; controventamenti con nastri o profili a L; membrature che lavorano prevalentemente a trazione e puntoni; connessioni con viti autofilettanti e rivetti; profili per cartongesso (montante 48-70 mm, guida) separati dai profili strutturali portanti.",
 applicazioni="Contropareti e controsoffitti, tamponamenti interni, piccole strutture di copertura, soppalchi leggeri, case prefabbricate in steel framing.",
 vantaggi="Leggerezza, velocità di posa, sezioni ridotte, ottimo rapporto peso/resistenza, materiali standardizzati e riciclabili.",
 limiti="Spessori sottili sensibili all'instabilità locale, corrosione agli estremi tagliati da proteggere, limiti di luce rispetto ai profili pesanti.",
 costi_e_economia="Ordini di grandezza indicativi: profili leggeri zincati 1,0-1,8 €/kg; parete in controparete posata 25-60 €/m² compresa lana e lastre.",
 casi_real_world="Sistemi costruttivi a secco diffusissimi in edilizia interna; steel framing residenziale di riferimento nei paesi anglosassoni e in crescita in Italia.",
 normative="UNI EN 10346 (lamiere zincate di base); Eurocodice 3 parte 1-3 per gli elementi in pareti sottili; ETA dei sistemi costruttivi certificati.",
 note_cantiere="I tagli e le forature in zona zincata vanno ritoccati con vernice a base di zinco; il ferro scoperto arrugginisce in pochi mesi in facciata."),

dict(categoria="Saldature", nome="Saldature strutturali: processi, qualifica e difetti",
 descrizione="La saldatura come cuore della carpenteria: processi, procedure e controllo della qualità.",
 tecnologia="Processo MAG/MIG-MAG (arco con gas di protezione, filo animato o pieno) per l'acciaio strutturale; sommerso (SAW) per cordoni lunghi in officina; elettrodo rivestito (MMA) per riparazioni; qualifica della procedura (WPQR secondo UNI EN ISO 15614-1) e dei saldatori (UNI EN ISO 9606-1); preparazione dei bordi (K, V, I, Y) e gap; livelli di accettazione dei difetti secondo UNI EN ISO 5817 (B, C, D); controllo visivo al 100% e NDT sulle giunzioni principali.",
 applicazioni="Assemblaggio in officina di travi e telai, giunzioni di cantiere, rinforzi e riparazioni, strutture di ponti e grandi luci.",
 vantaggi="Continuità statica piena, rigidezza, economia su grandi serie, libertà geometrica nella forma delle giunzioni.",
 limiti="Deformazioni da ritiro e concentrazioni di tensione residua, sensibilità alla fatica dei cordoni, necessità di qualifiche e controlli costosi, fumi e rischi per il saldatore.",
 costi_e_economia="Ordini di grandezza indicativi: costo saldatura strutturale 0,5-1,5 €/kg di metallo d'apporto saldato; qualifica procedura 1.000-3.000 € per set di prova.",
 casi_real_world="Criteri di accettazione ISO 5817 livello C tipici per strutture edili; livello B per ponti e grandi opere secondo specifiche.",
 normative="UNI EN ISO 5817 (livelli qualità giunzioni); UNI EN ISO 15614-1 (qualifica procedure); UNI EN ISO 9606-1 (qualifica personale); UNI EN ISO 13920 (tolleranze dimensionali saldature); UNI EN 1090-2 per l'esecuzione.",
 note_cantiere="Prima di saldare in cantiere: vento e umidità rovinano il gas di protezione; in esterno servono tende o processi con autoprotettivi."),

dict(categoria="Assemblaggi", nome="Assemblaggi bullonati: sistemi HR e svolgimento A/B/C",
 descrizione="I collegamenti a bullone ad alta resistenza: precarico, superfici e calcolo.",
 tecnologia="Sistemi HR (ad alta resistenza) secondo UNI EN 14399 (parti 1-10, classi 8.8/10.9) con elementi precaricati; superfici di contatto classificate: classe A (sabbiatura fino a grado Sa 2½, friccione elevata) e classi B/C (con ridotta o incerta frizione); svolgimento A: calcolo secondo la resistenza all'attrito (giunti non slittanti); svolgimento B: calcolo come connessione saldata con bulloni precaricati come serraggio; svolgimento C: bulloni non precaricati lavoranti a taglio e punzonamento; serraggio controllato con chiavi tarate o metodo combinato parte-angolo.",
 applicazioni="Giunti di travi e colonne, coperture industriali, ponti, strutture smontabili e provvisorie, rinforzi in esteso.",
 vantaggi="Montaggio rapido senza attrezzature speciali, controllo di qualità semplice, possibilità di smontaggio, minori deformazioni in officina.",
 limiti="Perdita di precarico nel tempo, fattori di attrito sensibili alla preparazione superficiale, ingombro delle teste in spazi stretti, verifiche da documentare.",
 costi_e_economia="Ordini di grandezza indicativi: giunzione bullonata HR 2-5 volte il costo del solo materiale a seconda dei collaudi richiesti; verifica serraggio documentata 5-15 €/giunzione.",
 casi_real_world="Svolgimento A diffuso nei ponti italiani (classe superficiale A con sabbiatura); svolgimento C comune in edilizia industriale ordinaria.",
 normative="UNI EN 14399 (sistemi HR); Eurocodice 3 UNI EN 1993-1-8 (progettazione delle connessioni); CNR 10011 (istruzioni per le costruzioni in acciaio) come riferimento storico.",
 note_cantiere="Il precarico si perde se le superfici sono sporche o oliate: sabbiatura e pulizia immediata prima del montaggio; le guarnizioni non vanno mai tra le superfici di attrito."),

dict(categoria="Marcatura CE", nome="Marcatura CE e controllo di produzione in fabbrica (FPC)",
 descrizione="UNI EN 1090: il passaporto europeo della carpenteria strutturale.",
 tecnologia="Norma UNI EN 1090-1 per la marcatura CE degli elementi strutturali metallici; UNI EN 1090-2 per i requisiti di esecuzione con classi EXC1 (edilizia ordinaria), EXC2 (strutture principali), EXC3 (grandi opere, ponti) e EXC4 (eccezionale); sistema di controllo di produzione in fabbrica (FPC) documentato; fascicolo di fabbricazione con certificati materiali, procedure saldate, scarti e NDT; distinzione tra esecutore (fabbrica) e progettista (classi EXC).",
 applicazioni="Ogni carpenteria strutturale destinata al mercato europeo: telai, ponti, facciate portanti, torri e pali.",
 vantaggi="Garanzia uniforme europea di qualità, tracciabilità documentale completa, accesso al mercato unico.",
 limiti="Onere documentale rilevante per le fabbriche piccole, costi di certificazione e audit annuali, classi superiori richiedono personale qualificato dedicato.",
 costi_e_economia="Ordini di grandezza indicativi: certificazione e mantenimento FPC 5.000-20.000 €/anno per officina; impatto sul prezzo del fabbricato 3-10% secondo la classe EXC.",
 casi_real_world="EXC2 come classe minima diffusa nella carpenteria edilizia italiana; EXC3 nei ponti e nelle grandi opere secondo il capitolato.",
 normative="UNI EN 1090-1 e UNI EN 1090-2; Reg. UE 305/2011 (CPR — regolamento prodotti da costruzione).",
 note_cantiere="Senza marcatura CE e fascicolo di fabbricazione l'elemento non si può installare: verificarlo alla consegna, non dopo il montaggio."),

dict(categoria="Collaudi NDT", nome="Prove non distruttive sulla carpenteria",
 descrizione="VT, PT, MT, UT e RX: il protocollo di verifica dei giunti senza smontare nulla.",
 tecnologia="Controllo visivo VT al 100% dei cordoni con lente e gauge; liquidi penetranti PT per le cricche superficiali; magnetoscopia MT per i difetti sotto-superficiali su ferromagnetici; ultrasuoni UT (UNI EN ISO 17640) per difetti interni di pienezza e giunzioni a T; radiografia RT per piastre e giunzioni accessibili; campionamento dei punti saldati secondo piano di controllo; registrazione su rapporti di prova con accettazione riferita alla ISO 5817.",
 applicazioni="Collaudi di officina e di cantiere, giunzioni di ponti, riparazioni e rinforzi, sospetti difetti in esercizio.",
 vantaggi="Rilevano i difetti prima che diventino rotture, frazionabili per estensione con economia, documentazione oggettiva per il collaudo.",
 limiti="Richiedono personale certificato (livello 2/3), accessibilità della superficie, interpretazione specialistica dei segnali UT, costi di apparecchiature.",
 costi_e_economia="Ordini di grandezza indicativi: UT su giunzione 50-200 €/metro di cordone secondo accessibilità; RT 100-300 €/lastra; piano NDT completo di un ponte da decine di migliaia di euro.",
 casi_real_world="Campionamenti UT al 10-100% su giunzioni principali di ponti secondo classe EXC3; verifiche MT obbligatorie dopo riparazioni in sito.",
 normative="UNI EN ISO 17640 (utensili e procedure UT); UNI EN ISO 17638 (MT); UNI EN ISO 3452 (PT); UNI EN ISO 5817 (criteri accettazione); UNI EN ISO 9712 (certificazione personale NDT).",
 note_cantiere="Le verifiche NDT vanno pianificate PRIMA della verniciatura definitiva: ritrovare un difetto sotto la vernice costa il doppio."),

dict(categoria="Corrosione", nome="Protezione dalla corrosione: classi ambientali e sistemi",
 descrizione="Durabilità dell'acciaio: dalla classificazione ISO 12944 alla zincatura e ai cicli vernicianti.",
 tecnologia="Classi di corrosività ISO 12944-2: C1 (interni asciutti), C2 (interni), C3 (urbano e industriale leggero), C4 (industriale, costiero con bassa salinità), C5-I/C5-M (industriale aggressivo, marino); durabilità bassa/medio-alta/very high definita in anni fino alla prima manutenzione; sistemi: zincatura a caldo (EN ISO 1461, ~55-85 µm di Zn), zinco a spruzzo (metallizzazione), vernici epossidiche ricche di zinco + poliuretano con spessori 160-320 µm; rinnovo zincatura per i tagli e le saldature di cantiere.",
 applicazioni="Facciate metalliche, strutture industriali, ponti, opere marittime e costiere, serramenti esterni.",
 vantaggi="Vita utile moltiplicata rispetto all'acciaio nero, manutenzione programmabile, costo poco incidere sul totale strutturale.",
 limiti="La qualità della preparazione superficiale (sabbiatura grado Sa 2½) decide tutto, i danneggiamenti da trasporto vanno ritoccati, nel marino servono cicli spessi e controlli ravvicinati.",
 costi_e_economia="Ordini di grandezza indicativi: zincatura a caldo 0,5-1,0 €/kg; ciclo verniciante epossidico+PU 15-40 €/m² seconda preparazione; preparazione sabbiatura 8-20 €/m².",
 casi_real_world="Cicli ISO 12944 C4 molto alta adottati su facciate urbane; strutture portuali con zincatura + rivestimento duplex (zinco+vernice).",
 normative="UNI EN ISO 12944 (protezione anticorrosiva con vernici); UNI EN ISO 1461 (zincatura a caldo); UNI EN ISO 2063 (metallizzazione); UNI EN ISO 8501-1 (gradi di sabbiatura).",
 note_cantiere="Il ferro scoperto dal taglio, dalla foratura o dal trasporto si ritocca con vernice a base di zinco a spessori adeguati: il ritocco a pennello leggero è la prima causa di ruggine precoce."),

dict(categoria="Antincendio", nome="Protezione antincendio delle strutture metalliche",
 descrizione="Conservare la portanza dell'acciaio al fuoco: intumescenti, vermiculite e protezioni passive.",
 tecnologia="La resistenza meccanica dell'acciaio crolla oltre i 500-600 °C (ceduta), con temperatura critica di progetto a seconda del rapporto carico/resistenza; protezioni passive: vernici intumescenti (gonfiamento che forma schermo cokeificato, spessori 0,5-2,5 mm) per profili non esposti, vermiculite spruzzata cementizia o a base legante organico per profili esposti, lastre e mantelli, massetti e controsoffitti, sistemi a lame d'acqua per facciate e coperture; classi di resistenza R 30, R 60, R 90, R 120.",
 applicazioni="Strutture portanti di edifici civili, coperture e facciate metalliche, ponti sotto gallerie, aree con rischio incendio definito.",
 vantaggi="Senza protezione l'acciaio non supera R 15: la protezione permette l'uso diffuso con classi fino a R 120, scelta tra estetica (intumescente) e economia (vermiculite).",
 limiti="Spessore intumescente legato al profilo e alla classe R (massa superficiale), applicazione in officina per garantire il certificato, danneggiamenti da cantiere da riparare con lo stesso prodotto.",
 costi_e_economia="Ordini di grandezza indicativi: vermiculite spruzzata 15-35 €/m² di profilo; intumescente in officina 20-60 €/m²; riparazione cantiere a preventivo del produttore.",
 casi_real_world="Certificazioni secondo UNI EN 13381 con tabella di massa superficiale per classe R; sistemi con valutazione ETA applicati su edilizia commerciale.",
 normative="UNI EN 13381 (metodi di prova e valutazione della protezione); Eurocodice 1 parte 1-2 (UNI EN 1991-1-2) per le curve di incendio e la temperatura critica; NTC 2018 e Codice prevenzione incendi per i requisiti.",
 note_cantiere="L'intumescente va applicato in officina controllata con sistema certificato completo (fondo, intermedio, finitura): la finitura estetica diversa annulla la certificazione."),

dict(categoria="Montaggio", nome="Montaggio della carpenteria in cantiere",
 descrizione="Dalla consegna in officina alla struttura in opera: sequenza, giunti e precisione.",
 tecnologia="Sequenza di montaggio dalle colonne ai correnti, con giunti principali a bullone per taratura e giunti secondari saldati; taratura con viti di regolazione e lamelle di taratura in cls o acciaio; verifica di verticalità con teodolite e livella; serraggi con sequenza incrociata documentata; distacchi elettrici per la saldatura vicino a impianti; coordinamento con la gru (portata, raggi, fasci di sollevamento con bilancieri).",
 applicazioni="Capannoni industriali, coperture, ponti, sopralzi e ampliamenti di edifici esistenti.",
 vantaggi="Cantiere rapido e pulito rispetto al cls, qualità controllata in officina, riduzione dei tempi di costruzione.",
 limiti="Dipendenza dalle condizioni meteo per le altezze, necessità di precisione dei nuclei di fondazione, vincoli di trasporto per elementi lunghi.",
 costi_e_economia="Ordini di grandezza indicativi: montaggio 0,5-1,5 €/kg seconda complessità e altezza; gru a torre o autogru 1.000-4.000 €/giornata.",
 casi_real_world="Capannoni industriali montati in 4-12 settimane; ponti assemblati per lotti con giunti di cantiere minimizzati.",
 normative="UNI EN 1090-2 per tolleranze di montaggio; procedure di sollevamento secondo D.Lgs 81/2008 per attrezzature; Piano di Montaggio documentato.",
 note_cantiere="La tolleranza si accumola: la quota del primo pilastro decide la copertura; la taratura dei plinti con resine o lamelle avviene prima del serraggio definitivo."),

dict(categoria="Grandi strutture", nome="Ponti e grandi strutture metalliche",
 descrizione="Cenni tecnici sulle grandi strutture di acciaio: forme, cantiere e fatica.",
 tecnologia="Ponti ad impalcato metallico (piatto ortotropo o reticolare), a stralli o a arco con impalcato sospeso; controfrecce e frecce per ridurre i momenti in campata; verifiche a fatica secondo UNI EN 1993-1-9 per i dettagli sensibili; giunti strutturali che consentono dilatazioni e rotazioni; cantiere di varo con spinte, carrelli o centina a sbalzo; protezione anticorrosiva e antincendio di lunga durata.",
 applicazioni="Grandi luci su valli e corsi d'acqua, sovrappassi, passerelle, coperture di grandi spazi e stadi.",
 vantaggi="Luci impossibili al cls, leggerezza sulle fondazioni, prefabbricazione di precisione, ripristino rapido delle infrastrutture.",
 limiti="Sensibilità a fatica e vibrazioni, manutenzione della protezione superficiale, costi di verifica e collaudo elevati.",
 costi_e_economia="Ordini di grandezza indicativi: carpenteria di ponte 4-8 €/kg installata; verifiche e collaudi 3-8% del valore strutturale.",
 casi_real_world="Nuovo viadotto Polcevera (Ponte Genova San Giorgio, 2020) come riferimento della ricostruzione rapida in acciaio; passerelle pedonali metalliche diffuse nelle reti ciclopedonali.",
 normative="UNI EN 1993-1-9 (fatica); UNI EN 1090-2 classe EXC3; Eurocodici strutturali e NTC 2018 per il calcolo; specifiche ministeriali per le opere d'arte.",
 note_cantiere="Le giunzioni di continuità sulle strutture a fatica vanno progettate e controllate con la stessa attenzione delle membrature: è lì che nascono le cricche."),

dict(categoria="Sostenibilità", nome="Acciaio, sostenibilità ed economia circolare",
 descrizione="L'impronta ambientale e il costo dell'acciaio da costruzione: LCA, EPD e riciclo.",
 tecnologia="L'analisi del ciclo di vita (LCA) secondo UNI EN 15804 e UNI EN 15978 per confrontare le soluzioni strutturali; Dichiarazioni Ambientali di Prodotto (EPD) dei laminati con contenuto di acciaio di ricircolo tipicamente elevato (acciaio EAF prodotto in forno elettrico con altissima quota di scarto); riciclabilità teorica del 100% senza degrado di qualità; riduzione di peso = riduzione di trasporti e fondazioni; ricondizionamento degli elementi di seconda mano (beam reuse).",
 applicazioni="Scelta strutturale nella progettazione sostenibile, certificazioni energetiche e ambientali degli edifici, acquisti verdi.",
 vantaggi="Materiale circolare per eccellenza, peso strutturale contenuto riduce il cemento delle fondazioni, precisione che riduce gli scarti di cantiere.",
 limiti="L'acciaio primario da minerali di ferro ha emissioni elevate: la scelta conta (EAF vs BF-BOF), i costi di mercato sono volatili, le distanze di trasporto incidono.",
 costi_e_economia="Ordini di grandezza indicativi: carpenteria realizzata e montata 2,5-5,0 €/kg; ponti e lavori speciali 4-8 €/kg; il prezzo del materiale rappresenta 25-40% del costo chiavi in mano.",
 casi_real_world="Crescente richiesta di EPD e acciaio a basso impatto negli appalti pubblici italiani; riuso strutturale di elementi metallici in progetti di economia circolare.",
 normative="UNI EN 15804 e UNI EN 15978 (LCA e indicatori ambientali); Regolamento EU 305/2011 (CPR); criteri ambientali minimi (CAM) per le costruzioni dove applicabili.",
 note_cantiere="Chiedere sempre l'EPD del laminato per la certificazione dell'edificio: senza dichiara-ambientale, il punteggio green del progetto perde un pezzo."),
]

write_pack("CARPENTERIA_METALLICA_E_ACCIAIO_PACK",
 "Carpenteria metallica e acciaio", "FACOLTA_INGEGNERIA", "L1-L2",
 "Acciai, profili, saldature, bullonati, CE 1090, NDT, corrosione, antincendio, montaggio, ponti, sostenibilità.",
 """# CARPENTERIA_METALLICA_E_ACCIAIO_PACK

**Tecnologia della carpenteria metallica**

Acciai strutturali e zincati, profili laminati e leggeri, saldature e qualifiche, sistemi HR e svolgimenti A/B/C, marcatura CE EN 1090, prove non distruttive, corrosione ISO 12944, protezione antincendio, montaggio in cantiere, ponti e sostenibilità.

Schede: 12 (formato JSONL, un oggetto per riga).
""", carpenteria)

print("OK giro K")
