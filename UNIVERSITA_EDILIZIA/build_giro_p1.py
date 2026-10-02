# -*- coding: utf-8 -*-
"""Giro P: crea ILLUMINAZIONE_TECNICA_PACK (12 schede)."""
import json, os

KEYS = ['categoria','nome','descrizione','tecnologia','applicazioni','vantaggi','limiti','costi_e_economia','casi_real_world','normative','note_cantiere']
P = 'UNIVERSITA_EDILIZIA/ILLUMINAZIONE_TECNICA_PACK'
os.makedirs(P + '/schede', exist_ok=True)

S = [
("Fondamenti","Le grandezze fotometriche: lumen, lux, candela, nit",
 "Il lessico minimo per ragionare sulla luce: flusso luminoso (lumen, lm), intensita' (candela, cd), illuminamento (lux, lx = lm/m²), luminanza (nit, cd/m²) e grandezze cromatiche (temperatura di colore in kelvin, indice di resa cromatica IRC/Ra). Senza queste unita' ogni discorso su impianti di illuminazione resta aneddotico.",
 "Flusso: quantita' totale di luce emessa dalla sorgente. Illuminamento E = flusso su superficie / area; su piano di lavoro si misura con luxmetro a griglia di punti. Luminanza: luce che una superficie invia all'occhio, la grandezza del riverbero e dell'abbagliamento. CCT (temperatura di colore correlata): sotto 3.000 K luce calda, oltre 5.000 K fredda. IRC 100 = resa cromatica perfetta; sotto 80 i colori si deformano.",
 "Preventivi, verifiche di accettazione, dialogo con progettisti e fornitori, scelta lampade in ristrutturazione.",
 "Permette di leggere schede prodotto e relazioni di calcolo; distingue sorgenti equivalenti in lumen ma diverse in resa cromatica; evita l'errore classico di confrontare watt invece di lumen.",
 "Non dice nulla da sola sulla distribuzione spaziale: due apparecchi con stesso flusso danno lux diversi su piano a seconda dell'ottica; la lettura lux a un punto non rappresenta la media della stanza.",
 "Ordini di grandezza indicativi: luxmetro digitale da cantiere 40-150 €; luxmetro professionale con sonda classe B 300-900 €; ricarica misura impianto completo uffici da alcune centinaia di euro secondo metratura.",
 "Supermercati: verifica lux su banco carne e ortofrutta con luxmetro a griglia, con sorgenti ad alta resa cromatica per non deformare il colore dei prodotti freschi.",
 "UNI EN 12464-1 (illuminazione luoghi di lavoro, grandezza di riferimento); UNI EN 13032 (misura e dichiarazione delle prestazioni fotometriche); D.Lgs 81/2008 (illuminamento adeguato dei luoghi di lavoro, richiama valori di riferimento).",
 "Misurare sempre a piano di lavoro con sonda orizzontale; segnare su pianta i punti di misura prima di accettare i valori dichiarati dal fornitore."),
("Fondamenti","La norma UNI EN 12464-1: livelli di illuminamento per ambiente",
 "La norma europea (adottata in Italia come UNI EN 12464-1) fissa i valori minimi medi di illuminamento misurati sul piano di riferimento di ciascun ambiente di lavoro: uffici con attivita' di scrittura e lettura, scuole, laboratori, industria leggera e pesante, aree di transito.",
 "Ogni ambiente ha piano di riferimento (0,75 m per attivita' seduta, pavimento per transiti), valore medio mantenuto Em, uniformita', valore di abbagliamento UGR limite, resa cromatica minima. Il progettista dichiara i valori calcolati; la manutenzione deve garantire il valore mantenuto tenendo conto del deprezzamento.",
 "Progettazione e collaudo di uffici, aule, laboratori, reparti produttivi; verifica di conformita' in caso di contestazione su lavoro al videoterminale.",
 "Riduce liti su luce insufficiente: il riferimento e' un valore di norma, non un'opinione; facilita la scrittura di capitolati con requisiti oggettivi.",
 "I valori sono minimi per attivita': ambienti con compiti visivi critici (controllo qualita', laboratori di colore) richiedono livelli superiori e va valutato il progetto specifico.",
 "Ordini di grandezza indicativi: relazione fotometrica di un impianto uffici da 150-600 € secondo complessita'; integrazione illuminotecnica in pratica edilizia da qualche centinaio a poche migliaia di euro.",
 "Ufficio open space: piano di calcolo a 0,75 m, Em 500 lx e controllo UGR come valori di riferimento per attivita' di scrittura, lettura e dati su schermo.",
 "UNI EN 12464-1 (luoghi di lavoro interni); D.Lgs 81/2008 (richiamo ai valori di riferimento per i luoghi di lavoro).",
 "I valori vanno intesi come mantenuti: se il progetto dichiara 500 lx iniziali, dopo il deprezzamento della sorgente si scende; capitolare il fattore di manutenzione."),
("Sorgenti","Le sorgenti LED: chip, driver, binning e schemi ottici",
 "Il LED ha sostituito incandescenza, fluorescenza e scarica: lunga vita, elevata efficienza, controllo istantaneo e dimmerabilita'. Ma la qualita' di un apparecchio LED dipende da chip, alimentatore (driver), selezione cromatica (binning) e ottica.",
 "Sorgente = chip LED su scheda + ottica (lente, riflettore) + driver che converte e stabilizza la corrente. Efficienza espressa in lumen/watt (70-150 lm/W su apparecchi da interno). Binning: i chip vengono selezionati per flusso, colore e tensione; apparecchi economici mescolano bin diversi con tinte visibili tra apparecchio e apparecchio. IRC 80 standard, 90 per retail e sanita'.",
 "Nuovi impianti, relamping, specifiche in capitolato, verifica della qualita' percepita in retail e hospitality.",
 "Risparmio energetico del 40-70% rispetto a vecchie sorgenti; manutenzione ridotta; possibilita' di dimming, sensori e gestione scenari.",
 "Driver di scarsa qualita' = flicker invisibile ma dannoso per la stanchezza visiva; degradazione (L80/B10) non sempre dichiarata; riparabilita' spesso limitata perche' l'apparecchio e' monoblocco.",
 "Ordini di grandezza indicativi: faretto LED da interno 15-60 €; pannello 60x60 40-120 €; apparecchio architettonico 150-800 €; driver dimmerabile 25-90 €.",
 "Catena retail: relamping completo con LED ad alta resa cromatica e CCT coordinata tra reparti, dimezzamento consumi e rientro indicativo sotto i 3 anni con uso intenso.",
 "Regolamento (UE) 2019/2020 (requisiti ecodesign delle sorgenti luminose e degli apparecchi); marcatura CE secondo direttiva 2014/35/UE.",
 "Chiedere sempre la scheda fotometrica completa (file IES/LDT) del produttore: senza file l'apparecchio non e' verificabile in software di calcolo; diffidare di apparecchi senza marca del driver."),
("Impianto","L'impianto elettrico della luce: quadri, linee e sicurezza",
 "L'illuminazione e' un carico elettrico: il circuito va progettato come impianto, con quadro, protezioni, sezioni di cavo adeguate e canalizzazioni secondo le regole degli impianti elettrici.",
 "Linee dedicate per gruppi di apparecchi, magnetotermici e differenziali, canaline dimensionate per il riempimento ammissibile, cablaggi basse tensione per i controlli (0-10 V, DALI), alimentazioni di emergenza su linea separata. Negli ambienti umidi o esterni: grado IP e isolamento rinforzato; nei bagni: volumi di protezione secondo norma.",
 "Nuovi impianti, ristrutturazioni, adeguamento quadri, cablaggio sensori e attuatori domotici.",
 "Affidabilita' e sicurezza dell'impianto; manutenzione semplificata con linee identificate; espandibilita' per sensori e scenari futuri.",
 "Sovraccarico di quadri aggiungendo LED su linee vecchie pensate per carichi diversi; cavi sottodimensionati su lunghe tratte con cadute di tensione; canaline troppo piene che scaldano.",
 "Ordini di grandezza indicativi: quadretto con 8 moduli 60-150 €; differenziale 30-90 €; canalina installata 8-20 €/metro; cablaggio punto luce 25-70 €.",
 "Ristrutturazione uffici: rifacimento canaline, nuovi quadri per reparti e linee DALI per il controllo scenari, collaudo con misura di continuita' di terra.",
 "CEI 64-8 (impianti elettrici utilizzatori a tensione non superiore a 1000 V); direttiva 2014/35/UE (bassa tensione); DPR 462/2001 (utilizzazione energetica elettrica).",
 "Non superare il 70% della portata del magnetotermico in regime continuativo: gli LED in produzione restano accesi molte ore."),
("Esterno","Illuminazione esterna: stradale, aree verdi e tutto il cielo",
 "L'illuminazione esterna serve viabilita', sicurezza e fruizione notturna degli spazi, ma va contenuta: l'obiettivo e' la luce giusta dove serve, con controllo dell'emissione verso l'alto.",
 "Per strade e corsie i requisiti di progetto sono definiti dalle norme sull'illuminazione stradale (serie UNI EN 13201) con classi di illuminamento secondo tipologia di via, flusso, uniformita' e abbagliamento. Per parchi e aree: apparecchi con ottica che taglia il flusso verso l'alto, sensori di presenza e abbassamenti notturni per risparmio.",
 "Strade comunali, parchi, parcheggi, percorsi pedonali, aree industriali esterne, impianti sportivi esterni.",
 "Sicurezza percepita e reale in spazi notturni; consumi ridotti con LED e gestione oraria; valorizzazione paesaggistica di giardini e facciate.",
 "Illuminazione mal progettata genera abbagliamento per automobilisti e finestre esposte; l'inquinamento luminoso e' oggetto di attenzione normativa locale e regionale.",
 "Ordini di grandezza indicativi: apparecchio stradale LED 150-600 €; palo 300-1.200 €; punto luce da giardino 40-250 € installato secondo lavori civili.",
 "Comune: riqualificazione dell'illuminazione pubblica con apparecchi a fascio controllato, abbassamento di potenza dopo mezzanotte e risparmio percepito in bolletta.",
 "Serie UNI EN 13201 (illuminazione stradale); leggi regionali e regolamenti comunali contro l'inquinamento luminoso (variano per territorio, da verificare caso per caso).",
 "Orientare il fascio lontano dalle finestre e dal cielo; sulle facciate storiche usare luce calda e fasci stretti per non schiarire le superfici intonacate oltre misura."),
("Sicurezza","L'illuminazione di emergenza: norma UNI EN 1838 e adempimenti",
 "In caso di black-out l'illuminazione di emergenza deve garantire l'evacuazione: percorsi, uscite, zone ad alto rischio. E' un impianto obbligatorio con requisiti di funzionalita' e verifiche periodiche.",
 "Sistemi: plafoniere autonome con batteria (autonomia tipica 1-3 ore), centraline con batterie centrali, lampade per grandi spazi. Requisiti UNI EN 1838: illuminamento minimo sul percorso d'evacuazione, rapporto corretto tra zone chiare e scure per evitare abbagliamento improvviso, segnaletica verde per le uscite. Prove periodiche secondo norma antincendio e assicurazioni.",
 "Uffici, scuole, attivita' commerciali, industria, luoghi di intrattenimento, ogni edificio aperto al pubblico.",
 "Evacuazione sicura in black-out; adempimento verso vigili del fuoco e assicurazioni; riduzione della responsabilita' del gestore.",
 "Pile esauste non rilevate: le prove periodiche esistono proprio perche' le batterie degradano; apparecchi ostruiti nel tempo da scaffali o cartelloni.",
 "Ordini di grandezza indicativi: lampada di emergenza 15-60 €; centralina con batterie da 400-3.000 € secondo potenza; contratto di manutenzione programmata da qualche centinaio di euro/anno per sede media.",
 "Scuola: collaudo dell'impianto di emergenza con prova funzionale di scarica e registrazione nel libretto, come richiesto dalle verifiche.",
 "UNI EN 1838 (sistemi di illuminazione di emergenza); normativa antincendio nazionale per la destinazione d'uso (es. attivita' soggette) e CEI 64-8 per l'impianto.",
 "Registrare ogni prova nel libretto impianti: in caso di sinistro l'assicurazione chiede i verbali di funzionamento."),
("Efficienza","Efficienza energetica e gestione intelligente della luce",
 "La luce e' spesso la prima voce in bolletta di uffici e retail: sensori di presenza, daylight harvesting e regolazione oraria tagliano consumi senza togliere qualita' visiva.",
 "Strategie: sensori di presenza che abbassano o spengono a stanza vuota; regolazione in funzione della luce naturale (daylight harvesting, soprattutto in open space vicino a vetrate); scenari orari per pulizie, manutenzione e vigilanza; sistemi centralizzati (DALI, KNX) con monitoraggio dei guasti. KPI: kWh/m² anno per l'illuminazione.",
 "Open space, retail, scuole, industria, condomini con parti comuni, illuminazione pubblica gestita da remoto.",
 "Riduzioni del 30-60% sui consumi di illuminazione con interventi di sola gestione; diagnosi dei guasti senza sopralluogo; vita utile piu' lunga delle sorgenti con dimming.",
 "Sensori mal posizionati (vicino a finestre leggono il giorno e tengono le luci spente anche d'inverno, o il contrario); sistemi troppo complessi per gli utenti che poi vengono bypassati.",
 "Ordini di grandezza indicativi: sensore di presenza 20-80 €; attuatore/dimmer 40-150 €; centralina KNX per sede 500-3.000 €; retrofit della gestione di un open space da 2.000-10.000 € secondo postazioni.",
 "Ufficio direzionale: sensori di presenza negli open space, abbassamento automatico nelle ore serali e report mensile dei consumi.",
 "Regolamento (UE) 2019/2020 (ecodesign); direttiva 2012/27/UE (efficienza energetica) richiamata dalla normativa nazionale; indicazioni ENEA sull'efficientamento dell'illuminazione.",
 "Partire da un audit con luxmetro e conteggio delle ore di accensione: senza misura non si puo' quantificare il risparmio ne' verificarlo dopo l'intervento."),
("Progetto","Il calcolo illuminotecnico: metodo del flusso totale e software",
 "Il calcolo serve a garantire i livelli richiesti dalla norma prima di comprare un apparecchio: il metodo del flusso totale da' una stima rapida, i software fotometrici danno la simulazione vera.",
 "Metodo del flusso totale: E = (flusso lampade x coefficiente di utilizzazione x fattore di manutenzione) / area. Il coefficiente di utilizzazione dipende dall'indice locale (dimensioni stanza, altezza apparecchi) e dalle riflettenze. Software come DIALux e Relux importano i file IES/LDT dei produttori e calcolano lux punto per punto, luminanze e UGR; il risultato e' la relazione fotometrica di progetto.",
 "Preventivi di nuovi impianti, verifica di relazioni altrui, adeguamenti, progetti in BIM con scambio file.",
 "Si compra cio' che serve: numero e potenza degli apparecchi giusti dal primo colpo; preventivi confrontabili tra loro su base di calcolo omogenea.",
 "Il metodo del flusso ignora abbagliamento e uniformita' puntuali; i file IES di produttori sconosciuti possono dichiarare valori ottimistici: verificare marca e laboratorio.",
 "Ordini di grandezza indicativi: software DIALux/Relux gratuiti; relazione di calcolo da professionista 150-600 € per commessa semplice; corso base software 200-500 €.",
 "Aula scolastica: simulazione con apparecchi scelti dai file del produttore, verifica di Em e UGR sul piano dei banchi prima dell'ordine.",
 "UNI EN 12464-1 (valori da rispettare); UNI EN 13032 (dichiarazione fotometrica delle sorgenti).",
 "Salvare la relazione firmata con i file IES usati: e' la prova che l'impianto e' stato scelto con criterio e non a occhio."),
("Architettura della luce","Luce per uffici, scuole, sanita', industria e retail",
 "Ogni tipologia ha bisogni luminosi diversi: l'errore e' usare la stessa soluzione ovunque. La luce giusta migliora performance, sicurezza e vendite.",
 "Uffici e scuole: luce diffusa, controllo dell'abbagliamento per chi lavora a schermo, CCT 3500-4000 K. Sanita': resa cromatica alta per le visite e notturni caldi nei reparti. Industria: resa dei dettagli, protezione meccanica degli apparecchi, eventuale emergenza maggiorata lungo le linee pericolose. Retail: accenti sui prodotti, CCT coerente con il marchio, verticali luminosi che guidano lo sguardo. Hospitality e residenziale: fasce cromatiche calde e dimming scenografico.",
 "Progettazione per destinazione d'uso, direzionale lavoro, relamping mirati per tipologia di cliente.",
 "Migliora produttivita' e comfort percepito; aumenta le vendite in retail con l'esposizione corretta del colore; riduce errori e infortuni in industria.",
 "Il gusto cambia: CCT troppo fredda in un hotel sembra ospedale; accenti troppo forti creano disuniformita' percepita come trascuratezza.",
 "Ordini di grandezza indicativi: punto luce ufficio 60-200 €; apparecchio industriale stagno 80-250 €; faretto retail 80-400 €; progettazione luce retail da 1.000 € in su per punto vendita.",
 "Ristorante di design: binari con faretti caldi sui tavoli, luce di lavoro neutra in cucina, scenografia cromatica coerente con l'identita' del locale.",
 "UNI EN 12464-1 (requisiti per destinazione); prescrizioni igienico-sanitarie regionali per locali di pubblico esercizio e sanita'.",
 "Fare una prova sul campo con un campione illuminato prima dell'ordine completo: resa cromatica e CCT si giudicano solo a luce accesa."),
("Manutenzione","Manutenzione, deprezzamento e relamping",
 "Un impianto di illuminazione non si mantiene da solo: sorgenti degradano, ottiche si sporcano, batterie di emergenza invecchiano. La manutenzione programmata mantiene i valori di progetto.",
 "Deprezzamento LED dichiarato come L80/B10: tempo in cui l'80% dei campioni resta sopra l'80% del flusso iniziale (tipicamente 25.000-50.000 ore). Piano di manutenzione: pulizia ottiche annuale, verifica batterie secondo norma, relamping preventivo a fine vita (non a guasto). Gli apparecchi modulari riducono i costi di riparazione.",
 "Gestione facility di edifici in uso, condomini, catene retail, manutenzione industriale.",
 "Consumi stabili nel tempo, niente cali di produzione per luce insufficiente, emergenza sempre pronta, costi prevedibili.",
 "Il relamping al guasto costa di piu' (interventi singoli, banchi vuoti in retail durante la sostituzione); gli apparecchi monoblocco a guasto totale vanno sostituiti interi.",
 "Ordini di grandezza indicativi: pulizia straordinaria apparecchi 5-15 € a punto; contratto annuale di manutenzione per sede media da poche centinaia a poche migliaia di euro; relamping 10-40 € a punto luce.",
 "Retail: piano di relamping scaglionato per reparti con breve chiusura del banco e scorta dedicata di sorgenti.",
 "D.Lgs 81/2008 (manutenzione degli ambienti di lavoro); obblighi di verifica dell'illuminazione di emergenza secondo la norma antincendio applicabile.",
 "Tenere un registro di ore di accensione e date di sostituzione: la prossima sostituzione si pianifica sui dati, non a memoria."),
("Controlli","Verifica in opera: luxmetro, accettazione e documentazione",
 "La fase finale e' la verifica: misurare i lux reali a impianto completato e confrontarli con la relazione di calcolo, poi archiviare la documentazione.",
 "Verifica con luxmetro a griglia di punti sul piano di lavoro, calcolo della media e confronto con il valore di progetto mantenuto; controllo delle posizioni degli apparecchi rispetto agli schermi per l'abbagliamento. Documentazione da consegnare: schede tecniche, dichiarazione CE, file IES usati, relazione fotometrica, schema dei quadri e libretto delle verifiche di emergenza.",
 "Collaudo di nuovi impianti, accettazione di lavori di ristrutturazione, verifiche periodiche di edifici in gestione.",
 "Chiudere il cerchio progetto-reale: se i lux misurati non tornano si interviene prima del trasferimento; documentazione pronta per assicurazioni e controlli.",
 "Misurare subito dopo la pulizia di fine cantiere, quando le ottiche sono pulite, da' valori migliori della vita operativa; superfici specchiate falsano le letture puntuali.",
 "Ordini di grandezza indicativi: verifica completa con rilascio di relazione 300-1.000 € per sede; luxmetro in comodato con contratto di manutenzione spesso incluso.",
 "Consegna open space: rilievo lux a griglia su ogni postazione, media conforme, verbale firmato tra impresa e committente.",
 "UNI EN 13032 (metodi di misura); UNI EN 12464-1 (criteri di valutazione dei valori); prassi professionali di collaudo degli impianti elettrici.",
 "Misurare a parecchie ore di distanza dall'accensione: alcuni LED modificano leggermente il flusso a freddo; annotare temperatura e condizioni nel verbale."),
]

