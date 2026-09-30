# -*- coding: utf-8 -*-
"""Edilizia: BIM e digitale + urbanistica e progetto del territorio."""
import json, os

S = []

# ============ BIM E DIGITALE (7) ============
S.append(("bim_digital","metodologia_bim",
"METODOLOGIA BIM - DAL DISEGNO AL MODELLO",
"""Il BIM (Building Information Modeling) non e' un software ma una metodologia di lavoro collaborativa:

1. DEFINIZIONE: un processo digitale di gestione dell'intero ciclo di vita dell'opera (progettazione, costruzione, gestione) basato su un modello informativo condiviso (ISO 19650).

2. AMBIENTE COMUNE DATI (CDE - Common Data Environment): un sistema di gestione delle informazioni in cui fluiscono dati, documenti e modelli tra i soggetti del progetto, con stati di avanzamento (work in progress, shared, published, archived).

3. LOD (Level of Development/Definition): livello di dettaglio del modello: LOD 100 (concept), LOD 200 (approximate geometry), LOD 300 (accurate), LOD 350 (connections), LOD 400 (fabrication), LOD 500 (as-built).

4. BIM USES: uso del modello per specifici scopi (3D coordination, quantity takeoff, 4D scheduling, 5D cost estimation, energy analysis, facility management).

5. VANTAGGI: riduzione errori e interference (clash detection), controllo costi e tempi, documentazione integrata, gestione del patrimonio.

6. NORMATIVA ITALIANA: D.M. 560/2017 (metodologia BIM per i lavori pubblici, obbligatoria per appalti sopra 1 milione di euro dal 2019), decreto rilancio (obbligo BIM per appalti sopra soglia), UNI 11337 (norme tecniche BIM)."""))
S.append(("bim_digital","ifc_openbim",
"IFC E OPEN BIM - L'INTEROPERABILITA' DEI MODELLI",
"""L'interoperabilita' e' la chiave del BIM collaborativo:

1. IFC (Industry Foundation Classes): formato standard aperto (ISO 16739) per lo scambio di modelli tra software diversi (Revit, Archicad, Allplan, Tekla, Solibri). Contiene geometria, proprietà, relazioni, tipologie di oggetti.

2. OPEN BIM: filosofia di collaborazione basata su formati aperti (IFC, BCF - BIM Collaboration Format per la comunicazione di problemi, IDS - Information Delivery Specification per i requisiti).

3. VIEWER E CONTROLLO: Solibri, BIMcollab, Navisworks per clash detection, revisione e verifica della qualità del modello.

4. IDS: specifica le informazioni richieste per ogni oggetto (es. il muro deve avere U-value, spessore, classe fuoco) per la verifica automatica.

5. BCF: scambio di issue tra piattaforme (commenti, screenshot, posizione 3D) senza condividere il modello intero.

6. ASSET INFORMATION MODEL (AIM): il modello per la gestione (facility management) con dati di manutenzione."""))
S.append(("bim_digital","scan_bim",
"SCAN-TO-BIM, GIS E DIGITAL TWIN",
"""Le tecnologie di acquisizione e digitalizzazione estendono il BIM al contesto:

1. SCAN-TO-BIM: acquisizione dello stato di fatto con laser scanner 3D (nuvole di punti) o fotogrammetria da drone, e conversione in modello BIM; usato per rilievi di esistenti, verifica avanzamento lavori, deformazione strutture.

2. GIS (Geographic Information System): gestione dei dati territoriali (georeferenziazione, mappe, reti, vincoli); l'integrazione BIM-GIS collega l'edificio al contesto (CityGML, IFC per infrastrutture).

3. DIGITAL TWIN: gemello digitale dell'edificio o citta' che si aggiorna in tempo reale con sensori (IoT), per gestione energetica, manutenzione predittiva, simulazione scenari.

4. DRONE E PHOTOGRAMMETRIA: rilievi aerei per topografia, monitoraggio cantieri, ispezioni di facciate e coperture.

5. REALTA' VIRTUALE ED AUMENTATA: visualizzazione immersiva del progetto per clienti e verifiche progettuali, AR in cantiere per sovrapporre il modello allo stato di fatto.

6. AI E MACHINE LEARNING: riconoscimento oggetti nelle nuvole di punti, generazione automatica di modelli, analisi di immagini per sicurezza e qualita'."""))
S.append(("bim_digital","computo_bim",
"COMPUTO BIM, 4D E 5D",
"""Il modello BIM alimenta computi, tempi e costi:

1. COMPUTO BIM (quantity takeoff): estrazione automatica delle quantità dagli oggetti del modello (muri, solai, infissi) con LOD adeguato; riduzione errori rispetto al computo manuale.

2. 4D (SIMULAZIONE TEMPORALE): collegamento del modello 3D con il cronoprogramma (MS Project, Primavera); simulazione della sequenza costruttiva, ottimizzazione dei tempi.

3. 5D (COSTO): collegamento con il computo e i prezzi unitari; stima dei costi in tempo reale, analisi del costo variando il progetto.

4. N-D: 6D (sostenibilità), 7D (facility management), con informazioni aggiuntive per la gestione.

5. LIMITI: il computo BIM richiede LOD 300+ e oggetti classificati correttamente; il costo del modello deve essere commisurato al beneficio.

6. STRUMENTI: plug-in di quantità takeoff (Vico, Innovaya), piattaforme cloud (Autodesk Construction Cloud, BIM 360, Trimble Connect)."""))
S.append(("bim_digital","bim_cantiere",
"BIM IN CANTIERE: DAL PROGETTO ALLA COSTRUZIONE",
"""Il BIM in cantiere migliora la qualità e riduce gli sprechi:

1. MODELLO ESECUTIVO: il progetto esecutivo BIM con LOD 400 fornisce la geometria di produzione per le macchine (taglio, piegatura), le tavole esecutive e le quantità per gli ordini.

2. COORDINAMENTO: clash detection tra strutture, impianti e architetture prima della costruzione, riducendo i rilievi in cantiere.

3. LAY-OUT E POSA: tavole di posa (shop drawings) generate dal modello, punti di riferimento 3D (total station integrata), verifica con AR.

4. MONITORAGGIO: confronto del modello con lo stato di fatto (scan-to-BIM), rilevamento scostamenti, documentazione fotografica georeferenziata.

5. CONSEGNA: modello as-built (LOD 500) con tutte le modifiche di cantiere, integrazione dei certificati di collaudo, manutenzione integrata (BIM per il facility management).

6. FORMAZIONE: il personale di cantiere usa tablet e viewer 3D per accedere al modello, riducendo la dipendenza dalle tavole cartacee."""))
S.append(("bim_digital","contratti_bim",
"CONTRATTI, RESPONSABILITA' E EPC CON IL BIM",
"""Il BIM cambia i rapporti contrattuali e le responsabilità:

1. INFORMATION REQUIREMENT: il committente definisce i requisiti informativi (EIR - Exchange Information Requirements) nel capitolato; il progettista risponde con il BIM Execution Plan (BEP).

2. RESPONSABILITA': il progettista risponde della correttezza del modello come dell'elaborato grafico; la responsabilità si ripartisce tra disciplinisti secondo il contributo; la consegna del modello come documento contrattuale (art. 2229 c.c.).

3. EPC (Engineering, Procurement, Construction): il contratto chiavi in mano in cui il general contractor progetta, approvvigiona e costruisce, con responsabilità unica verso il committente; il BIM e' lo strumento di coordinamento.

4. ALLIANCING E IPD (Integrated Project Delivery): contratti di collaborazione premiante con rischio/beneficio condiviso, incentivando la cooperazione invece della contesa.

5. NORME: ISO 19650-1:2 (gestione informativa), contrattualizzazione del CDE, ruolo del BIM manager.

6. CRITICITA': i modelli non sostituiscono il progetto normativo; la validità legale dei documenti digitali (CAD, BIM) richiede firme digitali e conservazione a norma."""))
S.append(("bim_digital","facility_management",
"BIM E FACILITY MANAGEMENT: L'EDIFICIO GESTITO",
"""Il BIM dopo la consegna: la gestione dell'edificio con il modello informativo:

1. AIM (Asset Information Model): il modello as-built arricchito con dati di gestione (schede tecniche, manutenzioni, garanzie, manuali, certificati) in formato COBie (Construction Operations Building information exchange).

2. CAFM (Computer Aided Facility Management): sistemi di gestione immobiliare (Archibus, Planon, IBM TRIRIGA) che integrano il BIM con gestione manutenzioni, spazi, utenze, sicurezza.

3. MANUTENZIONE PREDITTIVA: sensori IoT (vibrazioni, temperatura, consumi) integrati nel modello per interventi prima del guasto; riduzione del downtime e dei costi.

4. ENERGIA E SOSTENIBILITA': monitoraggio continuo dei consumi (energy management), certificazione energetica mantenuta, ottimizzazione impianti.

5. RENOVATION E END OF LIFE: il modello BIM supporta le ristrutturazioni (scan-to-BIM aggiornato) e la demolizione con riciclo dei materiali (material passport).

6. VALORE: l'edificio con modello BIM e documentazione completa ha valore di mercato superiore (due diligence facilitata)."""))

