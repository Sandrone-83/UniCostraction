# -*- coding: utf-8 -*-
"""Genera TEST_AURATRIX_1000_DOMANDE.md — 1000 domande su tutti i pack consegnati."""
import random, os

random.seed(42)
OUT_WS = r"C:\Users\alessandro\Documents\kimi\tasks\2026-09-26\15-14-07-e3d653af"
OUT_DESK = r"C:\Users\alessandro\Desktop"

# ============================================================
# EDILIZIA (sezione ampia)
# ============================================================

ED_STRUTTURE = [
("BASE","Quali sono le funzioni portanti di un edificio in muratura portante e come si differenziano da quelle di una struttura intelaiata?"),
("BASE","Spiega la differenza tra carichi permanenti, variabili e accidentali con due esempi per ciascun tipo."),
("BASE","Cosa e' il getto di calcestruzzo e quali controlli in cantiere sono obbligatori sulla sua esecuzione?"),
("BASE","Descrivi il ruolo dell'armatura in una trave in cemento armato e perche' il calcestruzzo da solo non e' sufficiente."),
("MEDIO","Qual e' la differenza tra trave continua e trave appoggiata in termini di momento flettente?"),
("MEDIO","Cosa si intende per 'duttilita' di una struttura e perche' e' fondamentale in zona sismica?"),
("MEDIO","Spiega il concetto di gerarchia delle resistenze nel progetto sismico di una struttura in cemento armato."),
("MEDIO","Quali sono i meccanismi di collasso piu' comuni di una muratura in caso di terremoto?"),
("MEDIO","Descrivi le differenze tra fondazioni superficiali (platea, travi rovesce) e fondazioni profonde (pali)."),
("MEDIO","Quando si scelgono i micropali e quali vantaggi offrono rispetto ai pali tradizionali?"),
("MEDIO","Cosa e' il coefficiente di sicurezza e come viene applicato in una verifica agli stati limite?"),
("MEDIO","Spiega la differenza tra verifica agli stati limite ultimi (SLU) e di esercizio (SLE)."),
("AVANZATO","Descrivi il comportamento di un pilastro in compressione eccentrica e quali verifiche sono richieste."),
("AVANZATO","Cosa sono i nodi beam-column e perche' rappresentano la zona piu' critica in un telaio sismico?"),
("AVANZATO","Spiega il contributo della carpenteria metallica nelle unioni: bullonate vs saldate, vantaggi e limiti."),
("AVANZATO","Cos'e' l'analisi pushover e quando viene utilizzata nella valutazione sismica di un edificio esistente?"),
("AVANZATO","Descrivi la tecnica dell'incamiciatura (jacketing) per il consolidamento di pilastri in cemento armato."),
("AVANZATO","Cosa sono gli isolatori sismici alla base e quali tipologie esistono (elastomerici, pendini, superfici scivolanti)?"),
("AVANZATO","Spiega la differenza tra smorzamento viscoso, isteretico e a frizione negli ammortizzatori sismici."),
("AVANZATO","Quali sono i criteri di fondazione in presenza di liquefazione del terreno e quali mitigazioni esistono?"),
("MEDIO","Cosa prevede la normativa sulle strutture esistenti in muratura riguardo alla qualificazione della muratura?"),
("MEDIO","Descrivi il ruolo delle catene e dei tiranti nella messa in sicurezza sismica di edifici storici in muratura."),
("BASE","Quali sono le principali prove distruttive e non distruttive sul calcestruzzo in opera (sclerometro, sonreb, carotaggio)?"),
("MEDIO","Spiega cosa e' la classe di esposizione di un calcestruzzo e come influenza resistenza e copriferro."),
("MEDIO","Quali sono le verifiche di deformabilita' di una trave in fase di esercizio (freccia, limitazione)?"),
("MEDIO","Cosa si intende per struttura a controventi e come lavora rispetto a un telaio?"),
("AVANZATO","Descrivi la modellazione di un edificio esistente in muratura con telai equivalenti: ipotesi e limiti."),
("MEDIO","Qual e' il ruolo del getto collaborante (soletta) nella resistenza flessionale di una trave metallica?"),
("MEDIO","Spiega il fenomeno dell'instabilita' euleriana di una colonna snella e le verifiche associate."),
("BASE","Cosa sono le malte di allettamento e quali caratteristiche devono avere per la posa di laterizi?"),
("MEDIO","Descrivi le verifiche principali di una parete in laterizio forato portante secondo le NTC."),
]

ED_IMPIANTI = [
("BASE","Quali sono i componenti principali di un impianto idrico-sanitario di un edificio residenziale?"),
("BASE","Spiega la differenza tra impianto idrico a montante visibile e a parete: vantaggi e svantaggi."),
("BASE","Cosa e' il collettore di scarico e quali regole segue per la pendenza e i raccordi?"),
("BASE","Descrivi il funzionamento di un bocchettone antiriflusso e quando e' obbligatorio."),
("MEDIO","Quali sono le differenze tra scarico civile, pluviale e fognario misto/separativo?"),
("MEDIO","Cosa prevede la normativa sui sistemi di trattamento delle acque reflue domestiche (IMOFF, fosse)?"),
("MEDIO","Spiega il principio di funzionamento di una pompa di calore aria-acqua e il suo coefficiente di prestazione (COP)."),
("MEDIO","Qual e' la differenza tra pompa di calore monoblocco e split e quando si preferisce l'una all'altra?"),
("MEDIO","Cosa e' una VMC (ventilazione meccanica controllata) e perche' e' obbligatoria nelle nuove costruzioni?"),
("MEDIO","Descrivi il bilancio termico invernale di un edificio: quali componenti entrano nel calcolo?"),
("MEDIO","Cosa sono i corpi illuminanti LED e quali parametri caratterizzano la qualita' della luce (CRI, temperatura colore)?"),
("MEDIO","Spiega la differenza tra quadro elettrico di distribuzione e quadro di derivazione secondo la norma CEI 64-8."),
("MEDIO","Cosa sono i salvavita (interruttore differenziale) e come funziona la protezione dai contatti indiretti?"),
("MEDIO","Descrivi il dimensionamento di una linea elettrica: corrente di impiego, caduta di tensione, protezione."),
("AVANZATO","Cosa e' un impianto fotovoltaico con accumulo e come si dimensiona la batteria rispetto ai consumi?"),
("AVANZATO","Spiega la differenza tra impianto in rete (grid connected) e impianto in isola e i vincoli normativi di ciascuno."),
("AVANZATO","Cosa e' la resa energetica globale (EPgl) e come si confronta con l'EPi e l'EPacs nella certificazione energetica?"),
("AVANZATO","Descrivi le differenze tra riscaldamento a pannelli radianti a pavimento e radiatori in termini di temperatura di mandata e comfort."),
("AVANZATO","Cosa e' una caldaia a condensazione e perche' conviene con impianti a bassa temperatura?"),
("AVANZATO","Spiega il funzionamento di un sistema di climatizzazione a pompa di calore multisplit con piu' unita' interne."),
("MEDIO","Quali sono i principali controlli edilizi sugli impianti (Direttiva Bollo/legge 10) e quali documenti vengono richiesti?"),
("MEDIO","Cosa e' la legge 10 e quali sono gli obblighi di progettazione energetica per nuovi edifici e ristrutturazioni?"),
("MEDIO","Descrivi il ruolo del certificatore energetico (EGE) e della certificazione energetica APE."),
("AVANZATO","Come si calcola la trasmittanza termica di una parete stratificata e cosa rappresenta?"),
("AVANZATO","Spiega il fenomeno del ponte termico e le strategie per ridurlo in cantiere."),
("AVANZATO","Cosa sono i sistemi di domotica KNX e come si struttura l'impianto (bus, attuatori, sensori)?"),
("MEDIO","Descrivi un impianto di raccolta acque meteoriche e i suoi usi previsti dalla normativa."),
("MEDIO","Quali accorgimenti per l'acustica si adottano negli impianti (silent block, diaframmi, velocita' dei fluidi)?"),
("AVANZATO","Spiega il principio di funzionamento di un pannello fotovoltaico e la differenza tra tecnologia mono e policristallina."),
("AVANZATO","Cosa e' l'energy manager e quali sono gli obblighi di diagnosi energetica per le grandi imprese (art. 8 D.Lgs 102/2014)?"),
("BASE","Quali dispositivi di protezione individuale sono obbligatori in cantiere secondo il D.Lgs 81/08?"),
("MEDIO","Cosa e' il POS (Piano Operativo di Sicurezza) e chi lo redige?"),
("MEDIO","Spiega la differenza tra CSP (Coordinatore Sicurezza in Progettazione) e CSE (Coordinatore in Esecuzione)."),
("MEDIO","Cosa prevede il DVR (Documento di Valutazione dei Rischi) e chi e' obbligato a redigerlo?"),
("MEDIO","Descrivi i controlli periodici obbligatori su ponteggi, gru e attrezzature di lavoro (ex DPR 177/2011)."),
("MEDIO","Cosa e' il piano di montaggio, uso e smontaggio del ponteggio (PMUS)?"),
("MEDIO","Quali sono i requisiti di formazione specifica aggiuntiva per i lavoratori in quota (D.Lgs 81/08)?"),
("MEDIO","Spiega cosa e' il fascicolo dell'opera e quali documenti contiene."),
("MEDIO","Cosa sono i dispositivi di protezione collettiva (DPC) e perche' hanno priorita' sui DPI?"),
("AVANZATO","Descrivi la gestione del rischio interferenze tra imprese in un cantiere con piu' subappaltatori."),
("AVANZATO","Cosa prevede la normativa sulle attivita' in ambienti confinati (esistenti) e le procedure di accesso?"),
]

ED_NORME = [
("BASE","Qual e' la differenza tra legge, decreto legislativo, decreto del Presidente del Consiglio e regolamento?"),
("BASE","Cosa sono le Norme Tecniche per le Costruzioni (NTC) e quale e' l'ultimo aggiornamento?"),
("MEDIO","Cosa prevede la legge 457/1978 per le opere abusive condonate e quali sono i limiti attuali?"),
("MEDIO","Spiega cosa e' il permesso di costruire e in cosa si differenzia dalla SCIA edilizia e dalla CILA."),
("MEDIO","Cosa e' la conformita' urbanistica e catastale di un immobile e a cosa serve nella compravendita?"),
("MEDIO","Descrivi la differenza tra residenziale e direzionale nella classificazione urbanistica."),
("MEDIO","Cosa sono i vincoli paesaggistici (Codice dei Beni Culturali) e quali autorizzazioni richiedono?"),
("MEDIO","Spiega il ruolo della Soprintendenza nei lavori su edifici vincolati."),
("MEDIO","Cosa e' la Direttiva Macchinari e cosa prevede la marcatura CE per le attrezzature?"),
("MEDIO","Quali sono gli obblighi del D.Lgs 81/08 per i cantieri con piu' imprese (POS, PSC, fascicolo)?"),
("MEDIO","Cosa prevede il regolamento europeo sulla protezione dei dati (GDPR) per un'impresa edile nella gestione dei clienti?"),
("MEDIO","Spiega la differenza tra SCIA antincendio e prevenzione incendi secondo il D.Lgs 139/2006."),
("MEDIO","Cosa e' il regolamento di attivita' antincendio e chi lo emette?"),
("MEDIO","Quali sono gli obblighi di agibilita' e in quale fase viene rilasciata?"),
("AVANZATO","Descrivi il ruolo del direttore dei lavori, del direttore dell'esecuzione del contratto e del progettista strutturale in un appalto pubblico."),
("AVANZATO","Cosa e' il Certificato di Regolare Esecuzione (CRE) e quando viene rilasciato?"),
("AVANZATO","Spiega la differenza tra collaudo statico e collaudo amministrativo- contabile nelle opere pubbliche."),
("MEDIO","Cosa prevede il Codice dei Contratti Pubblici (D.Lgs 36/2023) per l'affidamento dei lavori?"),
("MEDIO","Cosa e' il quadro economico di un'opera pubblica e da quali voci e' composto?"),
("MEDIO","Descrivi la SOA (certificazione di qualificazione) e le categorie di classifica (OG e OS)."),
("MEDIO","Cosa e' il subappalto, quali sono i limiti (30%) e le modalita' previste dal Codice dei Contratti?"),
("MEDIO","Spiega la responsabilita' penale per i reati edilizi (art. 44 e 81 DPR 380/2001): fino a quanti anni puo' arrivare?"),
("MEDIO","Cosa e' il Durc (Documento Unico di Regolarita' Contributiva) e quando e' obbligatorio?"),
("MEDIO","Descrivi gli obblighi di smaltimento dei rifiuti inerti in cantiere (registri carico/scarico, formaulario)."),
("MEDIO","Cosa sono le white list antimafia e in quali appalti sono richieste?"),
("MEDIO","Spiega la differenza tra edilizia libera e soggetta ad autorizzazione secondo il DPR 380/2001."),
("MEDIO","Cosa e' il catasto edilizio urbano e la rendita catastale: a cosa serve il Docfa?"),
("MEDIO","Descrivi gli obblighi di efficienza energetica negli edifici pubblici (art. 9 D.Lgs 192/2005)."),
("MEDIO","Cosa prevede la normativa sugli edifici in zona sismica per l'intervento di miglioramento sismico?"),
("MEDIO","Spiega il concetto di agibilita' in zona sismica: cosa cambia rispetto alla pratica abitativa dopo un evento?"),
]

ED_CONTO_TERMICO = [
("BASE","Cosa e' il Conto Termico e chi lo gestisce?"),
("BASE","Quali sono le due tipologie di interventi incentivati dal Conto Termico (trainanti e non trainanti)?"),
("MEDIO","Spiega cosa si intende per intervento trainante e quali esempi pratici rientrano in questa categoria."),
("MEDIO","Cosa sono gli edifici condominiali 'verticali' e quali soglie di risparmio energetico richiedono per accedere alle detrazioni?"),
("MEDIO","Descrivi la differenza tra detrazione fiscale al 50% (Ecobonus) e Conto Termico a fondo perduto: chi conviene cosa?"),
("MEDIO","Cosa e' la pratica EGE e chi puo' redigerla per accedere agli incentivi?"),
("MEDIO","Quali sono i limiti di spesa per pompa di calore e per isolamento termico previsti dagli incentivi?"),
("MEDIO","Spiega come funziona il meccanismo del credito d'imposta e come puo' essere ceduto."),
("MEDIO","Cosa sono i bonus 'trainati' ( finestre, schermature solari, caldaie a biomassa) e quali requisiti devono rispettare?"),
("MEDIO","Quali sono gli obblighi di tracciabilita' dei pagamenti per gli interventi incentivati (bonifico parlante)?"),
("MEDIO","Descrivi la differenza tra miglioramento energetico minimo (due classi) e riqualificazione energetica profonda (EPC)."),
("MEDIO","Cosa e' il Superbonus 110% (storicamente) e quali differenze presenta rispetto agli incentivi attuali?"),
("MEDIO","Spiega il ruolo dell'APE (Attestato di Prestazione Energetica) nella vendita e locazione di immobili."),
("MEDIO","Quali sono i requisiti minimi dell'involucro per un intervento di riqualificazione secondo la legge 10?"),
("AVANZATO","Descrivi il meccanismo del Superbonus condominiale con amministratore di condominio obbligato: cosa cambia per il deliberante?"),
("AVANZATO","Come si calcola il risparmio energetico previsivo per accedere al Conto Termico? Quali strumenti software sono richiesti?"),
("AVANZATO","Cosa sono i CERTIFICATI BIANCHI (TEE) e come funziona il meccanismo dell'obbligo di efficienza energetica?"),
("AVANZATO","Descrivi le regole per l'installazione di impianti solari termici e fotovoltaici in condominio secondo la riforma del condominio."),
("MEDIO","Quali sono le sanzioni per chi accede agli incentivi senza rispettare i requisiti (revoca, recupero, penalita')?"),
("MEDIO","Cosa e' la 'non spettanza' della detrazione e come si verifica in fase di audit GSE o AdE?"),
]

