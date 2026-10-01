# -*- coding: utf-8 -*-
"""Giro L: 3 corsi nuovi — Metodi costruttivi avanzati, Prefabbricazione industrializzata,
Perizie/stime/assicurazioni. Contenuti classici verificabili; nessuna norma inventata."""
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
# PACK 1 — METODI COSTRUTTIVI AVANZATI
# =====================================================================
metodi = [
dict(categoria="Cantieri sotterranei", nome="Metodo top-down (costruzione dal basso verso l'alto)",
 descrizione="Realizzazione di scavi profondi con getto del solaio di copertura subito dopo lo scavo, che lavora come sostegno.",
 tecnologia="Posa di diaframmi (pareti primarie in cls, pali di coronamento) o paratie con tiranti; scavo parziale, getto del solaio di copertura ancorato alle paratie; prosecuzione dello scavo sotto il solaio già realizzato, con getti dei solai intermedi man mano che lo scavo procede verso il basso; fondo ultimo con getto della platea ancorata alle paratie; puntelli temporanei ridotti al minimo perché i solai fungono da controvento.",
 applicazioni="Stazioni metropolitane interrate, parcheggi e cantine profonde in città, edifici interrati dove la superficie deve restare trafficata.",
 vantaggi="Superficie libera e subito riutilizzabile, deformazioni delle paratie contenute (i solai irrigidiscono il sistema), sicurezza contro il ribaltamento, minore occupazione urbana.",
 limiti="Costi dei diaframmi e dei getti a castello, necessità di progettazione integrata paratie-solai, tempi non necessariamente inferiori al metodo tradizionale.",
 costi_e_economia="Ordini di grandezza indicativi: diaframmi 400-900 €/m² di parete; premium complessivo top-down +20-60% rispetto a scavo tradizionale con puntoni.",
 casi_real_world="Stazioni di metropolitana interrate realizzate in ambito urbano con diaframmi e solai a castello; cantieri di parcheggi interrati multipiano sotto aree pedonali.",
 normative="Norme tecniche per le opere di sostegno delle scavo (UNI EN 1536 per pali, UNI EN 1538 per diaframmi); Eurocodice 7 (UNI EN 1997-1) per le verifiche geotecniche; NTC 2018.",
 note_cantiere="La sequenza dei getti è critica: nessuno scavo sotto un solaio prima del raggiungimento della resistenza di progetto dichiarata; i puntelli provvisori si rimuovono solo con getto dell'elemento di ricambio."),

dict(categoria="Cantieri sotterranei", nome="Cut & cover e trincee foderate",
 descrizione="Scavo a cielo aperto seguito dalla realizzazione dell'opera e dalla ricopertura, intera o parziale.",
 tecnologia="Scavo a cielo aperto con sostegno delle pareti (paratie, tiranti, sverniciamento di scarpate) o con tavolati; posa della struttura impermeabilizzata (fodera in cls con guaine) a botte o a spalle dritte; rinterro stratificato e compattato; variante con copertura parziale in c.a.p. o in acciaio che permette il recupero della superficie (trincea foderata) con giunti di posa prefabbricati.",
 applicazioni="Metropolitane superficiali, gallerie stradali urbane, gallerie di stazione, canali e collettori, opere idrauliche coperte.",
 vantaggi="Costruttivamente semplice e controllabile, ispezionabilità dell'opera durante la costruzione, adatto a geometrie complesse e grandi sezioni.",
 limiti="Impatto superficiale duraturo sul traffico, gestione delle acque di scavo, vinci di falda; in città può richiedere rettifiche degli assi e mantenimento dei flussi.",
 costi_e_economia="Ordini di grandezza indicativi: 5.000-15.000 €/m lineare per sezioni stradali standard; le paratie di sostegno in ambito urbano raddoppiano la voce scavo.",
 casi_real_world="Tratte metropolitane e gallerie urbane a cielo aperto ricoperte; canali e vasche di laminazione coperte nei parchi urbani.",
 normative="Verifiche di stabilità delle pareti di scavo secondo Eurocodice 7; gestione acque secondo D.Lgs 152/2006; sicurezza degli scavi secondo D.Lgs 81/2008.",
 note_cantiere="Il controllo della falda decide il metodo: con falda alta servono abbassamenti o diaframmi impermeabilizzanti, e il rinterro va eseguito con materiali e compattazioni che non caricano indebitamente la struttura."),

dict(categoria="Sollevamento opere", nome="Sollevamento, raddrizzamento e messa in asse di edifici esistenti",
 descrizione="Interventi su costruzioni dissestate: si solleva, si raddrizza o si trasla l'edificio invece di demolirlo.",
 tecnologia="Sostituzione delle fondazioni con micropali o pali radice; inserimento di martinetti idraulici o presse a puntelli tra zoccolo e struttura per sollevamenti fino a diversi metri; sistemi di raddrizzamento con tiranti post-tensionati, piastre di ripresa e getti strutturali; traslazione su binari o rulli per edifici da spostare; monitoraggio continuo con estensimetri, livelle e stazioni totali durante tutte le fasi.",
 applicazioni="Edifici storici dissestati, casolari rurali da recuperare, edifici sotto cui passano nuove infrastrutture, rimessa in quota dopo cedimenti differenziali.",
 vantaggi="Salvaguardia del costruito esistente, risparmio rispetto alla demolizione e ricostruzione, possibilità di rinnovare interamente le fondazioni senza smontare l'edificio.",
 limiti="Richiede indagini strutturali approfondite, lavorazioni millimetriche con squadre specializzate, imprevedibilità del comportamento di murature antiche, costi elevati.",
 costi_e_economia="Ordini di grandezza indicativi: consolidamento fondazioni con micropali 150-400 €/m lineare; sollevamento e messa in asse di una villetta 30.000-150.000 € secondo entità; monitoraggio continuo 5.000-30.000 €.",
 casi_real_world="Sollevamento di edifici storici dopo cedimenti; traslazioni di edifici per allineamenti stradali e ferroviari (casistica internazionale ampia).",
 normative="UNI EN 14199 per i micropali; NTC 2018 e circolare applicativa per le verifiche sulle strutture esistenti; aggiornamento del quadro sismico se richiesto dalla modifica delle fondazioni.",
 note_cantiere="Nessun sollevamento senza piano di monitoraggio e valori limite di arresto: le murature antiche tollerano pochi millimetri di differenziale tra un lato e l'altro."),

dict(categoria="Scavo meccanizzato", nome="TBM (tunnel boring machine): EPB e doppio scudo",
 descrizione="La meccanizzazione dello scavo in galleria: macchine a piena sezione con sostegno simultaneo della calotta.",
 tecnologia="TBM EPB (Earth Pressure Balance) per terreni a bassa copertura e falda: miscelazione del terreno scavato nella camera di scavo per controbilanciare la pressione del fronte, espulsione controllata con coclea; doppio scudo per rocce stratificate e terreni misti con rivestimento in conci (voussoir) posati dentro il manicotto; sistema di rincalzi idraulici per la spinta; impianti di separazione dei materiali in superficie; anelli prefabbricati in cls con guarnizioni di tenuta.",
 applicazioni="Gallerie stradali e ferroviarie lunghe, metropolitane, collettori e condotte forzate, attraversamenti sotto corsi d'acqua e centri urbani.",
 vantaggi="Velocità di avanzamento (10-30 m/giorno), sicurezza del personale lontano dal fronte, qualità del rivestimento, minore impatto superficiale con un solo pozzo di lancio e uno di arrivo.",
 limiti="Investimenti in apparecchiature (decine di milioni), sensibilità a terreni eterogenei e cedimenti, necessità di progettazione 'su misura' della macchina, gestione dei materiali di scavo.",
 costi_e_economia="Ordini di grandezza indicativi: costruzione meccanizzata 8.000-30.000 €/m lineare a seconda di diametro e geologia; TBM di grande diametro 30-100+ M€ di valore macchina.",
 casi_real_world="Grandi gallerie stradali e ferroviarie italiane ed europee scavate con EPB e doppio scudo; linee metropolitane di recente costruzione.",
 normative="Sicurezza nei lavori sotterranei secondo D.Lgs 81/2008; verifiche geotecniche secondo Eurocodice 7 e normativa specifica per le gallerie; specifiche progettuali per il dimensionamento dei conci.",
 note_cantiere="La TBM non perdona l'improvvisazione: i parametri di pressione frontale e coppia si tarano con prove e con il controllo continuo dei cedimenti superficiali; i pozzi di lancio sono opere provvisionali a sé."),

dict(categoria="Scavo convenzionale", nome="Metodo NATM (scavo tradizionale ad avanzamento ridotto) in galleria",
 descrizione="Il metodo austriaco: scavo per fasi ridotte con sostegno flessibile in rapida successione.",
 tecnologia="Scavo per cunei o mezza sezione (prima la calotta, poi gli spalleti), avanzamenti ridotti 0,5-1,5 m; rivestimento primario rapido in cls proiettato (shotcrete) con rete elettrosaldata e puntali in acciaio o calcestruzzo; copertura a cuscinetto dove il terreno lo richiede; consolidamento preliminare del terreno (iniezioni, pipe umbrella, spiling); rivestimento definitivo in cls gettato in casseri a telaio scorrevole o a telaio autoperforante; strumentazione di controllo (convergenze, cedimenti) per gestire la celerità di intervento.",
 applicazioni="Gallerie in montagna, accessi e allargamenti, gallerie di piccola sezione, cantieri dove la TBM non è economicamente giustificabile.",
 vantaggi="Flessibilità totale di fronte ai cambiamenti geologici, investimenti in apparecchiature contenuti, adattamento in tempo reale alla classe di terreno (approccio osservazionale).",
 limiti="Maggior presenza umana vicino al fronte, cicli più lenti della TBM, qualità del rivestimento dipendente dall'operatività del getto proiettato.",
 costi_e_economia="Ordini di grandezza indicativi: 5.000-20.000 €/m lineare secondo geologia e sezione; il costo dell'osservazione (strumentazione 1-5% del valore lavori) ripaga in sicurezza.",
 casi_real_world="Storico metodo delle gallerie alpine; ampiamente usato per accessi, gallerie di valico secondarie e allargamenti.",
 normative="Linee guida e norme nazionali ed europee per il progetto delle gallerie (raccomandazioni ITA/AITES e documenti nazionali); D.Lgs 81/2008 per i lavori sotterranei; Eurocodice 7.",
 note_cantiere="La regola del NATM è la rapidità: il sostegno primario segue il fronte entro distanze prefissate, e la lettura della strumentazione decide l'accelerazione o il rallentamento del ciclo."),

dict(categoria="No-dig", nome="Microtunneling e perforazioni guidate (tecnologie no-dig)",
 descrizione="La posa di condotte sotto le superfici senza aprire scavi: microtunneling e perforazioni.",
 tecnologia="Microtunneling: macchine a pressione di terra o con miscela bentonitica che scavano e posano tubi in acciaio o cls di diametro 0,4-4 m con guida laser; spinta idraulica continua dai pozzetti di partenza; evacuazione dei detriti con circuito idraulico. Perforazioni guidate (HDD — Horizontal Directional Drilling): tracciato curvo con testa orientabile, allargamento del foro e traino della condotta; utilizzo di fanghi bentonitici per la stabilità. Sistema di rilevamento del percorso con sonde e tracciamento topografico continuo.",
 applicazioni="Attraversamenti di strade, ferrovie, fiumi e corsi d'acqua per fognature, acquedotti, gasdotti, elettrodotti, pozzi di raccolta; interventi dove lo scavo aperto è vietato o impossibile.",
 vantaggi="Nessuna interruzione del traffico superficiale, nessuna trincea, tempi rapidi, minore impatto ambientale e paesaggistico.",
 limiti="Diametri e lunghezze limitate rispetto alle gallerie, sensibilità alla geologia (sassi e ghiaie difficili), gestione dei fanghi di perforazione, costo alto per singolo attraversamento.",
 costi_e_economia="Ordini di grandezza indicativi: microtunneling 1.500-6.000 €/m lineare; HDD 80-300 €/m a seconda di diametro e lunghezza; pozzetti di partenza/arrivo 5.000-50.000 €.",
 casi_real_world="Migliaia di attraversamenti realizzati per reti fognarie e gasdotti sotto autostrade e corsi d'acqua; uso standard nelle metropolitane per i sottoservizi.",
 normative="Riferimenti tecnici ASTT e norme prodotti per le tubazioni; gestione fanghi secondo D.Lgs 152/2006; accordi con i gestori delle infrastrutture attraversate.",
 note_cantiere="La precisione del tracciato è tutto: il monitoraggio continuo del percorso evita la collisione con le strutture esistenti; i fanghi di risulta si gestiscono a ciclo chiuso."),

dict(categoria="Consolidamento terreni", nome="Jet grouting, iniezioni e miglioramento dei terreni",
 descrizione="Trasformare il terreno in un materiale di progetto: colonne, schermi e masse consolidate.",
 tecnologia="Jet grouting: monitor con ugelli ad alta pressione (300-600 bar) che erodono e miscelano il terreno con cemento, formando colonne 0,6-2,5 m di diametro; parametri controllati (pressione, portata, rotazione, sollevamento); iniezioni di consolidamento con sospensioni cementizie o chimiche (silicati, resine) a bassa e media pressione; drenaggi orizzontali e pozzi per l'abbassamento della falda; masse di jet grouting sovrapposte per schermi impermeabili sotto le paratie.",
 applicazioni="Consolidamento sotto fondazioni esistenti, sostegno del fronte di scavo, schermi taglia-acqua, miglioramento dei terreni sotto le pavimentazioni, riempimento di cavità.",
 vantaggi="Intervento dall'interno senza scavi, terreno trattato diventa il sostegno, possibilità di lavorare sotto edifici in esercizio con macchine di modeste dimensioni.",
 limiti="Risultato non sempre uniforme (controllo con prove su carote), consumi di cemento elevati nei terreni organici, pianificazione del tracciato critica vicino a sottoservizi.",
 costi_e_economia="Ordini di grandezza indicativi: jet grouting 150-400 €/m lineare di colonna; iniezioni di consolidamento 50-200 €/m³ trattato; indagini di controllo 5-15% del valore lavori.",
 casi_real_world="Schermi di jet grouting per stazioni metropolitane e sottopassi; consolidamenti sotto fondazioni di edifici storici in operazioni di scavo adiacente.",
 normative="UNI EN 12716 per il jet grouting; UNI EN 12715 per le iniezioni; Eurocodice 7 per il dimensionamento; specifiche di accettazione con carotaggi e prove di resistenza.",
 note_cantiere="La verifica del diametro e della resistenza reale delle colonne si fa su carote e prove non distruttive: il costruttore dichiara i parametri di esercizio e li dimostra a campione."),

dict(categoria="Costruzione ponti", nome="Varo di ponti: spinta, sbalzo e grandi sollevamenti",
 descrizione="I metodi di costruzione dei ponti senza impalcato dal basso: spinta incrementale, sbalzi simmetrici, varo.",
 tecnologia="Spinta incrementale (incremental launching): il viadotto si costruisce dietro l'imbocco e viene spinto in avanti con martinetti su pattini di scorrimento, con testa di varo provvisoria in acciaio; sbalzo simmetrico (cantilever): le campate si gettano a coppie in equilibrio dal pilaio verso il centro, con cavi di precompressione di cantiere; varo dell'impalcato prefabbricato intero o per tratti con grandi gru o cuscinetti di scorrimento; sistemi di controllo geometrico e delle tensioni durante tutte le fasi provvisorie.",
 applicazioni="Viadotti su valli e corsi d'acqua, ponti in zone sismiche, attraversamenti dove l'impalcato dal basso è impossibile (alte luci, corsi d'acqua navigabili).",
 vantaggi="Nessun cantiere in quota esposto e nessun appoggio nel fondovalle, qualità controllata in officina o in banco, adattamento alla morfologia.",
 limiti="Ingegneria di fase complessa (ogni fase provvisoria va verificata), necessità di spazi dietro gli imbocchi per la spinta, equipaggiamenti specializzati.",
 costi_e_economia="Ordini di grandezza indicativi: attrezzature di varo 1-10% del valore strutturale; metodo scelto in fase di gara con preventivo comparato dei cicli.",
 casi_real_world="Viadotti autostradali a sbalzo e a spinta sulle tratte montane; varo di impalcati prefabbricati sulle linee ferroviarie in finestre di blocco.",
 normative="Verifiche di fase secondo NTC 2018 ed Eurocodici con coefficienti parziali delle condizioni provvisorie; piani di montaggio approvati dal progettista; accordi per i vari sopra linee in esercizio.",
 note_cantiere="Le fasi provvisorie NON sono dettagli secondari: la crisi di un impalcato in fase di varo è tra le cause più frequenti di crollo; ogni fase va calcolata e firmata."),

dict(categoria="Casseforme", nome="Casseforme e opere gettate in loco: tecnologie e cedimenti",
 descrizione="Il cassero come tecnologia: casseri tradizionali, a telaio scorrevole, a perdere e autocarranti.",
 tecnologia="Casseratura tradizionale in legno o metallo con puntelli (torri, transenne); caseri a telaio scorrevole per i rivestimenti di galleria (telaio metallico con casseri idraulici che avanzano con l'avanzamento del getto); caseri a perdere in cartone ondulato o materassi metallici per getti di ricongiunzione in profondità; caseri autocarranti (tunnel formwork) per gallerie; caseri per getti di cls di grandi masse con gestione termica (tubi di raffreddamento, getti per strati).",
 applicazioni="Strutture in cls gettate in loco, rivestimenti di galleria, getti di ricongiunzione tra prefabbricati, grandi fondazioni e masse di cls.",
 vantaggi="Adattabilità a qualsiasi geometria, integrazione con armature complesse, uso di materiali semplici disponibili ovunque.",
 limiti="Costo della manodopera di allestimento e disarmo, sensibilità alla taratura dei carichi di getto (rischio sfondamento), tempi legati ai cicli di maturazione.",
 costi_e_economia="Ordini di grandezza indicativi: noleggio caseri tradizionale 15-40 €/m²/mese; caseri scorrevoli per galleria da progetto (significativi investimenti specifici); caseri a perdere 3-10 €/m².",
 casi_real_world="Telai scorrevoli per le gallerie del Quadrilatero e delle grandi opere autostradali; caseri a perdere nei getti di ricongiunzione dei prefabbricati.",
 normative="Requisiti di resistenza e stabilità dei caseri secondo UNI EN 12812 (regole generali di progettazione); verifiche delle strutture provvisionali secondo NTC 2018; gestione termica dei getti di massa con riferimento alle norme sul cls.",
 note_cantiere="Lo sfondamento del cassero durante il getto è il più comune crollo di cantiere: il getto si arresta se i rilevamenti verticali superano i valori ammessi dal piano di getto."),

dict(categoria="Costruzione in mare", nome="Opere marittime e subacquee: cassoni, pali e getti subacquei",
 descrizione="Costruire nel mare e nei corsi d'acqua: opere a riva, cassoni fondati e fondazioni marine.",
 tecnologia="Cassoni in cls prefabbricati o gettati in banchina, varati e posati su letto preparato (scogliere di riempimento, tetrapodi); pali in cls precompresso o acciaio infissi con martelli e battipalo, anche in gruppo; getti di cls subacquei con tubi a perdere (tremie) e miscela autosistemante; piattaforme provvisorie e pontoni per i mezzi; protezione della miscela dalla dispersione con fango bentonitico di risalita; lavorazioni interrotte dalla stagione del mare.",
 applicazioni="Porti, dighe foranee, moli e pontili, opere di presa, condotte sottomarine, attraversamenti fluviali.",
 vantaggi="Fondazioni resistenti a carichi verticali e orizzontali, opere durature in ambiente aggressivo con le giuste protezioni, fattibilità di attraversamenti altrimenti impossibili.",
 limiti="Costi ambientali e di sicurezza molto alti, finestre meteo marine, corrosione aggressiva (cicli di marea), logistiche di cantiere complesse.",
 costi_e_economia="Ordini di grandezza indicativi: opere marittime 2-10 volte il costo analogo a terra; getto subacqueo +30-80% rispetto al getto aereo; pontoni e attrezzature marine a noleggio giornaliero elevato.",
 casi_real_world="Dighe foranee e moli dei porti commerciali italiani realizzati con cassoni e pali; condotte sottomarine posate con barche cantiere.",
 normative="Normativa sulle concessioni demaniali marittime; classificazione ambientale marina per la protezione anticorrosiva (ISO 12944 parte CX/im2); norme sulle costruzioni portuali e sul cls in ambiente marino.",
 note_cantiere="Il mare comanda il cantiere: le finestre di posa si pianificano sulle previsioni meteomarine; il cls in ambiente marino richiede copriferro maggiorato e massa volumica controllata contro la pressione osmotica."),

dict(categoria="Demolizioni", nome="Demolizioni selettive e smontaggi controllati",
 descrizione="Il cantiere al contrario: demolire, smontare e recuperare in sicurezza e con recupero dei materiali.",
 tecnologia="Demolizioni meccaniche con escavatori dotati di pinze e frantumi a ginocchiello; demolizioni selettive (piece by piece) con smontaggio degli elementi in ordine inverso alla costruzione; demolizioni controllate per fasi con sostegni provvisori (puntelli, controventi) e monitoraggio; bonifica preliminare di amianto, PCB e materiali pericolosi prima del cantiere; taglio di cls e acciaio con filo diamantato e demolizioni a microcariche dove serve; separazione in cantiere per il recupero di rottami e inerti.",
 applicazioni="Riqualificazioni urbane, rimozione di ponti e cavalcavia, smantellamento di capannoni industriali, preparazione di aree per nuove costruzioni.",
 vantaggi="Recupero di materiali (rottami ferrosi di valore, inerti da riciclare), riduzione dei rifiuti in discarica, continuità dei servizi vicini con metodi selettivi.",
 limiti="Polveri, rumore e vibrazioni da gestire, rischio crollo non controllato, presenza di materiali pericolosi che impongono bonifiche preventive, costi di smaltimento dei rifiuti speciali.",
 costi_e_economia="Ordini di grandezza indicativi: demolizione meccanica 15-40 €/m³; selettiva con recupero 30-80 €/m³; smaltimento rifiuti speciali 100-500 €/t; ricavo rottami acciaio variabile col mercato.",
 casi_real_world="Smantellamento di viadotti e ponti con fasi notturne e monitoraggio; recupero dei materiali dei capannoni industriali dismessi nelle aree da rigenerare.",
 normative="D.Lgs 81/2008 (Titolo IV) per le demolizioni e i rischi di crollo; D.Lgs 152/2006 per la gestione dei rifiuti da costruzione e demolizione; D.M. 17/6/2015 (recupero degli inerti) per il riciclo; adempimenti su amianto (D.Lgs 257/2006).",
 note_cantiere="La demolizione si progetta come una costruzione inversa: il piano delle fasi con i sostegni provvisori va firmato dal progettista prima del primo colpo di pinza."),

dict(categoria="Organizzazione", nome="Organizzazione del cantiere e costruzione per fasi",
 descrizione="Il cantiere come sistema: layout, fasi, interferenze e continuità operativa.",
 tecnologia="Layout di cantiere con viabilità, aree di stoccaggio, banche di preparazione, posa degli uffici e dei servizi igienici; matrice delle interferenze tra squadre e attrezzature; cronoprogramma con cammino critico che concatena fasi strutturali, impianti e finiture; gestione dei sottoservizi e delle presenze in quota; logistica dei materiali just-in-time o a stock; rotazione dei mezzi di sollevamento; coordinamento BIM tra progettazione e fasi di cantiere (4D).",
 applicazioni="Cantieri edili di ogni dimensione, cantieri urbani vincolati, complessi residenziali e industriali a lotti.",
 vantaggi="Riduzione dei tempi morti e delle interferenze, sicurezza migliorata con aree definite, prevedibilità dei costi e dei consumi, qualità uniforme.",
 limiti="Richiede pianificazione seria e personale dedicato, rigidità del piano che può scontrarsi con imprevisti, investimenti in attrezzature di cantiere.",
 costi_e_economia="Ordini di grandezza indicativi: costi generali di cantiere 8-15% del valore dei lavori; attrezzature e ponteggi 5-12%; ritardi del cronoprogramma costano in genere 0,5-2% del contratto al mese.",
 casi_real_world="Cantieri general contractor con pianificazione 4D e controllo avanzamento settimanale; cantiere urbano a lotti con logistica di trasporti programmata su fasce orarie.",
 normative="D.Lgs 81/2008 per la sicurezza e il piano di sicurezza di cantiere; D.Lgs 36/2023 per gli obblighi di esecuzione e collaudo; obblighi di gestione delle attrezzature (registro, manutenzione, verifiche periodiche).",
 note_cantiere="La buona organizzazione si vede nei dettagli: banche ordinate, materiali etichettati, percorsi pedonali segnati e mezzi revisionati. Il disordine di cantiere è il primo indicatore di rischio."),

dict(categoria="Digitalizzazione cantieri", nome="Metodi digitali di cantiere: 4D, machine control e gemelli digitali",
 descrizione="Come la digitalizzazione cambia i metodi costruttivi: dalla simulazione delle fasi al controllo macchine.",
 tecnologia="BIM 4D che collega il modello 3D al cronoprogramma per simulare le fasi e gli accesi; machine control su escavatori, dozer e livellatrici con antenna GPS/GNSS e sensori che guidano la lama secondo il modello di progetto; stazioni totali robotiche e laser scanner per l'as-built continuo; gemello digitale del cantiere con dati da sensori IoT (polveri, rumore, posizioni mezzi, pesate); droni per rilievi di avanzamento e calcolo volumi; piattaforme di gestione cantieristica (reportistica fotografica, SAL digitali).",
 applicazioni="Grandi opere, scavi di precisione, pavimentazioni stradali, cantieri complessi con molte squadre, monitoraggi di opere esistenti.",
 vantaggi="Eliminazione dei rilievi e dei riferimenti manuali, riduzione degli errori di quota, documentazione oggettiva dell'avanzamento, sicurezza migliorata con meno personale vicino alle macchine.",
 limiti="Investimenti in hardware, software e formazione, dipendenza da copertura satellitare o reti locali, necessità di personale che sappia gestire i dati.",
 costi_e_economia="Ordini di grandezza indicativi: retrofit machine control 5.000-30.000 € per macchina; software 4D/gemello 5.000-50.000 €/anno; servizio droni rilievo 300-1.500 €/giornata.",
 casi_real_world="Cantieri stradali con finitrici guidate da GPS; scavi di fondazioni con escavatori in machine control; gemelli digitali su grandi opere infrastrutturali.",
 normative="Requisiti di sicurezza per l'uso delle macchine guidate da sistema (D.Lgs 81/2008 e norme armonizzate macchine); gestione dei dati di cantiere secondo GDPR quando rilevano persone.",
 note_cantiere="Il machine control non sostituisce il controllo umano: i rilievi a campione restano obbligatori per verificare la calibrazione del sistema sui punti di riferimento."),
]

