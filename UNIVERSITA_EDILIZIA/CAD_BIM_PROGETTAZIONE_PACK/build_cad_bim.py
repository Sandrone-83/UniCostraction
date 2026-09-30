# -*- coding: utf-8 -*-
"""Costruisce CAD_BIM_PROGETTAZIONE_PACK: metodo BIM, IFC, ISO 19650, authoring, scan-to-BIM."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Fondamenti BIM", "Che cos'è il BIM: modello, processo, collaborazione",
 "BIM (Building Information Modeling) non è un software: è un metodo di lavoro in cui un modello digitale condiviso, a oggetti informati, descrive geometria E dati (materiali, costi, tempi, manutenzione) dell'edificio lungo tutto il ciclo di vita.",
 "Ogni elemento (muro, porta, tubo) è un oggetto con proprietà parametriche; le viste (piante, sezioni, prospetti) sono estrazioni automatiche dello stesso modello: cambia il muro, si aggiornano tutte le tavole, il computo e le viste 3D.",
 "Progettazione integrata, gare pubbliche (BIM obbligatorio sopra soglie in Italia dal 2022-2025 con DM 312/2021), gestione e manutenzione.",
 "Una fonte unica di verità: fine alle inconsistenze tra tavole; computo metrico e distinta materiali quasi automatici; simulazioni energetiche e strutturali sullo stesso oggetto.",
 "Richiede un cambio organizzativo, non solo tecnico: convenzioni condivise, responsabilità sui dati, formazione; il modello 'sporco' informativamente è peggio di un CAD 2D ben fatto.",
 "Avvio: formazione 3-10 gg/persona; modellazione BIM di un edificio medio costa in genere come il doppio del CAD 2D iniziale, ripagata sulle varianti e sul computo.",
 "Commessa pubblica con BIM obbligatorio: il computo automatico dal modello ha ridotto da 3 settimane a 2 giorni la redazione della distinta base della gara, con zero errori di trascrizione.",
 "DM 312/2021 (BIM obbligatorio PA); UNI 11337 (informatizzazione processi edilizi).",
 "Regola: il BIM non sostituisce il progettista che sa costruire — sostituisce la riscrittura dei dati."),
s("LOD e informativa", "LOD e LOIN: quanta informazione nel modello",
 "Il LOD (Level of Development, standard americano; in Italia spesso 'Level of Detail') indica quanto l'elemento del modello è affidabile: LOD 100 concettuale, 200 generico, 300 produzione esecutiva, 400 fabbricazione, 500 as-built. Il LOIN (Level of Information Need, UNI EN ISO 19650) specifica invece QUALI dati servono per ogni uso (quantità, geometria, documentazione).",
 "Si definisce una matrice uso-informazione per ogni fase: gara (LOD 200-300), esecutivo (300), produzione serramenti (350-400), as-built (500); i LOD sono definiti per singolo elemento, non per tutto il modello uniformemente.",
 "Capitolati informativi, gare BIM, commesse con premi/penali sulla qualità del modello.",
 "Il LOD scritto nel contratto rende misurabile la qualità del modello: niente più 'il modello è finito' senza definizione di 'finito'.",
 "Sovradimensionare i LOD costa denaro senza valore: modellare il singolo chiodo a LOD 400 in fase preliminare è spreco.",
 "Modellazione esecutiva di un edificio residenziale: 20-60 €/m² in più rispetto al solo 2D, a seconda del LOD richiesto.",
 "Gara con LOD 300 prescritto: il progettista che consegnava un modello LOD 200 si è visto rigettare la fase progettuale; il criterio LOD ha reso oggettiva la verifica.",
 "UNI EN ISO 19650-1/2 (LOIN); LOD Specification (bimFORUM, uso internazionale).",
 "Nel contratto BIM: scrivere LOD/LOIN per disciplina e per fase, con verifica puntuale sul campione."),
s("IFC e openBIM", "IFC: il formato aperto per lo scambio dei modelli",
 "IFC (Industry Foundation Classes, ISO 16739) è lo schema aperto con cui i modelli BIM passano tra software diversi: geometria, proprietà, gerarchie di oggetti; è la base dell'openBIM (collaborazione senza vincolo a un unico vendor).",
 "Esportazione IFC2x3 o IFC4 dal modello nativo; mappatura delle classi (IfcWall, IfcDoor, IfcSpace...); i 'Property Set' portano i dati (es. Pset_WallCommon con fuoco, portanza, U-value); BCF (BIM Collaboration Format) scambia annotazioni e collisioni fuori dal modello.",
 "Scambio tra progettisti con software diversi, consegna al committente pubblico, archivio digitale dell'opera.",
 "Indipendenza dal vendor: il committente non resta prigioniero del software di chi ha progettato; verifiche e computi terzi possibili.",
 "L'export IFC perde spesso intelligenza parametrica: il modello importato è 'fotografia', non più modificabile come l'originale; i mapping delle proprietà richiedono disciplina.",
 "Plugin e gestione IFC inclusi nei principali BIM authoring; validazione IFC con tool open source gratuiti (es. BIMserver/IfcOpenShell).",
 "Consegna IFC del modello strutturale al coordinatore: rilevate 140 collisioni con gli impianti PRIORA del cantiere; risolverle sul modello è costato giorni, in cantiere sarebbero stati mesi di varianti.",
 "ISO 16739 (IFC); buildingSMART Italia (convenzioni nazionali).",
 "Nel flusso di lavoro: esportare IFC a ogni revisione significativa e archiviarlo col numero di revisione, come si fa col PDF delle tavole."),
s("ISO 19650", "ISO 19650: gestione informativa dell'edificio",
 "La serie ISO 19650 (derivata dal britannico PAS 1192) definisce il processo: Information Requirements del committente (EIR), BIM Execution Plan (BEP) del fornitore, convenzione di denominazione degli oggetti e dei documenti, Common Data Environment (CDE) con stati del dato (work in progress, shared, published, archived).",
 "Flusso: il committente scrive le EIR (cosa vuole, quando, a che livello) → i fornitori rispondono col BEP (come lo faranno) → il CDE gestisce i passaggi di stato Work In Progress → Shared → Published con regole di responsabilità; convenzione di naming: Origine-Campo-Tipo-Numero (es. AC-M3-AR-RP-0001).",
 "Commesse pubbliche e private organizzate, team multidisciplinari, gestione documentale digitale.",
 "Chiarezza contrattuale: ognuno sa cosa deve produrre e chi verifica; lo storico completo dei dati è tracciato e giuridicamente difendibile.",
 "Burocratizzazione eccessiva su commesse piccole: applicare ISO 19650 'light' (EIR di 2 pagine, CDE = cartella condivisa disciplinata) è più efficace del metodo completo su una villetta.",
 "Implementazione CDE: da cartella condivisa (0 €) a piattaforme professionali (5-30 €/utente/mese).",
 "Commessa ospedaliera: il CDE con stati del dato ha permesso di dimostrare in arbitrato quale versione della sala operatoria era stata approvata e da chi, chiudendo una controversia da 400.000 € in settimane.",
 "UNI EN ISO 19650-1/2 (adottate in Italia); UNI 11337-6 (modello informativo).",
 "Principio cardine: lo stato del dato nel CDE è più importante del software usato — il WIP non va mai in cantiere."),
s("Authoring tool", "Gli authoring BIM: Revit, Archicad, Allplan, Edificius",
 "I principali strumenti di modellazione: Autodesk Revit (più diffuso, disciplne architettonica/strutturale/MEP), Graphisoft Archicad (forte in architettura, storico italiano), Allplan (diffuso nei grandi studi e nelle infrastrutture), Edificius e le suite Namirial/ACC (forti in Italia, integrate col computo), Tekla Structures (carpenterie e strutture metalliche).",
 "Modellazione per famiglie/tipi di oggetto con parametri; viste filtrabili per disciplina; tavole come composizioni di viste; quantità estratte da tabelle di scheda; interoperabilità via IFC, API e plug-in; cloud: modelli federati e visualizzazione web.",
 "Scelta dello strumento in base a: disciplina dominante, ecosistema dello studio, esigenze di computo (integrazione con i prezzari italiani), collaborazione con altri studi.",
 "Il tipo giusto dimezza i tempi: chi fa computi in Italia spesso preferisce suite integrate (Edificius/Primus); chi lavora su larga scala internazionale va su Revit; chi fa capannoni metallici su Tekla.",
 "La migrazione tra strumenti a progetto in corso è costosa; i formati nativi non sono interoperabili tra loro (solo via IFC, con perdite).",
 "Licenze: 1.500-3.500 €/anno per posto (Revit/Archicad/Allplan); suite italiane: offerte anche in abbonamento mensile più accessibile; hardware: workstation 2.000-4.000 €.",
 "Studio di 8 persone passato da CAD 2D a Archicad: le tavole esecutive di una villa sono passate da 6 settimane a 3, e il computo ha smesso di essere la fase 'temuta'.",
 "Nessuna norma sul software; riferimento processi UNI 11337 / ISO 19650.",
 "Criterio di scelta per il LLM da consigliare: tipo di commessa, ecosistema dei partner, requisiti di gara, budget formazione."),
s("Discipline e federazione", "Le discipline del modello: architettonica, strutturale, MEP",
 "Il modello dell'edificio si costruisce per discipline distinte che poi si federano: architettonico (A), strutturale (S), meccanico/impiantistico (M), elettrico (E), idraulico (P); ogni disciplina modella i propri elementi secondo le EIR condivise.",
 "Origini e punti di aggancio comuni (shared coordinates, griglie, livelli identici); convenzione di colori/filtri per disciplina; il modello federato si ottiene caricando i file disciplinari nello stesso spazio (Navisworks, Solibri, BIM 360/ACC, usBIM).",
 "Coordinamento progettuale, verifica interferenze, consegna al committente multi-disciplina.",
 "Le interferenze si scoprono sul modello, non in cantiere: il risparmio medio documentato da studi settoriali è intorno al 20-30% dei costi di variante (stima McKinsey/Autodesk da trattare come ordine di grandezza).",
 "Se le discipline non condividono origini e livelli, la federazione è un disastro di falsi allineamenti; serve un BEP rispettato da tutti.",
 "Verifica interferenze con software di clash detection: inclusa o poche centinaia di euro/mese; costo maggiore è l'organizzazione, non il software.",
 "Modello federato di un edificio scolastico: 210 interferenze struttura-impianti risolte in progettazione; in cantiere le stesse avrebbero richiesto trapani sulle travi e richieste di variante.",
 "UNI 11337-4 (attività progettuali informatizzate); convenzioni buildingSMART.",
 "Regola: nessuna disciplina modella sopra gli altri senza aver caricato la versione 'shared' più recente delle altre."),
s("Clash detection", "Clash detection e coordinamento delle interferenze",
 "La verifica automatica delle collisioni tra discipline (clash detection) confronta solidi dei modelli federati: tubo contro trave, porta contro armadio contro montante, canalina contro intelaiatura; i clash si classificano hard (collisione fisica), soft (tolleranza/manutenzione), workflow (logistica tempi).",
 "Regole di verifica per coppie di discipline con tolleranze (es. tubazioni vs struttura: nessuna tolleranza; illuminazione vs controsoffitto: 5 cm di servizio); report con screenshot, ID degli elementi, gravità, assegnatario, scadenza; ciclo: rilevamento → assegnazione → risoluzione nel modello nativo → rifederazione → verifica chiusura.",
 "Tutte le commesse BIM con più discipline; in particolare impianti vs strutture in edifici tecnologicamente densi (ospedali, data center, industriali).",
 "Sposta il costo dell'errore dalla fase di cantiere (prezzo pieno, ritardi) alla fase di progetto (prezzo quasi nullo): è il business case principale del coordinamento BIM.",
 "Troppi falsi positivi (tolleranze non settate) fanno ignorare il report: calibrare le regole è un mestiere.",
 "Software di coordinamento: da gratuiti/open source a 1.000-3.000 €/anno; il costo vero è il tempo dei progettisti per risolvere.",
 "Data center: il coordinamento BIM degli impianti ha permesso il montaggio 'a secco' di 40 km di canaline senza una sola modifica in cantiere, con il programma rispettato al giorno.",
 "buildingSMART MVD; convenzioni di coordinamento del BEP.",
 "Metrica da insegnare al LLM: numero di clash aperti per area alla consegna di ogni fase, tendenza a zero prima dell'esecutivo."),
s("Scan-to-BIM", "Scan-to-BIM: dal rilievo alla modello dell'esistente",
 "Lo scan-to-BIM converte la nuvola di punti del rilievo laser in un modello BIM fedele dell'esistente (HBIM per i beni storici): geometria semplificata LOD 200-300 con la giusta approssimazione delle irregolarità reali.",
 "Registrazione nuvola → pulizia → suddivisione per ambiente/livello → modellazione 'as-found' su sezioni della nuvola con tolleranza dichiarata (es. muri fuori piombo modellati al piano medio con nota); i materiali e lo stato degrado si documentano in proprietà e foto collegate.",
 "Ristrutturazioni senza disegni, retrofit energetico, patrimonio storico, verifica deformazioni, impianti su esistente.",
 "Il modello dell'esistente alimenta computo, verifiche strutturali ed energetiche con dati veri invece che supposizioni: il preventivo sul serio nasce qui.",
 "La nuvola è infinitamente dettagliata: modellare TUTTO è impossibile; serve una convenzione di semplificazione, altrimenti costi fuori controllo.",
 "Scan-to-BIM: 8-25 €/m² a seconda di LOD e regolarità dell'edificio; edifici storici verso l'alto.",
 "Palazzo storico: HBIM con distacchi della malta e umidità mappati sulle pareti ha guidato la scelta di consolidamento senza demolizioni, risparmiando circa il 30% rispetto alla soluzione ipotizzata a tavolino.",
 "UNI 11337; linee guida HBIM per il patrimonio culturale (maturità varia, da verificare caso per caso).",
 "Da dichiarare sempre nel deliverable: data del rilievo, strumento, tolleranza di rappresentazione — l'as-built di oggi è il riferimento dei lavori di domani."),
s("Computo dal modello", "Quantità, computo e distinta base dal modello",
 "Dal modello BIM si estraggono le quantità (quantity take-off): volumi di muratura, superfici di intonaco, metri lineari di tubazione, numero di porte per tipo; i software italiani integrano i prezzari (Prezzario DEI, REGIONALI) per produrre il computo metrico estimativo quasi automatico.",
 "Le quantità derivano dalle proprietà degli oggetti: se il muro è modellato correttamente (lunghezza × altezza × spessore, intersezioni gestite), il computo conta da solo; attenzione ai 'trucchi grafici' (muri disegnati a pezzi, porte mancanti, falsi solai) che producono quantità sbagliate con apparente precisione.",
 "Gare d'appalto, contabilità lavori, controllo avanzamento, analisi prezzi unitari.",
 "Zero errori di trascrizione: finita la contabilità 'a mano' tra tavole, fogli Excel e Excel; il computo vive col modello e si aggiorna con esso.",
 "Il computo del modello sporco è falsamente preciso: la regola è 'sporco il modello = sporco il computo'; serve un controllo di qualità sulle quantità campione.",
 "Software con prezzari integrati: abbonamenti 50-150 €/mese (Primus, MC4, usBIM); il tempo risparmiato sulla contabilità di commessa ripaga l'abbonamento in genere entro il primo mese.",
 "Contabilità di un cantiere da 2 M€: il computo dal modello con stato avanzamento per oggetti ha ridotto la preparazione dei SAL da una settimana a mezza giornata, con contestazioni azzerate da parte dell'impresa.",
 "UNI 11891 (computo metrico); prezzari ufficiali (DEI, regionali).",
 "Prima di affidarsi alle quantità del modello: verifica campione manuale su 5-10 voci significative."),
s("BIM in cantiere", "BIM in cantiere: sequenze, sicurezza, qualità",
 "Il modello arriva in cantiere: sequenze di montaggio 4D (modello + tempi), verifica posizionamento con GPS/total station, controllo qualità su tablet (il modello come riferimento da confrontare col costruito), sicurezza con simulazione degli allestimenti.",
 "4D: si collegano gli elementi del modello al cronoprogramma (MS Project/P6) e si visualizza la costruzione; mock-up e riunioni di coordinamento col modello su tablet; rilievi di avanzamento confrontati col modello; i modelli di ponteggi e casseformi verificano gli interferenze PRIORA del montaggio.",
 "Grand cantieri, edilizia industriale, opere infrastrutturali, coordinamento HSE.",
 "Il cantiere vede prima di costruire: sequenze impossibili o pericolose emergono in riunione, non con la gru sul campo.",
 "In cantieri piccoli e artigianali il modello resta poco usato operativemente: serve sforzo di traduzione (tavole semplici dal modello) per non lasciare l'operaio senza documento utilizzabile.",
 "Tablet rugged per cantiere: 300-800 €; software di cantiere BIM: spesso incluso nell'ecosistema licenziato.",
 "Cantiere di un ponte: la sequenza 4D ha mostrato che il getto previsto in settimana 24 avrebbe richiesto il ponteggio già smontato in settimana 22: anticipato di 2 settimane il rifornimento, evitato 10 giorni di fermo macchina.",
 "DM 81/2008 (sicurezza, con l'obbligo della valutazione dei rischi da interferenze); UNI 11337.",
 "Il principio da insegnare: il modello in cantiere serve se qualcuno LO USA ogni giorno; altrimenti resta un esercizio accademico."),
s("BIM e gare", "Il BIM nelle gare pubbliche italiane",
 "Con il DM 312/2021 il BIM è obbligatorio per le commesse pubbliche oltre soglia progressiva (interamente dal 2025 per lavori > 1 M€): gare con requisiti informativi, consegna IFC, a volte premi di qualità informativa; le stazioni appaltanti pubblicano EIR e convenzioni.",
 "Il bando richiede: BEP preliminare in offerta, LOD per fase, consegna IFC e documentazione nativa, a volte CDE fornito dalla stazione; punteggi di qualità del progetto informativo; verifiche con validatori (es. check LOD, presenza Pset obbligatori).",
 "Appalti pubblici di lavori, servizi di progettazione, concessioni.",
 "Chi sa lavorare in BIM accede a gare dove chi non sa non può nemmeno partecipare: è barriera d'ingresso e vantaggio competitivo.",
 "Requisiti talvolta scritti da chi il BIM non lo pratica: EIR impossibili o contraddittori; va chiesta chiarezza in sede di offerta (a rischio di penali).",
 "Costo di conformità: tempo di redazione BEP e validazione (giorni/uomo per commessa); software validatori spesso gratuiti.",
 "Gara da 5 M€ con EIR LOD 300: lo studio che aveva automatizzato i controlli di qualità sul modello ha consegnato senza osservazioni alla verifica informatica, mentre 3 concorrenti su 8 furono ammessi con riserva.",
 "DM 312/2021; UNI 11337; linee guida ANCI/Consiglio Nazionale degli Architetti per l'attuazione BIM.",
 "Per il LLM: saper leggere un EIR e dire subito cosa è richiesto, a che LOD, in che formato e con quali penali è una competenza da 'laurea specialistica' nel settore pubblico."),
s("Digital twin", "Digital twin e gestione: il modello dopo il cantiere",
 "Il digital twin è il gemello digitale dell'edificio in esercizio: modello as-built + dati sensori (IoT) + storico manutentivo; alimenta la gestione energetica, la manutenzione predittiva, la gestione degli spazi.",
 "Sensori (temperatura, CO2, occupazione, energia) riversati su piattaforma; il modello as-built (LOD 500) è la mappa navigabile degli asset; ticket di manutenzione agganciati agli oggetti; integrazione con CAFM/IWMS e BMS; standard di scambio: IFC per la geometria, COBie (o Pset dedicate) per i dati di asset.",
 "Gestioni immobiliari grandi (ospedali, scuole, centri commerciali, gestori di patrimonio), facility management, energy manager.",
 "Manutenzione predittiva e meno guasti: si interviene sull'asset giusto al momento giusto; il modello è il 'cervello' dell'edificio per chi lo gestisce.",
 "Costo di presidio dati e sensoristica non banale; twin senza processo di gestione è un modello bello ma inutile.",
 "Sensoristica base: 5-30 €/m²; piattaforme twin: abbonamenti variabili (centinaia di euro/mese); ritorno documentato su grandi patrimoni (riduzione costi gestione 10-20%, stime settoriali).",
 "Ospedale con twin operativo: il localizzamento guasto da una valvola su modello + storico interventi ha dimezzato i tempi di ripristino del reparto rispetto alla ricerca 'a schemi cartacei'.",
 "UNI EN ISO 19650-3 (fase operativa); COBie (schema dati asset, buildingSMART).",
 "Il twin si costruisce PRIMA del cantiere (convenzioni sui dati) e si consegna DOPO: chi progetta pensando alla gestione vende un edificio migliore."),
]

README = """# CAD_BIM_PROGETTAZIONE_PACK — Progettazione digitale CAD/BIM a livello professionale

**Facoltà:** FACOLTA_TECNOLOGIA_E_COSTRUZIONE · **Livello:** L2 (intermedio-avanzato) · **Schede:** {n}

## Contenuto
Il metodo BIM completo: cosa è (processo, non software), LOD/LOIN e Information Requirements,
IFC e openBIM, ISO 19650 con CDE e convenzioni di denominazione, authoring tool
(Revit, Archicad, Allplan, Edificius, Tekla), federazione delle discipline e clash detection,
scan-to-BIM e HBIM, computo dal modello, BIM in cantiere (4D, sicurezza, qualità),
BIM nelle gare pubbliche italiane (DM 312/2021) e digital twin in fase di gestione.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi: categoria, nome, descrizione,
  tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: flussi di lavoro BIM end-to-end, lettura di EIR/BEP, consulenza sulla scelta
degli strumenti, gestione del passaggio CAD→BIM, coordinamento multidisciplinare.
Le stime di risparmio citate sono ordini di grandezza settoriali, da verificare per singola commessa.
""".format(n=len(DATA))

COURSE = """corso: "Progettazione digitale CAD e BIM"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
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