with open(P + '/schede/schede.jsonl', 'w', encoding='utf-8') as f:
    for row in S:
        d = dict(zip(KEYS, row))
        assert list(d.keys()) == KEYS
        f.write(json.dumps(d, ensure_ascii=False) + '\n')

course = '''corso: "Illuminazione tecnica e illuminotecnica"
facolta: "FACOLTA_IMPIANTI_ENERGIA"
livello: "L1-L2"
schede: 12
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "UNI EN 12464-1, UNI EN 1838, UNI EN 13032, serie UNI EN 13201, CEI 64-8, Regolamento (UE) 2019/2020, D.Lgs 81/2008, direttiva 2014/35/UE"
nota_metodologica: "Illuminotecnica operativa: grandezze fotometriche, norma sui livelli di illuminamento, LED, impianto, esterno, emergenza, efficienza, calcolo, manutenzione e verifica in opera. Norme citate solo dove consolidate; per le soglie specifiche degli ambienti si rimanda al testo vigente della UNI EN 12464-1."
'''
open(P + '/COURSE.yaml', 'w', encoding='utf-8').write(course)

readme = '''# Illuminazione tecnica e illuminotecnica — Pack

Dodici schede operative per progettare, installare, controllare e mantenere
l'impianto di illuminazione di un edificio: dalle grandezze fotometriche
(lumen, lux, candela, nit) alla norma UNI EN 12464-1, dai LED e dai driver
all'impianto elettrico secondo CEI 64-8, dall'illuminazione stradale
(serie UNI EN 13201) all'emergenza UNI EN 1838, dall'efficienza energetica
al calcolo con software e alla verifica finale con luxmetro.

Struttura dati: `schede/schede.jsonl`, una scheda JSON per riga, con le 11
chiavi standard della repository (categoria, nome, descrizione, tecnologia,
applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world,
normative, note_cantiere). I costi sono ordini di grandezza indicativi.

Fonte principale: norme europee adottate in Italia (UNI EN) e normativa
degli impianti (CEI 64-8), citate per esteso nelle schede.
'''
open(P + '/README.md', 'w', encoding='utf-8').write(readme)
print('ILLUMINAZIONE_TECNICA_PACK creata:', len(S), 'schede')
