# -*- coding: utf-8 -*-
"""Giro M: 3 corsi nuovi — Edilizia agricola e zootecnica, Gestione condominiale,
Dighe e sistemazioni idrauliche. Contenuti classici verificabili; nessuna norma inventata."""
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
# PACK 1 — EDILIZIA AGRICOLA E ZOOTECNICA
# =====================================================================
agricola = [
dict(categoria="Stalle", nome="Stalle da latte: requisiti strutturali e di benessere",
 descrizione="La costruzione della stalla moderna: box, mangiatoie, pavimentazioni e benessere della bovina da latte.",
 tecnologia="Box individuali o group-housing (sistema brado) con cuccette da 1,0-1,2 m di larghezza per capo e lunghezza 2,1-2,3 m, divisori a tronchetti, materassini e lettiera; mangiatoie a corridoio 60-70 cm per capo in bovine da latte; pavimentazioni a griglia con zavorra gommata per ridurre infortuni alle mammelle; corsie di lavoro 3,5-4 m per i mezzi; saletta mungitura con ristagni e collettori a tenuta per il latte; impianto di ventilazione (tunnel o flussi incrociati); canalette di raccolta liquami con pendenze 1-1,5%; vasche di stoccaggio con volume per 120-180 giorni di produzione; altezza libera minima 2,2-2,5 m alla mangiatoia per l'areazione.",
 applicazioni="Allevamenti bovini da latte nuovi e ristrutturati, convezione a group-housing, ampliamenti di capienza.",
 vantaggi="Benessere conforme ai requisiti minimi di legge, riduzione del rischio mastiti e zoppie, efficiente raccolta dei liquami, qualità ambientale che si traduce in produzione.",
 limiti="Investimenti importanti per capienza, odorigenicità da gestire con le distanze dagli insediamenti, normativa sanitaria in aggiornamento, coordinamento con la campagna di mungitura.",
 costi_e_economia="Ordini di grandezza indicativi: nuova costruzione stalla 1.200-2.500 €/m²; ristrutturazione box e pavimentazioni 300-800 €/capo; vasca liquami 20-60 €/m³.",
 casi_real_world="Conversione diffusa delle stalle italiane da fissa a group-housing con cuccette; cantieri di ristrutturazione a reparti con spostamento degli animali.",
 normative="Requisiti minimi di protezione dei bovini secondo il decreto ministeriale vigente; D.Lgs 152/2006 per gli allevamenti intensivi e la gestione dei liquami; Reg. CE 852/2004 per l'igiene nella produzione alimentare.",
 note_cantiere="La stalla si progetta intorno alla mungitura: ogni intervento avviene per reparti con spostamento degli animali; la continuità della raccolta lattea vincola i tempi di fermo della saletta."),

dict(categoria="Stalle", nome="Stalle da carne e ricoveri per bovini all'aperto",
 descrizione="I ricoveri per la vita libera degli animali: piazzali, pannelli frangivento e capannoni di riparo.",
 tecnologia="Sistemi di allestimento all'aperto (vita libera) con piazzali recintati, pannelli frangivento in cls o acciaio alti 2-2,5 m, capannoni di riparo con tettoia semplice o doppia falda, aste di abbeveraggio con abbeveratoi a zampillo, mangiatoie su piazzale con fondo in cls o in terra stabilizzata; capannoni con apertura laterale di almeno 2/3 della superficie per la ventilazione; sistemi di raccolta delle deiezioni nei piazzali con pendenze verso le canalette; punti di isolamento per gli animali malati.",
 applicazioni="Allevamenti da carne (podolici, marchigiana, chianina), viticoltura mista, aziende con ampi piazzali disponibili.",
 vantaggi="Costi di costruzione contenuti rispetto alla stalla piena, benessere compatibile con le razze autoctone a rusticità elevata, gestione semplice dei gruppi.",
 limiti="Occupazione di suolo elevata, gestione del fango nei piazzali nelle stagioni piovose, flessibilità climatica limitata in inverno rigido.",
 costi_e_economia="Ordini di grandezza indicativi: tettoia di riparo 80-150 €/m²; piazzale recintato con pannelli 15-40 €/m lineare; complessivo vita libera 300-700 €/capo.",
 casi_real_world="Ricoveri per bovini da carne in pianura padana e zone appenniniche; ristrutturazioni di cascine con ricoveri rustici.",
 normative="Requisiti minimi di protezione dei bovini per i ricoveri all'aperto; distanze dagli insediamenti secondo normativa regionale per la limitazione degli odori; D.Lgs 152/2006.",
 note_cantiere="La vita libera richiede comunque il riparo e l'abbeveraggio garantiti: il capannone senza piazzale drenato diventa un fango d'inverno, con zoppie e mastiti."),

dict(categoria="Allevamenti suini", nome="Allevamenti suinicoli: capannoni, ventilazione e gestione dei liquami",
 descrizione="La costruzione degli allevamenti di suini: capannoni climaticamente controllati e rigidi requisiti ambientali.",
 tecnologia="Capannoni a navata singola o doppia con aste di alimentazione e abbeveraggio, pavimentazioni in griglia parziale o totale (fessurati in cls o plastica) con canalette sottostanti; ventilazione meccanica forzata con ventilatori a parete o a tetto calibrati sui cicli di vita (maiali da 10-110 kg richiedono temperatura da 30 °C iniziale a 18-20 °C finale); riscaldamento con tappetini o radiatori per i suinetti; reparti di quarantena e isolamento; vasche e sili di stoccaggio dei liquami; impianti di lavaggio ad alta pressione con acque di prima pioggia raccolte a parte; biosicurezza con spalti, recinzioni e percorsi separati.",
 applicazioni="Allevamenti di suini da ingrasso, da riproduzione, nursery e ingrasso; ristrutturazioni per il rispetto dei requisiti di benessere.",
 vantaggi="Conversione efficiente del mangime, mortalità contenuta con clima controllato, gestione dei liquami centralizzata, conformità alla normativa di benessere.",
 limiti="Odorosità molto sentita dalla vicinanza urbana, rischio epizootico alto che impone biosicurezza rigida, requisiti di distanza e di autorizzazione in regioni ad alta densità, investimenti continui su ventilazione e pavimentazioni.",
 costi_e_economia="Ordini di grandezza indicativi: capannone suinicolo completo 250-500 €/m² con impianti; posta suinetto in nursery 150-300 €/posto; vasca liquami 20-60 €/m³.",
 casi_real_world="Ristrutturazione degli allevamenti italiani verso il benessere dei suini (coda intera, materiale manipolabile); cantieri di adeguamento delle pavimentazioni.",
 normative="Requisiti minimi di protezione dei suini secondo il decreto ministeriale vigente; D.Lgs 152/2006 (all. IV per gli allevamenti); disciplina delle aree sottoposte a vincolo di destinazione secondo normativa regionale (distanze).",
 note_cantiere="La ventilazione si dimensiona sul ciclo estivo critico: un capannone sottodimensionato in estate perde suinetti per stress termico; le canalette dei liquami si puliscono per fasi con sblocco degli animali."),

dict(categoria="Serre", nome="Serre per orticoltura e florovivaismo: strutture e climatizzazione",
 descrizione="La serra come macchina agricola: struttura, copertura e controllo del clima interno.",
 tecnologia="Strutture in profili zincati (zinco Z275) a capannone ad arco o a falde, con luce 8-12 m e altezza colmo 4-6 m; coperture in vetro (durata lunga, peso elevato), policarbonato alveolare o film plastici PE-EVA (rinnovo ogni 3-5 anni); sistemi di apertura laterali con tende o scorrevoli per la ventilazione naturale; schermature termiche interne; riscaldamento con caldaie a gas o biomassa, tubi di riscaldamento o termoconvettori; nebulizzazione per l'umidificazione estiva; raccolta acque piovane dalla copertura con grondaie e vasche; impianti di fertirrigazione goccia a goccia con sistemi di ricircolo delle acque di drenaggio.",
 applicazioni="Orticoltura intensiva (pomodoro, cetriolo, peperone), florovivaismo, vivai, coltivazioni fuori stagione e produzione di piante madri.",
 vantaggi="Resa produttiva per m² multipla rispetto al pieno campo, controllo qualitativo e fitosanitario, uso efficiente di acqua e fertilizzanti con fertirrigazione, produzione fuori stagione a prezzi migliori.",
 limiti="Investimenti iniziali per gli impianti, consumi energetici per clima freddo, rischio botriti e malattie da eccesso di umidità, fine vita dei film plastici da gestire come rifiuti.",
 costi_e_economia="Ordini di grandezza indicativi: serra tecnologica completa 80-250 €/m²; serra semplice in film 30-80 €/m²; caldaia e riscaldamento 20-50 €/m²; rinnovo film 2-5 €/m².",
 casi_real_world="Aree serricole intensive della costa tirrenica, siciliana e pugliese; serra 'madre' per la produzione di propagazione nel florovivaismo.",
 normative="Requisiti di sicurezza per le strutture (norme UNI per le serre e carichi neve/vento regionali); gestione acque e fertilizzanti secondo D.Lgs 152/2006; normativa fitosanitaria per la produzione di piante.",
 note_cantiere="La serra si calcola sui carichi neve e vento della zona: la neve del 2017 e il vento hanno distrutto serre sottodimensionate; la pendenza minima della copertura per lo scolo è del 15-20%."),

dict(categoria="Stoccaggio", nome="Silos, essiccatoi e opere di stoccaggio agricolo",
 descrizione="Conservare il raccolto: silos di cereali, essiccatoi e pavimentazioni di stoccaggio.",
 tecnologia="Silos in acciaio zincato a fondo piatto o conico con capacità 100-5.000 t per cereali, muniti di coclea di estrazione, sistemi di ventilazione del grano (perdite di umidità e conservabilità), termometrie per il monitoraggio della temperatura del grano; torri di essiccazione con bruciatori a gasolio o biomassa (capacità 10-40 t/h di abbassamento umidità); pavimentazioni di stoccaggio in cls per mais, triticale e fieno con pendenze e bordi; magazzini per le balle e i macchinari con altezze 4-6 m; scale, passerelle e sistemi di trasporto meccanico (nastri, coclee); protezione antincendio e impianto di messa a terra per la polveri.",
 applicazioni="Aziende cerealicole, foraggere, stabilimenti di mangimi, centri di raccolta cooperativi.",
 vantaggi="Conservazione del raccolto senza perdite, gestione della filiera mangime in proprio, valorizzazione delle eccedenze, controllo della qualità commerciale.",
 limiti="Investimenti elevati e uso stagionale, rischio incendio e polveri da gestire con formazione e manutenzione, corrosione degli sfaldamenti umidi del silo, necessità di logistica di trasporto interno.",
 costi_e_economia="Ordini di grandezza indicativi: silo metallico 150-400 €/t di capacità; torre essiccazione 150.000-600.000 €; pavimentazione stoccaggio 40-90 €/m².",
 casi_real_world="Silos diffusi nelle aziende cerealicole del nord Italia; essiccatoi collettivi delle cooperative per mais e riso.",
 normative="Normativa antincendio per i depositi di prodotti combustibili e polveri; marcatura CE dei silos e degli impianti di sollevamento; sicurezza macchine secondo direttiva macchine.",
 note_cantiere="La ventilazione del grano è la vita del silo: senza aerazione corretta il grano 'cuoce' nel silo con perdite di peso e di qualità; le coclee si verificano prima della campagna, non durante."),

dict(categoria="Cantine", nome="Cantine e stabilimenti vinicoli: edilizia e processo",
 descrizione="Costruire dove si trasforma l'uva: cantine con vinificazione, barriques e stabilimenti imbottigliamento.",
 tecnologia="Locali di vinificazione con pavimentazioni in cls lavabili con pendenze e canalette di raccolta delle acque di processo; serbatoi in acciaio inox di capacità 10-500 hl con camicie di refrigerazione; locali a temperatura controllata per l'affinamento (barriques a 14-16 °C, umidità 70-80%); stabilimenti di imbottigliamento con linee automatiche, tunnel di pastorizzazione o microfiltrazione; spazi logistici di stoccaggio con scaffalature alte 6-10 m; locali di visita e sale degustazione con standard museali; impianti di depurazione delle acque di processo (fonti di inquinamento elevate nei periodi di vendemmia); sistemi di controllo accessi e tracciabilità.",
 applicazioni="Cantine sociali e cooperative, aziende vinicole private, stabilimenti di imbottigliamento, distillerie e oleifici.",
 vantaggi="Integrazione tra processo e spazio (flussi logistici corti), controllo termico per la qualità del vino, capacità di accoglienza turistica valorizzante, efficientamento energetico con refrigerazione centralizzata.",
 limiti="Stagionalità intensa della produzione che stressa gli impianti, acque di processo da trattare in breve tempo, vincoli paesaggistici spesso pesanti sulle cantine di pregio, investimenti specifici del processo elevati.",
 costi_e_economia="Ordini di grandezza indicativi: edilizia cantina 800-1.500 €/m²; impianto di vinificazione e serbatoi 100-300 €/hl di capacità; impianto depurazione acque 100.000-500.000 €.",
 casi_real_world="Cantine di design in Toscana e Piemonte con architetture di pregio; ampliamenti di cantine sociali con logistica automatizzata.",
 normative="Requisiti igienico-sanitari per gli stabilimenti alimentari (Reg. CE 852/2004 e D.Lgs 193/2007 HACCP); gestione acque di processo secondo D.Lgs 152/2006; vincoli paesaggistici per le cantine in zone di pregio.",
 note_cantiere="La vendemmia non aspetta: gli impianti idraulici e di refrigerazione si collaudano prima di settembre; i getti vicino ai serbatoi in acciaio richiedono protezioni contro gli schizzi di cls."),

dict(categoria="Opere di sistemazione", nome="Opere di sistemazione agraria: muri a secco e terrazzamenti",
 descrizione="La costruzione tradizionale del paesaggio collinare: muri a secco e terrazzamenti per l'agricoltura eroica.",
 tecnologia="Muri a secco in pietra locale (spessori alla base 40-60 cm, infittimento verso l'alto) costruiti a secco o con malta di calce nelle versioni restaurate; terrazzamenti con muri di sostegno in cls o cls di pietra vista, con lunghezze di 10-100 m e altezze 1-4 m; sistemi di drenaggio retro-murale con tubi forati e ghiaia per la pressione idraulica; canali di scolo superficiale lungo i cordoli; recupero e ricostruzione di muri a secco con cantieri scuola per la conservazione del paesaggio; collegamenti con reti di sentieri e strade poderali in massicciata o cls bianco.",
 applicazioni="Aree collinari e montane vitate e olivate, paesaggi terrazzati (Cinque Terre, costiera amalfitana, Langhe), contrasto al dissesto idrogeologico.",
 vantaggi="Conservazione del paesaggio e prevenzione del dissesto, manutenzione tradizionale a bassa tecnologia, valorizzazione turistica e culturale del territorio.",
 limiti="Manodopera specializzata sempre più rara, costi di ricostruzione elevati per la manualità, degrado continuo se non mantenuti, vincoli paesaggistici molto stringenti.",
 costi_e_economia="Ordini di grandezza indicativi: ricostruzione muro a secco 150-400 €/m² di parete; terrazzamenti in cls 100-250 €/m²; cantieri scuola e manutenzione con personale formato 30-60 €/h.",
 casi_real_world="Recupero dei terrazzamenti delle Cinque Terre dopo l'alluvione del 2011 con cantieri scuola; ricostruzione dei muri a secco nelle Langhe e sulle coste di pregio.",
 normative="Vincoli paesaggistici (D.Lgs 42/2004) per i muri a secco storici; interventi di difesa del suolo secondo la normativa forestale e di sistemazione idraulico-forestale; PNRR e bandi per il dissesto idrogeologico e il paesaggio rurale.",
 note_cantiere="Il muro a secco è ingegneria senza cls: il drenaggio retro-murale e la selezione delle pietre decidono la vita del muro più della malta; la ricostruzione fedele chiede il cantiere scuola con i maestri murettori."),

dict(categoria="Ambiente", nome="Edilizia rurale e vincoli: costruire nel paesaggio agricolo",
 descrizione="Le regole del costruire in campagna: fabbricati rurali, vincoli paesaggistici e pratiche semplificate.",
 tecnologia="Riconoscimento dei fabbricati rurali strumentali (annessi) ai sensi della normativa catastale ed edilizia; interventi di recupero dei fabbricati rurali dismessi con finalità agrituristica e ricettiva; pratiche edilizie per gli annessi agricoli secondo il regolamento edilizio comunale e le eventuali semplificazioni per l'agricoltura; distanze dai confini e volumetrie riconosciute secondo la legge nazionale e i regolamenti locali; recupero dei borghi e dei cascinali con vincoli paesaggistici (autorizzazione paesaggistica semplificata); interconnessione con i piani paesaggistici regionali; segnalazione certificata di inizio attività dove prevista per gli interventi minori.",
 applicazioni="Recupero di cascine e case coloniche, ampliamenti degli annessi di azienda agricola, agriturismi, fattorie didattiche, cantine di piccola dimensione.",
 vantaggi="Valorizzazione del patrimonio rurale esistente senza consumo di nuovo suolo, possibilità di diversificazione dell'azienda agricola, pratiche più snelle degli interventi urbani dove la legge lo prevede.",
 limiti="Vincoli paesaggistici e agro-forestali spesso molto stringenti, rischio di interpretazioni diverse tra comuni, l'abusivismo edilizio storico sul territorio agricolo è presidio dei controlli.",
 costi_e_economia="Ordini di grandezza indicativi: recupero cascinale con ristrutturazione pesante 800-1.800 €/m²; pratiche edilizie e paesaggistiche 2.000-15.000 € secondo complessità.",
 casi_real_world="Recupero di cascine lombarde e venete per agriturismi e aziende agricole; cantine e case coloniche recuperate nei territori vitati.",
 normative="DPR 380/2001 (Testo Unico Edilizia) per gli interventi sugli edifici rurali; D.Lgs 42/2004 per i vincoli paesaggistici; normativa catastale per la qualificazione dei fabbricati rurali (categorie catastali dedicate).",
 note_cantiere="Prima di acquistare un cascinale si verifica tutto: conformità urbanistica, catastale, vincoli (paesaggistici, idrogeologici, forestali) e situazione abitativa: il recupero economico nasce da una pratica pulita."),

dict(categoria="Materiali", nome="Corrosione e materiali negli ambienti zootecnici",
 descrizione="L'ambiente aggressivo della stalla: ammoniaca, umidità e deiezioni contro i materiali da costruzione.",
 tecnologia="Classificazione degli ambienti zootecnici come aggressivi per la corrosione (ammoniaca >20 ppm accelera la corrosione dell'acciaio zincato e del cls); protezioni per le strutture metalliche: zincatura a caldo pesante + verniciatura duplex, acciaio inox AISI 304/316 nei punti di contatto con le deiezioni; cls con basso rapporto a/c, copriferro maggiorato (4-5 cm), additivi idrorepellenti; pavimentazioni in cls con superfici antiscivolo e resistenza chimica alle deiezioni; rivestimenti epossidici per le vasche e le canalette; serramenti e grigliati in materiali non corrosivi; verifica periodica dello stato di corrosione nelle strutture di copertura.",
 applicazioni="Stalle, capannoni suinicoli, locali di stoccaggio liquami, sale di mungitura, essiccatoi e opere di processo.",
 vantaggi="Vita utile delle strutture moltiplicata con le protezioni corrette, manutenzione programmabile, igiene superiore con superfici lavabili e resistenti.",
 limiti="Costi superiori dei materiali protetti, la manutenzione resta obbligatoria (lavaggi acidi controllati), il degrado nascosto delle strutture portanti richiede ispezioni.",
 costi_e_economia="Ordini di grandezza indicativi: premium per materiali protetti +10-30%; rivestimento epossidico vasche 15-40 €/m²; ispezione corrosione periodica 500-2.000 €/anno per azienda.",
 casi_real_world="Capannoni zootecnici con strutture in acciaio zincato a spessore maggiorato; vasche liquami con rivestimenti in resina o acciaio inox.",
 normative="UNI EN ISO 12944 per la classificazione degli ambienti corrosivi e i cicli di protezione; norme sul cls per gli ambienti aggressivi (UNI EN 206 con classi di esposizione); verifiche di manutenzione programmata.",
 note_cantiere="Nella stalla la corrosione non è un dettaglio: le strutture di copertura si ispezionano ogni anno e i lavaggi disinfettanti aggressivi si scelgono compatibili con le protezioni."),

dict(categoria="Sostenibilità", nome="Sostenibilità in azienda agricola: fotovoltaico, biogas e autoconsumo",
 descrizione="Il cantiere agricolo come centrale energetica: integrazione di FV, biogas ed efficienza negli edifici rurali.",
 tecnologia="Fotovoltaico su tetti di stalle e capannoni (potenze 20-200 kWp, tetti spioventi o piani con strutture a spessore), vantaggiosi per le grandi superfici disponibili; agrivoltaico su vigneti e pannelli rialzati dove la normativa lo consente; biogas da digestione di letame e colture dedicate (synergy: schede dedicate nel corso RINNOVABILI_IDRO_BIOMASSA_GEOTERMIA); accumulo elettrico con batterie per l'autoconsumo degli essiccatoi e delle sale di mungitura; pompe di calore per l'acqua calda di processo e i locali di lavorazione; isolamento e ventilazione delle sale con recupero di calore; misuratori di consumo per la rendicontazione della sostenibilità (LCA dei prodotti agricoli); collegamento alle CER rurali per la vendita delle eccedenze.",
 applicazioni="Aziende agricole con consumi elettrici e termici rilevanti, consorzi energetici rurali, cantine cooperative.",
 vantaggi="Riduzione dei costi energetici dell'azienda, reddito dalle vendite di eccedenza e biometano, miglioramento del bilancio ambientale del prodotto, accesso a canali di vendita premium (filiera sostenibile).",
 limiti="Investimenti complessi da pianificare con i cicli agricoli, gli incentivi cambiano a ogni manovra (verifica annuale), la gestione dei digestati e le emissioni richiedono competenze tecniche.",
 costi_e_economia="Ordini di grandezza indicativi: FV agricolo 800-1.200 €/kWp installato; batterie accumulo 300-600 €/kWh; recupero calore mungitura 3.000-10.000 €; CER rurale secondo la configurazione.",
 casi_real_world="Tetti fotovoltaici delle stalle cooperative; biogas di azienda in upgrading a biometano per l'autoconsumo dei mezzi agricoli.",
 normative="D.Lgs 28/2011 per le FER; regole GSE aggiornate per scambio, RID, CER e Tariffa Premio (verifica vigente); D.M. 7 agosto 2025 (Conto Termico 3.0) per pompe di calore ed efficienza; disciplina agrivoltaica secondo le regole attuali.",
 note_cantiere="L'energia agricola si pianifica insieme all'edilizia: la nuova stalla si predispone con portanti e cablaggi per il FV; il tetto si orienta e si calcola per i pannelli prima del progetto strutturale definitivo."),

dict(categoria="Sicurezza", nome="Sicurezza nei cantieri agricoli e zootecnici",
 descrizione="Il D.Lgs 81/08 applicato all'azienda agricola: rischi specifici e prevenzione.",
 tecnologia="Rischi specifici dell'azienda agricola: attrezzature di lavoro (trattori con ROPS e cinture, verifiche periodiche), rimorchi e attrezzi con scudi e protezioni; rischio incendio e polveri nei silos e negli essiccatoi (classificazione zone ATEX dove necessario); rischio gas in ambiente confinato (vasche di liquami, pozzi neri) con misuratori e procedure di accesso; rischio zootecnico (animali, calci, malattie trasmissibili) con recinti e percorsi protetti; lavori in quota sui tetti (linee vita per la pulizia dei pannelli FV); rischio biologico con le procedure di igiene; formazione degli addetti alla conduzione delle macchine e alla sicurezza dei cantieri di ristrutturazione.",
 applicazioni="Cantieri di ristrutturazione degli allevamenti, manutenzione degli impianti aziendali, cantieri agricoli in generale.",
 vantaggi="Riduzione degli infortuni nei settori a più alta incidenza, conformità alle verifiche degli enti di vigilanza, continuità produttiva con personale formato.",
 limiti="La frammentazione delle aziende rende la formazione costosa, i cantieri agricoli sono spesso senza PSC formale (verificare gli obblighi), la manutenzione è posticipata per la stagionalità.",
 costi_e_economia="Ordini di grandezza indicativi: formazione sicurezza 50-150 €/addetto/giornata; verifica periodica attrezzature 100-500 €/macchina; linee vita e DPI quota 300-2.000 €.",
 casi_real_world="Verifiche periodiche delle attrezzature agricole secondo il calendario del D.Lgs 81/08; cantieri di ristrutturazione delle stalle con PSC redatto dal committente.",
 normative="D.Lgs 81/2008 (Titolo I e norme per le attrezzature di lavoro e gli ambienti confinati); normativa sulla salute e sicurezza nei cantieri (Titolo IV) quando si tratta di lavori di ristrutturazione; accordi Stato-Regioni per la formazione.",
 note_cantiere="Le vasche di liquami sono ambienti confinati con rischio di morte per asfissia: accesso solo con misuratori, imbracature e presidio esterno; nessun ingresso per esperienza o coraggio."),
]