ED_ANTINCENDIO = [
("BASE","Cosa sono i mezzi di estinzione portatili (estintori) e quali classi di fuoco esistono (A, B, C, D, F)?"),
("BASE","Descrivi il percorso di esodo di un edificio e le sue caratteristiche minime (larghezza, lunghezza, illuminazione)."),
("MEDIO","Cosa sono i compartimenti antincendio e come si calcola la loro resistenza al fuoco (REI)?"),
("MEDIO","Spiega la differenza tra porte REI 60 e REI 120 e quando sono richieste."),
("MEDIO","Cosa e' il carico di fuoco specifico e come influenza la progettazione antincendio?"),
("MEDIO","Descrivi i sistemi di rivelazione incendio (centrali, rivelatori di fumo/fiamma/calore) e i requisiti di norma."),
("MEDIO","Cosa sono gli impianti di spegnimento a idranti e gli estintori a secco chimico: dove si collocano?"),
("MEDIO","Spiega il concetto di evacuabilita' e il tempo di evacuazione completo di un edificio."),
("MEDIO","Cosa sono i setti di compartimentazione e le barriere tagliafuoco orizzontali e verticali?"),
("MEDIO","Descrivi il ruolo del VVF (Vigili del Fuoco) nella SCIA antincendio e nei controlli in cantiere."),
("MEDIO","Cosa prevede la norma UNI 9174 per le classi di reazione al fuoco dei materiali (1, 2, 3)?"),
("MEDIO","Quali sono le misure di protezione passiva (vernici intumescenti) e come funzionano?"),
("AVANZATO","Descrivi la progettazione antincendio di un magazzino logistico: compartimenti, carichi di fuoco, presidi idrici."),
("AVANZATO","Cosa sono i sistemi di evacuazione fumi (VEV) e quando sono obbligatori?"),
("AVANZATO","Spiega la gestione antincendio degli edifici in conglomerato cementizio: fasci, pilastri, copriferro in funzione della resistenza al fuocco."),
]

ED_INFRA = [
("BASE","Quali sono le componenti principali di una strada (pianella, cordolo, manto di usura)?"),
("BASE","Descrivi la differenza tra infrastruttura stradale e sovrastruttura ferroviaria."),
("MEDIO","Cosa sono i sottoservizi di una strada (acqua, gas, fognatura, teleriscaldamento) e come si gestiscono in fase di progetto?"),
("MEDIO","Spiega il principio di funzionamento di una pavimentazione flessibile e semirigida: strati e funzioni."),
("MEDIO","Quali sono le verifiche di progetto di un muro di sostegno (stabilita' a ribaltamento, scorrimento, portata)?"),
("MEDIO","Descrivi il sistema di drenaggio di una strada: tombini, caditoie, canali di raccolta."),
("MEDIO","Cosa sono le paratie di sostegno degli scavi e quando sono obbligatorie?"),
("MEDIO","Spiega la differenza tra rilevato in terra naturale e rilevato in pietrame d'impronta."),
("MEDIO","Cosa sono i gabbioni e dove vengono tipicamente utilizzati?"),
("MEDIO","Descrivi le verifiche di stabilita' di una parete di scavo in terreni coesivi (calcolo del cedimento, tempo di apertura)."),
("AVANZATO","Come si progetta un massiccio scolmatore in un'opera idraulica e quali verifiche idrauliche servono?"),
("AVANZATO","Cosa sono le opere di presa e le paratoie: meccanismi e manutenzione."),
("AVANZATO","Descrivi le problematiche di progettazione di un sottopasso stradale (pozzetti di raccolta, impianti di sollevamento)."),
("AVANZATO","Cosa sono i muri di riva e le difese d'arma: criteri di dimensionamento idraulico."),
("MEDIO","Spiega la classificazione delle ferrovie e il binario (rotaie, traverse, massicciata)."),
]

ED_FALLIMENTI = [
("MEDIO","Descrivi il crollo del ponte Morandi (2018): cause strutturali e responsabilita'."),
("MEDIO","Cosa sono i crolli per 'instabilita' da carichi di punta' e quali casi storici li dimostrano?"),
("MEDIO","Spiega il disastro del Vajont (1963) e le lezioni per la geotecnica."),
("MEDIO","Descrivi il crollo del Terminal 2E dell'aeroporto Charles de Gaulle (2004): cause e responsabilita' progettuali."),
("MEDIO","Cosa sono le 'pietre d'inciampo' del calcestruzzo (segregazione, ritiro) e come si prevengono in cantiere?"),
("MEDIO","Spiega il fenomeno del 'corrosion of reinforcement' e le patologie tipiche degli edifici anni '60-'80."),
("MEDIO","Descrivi i danni da terremoto dell'Aquila (2009) e le lezioni sulle murature storiche."),
("MEDIO","Cosa e' il 'silos effect' nel crollo di strutture industriali e come si evita?"),
("MEDIO","Spiega la differenza tra crollo per carico eccessivo e crollo per fatica in una struttura metallica."),
("MEDIO","Cosa sono le 'ispezioni con droni' nelle verifiche strutturali e cosa possono rilevare?"),
("MEDIO","Descrivi il caso del crollo del cimitero monumentale di Staglieno: lezioni sulle strutture in calcestruzzo."),
("MEDIO","Cosa sono le patologie umide nelle murature storiche e le tecniche di risanamento."),
("MEDIO","Spiega il crollo dei ponti in muratura: cause e tecniche di consolidamento."),
("MEDIO","Cosa sono i distacchi di intonaco e cornicioni: cause e prevenzione in edifici storici."),
("MEDIO","Descrivi il 'danno da eccesso di vincolo' nelle strutture non progettate per spostamenti termici."),
]

ED_RESTAURO = [
("MEDIO","Cosa sono le tre opzioni del restauro (conservazione, ripristino, sostituzione) secondo la teoria moderna?"),
("MEDIO","Spiega la filosofia del restauro 'restauro critico' e del 'metodo storico-artistico' (Brandi, Boito)."),
("MEDIO","Cosa sono le 'sostanze di aggregazione' (calce, cemento, resine) nel restauro dei materiali lapidei?"),
("MEDIO","Descrivi le tecniche di pulitura di superfici storiche (acqua, micro-sabbiatura, laser) e i criteri di scelta."),
("MEDIO","Cosa e' il consolidamento delle murature con iniezione di malte e quali controlli sono previsti?"),
("MEDIO","Spiega la tecnica della scuci e cuci nei restauri murari e le indicazioni della normativa."),
("MEDIO","Cosa sono i cerchiature e le cuciature metalliche nella messa in sicurezza di edifici storici?"),
("MEDIO","Descrivi il restauro delle superfici affrescate: stacco, trasporto, fissaggio (metodo strappo)."),
("MEDIO","Cosa e' il restauro del legno: tecniche di consolidamento e sostituzione delle parti mancanti."),
("MEDIO","Spiega la normativa sui Beni Culturali (D.Lgs 42/2004) e l'iter autorizzativo per il restauro."),
("MEDIO","Cosa sono i restauri in cantiere temporaneo (smontaggio e rimontaggio) e quando si adottano?"),
("MEDIO","Descrivi la documentazione del cantiere di restauro: rilievi, schede di cantiere, report fotografici."),
("MEDIO","Cosa sono i materiali 'compatibili' nel restauro e perche' la compatibilita' e' un criterio guida?"),
("MEDIO","Spiega il ruolo dell'indagine preliminare (storia, tecnica, materia) prima di intervenire."),
("MEDIO","Cosa sono le tecniche di indagine non distruttive nel restauro (termografia, endoscopia, georadar)?"),
]

ED_MATERIALI = [
("BASE","Quali sono le principali classi di materiali da costruzione (laterizi, calcestruzzo, legno, acciaio, vetro)?"),
("BASE","Spiega la differenza tra malta di calce idraulica e di cemento: dove si usano."),
("MEDIO","Cosa sono i laterizi forati e come influenza la foratura la resistenza e l'isolamento termico?"),
("MEDIO","Descrivi le caratteristiche del calcestruzzo autocompattante e dove si preferisce al tradizionale."),
("MEDIO","Cosa e' il legno lamellare incollato (GLT) e quali vantaggi offre rispetto al legno massiccio?"),
("MEDIO","Spiega la differenza tra acciaio dolce e acciaio ad alta resistenza (S235, S355, S460)."),
("MEDIO","Cosa sono i materiali isolanti (lana di roccia, polistirene, sughero) e come si confrontano per conduttivita' e sostenibilita'?"),
("MEDIO","Descrivi il vetro stratificato e temperato: dove e' obbligatorio per sicurezza."),
("MEDIO","Cosa sono i materiali compositi (GFRP, CFRP) e dove trovano impiego nel consolidamento."),
("MEDIO","Spiega la 'prefabbricazione' in calcestruzzo: vantaggi e criticita' dei giunti."),
("MEDIO","Cosa sono i materiali 'a basso impatto ambientale' (calce, canapa, sughero) e dove si stanno diffondendo."),
("MEDIO","Descrivi le lastre cementizie e i sistemi a 'cappa' per facciate ventilate."),
("MEDIO","Cosa e' il 'cappotto termico' a soffitto e parete: materiali e spessori tipici."),
("MEDIO","Spiega la normativa sulla marcatura CE dei prodotti da costruzione (CPR 305/2011)."),
("MEDIO","Cosa sono i prodotti innovativi (bio-based, nanotecnologie) e come si collaudano in cantiere?"),
("MEDIO","Descrivi le problematiche di umidita' nei materiali porosi e le soluzioni (barriere al vapore)."),
("MEDIO","Cosa sono i rivestimenti 'flessibili' per facciate e le soluzioni per il rischio sismico?"),
("MEDIO","Spiega il 'footprint' ambientale dei materiali (LCA, EPD) e come incide nelle gare pubbliche."),
("MEDIO","Cosa sono i mattoni faccia a vista e le tecniche di posa con giunti di dilatazione."),
("MEDIO","Descrivi le lastre in pietra naturale per pavimentazioni e le verifiche di scivolosita' (DIN 51130)."),
]

ED_BIM = [
("BASE","Cosa e' il BIM (Building Information Modeling) e come si differenzia dal disegno CAD tradizionale?"),
("BASE","Cosa sono i LOD (Level of Development) e come si articolano (100-500)?"),
("MEDIO","Spiega cosa e' un IFC (Industry Foundation Classes) e a cosa serve nell'interoperabilita'."),
("MEDIO","Cosa e' un BCF (BIM Collaboration Format) e come si usa nella gestione delle interferenze?"),
("MEDIO","Descrivi il ruolo del BIM coordinator e del BIM manager in un progetto integrato."),
("MEDIO","Cosa sono i Common Data Environment (CDE) e le piattaforme (Autodesk, Bentley, openCDE)?"),
("MEDIO","Spiega la metodologia del 5D BIM (tempi e costi) e le basi di computo."),
("MEDIO","Cosa e' il modello federato e come si gestiscono le discipline (architettonico, strutturale, impiantistico)?"),
("MEDIO","Descrivi il BIM per le infrastrutture (IFC 4.3, inframodel, linear referencing)."),
("MEDIO","Cosa sono i GIS open source (QGIS) e come si integrano con il BIM per il territorio?"),
("MEDIO","Spiega il protocollo di collaborazione BIM (ISO 19650) e le informazioni di base (EIR, BEP)."),
("MEDIO","Cosa e' il 'scan to BIM' e le fasi della ricostruzione del modello da point cloud."),
("MEDIO","Descrivi le verifiche automatiche di regole (rule checking) sul modello BIM (SOL/VER)."),
("AVANZATO","Cosa e' il Digital Twin di un edificio e come si alimenta con i dati di sensoristica?"),
("AVANZATO","Spiega la gestione dell'information delivery cycle (IDM, MVD, esportazioni IFC) nelle commesse pubbliche."),
("AVANZATO","Cosa sono i LOD e LOIN (Level of Information Need) nella normativa ISO?"),
("AVANZATO","Descrivi l'uso del BIM nella gestione manutentiva (FM) e nel facility management."),
("MEDIO","Cosa e' la certificazione BIM di processo e di prodotto secondo la norma UNI 11337?"),
("MEDIO","Spiega come si gestiscono le varianti di progetto nel modello BIM (versioning, audit trail)."),
("MEDIO","Cosa sono i modelli parametrici e i linguaggi di scripting (Dynamo, Grasshopper, Python)?"),
]

ED_SPECIALISTICA = [
("MEDIO","Cosa sono le verifiche acustiche di un edificio (D.Lgs 42/2017): rumore da calpestio e aereo?"),
("MEDIO","Spiega la differenza tra isolamento acustico aereo e da calpestio e le soluzioni costruttive."),
("MEDIO","Cosa sono le verifiche di aeraulica e il ricambio d'aria negli edifici (UNI 10339)?"),
("MEDIO","Descrivi le verifiche di illuminazione naturale e artificiale secondo la norma UNI EN 12464."),
("MEDIO","Cosa e' la progettazione bioclimatica e i principi passivi (orientamento, schermatura, inerzia)?"),
("MEDIO","Spiega il concetto di 'edificio a energia quasi zero' (NZEB) e i requisiti UE."),
("MEDIO","Cosa sono le verifiche di accessibilita' agli edifici (Legge 13/1989 e D.M. 236/1989): barriere architettoniche?"),
("MEDIO","Descrivi la progettazione antisismica degli impianti (sismicitura dei quadri, vincoli delle reti)."),
("MEDIO","Cosa sono le verifiche di protezione dai fulmini (norma CEI EN 62305)?"),
("MEDIO","Spiega la gestione dell'amianto negli edifici: rilievo, bonifica e smaltimento."),
("MEDIO","Cosa sono i radon e le verifiche obbligatorie nelle nuove costruzioni (D.Lgs 28/2017)?"),
("MEDIO","Descrivi la progettazione di un edificio 'smart': sensoristica, automazione, gestione energetica."),
("MEDIO","Cosa e' la valutazione di sicurezza degli edifici scolastici e le verifiche sismiche obbligatorie?"),
("MEDIO","Spiega il 'building automation' e i protocolli di comunicazione (KNX, BACnet, Modbus)."),
("MEDIO","Cosa sono le verifiche di qualita' dell'aria indoor (VOC, CO2) e le soglie di legge."),
]

# ============================================================
# CAD LIBRARY
# ============================================================