write_pack("METODI_COSTRUTTIVI_AVANZATI_PACK",
 "Metodi costruttivi avanzati", "FACOLTA_INGEGNERIA", "L2-L3",
 "Top-down, cut&cover, sollevamento edifici, TBM, NATM, no-dig, jet grouting, varo ponti, casseforme, opere marine, demolizioni, organizzazione e digitalizzazione.",
 """# METODI_COSTRUTTIVI_AVANZATI_PACK

**Metodi e tecniche costruttive avanzate**

Top-down, cut & cover, sollevamento e raddrizzamento di edifici, TBM (EPB e doppio scudo), NATM, microtunneling e HDD, jet grouting e miglioramento dei terreni, varo di ponti, casseforme e getti speciali, opere marittime, demolizioni controllate, organizzazione del cantiere, digitalizzazione 4D e machine control.

Schede: 13 (formato JSONL, un oggetto per riga).
""", metodi)

# =====================================================================
# PACK 2 — PREFABBRICAZIONE INDUSTRIALIZZATA
# =====================================================================
prefabbricazione = [
dict(categoria="Sistema costruttivo", nome="Il sistema costruttivo a prefabbricati: logica e campi d'impiego",
 descrizione="L'industrializzazione dell'edilizia: elementi prodotti in stabilimento e assemblati in cantiere.",
 tecnologia="Suddivisione dell'opera in elementi prodotti in centri di prefabbricazione con stampi a riutilizzo ciclico; classificazione in pesante (elementi strutturali in cls gettato in stampo, trasportati e montati con gru) e leggera (pannelli, profili, sistemi a secco); gradi di prefabbricazione dal componente singolo al modulo completo con impianti integrati; logica di progettazione per elementi ripetuti con tolerance di produzione e di montaggio definite.",
 applicazioni="Capannoni industriali, grandi coperture, edilizia residenziale a moduli, scuole e uffici a pareti prefabbricate, ponti con impalcati precompressi.",
 vantaggi="Qualità controllata in stabilimento, tempi di cantiere ridotti del 30-60%, minori rifiuti e maggiore precisione, indipendenza dalle condizioni meteo.",
 limiti="Investimenti in stampi e logistica, rigidità progettuale verso personalizzazioni, trasporti che limitano dimensioni e pesi, connessioni tra elementi critiche.",
 costi_e_economia="Ordini di grandezza indicativi: prefabbricato pesante strutturale 100-250 €/m² di elemento; montaggio e gru 30-80 €/m²; convenienza crescente con la ripetitività degli elementi.",
 casi_real_world="Capannoni industriali in serie in tutta Italia; edilizia scolastica e residenziale con moduli industrializzati; impalcati di ponti prefabbricati precompressi.",
 normative="UNI EN 13369 (requisiti comuni dei prodotti prefabbricati di cls) e norme di prodotto specifiche per elementi; marcatura CE con dichiarazione di prestazione (DOP); NTC 2018 per le strutture.",
 note_cantiere="La prefabbricazione si progetta fin dal concept: ogni foro, ogni giunto e ogni attacco impianti va definito prima della produzione, non in cantiere."),

dict(categoria="Elementi strutturali", nome="Travi, colonne e solai prefabbricati precompressi",
 descrizione="L'ossatura portante industrializzata: elementi in cls precompresso gettati in stampo.",
 tecnologia="Travi in cls precompresso (armature pre-tese o tese in opera) per luci 10-30 m, con sezioni rettangolari, a doppia T o a I; colonne prefabbricate con casseri a piombo e piatti di base bullonati; solai a lastre pretensionate filo pieno (TT o predalles) che funzionano da cassero per il getto di completamento; dispositivi di sollevamento (anelli, attacchi a scomparsa) integrati; giunti di continuità gettati in loco con attese e ferri di ripresa.",
 applicazioni="Coperture di capannoni e centri commerciali, solai di piani intermedi industriali, ponti con impalcato precompresso.",
 vantaggi="Resistenza immediata dopo il montaggio (precompressione), luci elevate con pesi contenuti, superfici di finitura lisce dal calco.",
 limiti="Trasporti e sollevamenti limitano luci e pesi, i giunti di continuità restano getti di cantiere, sensibilità agli urti durante il trasporto.",
 costi_e_economia="Ordini di grandezza indicativi: trave precompressa 60-150 €/m lineare; solaio predalles 40-90 €/m²; montaggio 20-50 €/m² compresa gru.",
 casi_real_world="Impalcati TT diffusi nelle coperture industriali; ponti a travi prefabbricate precompresso sulle rete secondaria.",
 normative="UNI EN 13225 per gli elementi strutturali cavi e UNI EN 1168 per solai alveolari precompressi; UNI EN 13369 per i requisiti comuni; marcatura CE.",
 note_cantiere="La trave appoggia su appoggi elastomerici o piastine con bulloni precaricati: il disallineamento superiore al millimetro si paga in tensioni parasite nel giunto."),

dict(categoria="Pareti", nome="Pannelli di tamponamento e pareti sandwich prefabbricate",
 descrizione="La pelle dell'edificio industrializzata: pannelli portanti e non portanti, isolati in sandwich.",
 tecnologia="Pannelli in cls gettato in stampo liscio o strutturato, armato con reti elettrosaldate e fibre, con attacchi a scomparsa per il sollevamento; pannelli sandwich con strato portante in cls, isolante (XPS, lana minerale, poliuretano) e finitura interna in cls alleggerito o gesso; giunti verticali tra pannelli con profili a camicia o getto di ricongiunzione; pannelli a doppia pelle per facciate continue con sistemi di ancoraggio a scomparsa; superfici di finitura dal calco con smalti o vernici in stabilimento.",
 applicazioni="Tamponamenti di capannoni industriali, facciate di edifici commerciali e logistici, pareti di camere bianche e celle frigorifere, edilizia residenziale a pannelli portanti.",
 vantaggi="Isolamento integrato e controllato in stabilimento, finiture di pregio dal calco, montaggio rapido (centinaia di m² al giorno), qualità termoigrometrica uniforme.",
 limiti="Giunti come punto debole termico e di tenuta all'acqua, trasporti che limitano le dimensioni (4-12 m), difficoltà di modifica in cantiere.",
 costi_e_economia="Ordini di grandezza indicativi: pannello sandwich 60-140 €/m²; pannello portante con finitura 80-180 €/m²; posa 15-35 €/m².",
 casi_real_world="Facciate di centri logistici e GDO con pannelli sandwich; edilizia residenziale con pareti a pannelli portanti prefabbricati.",
 normative="UNI EN 14992 per i pannelli di tamponamento in cls; requisiti di resistenza al fuoco e reazione al fuoco secondo le norme di prodotto; marcatura CE; verifica termica secondo UNI/TS 11300.",
 note_cantiere="I giunti tra pannelli si trattano con sigillanti elastici compatibili o schiume e profili coibentati: la tenuta all'acqua di una facciata a pannelli si vince o si perde sui giunti, mai sul pannello."),

dict(categoria="Moduli", nome="Moduli completi e building system industrializzati (volumi a modulo)",
 descrizione="Dalla cella al modulo intero: edilizia a volumi completi assemblati in stabilimento.",
 tecnologia="Moduli 3D completi di struttura, tamponamenti, serramenti e impianti realizzati in linea di produzione; collegamento dei moduli in cantiere con giunti strutturali, di tamponamento e impiantistici (quick connection) accessibili da zone tecniche; sistemi costruttivi a telaio (frame) o a pannelli portanti (panelized); scalabilità verticale dei moduli con giunzioni bullonate o saldate certificata; possibilità di ri-configurazione e trasporto intermodale (ISO corner).",
 applicazioni="Edilizia residenziale temporanea e permanente, studentati, hotel modulari, uffici temporanei, espansioni di edifici esistenti, health care.",
 vantaggi="Tempi di realizzazione estremamente ridotti (settimane), qualità da produzione seriale, minimo impatto del cantiere su siti sensibili, possibilità di smontaggio e riuso.",
 limiti="Spese di progettazione di sistema e certificazioni, vincoli di trasporto (moduli 3-4 m di larghezza), percezione di edilizia 'a container' da superare, costi non sempre inferiori al tradizionale.",
 costi_e_economia="Ordini di grandezza indicativi: modulo residenziale completato 1.200-2.500 €/m²; soluzioni speciali (camere bianche, celle) fino a 4.000 €/m²; risparmio di tempo 40-70%.",
 casi_real_world="Hotel e studentati modulari realizzati in tempi record; espansioni ospedaliere con moduli in emergenza; case per il disagio abitativo con moduli riutilizzabili.",
 normative="Marcatura CE dei componenti e procedure di valutazione per i sistemi costruttivi; NTC 2018 per le verifiche strutturali del sistema; agibilità secondo regolamenti edilizi locali.",
 note_cantiere="Il modulo è un prodotto finito che viaggia su strada: la logistica (permessi eccezionali, gru, sequenze di consegna) progetta il cantiere più della costruzione."),

dict(categoria="Unioni", nome="Unioni e giunti tra elementi prefabbricati",
 descrizione="Il punto critico del sistema: come i prefabbricati diventano un'opera unica.",
 tecnologia="Giunti strutturali gettati in loco: casseri a perdere o ricongiunzione a ferri di ripresa emersi, getto con cls ad alta resistenza e additivi espansivi (o ritiro compensato); giunti a secco con profili metallici saldati o bullonati e riempimento con malta espansiva; connessioni emi-incastrate (denti e spallamenti) che trasmettono sforzi per contatto; giunti di dilatazione che separano setti strutturali; sigillatura dei giunti di tamponamento con poliuretano, silicone o profili a labirinto; catene di continuità elettrica e impiantistica attraverso i giunti.",
 applicazioni="Collegamenti trave-pilastro, continuità dei solai, giunti tra pannelli di tamponamento, dilatazioni di grandi edifici prefabbricati.",
 vantaggi="Rigidezza e monoliticità dopo il getto di ricongiunzione, velocità del montaggio a secco dove possibile, ispezionabilità delle connessioni.",
 limiti="I giunti gettati sono cantieri nel cantiere (umidità, temperature, stagionatura), i giunti a secco richiedono tolleranze strette, ogni giunto è potenziale punto di infiltrazione e di discontinuità termica.",
 costi_e_economia="Ordini di grandezza indicativi: getto di ricongiunzione 30-80 €/m lineare di giunto; connessioni metalliche speciali da progetto (100-500 €/punto secondo carico).",
 casi_real_world="Capannoni con colonne a dente che alloggiano le travi; edilizia residenziale con giunti gettati tra pannelli portanti.",
 normative="NTC 2018 per la verifica dei giunti come connessioni strutturali; specifiche di prodotto per malte e sistemi di connessione; norme sui cls per getti di ripresa (additivi espansivi).",
 note_cantiere="Il getto di ricongiunzione va bagnato e stagionato come ogni cls: accelerarlo con il getto 'a freddo' senza controllo produce i famosi giunti che si aprono dopo un anno."),

dict(categoria="Trasporti", nome="Trasporti e sollevamento dei prefabbricati",
 descrizione="Dal cancello dello stabilimento al punto di montaggio: la logistica del pesante.",
 tecnologia="Trasporti su rimorchi modulari (carrelloni) con carichi fino a 40-60 t per elementi standard e mezzi eccezionali per i grandi elementi (travi di ponte fino a 100+ t); vincoli di gabarit stradale (larghezza 2,5-3,5 m, altezza 4-4,5 m) che decidono le dimensioni di fabbrica; sistemi di sollevamento con ganci, bilancieri e traverse per distribuire i carichi agli attacchi previsti; gru a torre, gru mobili (portata 50-500 t) e gantry crane per i grandi impianti; piani di sollevamento con angoli di inclinazione e punti di presa certificati.",
 applicazioni="Ogni cantiere con prefabbricati pesanti: capannoni, ponti, pannelli portanti, moduli.",
 vantaggi="Elementi posati in ore invece di settimane di getto e stagionatura, costruttivamente indipendente dal meteo (salvo vento forte per le gru).",
 limiti="Costi di trasporto mezzi eccezionali elevati, necessità di strade e accessi idonei, il vento sopra i limiti ferma le gru, le tabelle di portata delle gru governano i cicli.",
 costi_e_economia="Ordini di grandezza indicativi: trasporto ordinario 1-3 €/t·km; mezzo eccezionale con scorte 3.000-15.000 €/viaggio; noleggio gru mobile 1.500-8.000 €/giornata.",
 casi_real_world="Travi di ponte da 40-60 m trasportate su più carrelli con autista al traino; moduli residenziali consegnati a 10-20 al giorno su cantiere attrezzato.",
 normative="Codice della strada per trasporti eccezionali (autorizzazioni, scorte); verifiche di sollevamento come attrezzature di lavoro (D.Lgs 81/2008); piani di manutenzione e verifica delle attrezzature di sollevamento.",
 note_cantiere="Il piano di sollevamento scritto (carichi, angoli, vento massimo, raggio) è parte del PSC: non si solleva niente che non sia nel piano firmato dal responsabile."),

dict(categoria="Centri di produzione", nome="Centri di prefabbricazione: stabilimenti e cicli di produzione",
 descrizione="Dentro lo stabilimento: stampi, cicli, controllo qualità e marcatura.",
 tecnologia="Banchi di getto in acciaio o cls con piano di calibratura per garantire la planarità (±1-2 mm); stampi modulari per travi, pannelli e moduli con pareti a magneti o profili regolabili; ciclo di getto con betoniere a caricamento controllato e getto in vibrazione; camere di stagionatura controllata (termoigrometrica) con curing accelerato; aree di sformo e stoccaggio a magazzino con appoggi puntuali; laboratorio interno per prove su cls e su armature; tracciabilità di ogni elemento con codice e DOP.",
 applicazioni="Stabilimenti di prefabbricati per edilizia, cementerie, produzione di elementi per ponti e grandi opere.",
 vantaggi="Ripetibilità della qualità in ambiente controllato, produzione continua indipendente dal meteo, ottimizzazione dei consumi di cls e armature.",
 limiti="Investimenti iniziali alti (milioni di euro per un centro attrezzato), rigidità della produzione verso variazioni del progetto, costi di manutenzione degli stampi.",
 costi_e_economia="Ordini di grandezza indicativi: costruzione di uno stabilimento 2-20 M€ secondo capacità; costo di produzione 60-70% del prezzo di vendita dell'elemento.",
 casi_real_world="Reti di centri di prefabbricazione con copertura nazionale; stabilimenti dedicati per grandi opere (gallerie, ponti) con stampi specifici.",
 normative="UNI EN 13369 e norme di prodotto per la marcatura CE; sistema di controllo di produzione in fabbrica (FPC) documentato; gestione degli scarichi e dell'acqua di processo secondo D.Lgs 152/2006.",
 note_cantiere="Lo stabilimento è un cantiere continuo: la manutenzione dei calchi e la taratura delle bilance sono la qualità del prodotto finito."),

dict(categoria="Facciate", nome="Facciate continue e sistemi di rivestimento prefabbricati",
 descrizione="La facciata come sistema industrializzato: pannellature leggere, ventilate e continue.",
 tecnologia="Sistemi a taglio termico con montanti e traversini in alluminio (facciata continua a montanti visibili o a griglia coperta) vetrati con doppie o triple lastre; facciate ventilate con pannelli di rivestimento (gres, fibrocemento, alluminio composito, cls fibrorinforzato) ancorati a sottostrutture con camera d'aria isolata; pannelli compositi (ACM) con nucleo in polietilene o minerali a seconda dei requisiti di reazione al fuoco; sistemi di ancoraggio a scomparsa con staffe inox o alluminio; giunti di dilatazione a taglio orizzontale e verticale.",
 applicazioni="Uffici, direzionali, edilizia commerciale, riqualificazioni energetiche di facciate esistenti (overcladding).",
 vantaggi="Rapida posa con produzione su misura, qualità di finitura controllata, possibilità di retrofit energetico senza sgombero dell'edificio, ampia libertà architettonica.",
 limiti="Costi dei sistemi a montanti, manutenzione dei sigillanti e dei giunti, complessità dei punti singolari (angoli, fori, parapetti), reazione al fuoco dei compositi da verificare.",
 costi_e_economia="Ordini di grandezza indicativi: facciata ventilata 180-400 €/m²; facciata continua vetrata 350-800 €/m²; retrofit overcladding 150-350 €/m².",
 casi_real_world="Direzionali con facciate continue vetrate; rivestimenti ventilati di edilizia pubblica e privata; retrofit energetici con pannelli sopra facciate esistenti.",
 normative="Requisiti di reazione/resistenza al fuoco secondo il Codice prevenzione incendi (D.Lgs 139/2006) e DM applicativi; UNI EN 13830 per le facciate continue; marcatura CE dei componenti e sistemi ETA.",
 note_cantiere="La posa di una facciata continua avviene da piattaforme o da dentro l'edificio: il piano di posa definisce la sequenza dei piani e i carichi di vento ammessi per le piattaforme."),

dict(categoria="Strutture ibride", nome="Strutture ibride cls-acciaio e collaboranti",
 descrizione="Il meglio dei due materiali: sezioni miste acciaio-cls e sistemi collaboranti.",
 tecnologia="Travi e colonne composte con profilo metallico inglobato in cls (steel reinforced concrete) o cls appoggiato su profilo (doppia T con testa superiore collaborante); connettori a taglio (tasselli, perni Nelson o reti) che garantiscono la collaborazione tra acciaio e cls; solai collaboranti con lamiera grecata (piena o forata) funzionante da cassero armato e flangia compressa con il getto di cls; travi di rinforzo incamiciate; verifiche secondo l'Eurocodice 4 con interazione parziale o completa.",
 applicazioni="Edifici alti, grandi luci, solai rapidi di edilizia commerciale e industriale, rinforzi di strutture esistenti, ponti con impalcato misto.",
 vantaggi="Sfrutta la resistenza a compressione del cls e a trazione dell'acciaio, solai veloci senza caseri tradizionali, rigidezza elevata con pesi contenuti, risparmio sui caseri.",
 limiti="Costo dei connettori e delle verifiche di interazione, il getto di completamento resta in cantiere, protezione antincendio dei profili esposti, problemi di ritiro del cls nella zona collaborante.",
 costi_e_economia="Ordini di grandezza indicativi: lamiera grecata collaborante 15-35 €/m²; solaio collaborante completo 60-120 €/m²; travi composte 2-4 volte il costo del solo profilo.",
 casi_real_world="Solai in lamiera grecata standard nell'edilizia industriale e commerciale; ponti a struttura mista acciaio-cls per luci elevate.",
 normative="Eurocodice 4 (UNI EN 1994) per le strutture composte; UNI EN 1090-2 per i profili; NTC 2018 per l'applicazione nazionale.",
 note_cantiere="I connettori si saldano su profilo zincato con procedure qualificate e ritoccati dopo; la lamiera grecata piena evita l'appoggio di caseri e accelera i cicli di solaio."),

dict(categoria="Qualità", nome="Qualità, collaudo e marcatura CE dei prefabbricati",
 descrizione="La garanzia dell'elemento prefabbricato: certificazioni, prove e documentazione.",
 tecnologia="Sistema di controllo di produzione in fabbrica (FPC) documentato e auditato; certificati di conformità del cls (resistenza, copriferro, additivi) per ogni gettata; prove di laboratorio su campioni prelevati a rotazione (resistenza a compressione, assorbimento, modulo elastico); verifica dimensionale e di planarità degli elementi prima dello stoccaggio; prove di carico su elementi tipo ogni campagna; marcatura CE con dichiarazione di prestazione (DOP) che riporta classe di resistenza, esposizione ambientale, reazione al fuoco; fascicolo tecnico dell'elemento consegnato al cantiere.",
 applicazioni="Ogni elemento prefabbricato destinato al mercato italiano ed europeo, dai pannelli ai grandi elementi strutturali.",
 vantaggi="Tracciabilità completa elemento per elemento, difetti individuati in stabilimento invece che in cantiere, scontistica sulle polizze di cantiere con prodotti certificati.",
 limiti="Onere documentale per i piccoli produttori, costi delle prove di laboratorio, il CE copre il prodotto non il progetto dell'opera (resta onere del progettista).",
 costi_e_economia="Ordini di grandezza indicativi: costi di qualità e certificazione 3-8% del prezzo dell'elemento; prove di carico su campagna 2.000-10.000 €.",
 casi_real_world="Elementi CE marcatura con DOP tracciabile via codice QR in tutti i centri di prefabbricazione accreditati.",
 normative="UNI EN 13369 (marcatura CE e DOP); UNI EN 206 per la specificazione del cls; regolamento CPR (UE 305/2011); NTC 2018 per la verifica strutturale in opera.",
 note_cantiere="La DOP si controlla alla consegna: se manca o riporta prestazioni inferiori al progetto, l'elemento non si monta — la verifica a monte costa un viaggio, quella a valle un cantiere."),

dict(categoria="Economia", nome="Economia dell'industrializzazione: quando conviene il prefabbricato",
 descrizione="La scelta tra getto in loco e prefabbricato si gioca su tempi, ripetitività e costi totali.",
 tecnologia="Analisi comparativa per ciclo di vita tra soluzione tradizionale e industrializzata: costo diretto (produzione, trasporto, montaggio), costi indiretti (cantiere ridotto, tempi, gru), costi di esercizio (qualità, manutenzione), costi di rischio (meteo, manodopera scarsa); parametri di ripetitività (numero di elementi identici, standardizzazione delle misure); logistica di progetto che determina il raggio economico dello stabilimento (tipicamente 100-300 km).",
 applicazioni="Scelta costruttiva in fase di progettazione e gara: capannoni, scuole, residenze, ospedali, ponti.",
 vantaggi="Con ripetizioni >20-30 elementi identici la fabbrica batte quasi sempre il getto in loco; tempi certi riducono i costi finanziari; minori rifiuti e maggiore sicurezza abbassano i costi indiretti.",
 limiti="Progetti unici o fortemente personalizzati perdono il vantaggio; i costi di trasporto oltre il raggio economico mangiano il risparmio; la rigidità di commessa penalizza le variazioni.",
 costi_e_economia="Ordini di grandezza indicativi: risparmio 5-15% sul costo diretto in serie ripetute; riduzione dei tempi 30-60% con conseguente minore costo finanziario; costi di variazione in corso +50-200%.",
 casi_real_world="Programmi di edilizia scolastica e residenziale pubblica con gare a sistema costruttivo; capannoni logistici in serie con tempi di consegna certificati.",
 normative="D.Lgs 36/2023 per gli appalti integrati e il project financing dove il sistema costruttivo è parte dell'offerta; NTC 2018 per la scelta delle strutture.",
 note_cantiere="Il prefabbricato conviene quando il progetto si 'sistema' sui moduli prima della commessa: chi progetta il dettaglio dopo aver comprato gli elementi paga il doppio."),
]