write_pack("EDILIZIA_AGRICOLA_ZOOTECNICA_PACK",
 "Edilizia agricola e zootecnica", "FACOLTA_TECNOLOGIA_E_COSTRUZIONE", "L1-L2",
 "Stalle, ricoveri, allevamenti suinicoli, serre, silos, cantine, terrazzamenti, vincoli rurali, corrosione, sostenibilità, sicurezza.",
 """# EDILIZIA_AGRICOLA_ZOOTECNICA_PACK

**Edilizia agricola e zootecnica**

Stalle da latte e da carne, allevamenti suinicoli, serre e florovivaismo, silos e stoccaggi, cantine e stabilimenti vinicoli, terrazzamenti e muri a secco, edilizia rurale e vincoli, corrosione negli ambienti zootecnici, sostenibilità energetica in azienda agricola, sicurezza nei cantieri agricoli.

Schede: 11 (formato JSONL, un oggetto per riga).
""", agricola)

# =====================================================================
# PACK 2 — GESTIONE CONDOMINIALE
# =====================================================================
condominio = [
dict(categoria="Quadro normativo", nome="Il condominio nel codice civile: parti comuni, assemblea e regolamenti",
 descrizione="Le basi giuridiche del condominio: cosa sono le parti comuni, come funziona l'assemblea e i due regolamenti.",
 tecnologia="Parti comuni per legge (art. 1117 c.c.): suolo, cortili, muri portanti, tetti, scale, ascensori, impianti centralizzati, beni destinati all'uso comune; distinzione tra proprietà esclusiva e comproprietà per millesimi; assemblea ordinaria (prima convocazione con metà dei millesimi, seconda il giorno dopo con almeno un terzo, deliberazioni a maggioranza di millesimi e teste) e straordinaria per modifiche alle destinazioni d'uso (due terzi del valore); regolamento contrattuale (vincolante anche i successori) e regolamento assembleare (con voti favorevoli di altra metà dei millesimi); amministratore eletto con la maggioranza di metà dei millesimi e teste dell'assemblea.",
 applicazioni="Amministrazione ordinaria di condomini residenziali e direzionali, redazione di regolamenti, gestione delle deliberazioni.",
 vantaggi="Quadro giuridico consolidato che regola i rapporti tra condomini, flessibilità dei regolamenti per le esigenze specifiche, tutela dei dissenzienti con le azioni di impugnazione.",
 limiti="Litigiosità elevata sui confini tra parti comuni ed esclusive, i quesiti di maggioranza richiedono il calcolo preciso dei millesimi, la giurisprudenza evolve sui casi nuovi (b&b, ricariche auto).",
 costi_e_economia="Ordini di grandezza indicativi: onorari 300-600 €/anno per unità immobiliare; legali per impugnazioni da 1.500 € in su.",
 casi_real_world="Giurisprudenza consolidata su terrazzi, lastrici solari e facciate come parti comuni; contenziosi sui regolamenti che vietano le attività turistiche.",
 normative="Artt. 1117-1139 c.c. (condominio negli edifici) e L. 220/2012 (riforma del condominio); artt. 1130-1138 c.c. su amministratore e assemblea; giurisprudenza di legittimità.",
 note_cantiere="Ogni intervento su parti comuni nasce da una deliberazione valida: verificare il numero di millesimi presenti e il quorum PRIERA di firmare l'appalto."),

dict(categoria="Gestione tecnica", nome="Millesimali, ripartizioni e tabelle di riparto",
 descrizione="La matematica del condominio: come si formano le tabelle millesimali e come si ripartiscono le spese.",
 tecnologia="Tabelle millesimali di proprietà (valori di diritto) redatte dal costruttore o dal tecnico nominato dal giudice in mancanza di accordo (art. 68 disp. att. c.c.); tabelle millesimali di possibilità di uso per gli spazi comuni soggetti a valutazione; ripartizione delle spese generali per millesimi di proprietà (art. 1123 c.c.); ripartizione delle spese per cose serventi a parti di edificio (scale, impianti parziali) solo ai proprietari serviti (art. 1124-1126 c.c.); riparto dei consumi con contabilizzazione diretta o indiretta dove i millesimi non bastano; revisione delle tabelle in caso di errori materiali o modifiche degli edifici; gestione dei debiti verso l'amministratore con le rate ordinarie e straordinarie.",
 applicazioni="Redazione e revisione di tabelle millesimali, ripartizione delle spese di ristrutturazione, gestione dei contenziosi sulle ripartizioni.",
 vantaggi="Criteri di riparto giuridicamente certi che evitano i contenziosi, la revisione delle tabelle corregge gli errori storici, la contabilizzazione diretta allinea consumi e costi.",
 limiti="Le tabelle storiche sono spesso obsolete o sbagliate, le modifiche richiedono consenso o perizia, i contenziosi sui riparti sono frequenti e lunghi.",
 costi_e_economia="Ordini di grandezza indicativi: redazione nuova tabella millesimale 500-2.000 €; revisione con perizia 300-1.000 €; perizia CTU per tabelle in giudizio 800-2.500 €.",
 casi_real_world="Tabelle millesimali corrette dopo decenni di errori materiali; ripartizioni delle spese facciate solo ai piani serviti secondo la giurisprudenza.",
 normative="Artt. 1117, 1123-1126 c.c. per le ripartizioni; art. 68 disp. att. c.c. per la nomina giudiziale del tecnico; L. 220/2012 per le regole di gestione.",
 note_cantiere="Prima di ripartire una spesa grande si verifica la tabella: l'errore di millesimi su una facciata da 200.000 € si paga in anni di rate."),

dict(categoria="Lavori comuni", nome="Lavori alle parti comuni: facciate, tetti e cappotto condominiale",
 descrizione="Il cantiere condominiale: ristrutturare parti comuni con la delibera giusta e la sicurezza di cantiere.",
 tecnologia="Delibera assembleare di spesa straordinaria con la maggioranza prevista dal regolamento; redazione del quadro economico con computo e riparto; PSC e POS per il cantiere in edificio occupato (lavori con occupazione dei locali); ponteggi alla facciata con protezioni e reti, carichi sui lastrici solari e verifiche; gestione dei passaggi pedonali e delle auto in rimozione; comunicazioni ai condomini con verbali di sporcizia e danni pregressi; collaudo con perizia di conformità e verbale di fine lavori; garanzie decennali per le opere strutturali.",
 applicazioni="Rifacimento facciate e cappotti termici, rifacimento coperture e lastrici solari, risanamento di tetti, tinteggiature esterne, sostituzione serramenti comuni.",
 vantaggi="Miglioramento del patrimonio comune con riparto equo, accesso a detrazioni fiscali (alla data di progetto) per le riqualificazioni, aumento del valore dell'immobile.",
 limiti="Il cantiere in edificio occupato richiede gestione continua delle lamentele, i condomini morosi bloccano i pagamenti (l'amministratore non può pagare l'impresa), i tempi si allungano con le delibere contestate.",
 costi_e_economia="Ordini di grandezza indicativi: cappotto esterno 80-150 €/m²; rifacimento copertura con manto e isolamento 100-250 €/m²; ponteggio 15-35 €/m²; detrazioni secondo normativa vigente.",
 casi_real_world="Riqualificazioni energetiche di condomini con cessione del credito (regole in evoluzione, verificare); cantieri di facciata con ponteggi a telai di protezione.",
 normative="Artt. 1130-1138 c.c. per le delibere e l'amministratore; D.Lgs 81/2008 (Titolo IV) per la sicurezza in cantiere condominiale; normativa fiscale delle detrazioni (verifica vigente); D.Lgs 36/2023 per i contratti di appalto sopra le soglie.",
 note_cantiere="Nel condominio la sicurezza passa anche dai condomini: vietare l'accesso ai balconi sopra i ponteggi e comunicare i turni dei lavori rumorosi evita incidenti e contenziosi."),

dict(categoria="Impianti comuni", nome="Impianti centralizzati, contabilizzazione calore e acqua calda comune",
 descrizione="La gestione tecnica degli impianti centralizzati: dai contatori di calore alla legionella.",
 tecnologia="Impianti di riscaldamento centralizzati con caldaia a servizio dell'edificio e contabilizzazione diretta (ripartitori di calore sul radiatori più contatori di calore) o indiretta (riparto per millesimi con correttivi); obbligo di contabilizzazione diretta del calore negli edifici esistenti con centralizzato (legge 102/2013 con scadenze e sanatorie successive); produzione ACS centralizzata: sistema a svuotamento con ricircolo, controllo temperatura anti-legionella (custodia e ricircolo ≥60 °C), analisi periodiche dell'acqua (verifica secondo le linee guida); sostituzione caldaie centralizzate a gas con pompe di calore e integrazione FV collettivo; impianti di ricarica auto elettriche nelle autorimesse comuni con riparto dei consumi.",
 applicazioni="Condomini con riscaldamento centralizzato, gestione della ACS comune, ammodernamenti impiantistici, installazione di colonnine di ricarica.",
 vantaggi="Equità tra i condomini con la contabilizzazione diretta, risparmio energetico stimato del 15-30% con i ripartitori, sicurezza sanitaria con la gestione della legionella, modernizzazione con pompe di calore e FV collettivo.",
 limiti="Costi di adeguamento degli impianti centralizzati, la manutenzione della legionella è un adempimento continuo, i ripartitori richiedono tarature e gestione del software di riparto, i condomini con consumi minimi litigano sui consumi fissi.",
 costi_e_economia="Ordini di grandezza indicativi: ripartitore di calore 30-60 €/radiatore installato; contatore di calore 150-300 €; pompa di calore centralizzata 500-1.500 €/kW installata; analisi legionella 100-300 €/punto.",
 casi_real_world="Condomini che hanno dimezzato le spese di riscaldamento con la contabilizzazione; sostituzione di caldaie a gas centralizzate con pompe di calore in edilizia sociale.",
 normative="Art. 9 L. 102/2013 (contabilizzazione diretta del calore negli edifici esistenti); L. 238/2004 e linee guida nazionali per la prevenzione della legionella nelle torri e negli impianti idrici; UNI EN 834/835 per i ripartitori e contatori di calore.",
 note_cantiere="La contabilizzazione non si limita a posare i contatori: serve il software di riparto, la taratura iniziale e la comunicazione annuale ai condomini; la legionella si gestisce con temperature e ricircoli, non con gli interventi d'emergenza."),

dict(categoria="Contenzioso", nome="Il contenzioso condominiale: morosità, lavori e diffida dell'amministratore",
 descrizione="Come si gestiscono i conflitti nel condominio: dai morosi alle assemblee contestate.",
 tecnologia="Diffida dell'amministratore al condomino moroso con richiesta di pagamento entro 30 giorni (passaggio pregiudiziale alla sospensione dei servizi); sospensione del servizio del riscaldamento dopo la diffida (con le cautele per i soggetti deboli); intervento del giudice per le morosità elevate con decreto ingiuntivo; impugnazione delle delibere assembleari entro 30 giorni (condomini dissenzienti o assenti non avvisati) con possibilità di sospensiva; azione di responsabilità contro l'amministratore (anche per i danni da ritardo delle manutenzioni); mediazione obbligatoria per le controversie condominiali prima del giudizio; tutela del condomino 'critico' e del dissenziente.",
 applicazioni="Recupero crediti condominiali, impugnazione delibere, contenziosi sui lavori, responsabilità dell'amministratore.",
 vantaggi="Strumenti processuali snelli (decreto ingiuntivo) per i crediti certi, tutela giurisdizionale delle delibere irregolari, mediazione che sgrava i tribunali e velocizza le soluzioni.",
 limiti="Recupero dei crediti lento e incerto nei condomini in crisi, l'impugnazione blocca i lavori in corso, il contenzioso affossa il rapporto di vicinato.",
 costi_e_economia="Ordini di grandezza indicativi: decreto ingiuntivo 500-1.500 €; mediazione 500-2.000 €; giudizio ordinario da 3.000 € in su; morosità media nei condomini gestiti 5-15%.",
 casi_real_world="Sospensione del riscaldamento al moroso secondo la giurisprudenza consolidata; delibere annullate per errore di convocazione.",
 normative="Artt. 63 e ss. c.p.c. (decreto ingiuntivo); artt. 1137-1138 c.c. (impugnazione delle delibere e azioni); D.Lgs 28/2010 (mediazione); giurisprudenza sulla sospensione dei servizi ai morosi.",
 note_cantiere="L'amministratore che lavora 'a spanne' sulle delibere regala all'impresa un contenzioso: convocazioni, quorum e verbali corretti sono la prima difesa del cantiere condominiale."),

dict(categoria="Innovazione", nome="Supercondomini, contratti di quartiere e riqualificazione di edilizia residenziale pubblica",
 descrizione="La scala del condominio si allarga: supercondomini, contratti tipo e la riqualificazione dei grandi complessi.",
 tecnologia="Supercondominio: organismi che riuniscono più edifici o lotti con parti comuni condivise (vie, impianti centrali, parcheggi) e regolamenti di coordinamento; contratto di quartiere e accordi di programma per le riqualificazioni di grandi aree; riqualificazione energetica di edilizia residenziale pubblica con i bandi nazionali e regionali; gestione delle parti comuni nelle lottizzazioni con diritto di prelazione e norme di attuazione; manutenzione programmata dei grandi patrimoni con piani pluriennali; integrazione dei servizi di quartiere (vigilanza, pulizia, verde) nei regolamenti di supercondominio.",
 applicazioni="Grandi complessi residenziali, lottizzazioni, edilizia pubblica in riqualificazione, quartieri in trasformazione.",
 vantaggi="Economie di scala nella gestione e nella manutenzione, qualificazione energetica di interi quartieri, semplificazione amministrativa con un unico interlocutore, valorizzazione del quartiere.",
 limiti="Complessità giuridica della formazione dei supercondomini, gli interventi su edilizia pubblica richiedono bandi e tempi lunghi, il coordinamento tra tanti proprietari resta difficile.",
 costi_e_economia="Ordini di grandezza indicativi: riqualificazione energetica di edilizia pubblica 100-250 €/m²; contratti di quartiere con piani pluriennali da milioni di euro; gestione supercondominio 20-40% in meno dei singoli condomini.",
 casi_real_world="Contratti di quartiere nelle grandi città per la riqualificazione delle periferie; supercondomini nei nuovi complessi residenziali.",
 normative="Artt. 1117 ss. c.c. estesi ai supercondomini con gli accordi dei singoli; normativa sugli interventi edilizi di interesse pubblico (piani di zona, PRG); bandi nazionali per la riqualificazione con i testi vigenti alla data.",
 note_cantiere="Nel supercondominio i lavori si appaltano con un unico progetto ma si ripartiscono con le tabelle di ogni edificio: il computo deve prevedere il distacco per lotti fin dall'inizio."),

dict(categoria="Amministrazione", nome="Il ruolo dell'amministratore di condominio: compiti, responsabilità e organizzazione",
 descrizione="La figura chiave: cosa deve fare l'amministratore e dove risponde dei danni.",
 tecnologia="Compiti dell'amministratore (art. 1130 c.c.): cura della conservazione, manutenzione ordinaria e straordinaria secondo le delibere, amministrazione del danaro con conto corrente intestato al condominio, rappresentanza in giudizio, convocazione dell'assemblea, esecuzione delle delibere; obblighi di rendiconto annuale con gli allegati (libro cassa, stato patrimoniale); organizzazione dello 'studio amministrativo' con software di contabilità condominiale, protocollo dei verbali, archivio dei contratti; verifiche di gestione: fornitori con certificazioni (DURC), assicurazioni del condominio, libretto di impianto; responsabilità per danni da mancata manutenzione e per gli atti eccedenti il mandato.",
 applicazioni="Amministrazioni di condomini di ogni dimensione, organizzazione degli studi professionali, gestione dei passaggi di amministrazione.",
 vantaggi="Professionalizzazione della gestione con tutela del patrimonio comune, trasparenza con i rendiconti, riduzione del contenzioso con la gestione corretta.",
 limiti="Responsabilità elevate per un onorario contenuto, conflitto di interessi con le imprese 'di fiducia', il carico amministrativo cresce con la normativa.",
 costi_e_economia="Ordini di grandezza indicativi: onorari 300-600 €/anno per unità negli studi tradizionali; software di gestione 20-60 €/anno per condominio; assicurazione RC amministratore 300-1.000 €/anno.",
 casi_real_world="Studi amministrativi che passano da decine a centinaia di condomini con la digitalizzazione; condomini passati a amministratori con rendicontazione trasparente.",
 normative="Art. 1130 c.c. (compiti), art. 1136 (revoca e passaggio), art. 1137 (azioni verso l'amministratore); L. 220/2012 per la disciplina aggiornata; giurisprudenza sulla responsabilità per mancata manutenzione.",
 note_cantiere="L'amministratore che non mantiene l'impalcato del registro manutenzioni risponde dei danni: il diario di manutenzione è la prima difesa professionale."),

dict(categoria="Vita quotidiana", nome="B&B, affitti brevi, ricariche auto e i nuovi conflitti condominiali",
 descrizione="Le nuove frontiere del condominio: uso turistico, mobilità elettrica e tecnologia in casa.",
 tecnologia="Locazioni turistiche (b&b, affitti brevi) negli appartamenti: regole del regolamento contrattuale e della giurisprudenza in evoluzione, obblighi di registrazione e comunicazione (cedolare secca, CIN), gestione del decoro e dei flussi; ricarica auto elettriche in autorimesse comuni: diritto del singolo condomino di installare la colonna con riparto dell'energia, cablaggi in proprietà esclusiva o parti comuni, gestione dei contratti di fornitura; postazioni bici e monopattini, depositi in parti comuni; videosorveglianza e domotica condivisa negli spazi comuni; internet e fibra nelle case con riparto delle infrastrutture comuni; finestre anti-rumore e accorgimenti acustici tra unità.",
 applicazioni="Condomini con unità in locazione turistica, installazione di colonnine elettriche, gestione delle autorimesse, servizi digitali comuni.",
 vantaggi="Nuovi servizi per i condomini, valorizzazione delle unità, integrazione della mobilità sostenibile, sicurezza migliorata con la videosorveglianza.",
 limiti="La giurisprudenza sui b&b è in evoluzione (accoglienza consentita salvo regolamenti e disturbi), i costi delle infrastrutture di ricarica si ripartiscono, la privacy della videosorveglianza va gestita.",
 costi_e_economia="Ordini di grandezza indicativi: colonna ricarica domestica 500-1.500 € installata (escluso allaccio); cablaggio autorimessa 300-1.000 €; sistemi di videosorveglianza comune 1.000-5.000 €.",
 casi_real_world="Colonnine installate in autorimesse condominiali con il consenso dell'assemblea; regolamenti aggiornati che disciplinano gli affitti brevi.",
 normative="Art. 1117 c.c. per la destinazione d'uso e i regolamenti; L. 220/2012 e giurisprudenza su locazioni turistiche; normativa sulla ricarica dei veicoli elettrici (decreti in materia di colonnine e semplificazioni); GDPR per la videosorveglianza.",
 note_cantiere="Le regole si scrivono prima dei problemi: regolamenti che disciplinano affitti brevi, ricariche e videosorveglianza evitano il nove condomini su dieci dei contenziosi."),

dict(categoria="Acustica e decoro", nome="Rumore tra unità, decoro delle parti comuni e qualità della vita",
 descrizione="Il condominio come ambiente di vita: acustica, decoro e gestione dei disturbi.",
 tecnologia="Trasmissione del rumore tra unità immobiliari: suoni aerei e da calpestio, la rilevanza delle tramezze e dei massetti galleggianti; standard acustici di legge (DPCM 5/12/1997 per i requisiti acustici passivi degli edifici); interventi di miglioramento acustico tra unità (controsoffitti fonoassorbenti, massetti isolanti, tramezze con lana minerale); gestione dei rumori di calpestio (tacchi, mobili) con i regolamenti di buon vicinato; decoro delle scale, dei ballatoi e dei giardini comuni con i regolamenti e le sanzioni interne; gestione dei cani e degli animali comuni; illuminazione delle parti comuni con sensori di presenza e rilevamento fumi.",
 applicazioni="Reclami per rumori tra vicini, lavori di miglioramento acustico, gestione del decoro, riqualificazione delle parti comuni.",
 vantaggi="Qualità della vita che si traduce in valore immobiliare, riduzione dei contenziosi con le regole chiare, efficienza energetica delle parti comuni.",
 limiti="I massetti esistenti non rispettano i moderni standard acustici, gli interventi acustici tra unità richiedono coordinamento tra vicini, le sanzioni interne hanno limiti giuridici.",
 costi_e_economia="Ordini di grandezza indicativi: miglioramento acustico di un solaio 30-80 €/m²; massetto galleggiante 25-50 €/m²; illuminazione LED comune 20-50 €/punto luce.",
 casi_real_world="Condomini con massetti galleggianti nei nuovi solai; sentenze sul rumore da calpestio come disturbo della quiete.",
 normative="DPCM 5/12/1997 (requisiti acustici passivi); artt. 1117 e regolamenti per il decoro; normativa sulla quiete e sui reati di disturbo (art. 659 c.p.); L. 238/2004 e norme per gli impianti nelle parti comuni.",
 note_cantiere="Il contenzioso acustico si vince in fase di ristrutturazione: il massetto galleggiante e le tramezze coibentate costano poco in costruzione e molto in giudizio."),

dict(categoria="Manutenzione programmata", nome="Piano manutentivo condominiale e ammodernamento energetico",
 descrizione="Dal guasto all'emergenza alla manutenzione programmata: il piano che allunga la vita dell'edificio.",
 tecnologia="Piano di manutenzione pluriennale con schede di manutenzione per ogni parte comune (copertura, facciata, impianti, ascensore, infissi): frequenze, costi previsti, responsabili; sostituzione programmata degli elementi a fine vita (caldaia 15-20 anni, serramenti 25-30, impermeabilizzazioni 15-25); gestione delle pratiche con il libretto di edificio e di impianto; diagnosi energetiche con certificatori per le riqualificazioni; accesso ai bandi per la riqualificazione con la rendicontazione dei consumi; monitoraggio dei consumi comuni con il contabilità centralizzata; gestione dei rinnovi delle certificazioni (legionella, antincendio, ascensori).",
 applicazioni="Condomini con piano manutentivo attivo, riqualificazioni energetiche pianificate, gestione dei patrimoni residenziali.",
 vantaggi="Costi prevedibili e ripartiti nel tempo, emergenze ridotte al minimo, accesso agevolato ai bandi con la documentazione pronta, allungamento della vita utile dell'edificio.",
 limiti="Costi di avvio del piano, la rendicontazione richiede disciplina, i condomini tendono a rinviare le manutenzioni non urgenti, i fornitori di manutenzione programmata vanno selezionati.",
 costi_e_economia="Ordini di grandezza indicativi: piano manutentivo pluriennale 500-2.000 €; manutenzione ordinaria programmata 1-3 €/m²/anno; diagnosi energetica 200-800 €.",
 casi_real_world="Condomini che hanno dimezzato le emergenze con il piano pluriennale; riqualificazioni accessibili con la documentazione pronta.",
 normative="UNI 10329 per il codice di manutenzione degli edifici; D.Lgs 102/2014 e normativa cam per la riqualificazione; D.Lgs 81/2008 per la manutenzione delle attrezzature comuni (ascensori, caldaie).",
 note_cantiere="Il piano manutentivo si aggiorna ogni anno con gli interventi eseguiti e i costi reali: il piano che resta sullo scaffale è peggio di nessun piano, perché crea aspettative di protezione che non esiste."),

dict(categoria="Gare e appalti", nome="Appalti nel condominio: gare, contratti e gestione delle imprese",
 descrizione="Come il condominio sceglie e gestisce le imprese: dalle gare alla direzione lavori.",
 tecnologia="Procedure di selezione: richiesta di più preventivi per i lavori, gare formali per le spese grandi (con il progetto e il computo); contratti di appalto per lavori e servizi (pulizia, portineria, giardinaggio) con durata e rinnovi; sopralluoghi tecnici con le imprese e redazione dei verbali di constatazione; nomina del direttore dei lavori e della direzione lavori per i cantieri importanti; gestione delle pratiche con la comunicazione delle scadenze (DURC, assicurazioni, certificazioni delle imprese); SAL e contabilità dei lavori con le perizie di variante; collaudo finale con la perizia di conformità; gestione delle garanzie (fideiussioni, ritenute di garanzia) fino alla fine lavori.",
 applicazioni="Selezione delle imprese per i lavori condominiali, gestione dei contratti di servizio, controllo dei cantieri comuni.",
 vantaggi="Trasparenza nella spesa con le gare documentate, qualità con la direzione lavori, tutela con le garanzie, riduzione delle contestazioni post-lavori.",
 limiti="Le gare al ribasso premiano chi sottovaluta, la direzione lavori costa e i condomini la rifiutano per i lavori piccoli, la gestione amministrativa delle pratiche è pesante.",
 costi_e_economia="Ordini di grandezza indicativi: direzione lavori 3-8% del valore lavori; computo e gare 500-2.000 €; gestione SAL e contabilità 300-1.000 € per cantiere.",
 casi_real_world="Gare condominiali documentate con il computo anonimo; cantieri con direzione lavori senza contestazioni finali.",
 normative="D.Lgs 36/2023 per le soglie e le procedure degli appalti privati sopra le soglie; D.Lgs 81/2008 per i POS e i cantieri; normativa sulla sicurezza e sui pagamenti con le imprese (DURC).",
 note_cantiere="La gara al miglior prezzo senza progetto regala il contenzioso: anche nei lavori condominiali il computo metrico e la relazione tecnica pagano il loro costo."),
]