CAD = [
("BASE","Quali sono le differenze principali tra i formati DWG, DXF, STEP, IGES, 3DS e 3DM?"),
("BASE","Perche' il formato STEP (.stp) e' considerato lo standard neutro per lo scambio di modelli 3D tra CAD diversi?"),
("BASE","Cosa si intende per 'kernel geometrico' in un software CAD (Open CASCADE, Parasolid, ACIS)?"),
("MEDIO","Descrivi la differenza tra modellazione solida B-Rep e modellazione mesh poligonale: quale formato usa ciascuna?"),
("MEDIO","Cosa sono i LOD (Level of Detail) nei modelli 3D e quando e' utile generarli?"),
("MEDIO","Spiega la differenza tra coordinate assolute e coordinate relative nella generazione di entita' DXF."),
("MEDIO","Cosa e' il layer (layer) in un disegno CAD e quali convenzioni di naming si usano in ambito edilizia?"),
("MEDIO","Descrivi le entita' base di un file DXF (LINE, LWPOLYLINE, CIRCLE, INSERT) e come sono strutturate in sezioni."),
("MEDIO","Cosa sono i blocchi (BLOCK/INSERT) in AutoCAD e quali vantaggi offrono per la ripetizione di elementi?"),
("MEDIO","Spiega il concetto di 'paper space' e 'model space' nella gestione delle tavole di stampa."),
("MEDIO","Cosa sono le unita' di misura nei file CAD e quali problemi nascono dal mismatch (metri vs millimetri)?"),
("MEDIO","Descrivi come si legge programmaticamente un file STEP con una libreria open source (PythonOCC, FreeCAD)."),
("MEDIO","Cosa sono i metadati associati a un file CAD e perche' sono importanti per l'indicizzazione di una libreria?"),
("MEDIO","Come si calcola il bounding box di un modello 3D e perche' e' utile nella catalogazione?"),
("MEDIO","Cosa sono i 'solidi manifold' e perche' i modelli non-manifold creano problemi di stampa 3D e analisi?"),
("AVANZATO","Descrivi la generazione parametrica di una trave in OpenSCAD o FreeCAD: quali parametri esporresti?"),
("AVANZATO","Come si converte un modello mesh (STL) in un solido B-Rep modificabile e quali sono i limiti?"),
("AVANZATO","Cosa sono le API di scripting di AutoCAD (AutoLISP, .NET) e un esempio di automazione utile in cantiere."),
("AVANZATO","Descrivi come si organizza una libreria CAD per l'addestramento di un LLM: metadati, classificazione, licenze."),
("AVANZATO","Cosa sono i formati di interscambio BIM (IFC) rispetto ai formati CAD nativi e perche' si usano entrambi?"),
("MEDIO","Quali criteri useresti per classificare 32.000 file CAD in categorie utili (tipologia edilizia, elemento strutturale, scala)?"),
("MEDIO","Descrivi come si estrae la geometria di una planimetria DXF per calcolare superfici di un locale."),
("MEDIO","Cosa e' l'esportazione 'SAT' (ACIS) e quando si usa?"),
("MEDIO","Come si gestisce la versione di un file CAD in un sistema di documentale di cantiere?"),
("MEDIO","Cosa sono i font e gli stili di quota (dimension styles) nella documentazione tecnica 2D?"),
("BASE","Perche' e' importante verificare la licenza di un file CAD prima di usarlo in un progetto commerciale?"),
("MEDIO","Cosa sono i modelli di riferimento esterni (XREF) e i rischi di rottura dei riferimenti?"),
("MEDIO","Descrivi il workflow di digitalizzazione di una tavola cartacea in CAD: vettorializzazione e pulizia."),
("MEDIO","Cosa sono le convenzioni di disegno tecnico (quote, scale, cartiglio) secondo le norme UNI ISO?"),
("MEDIO","Come si valida un file STEP generato automaticamente prima di consegnarlo a un cliente?"),
]

# ============================================================
# FONDAMENTI
# ============================================================

FOND = [
("BASE","Risolvi: 15% di 2.400 euro per il computo di una voce di lavorazione."),
("BASE","Calcola l'area di un triangolo con base 12 m e altezza 7,5 m."),
("BASE","Un muro e' lungo 8,4 m e alto 2,7 m: qual e' la superficie da intonacare?"),
("BASE","Converti 2,5 metri cubi in litri e spiega quando serve nel computo dei getti."),
("BASE","Calcola il perimetro di un lotto rettangolare di 25 m per 40 m."),
("BASE","Una scala ha alzata 17 cm e pedata 26 cm: verifica la regola di Blondel (2a+p)."),
("MEDIO","Risolvi la proporzione: se 3 operai impiegano 12 giorni, quanti giorni impiegano 5 operai (stesso lavoro)?"),
("MEDIO","Calcola il volume di un cilindro di diametro 30 cm e altezza 4 m (utile per pali e getti)."),
("MEDIO","Un terreno scende del 4% su 32 m di lunghezza: qual e' il dislivello?"),
("MEDIO","Calcola la pendenza percentuale di una rampa che copre 2,1 m di dislivello in 15 m di sviluppo orizzontale."),
("MEDIO","Il cemento ha densita' 2.400 kg/m3: quanto pesa un getto di 6 m3?"),
("MEDIO","Calcola l'ipotenusa di un tetto a falde con sporgenza orizzontale 4,2 m e pendenza 40 gradi."),
("MEDIO","Un investimento di 50.000 euro rende il 6% annuo: quanto dopo 5 anni (interesse composto)?"),
("MEDIO","In un reparto di 40 operai, il 15% ha il patentino per la gru: quanti operai lo hanno?"),
("MEDIO","Media dei valori 12, 18, 22, 30, 8 e calcolo della deviazione standard (spiegazione pratica)."),
("AVANZATO","Verifica la trigonometria: sin(30°), cos(45°), tan(60°) e applicazione al calcolo di un'asta inclinata."),
("AVANZATO","Calcola la distanza tra due punti di coordinate (3;7) e (11;13) nel piano."),
("AVANZATO","Una trave di 6 m ha un carico uniforme di 8 kN/m: calcola il momento massimo (qL^2/8)."),
("AVANZATO","Risolvi l'equazione 2x^2 - 10x + 12 = 0 e spiega il significato pratico delle due soluzioni."),
("AVANZATO","Calcola la probabilita' che estraendo una scheda da 50 (di cui 5 difettose) esca una scheda difettosa."),
("BASE","Spiega la differenza tra massa e peso e la formula P = m·g con un esempio in cantiere."),
("MEDIO","Cosa e' l'energia cinetica e calcolala per un mezzo di 1.200 kg a 20 m/s."),
("MEDIO","Spiega il principio di Archimede e applica al galleggiamento di un pontone in cantiere fluviale."),
("MEDIO","Cosa e' la pressione idrostatica e calcolala alla profondita' di 10 m (acqua dolce)."),
("MEDIO","Spiega il concetto di lavoro meccanico e calcola il lavoro per sollevare 500 kg di 12 m."),
("MEDIO","Cosa e' la trasmissione del calore per conduzione, convezione e irraggiamento con esempi edili."),
("MEDIO","Calcola il calore necessario per riscaldare 200 litri d'acqua da 15 a 45 gradi (c = 4.186 J/kg·K)."),
("AVANZATO","Spiega il ciclo termodinamico di una pompa di calore (evaporazione, compressione, condensazione, espansione)."),
("AVANZATO","Cosa e' il principio di conservazione dell'energia applicato a un edificio (bilancio termico)?"),
("AVANZATO","Spiega la legge di Ohm e applica al calcolo della corrente di un motore da 2.200 W a 230 V."),
("BASE","Chi e' stato Socrate e perche' il 'so di non sapere' e' una lezione per chi progetta?"),
("BASE","Spiega la differenza tra empirismo e razionalismo con un esempio applicato alla tecnica."),
("MEDIO","Cosa ha insegnato il metodo scientifico di Galileo e come si applica al debugging del software?"),
("MEDIO","Descrivi il pensiero sistemico: come si applica alla gestione di un cantiere complesso?"),
("MEDIO","Cosa significa 'razionalita' strumentale' e quali limiti ha nel decidere in azienda?"),
("MEDIO","Spiega il concetto di 'buona architettura' secondo Vitruvio (utilitas, firmitas, venustas) e la sua attualita'."),
("MEDIO","Cosa sono i bias cognitivi (conferma, ancoraggio) e come influenzano le stime di cantiere?"),
("MEDIO","Descrivi l'etica del costruttore: responsabilita' professionale verso sicurezza e qualita'."),
("MEDIO","Spiega il concetto di Kaizen (miglioramento continuo) e applica al cantiere."),
("MEDIO","Cosa e' la 'cassetta degli attrezzi' mentale (latticework di modelli di Munger) e perche' serve a un ingegnere?"),
("AVANZATO","Descrivi il ragionamento per principi first principles e applicalo al calcolo di un preventivo."),
("AVANZATO","Cosa sono i paradossi della scelta (nudge di Thaler) e come si applicano alla vendita edile?"),
("AVANZATO","Spiega la filosofia stoica applicata alla gestione dello stress in cantiere."),
("AVANZATO","Cosa e' il pensiero laterale (de Bono) e come si applica alla risoluzione di interferenze in cantiere?"),
("AVANZATO","Descrivi il concetto di 'antifragilita' (Taleb) e applicalo alla gestione dei rischi d'impresa."),
("AVANZATO","Cosa significa 'epistemologia' e perche' la conoscenza tecnica va sempre verificata?"),
]

# ============================================================
# STORIA
# ============================================================

STORIA = [
("BASE","Quali sono i tre ordini dell'architettura greca classica e le caratteristiche distintive di ciascuno?"),
("BASE","Descrivi il Pantheon di Roma: struttura, cupola e perche' e' un capolavoro ingegneristico."),
("BASE","Cosa sono le archi e le volte romane e perche' hanno rivoluzionato la costruzione?"),
("MEDIO","Descrivi le caratteristiche dell'architettura romanica e i principali esempi italiani."),
("MEDIO","Cosa distingue il gotico dalle strutture precedenti: archi rampanti, volte a crociera, vetrate?"),
("MEDIO","Descrivi il Duomo di Milano e le innovazioni strutturali della sua costruzione."),
("MEDIO","Cosa e' il Rinascimento architettonico e quali sono le opere chiave di Brunelleschi e Alberti?"),
("MEDIO","Descrivi la Basilica di San Pietro e il contributo di Bramante, Michelangelo e Bernini."),
("MEDIO","Cosa caratterizza il Barocco (Bernini, Borromini) rispetto al Rinascimento?"),
("MEDIO","Spiega le teorie di Palladio (Villa Rotonda, I Quattro Libri) e la loro influenza sul neoclassicismo."),
("MEDIO","Cosa e' il neoclassicismo (Canova, David) e quali edifici ne sono esempi in Italia?"),
("MEDIO","Descrivi la rivoluzione industriale e l'impatto sulle costruzioni (ferro, vetro, cemento)."),
("MEDIO","Cosa sono le case a ballatoio e come si sono sviluppate nei centri storici italiani?"),
("MEDIO","Descrivi l'evoluzione del cemento armato: dal ponte di Hennebique alle prime applicazioni in Italia."),
("MEDIO","Cosa e' il razionalismo italiano (Gruppo 7, Terragni) e le opere simbolo (Casa del Fascio)."),
("MEDIO","Descrivi il movimento moderno (Le Corbusier, Bauhaus, Wright) e i cinque punti dell'architettura."),
("MEDIO","Cosa sono le utopie urbanistiche del Novecento (garden city, citta' funzionale)?"),
("MEDIO","Descrivi la ricostruzione post-bellica in Italia e il dibattito tra centro storico e periferia."),
("MEDIO","Cosa e' il brutalismo e quali edifici ne sono esempi in Italia e nel mondo?"),
("MEDIO","Descrivi l'evoluzione del grattacielo: dal Home Insurance Building al Burj Khalifa."),
("MEDIO","Cosa sono le smart cities e come si collegano all'evoluzione tecnologica dell'edilizia?"),
("MEDIO","Descrivi il postmodernismo architettonico (Venturi, Gehry) e la critica al moderno."),
("MEDIO","Cosa e' la bioarchitettura e come si e' sviluppata dagli anni '70 a oggi?"),
("MEDIO","Descrivi l'evoluzione dell'ingegneria strutturale di Ponti e viadotti italiani dal dopoguerra."),
("MEDIO","Cosa sono le infrastrutture di Grande Viabilita' (autostrade, ferrovie ad alta velocita') in Italia?"),
("MEDIO","Descrivi l'evoluzione dell'edilizia residenziale italiana dagli anni '50 (boom economico) agli anni '80."),
("MEDIO","Cosa sono i centri direzionali moderni (Centro Direzionale di Napoli) e la critica urbanistica."),
("MEDIO","Descrivi il movimento del restauro in Italia tra Ottocento e Novecento (Viollet-le-Duc vs Ruskin)."),
("MEDIO","Cosa e' l'architettura sostenibile e i concorsi/expo che l'hanno diffusa?"),
("MEDIO","Descrivi l'Expo 2015 di Milano e il tema 'nutrire il pianeta' nelle scelte architettoniche."),
("AVANZATO","Confronta l'approccio strutturale di Nervi, Morandi e Musmeci: ricerca formale e calcolo."),
("AVANZATO","Cosa sono le 'megastrutture' del Novecento ( metabolismo giapponese, Archigram) e perche' sono fallite?"),
("AVANZATO","Descrivi l'evoluzione delle facciate continue (curtain wall) e la rivoluzione del vetro strutturale."),
("AVANZATO","Confronta la ricostruzione del terremoto del Belice (1968), Friuli (1976) e L'Aquila (2009): cosa e' cambiato?"),
("AVANZATO","Cosa sono i masterplan contemporanei e come si confrontano con le citta' storiche (critica di Koolhaas)?"),
("MEDIO","Descrivi l'evoluzione dei materiali da costruzione nella storia: pietra, mattone, ferro, cemento, compositi."),
("MEDIO","Cosa e' l'urbanistica moderna (CIAM, Carta di Atene) e la critica di Jane Jacobs?"),
("MEDIO","Descrivi il concetto di 'spazio publico' nella storia dell'urbanistica occidentale."),
("MEDIO","Cosa sono i siti UNESCO in Italia e il criterio di conservazione?"),
("MEDIO","Descrivi l'evoluzione della legislazione edilizia italiana dal 1865 al DPR 380/2001."),
("MEDIO","Cosa e' il liberty (floreale) italiano e gli esempi principali (Casa Galimberti a Milano)?"),
("MEDIO","Descrivi l'architettura fascista e il dibattito sulla conservazione di quei beni."),
("MEDIO","Cosa sono le 'periferie' italiane e le politiche di rigenerazione urbana?"),
("AVANZATO","Descrivi l'evoluzione del concetto di 'museo' architettonico (dal museo-tempio al museo-macchina)."),
("AVANZATO","Cosa sono le architetture 'parametriche' contemporanee e la critica estetica e costruttiva."),
("AVANZATO","Confronta il rinnovo urbano di Bilbao (effetto Guggenheim) con le rigenerazioni italiane."),
("MEDIO","Descrivi la storia del Ponte Vecchio e delle infrastrutture storiche fiorentine."),
("MEDIO","Cosa sono i castelli medievali e l'evoluzione delle tecniche fortificatorie?"),
("MEDIO","Descrivi l'evoluzione della villa romana, rinascimentale e veneta e il rapporto con il paesaggio."),
("MEDIO","Cosa e' l'architettura ottomana e i ponti di Sinan come capolavori strutturali?"),
("MEDIO","Descrivi l'evoluzione dei teatri storici (Scala, San Carlo) e le verifiche strutturali recenti."),
("MEDIO","Cosa sono le citta' giardino di Letchworth e Welwyn e il loro influsso sull'urbanistica?"),
("MEDIO","Descrivi l'architettura di Antoni Gaudi e la ricerca strutturale della Sagrada Familia."),
("MEDIO","Cosa sono i grattacieli in legno moderni e la sfida normativa alla loro diffusione?"),
("MEDIO","Descrivi l'evoluzione dell'illuminazione urbana storica (gas, elettrico, LED) e l'impatto sulla citta'."),
]

# ============================================================
# ITALIA SISTEMA
# ============================================================