write_pack("PREFABBRICAZIONE_INDUSTRIALIZZATA_PACK",
 "Prefabbricazione e industrializzazione edilizia", "FACOLTA_TECNOLOGIA_E_COSTRUZIONE", "L2",
 "Sistema costruttivo, elementi strutturali, pannelli, moduli, unioni, trasporti, centri di produzione, facciate, strutture ibride, qualità CE, economia.",
 """# PREFABBRICAZIONE_INDUSTRIALIZZATA_PACK

**Prefabbricazione e industrializzazione dell'edilizia**

Logica del sistema costruttivo, elementi strutturali precompressi, pannelli e sandwich, moduli completi, unioni e giunti, trasporti e sollevamento, centri di produzione e marcatura CE, facciate continue e ventilate, strutture ibride cls-acciaio, economia dell'industrializzazione.

Schede: 11 (formato JSONL, un oggetto per riga).
""", prefabbricazione)

# =====================================================================
# PACK 3 — PERIZIE, STIME E ASSICURAZIONI
# =====================================================================
perizie = [
dict(categoria="Estimo", nome="La perizia immobiliare: metodi di stima",
 descrizione="Determinare il valore di un immobile: metodo comparativo, sintetico e analitico.",
 tecnologia="Metodo comparativo di mercato: correzione delle quotazioni di immobili simili con tariffe di differenziazione (OMI quando disponibile); metodo del costo di ricostruzione: valore a nuovo al netto delle obsolescenze fisiche, funzionali ed economiche; metodo reddituale (capitalizzazione del reddito lordo e netto con tassi di capitalizzazione di mercato); metodo sintetico catastale (tariffe OMI per tipologie e zone OMI); valutazione a stima sintetica per singole unità con coefficienti di merceologia (vetustà, piano, esposizione, ascensore).",
 applicazioni="Compravendite, successioni, divisioni, garantie bancarie, bilanci, perizie giudiziarie, stime per danno.",
 vantaggi="Metodi consolidati e accettati in giudizio, disponibilità di banche dati (OMI, Borsa Immobiliare, quotazioni di zona), ripetibilità e trasparenza dei calcoli.",
 limiti="Sensibilità alla disponibilità di comparabili reali, le quotazioni medie OMI mascherano le singolarità, la vetustà e le obsolescenze richiedono giudizio tecnico.",
 costi_e_economia="Ordini di grandezza indicativi: perizia semplice 300-800 €; perizia giudiziale CTU 800-3.000 € secondo complessità; valutazioni complesse con ispezioni strumentali 2.000-10.000 €.",
 casi_real_world="Tariffe OMI pubblicate semestralmente per zone omogenee in tutti i capoluoghi; quotazioni Borsa Immobiliare di Tecnoborsa per il residenziale.",
 normative="Prezzi-valori OMI del Dipartimento delle Finanze; norme UNI sulla valutazione immobiliare e sulla perizia; codice deontologico dei periti.",
 note_cantiere="La stima si difende con la trasparenza: fonti citate, tariffe di correzione espresse e stato d'uso ispezionato di persona. La perizia da scrivania non regge in tribunale."),

dict(categoria="Stima lavori", nome="Perizia di stima dei lavori: estimo di cantiere",
 descrizione="Valutare il valore di opere in corso, di opere da eseguire e di varianti: l'estimo applicato al cantiere.",
 tecnologia="Stima per computo metrico estimativo con prezzi di mercato dei singoli lavori (prezzari DEI, CIFE, Camere di Commercio, prezzi reali di contratto); metodo dei prezzi parametrici per opere standardizzate (€/m² per tipologie edilizie, €/m³ di cls); stima delle opere provvisionali e dei trasporti; perizia di avanzamento lavori con scomputo delle opere eseguite (stato avanzamento alla data); stima delle varianti in corso d'opera con confronto dei prezzi unitari del contratto.",
 applicazioni="Stime per SAL e chiusure contabili, valutazione di opere incompiute, stime per espropri, perizie di variante, contenziosi su prezzi.",
 vantaggi="Metodo oggettivo basato su quantità e prezzi verificabili, accettabilità in arbitrato e giudizio, raffronto diretto con il contratto in corso.",
 limiti="Dipendenza dalla qualità del computo di base, prezzi di mercato variabili nel tempo e per zona, le opere speciali richiedono listini dedicati.",
 costi_e_economia="Ordini di grandezza indicativi: prezzario DEI annuale in abbonamento; estimo completo di una villa 500-2.000 €; perizia di avanzamento lavori 300-1.000 €.",
 casi_real_world="Prezzari DEI e CIFE come riferimento per le stime di enti pubblici e CTU; prezzi reali dei contratti regionali per le opere pubbliche.",
 normative="Prezzari ufficiali di riferimento (DEI, CIFE); per gli enti pubblici, prezzario dei lavori pubblici della regione; UNI 11652 per la valutazione di beni e opere.",
 note_cantiere="Nella stima di varianti vale il principio di continuità contrattuale: i prezzi del contratto prevalgono quando le opere sono comparabili; i nuovi prezzi si giustificano con listini e mercato."),

dict(categoria="Giustizia", nome="CTU e CTP nel processo civile",
 descrizione="La consulenza tecnica in tribunale: ruolo, doveri e svolgimento dell'incarico.",
 tecnologia="CTU (Consulente Tecnico d'Ufficio) nominato dal giudice (art. 61 c.p.c.) con compito di fornire elementi tecnici di giudizio con oggettività e imparzialità; CTP (Consulente Tecnico di Parte) assiste il proprio assistito (art. 84 c.p.c.) con accesso all'incartamento e diritto di replica alle CTU; svolgimento: accettazione e giuramento, deposito di quesiti, sopralluoghi, consulenze collegiali, redazione della relazione con illustrazione dei criteri adottati; le parti possono richiedere chiarimenti integrativi (art. 87 c.p.c.).",
 applicazioni="Contenziosi edilizi (difetti, ritardi, vizi di conformità), divisioni, confini, responsabilità professionali, sinistri, valutazioni immobiliari.",
 vantaggi="La CTU è il mezzo di prova tecnico privilegiato per il giudice; il CTP permette alla parte di controllare e contestare la consulenza; criteri e metodi esposti rendono la prova verificabile.",
 limiti="Tempi lunghi del processo, rischio di consulenze di parte polarizzate, responsabilità civile e penale del consulente per dolo o colpa grave, onorari regolati secondo parametri forensi.",
 costi_e_economia="Ordini di grandezza indicativi: onorari CTU secondo i parametri forensi vigenti (aggiornati periodicamente con decreto ministeriale); CTP 1.500-10.000 € secondo controversia.",
 casi_real_world="Contenziosi su vizi di costruzione risolti sulla CTU strutturale; divisioni ereditarie con stime CTU di immobili multipli.",
 normative="Artt. 61 e ss. c.p.c. (CTU); artt. 84-87 c.p.c. (CTP); parametri forensi vigenti per gli onorari.",
 note_cantiere="Il consulente risponde dei propri atti: la relazione CTU va firmata con coscienza dei criteri, delle fonti e dei limiti dell'indagine; il silenzio su un vizio noto è colpa grave."),

dict(categoria="Responsabilità", nome="Responsabilità della costruzione: vizi, decadenze e garanzie legali",
 descrizione="Chi risponde di cosa nell'edilizia: i termini di decadenza e le garanzie per legge.",
 tecnologia="Responsabilità decennale per rovina dell'opera o gravi difetti di conservazione e per difetti che rendono l'opera inidonea all'uso (10 anni, art. 1669 c.c.); azioni per difformità e difetti di qualità entro 1 anno dalla consegna (art. 1667 c.c.) e per i difetti rilevabili successivamente 2 anni (art. 1668 c.c.); responsabilità del costruttore e di chi ha venduto l'immobile per vizi gravi; responsabilità del progettista secondo il contratto e per colpa professionale; azione diretta del terzo acquirente contro il costruttore entro i termini; decorrenza dei termini dalla consegna dell'opera.",
 applicazioni="Contenziosi su difetti edilizi, vendite di immobili con vizi, gestione delle garanzie di cantiere, assicurazioni decennali.",
 vantaggi="Quadro di responsabilità consolidato che protegge acquirenti e committenti; i termini di decadenza sono certi e stimolano la verifica in consegna; le garanzie legali convivono con le assicurazioni.",
 limiti="Termini brevi per le difformità (1 anno) che richiedono verifiche immediate; la prova del vizio e del nesso causale è complessa; contenziosi lunghi e costosi.",
 costi_e_economia="Ordini di grandezza indicativi: consulenza pre-contenzioso su difetti 500-3.000 €; contenzioso decennale 10.000-100.000 € di spese secondo valore.",
 casi_real_world="Giurisprudenza consolidata su vizi strutturali e umidità; sentenze di legittimità su decorrenza dei termini dalla consegna effettiva.",
 normative="Artt. 1667, 1668, 1669 c.c. (responsabilità per rovina e difetti dell'opera); artt. 2050 e ss. c.c. per le responsabilità professionali; giurisprudenza di legittimità e merito.",
 note_cantiere="Alla consegna dell'opera si fa la verifica di conformità completa: i difetti non segnalati in consegna si presumono accettati salvo quelli occulti o gravi."),

dict(categoria="Assicurazioni", nome="Assicurazioni del cantiere: CAR, postuma e tutela legale",
 descrizione="Il sistema assicurativo che copre il cantiere durante e dopo i lavori.",
 tecnologia="Polizza CAR ( Contractor's All Risks): copre i danni materiali diretti all'opera in corso di costruzione (incendio, eventi naturali, crollo, errori di esecuzione non professionali); polizza decennale postuma: copre per 10 anni la responsabilità civile per rovina o gravi difetti (obbligatoria quando l'acquisto è assistito da finanziamento ipotecario, ex D.L. 223/2006); RC professionale per progettisti e direzione lavori; polizza tutela legale per le spese di difesa; RC cantieri per danni a terzi; decennale prodotti per i produttori di elementi e componenti.",
 applicazioni="Ogni cantiere edile, gli studi professionali, le imprese produttrici di componenti edilizi.",
 vantaggi="Trasferimento del rischio catastrofale, accesso al credito ipotecario (postuma), protezione professionale dei tecnici, continuità dell'impresa in caso di sinistro grave.",
 limiti="Premi elevati sulla postuma (1-3% del valore ricostruzione), franchigie e massimali da calibrare, esclusioni (difetti professionali nella CAR), iter di liquidazione complessi.",
 costi_e_economia="Ordini di grandezza indicativi: CAR 0,3-1% del valore lavori; postuma 1-3% del valore di ricostruzione; RC professionale 0,5-2% del fatturato professionale.",
 casi_real_world="Cantiere coperti da CAR con massimali proporzionati all'opera; postuma obbligatoria su mutui ipotecari per legge (D.L. 223/2006).",
 normative="D.L. 223/2006 (convertito in L. 248/2006) con l'obbligo di polizza decennale per i mutui ipotecari; Codice delle Assicurazioni Private (D.Lgs 209/2005); condizioni di polizza tipo RC cantieri.",
 note_cantiere="La CAR copre i danni materiali, non gli errori di progetto: la distinzione decide i contenziosi tra assicurazione di cantiere e RC professionale."),

dict(categoria="Danno tecnico", nome="Perizia dei danni edilizi: infiltrazioni, umidità e dissesti",
 descrizione="Individuare causa, entità e rimedio del danno: la perizia tecnica sui vizi più comuni.",
 tecnologia="Indagine con ispezione visiva, rilevamento planimetrico dei dissesti (mappe di fessurazione), termografia IR per individuare ponti termici e infiltrazioni, misura di umidità nei materiali con igrometro e carburo, misura di spessori e copriferro con radiodensimetro, analisi chimiche su malte e cls, auscultazione strumentale (estensimetri, pendoli, celle di carico) per i dissesti strutturali; determinazione del percorso delle infiltrazioni con prove di tenuta e rilevamento in episodi di pioggia; correlazione temporale con eventi (lavori vicini, terremoti, stagioni).",
 applicazioni="Sinistri su immobili, contenziosi tra confinanti, verifiche pre-acquisto, bonifiche per umidità di risalita e condensa, verifiche post-terremoto.",
 vantaggi="Strumenti non distruttivi che localizzano il danno senza danneggiare, metodo che separa cause (risalita vs condensa vs infiltrazione), documentazione oggettiva per assicurazioni e tribunali.",
 limiti="Le cause multiple si sovrappongono e rendono la diagnosi complessa, le prove chimiche richiedono laboratori, il costo della diagnosi completa incide su interventi modesti.",
 costi_e_economia="Ordini di grandezza indicativi: perizia su infiltrazioni 400-1.500 €; diagnosi strutturale completa 1.500-8.000 €; monitoraggio estensimetrico 2.000-15.000 €.",
 casi_real_world="Termografia come prova standard nei contenziosi su ponti termici; mappe di fessurazione obbligatorie nei monitoraggi post-sisma.",
 normative="Linee guida per la valutazione del danno sismico (schede AeDES e successivi aggiornamenti); norme UNI per le misure di umidità dei materiali edilizi; giurisprudenza sulle cause di umidità.",
 note_cantiere="Prima di autorizzare un'impermeabilizzazione chiedere sempre la diagnosi della causa: risanare il sintomo (il segno di umidità) lasciando la causa (il ponte termico) significa pagare due volte."),

dict(categoria="Sopralluogo", nome="Collaudo tecnico-amministrativo e perizia di conformità",
 descrizione="La verifica finale: cosa controlla il collaudo e cosa certifica la perizia di conformità.",
 tecnologia="Collaudo tecnico-amministrativo per le opere pubbliche: verifica della conformità dell'opera al progetto e ai capitolati, esame delle relazioni di cantiere, prove e collaudi di singole categorie, verbale di collaudo con giudizio finale; collaudi funzionali di impianti (efficienza, tarature, certificazioni); perizia di conformità per opere private o varianti: verifica che le opere eseguite corrispondano al progetto approvato, con sopralluogo metrico e fotografico; rilascio della certificazione energetica finale e delle dichiarazioni di conformità impianti (Dichiarazione di Conformità CEI 64-8 per gli elettrici, UNI 7129 per gas, DM 37/08 per gli impianti termoidraulici).",
 applicazioni="Consegna delle opere pubbliche, chiusura delle pratiche edilizie, collaudo di impianti, verifica di varianti in corso d'opera, agibilità.",
 vantaggi="Certificazione oggettiva dello stato finale, tutela del committente, documentazione per la manutenzione e l'assicurazione, chiusura formale dei contratti.",
 limiti="Onere di organizzazione e documentazione, il collaudatore deve essere indipendente, i tempi si allungano se la documentazione di cantiere è carente.",
 costi_e_economia="Ordini di grandezza indicativi: collaudo opere pubbliche 1-5% del valore lavori secondo entità; perizia di conformità edilizia 300-1.500 €; collaudi funzionali impianti 200-800 € ad impianto.",
 casi_real_world="Collaudi di ponti e viadotti con prove di carico; perizie di conformità nelle pratiche di agibilità presso i comuni.",
 normative="D.Lgs 36/2023 per i collaudi delle opere pubbliche; DM 37/2008 per le dichiarazioni di conformità impianti; UNI CEI 64-8 e UNI 7129 per le dichiarazioni impiantistiche; regolamenti edilizi comunali per l'agibilità.",
 note_cantiere="Il collaudo inizia al primo giorno di cantiere: il libro firme, le relazioni di collaudo dei singoli corpi di stato e le prove di laboratorio altrimenti il collaudo finale diventa una fotografia senza memoria."),

dict(categoria="Catasto", nome="Perizie catastali: ricostruzione della storia formale e sanatoria",
 descrizione="Verificare cosa dice il catasto e cosa c'è in realtà: la perizia per regolarizzare.",
 tecnologia="Ricostruzione della storia formale dell'immobile (visure catastali di tutti gli anni, atti di provenienza, planimetrie, successioni); raffronto tra stato di fatto (rilievo) e stato di diritto (catasto): superfici, destinazioni d'uso, distanze, vincoli; individuazione delle difformità edilizie e catastali; valutazione delle sanabilità (DPR 380/2001, Titolo IV per le irregolarità edilizie, titolo IX per i difformi catastali con le sanatorie specifiche); pratiche DOCFA e SCORM per gli aggiornamenti; verifica delle successioni degli atti e delle omessa denuncia di variazione.",
 applicazioni="Acquisti immobiliari, pratiche di sanatoria (condono edilizio o sanatoria catastale), divisioni, accatastamenti di nuove costruzioni, verifiche pre-mutuo.",
 vantaggi="Ricostruzione documentale completa che previene contenziosi, individuazione delle sanabilità prima dell'acquisto, pratiche corrette al primo colpo.",
 limiti="Archivi storici incompleti, cambi di confini e riclassificazioni catastali da interpretare, le sanatorie hanno termini e requisiti diversi, il tecnico non sostituisce il notaio.",
 costi_e_economia="Ordini di grandezza indicativi: perizia catastale con ricostruzione storica 300-1.200 €; pratica DOCFA 150-500 €; sanatoria completa 800-3.000 €.",
 casi_real_world="Pratiche di sanatoria catastale (Titolo IX DPR 380/2001) per difformità documentali; ricostruzioni di conformità edilizia ante-DPR 380/2001 per acquisti sicuri.",
 normative="DPR 380/2001 (Testo Unico Edilizia, Titolo IV sanatoria edilizia, Titolo IX sanatoria catastale); D.M. 2 gennaio 1998 n. 28 (Do.C.Fa.); DPR 138/1998 (sistema catastale).",
 note_cantiere="Prima di comprare si chiede sempre la perizia di regolarità: un difetto di sanatoria scoperto dopo il rogito costa molto più della perizia."),

dict(categoria="Sinistri", nome="Perizia assicurativa e liquidazione dei sinistri edilizi",
 descrizione="Come si valuta e si liquida un sinistro su costruzioni e cantiere.",
 tecnologia="Accertamento del sinistro con sopralluogo immediato, documentazione fotografica e raccolta di testimonianze; determinazione della entità del danno (perizia di massima per le procedure semplificate, perizia completa per i danni complessi); applicazione delle condizioni di polizza (massimali, franchigie, esclusioni, sottassicurazione con la regola proporzionale); liquidazione del danno diretto (costo di riparazione) e del danno indiretto (perdita di godimento, mancato esercizio); perizia di parte e perizia di contro di assicurazione; conciliazione e, se necessario, arbitrato o giudizio.",
 applicazioni="Sinistri CAR su cantieri, danni da eventi naturali su immobili, incendi, crolli, danni da terzi, contenziosi con le compagnie.",
 vantaggi="Liquidazione rapida se la documentazione è completa, perizia di parte che controbilancia l'assicurazione, percorsi stragiudiziali che risparmiano tempo e costi.",
 limiti="Le compagnie applicano franchigie e massimali spesso contestati, la prova del valore del bene e del danno è onere dell'assicurato, i tempi si allungano nei sinistri complessi.",
 costi_e_economia="Ordini di grandezza indicativi: perizia di massima 150-400 €; perizia completa di sinistro 500-3.000 €; onorario CTU assicurativo secondo i parametri forensi.",
 casi_real_world="Procedure semplificate di liquidazione per i sinistri di modesta entità; contenziosi su sottassicurazione e su cause escluse.",
 normative="Codice delle Assicurazioni Private (D.Lgs 209/2005) e condizioni di polizza tipo; regola proporzionale della sottassicurazione (art. 1907 c.c.); parametri forensi per le perizie.",
 note_cantiere="Dopo un sinistro la documentazione vale oro: foto prima dei ripristini, registrazione dei danni in continuo, conservazione dei pezzi danneggiati fino al sopralluogo dell'assicurazione."),

dict(categoria="Esercizio", nome="Audit tecnico di edifici in esercizio e pre-acquisto",
 descrizione="La perizia periodica e la due diligence tecnica: lo stato di salute dell'edificio.",
 tecnologia="Audit strutturale: verifica di fessurazioni, degrado del cls (carbonatazione, corrosione armature), stato dei solai e dei tetti; audit energetico: analisi della classe energetica, ispezioni termografiche, verifica degli impianti e delle loro età residue; audit impiantistico: stato di manutenzione, certificazioni, rischio legionella, conformità; audit antincendio e accessibilità: stato dei mezzi di estinzione, percorsi di esodo, agibilità dei locali; stima dei costi di manutenzione e miglioramento programmato (10 anni); redazione del piano di manutenzione previsionale.",
 applicazioni="Acquisto di immobili commerciali e industriali, gestione di patrimoni immobiliari, condomini, scuole e uffici pubblici, property management.",
 vantaggi="Fotografia completa dello stato reale, pianificazione dei costi futuri, leva negoziale sull'acquisto, programmazione delle manutenzioni anziché emergenze.",
 limiti="Ispezioni limitate dalle parti non accessibili, i costi futuri sono stimati non certi, richiede competenze multidisciplinari (strutture, impianti, energia).",
 costi_e_economia="Ordini di grandezza indicativi: audit residenziale 300-800 €; due diligence edificio commerciale 1.500-8.000 €; audit industriale completo 3.000-20.000 €.",
 casi_real_world="Due diligence tecniche negli acquisti di portafogli immobiliari; audit energetici obbligatori per grandi imprese e energivore.",
 normative="Art. 8 D.Lgs 102/2014 (audit energetici obbligatori per grandi imprese ed energivore ogni 4 anni); linee guida per le ispezioni degli edifici; norme UNI per la valutazione delle prestazioni degli edifici.",
 note_cantiere="L'audit si chiude sempre con una tabella interventi-priorità-costi: un audit senza piano di azione è una fotografia che nessuno userà."),

dict(categoria="Contenzioso", nome="La perizia nel contenzioso edilizio: strategia, tempi e rischi",
 descrizione="Come si costruisce e si affronta un contenzioso tecnico-edilizio con la testa.",
 tecnologia="Valutazione preliminare della posizione (documentazione, fotografie, contratti, varianti, verbali); definizione della strategia: tentativo bonario (diffida, incontro tecnico, perizia asseverata), mediazione, arbitrato o giudizio; scelta del consulente (CTP) con competenza specifica e indipendenza; raccolta della documentazione di cantiere (libro firme, SAL, relazioni, foto, meteo); gestione delle perizie di parte e di contro; valutazione dei rischi tecnici, economici e di tempo; perizia asseverata come tentativo di definizione bonaria con efficacia probatoria rafforzata.",
 applicazioni="Contenziosi su appalti, difetti di costruzione, ritardi, prezzi di variante, responsabilità professionali, sinistri.",
 vantaggi="Strategia chiara prima di entrare in causa, selezione dello strumento giusto (bonario vs giudizio), riduzione dei rischi di soccombenza, valorizzazione della documentazione di cantiere.",
 limiti="I costi di consulenza e CTU si sommano ai tempi lunghi del giudizio, la perizia asseverata ha efficacia solo se accettata dalle parti, la vittoria tecnica non sempre giustifica il costo economico.",
 costi_e_economia="Ordini di grandezza indicativi: perizia asseverata 500-2.500 €; mediazione 1.000-5.000 €; contenzioso completo 10.000-100.000 € secondo valore; CTU 1.000-10.000 €.",
 casi_real_world="Mediazioni edilizie con esito positivo su vizi di costruzione; arbitrati camerali per le controversie d'appalto con periti nominati dalle parti.",
 normative="Artt. 61 ss. c.p.c. (CTU); D.Lgs 28/2010 (mediazione obbligatoria per talune materie, non generalmente per l'edilizia salvo scelta delle parti); regolamenti di arbitrato camerale; perizia asseverata secondo le regole tecniche deontologiche.",
 note_cantiere="La miglior perizia del mondo non sostituisce il verbale firmato in cantiere: chi documenta durante l'esecuzione vince il contenzioso prima di aprirlo."),
]

write_pack("PERIZIE_STIME_ASSICURAZIONI_PACK",
 "Perizie, stime e assicurazioni", "FACOLTA_GEOMETRI_PERITI", "L2-L3",
 "Stime immobiliari, estimo di cantiere, CTU/CTP, responsabilità e decadenze, assicurazioni CAR e postuma, danno edilizio, collaudi, catasto, sinistri, audit, contenzioso.",
 """# PERIZIE_STIME_ASSICURAZIONI_PACK

**Perizie, stime e assicurazioni nel mondo delle costruzioni**

Metodi di stima immobiliare, estimo di cantiere, CTU e CTP, responsabilità della costruzione e decadenze (artt. 1667-1669 c.c.), assicurazioni CAR e decennale, diagnosi dei danni, collaudi e conformità, perizie catastali, liquidazione dei sinistri, audit di edificio, strategia del contenzioso.

Schede: 10 (formato JSONL, un oggetto per riga).
""", perizie)

print("OK giro L")