write_pack("GESTIONE_CONDOMINIO_PACK",
 "Gestione condominiale", "FACOLTA_GESTIONE_SISTEMA", "L1-L2",
 "Parti comuni, assemblea, millesimali, lavori e impianti centralizzati, contenzioso, supercondomini, amministratore, nuovi conflitti, acustica, manutenzione programmata, appalti.",
 """# GESTIONE_CONDOMINIO_PACK

**Gestione condominiale**

Parti comuni e regolamenti, assemblea e delibere, tabelle millesimali e riparti, lavori alle parti comuni, impianti centralizzati e contabilizzazione del calore, contenzioso e morosità, supercondomini e contratti di quartiere, ruolo dell'amministratore, b&b e ricariche auto, acustica tra unità, manutenzione programmata, appalti nel condominio.

Schede: 11 (formato JSONL, un oggetto per riga).
""", condominio)

# =====================================================================
# PACK 3 — DIGHE E SISTEMAZIONI IDRAULICHE
# =====================================================================
dighe = [
dict(categoria="Tipi di diga", nome="Dighe a gravità e a gravità alleggerita",
 descrizione="La diga più antica: il peso del cls che resiste alla spinta dell'acqua.",
 tecnologia="Dighe a gravità in cls o muratura: il volume del corpo diga genera un peso sufficiente a controbilanciare la spinta idrostatica con la risultante che resta nel nocciolo centrale (no trazione); profilo triangolare con cresta minima 3-4 m e appoggio largo 0,7-0,9 volte l'altezza; variante alleggerita con grandi vuoti interni (camere di ispezione) per ridurre il cls del 30-40%; giunti di dilatazione verticali con waterstop; drenaggi di fondazione con tubi forati sotto il paramento di monte; gallerie di visita e scarichi di fondo.",
 applicazioni="Valli strette e rocciose, altezze medie (10-60 m), bacini idroelettrici e di irrigazione.",
 vantaggi="Robustezza e durata secolare, manutenzione contenuta, resistenza al sisma con progettazione moderna, spazi interni ispezionabili.",
 limiti="Consumi enormi di cls, sensibilità alla qualità della roccia di fondazione, difficoltà di adeguamento in altezza, costi alti nei siti lontani dalle concreteiere.",
 costi_e_economia="Ordini di grandezza indicativi: costruzione 100-300 €/m³ di cls di diga; il cls rappresenta 40-70% del costo totale seconda accessibilità.",
 casi_real_world="Dighe a gravità alpine e appenniniche storiche in muratura rinforzate; grandi dighe a gravità alleggerite del novecento idroelettrico.",
 normative="Normativa speciale sulle dighe: classificazione per altezza e capacità, regole di sicurezza, prescrizioni di sorveglianza (testo consolidato vigente); NTC 2018 ed Eurocodici per le verifiche; normativa sulle opere che intralciano le acque pubbliche.",
 note_cantiere="Il getto della diga a gravità si pianifica in strati di 1,5-2,5 m con controllo della temperatura del cls (massa che matura): i giunti si trattano con waterstop e i drenaggi di fondazione si collaudano prima dell'imvaso."),

dict(categoria="Tipi di diga", nome="Dighe ad arco e a cupola",
 descrizione="La diga sottile che scarica le spinte sulla roccia delle sponde: l'arco e la cupola.",
 tecnologia="Dighe ad arco a spinta singola o doppia (volta inclinata a monte) con spessori alla base di 5-15 m anche per altezze 100-200 m: la spinta si scarica prevalentemente sugli abutment (spallette) come compressione dell'arco; requisito fondamentale di roccia sana nelle spallette; profilo a doppia curvatura (arco verticale e orizzontale) per aumentare la rigidità; dighe a cupola (FRP shells) rare, sfruttano la geometria tridimensionale; giunti perimetrali e centrali di getto; misuratori di convergenza e pendoli per il monitoraggio della flessa; scarichi di superfondo con valvole a bicchiere o cono.",
 applicazioni="Valli strette e profonde con pareti rocciose, grandi salti idroelettrici, altezze elevate con poco cls.",
 vantaggi="Consumi di cls minimi per metro di altezza, spinte sulle fondazioni ridotte e prevalentemente verticali, architetture possenti nel paesaggio.",
 limiti="Dipendenza assoluta dalla qualità delle spallette rocciose, sensibilità agli scavi e alle frane di rivestimento, controllo strumentale continuo necessario, sensibilità sismica da verificare di progetto.",
 costi_e_economia="Ordini di grandezza indicativi: il cls risparmiato si converte in costi di scavo e consolidamento delle spallette; costi da progetto a progetto nei grandi valichi.",
 casi_real_world="Grandi dighe ad arco europee e a doppia curvatura; la Hoover Dam come riferimento della diga ad arco-gravità; dighe a cupola sperimentali in alcuni paesi.",
 normative="Normativa speciale dighe con classificazione e prescrizioni; Eurocodice 8 per la sismica; linee guida internazionali ICOLD per il progetto e la sorveglianza.",
 note_cantiere="Prima dell'imvaso la diga ad arco si collauda con l'imvaso graduale e la lettura degli estensimetri: la prima stagione di riempimento è la prova definitiva della struttura."),

dict(categoria="Tipi di diga", nome="Dighe a contrafforti e dighe in materiali sciolti",
 descrizione="Le dighe dei grandi bacini in pianura: contrafforti in cls e dighe in terra o pietrame.",
 tecnologia="Diga a contrafforti (buttress): paramento di monte verticale in cls sostenuto da contrafforti triangolari a valle che alleggeriscono la sezione rispetto alla gravità piena; diga in terra: nucleo argilloso impermeabile con scarpate di sabbia e ghiaia (pendenze 1:2-1:3), dreni e filtri orizzontali e verticali, prismi di monte e di valle; diga in pietrame con nucleo impermeabile o schermo di cls asfaltico; protezione delle scarpate di monte con pietrame o conglomerati contro l'onda e l'erosione; tettoia di collegamento con il corpo diga; scarichi di superfondo e di fondo.",
 applicazioni="Grand bacini di laminazione e irriguo, valli larghe in pianura, altezze modeste (5-30 m) con lunghezze chilometriche.",
 vantaggi="Adatte a fondazioni cedevoli e materiali locali, lavorazioni con macchine terra senza getti continui, allungabili e riparabili per fasi.",
 limiti="Occupazione di suolo enorme, erodibilità delle scarpate da controllare per sempre, sensibilità alla colonizzazione animale dei dreni, la qualità del nucleo argilloso è critica.",
 costi_e_economia="Ordini di grandezza indicativi: 10-40 €/m³ di materiale piazzato; i costi di gestione delle scarpate e dei dreni durano per tutta la vita.",
 casi_real_world="Dighe in terra dei grandi bacini di irrigazione italiani e mediterranei; dighe a contrafforti del novecento.",
 normative="Normativa speciale dighe con prescrizioni per i materiali e la sorveglianza; UNI EN 1997 per le verifiche geotecniche; norme sugli argini e le opere di difesa del territorio.",
 note_cantiere="Le dighe in terra si costruiscono per strati compattati con il controllo in continuo della densità e dell'umidità: il nucleo argilloso non ammette 'abbastanza bene', ammette solo i valori del progetto."),

dict(categoria="Opere di presa", nome="Opere di presa, scarichi e dissipatori",
 descrizione="L'apparato che regola l'acqua: prese, scarichi di superficie e di fondo, energodissipatori.",
 tecnologia="Opere di presa a monte con paratoie o cancelli a ruota, bocche di presa per l'idroelettrico e l'irriguo; scarichi di superfondo per la regolazione dei deflussi e le piene (sezioni con paratoie piane o a segmento); scarichi di fondo (bottom outlets) per lo sgrondo del bacino e la qualità dell'acqua; canalizzazioni in galleria o a vista con curve di stretta; energodissipatori a salto di ski per restituire l'energia all'alveo senza erosione; paratie e manufatti di fondazione in cls con ancoraggi; sistemi di comando elettrico e di emergenza manuale.",
 applicazioni="Ogni diga di una certa dimensione, opere di presa fluviale, derivazioni idroelettriche, scaricatori di piena.",
 vantaggi="Controllo completo del bacino in ogni condizione idraulica, qualità dell'acqua gestibile per strati, sicurezza delle opere a valle con i deflussi controllati.",
 limiti="Opere ad altissima responsabilità in caso di guasto (la paratoia bloccata in piena è un'emergenza nazionale), usura cavitativa nelle parti a alta velocità, manutenzione in ambienti difficili.",
 costi_e_economia="Ordini di grandezza indicativi: le opere di presa e scarico rappresentano 10-30% del costo di una grande diga; revisioni e collaudi periodici obbligatori.",
 casi_real_world="Scarichi di fondo di dighe storiche revisionati dopo decenni; energodissipatori a salto di ski delle dighe alpine.",
 normative="Normativa speciale dighe (prescrizioni di sicurezza, prove e collaudi periodici); norme idrauliche per gli scaricatori di piena; direttive sulle acque e le infrastrutture critiche.",
 note_cantiere="Ogni paratoia si collauda a vuoto e in carico prima dell'imvaso completo: il mancato collaudo delle paratoie di fondo è tra le cause più gravi delle emergenze dighe."),

dict(categoria="Sicurezza", nome="Sicurezza delle dighe: classificazione, sorveglianza e piano di emergenza",
 descrizione="Il sistema di gestione della sicurezza: chi vigila, come si classifica, cosa si fa in emergenza.",
 tecnologia="Classificazione delle dighe per altezza e capacità del bacino (classi I-IV con prescrizioni crescenti); sistema di sorveglianza con ispezioni periodiche (ordinarie e straordinarie), controllo strumentale (pendoli, convergenze, piezometri, stazioni di misura) e telecontrollo; gestione dell'imvaso con regole di riempimento e sgrondo; piano di emergenza con le zone di allagamento a valle (flood mapping), le sirene, le vie di fuga e le esercitazioni; responsabilità del gestore e del collaudatore; lezioni apprese dagli incidenti storici (Vajont 1963: frana nel bacino che ha generato l'onda di straripamento) integrate nella moderna gestione dei bacini.",
 applicazioni="Tutte le dighe classificate, i bacini con insediamenti a valle, gli impianti idroelettrici e di irrigazione.",
 vantaggi="Riduzione del rischio di rottura a livelli minimi con la gestione strumentale, la prevenzione attraverso il controllo del bacino (frane, sismi), preparazione dell'emergenza con le esercitazioni.",
 limiti="La sicurezza costa in strumentazione e personale per sempre, il rischio residuo esiste e va comunicato, il degrado delle opere storiche richiede investimenti continui.",
 costi_e_economia="Ordini di grandezza indicativi: costi di sorveglianza e gestione della sicurezza 0,5-2% del valore di ricostruzione l'anno; strumentazione di nuova generazione da decine di migliaia di euro per diga.",
 casi_real_world="Vajont 1963 come lezione fondamentale di gestione del bacino; revisione della sicurezza delle dighe storiche italiane dopo gli eventi sismici.",
 normative="Normativa speciale sulle dighe: classificazione, requisiti di sicurezza, sorveglianza e piano di emergenza (testo consolidato vigente, con i regolamenti di dettaglio); direttive e linee guida ICOLD di riferimento internazionale.",
 note_cantiere="La diga non si consegna e basta: il collaudo definitivo avviene dopo anni di esercizio monitorato; il piano di emergenza si aggiorna con le mappe di rischio a valle."),

dict(categoria="Opere idrauliche", nome="Sistemazione idraulica di torrenti: briglie, soglie e massi",
 descrizione="Guidare l'acqua in montagna: le opere di sistemazione che fermano l'erosione e l'alluvione.",
 tecnologia="Soglie a pettine e a botti di sbarramento per la stabilizzazione del fondo; briglie in cls o pietrame a sezione variabile che riducono la pendenza del canale e trattengono i sedimenti; soglie gommate per la formazione di salti e la ricreazione ambientale; massi sciolti (rip-rap) e gabbioni per la protezione degli argini; transetti e opere di imbrigliamento per la canalizzazione; drenaggi di monte per abbassare la pressione dei terreni; boschi e opere di ingegneria naturalistica (prove di gerarchia con le opere strutturali); manutenzione ordinaria del materiale che si deposita a monte delle opere.",
 applicazioni="Torrenti e fiumi montani soggetti a colate detritiche, valli con centri abitati a valle, opere di bonifica idraulico-forestale.",
 vantaggi="Riduzione della velocità e dell'erosione, trattenimento dei detriti prima che raggiungano i centri abitati, ricostruzione ambientale delle sezioni fluviali, integrazione con l'ingegneria naturalistica.",
 limiti="Le opere si riempiono di sedimenti e perdono efficienza senza manutenzione, possono deviare i danni a valle, la gabbionata si degrada nei climi aggressivi, il cantiere in alveo lavora con l'acqua che arriva.",
 costi_e_economia="Ordini di grandezza indicativi: briglie 3.000-20.000 €/m lineare; gabbionate 80-200 €/m² di parete; manutenzione ordinaria 5-15% del costo di costruzione l'anno.",
 casi_real_world="Sistemazioni post-alluvione dei torrenti liguri e veneti; reti di briglie nelle valli alpine per la difesa delle frazioni.",
 normative="Autorizzazioni per le opere in alveo e la disciplina delle acque pubbliche; piani di bacino e strumenti di pianificazione idraulica; normativa sulla difesa del suolo e la gestione del rischio idrogeologico.",
 note_cantiere="La briglia si progetta con il deflusso di piena e la soglia di tracimazione controllata: un'opera mal dimensionata di piena diventa un pericolo per i cittadini a valle."),

dict(categoria="Argini", nome="Arginature fluviali e di bonifica: la difesa delle pianure",
 descrizione="I fiumi di pianura e la loro gabbia: argini in terra rinforzata e opere in cls.",
 tecnologia="Argini tradizionali in terra con nucleo di miglioramento argilloso e manti erbosi, con sezioni a dorso d'asino o a doppia scarpa; argini in terra rinforzata (geogriglie e conci vegetali) per le ricostruzioni compatte; opere di rivestimento della sponda in cls, massi o gabbioni dove l'erosione è attiva; argini cellulari in cls per gli attraversamenti urbani; marciapiedi, guard rail e percorsi di manutenzione lungo gli argini; sistemi di monitoraggio delle infiltrazioni (tubi piezometrici, sonde) nelle arginature storiche; colmata e ricostruzione dopo le piene.",
 applicazioni="Fiumi di pianura con centri abitati e campagne protette, reti di bonifica (Emilia-Romagna, Veneto, Polesine), attraversamenti urbani dei corsi d'acqua.",
 vantaggi="Protezione di territori densamente antropizzati e produttivi, continuità delle infrastrutture di bonifica, valorizzazione degli argini come percorsi e parco fluviale.",
 limiti="La sicurezza è relativa alla piena di progetto (le piene oltre soglia sono emergenza), la manutenzione delle sezioni erbose continua, gli argini storici possono nascondere problemi di filtrazione.",
 costi_e_economia="Ordini di grandezza indicativi: ricostruzione argini 50-150 €/m lineare; opere di rivestimento 200-800 €/m lineare; manutenzione ordinaria 2.000-10.000 €/km/anno.",
 casi_real_world="La storia del Polesine e della grande piena del Po del 1951 come lezione di arginature; ricostruzioni in terra rinforzata dei tratti critici.",
 normative="Autorizzazioni per le opere lungo i corsi d'acqua pubblici; normativa sulla difesa del suolo, sui consorzi di bonifica e sulle reti irrigue; piani di gestione del rischio di alluvione secondo la direttiva europea.",
 note_cantiere="L'argine si tiene con la manutenzione: il taglio dell'erba, il controllo dei cunicoli animali e la pulizia degli scarichi sono la difesa della piena."),

dict(categoria="Bacini", nome="Vasche di laminazione e bacini di espansione",
 descrizione="L'alleato delle piene: bacini che trattengono l'onda di piena e la restituiscono lentamente.",
 tecnologia="Bacini di laminazione in testata dei centri urbani con dighe a scorbie (threshold) o paratoie; vasche interrate o superficiali che riempiono nei picchi di piena (filling 1-6 ore) e svuotano in 12-48 ore attraverso scarichi regolati; sistemi di previsione pluviometrica e radar per l'ottimizzazione del volume disponibile; paratoie a ghigliottina azionate automaticamente; opere di collegamento con il collettore esistente (sfioratori, saracinesche); gestione del sedimento e del primo fiotto (first flush) per la qualità dell'acqua; integrazione con parchi urbani e uso a scopi ricreativi in condizioni ordinarie.",
 applicazioni="Centri urbani con reti fognarie insufficienti alle piene intense, corsi d'acqua urbanizzati, bacini imbriferi con tempi di risposta rapidi.",
 vantaggi="Riduzione della portata di piena che arriva al centro urbano, protezione con un volume noto e controllabile, valorizzazione urbana del bacino in condizioni ordinarie, gestione integrata con le previsioni meteo.",
 limiti="Richiedono volumi notevoli in area urbana (costo del suolo), funzionano solo se le soglie di esercizio sono rispettate, la manutenzione di pulizia dopo gli eventi è onerosa, il primo fiotto inquinato va gestito.",
 costi_e_economia="Ordini di grandezza indicativi: vasche di laminazione interrate 200-600 €/m³ di volume; bacini a scerbata 30-100 €/m³; gestione e pulizia post-evento da decine di migliaia di euro.",
 casi_real_world="Vasche di laminazione dei grandi centri urbani europei; bacini di espansione realizzati nei parchi urbani italiani.",
 normative="Piani di gestione del rischio alluvioni e gli strumenti urbanistici per i volumi di laminazione; autorizzazioni per le opere idrauliche; gestione delle acque meteoriche di primo fiotto secondo D.Lgs 152/2006.",
 note_cantiere="La vasca di laminazione si progetta con l'evento di piena di progetto E il volume del primo fiotto da trattare: dimenticare il fiotto inquinato trasforma la vasca in fonte di inquinamento cronico."),

dict(categoria="Frane", nome="Opere di stabilizzazione dei versanti: dreni, palificazioni e consolidamenti",
 descrizione="La difesa dal dissesto idrogeologico: ingegneria del versante per fermare la frana.",
 tecnologia="Opere di drenaggio: dreni profondi (trincee drenanti con tubi forati e massa filtrante) per abbassare la falda nel versante, pozzi drenanti con pompe o drenaggi orizzontali (drains radenti); opere di sostegno: pali e palificate, muri di sostegno in cls o gabbioni, tirovalli; consolidamento del terreno: iniezioni, jet grouting, perde d'acqua di fondazione; opere di bioingegneria: idrosemina, stuoie, frangiflutti vegetali per i versanti superficiali; opere di copertura e canalizzazione delle acque meteoriche per non innaffiare il versante; monitoraggio del versante con estensimetri, inclinometri e radar.",
 applicazioni="Frane in atto nei centri abitati, versanti sopra le infrastrutture stradali e ferroviarie, coste in erosione, siti post-crollo da riqualificare.",
 vantaggi="Riduzione del rischio idrogeologico per le opere pubbliche e i centri abitati, integrazione tra opere strutturali e naturalistiche, efficacia scientificamente misurabile con il monitoraggio.",
 limiti="I tempi di frana sono geologici e le opere rallentano ma non arrestano sempre, la manutenzione dei dreni è critica (si intasano), i costi sono elevati e il beneficio si valuta in decenni.",
 costi_e_economia="Ordini di grandezza indicativi: trincee drenanti 200-600 €/m lineare; consolidamenti con pali 500-1.500 €/m lineare; monitoraggio continuo 10.000-100.000 €/anno per sito complesso.",
 casi_real_world="Stabilizzazioni dei versanti delle grandi infrastrutture e dei centri storici a rischio; opere di bioingegneria sui versanti delle strade montane.",
 normative="Legge sulla difesa del suolo e la normativa forestale per gli interventi sui versanti; piani di assetto idrogeologico (PAI) con le classificazioni di rischio; autorizzazioni per le opere nelle aree vincolate.",
 note_cantiere="Il dreno si collauda misurando la portata drenata in secca: un dreno che non scarica è solo un tubo interrato; il monitoraggio pre-intervento guida la scelta tra le opere."),

dict(categoria="Acque potabili", nome="Acquedotti e reti idriche: adduttrici, serbatoi e ripartizione",
 descrizione="L'acqua che arriva in casa: le opere di captazione, adduzione e distribuzione.",
 tecnologia="Opere di captazione sorgenti e pozzi con camere di raccolta e pre-filtrazione; adduttrici in pressione con tubi in ghisa sferoidale (DN 100-1000) o acciaio rivestito, lunghe decine di chilometri, con saracinesche e sfiati; serbatoi di accumulo e compenso (elevati, interrati, coperti) che garantiscono portata e pressione nei picchi; reti di distribuzione con tubi in PE (DN 63-315), nodi con pozzetti, valvole di sfiato e scarico; sistemi di misura delle portate e delle pressioni (telecontrollo) per la ricerca delle perdite; impianti di potabilizzazione con filtrazione, disinfezione (cloro, biossido) e fluorazione dove prevista; gestione delle perdite (leak detection) con correlatori e gas tracciante.",
 applicazioni="Acquedotti comunali, reti regionali di adduzione, acquedotti rurali, reti industriali.",
 vantaggi="Continuità del servizio idrico con i serbatoi di compenso, qualità garantita dalla potabilizzazione, riduzione delle perdite con il telecontrollo, standard di servizio definiti dalla legge.",
 limiti="Investimenti continui per la sostituzione delle reti vecchie, la qualità dell'acqua si degrada nelle reti con le incrostazioni, le perdite sono difficili da trovare e costose, l'accesso alle condotte per manutenzione è complesso.",
 costi_e_economia="Ordini di grandezza indicativi: adduttrice in ghisa 100-300 €/m lineare secondo diametro; serbatoi 200-600 €/m³; gestione standard: la tariffa idrica copre i costi di gestione, manutenzione e ammortamento.",
 casi_real_world="Grandi adduttrici regionali di sussistenza (acquedotto pugliese, adduzioni alpine); programmi di sostituzione delle reti con il contrasto alle perdite.",
 normative="D.Lgs 152/2006 (requisiti delle acque destinate al consumo umano, Titolo III); L. 36/1994 (legge Galli) e normativa di recepimento per il servizio idrico integrato; standard tariffari secondo la normativa ARERA.",
 note_cantiere="Le condotte si collaudano con la prova di tenuta in pressione prima della consegna; i giunti della ghisa sferoidale si verificano uno a uno e la linea si sterilizza prima dell'immissione."),

dict(categoria="Fognature", nome="Fognature e depurazione: collettori, vasche e scarichi",
 descrizione="Il viaggio dell'acqua sporca: fognatura unita e separata, depurazione e scarico.",
 tecnologia="Schemi di fognatura unita (tutto in un tubo) e separata (acque nere e bianche divise) con i collettori in cls o PVC (DN 200-1500); pozzetti di ispezione e caduta; impianti di sollevamento (pozzetti di sollevamento con pompe sommergibili) per i centri sotto il livello della fognatura; trattamenti primari (decantazione) e secondari (fanghi attivi, biofiltri) fino al rilascio con gli scarichi secondo i limiti di legge; vasche di prima pioggia (first flush) per i piccoli bacini urbanizzati; biogas dai fanghi con digestori e cogenerazione; gestione dei fanghi di depurazione (disidratazione, smaltimento o recupero agricolo secondo le norme); scarichi a mare o in corpo idrico con i diffusori sommersi.",
 applicazioni="Reti fognarie comunali, impianti di depurazione (depuratori), depurazioni industriali preliminari, fognature parziali nei piccoli centri.",
 vantaggi="Salute pubblica con la raccolta delle acque reflue, depurazione che rispetta i limiti di scarico, recupero di biogas e fanghi come risorse, protezione dei corpi idrici ricettori.",
 limiti="Le reti separate convivono con gli allacciamenti sbagliati (acque bianche nelle nere), i depuratori richiedono competenze e personale, gli scarichi in mare sono sensibili, le vasche di prima pioggia riempiono rapidamente.",
 costi_e_economia="Ordini di grandezza indicativi: collettore in cls 100-400 €/m lineare; depurazione 500-2.000 €/abitante equivalente; gestione dei fanghi 30-80 €/t.",
 casi_real_world="Depuratori costieri con scarichi sommersi; campagne di verifica degli allacciamenti fognari nei centri storici.",
 normative="D.Lgs 152/2006 (scarichi e depurazione, con i regolamenti di recepimento delle direttive europee); normativa sulle acque reflue urbane e sulle fognature nelle zone sottoposte a vincolo; standard tariffari ARERA per il servizio idrico integrato.",
 note_cantiere="La fognatura funziona se gli allacci sono giusti: la verifica degli allacciamenti (bianche nelle nere) con le telecamere e i coloranti decide più della nuova condotta."),

dict(categoria="Economia", nome="Economia e programmazione delle grandi opere idrauliche",
 descrizione="Quanto costa e come si programma una grande opera idraulica: il cantiere che dura anni.",
 tecnologia="Stima dei costi per grandi opere con il breakdown: opere civili (diga, scarichi), impianti, espropri e mitigazioni ambientali, gestione del cantiere in montagna; programmazione pluriennale con i vincoli stagionali (imvasi, piene, innevamento); gestione delle interferenze con l'esistente (strade, linee elettriche, impianti idroelettrici in esercizio); finanziamenti pubblici e UE con i bandi e le rendicontazioni; le variabili di rischio (geologia, eventi meteo estremi, contenziosi) con le riserve di contingenza; il collaudo in fasi con l'imvaso graduale e l'esercizio di prova; i costi di esercizio e manutenzione pluriennali che pesano per decenni.",
 applicazioni="Grandi dighe, acquedotti interregionali, opere di difesa del territorio, riqualificazioni fluviali.",
 vantaggi="Investimenti che proteggono territori e produzioni per generazioni, finanziamenti pubblici che rendono sostenibili le opere, programmazione seria che riduce i rischi di stallo.",
 limiti="Tempi lunghissimi (10-30 anni dalla pianificazione all'imvaso), i costi reali superano spesso i preventivi, il contenzioso ambientale e territoriale può bloccare, la manutenzione futura sottovalutata.",
 costi_e_economia="Ordini di grandezza indicativi: grande diga da centinaia di milioni a diversi miliardi; acquedotto interregionale 0,5-2 M€/km; la manutenzione pluriennale vale 1-3% l'anno del valore dell'opera.",
 casi_real_world="Grandi opere idrauliche del novecento italiano ancora in esercizio; nuove opere di laminazione e difesa finanziate con i fondi nazionali per l'idrogeologico.",
 normative="Pianificazione delle opere pubbliche secondo D.Lgs 36/2023; valutazioni ambientali (VIA/VAS) per le grandi opere; normativa sugli espropri per pubblica utilità; disciplina dei contratti di servizio idrico integrato.",
 note_cantiere="La grande opera idraulica si misura su due generazioni: chi la progetta non la vede finita; la documentazione tecnica completa è il regalo più grande a chi verrà dopo."),
]

write_pack("DIGHE_E_SISTEMAZIONI_IDRAULICHE_PACK",
 "Dighe e sistemazioni idrauliche", "FACOLTA_INGEGNERIA", "L2-L3",
 "Dighe a gravità, arco, contrafforti e terra; opere di presa e scarichi; sicurezza e classificazione; sistemazioni torrentizie; argini; laminazione; frane; acquedotti; fognature; economia.",
 """# DIGHE_E_SISTEMAZIONI_IDRAULICHE_PACK

**Dighe e grandi opere idrauliche**

Dighe a gravità, ad arco, a contrafforti e in terra; opere di presa, scarichi e dissipatori; sicurezza, classificazione e piani di emergenza; sistemazioni idrauliche di torrenti; arginature fluviali; vasche di laminazione; stabilizzazione dei versanti; acquedotti e reti idriche; fognature e depurazione; economia e programmazione delle grandi opere.

Schede: 11 (formato JSONL, un oggetto per riga).
""", dighe)

print("OK giro M")