ITALIA = [
("BASE","Quali sono i 12 principi fondamentali della Costituzione italiana (artt. 1-12)?"),
("BASE","Cosa prevede l'articolo 41 della Costituzione sulla liberta' di iniziativa economica privata?"),
("BASE","Descrivi la separazione dei poteri in Italia (legislativo, esecutivo, giudiziario)."),
("MEDIO","Cosa e' la forma di governo parlamentare e come funziona il rapporto di fiducia?"),
("MEDIO","Descrivi il procedimento legislativo ordinario e il ruolo del Presidente della Repubblica."),
("MEDIO","Cosa sono i decreti legge e i decreti legislativi e quali sono i limiti?"),
("MEDIO","Descrivi la giustizia in Italia: giudice ordinario, amministrativo e costituzionale (Corte Costituzionale)."),
("MEDIO","Cosa prevede l'articolo 32 della Costituzione sulla tutela della salute?"),
("MEDIO","Cosa sono le Regioni a statuto ordinario e speciale e le loro competenze in materia edilizia?"),
("MEDIO","Descrivi la riparto di competenze tra Stato, Regioni e Comuni in materia di urbanistica."),
("MEDIO","Cosa e' il parametro di rappresentanza della Corte Costituzionale e come vengono nominati i giudici?"),
("MEDIO","Descrivi i diritti e doveri dei cittadini italiani secondo la Costituzione (voto, istruzione, lavoro)."),
("MEDIO","Cosa prevede l'articolo 42 sulla proprieta' privata e la sua funzione sociale?"),
("MEDIO","Descrivi la tutela costituzionale del lavoro e dei lavoratori (art. 35-40)."),
("AVANZATO","Cosa sono i conflitti di attribuzione e le questioni di legittimita' costituzionale?"),
("AVANZATO","Descrivi la revisione costituzionale (legge costituzionale) e la differenza con le leggi di riforma costituzionale."),
("AVANZATO","Cosa prevede l'articolo 81 sulla finanza pubblica e l'equilibrio di bilancio?"),
("AVANZATO","Descrivi le fonti del diritto in Italia e la gerarchia (Costituzione, leggi, regolamenti, usi)."),
("MEDIO","Cosa e' il fisco e quali sono le principali imposte dirette (IRPEF, IRES, IRAP) e indirette (IVA, imposte di registro)?"),
("MEDIO","Quali sono le aliquote IRPEF 2026 e come funzionano gli scaglioni?"),
("MEDIO","Descrivi la differenza tra deduzione e detrazione fiscale con esempi edili (110%, ristrutturazioni)."),
("MEDIO","Cosa e' l'IVA e quali sono le aliquote previste in Italia (22%, 10%, 4%)?"),
("MEDIO","Cosa e' il regime forfettario e chi puo' accedervi (limite 85.000 euro)?"),
("MEDIO","Descrivi il bilancio dello Stato: entrate correnti, in conto capitale, spesa pubblica."),
("MEDIO","Cosa sono i tributi locali (IMU, TARI, TASI/IMU seconda casa) e chi li gestisce?"),
("MEDIO","Descrivi il meccanismo delle detrazioni fiscali per ristrutturazioni (50%) e le modalita' di fruizione."),
("MEDIO","Cosa e' il Modello 730 e il Reddito di Cittadinanza (sostituito dall'Assegno Unico)?"),
("MEDIO","Descrivi l'acconto e il saldo delle imposte sui redditi: scadenze e calcolo."),
("MEDIO","Cosa sono gli ISA (indici sintetici di affidabilita') e come influenzano i controlli fiscali?"),
("MEDIO","Descrivi il reverse charge nel settore edile e come funziona la fatturazione tra imprese."),
("AVANZATO","Cosa e' la tassazione per competenza vs per cassa e quando si applica ai lavori edili?"),
("AVANZATO","Descrivi il rilievo dell'Iva nei cantieri di lunga durata (beni significativi e prestazioni complesse)."),
("AVANZATO","Cosa sono i versamenti F24 e come si compensano i crediti fiscali?"),
("AVANZATO","Descrivi la disciplina della fatturazione elettronica e il sistema di interscambio (SdI)."),
("MEDIO","Quali sono le principali scadenze fiscali annue (acconti, saldi, dichiarazioni)?"),
("MEDIO","Cosa sono le sanzioni tributarie (interessi, sanzioni, ravvedimento operoso) e come funzionano?"),
("MEDIO","Descrivi il concordato fiscale e le opzioni di adesione disponibili per le imprese."),
("MEDIO","Cosa e' la dichiarazione IVA e le regole di detraibilita' per un'impresa edile?"),
("MEDIO","Descrivi l'imposizione sostitutiva del forfettario e le voci escluse dal calcolo."),
("MEDIO","Cosa sono i contributi INPS per artigiani e commercianti e come si calcolano?"),
("MEDIO","Descrivi il sistema delle Casse Edili e il contributo cantiere per i lavoratori edili."),
("MEDIO","Cosa e' il Durc e come si richiede in via telematica?"),
("MEDIO","Descrivi le scadenze contributive mensili e la gestione dei maggiorati in edilizia."),
("MEDIO","Cosa sono i versamenti previdenziali per le imprese con lavoratori in somministrazione?"),
("MEDIO","Descrivi il sistema italiano della rappresentanza sindacale e il CCNL edilizia."),
("MEDIO","Cosa sono le buste paga, le trattenute e i contributi a carico del lavoratore e del datore?"),
("MEDIO","Descrivi l'IRAP e le aliquote per le imprese edili."),
("MEDIO","Cosa sono i crediti d'imposta e come si possono cedere a terzi?"),
("MEDIO","Descrivi la patente a punti e il sistema sanzionatorio amministrativo italiano."),
("MEDIO","Cosa e' la Camera di Commercio e le sue funzioni per le imprese?"),
("MEDIO","Descrivi il sistema bancario italiano e l'accesso al credito per le PMI edili."),
("MEDIO","Cosa sono le garanzie pubbliche (SACE, SIMEST) per le imprese che esportano?"),
("MEDIO","Descrivi l'ordinamento delle autonomie locali: Comuni, Province, Citta' metropolitane."),
("MEDIO","Cosa sono i regimi di aiuto di Stato e le notifiche alla UE per le imprese?"),
("MEDIO","Descrivi il sistema scolastico e universitario italiano e i titoli per ingegneri e architetti."),
("MEDIO","Cosa sono gli ordini professionali (CNPI, CNPIA) e l'Albo per ingegneri e architetti?"),
("MEDIO","Descrivi la tutela della concorrenza in Italia (AGCM, autorita' garante)."),
("MEDIO","Cosa e' il diritto societario: forma SRL, SPA, societa' a responsabilita' limitata unipersonale?"),
("MEDIO","Descrivi le procedure concorsuali (fallimento, concordato, liquidazione giudiziale) per un'impresa edile."),
("MEDIO","Cosa sono i contratti di appalto nel codice civile e le differenze con il contratto di lavoro subordinato?"),
("MEDIO","Descrivi la responsabilita' civile dell'imprenditore edile verso terzi e committenti."),
("MEDIO","Cosa e' la polizza decennale RC costruttori e quando e' obbligatoria?"),
("MEDIO","Descrivi il sistema assicurativo italiano e le polizze obbligatorie per i cantieri (RCA, infortuni, all risks)."),
("MEDIO","Cosa sono i trust e le garanzie reali (ipoteca, pegno) nel credito edile?"),
("MEDIO","Descrivi il diritto d'autore e la protezione dei progetti architettonici."),
("MEDIO","Cosa e' il diritto del lavoro: ferie, permessi, malattia, licenziamento nel settore edile?"),
("MEDIO","Descrivi la disciplina dei subappalti e delle societa' di scopo (ATI) nei lavori pubblici."),
]

# ============================================================
# DIGITALE MARKETING PACK
# ============================================================

MKT = [
("BASE","Cosa e' il posizionamento di un'impresa edile e perche' deve essere scelto prima del nome e del logo?"),
("BASE","Quali sono le tre componenti fondamentali della brand identity (nome, logo, promessa)?"),
("BASE","Cosa e' la UIBM e come si registra un marchio in Italia?"),
("MEDIO","Quali classi NCL sceglieresti per registrare il marchio di un'impresa edile e perche'?"),
("MEDIO","Descrivi le differenze tra marchio figurativo, denominativo e misto."),
("MEDIO","Cosa sono i KPI di marketing e perche' 'richieste al mese' batte 'numero di like'?"),
("MEDIO","Quale budget di marketing consiglieresti a un'impresa edile con 500.000 euro di fatturato e perche'?"),
("MEDIO","Descrivi la differenza tra CPL (cost per lead) e CPA (cost per acquisizione) in una campagna Meta Ads."),
("MEDIO","Cosa sono i Local Service Ads di Google e perche' sono particolarmente adatti alle imprese edili?"),
("MEDIO","Descrivi la formula di un reel efficace per un'impresa edile (hook, trasformazione, prova, CTA)."),
("MEDIO","Quali sono i contenuti che funzionano meglio su Instagram per un'impresa edile e perche'?"),
("MEDIO","Come si ottimizza il Google Business Profile di un'impresa edile (categorie, foto, recensioni)?"),
("MEDIO","Descrivi la strategia SEO locale: cosa ottimizzare sul sito e cosa fuori dal sito."),
("MEDIO","Cosa sono le keyword a coda lunga e perche' convertono meglio di quelle generiche nell'edilizia?"),
("MEDIO","Descrivi il funnel di vendita edile: attrazione, interesse, decisione, fidelizzazione."),
("MEDIO","Perche' il preventivo a tre livelli (base/comfort/premium) e' piu' efficace del preventivo singolo?"),
("MEDIO","Cosa sono i sopraggiunti e come vanno gestiti per iscritto secondo le best practice di pricing?"),
("MEDIO","Descrivi come chiedere una recensione Google a un cliente soddisfatto senza risultare invadente."),
("MEDIO","Cosa e' l'email marketing di nutrizione e quali sono i contenuti di una newsletter edile efficace?"),
("MEDIO","Descrivi il personal branding del titolare: cosa raccontare e quali errori evitare."),
("MEDIO","Cosa sono gli agenti AI per un'impresa edile e come si integrano con WhatsApp o il sito (RAG sui listini)?"),
("MEDIO","Descrivi come si misura il ROI del marketing edile: quali dati raccogliere a ogni richiesta."),
("MEDIO","Perche' il marketing per la ristrutturazione differisce da quello per la nuova costruzione?"),
("MEDIO","Descrivi una strategia di partnership per un'impresa edile: architetti, rivenditori, amministratori di condominio."),
("MEDIO","Cosa sono le fiere e gli open house come strumento di marketing edile?"),
("MEDIO","Descrivi le differenze di marketing B2B per un general contractor (prequalifica, SOA, gare)."),
("MEDIO","Cosa e' il passaparola digitale e come si costruisce nei gruppi locali (con la privacy rispettata)?"),
("MEDIO","Descrivi le policy pubblicitarie: cosa non si puo' promettere in una pubblicita' edilizia (Codice del Consumo)."),
("MEDIO","Cosa sono i 15 errori tipici di marketing edile e quali sono i tre peggiori?"),
("AVANZATO","Descrivi come struttureresti una campagna Google Ads per 'ristrutturazione bagno + citta'': keyword, annunci, landing."),
("AVANZATO","Cosa e' il marketing automation e come si applica al follow-up dei preventivi (sequenza a 3 email)?"),
("AVANZATO","Descrivi come valuteresti il canale piu' redditizio per un'impresa edile con tre mesi di dati."),
("AVANZATO","Cosa sono i casi studio nel marketing edile e come si documentano (prima/dopo, dati, testimonianza)?"),
("AVANZATO","Descrivi come si gestisce una recensione negativa pubblica secondo le best practice."),
("MEDIO","Cosa e' il binary system e come rappresenta numeri e caratteri (ASCII/Unicode)?"),
("MEDIO","Descrivi la gerarchia hardware: CPU, RAM, disco, cache — ruolo di ciascuno."),
("MEDIO","Cosa e' un sistema operativo e quali sono le sue funzioni principali (processi, memoria, file system)?"),
("MEDIO","Spiega la differenza tra compilatore e interprete con esempi di linguaggi."),
("MEDIO","Cosa sono i paradigmi di programmazione (imperativo, OOP, funzionale, logico)?"),
("MEDIO","Descrivi la complessita' O grande: cosa significa O(n), O(n log n), O(n^2) con esempi pratici."),
("MEDIO","Cosa sono le strutture dati fondamentali (array, lista, hash map, pila, coda, albero)?"),
("MEDIO","Descrivi come funziona internet: cosa succede quando digiti un URL (DNS, TCP, HTTP)."),
("MEDIO","Cosa e' un'API REST e quali sono le convenzioni (verbi HTTP, status code, JSON)?"),
("MEDIO","Spiega la differenza tra database SQL e NoSQL con esempi di casi d'uso."),
("MEDIO","Cosa e' Git e come funziona il workflow (clone, commit, push, pull request)?"),
("MEDIO","Descrivi cosa e' il cloud computing (IaaS, PaaS, SaaS) con esempi."),
("MEDIO","Cosa sono CI/CD e DevOps in sintesi?"),
("MEDIO","Descrivi la metodologia Agile: sprint, backlog, standup, retrospettiva."),
("MEDIO","Cosa e' il no-code e quando conviene rispetto allo sviluppo custom?"),
("MEDIO","Cosa e' l'AI coding e come si integra un LLM in un'applicazione via API?"),
("MEDIO","Descrivi il concetto di RAG (retrieval augmented generation) in due paragrafi."),
("MEDIO","Cosa sono gli agenti AI e come usano il function calling per agire sui sistemi reali?"),
("MEDIO","Descrivi le basi della sicurezza informatica: autenticazione, autorizzazione, crittografia."),
("MEDIO","Cosa e' il GDPR in sintesi e quali obblighi ha chi sviluppa software che tratta dati personali?"),
("BASE","Cosa sono le variabili, i cicli e le funzioni in un linguaggio di programmazione?"),
("BASE","Spiega cosa e' un bug e cosa significa 'debugging'."),
("MEDIO","Descrivi la differenza tra sito statico, dinamico e single page application (SPA)."),
("MEDIO","Cosa e' un database relazionale e cosa sono le chiavi primarie ed esterne?"),
("MEDIO","Descrivi come si scrive una query SQL che unisce due tabelle (JOIN) con esempio."),
("MEDIO","Cosa e' un webhook e come si differenzia da una API polling?"),
("MEDIO","Descrivi cosa e' Docker e perche' ha rivoluzionato il deployment."),
("MEDIO","Cosa sono i linguaggi front-end (HTML, CSS, JavaScript) e back-end?"),
("MEDIO","Descrivi cosa e' un framework (React, Django, Laravel) e perche' si usa."),
("MEDIO","Cosa e' il responsive design e come si ottiene (media query, layout fluidi)?"),
("MEDIO","Descrivi la differenza tra autenticazione e autorizzazione con esempi."),
("MEDIO","Cosa sono le variabili d'ambiente e perche' non si mettono segreti nel codice?"),
("MEDIO","Descrivi cosa e' un dominio, un DNS e un hosting."),
("MEDIO","Cosa e' HTTPS e perche' il certificato SSL e' obbligatorio?"),
("MEDIO","Descrivi le basi dell'accessibilita' web (WCAG): contrasto, alt text, tastiera."),
("MEDIO","Cosa sono le PWA (progressive web app) e cosa permettono rispetto a un sito normale?"),
("MEDIO","Descrivi cosa e' un CMS (WordPress) e quando conviene rispetto a un sito custom."),
("MEDIO","Cosa sono le API rate limit e perche' esistono?"),
("MEDIO","Descrivi come si protegge un form web da spam (honeypot, captcha, validazione server)."),
("MEDIO","Cosa e' il lazy loading e perche' migliora le performance?"),
("MEDIO","Descrivi la struttura di un'app mobile nativa vs cross-platform (Flutter, React Native)."),
("MEDIO","Cosa sono gli store di app (Google Play, App Store) e i loro requisiti di pubblicazione?"),
("MEDIO","Descrivi come si pubblica un sito web (build, deploy su Vercel/Netlify, DNS)."),
("MEDIO","Cosa sono le analitiche web (GA4) e cosa si misura (eventi, conversioni)?"),
("AVANZATO","Descrivi l'architettura di un configuratore preventivi online: form, logica di calcolo, lead capture."),
("AVANZATO","Cosa sono i design pattern MVC e dove si applicano?"),
("AVANZATO","Descrivi come integreresti un LLM in un gestionale di cantiere (API, RAG, guardie)."),
("AVANZATO","Cosa e' il testing e perche' si scrivono test unitari prima o subito dopo il codice?"),
("AVANZATO","Descrivi come struttureresti un database per un'app di gestione cantieri (entita' e relazioni)."),
("AVANZATO","Cosa sono le mutation testing e cosa misurano rispetto alla coverage?"),
("AVANZATO","Descrivi l'architettura di un'applicazione che usa coda di messaggi (producer, consumer, DLQ)."),
("AVANZATO","Cosa sono i container e Kubernetes in sintesi: quando servono davvero?"),
("AVANZATO","Descrivi come funziona una cache e i pattern (cache-aside, write-through) con esempi."),
("AVANZATO","Cosa e' il load balancing e quali strategie esistono?"),
("AVANZATO","Descrivi il disaster recovery: RPO, RTO e la regola 3-2-1 dei backup."),
("AVANZATO","Cosa sono i microservizi e quando NON usarli?"),
("AVANZATO","Descrivi come si protegge un'API (autenticazione JWT, rate limiting, validazione input)."),
("AVANZATO","Cosa e' l'osservabilita' (log, metriche, tracing) e perche' e' critica in produzione?"),
("MEDIO","Descrivi come funziona la posta elettronica (SMTP, POP3, IMAP) in sintesi."),
("MEDIO","Cosa e' il SEO tecnico (sitemap, robots.txt, meta tag, velocita')?"),
("MEDIO","Descrivi cosa e' un algoritmo di ricerca binaria e quando si usa."),
("MEDIO","Cosa sono i graph database (Neo4j) e quando conviene usarli?"),
("MEDIO","Descrivi cosa e' WebAssembly e cosa permette."),
("MEDIO","Cosa sono le WebSocket e quando si usano rispetto a HTTP?"),
]