# ============ URBANISTICA (7) ============
S.append(("urbanistica","piani_territoriali",
"I PIANI TERRITORIALI: PRG, PSC E GOVERNO DEL TERRITORIO",
"""La pianificazione urbanistica italiana e' organizzata su più livelli:

1. PIANO PAESAGGISTICO (art. 135 D.Lgs 42/2004): governa la trasformazione del territorio in ottica paesaggistica; vincola i piani comunali.

2. PTCP (Piano Territoriale di Coordinamento Provinciale / PTC per le città metropolitane): programma le grandi infrastrutture e le aree strategiche.

3. PSC (Piano Strutturale Comunale): sostituisce il PRG nelle regioni che hanno adottato la pianificazione strutturale (Toscana, Emilia-Romagna, ecc.); definisce il progetto strutturale del territorio (ambiti, reti, servizi).

4. PRG (Piano Regolatore Generale): nelle regioni con pianificazione tradizionale, e' composto da Piano dei Servizi, Piano delle Regole (con norme attuative), e previsioni (zone omogenee).

5. PIANI ATTUATIVI: strumenti di attuazione (PI/PIP programmi integrati, Lottizzazioni convenzionate, Piani di Zona, convenzioni urbanistiche) che trasformano le previsioni in progetti esecutivi.

6. VINCOLI: vincoli paesaggistici, idrogeologici, archeologici, sismici che limitano la trasformabilita' delle aree."""))
S.append(("urbanistica","progetto_paese",
"PROGETTARE UN QUARTIERE O UN PAESE: FASI E CONTENUTI",
"""La progettazione urbana ex novo (quartiere, paese, espansione) e' il compito piu' complesso dell'urbanistica:

1. FASE DI INDAGINE: analisi del contesto (territorio, paesaggio, vincoli, mercato), censimento delle esigenze (residenti, servizi, infrastrutture), valutazione della fattibilità economica.

2. PROGRAMMA: definizione del programma funzionale (residenze, servizi, industria, verde) e quantitativo (abitazioni per piano, densità edilizia, standard urbanistici).

3. PROGETTO STRUTTURALE: disegno delle reti (strade, reti tecnologiche, verde), definizione degli isolati e delle lottizzazioni, localizzazione dei servizi (scuole, sanità, commercio).

4. PROGETTO URBANO: disegno degli spazi pubblici (piazze, parchi, strade), standard qualitativi (materiali, arredo, illuminazione), regolamento urbanistico ed edilizio.

5. ATTUAZIONE: convenzioni urbanistiche con i costruttori, finanziamento delle opere di urbanizzazione, fasi di realizzazione (lotti), gestione del cantiere urbano.

6. PARTECIPAZIONE: coinvolgimento dei cittadini (bilancio partecipativo, consultazioni pubbliche) per la costruzione del consenso."""))
S.append(("urbanistica","reti_urbane",
"LE RETI TECNOLOGICHE URBANE: ACQUA, FOGNATURE, ENERGIA",
"""Le reti sotterranee sono il sistema circolatorio della città:

1. RETE IDRICA: adduttrici (dalle fonti), distribuzione (condotte primarie, secondarie), serbatoi di accumulo e rilancio, utenze (idrometri), reti antincendio (idranti); dimensionamento con portate massime orarie e coefficienti di contemporaneità.

2. FOGNATURE: reti separate (acque nere, acque bianche) o miste; pozzetti di ispezione, caditoie, collettori, impianti di sollevamento (risalenti), depuratori (consorzi di depurazione); il principio 'chi inquina paga' (D.Lgs 152/2006).

3. ENERGIA: reti gas (metano), elettriche (cabine di trasformazione MT/BT), teleriscaldamento (reti di calore), gasdotti, metanodotti.

4. TELECOMUNICAZIONI: fibra ottica (FTTH - Fiber To The Home), cabinet stradali, reti 5G, smart city sensors.

5. TECNOLOGIE: trenchless technology (posa senza scavo: microtunneling, fotriatrici), tubi in PE, PVC, ghisa sferoidale, monitoraggio smart (sensori di flusso, pressione, perdite)."""))
S.append(("urbanistica","standard_edilizi",
"GLI STANDARD URBANISTICI E LE DOTAZIONI DI SERVIZI",
"""Gli standard definiscono quanto spazio pubblico e servizi servono alla comunità:

1. STANDARD URBANISTICI: parametri minimi di dotazione (mq di verde per abitante, mq di scuola per 1.000 abitanti, posti letto ospedalieri, mq di mercato) secondo la legge regionale; le opere di urbanizzazione primaria (strade, reti) e secondaria (scuole, parchi) sono a carico del costruttore.

2. INDICI DI EDILIZIA': indice di fabbricabilità (mc/mq o mq/mq), indice di copertura, altezza massima, distanze (corte, laterale, frontale), rapporto di copertura (fattore di forma); questi indici determinano la capacità edilizia dei lotti.

3. ZONE OMOGENEE: A (agricola, vincolata), B (edilizia residenziale completata), C (edilizia residenziale da completare), D (edilizia completa da ristrutturare), E (edilizia artigianale/industriale), F (edilizia commerciale, direzionale).

4. COMPENSI E ONERI: oneri di urbanizzazione ( contributo al posto delle opere), monetizzazione degli standard, compensazioni paesaggistiche (D.Lgs 42/2004).

5. REGOLAMENTO EDILIZIO: norme di attuazione comunali (altezze, materiali, colori, coperture, parcheggi) che ogni progetto deve rispettare."""))
S.append(("urbanistica","mobilita",
"MOBILITA' URBANA E PROGETTO DELLA STRADA",
"""La mobilità è un criterio di qualità urbana:

1. GERARCHIA DELLE VIE: arterie principali, secondarie, locali, vicoli; a ciascuna corrispondono velocità, sezioni, funzioni diverse.

2. MOBILITA' DOLCE: piste ciclabili (rete ciclabile minima), percorsi pedonali (marciapiedi, zone pedonali, attraversamenti), zone 30 (limitazione velocità), isole ambientali.

3. TRASPORTO PUBBLICO: rete bus, tram, metro, funicolari; interscambi (park & ride, kiss & ride), corsie preferenziali.

4. PARCHEGGI: standard minimi (posti auto per abitazione, per mq di commercio), parcheggi di interscambio, parcheggi in struttura, parcheggi scambiatori.

5. PROGETTO DELLA STRADA: sezione stradale (corsie, parcheggi laterali, verde), attraversamenti pedonali (sovra o sottopassi, attraversamenti rialzati), arredo urbano (illuminazione, panchine, cestini, segnaletica), verde stradale.

6. SMART MOBILITY: car sharing, bike sharing, monopattini elettrici, Mobility as a Service (MaaS), sensori traffico."""))
S.append(("urbanistica","paesaggio_ambiente",
"PAESAGGIO, AMBIENTE E SOSTENIBILITA' TERRITORIALE",
"""La sostenibilità ambientale è un vincolo e un'opportunità per la progettazione urbana:

1. TUTELA DEL PAESAGGIO: D.Lgs 42/2004 tutela il paesaggio come bene culturale; il piano paesaggistico vincola l'edilizia (materiali, colori, volumi, coperture); le opere di pregio richiedono il nullaosta della Soprintendenza.

2. IDROGEOLOGIA: vincoli di pericolosità idraulica (fiumi, torrenti, coste), frane (Piano di Assetto Idrogeologico, PAI), sismico (microzonazione sismica); edilizia consentita con prescrizioni o vietata.

3. INQUINAMENTO E RUMORE: zonizzazione acustica (classi di destinazione acustica, limiti di emissione), piano regionale di risanamento aria, gestione rifiuti (raccolta differenziata, isole ecologiche, impianti).

4. ENERGIA TERRITORIALE: piani energetici comunali, teleriscaldamento da fonti rinnovabili, fotovoltaico urbano, geotermia a bassa entalpia, quartieri a energia quasi zero.

5. ECONOMIA CIRCOLARE: riciclo dei materiali da demolizione (inerti), edilizia a basso impatto, riuso degli edifici esistenti (rigenerazione urbana), bonifica delle aree contaminate (brownfield).

6. CLIMATE CHANGE: adattamento (città resilienti a ondate di calore, piogge intense), mitigazione (riduzione consumo suolo, aumento verde urbano, materiali riflettenti)."""))
S.append(("urbanistica","ammodernamento",
"RIGENERAZIONE URBANA E RIOCCUPAZIONE DEL TERRITORIO",
"""La città contemporanea si riqualifica più che espandersi:

1. RIGENERAZIONE URBANA: recupero di quartieri degradati con interventi integrati (edilizia, servizi, verde, sicurezza); strumenti: PRU (Programmi di Riqualificazione Urbana), Contratti di Quartiere, Bandi periferie.

2. RIOCCUPAZIONE DELLE AREE DISMESSE: ex industriali (brownfield), ex ferroviarie, ex militari, cave e discariche; bonifica e nuova destinazione (residenza, parco, tecnologia).

3. RECUPERO EDILIZIO: ristrutturazione di edifici storici, sostituzione edilizia (demolizione e ricostruzione con aumento di densità), recupero dei sottotetti e dei seminterrati.

4. CONTRASTO AL CONSUMO DI SUOLO: obiettivo nazionale di riduzione del consumo di suolo a 0 netto entro 2050 (PNRR e legge), riuso prioritario rispetto a nuova espansione.

5. ESEMPLI: ex Area Falck Sesto San Giovanni, ex Officine Grandi Riparazioni Torino, Parco Dora Torino, ex Zona Industriale Brescia.

6. STRUMENTI: convenzioni di riuso, diritto di superficie, partenariato pubblico-privato, bandi PNRR per la rigenerazione."""))

# ============ writer ============
os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "bim_urbanistica_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus BIM e urbanistica a cura di Kimi",
    "url": "",
}
out = []
for i, (cat, tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"BIM-{i:03d}", "categoria": cat, "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = os.path.join('Edilizia_Pack', 'parsed', 'bim_urbanistica.jsonl')
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede BIM/urbanistica -> {os.path.abspath(path)}")