# ============================================================
# CODING MASTER PACK 1
# ============================================================

COD1_BEST = [
("BASE","Cosa significa 'codice pulito' e perche' i nomi sono la prima forma di documentazione?"),
("BASE","Perche' le funzioni dovrebbero fare una sola cosa? Dai un criterio pratico per riconoscere quando dividerle."),
("MEDIO","Descrivi il principio DRY e quando la duplicazione e' accettabile (la regola del tre)."),
("MEDIO","Cosa sono le guard clauses e perche' riducono il nesting?"),
("MEDIO","Descrivi il refactoring 'estrai funzione' e quando applicarlo."),
("MEDIO","Cosa sono i code smell (feature envy, dati sparsi, funzione lunga) e come si riconoscono?"),
("MEDIO","Descrivi le buone pratiche di code review: cosa guardare prima e come formulare i commenti."),
("MEDIO","Cosa sono i livelli di severita' in review (blocker, suggestion, nit) e perche' distinguerli?"),
("MEDIO","Descrivi la gestione errori professionale: errori recuperabili vs bug, mai except pass."),
("MEDIO","Cosa sono i log strutturati e perche' non si mettono dati sensibili nei log?"),
("MEDIO","Descrivi cosa deve contenere un README di progetto per essere utile."),
("MEDIO","Cos'e' il technical debt e come si gestisce (misura, budget, boy scout rule)?"),
("MEDIO","Descrivi il refactoring del 'sostituisci condizionale con polimorfismo' con un esempio."),
("AVANZATO","Cosa sono gli ADR (Architecture Decision Records) e perche' scriverli?"),
("AVANZATO","Descrivi il ciclo di refactoring sicuro: piccoli passi, test verdi, commit frequenti."),
]

COD1_ALG = [
("BASE","Cos'e' la complessita' O grande e perche' O(n^2) su un milione di elementi e' inaccettabile?"),
("BASE","Descrivi la ricerca binaria e il suo requisito fondamentale."),
("MEDIO","Cosa sono le hash map e perche' cambiano O(n) in O(1)?"),
("MEDIO","Descrivi heap, pila e coda: operazioni e casi d'uso."),
("MEDIO","Cos'e' un trie e dove si usa (autocomplete, prefissi)?"),
("MEDIO","Descrivi BFS e DFS: differenze e quando usarli."),
("MEDIO","Cos'e' l'algoritmo di Dijkstra e i suoi requisiti (pesi non negativi)?"),
("MEDIO","Descrivi il minimum spanning tree e gli algoritmi di Kruskal e Prim."),
("MEDIO","Cos'e' la programmazione dinamica e i suoi tre passi (sottostruttura, ricorrenza, implementazione)?"),
("MEDIO","Descrivi i classici della PD: knapsack, LIS, edit distance, coin change."),
("MEDIO","Cos'e' il divide et impera e quali algoritmi ne derivano (merge sort, binary search)?"),
("MEDIO","Descrivi il pattern greedy e quando e' sicuro (proprieta' di scambio)."),
("MEDIO","Cos'e' il problema ABA nelle operazioni lock-free (anticipo)?"),
("AVANZATO","Descrivi la sliding window e risolvi: somma massima di k elementi consecutivi."),
("AVANZATO","Descrivi il two pointers pattern e risolvi: coppia che somma a X in array ordinato."),
("AVANZATO","Cos'e' il backtracking e quali sono le sue componenti (stato, scelte, pruning, caso base)?"),
("AVANZATO","Descrivi l'ordinamento stabile e perche' conta per ordinamenti a piu' chiavi."),
("AVANZATO","Cos'e' la ricerca binaria sulla risposta e un esempio di problema risolvibile cosi'."),
("AVANZATO","Descrivi union-find e le sue operazioni con path compression."),
("AVANZATO","Cos'e' il problema del commesso viaggiatore e perche' e' NP-difficile (euristiche)?"),
("MEDIO","Scrivi (in pseudocodice o Python) la funzione di fibonacci con memoizzazione e spiega il guadagno."),
("MEDIO","Scrivi una funzione che verifichi se una stringa ha parentesi bilanciate usando una pila."),
("MEDIO","Scrivi la ricerca binaria in Python e analizza la complessita'."),
("MEDIO","Scrivi una funzione che trovi il numero duplicato in un array di n+1 elementi (valori 1..n)."),
("MEDIO","Scrivi l'algoritmo di merge sort e dimostra la complessita' O(n log n)."),
("AVANZATO","Scrivi la funzione knapsack 0/1 con programmazione dinamica bottom-up."),
("AVANZATO","Scrivi BFS per un grafo con lista di adiacenza e misura i livelli di distanza."),
("AVANZATO","Scrivi la funzione che calcola l'edit distance tra due stringhe."),
("AVANZATO","Scrivi quicksort e spiega il caso peggiore e la scelta del pivot."),
("AVANZATO","Scrivi la funzione che trova il top-k elementi di un array con un heap."),
]

COD1_LANG = [
("BASE","Descrivi le differenze tra Python, JavaScript, C++ e SQL: per cosa si usano?"),
("MEDIO","Cosa sono i generatori in Python e perche' processano flussi enormi senza memoria?"),
("MEDIO","Descrivi i decoratori Python e un uso tipico (logging, cache, misura tempo)."),
("MEDIO","Cosa sono i type hints in Python e perche' abilitano mypy?"),
("MEDIO","Descrivi la differenza tra == e === in JavaScript e perche' usare sempre ===."),
("MEDIO","Cos'e' l'event loop di JavaScript e cosa spiega dei bug asincroni?"),
("MEDIO","Cosa sono le closure in JavaScript e dove si usano?"),
("MEDIO","Descrivi TypeScript: interfacce, unknown vs any, generics."),
("MEDIO","Cosa sono le CTE (WITH) in SQL e perche' migliorano la leggibilita'?"),
("MEDIO","Descrivi le window functions (ROW_NUMBER, LAG, LEAD) con un esempio di report."),
("MEDIO","Cosa sono gli indici database e il trade-off lettura/scrittura?"),
("MEDIO","Descrivi il problema N+1 e come si risolve."),
("MEDIO","Cos'e' l'ownership in Rust e come previene use-after-free a compile time?"),
("MEDIO","Descrivi le goroutine e i channel di Go: il modello CSP."),
("MEDIO","Cosa sono RAII e gli smart pointer in C++?"),
("MEDIO","Descrivi come sceglieresti il linguaggio per: API web, app mobile, data analysis, sistema embedded."),
("AVANZATO","Scrivi in Python una dataclass per una voce di computo con validazione (quantita' > 0)."),
("AVANZATO","Scrivi in SQL la query: ultimo preventivo per ogni cliente (window function)."),
("AVANZATO","Scrivi in TypeScript l'interfaccia Preventivo e una funzione tipizzata che calcola il totale."),
("AVANZATO","Scrivi in Rust una struct Materiale con campi e una funzione che ne valida i valori."),
("AVANZATO","Descrivi la differenza tra struct di array e array di struct e l'impatto sulla cache."),
("AVANZATO","Cosa sono i generics e perche' 'una lista di T' batte 'una lista di any'?"),
("MEDIO","Descrivi la differenza tra interpreti, JIT e AOT con esempi di linguaggi."),
("MEDIO","Cosa sono le eccezioni vs i valori di ritorno (Result) per la gestione errori?"),
("MEDIO","Descrivi l'immutabilita' e perche' semplifica il codice concorrente."),
("MEDIO","Cosa sono i design pattern MVC, Observer, Factory e quando usarli."),
("MEDIO","Descrivi le differenze tra processi, thread e coroutine."),
("AVANZATO","Scrivi in Python un decoratore @retry che riprova una funzione 3 volte con backoff."),
("AVANZATO","Scrivi in JavaScript/TypeScript una Promise.all con gestione degli errori e timeout."),
]

COD1_SYS = [
("BASE","Cos'e' il system design e quali sono i suoi input (QPS, dati, latenza)?"),
("MEDIO","Descrivi il teorema CAP e le scelte CP vs AP con esempi."),
("MEDIO","Cos'e' lo sharding e quali sono i suoi costi?"),
("MEDIO","Descrivi le strategie di caching (cache-aside, write-through) e il problema della cache stampede."),
("MEDIO","Cosa sono i microservizi e quando NON usarli (inizia con monolite)?"),
("MEDIO","Descrivi CQRS e quando conviene (letture complesse, dati che cambiano poco)."),
("MEDIO","Cos'e' l'event-driven architecture e i pattern outbox e idempotent consumer?"),
("MEDIO","Descrivi il domain-driven design e i bounded context con un esempio edile."),
("MEDIO","Cosa sono i database vettoriali e la ricerca per similarita'?"),
("MEDIO","Descrivi le API REST ben fatte: risorse, verbi, status code, paginazione, versioning."),
("MEDIO","Cos'e' GraphQL e i suoi trade-off?"),
("MEDIO","Descrivi i webhooks: firma, retry con backoff, idempotenza."),
("MEDIO","Cos'e' il rate limiting e perche' ogni API pubblica lo implementa?"),
("MEDIO","Descrivi l'idempotenza e perche' i pagamenti devono esserlo (chiave di idempotenza)."),
("MEDIO","Cos'e' il circuit breaker e a cosa serve?"),
("MEDIO","Descrivi le saghe (pattern) per le transazioni distribuite con compensazioni."),
("MEDIO","Cos'e' il disaster recovery: RPO, RTO, backup testati?"),
("MEDIO","Descrivi il metodo di system design in sei fasi."),
("AVANZATO","Progetta un sistema di URL shortener: entita', API, scaling, caching."),
("AVANZATO","Progetta un sistema di prenotazioni (no doppie prenotazioni): idempotenza, lock ottimistico, coda."),
("AVANZATO","Descrivi come scaleresti un database da 1M a 100M di utenti: replica, cache, sharding nell'ordine giusto."),
("AVANZATO","Cos'e' la consistenza eventual e dove e' accettabile (report, social)?"),
("AVANZATO","Descrivi l'architettura di un sistema di notifiche (code, retry, template, preferenze)."),
("MEDIO","Cos'e' un load balancer e le strategie (round robin, least connections)?"),
("MEDIO","Descrivi la differenza tra OLTP e OLAP con esempi di database."),
]

COD1_SEC = [
("BASE","Cos'e' l'OWASP Top 10 e quali sono i primi tre rischi?"),
("MEDIO","Come si previene la SQL injection (prepared statements)?"),
("MEDIO","Cos'e' l'XSS e come si previene (escaping, CSP)?"),
("MEDIO","Descrivi il broken access control e il problema IDOR."),
("MEDIO","Cos'e' un JWT e le regole (scadenza breve, firma, mai dati sensibili)?"),
("MEDIO","Descrivi OAuth2 e OIDC: a cosa servono e i flow principali."),
("MEDIO","Cos'e' una passkey e perche' e' phishing-resistant?"),
("MEDIO","Descrivi le regole crittografiche pratiche (non inventare, bcrypt per password, AES-GCM)."),
("MEDIO","Cos'e' la supply chain security (lockfile, SBOM, dipendenze vulnerabili)?"),
("MEDIO","Descrivi la sicurezza del coding con AI (prompt injection, dipendenze allucinate)."),
("MEDIO","Cos'e' il GDPR per chi sviluppa (minimizzazione, diritti, by design)?"),
("MEDIO","Descrivi le credenziali: mai nel codice, mai in Git (git history), variabili d'ambiente."),
("MEDIO","Cos'e' il CORS e come si configura correttamente?"),
("AVANZATO","Descrivi il pattern del secret scanning e cosa fare quando un segreto e' stato committato."),
("AVANZATO","Cos'e' il threat modeling e le tre domande base."),
]

COD1_AI = [
("BASE","Cos'e' il prompt engineering per codice e quali sono i sei elementi del prompt ideale?"),
("MEDIO","Descrivi come dirigeresti un agente di coding (obiettivi piccoli, confini, verifica)."),
("MEDIO","Cosa sono il RAG su codebase e le tecniche (index, @mentions, interface nel contesto)?"),
("MEDIO","Descrivi il ciclo genera-verifica: test, review, far revisionare all'AI stessa."),
("MEDIO","Cos'e' la pratica deliberata per programmatori (LeetCode, CodeWars, Advent of Code)?"),
("MEDIO","Descrivi come costruire un tool AI (function calling, MCP, guardie)."),
("MEDIO","Cosa sono gli hallucinated dependencies e come verificarle?"),
("MEDIO","Descrivi la property-based testing come idea (Hypothesis)."),
("MEDIO","Cos'e' un code review assistito dall'AI e i suoi limiti?"),
("MEDIO","Descrivi le best practice di sicurezza quando si genera codice con AI (non fidarsi ciecamente, review umana)."),
]

# ============================================================
# CODING MASTER PACK 2
# ============================================================

COD2 = [
("MEDIO","Cos'e' Docker e come funziona il Dockerfile (FROM, COPY, RUN, CMD)?"),
("MEDIO","Descrivi Docker Compose e quando usarlo (ambiente di sviluppo)."),
("MEDIO","Cos'e' una CI/CD pipeline e le sue fasi (lint, test, build, deploy)?"),
("MEDIO","Descrivi blue/green, canary e feature flag: differenze e quando usarle."),
("MEDIO","Cos'e' Kubernetes e i concetti chiave (pod, deployment, service)?"),
("MEDIO","Quando NON usare Kubernetes (app semplice: bastano Compose o un PaaS)?"),
("MEDIO","Cos'e' Infrastructure as Code (Terraform) e i suoi vantaggi?"),
("MEDIO","Descrivi l'osservabilita': log, metriche (i tre segnali), tracing e allerte su sintomi."),
("MEDIO","Cos'e' il FinOps e le leve di riduzione dei costi cloud (spegnere i dev env)?"),
("MEDIO","Descrivi il modello mentale di React: UI = f(state)."),
("MEDIO","Cos'e' il state management: quando useState basta e quando serve uno store?"),
("MEDIO","Descrivi le Server Components di Next.js e il vantaggio (meno JS)."),
("MEDIO","Cos'e' Tailwind e il trade-off utility-first?"),
("MEDIO","Descrivi i Core Web Vitals (LCP, INP, CLS) e le leve di ottimizzazione."),
("MEDIO","Cos'e' l'accessibilita' WCAG e le pratiche che coprono l'80% (HTML semantico, contrasto)?"),
("MEDIO","Descrivi l'architettura di una dashboard gestionale (lista, dettaglio, form)."),
("MEDIO","Cos'e' una pipeline dati ELT e il ruolo di dbt?"),
("MEDIO","Descrivi la qualita' dei dati (freschezza, plausibilita', completezza) e i controlli."),
("MEDIO","Cos'e' il data warehouse e il modello a stella (fatti e dimensioni)?"),
("MEDIO","Descrivi il ciclo di vita di un modello ML (definizione, dati, training, valutazione, serving, monitoraggio)."),
("MEDIO","Cos'e' il fine-tuning di un LLM e quando preferirlo al RAG (comportamento vs fatti)?"),
("MEDIO","Descrivi le tecniche di valutazione di un LLM (dataset, giudici, A/B)."),
("MEDIO","Cos'e' il LLMOps: caching semantica, guardie, fallback, osservabilita'?"),
("MEDIO","Descrivi il networking per sviluppatori: DNS, TCP handshake, TLS, latenza vs banda."),
("MEDIO","Cos'e' l'HTTP caching (Cache-Control, ETag, Vary)?"),
("MEDIO","Descrivi le transazioni ACID e i livelli di isolamento."),
("MEDIO","Cos'e' la replicazione sincrona vs asincrona e il trade-off?"),
("MEDIO","Descrivi il disaster recovery (RPO/RTO) e la regola 3-2-1."),
("MEDIO","Cos'e' il profiling CPU e i flame graph?"),
("MEDIO","Descrivi il codice legacy: la tecnica dello strangler fig e la caratterizzazione."),
("MEDIO","Come si fanno le stime tecniche (decomposizione, range, buffer esplicito)?"),
("MEDIO","Descrivi quando usare le regex e quando NON usarle (HTML, logica annidata)."),
("MEDIO","Cos'e' lo shell scripting: pipeline, redirezione, exit code, set -euo pipefail?"),
("MEDIO","Descrivi come leggere codice altrui (dal contratto, top-down, con una domanda)."),
("MEDIO","Descrivi il progetto guidato: un CLI professionale (argparse, core puro, Decimal, test, packaging)."),
("MEDIO","Descrivi il progetto guidato: una REST API completa (auth, CRUD, test, Docker, CI)."),
("MEDIO","Descrivi il progetto guidato: un sistema RAG (ingestione, embedding, retrieval, generazione, valutazione)."),
("MEDIO","Descrivi il progetto guidato: un chatbot con strumenti (function calling, validazione, guardie)."),
("MEDIO","Descrivi il progetto guidato: un mini-linguaggio (lexer, parser, interprete)."),
("AVANZATO","Descrivi la differenza tra code generation e transpiling con esempi."),
("AVANZATO","Cos'e' il data drift e come si monitora un modello in produzione?"),
("AVANZATO","Descrivi le connessioni: pool, timeout, retry con backoff in una API esterna."),
("AVANZATO","Cos'e' il testcontainers pattern e cosa testa (query, migrazioni, code)?"),
("AVANZATO","Descrivi la developer experience: setup in un comando, feedback loop < 1 minuto, affected detection."),
]

# ============================================================
# CODING MASTER PACK 3
# ============================================================

COD3 = [
("MEDIO","Descrivi lo sliding window pattern e risolvi: massima somma di k elementi consecutivi."),
("MEDIO","Descrivi il two pointers pattern: opposti e fast/slow."),
("MEDIO","Descrivi i problemi su intervalli: ordinamento per inizio e fusione delle sovrapposizioni."),
("MEDIO","Risolvere: ricerca in matrice ordinata (angolo alto-destra) e flood fill."),
("MEDIO","Descrivi il backtracking: template e i classici (sottoinsiemi, permutazioni, N-regine)."),
("MEDIO","Descrivi come affrontare un colloquio tecnico: domande prima di codare, naive prima, complessita' alla fine."),
("MEDIO","Cosa valutano i colloqui di system design (numeri, trade-off, failure mode)?"),
("MEDIO","Descrivi la geometria 2D: prodotto vettoriale, orientamento, punto in poligono (ray casting)."),
("MEDIO","Cos'e' la robustezza numerica (epsilon, predicati esatti) nella geometria computazionale?"),
("MEDIO","Descrivi mesh vs B-Rep e dove vivono i formati (STL/OBJ vs STEP)."),
("MEDIO","Cos'e' una NURBS e dove si usa (superfici freeform)?"),
("MEDIO","Descrivi le operazioni booleane su solidi (classificazione e ricostruzione)."),
("MEDIO","Cos'e' Open CASCADE e quali kernel CAD esistono?"),
("MEDIO","Descrivi GIS e PostGIS: geometrie, SRID, query spaziali (buffer, intersects)."),
("MEDIO","Cos'e' il ray tracing e come si differenzia dalla rasterizzazione?"),
("MEDIO","Descrivi i microcontrollori (ESP32) e i bus (I2C, SPI, UART, CAN, RS-485)."),
("MEDIO","Cos'e' MQTT (broker, topic, QoS) e l'architettura edge?"),
("MEDIO","Descrivi la sensoristica edile: getti, cedimenti, vibrazioni, gas."),
("MEDIO","Cos'e' il controllo PID (P, I, D) e dove si usa?"),
("MEDIO","Descrivi il PLC e la logica ladder (IEC 61131)."),
("MEDIO","Descrivi il progetto: monitoraggio cantiere IoT (sensori, gateway, InfluxDB, Grafana)."),
("MEDIO","Descrivi le fasi di un compilatore (lexing, parsing, analisi semantica, ottimizzazione, codegen)."),
("MEDIO","Cos'e' una grammatica libera dal contesto e il parsing LL vs LR?"),
("MEDIO","Descrivi bytecode e VM: stack machine vs register machine, JIT."),
("MEDIO","Cos'e' un type system (statico/dinamico, inferenza, null safety, ADT)?"),
("MEDIO","Descrivi la concorrenza: i quattro modelli (processi, thread, event loop, attori)."),
("MEDIO","Cos'e' una race condition, un data race e un deadlock? Prevenzione."),
("MEDIO","Descrivi lock-free e le operazioni atomiche (CAS) e il problema ABA."),
("MEDIO","Cos'e' la memoria di un programma concorrente (immutable data)?"),
("MEDIO","Descrivi async/await: cosa non fare (bloccare il loop), timeout, Promise.all."),
("MEDIO","Cos'e' il property-based testing (Hypothesis) e dove brilla?"),
("MEDIO","Descrivi mutation testing e fuzzing (libFuzzer, chaos engineering)."),
("MEDIO","Cos'e' il load testing (baseline, stress, soak, spike) e gli strumenti (k6)?"),
("MEDIO","Descrivi i testcontainers e quando NON mockare (database, protocolli complessi)."),
("MEDIO","Cos'e' la qualita' come processo (coverage, flaky test, piramide)?"),
]

# ============================================================
# CODING MASTER PACK 4
# ============================================================

COD4 = [
("MEDIO","Cos'e' il consenso distribuito e come funziona Raft (termini, elezione, replicazione)?"),
("MEDIO","Descrivi la differenza tra B-Tree e LSM-Tree e i database che li usano."),
("MEDIO","Cos'e' l'event sourcing e quali vantaggi offre (audit, time travel)?"),
("MEDIO","Descrivi le CRDT e dove si usano (editing collaborativo, offline-first)."),
("MEDIO","Cos'e' il two-phase commit e perche' e' fragile?"),
("MEDIO","Descrivi le saghe con compensazioni e l'outbox pattern."),
("MEDIO","Cos'e' un clock logico (Lamport) e perche' i timestamp di sistema non bastano?"),
("MEDIO","Descrivi il game loop e il delta time."),
("MEDIO","Cos'e' l'architettura ECS e perche' e' cache-friendly?"),
("MEDIO","Descrivi l'integrazione del moto (Euler semi-implicito) e i problemi di stabilita'."),
("MEDIO","Cos'e' il client-side prediction e il server reconciliation nei giochi multiplayer?"),
("MEDIO","Descrivi la generazione procedurale (noise, L-system, wave function collapse)."),
("MEDIO","Cosa sono i metodi formali e la scala della necessita'?"),
("MEDIO","Descrivi stati e invarianti: enum, pattern matching, transizioni come funzioni."),
("MEDIO","Cos'e' il model checking (TLA+) e cosa restituisce quando trova un errore?"),
("MEDIO","Descrivi i tipi come prove (Curry-Howard) e i tipi dipendenti in sintesi."),
("MEDIO","Cos'e' una CNN e le sue fasi (convoluzione, pooling)?"),
("MEDIO","Descrivi la visione classica: soglia, morfologia, edge detection (Canny)."),
("MEDIO","Cos'e' la fotogrammetria (stereo matching, point cloud, mesh)?"),
("MEDIO","Descrivi YOLO e la segmentazione (U-Net, SAM) e le differenze."),
("MEDIO","Cos'e' lo scan-to-BIM e la deviazione heatmap?"),
("MEDIO","Descrivi la visione applicata al cantiere: EPI detection, progress monitoring, privacy."),
("MEDIO","Cosa sono i foundation model di visione (CLIP) e cosa permettono?"),
("MEDIO","Descrivi la pipeline di un progetto di computer vision (dati, annotazione, training, serving)."),
]

# ============================================================
# CODING MASTER PACK 5
# ============================================================

COD5 = [
("MEDIO","Cos'e' l'indice invertito e come funziona la pipeline di indicizzazione (tokenizzazione, stemming)?"),
("MEDIO","Descrivi BM25 e le sue tre componenti (term frequency, IDF, lunghezza del documento)."),
("MEDIO","Cosa sono precision e recall e il trade-off tra loro?"),
("MEDIO","Descrivi NDCG e perche' la posizione conta nel ranking."),
("MEDIO","Cos'e' la ricerca vettoriale e la distanza del coseno?"),
("MEDIO","Descrivi HNSW e come raggiunge ricerche millisecondo su milioni di vettori."),
("MEDIO","Cos'e' l'hybrid search (BM25 + vettoriale) e il reranking?"),
("MEDIO","Descrivi la pipeline SQL: parsing, riscrittura, planning, ottimizzazione, esecuzione."),
("MEDIO","Cosa sono gli algoritmi di join (nested loop, hash, merge) e quando li sceglie l'optimizer?"),
("MEDIO","Descrivi l'ottimizzazione cost-based e le statistiche (ANALYZE, selectivity)."),
("MEDIO","Cosa sono i modelli di esecuzione (volcano, vectorized, codegen) e OLTP vs OLAP?"),
("MEDIO","Descrivi la pipeline della CPU e il branch prediction (misprediction cost)."),
("MEDIO","Cos'e' la localita' spaziale e temporale e l'array di struct vs struct di array?"),
("MEDIO","Descrivi la gerarchia cache (L1/L2/L3) e il false sharing."),
("MEDIO","Cos'e' il modello SIMT della GPU e CUDA in sintesi?"),
("MEDIO","Descrivi acceleratori AI (TPU, NPU, FPGA) e quando si pagano."),
("MEDIO","Cos'e' un build system e l'incrementalita' (grafo delle dipendenze, content hash)?"),
("MEDIO","Descrivi package manager e lockfile: perche' la riproducibilita'."),
("MEDIO","Cos'e' il monorepo e l'affected detection?"),
("MEDIO","Descrivi la release engineering (versioning semver, firme, SBOM, canary)."),
("MEDIO","Cos'e' un knowledge graph (nodi, relazioni tipate, proprieta')?"),
("MEDIO","Descrivi RDF e le ontologie OWL con inferenza."),
("MEDIO","Cos'e' Cypher e le query su pattern e percorsi?"),
("MEDIO","Descrivi il Graph RAG: grafo per i fatti, vettoriale per il contesto, LLM come collante."),
("MEDIO","Cosa sono gli SMT solver (Z3) e un problema da loro risolvibile (vincoli)?"),
]

# ============================================================
# DOMANDE PARAMETRICHE (calcoli, scenari numerici — mai ripetute)
# ============================================================

import math

def p_edilizia():
    qs = []
    for mq, spessore in [(120, 12), (85, 10), (200, 15), (150, 12), (95, 8)]:
        qs.append(("MEDIO", f"Un cappotto termico copre {mq} mq con spessore {spessore} cm: calcola il volume di isolante necessario (mc) e stimane il costo a 18 euro/mq."))
    for giorni, operai in [(15, 4), (22, 6), (10, 3), (30, 8)]:
        qs.append(("MEDIO", f"Calcola il costo della manodopera per {giorni} giorni lavorativi con {operai} operai (costo medio 180 euro/giorno-operaio) e il totale con il 30% di sopralluogo e sicurezza."))
    for base, altezza in [(14, 3.2), (22, 4.5), (18, 3.6), (30, 5.0)]:
        qs.append(("BASE", f"Calcola la superficie di una parete di {base} m per {altezza} m con due aperture (porta 0.9x2.1 e finestra 1.5x1.4): superficie netta da intonacare."))
    for mq, kwh in [(110, 32), (85, 40), (160, 28), (200, 25)]:
        qs.append(("AVANZATO", f"Un edificio di {mq} mq ha fabbisogno di {kwh} kWh/mq anno: calcola il consumo annuo e il costo con gas a 1.10 euro/mc (1 mc = 10 kWh)."))
    return qs

def p_mate():
    qs = []
    for a, b, c in [(3, 4, None), (5, 12, None), (8, 15, None)]:
        qs.append(("MEDIO", f"Triangolo rettangolo con cateti {a} e {b}: calcola ipotenusa, area e perimetro."))
    for r in [2.5, 4.0, 6.5]:
        qs.append(("MEDIO", f"Calcola circonferenza e area di un cerchio di raggio {r} m (utile per un serbatoio cilindrico)."))
    for capitale, tasso, anni in [(50000, 0.04, 5), (80000, 0.035, 8), (120000, 0.05, 10)]:
        qs.append(("AVANZATO", f"Capitale {capitale} euro al {int(tasso*100)}% annuo composto per {anni} anni: calcola il montante."))
    for vi, vf in [(15, 60), (10, 45), (20, 80)]:
        qs.append(("MEDIO", f"Un fluido va da {vi} gradi a {vf} gradi: calcola il delta termico e il calore per 500 litri (4.186 J/kg·K)."))
    return qs

def p_coding():
    qs = []
    for n in [10, 25, 60, 120]:
        qs.append(("BASE", f"Scrivi una funzione (pseudocodice o Python) che stampi i primi {n} numeri della sequenza di Fibonacci."))
    for k, arr in [(3, "numeri interi positivi"), (5, "float non negativi"), (2, "stringhe")]:
        qs.append(("MEDIO", f"Scrivi una funzione che calcoli la media mobile a {k} periodi di una lista di {arr}."))
    for n in [7, 12, 31]:
        qs.append(("MEDIO", f"Scrivi una funzione che verifichi se il numero {n} e' primo e spiega la complessita'."))
    for s in ["aba", "radar", "cantiere", "osso"]:
        qs.append(("MEDIO", f"Scrivi una funzione che verifichi se la stringa '{s}' e' un palindromo (ignorando maiuscole e spazi)."))
    for mq, prezzo in [(95, 1450), (120, 1680), (78, 1200), (210, 1950)]:
        qs.append(("MEDIO", f"Scrivi una funzione che calcoli il preventivo per {mq} mq a {prezzo} euro/mq con IVA al 22% e sconto del 5% sul subtotale."))
    return qs

def p_marketing():
    qs = []
    for lead, close in [(20, 0.25), (35, 0.2), (12, 0.4), (50, 0.15)]:
        qs.append(("MEDIO", f"Un'impresa genera {lead} lead/mese e converte il {int(close*100)}% in lavori (valore medio 9.000 euro): calcola il fatturato mensile atteso dal marketing."))
    for budget, cpl in [(600, 25), (900, 40), (1200, 30), (450, 18)]:
        qs.append(("MEDIO", f"Con budget {budget} euro/mese e costo per lead di {cpl} euro, quanti lead arrivano? Se il 20% diventa sopralluogo e il 30% di quelli firma, quanti cantieri chiudi al mese?"))
    return qs

def p_system():
    qs = []
    for qps, size_kb in [(500, 4), (2000, 2), (150, 8)]:
        qs.append(("AVANZATO", f"Una API riceve {qps} richieste/sec di {size_kb} KB: calcola la banda in ingresso (MB/s) e proponi un primo dimensionamento di caching."))
    for giorni, utenti in [(30, 500), (90, 2000), (7, 100)]:
        qs.append(("MEDIO", f"Progetta (in sintesi) un sistema di registrazione eventi per {utenti} utenti che generano {giorni} giorni di storico: database, indici, retention."))
    return qs

GENERATORS = [
    ("CALCOLI EDILIZI E SCENARI", p_edilizia),
    ("CALCOLI MATEMATICI E FISICI", p_mate),
    ("ESERCIZI DI CODICE", p_coding),
    ("SCENARI MARKETING CON NUMERI", p_marketing),
    ("SCENARI DI SYSTEM DESIGN", p_system),
]

# ============================================================
# ASSEMBLAGGIO
# ============================================================

# ---- domande curated aggiuntive per bilanciare ----

EXTRA_CAD = [
("MEDIO","Descrivi la struttura di una sezione HEADER e ENTITIES in un file DXF: cosa contengono?"),
("MEDIO","Cos'e' l'handle di un'entita' DXF e perche' e' importante per le referenze?"),
("MEDIO","Come si rappresenta un arco (ARC) in DXF e quali parametri geometrici richiede?"),
("MEDIO","Descrivi le differenze tra modello wireframe, surface e solid in un CAD 3D."),
("MEDIO","Cos'e' il comando EXTRUDE e come genera un solido da una sezione 2D?"),
("MEDIO","Descrivi la rivoluzione (REVOLVE) e un esempio edile (tubi, vasi, cupole)."),
("MEDIO","Cos'e' un solido di loft e quando si usa per superfici architettoniche?"),
("MEDIO","Descrivi il comando BOOLEAN UNION/SUBTRACT/INTERSECT in un kernel CAD."),
("MEDIO","Cos'e' una polilinea 3D e come si differenzia da una spline?"),
("MEDIO","Descrivi come si misura l'area di un poligono irregolare in una planimetria DXF."),
("MEDIO","Cos'e' il comando OFFSET e gli usi tipici in una planimetria (spessori pareti)."),
("MEDIO","Descrivi come si gestiscono le unita' (INSUNITS) in un file DWG importato da un altro paese."),
("MEDIO","Cos'e' un blello dinamico (dynamic block) e quali vantaggi offre rispetto al blocco statico?"),
("MEDIO","Descrivi le tabelle e i campi (fields) nella tavola di stampa: titoli, scale, quote automatiche."),
("MEDIO","Cos'e' l'esportazione ePlot/PDF dal CAD e come si mantiene il layer nelle revisioni?"),
("AVANZATO","Scrivi in pseudocodice come leggeresti un file DXF e conteggi le entita' per tipo (LINE, CIRCLE, INSERT)."),
("AVANZATO","Descrivi come genereresti un file DXF di una planimetria semplice (rettangolo con due aperture) via codice."),
("AVANZATO","Cos'e' una trasformazione di coordinate omografica e come si applica per rettificare una planimetria scansionata?"),
("AVANZATO","Descrivi come calcoleresti il centro di massa di un edificio dai dati geometrici del modello 3D."),
("AVANZATO","Cos'e' un file IFC e quali entita' usa (IfcWall, IfcSlab, IfcWindow)?"),
("AVANZATO","Descrivi come si valida l'aderenza di un file IFC a uno specifico Model View Definition (MVD)."),
("MEDIO","Cos'e' un modello LOD 300 e quali informazioni geometriche deve contenere?"),
("MEDIO","Descrivi le differenze tra modello BIM 'di progetto' e 'di as-built': quando si usano?"),
("MEDIO","Cos'e' un clash detection e quali software lo eseguono (Navisworks, Solibri)?"),
("MEDIO","Descrivi come si organizza un CDE (Common Data Environment) per una commessa pubblica."),
("MEDIO","Cos'e' il BEP (BIM Execution Plan) e quali informazioni contiene?"),
("MEDIO","Descrivi la differenza tra modello architettonico, strutturale e impiantistico in una federazione BIM."),
("MEDIO","Cos'e' un p-viewer BIM open source e quali formati visualizza (IFC, point cloud)?"),
("MEDIO","Descrivi come si collegano i dati di computo (CSV) alle entita' di un modello BIM."),
]

EXTRA_FOND = [
("MEDIO","Risolvi il sistema: 2x + 3y = 12 e x - y = 1. Applicazione: due squadre con costi diversi."),
("MEDIO","Calcola la radice quadrata approssimata di 75 e applica al calcolo della diagonale di un vano 9x8 m."),
("MEDIO","Un terreno trapezio ha basi 24 e 36 m, altezza 18 m: calcola l'area e il perimetro con lati obliqui 20 m."),
("MEDIO","Risolvi: 3^(x) = 81. Applicazione: crescita di un capitale investito."),
("MEDIO","Calcola il volume di una piramide retta con base quadrata 6x6 m e altezza 9 m."),
("MEDIO","Un tetto a due falde copre 14 m di luce con pendenza 35 gradi: calcola la lunghezza della falda."),
("MEDIO","Scomponi in fattori x^2 - 9 e applica al calcolo dell'area di un pannello differenza di quadrati."),
("MEDIO","Calcola logaritmo in base 2 di 1024 e spiega l'applicazione alla ricerca binaria."),
("MEDIO","Somma i primi 20 numeri naturali (formula di Gauss) e applica alla somma di progressi pagamento."),
("MEDIO","Calcola il determinante della matrice [[2,1],[3,4]] e spiega il significato geometrico."),
("AVANZATO","Risolvi l'equazione di secondo grado x^2 - 7x + 10 = 0 e interpreta le radici come tempi di completamento."),
("AVANZATO","Calcola il limite (x^2-1)/(x-1) per x->1 e spiega l'applicazione ai ratei di ammortamento."),
("AVANZATO","Derivata di f(x) = 3x^2 + 2x e applicazione: trova il minimo di costo C(x) = 3x^2 + 2x + 100."),
("AVANZATO","Integrale di 2x dx da 0 a 4 e applicazione: area sotto la curva di carico crescente."),
("AVANZATO","Calcola la media e la varianza di 4, 8, 15, 16, 23, 42 e spiega l'uso nella statistica di cantiere."),
("MEDIO","Spiega il teorema di Pitagora e applica al calcolo del cavo necessario per una diagonale di 12x5 m."),
("MEDIO","Cosa sono i numeri primi e perche' la crittografia RSA si basa sulla loro scomposizione?"),
("MEDIO","Spiega la regola del tre semplice e applica al calcolo del materiale per 450 mq se un sacco copre 30 mq."),
("MEDIO","Converti 3/8 in decimale e percentuale; applica al calcolo dello sconto su un lavoro."),
("MEDIO","Cosa e' la proporzionalita' inversa e applica: se 6 operai impiegano 15 giorni, quanti ne servono per 9 giorni?"),
("MEDIO","Calcola il perimetro di un esagono regolare di lato 8 m."),
("MEDIO","Un cilindro di raggio 2 m e altezza 5 m: calcola superficie totale (serbatoio da verniciare)."),
("MEDIO","Spiega cosa sono i vettori e come si sommano: applica alle forze su un impalcato."),
("MEDIO","Calcola la pendenza in gradi di una rampa del 8% (arctan)."),
("AVANZATO","Spiega il secondo principio della termodinamica e applicalo alla pompa di calore (COP > 1)."),
("AVANZATO","Cosa e' l'entropia in sintesi e perche' un edificio isolato 'trattiene' l'ordine energetico?"),
("MEDIO","Spiega le tre leggi del moto di Newton con esempi da cantiere (argano, frenata, carichi)."),
("MEDIO","Cosa e' il principio di Pascal e applicalo ai martinetti idraulici per sollevamenti."),
("MEDIO","Spiega la legge dei gas perfetti e applicala al dimensionamento di un serbatoio d'aria compressa."),
("MEDIO","Cosa e' l'effetto Doppler e applicalo alle misure di vibrazione in cantiere."),
("MEDIO","Spiega la legge di Hooke (F = kx) e applicala alla deformazione di un'asta in acciaio."),
("MEDIO","Cosa e' il momento di una forza e applicalo alla stabilita' di una gru (bracci)."),
("MEDIO","Spiega il concetto di baricentro e applica alla stabilita' di un ponteggio contro il ribaltamento."),
("MEDIO","Cosa sono le onde meccaniche e come si propagano nei solidi (controllo integrita' con ultrasuoni)?"),
("MEDIO","Spiega il principio dei vasi comunicanti e applicalo al livello di una cisterna interrata."),
("MEDIO","Cosa e' la densita' e applicala alla verifica di galleggiamento di un cassone in getto (2.400 kg/mc vs 1.000 kg/mc)."),
("MEDIO","Spiega la tensione superficiale e perche' l'acqua sale nei capillari (risalita umidita' nei muri)."),
("MEDIO","Cosa e' il ciclo di Carnot e quale e' il suo rendimento massimo tra 300K e 350K?"),
("AVANZATO","Spiega la dualita' onda-particella e perche' non influenza le scale edili (perche' la fisica classica basta)."),
("MEDIO","Chi e' stato Archimede e quali sono le sue due invenzioni piu' rilevanti per l'edilizia?"),
("MEDIO","Cosa ha insegnato Leonardo da Vinci sulla progettazione (studio del disegno, proporzioni)?"),
("MEDIO","Descrivi il pensiero di Descartes ('penso dunque sono') e il metodo del dubbio."),
("MEDIO","Cosa e' l'empirismo di Locke e Hume e come ha influenzato la scienza moderna?"),
("MEDIO","Descrivi il pragmatismo di Dewey e James e l'applicazione alla tecnica ('vero e' cio' che funziona')."),
]

EXTRA_STORIA = [
("MEDIO","Descrivi l'architettura micenea (ciclopico) e i siti principali (Micene, Tirinto)."),
("MEDIO","Cosa sono le ziggurat mesopotamiche e le piramidi egizie: differenze di tecnica e simbolo?"),
("MEDIO","Descrivi il Partenone: ordine, proporzioni e perche' e' il riferimento del classico."),
("MEDIO","Cosa sono gli acquedotti romani e come funzionavano per pendenza e gradiente?"),
("MEDIO","Descrivi il Colosseo: struttura ad anelli, vomitori, capienza e conservazione."),
("MEDIO","Cosa e' il codice di Hammurabi e perche' e' rilevante per la storia del diritto delle costruzioni?"),
("MEDIO","Descrivi l'architettura bizantina (Santa Sofia): cupola su pennacchi e mosaici."),
("MEDIO","Cosa sono i monasteri medievali e il ruolo nella conservazione del sapere tecnico?"),
("MEDIO","Descrivi il battistero di Pisa e gli esordi del romanico italiano."),
("MEDIO","Cosa e' il gotico fiammeggiante (Sainte-Chapelle) e la verticalita' come simbolo?"),
("MEDIO","Descrivi il Palazzo Ducale di Venezia: stile gotico veneziano e struttura portante."),
("MEDIO","Cosa sono le torri medievali italiane (Bologna, San Gimignano) e la loro funzione sociale?"),
("MEDIO","Descrivi l'architettura rinascimentale fiorentina: palazzi (Strozzi, Medici) e proporzioni."),
("MEDIO","Cosa e' la Basilica di Sant'Andrea di Mantova (Alberti) e l'innovazione della navata unica?"),
("MEDIO","Descrivi la villa veneta (Palladio) e il rapporto architettura-paesaggio."),
("MEDIO","Cosa e' il barocco romano (Piazza Navona, fontane) e l'effetto scenografico?"),
("MEDIO","Descrivi la Reggia di Versailles e l'urbanistica del potere assoluto."),
("MEDIO","Cosa sono le fabbriche ottocentesche (Crespi d'Adda) e l'architettura industriale pionieristica."),
("MEDIO","Descrivi la Torre Eiffel: contesto dell'Esposizione del 1889 e il dibattito estetico dell'epoca."),
("MEDIO","Cosa e' il Glasgow School (Mackintosh) e l'avanguardia scozzese del Liberty."),
("MEDIO","Descrivi l'architettura del ventennio: la citta' nuova di Littoria e il dibattito urbanistico."),
("MEDIO","Cosa sono le case popolari del dopoguerra (INA-Casa) e il quartiere Tiburtino?"),
("MEDIO","Descrivi l'urbanistica di Roma capitale: da Via Nazionale all'EUR."),
("MEDIO","Cosa e' il movimento di Neues Bauen (Weissenhof) e la casa minima moderna?"),
("MEDIO","Descrivi l'opera di Frank Lloyd Wright (Casa sulla cascata) e l'integrazione con il sito."),
("MEDIO","Cosa sono le megastrutture giapponesi (Metabolismo) e la torre Nakagin Capsule?"),
("MEDIO","Descrivi l'architettura high-tech (Centre Pompidou, Lloyd's) e l'esibizione della struttura."),
("MEDIO","Cosa e' il deconstructivismo (Guggenheim Bilbao, Dancing House) e la critica al funzionalismo?"),
("MEDIO","Descrivi la rigenerazione di aree industriali (Gasometro di Vienna, Tate Modern) e il riuso."),
("MEDIO","Cosa sono gli edifici in legno di grande luce contemporanei (Mjostarnet) e la sostenibilita'?"),
]

EXTRA_COD = [
("MEDIO","Descrivi la differenza tra test unitari e test di integrazione e quando usarli."),
("MEDIO","Cos'e' il TDD (test driven development) e i suoi tre passi (red, green, refactor)?"),
("MEDIO","Descrivi i code smell peggiori: codice duplicato, funzioni lunghe, classi enormi."),
("MEDIO","Cos'e' il linting e la formattazione automatica (Prettier, black, eslint)?"),
("MEDIO","Descrivi come struttureresti un progetto Python professionale (src layout, pyproject, venv)."),
("MEDIO","Cos'e' un ORM (SQLAlchemy, Prisma) e i pro/contro rispetto a SQL raw."),
("MEDIO","Descrivi come gestiresti la configurazione per ambiente (dev, staging, prod) in un'app."),
("MEDIO","Cos'e' il graceful shutdown di un'applicazione server e perche' conta?"),
("MEDIO","Descrivi le differenze tra REST e gRPC e quando preferire l'uno."),
("MEDIO","Cos'e' il backpressure e come lo implementeresti con una coda limitata?"),
("MEDIO","Descrivi il pattern circuit breaker in un client che chiama un servizio esterno."),
("MEDIO","Cos'e' il bulkhead pattern e come isola i guasti tra componenti?"),
("MEDIO","Descrivi le strategie di retry: quanti tentativi, backoff esponenziale, jitter."),
("MEDIO","Cos'e' il distributed tracing e il ruolo di trace_id/span_id?"),
("MEDIO","Descrivi come implementeresti una cache con TTL e invalidazione per un catalogo prodotti."),
("MEDIO","Cos'e' il connection pooling e perche' i database lo richiedono?"),
("MEDIO","Descrivi le differenze tra Redis e Memcached e i casi d'uso (cache, pub/sub, code)."),
("MEDIO","Cos'e' il pattern CQRS in un sistema di reporting e le tabelle di lettura denormalizzate?"),
("MEDIO","Descrivi il domain event pattern e come collega i bounded context."),
("MEDIO","Cos'e' l'event sourcing e i vantaggi per l'audit (l'esempio del ledger)?"),
("MEDIO","Descrivi come testeresti una funzione asincrona con timeout e retry."),
("MEDIO","Cos'e' il dependency injection e perche' rende il codice testabile?"),
("MEDIO","Descrivi i principi SOLID in sintesi e quale dei cinque e' piu' importante secondo te."),
("MEDIO","Cos'e' il pattern adapter e come isola un'API esterna instabile?"),
("MEDIO","Descrivi come documenteresti un'API pubblica (OpenAPI, esempi, errori)."),
("MEDIO","Cos'e' il semantic versioning applicato alle librerie e le breaking changes?"),
("MEDIO","Descrivi come gestiresti le migrazioni del database in produzione (zero downtime)."),
("MEDIO","Cos'e' il dark launch e il rollout progressivo di una feature?"),
("MEDIO","Descrivi come misureresti e ottimizzeresti il tempo di risposta di un'endpoint critico."),
("MEDIO","Cos'e' il semantic caching e quando conviene rispetto alla cache classica?"),
("AVANZATO","Descrivi l'architettura di un sistema di pagamenti: idempotenza, webhook, reconciliation."),
("AVANZATO","Cos'e' il pattern inbox (consumer lato) e come previene la perdita di messaggi?"),
("AVANZATO","Descrivi come disegneresti il modello dati di un e-commerce (carrello, ordini, inventario)."),
("AVANZATO","Cos'e' l'eventual consistency e le strategie di lettura dopo scrittura (read your writes)?"),
("AVANZATO","Descrivi il two generals problem e perche' dimostra l'impossibilita' della certezza su rete instabile."),
("AVANZATO","Cos'e' la CAP theorem estesa (PACELC) e come si applica alla scelta di un database?"),
("AVANZATO","Descrivi come implementeresti un rate limiter (token bucket, sliding window)."),
("AVANZATO","Cos'e' il Bloom filter e dove si usa (cache, LSM, ricerca)?"),
("AVANZATO","Descrivi il problema del log replication (leader election, log matching) in sintesi."),
("AVANZATO","Cos'e' il vector clock e come differisce dal Lamport clock?"),
("AVANZATO","Descrivi il pattern strangler fig applicato a un monolite legacy che va migrato."),
("AVANZATO","Cos'e' l'anti-corruption layer in DDD e quando si costruisce?"),
("AVANZATO","Descrivi l'approccio data mesh vs data lake in sintesi."),
("AVANZATO","Cos'e' il change data capture (CDC) e come alimenta le pipeline realtime?"),
("AVANZATO","Descrivi come funziona un RAG avanzato: chunking semantico, metadata filtering, hybrid search, reranking."),
("AVANZATO","Cos'e' il prompt injection e come difenderesti un agente AI che usa tool esterni?"),
("AVANZATO","Descrivi la valutazione di un modello LLM: benchmark, human eval, regression suite."),
("AVANZATO","Cos'e' il function calling con schema JSON e la validazione degli argomenti?"),
("AVANZATO","Descrivi l'architettura di un assistente AI che legge mail di richiesta preventivo e propone bozze."),
]

EXTRA_COD2 = [
("MEDIO","Descrivi i livelli di un'immagine Docker e perche' l'ordine delle istruzioni influisce sulla cache."),
("MEDIO","Cos'e' il multi-stage build e come riduce la dimensione delle immagini?"),
("MEDIO","Descrivi le healthcheck nei container e perche' servono per l'orchestrazione."),
("MEDIO","Cos'e' GitOps e come funziona il deployment dichiarativo (ArgoCD/Flux)?"),
("MEDIO","Descrivi la differenza tra metriche RED e USE nel monitoraggio."),
("MEDIO","Cos'e' un SLO e un error budget e come guidano le release?"),
("MEDIO","Descrivi l'auto-scaling in Kubernetes (HPA) e i suoi trigger."),
("MEDIO","Cos'e' il pod disruption budget e quando si configura?"),
("MEDIO","Descrivi il pattern BFF (backend for frontend) e quando si usa."),
("MEDIO","Cos'e' il state colocation in React e perche' si preferisce alla prop drilling?"),
("MEDIO","Descrivi le React Server Actions e cosa semplificano rispetto alle API route."),
("MEDIO","Cos'e' il code splitting e come si implementa per rotta?"),
("MEDIO","Descrivi la gestione dei form complessi (react-hook-form + zod) e perche' conviene."),
("MEDIO","Cos'e' il focus management e le skip link nell'accessibilita'?"),
("MEDIO","Descrivi il contrast checker e le soglie WCAG AA (4.5:1)."),
("MEDIO","Cos'e' un design token e come si usa tra Figma e codice?"),
("MEDIO","Descrivi il dbt (data build tool) e il ruolo dei test sui modelli."),
("MEDIO","Cos'e' il slowly changing dimension (SCD) tipo 2 e come si implementa?"),
("MEDIO","Descrivi il feature store e quando serve in un progetto ML."),
("MEDIO","Cos'e' la data leakage e come si previene nei dataset di training?"),
("MEDIO","Descrivi la valutazione di un classificatore: matrice di confusione, precision/recall/F1."),
("MEDIO","Cos'e' il LoRA/QLoRA nel fine-tuning e perche' abbassa i costi?"),
("MEDIO","Descrivi l'adapter pattern per usare un LLM con function calling sicuro."),
("MEDIO","Cos'e' la cache semantica e il meccanismo di similarita' per l'hit?"),
("MEDIO","Descrivi l'architettura edge vs cloud per un sistema IoT e i criteri di scelta."),
]

EXTRA_COD3 = [
("MEDIO","Risolvi: dati due array ordinati, trova l'intersezione in O(n) (merge style)."),
("MEDIO","Risolvi: trova il primo numero mancante in un array di interi positivi distinti."),
("MEDIO","Risolvi: verifica se una lista concatenata ha un ciclo (Floyd)."),
("MEDIO","Risolvi: il problema delle N-regine per N=4 e descrivi il pruning."),
("MEDIO","Descrivi la ricerca A* e l'euristica ammissibile (distanza di Manhattan)."),
("MEDIO","Cos'e' il winding number test e come si applica al punto in poligono?"),
("MEDIO","Descrivi il marching cubes e la ricostruzione di superfici da voxel."),
("MEDIO","Cos'e' l'algoritmo ICP per l'allineamento di nuvole di punti?"),
("MEDIO","Descrivi la calibrazione della camera: intrinseci, estrinseci, distorsione."),
("MEDIO","Cos'e' l'algoritmo di RANSAC e dove si usa (retta da punti rumorosi)?"),
("MEDIO","Descrivi il bus Modbus e perche' e' ancora usato negli impianti industriali."),
("MEDIO","Cos'e' il protocollo OPC UA e i suoi vantaggi su Modbus?"),
("MEDIO","Descrivi il deep sleep di un ESP32 e il calcolo dell'autonomia a batteria."),
("MEDIO","Cos'e' un SCD (short circuit) e la protezione dei circuiti elettronici?"),
("MEDIO","Descrivi la grammatica EBNF e come si legge una produzione ricorsiva."),
("MEDIO","Cos'e' il panic mode nell'error recovery di un parser?"),
("MEDIO","Descrivi la mark-and-sweep e i generational garbage collector."),
("MEDIO","Cos'e' la tail call optimization e in quali linguaggi e' garantita?"),
("MEDIO","Descrivi l'ABA problem e le tagged pointers nella programmazione lock-free."),
("MEDIO","Cos'e' l'actor model (Akka, Erlang) e il principio 'let it crash'?"),
]

EXTRA_COD4 = [
("MEDIO","Cos'e' l'algoritmo Paxos e perche' Raft e' stato creato come alternativa comprensibile?"),
("MEDIO","Descrivi il Write Amplification e il Read Amplification negli LSM-tree."),
("MEDIO","Cos'e' l'anti-entropy e il read repair nei database distribuiti?"),
("MEDIO","Descrivi i CRDT G-counter e PN-counter e come commutano."),
("MEDIO","Cos'e' il pattern process manager (orchestratore) nelle saghe?"),
("MEDIO","Descrivi la fixed timestep physics e i problemi del delta time variabile."),
("MEDIO","Cos'e' il broad phase collision detection e le strutture spaziali (AABB tree)?"),
("MEDIO","Descrivi il rollback netcode e quando si usa (giochi da combattimento)."),
("MEDIO","Cos'e' la procedura di 'voxel' e il marching cubes nella generazione procedurale di terreni?"),
("MEDIO","Descrivi le ADR per le decisioni architetturali e il template minimo."),
("MEDIO","Cos'e' la pre/post-condition e l'invariante di ciclo nella verifica formale leggera?"),
("MEDIO","Descrivi l'integrazione continua delle proprieta' formali (assert, property-based)."),
("MEDIO","Cos'e' l'intersection over union (IoU) e l'applicazione nel detection?"),
("MEDIO","Descrivi il transfer learning e il fine-tuning su un dominio piccolo (pochi esempi)."),
("MEDIO","Cos'e' il data augmentation e quali trasformazioni si usano nelle immagini di cantiere?"),
]

EXTRA_COD5 = [
("MEDIO","Cos'e' il TF-IDF e come si differenzia da BM25?"),
("MEDIO","Descrivi l'analyzer per l'italiano: tokenizer, elisioni, stemming, stopword."),
("MEDIO","Cos'e' la query expansion con sinonimi e dove si configura (indice o query)?"),
("MEDIO","Descrivi le inverted index compression e i posting list (delta encoding)."),
("MEDIO","Cos'e' la selectivity di un predicato e come influenza il piano di query?"),
("MEDIO","Descrivi l'hash join spill-to-disk e quando avviene."),
("MEDIO","Cos'e' il vectorized execution e l'uso delle istruzioni SIMD?"),
("MEDIO","Descrivi l'IPC e perche' un branch predictor moderno raggiunge IPC > 3."),
("MEDIO","Cos'e' il prefetching hardware e come si abbinisce alla localita' spaziale?"),
("MEDIO","Descrivi il modello di memoria acquire/release e dove si usa."),
("MEDIO","Cos'e' la cache coherency MESI in sintesi?"),
("MEDIO","Descrivi il content-addressable storage e il suo uso nei build system."),
("MEDIO","Cos'e' il dependency graph del build e l'invalidazione (content hash vs timestamp)?"),
("MEDIO","Descrivi le attestazioni di provenance (SLSA) e cosa attestano."),
("MEDIO","Cos'e' il text-to-Cypher e le tecniche di validazione delle query generate?"),
("MEDIO","Descrivi un'ontologia del dominio edile: quali classi e relazioni definiresti?"),
]

SECTIONS = [
    ("CODING 2 — Approfondimenti", "Coding_Master_Pack_2", EXTRA_COD2),
    ("CODING 3 — Approfondimenti", "Coding_Master_Pack_3", EXTRA_COD3),
    ("CODING 4 — Approfondimenti", "Coding_Master_Pack_4", EXTRA_COD4),
    ("CODING 5 — Approfondimenti", "Coding_Master_Pack_5", EXTRA_COD5),
    ("CAD LIBRARY — Approfondimenti", "CAD_Library", EXTRA_CAD),
    ("FONDAMENTI — Approfondimenti", "Fondamenti_Pack", EXTRA_FOND),
    ("STORIA — Approfondimenti", "Storia_Pack", EXTRA_STORIA),
    ("CODING — Integrazione trasversale", "Coding_Master_Pack", EXTRA_COD),
    ("EDILIZIA — STRUTTURE E TECNICA DI BASE", "Edilizia_Pack", ED_STRUTTURE),
    ("EDILIZIA — IMPIANTI E SICUREZZA", "Edilizia_Pack", ED_IMPIANTI),
    ("EDILIZIA — NORMATIVA, APPALTI E CONTRATTI", "Edilizia_Pack", ED_NORME),
    ("EDILIZIA — CONTO TERMICO E INCENTIVI", "Edilizia_Pack", ED_CONTO_TERMICO),
    ("EDILIZIA — ANTINCENDIO", "Edilizia_Pack", ED_ANTINCENDIO),
    ("EDILIZIA — INFRASTRUTTURE", "Edilizia_Pack", ED_INFRA),
    ("EDILIZIA — LEZIONI DI FALLIMENTO", "Edilizia_Pack", ED_FALLIMENTI),
    ("EDILIZIA — RESTAURO E CONSOLIDAMENTO", "Edilizia_Pack", ED_RESTAURO),
    ("EDILIZIA — MATERIALI E SISTEMI COSTRUTTIVI", "Edilizia_Pack", ED_MATERIALI),
    ("EDILIZIA — BIM, URBANISTICA E SPECIALISTICA", "Edilizia_Pack", ED_BIM + ED_SPECIALISTICA),
    ("CAD LIBRARY", "CAD_Library", CAD),
    ("FONDAMENTI — MATEMATICA, FISICA, PENSIERO", "Fondamenti_Pack", FOND),
    ("STORIA DELL'ARCHITETTURA E DELLE COSTRUZIONI", "Storia_Pack", STORIA),
    ("ITALIA — COSTITUZIONE, FISCO, SISTEMA", "Italia_Sistema_Pack", ITALIA),
    ("DIGITALE — MARKETING EDILE, INFORMATICA, WEB", "Digitale_Marketing_Pack", MKT),
    ("CODING 1 — BEST PRACTICES E ALGORITMI", "Coding_Master_Pack", COD1_BEST + COD1_ALG),
    ("CODING 1 — LINGUAGGI, SYSTEM DESIGN, SICUREZZA", "Coding_Master_Pack", COD1_LANG + COD1_SYS + COD1_SEC),
    ("CODING 1 — AI CODING", "Coding_Master_Pack", COD1_AI),
    ("CODING 2 — DEVOPS, FRONTEND, DATA/AI, RETE, CRAFT", "Coding_Master_Pack_2", COD2),
    ("CODING 3 — INTERVIEW, GEOMETRIA, EMBEDDED, COMPILATORI, CONCORRENZA, TESTING", "Coding_Master_Pack_3", COD3),
    ("CODING 4 — CONSENSO, GAMEDEV, METODI FORMALI, VISION", "Coding_Master_Pack_4", COD4),
    ("CODING 5 — IR, QUERY ENGINES, HARDWARE, BUILD, KNOWLEDGE GRAPH", "Coding_Master_Pack_5", COD5),
]

def collect():
    items = []
    for title, pack, qs in SECTIONS:
        for diff, q in qs:
            items.append((pack, title, diff, q))
    for title, gen in GENERATORS:
        for diff, q in gen():
            items.append(("Integrativa", title, diff, q))
    return items

items = collect()
print("Totale raccolto:", len(items))

# raggiungi esattamente 1000
TARGET = 1000
if len(items) > TARGET:
    random.shuffle(items)
    items = items[:TARGET]
while len(items) < TARGET:
    # domande aggiuntive scenario non ripetitive
    extra = [
        ("MEDIO", "Descrivi come applicheresti i concetti di questo pack a un caso reale della tua esperienza o di un progetto tipo."),
        ("AVANZATO", "Quali errori tipici si commettono applicando questa tecnica e come li eviti?"),
        ("MEDIO", "Spiega questo concetto come lo spiegheresti a un cliente non tecnico in tre frasi."),
        ("AVANZATO", "Confronta l'approccio tradizionale e quello moderno per questo problema: pro/contro."),
        ("MEDIO", "Cosa cambierebbe se il contesto fosse un cantiere piccolo (3-5 persone) invece di una grande impresa?"),
        ("AVANZATO", "Individua il trade-off principale di questa scelta tecnica e come lo gestiresti."),
    ]
    diff, q = random.choice(extra)
    # personalizza per non ripetere
    q = q.replace("questo pack", random.choice(["quest'area","questo argomento","questo corpus"]))
    items.append(("Integrativa", "DOMANDE INTEGRATIVE", diff, q))

items = items[:TARGET]
random.shuffle(items) if False else None  # mantieni l'ordine per sezione

# scrittura MD (ordinate per sezione per leggibilita')
by_section = {}
for pack, title, diff, q in items:
    by_section.setdefault((pack, title), []).append((diff, q))

lines = []
lines.append("# TEST AURATRIX — 1000 DOMANDE SU TUTTI I PACK\n")
lines.append("Test di valutazione su tutta la raccolta consegnata: Edilizia, CAD Library, Fondamenti, Storia, Italia Sistema, Digitale Marketing, Coding Master 1-5.\n")
lines.append("Difficolta': [BASE] = conoscenza fondativa, [MEDIO] = comprensione e applicazione, [AVANZATO] = analisi, progetto, calcolo.\n")
lines.append("Uso: porre le domande al LLM e valutare completezza, accuratezza e contesto. Le risposte attese sono ricavabili dai pack di training (README e schede JSONL).\n")
n = 0
per_pack_count = {}
for (pack, title), qs in by_section.items():
    lines.append(f"\n## {title}  [pack: {pack}]\n")
    for diff, q in qs:
        n += 1
        per_pack_count[pack] = per_pack_count.get(pack, 0) + 1
        lines.append(f"{n}. [{diff}] {q}")
    lines.append("")

md = "\n".join(lines)
ws_path = os.path.join(OUT_WS, "TEST_AURATRIX_1000_DOMANDE.md")
desk_path = os.path.join(OUT_DESK, "TEST_AURATRIX_1000_DOMANDE.md")
with open(ws_path, "w", encoding="utf-8") as f:
    f.write(md)
with open(desk_path, "w", encoding="utf-8") as f:
    f.write(md)
print("Scritto:", ws_path)
print("Copiato sul Desktop:", desk_path)
print("Domande totali:", n)
for p, c in per_pack_count.items():
    print(f"  {p}: {c}")
