# -*- coding: utf-8 -*-
"""Giro N: 3 corsi nuovi — Aeroporti e infrastrutture di volo, Porti e opere marittime,
Emergenze e ricostruzione post-sisma. Contenuti classici verificabili; nessuna norma inventata."""
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
# PACK 1 — AEROPORTI E INFRASTRUTTURE DI VOLO
# =====================================================================
aeroporti = [
dict(categoria="Piste", nome="Piste aeroportuali: geometria, pavimentazioni e portanza",
 descrizione="La piastra di volo: dimensionamento, pavimentazioni in cls e flessibili, il sistema ACN/PCN.",
 tecnologia="Geometrie delle piste (lunghezze 1.500-4.000 m, larghezza 45-60 m per traffico internazionale), code, piazzali e vie di rullaggio; pavimentazioni in cls lastricato (lastre 5x5 m con giunti) o flessibili (fondi stabilizzati + conglomerato bituminoso); classificazione della portanza con il sistema ACN/PCN (Aircraft Classification Number / Pavement Classification Number) che abbinano velivolo e pavimento; calcolo degli spessori sul traffico equivalente (metodo FAA e ricerca italiana); pavimentazioni dei piazzali con basi in cls rinforzato; giunti e sigillanti; drenaggi longitudinali e trasversali; rigature antiscivolo della superficie di contatto.",
 applicazioni="Aeroporti di ogni dimensione: aviazione generale, scali nazionali, hub internazionali, piste militari convertite.",
 vantaggi="Superfici con portanza certificata per ogni velivolo, durata con la manutenzione programmata dei giunti, drenaggio che riduce l'aquaplaning.",
 limiti="I giunti del lastricato sono il punto debole (FOD, infiltrazioni), il calcolo del traffico richiede dati di flotta certi, gli interventi in esercizio richiedono finestre notturne.",
 costi_e_economia="Ordini di grandezza indicativi: nuova pista 200-600 €/m² compresa di basi; rifacimento piazzale 80-200 €/m²; manutenzione ordinaria 2-5 €/m²/anno.",
 casi_real_world="Espansioni degli scali italiani con nuove piste e piazzali; rifacimenti notturni dei piazzali con conglomerati ad alta resistenza rapida.",
 normative="Reg. UE 139/2014 (requisiti di certificazione e gestione degli aerodromi) con i regolamenti EASA di attuazione; standard ICAO (Allegato 14) per le geometrie; specifiche ENAC nazionali.",
 note_cantiere="Il FOD (Foreign Object Debris) è il nemico: ogni lavorazione vicino alla piastra di volo termina con la bonifica meccanica della superficie prima della riapertura."),

dict(categoria="Segnaletica", nome="Segnaletica, balisaggio e sistemi di assistenza alla navigazione aerea",
 descrizione="Come gli aeroplani trovano la pista: ILS, luci di avvicinamento, balisaggi e torri.",
 tecnologia="Sistema ILS (Instrument Landing System) con componente locale e planata (radiofaro e glide path) che guida l'avvicinamento strumentale fino alla soglia; balisaggio luminoso: luci di soglia, di contorno pista, di rullaggio, di avvicinamento sequenziale (approach); segnalazione di ostacoli con luci rosse e bicolori; radioassistenze tradizionali (VOR/DME, NDB) e moderne (GBAS, sistemi satellitari); sistemi di calibrazione e monitoraggio con allarmi di disallineamento; torri di controllo (TWR) con ottica visiva e posizione di comando; sistemi di sorveglianza radar a superficie (SMR) per il controllo dei movimenti a terra.",
 applicazioni="Aeroporti strumentali di ogni categoria, avvicinamenti di precisione per scali con maltempo frequente, eliporti e aeroporti minori con procedura non strumentale.",
 vantaggi="Operatività garantita con visibilità ridotta, sicurezza degli avvicinamenti con i monitoraggi continui, capacità di scalo aumentata con i sistemi di superficie.",
 limiti="Criticità elettroniche elevate con servizi ridondanti obbligatori, manutenzione specializzata certificata, interferenze da nuove costruzioni da valutare in progetto.",
 costi_e_economia="Ordini di grandezza indicativi: sistema ILS da 1 a 3 M€ per pista; balisaggio di una pista 0,5-2 M€; manutenzione dei sistemi di assistenza 100-500 k€/anno.",
 casi_real_world="Avvicinamenti di precisione (CAT II/III) degli scali con nebbia frequente; ammodernamento dei balisaggi a LED degli aeroporti nazionali.",
 normative="Standard ICAO (Allegati 10 e 14) per i sistemi di assistenza; Reg. UE 139/2014 e regolamenti EASA di attuazione; requisiti di certificazione ENAC per i sistemi operativi.",
 note_cantiere="Le work zone vicino alle radioassistenze vanno coordinate con l'esercente: un mezzo che lavora nel campo protetto dell'ILS può oscurare il segnale di avvicinamento."),

dict(categoria="Terminal", nome="Terminal passeggeri: architetture, flussi e standard di servizio",
 descrizione="L'edificio dell'aeroporto: progettazione dei flussi passeggeri, sicurezza e standard IATA.",
 tecnologia="Flussi separati di imbarco (partenze, verifica sicurezza, gate) e sbarco (arrivi, ritiro bagagli, dogana); standard IATA di livello di servizio (LOS, Level of Service) con aree calcolate sui picchi orari; accettazione con check-in tradizionale, self-service e bag drop; controlli sicurezza con metal detector, scanner e standard EU (liquidi, elettronica); aree duty free e commerciali come raccolto di rendite non-aeronautiche; finger e piazzali di sosta aeromobili; movimentazione bagagli con sistemi automatici di smistamento (BHS); aree general aviation e business aviation; sostenibilità: certificazioni energetiche degli edifici, pannelli FV su pensiline e facciate.",
 applicazioni="Terminal di scali nazionali e internazionali, ampliamenti stagionali degli scali turistici, riqualificazioni degli edifici esistenti.",
 vantaggi="Flussi passeggeri efficienti con tempi di attesa controllati, revenue non-aeronautiche che sostengono l'economia dello scalo, edifici certificabili energeticamente, capacità di crescita modulare.",
 limiti="Sovradimensionamento rischioso per i picchi stagionali, standard di sicurezza in continuo aggiornamento, la rigidità degli edifici in esercizio rende i lavori complessi.",
 costi_e_economia="Ordini di grandezza indicativi: nuovo terminal 2.000-5.000 €/m² comprensivo di impianti e BHS; ammodernamento gate 0,5-2 M€/postazione; le revenue non-aeronautiche rappresentano 30-50% del totale dei grandi scali.",
 casi_real_world="Terminal di grandi scali italiani ristrutturati con i nuovi standard di sicurezza; finger e code ampliati per le nuove flotte a fusoliera larga.",
 normative="Standard IATA per i livelli di servizio; regolamenti UE sulla sicurezza dell'aviazione civile (controlli passeggeri e bagagli); requisiti di accessibilità (D.Lgs 198/2021); normativa antincendio per i locali di pubblico afflusso.",
 note_cantiere="Il terminal si ristruttifica per reparti con i flussi garantiti: ogni chiusura temporanea di un settore richiede il reindirizzamento dei passeggeri con segnaletica temporanea e personale."),

dict(categoria="Gestione scalo", nome="Gestione e certificazione dell'aeroporto: ENAC, EASA e sicurezza operativa",
 descrizione="Il quadro regolatorio e gestionale dello scalo: certificazione, SMS e piano aeroportuale.",
 tecnologia="Certificazione dell'aeroporto secondo il Reg. UE 139/2014 con il rilascio da parte dell'autorità competente (ENAC in Italia); Safety Management System (SMS) aeroportuale con la valutazione dei rischi operativi, la segnalazione degli incidenti e l'indagine; piano aeroportuale con la documentazione operativa (aerodrome manual); gestione della fauna pericolosa (wildlife management) con dissuasori e monitoraggi; controllo delle estensioni (RESAs) e delle pendenze; gestione del ghiaccio e della neve con piani di spazzamento e spargimento; gestione delle emergenze aeroportuali (RFF, soccorso e fuoco aeroportuale con categorie di protezione); coordinamento con le autorità (ENAV per il volo, dogane, sicurezza).",
 applicazioni="Tutti gli aeroporti certificati, gli scali in fase di rinnovo della certificazione, gli aeroporti in transizione gestionale.",
 vantaggi="Quadro certificatorio europeo uniforme che garantisce i livelli di sicurezza, la gestione del rischio documentata, l'interoperabilità tra scali nazionali e internazionali.",
 limiti="Adempimenti documentali e di personale pesanti per gli scali minori, le sanzioni per la non conformità, il rinnovo della certificazione richiede audit continui.",
 costi_e_economia="Ordini di grandezza indicativi: costi di certificazione e SMS 0,5-3% dei costi operativi dello scalo; sistemi di soccorso aeroportuale (RFF) 0,5-2 M€/anno per scalo medio.",
 casi_real_world="Certificazione degli scali italiani secondo il regolamento europeo con audit periodici; gestione della fauna negli scali vicini a zone umide con i programmi di monitoraggio.",
 normative="Reg. UE 139/2014 e regolamenti EASA di attuazione; standard ICAO (Allegato 14) e documenti di orientamento; quadro normativo nazionale di attribuzione delle competenze (ENAC, ENAV).",
 note_cantiere="Ogni modifica alla piastra di volo o ai sistemi operativi (opere edili comprese) entra nel sistema di certificazione: le varianti vanno comunicate e approvate prima dell'esercizio."),

dict(categoria="Ambientale", nome="Rumore aeroportuale, ostacoli al volo e compatibilità territoriale",
 descrizione="L'aeroporto e il territorio: mappe di rumore, zone di rispetto e piani di mitigazione.",
 tecnologia="Misure e mappe di rumore aeroportuale secondo la normativa vigente (classificazione acustica degli aeroporti con zone di rispetto); le aree di rispetto (A, B, C, D) con i vincoli edilizi corrispondenti; monitoraggio continuo del rumore con centraline fisse e mobili; ostacoli alla navigazione aerea: OLS (Obstacle Limitation Surfaces) con superfici di delimitazione coniche e transitorie che vietano le costruzioni in prossimità delle piste; valutazione dei nuovi edifici alte con procedure di autorizzazione; piani di mitigazione del rumore con le rotte e le procedure operative; compensazioni e barriere foniche; coinvolgimento delle comunità con i tavoli di concertazione.",
 applicazioni="Aeroporti vicini ai centri urbani, pianificazione territoriale attorno agli scali, valutazione di progetti edilizi in zona aeroportuale, procedimenti di autorizzazione degli ostacoli.",
 vantaggi="Compatibilità tra lo sviluppo dello scalo e la qualità ambientale, trasparenza verso le comunità con le mappe pubbliche, prevenzione dei contenziosi con i vincoli chiari.",
 limiti="Il rumore è percepito e politicamente sensibile, i vincoli edilizi impattano il mercato immobiliare, le mitigazioni costano e richiedono tempi, le rotte di mitigazione possono spostare il disturbo altrove.",
 costi_e_economia="Ordini di grandezza indicativi: sistemi di monitoraggio del rumore 100-500 k€; barriere foniche e mitigazioni edilizie 0,5-5 M€ secondo estensione; le compensazioni ambientali sono parte dei progetti di espansione.",
 casi_real_world="Tavoli di concertazione degli scali con le comunità locali; vincoli edilizi nelle zone di rispetto degli aeroporti nazionali.",
 normative="Normativa nazionale sulla classificazione acustica degli aeroporti e sulle zone di rispetto (testo consolidato vigente); regolamenti ICAO sulle superfici di delimitazione degli ostacoli; procedura di valutazione ambientale (D.Lgs 152/2006) per le opere.",
 note_cantiere="Prima di progettare vicino a un aeroporto si verifica la mappa di classificazione acustica e le superfici OLS: un edificio 'giusto' nella zona sbagliata diventa un ostacolo da demolire."),

dict(categoria="Cargo", nome="Cargo aeroportuale, hub di merci e logistica integrata",
 descrizione="L'aeroporto come piattaforma logistica: terminal merci, frigo e intermodalità.",
 tecnologia="Terminal cargo con magazzini di trasstamento, celle frigorifere per la catena del freddo, aree per merci pericolose (DGR) con standard IATA; piattaforme per gli integratori express con hub notturni di smistamento; collegamenti intermodali con la rete stradale e ferroviaria (rail hubs); movimentazione con traslochi elevabili e ULD (Unit Load Devices) conformi; sicurezza della catena merci con i regimi di sicurezza (Reg. CE 300/2008 — real: regolamento relativo alla sicurezza dell'aviazione civile per le merci); gestione della paperless con le e-AWB (air waybill elettroniche); integrazione con le zone economiche speciali e i distretti logistici.",
 applicazioni="Hub cargo internazionali, piattaforme per il trasporto farmaceutico e deperibile, aeroporti regionali con ambizioni logistiche, integratori express.",
 vantaggi="Valore per unità di peso delle merci aeree che giustifica i costi, catena del freddo garantita per farmaci e freschi, integrazione con la logistica terrestre che amplia il bacino d'utenza.",
 limiti="I mercati cargo sono ciclici e sensibili alla geopolitica, l'infrastruttura costosa richiede volumi minimi, la concorrenza tra scali è forte sullo stesso bacino.",
 costi_e_economia="Ordini di grandezza indicativi: terminal cargo 1.000-2.500 €/m²; celle frigo 300-800 €/m²; i canoni dei magazzini aeroportuali sono tra i più alti della logistica.",
 casi_real_world="Hub cargo degli scali internazionali europei; piattaforme farmaceutiche certificate GDP nei principali aeroporti.",
 normative="Reg. UE 300/2008 (sicurezza dell'aviazione civile per le merci); standard IATA per le DGR e le e-AWB; requisiti GDP per la catena del freddo farmaceutica.",
 note_cantiere="Il cargo lavora di notte e in sicurezza: i cantieri vicino ai terminal merci si coordinano con gli orari di volo e i controlli di accesso."),

dict(categoria="Aviazione leggera", nome="Aviazione generale, eliporti e aviazione leggera: infrastrutture minime",
 descrizione="La coda lunga del volo: aviosuperfici, eliporti e aeroporti minori.",
 tecnologia="Aviosuperfici e aeroporti minori con piste in erba o asfalto di 600-1.200 m; eliporti con piazzali circolari, balisaggi e servizi minimi (refueling, hangar); gestione delle licenze ENAC per le aviosuperfici e i campi di volo; aviazione sportiva e scuole di volo con aree dedicate; gestione del traffico VFR (Visual Flight Rules) con le frequenze di torre e l'informazione volo; manutenzione delle pavimentazioni leggere con cicli di budget contenuti; FBO (Fixed Base Operator) per l'aviazione business nei piccoli scali; valorizzazione turistica degli aeroporti territoriali.",
 applicazioni="Aeroporti regionali, campi di volo sportivi, eliporti ospedalieri e aziendali, aviosuperfici turistiche.",
 vantaggi="Accessibilità del volo per la formazione, il turismo e i servizi (elisoccorso), costi di gestione contenuti rispetto agli scali maggiori, valorizzazione dei territori periferici.",
 limiti="Sostenibilità economica debole senza volumi, standard di certificazione ridotti che impongono limiti operativi, dipendenza da enti locali e passioni private.",
 costi_e_economia="Ordini di grandezza indicativi: aviosuperficie semplice 0,2-1 M€; eliporto 0,3-2 M€ secondo servizi; gestione annuale di un campo di volo 50-300 k€.",
 casi_real_world="Rete degli aeroporti regionali italiani; eliporti di rete per l'elisoccorso e i collegamenti con le isole.",
 normative="Regolamenti ENAC per le aviosuperfici e gli eliporti; standard ICAO per le infrastrutture di volo generali; normativa per l'attività di volo sportivo e turistico.",
 note_cantiere="L'aviosuperficie non è 'il campo dietro casa': pendenze, ostacoli e gestione della fauna si verificano come in uno scalo maggiore, solo con standard ridotti."),

dict(categoria="Interventi", nome="Lavori in aeroporto in esercizio: coordinamento, sicurezza e finestre operative",
 descrizione="Costruire mentre gli aerei volano: i cantieri nello scalo operativo.",
 tecnologia="Piano di coordinamento con l'esercente (gestore aeroportuale) con le work zone certificate; finestre di lavoro notturne (notte di scalo) con la riapertura della piastra di volo certificata al termine; gestione degli accessi con badge aeroportuali e Security Awareness; protezione dei sistemi operativi (ILS, balisaggi) con distacchi e calibrazioni dopo i lavori; gestione del FOD con barriere, coperture dei materiali e bonifica finale; coordinamento con le torri di controllo per le chiusure temporanee di vie di rullaggio; gestione delle interferenze radar e radio delle gru e delle attrezzature; documentazione delle varianti per la certificazione.",
 applicazioni="Rifacimenti piazzali e piste, ampliamenti terminal, nuove infrastrutture (MRO, cargo) negli scali operativi.",
 vantaggi="Continuità dell'esercizio durante i lavori con la pianificazione delle finestre, la sicurezza garantita dal coordinamento certificato, la qualità con le bonifiche finali documentate.",
 limiti="Finestre brevi che impongono tecnologie rapide (cls ad alta resistenza precoce), i ritardi si accumulano con gli annulli per meteo o traffico, il costo del cantiere notturno è maggiorato.",
 costi_e_economia="Ordini di grandezza indicativi: premio notturno e di coordinamento +30-80% sul costo diretto; chiusura di una pista costa allo scalo decine di migliaia di euro l'ora in capacità persa.",
 casi_real_world="Rifacimenti notturni delle piste degli scali di grande traffico con riapertura quotidiana alle 6 del mattino; cantieri cargo con i work package settimanali.",
 normative="Reg. UE 139/2014 per le modifiche in esercizio; regolamenti sulla sicurezza (security) dell'accesso alle aree operativi; piani di coordinamento dell'esercente con i requisiti di certificazione.",
 note_cantiere="La regola d'oro del cantiere aeroportuale: nulla resta sulla piastra di volo che non sia documentato e bonificato; la bonifica finale firmata è il pass per riaprire."),

dict(categoria="Economia", nome="Economia aeroportuale: investimenti, revenue e modelli di gestione",
 descrizione="I numeri dello scalo: come si finanzia un aeroporto e da cosa vive.",
 tecnologia="Modello economico degli aeroporti: revenue aeronautiche (tasse di scalo, atterraggio, parcheggio) e non aeronautiche (commerciali, parking, cargo); gestione in house o in concessione (modello italiano con gestori privati e partecipazioni pubbliche); finanziamento degli investimenti con i piani pluriennali e il project financing; il rapporto con le compagnie aeree: incentivi, marketing route development; il peso degli oneri di sicurezza e certificazione sui conti; le esternalità positive (indotto occupazionale e turistico) usate nei dossier di progetto; gestione degli asset immobiliari (aree dismesse, cargo city); valutazione delle espansioni con l'analisi costi-benefici.",
 applicazioni="Piani di sviluppo aeroportuale, valutazioni di concessione, dossier di finanziamento delle opere.",
 vantaggi="Chiarezza dei modelli di business che guida gli investimenti, la diversificazione non-aeronautica stabilizza i conti, gli studi di indotto legittimano le opere pubbliche.",
 limiti="La stagionalità e i cicli del traffico aereo, la concorrenza tra scali sullo stesso bacino, i vincoli di concessione pubblica con gli equilibri di bilancio.",
 costi_e_economia="Ordini di grandezza indicativi: investimenti di espansione degli scali maggiori da centinaia di milioni a diversi miliardi; indotto occupazionale stimato per ogni milione di passeggeri annui da decine a centinaia di posti (da verificare per scalo).",
 casi_real_world="Modelli di gestione dei principali scali italiani con concessioni pluriennali; piani di sviluppo con le cargo city e i distretti logistici.",
 normative="D.Lgs 36/2023 per le concessioni e i contratti pubblici; regolamenti UE sulla gestione degli slot e sulle tasse aeroportuali; normativa nazionale di settore vigente.",
 note_cantiere="Il progetto aeroportuale si valuta su 20-30 anni con scenari di traffico prudenti: la storia degli scali pieni di infrastrutture sottoutilizzate insegna."),

dict(categoria="Innovazione", nome="Aeroporti sostenibili: elettrificazione, SAF e gestione delle risorse",
 descrizione="Il futuro dello scalo: voli meno impattanti, energia propria e gestione delle acque.",
 tecnologia="Elettrificazione delle operazioni di terra (GPU elettriche, bus elettrici, la pista di decollo assistita elettricamente nei progetti di breve termine); SAF (Sustainable Aviation Fuels) con obblighi di miscelazione in progressivo aumento secondo la normativa UE (RefuelEU Aviation); gestione energetica: impianti FV su pensiline e terminal, accumuli, parchi eolici laddove compatibili; gestione delle acque meteoriche delle piastre di volo (trattamenti prima dello scarico); la sfida dell'idrogeno per l'aviazione (H2 hub aeroportuali in sperimentazione); monitoraggio delle emissioni e delle microplastiche dai pneumatici; certificazioni ambientali degli scali e carbon management.",
 applicazioni="Aeroporti in piani di decarbonizzazione, infrastrutture di rifornimento SAF e idrogeno, gestione ambientale degli scali.",
 vantaggi="Riduzione delle emissioni di scalo e della dipendenza dai combustibili fossili, immagine ambientale che dialoga con le comunità, conformità alla normativa UE in anticipo.",
 limiti="Gli impianti SAF e H2 sono capital intensive, la disponibilità di SAF è limitata e costosa, l'idrogeno richiede infrastrutture e sicurezza dedicate, i benefici del SAF non eliminano le emissioni di scalo.",
 costi_e_economia="Ordini di grandezza indicativi: SAF 2-6 volte il costo del Jet A-1; GPU elettriche e infrastrutture 0,5-3 M€ per scalo; FV aeroportuali da centinaia di kWp a diversi MWp secondo superficie.",
 casi_real_world="Impianti SAF in costruzione in Europa con gli obiettivi RefuelEU; parchi FV installati negli aeroporti italiani sulle aree di nuova costruzione.",
 normative="Regolamento UE RefuelEU Aviation (obblighi di SAF); normativa sulle emissioni e sulla gestione ambientale degli aeroporti; standard ICAO CORSIA per le emissioni internazionali.",
 note_cantiere="Gli impianti H2 in aeroporto cambiano la sicurezza di progetto: zone ATEX, distanze di sicurezza e nuove competenze di gestione vanno previsti prima di firmare il progetto."),
]

write_pack("AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK",
 "Aeroporti e infrastrutture di volo", "FACOLTA_INGEGNERIA", "L2-L3",
 "Piste e pavimentazioni ACN/PCN, segnaletica e ILS, terminal, certificazione EASA/ENAC, rumore e ostacoli, cargo, aviazione generale, lavori in esercizio, economia, sostenibilità.",
 """# AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK

**Aeroporti e infrastrutture di volo**

Piste e pavimentazioni con sistema ACN/PCN, segnaletica e sistemi di assistenza alla navigazione (ILS, VOR/DME), terminal passeggeri e standard IATA, certificazione e gestione dello scalo (Reg. UE 139/2014, ENAC, SMS), rumore aeroportuale e ostacoli al volo, cargo e logistica integrata, aviazione generale ed eliporti, cantieri in esercizio, economia aeroportuale, elettrificazione e SAF.

Schede: 10 (formato JSONL, un oggetto per riga).
""", aeroporti)

# =====================================================================
# PACK 2 — PORTI E OPERE MARITTIME
# =====================================================================
porti = [
dict(categoria="Strutture portuali", nome="Dighe foranee, moli e banchine portuali",
 descrizione="L'ossatura del porto: le opere di riparo e gli attracchi delle navi.",
 tecnologia="Dighe foranee in cls a cassoni o in massi (tetrapodi, accropodi) che proteggono il bacino dall'onda; moli in cls con banchine d'attracco dotate di cuscinetti fenders (fenditori) e bollards (gallocce) con capacità 10-150 t; banchine a dente per il Ro-Ro con rampe e pontili mobili; strutture d'attracco per navi portacontainer con portata su pila e distanze per le gru; altezza d'attracco calcolata sui dislivelli di marea; correnti e sedimentazione nel bacino; sistemi di ancoraggio e boe per i grandi fondali; manutenzione dei fenders e dei rivestimenti.",
 applicazioni="Porti commerciali, terminal container, porti Ro-Ro passeggeri e traghetti, porti industriali.",
 vantaggi="Riparo garantito per le operazioni di carico in sicurezza, attracchi dimensionati per le flotte di progetto, durabilità delle strutture marine con le protezioni corrette.",
 limiti="Sedimentazione continua che richiede dragaggi, aggressione marina del cls e dell'acciaio, i cuscinetti fenders vanno sostituiti periodicamente.",
 costi_e_economia="Ordini di grandezza indicativi: diga foranea 10.000-30.000 €/m lineare; banchina commerciale 5.000-20.000 €/m lineare; manutenzione fenders 5-10% del valore installato ogni 5-10 anni.",
 casi_real_world="Digue foranee dei porti commerciali mediterranei realizzate a cassoni; ammodernamento delle banchine dei porti container.",
 normative="Normativa sulle concessioni demaniali marittime; classificazione ambientale marina per i materiali (ISO 12944 e specifiche marine); norme per gli appalti portuali e le opere marittime.",
 note_cantiere="La banchina si collauda in mare: i carichi di ormeggio di prova e l'ispezione subacquea con sonar e immersioni certificate chiudono la commessa."),

dict(categoria="Terminalistica", nome="Terminal container, Ro-Ro e piattaforme logistiche portuali",
 descrizione="L'interfaccia nave-terra: terminal a contenitori, rotabili e la logistica del porto.",
 tecnologia="Terminal container con banchine servite da gru portuali (Ship-to-Shore cranes, portata 40-100 t in spreader), piazzali con RTG (Rubber Tyred Gantry) o gru a portale su rotaia; movimentazione dei container con reach stacker e carrelli elevatori; terminal Ro-Ro con rampe a ponte mobile, piazzali di stoccaggio dei rimorchi, gates per l'imbarco dei passeggeri; connessioni ferroviarie portuali con binari di presa e stazioni di smistamento; depositi doganali e aree per le merci pericolose; sistemi informativi terminal (TOS, Terminal Operating System) per la gestione dei movimenti; sicurezza delle operazioni con i piani ISPS (International Ship and Port Facility Security).",
 applicazioni="Porti gateway del traffico internazionale, hub del Mediterraneo, porti Ro-Ro dell'Adriatico, terminal intermodali.",
 vantaggi="Velocità di movimentazione che riduce i tempi nave in porto, integrazione modale che allarga il bacino, efficienza con i sistemi informativi di terminal.",
 limiti="Investimenti in attrezzature elevati, la produttività dipende dall'integrazione delle fasi, i colli di bottiglia nei gate e nei trasporti interni, la sicurezza ISPS impone procedure rigide.",
 costi_e_economia="Ordini di grandezza indicativi: gru STS 8-20 M€ l'una; RTG 1-3 M€; piazzale portuale 50-150 €/m²; produttività di riferimento 20-40 movimenti/ora per gru.",
 casi_real_world="Terminal container dei porti del nord Europa e mediterranei; piattaforme Ro-Ro adriatiche con i collegamenti con la Grecia e la Turchia.",
 normative="Codice ISPS (convenzione IMO SOLAS XI-2) per la sicurezza portuale; standard internazionali per le attrezzature portuali; regolamenti UE sulla sicurezza delle operazioni portuali.",
 note_cantiere="Il terminalista lavora 24/7: i cantieri di ampliamento si fanno per fasi con la ricollocazione dei piazzali; ogni modifica agli assi di movimentazione si simula prima con il TOS."),

dict(categoria="Porti turistici", nome="Porti turistici e cantieri nautici: darsene, boe e assistenza",
 descrizione="La nautica da diporto: porti turistici, cantieri di manutenzione e servizi.",
 tecnologia="Porti turistici con darsene interne riparate, banchine d'ormeggio per imbarcazioni 6-30 m, servizi di banchina (acqua, energia, scarichi); sistemi di ormeggio su boe per i grandi yacht; travel lift e cantieri di manutenzione con rampe di varo; carenaggi con sistemi di raccolta delle acque di scarico e dei residui di sabbiatura (antifouling); sistemi di controllo accessi e servizi igienici; gestione ambientale delle acque di rifiuto nautiche con stazioni di raccolta; pontili galleggianti e passerelle; rifornimento carburante con sistemi antincendio dedicati.",
 applicazioni="Porti turistici dei litorali e delle isole, marina per lo yachting di lusso, cantieri nautici di manutenzione.",
 vantaggi="Ospitalità completa per la nautica con servizi di qualità, manutenzione integrata con l'ormeggio, presidio ambientale dei rifiuti nautici.",
 limiti="Stagionalità del traffico, il fondale dei bassi richiede dragaggi continui, la sabbiatura delle carene è tra le fonti principali di inquinamento da rame e biocidi.",
 costi_e_economia="Ordini di grandezza indicativi: posto barca in costruzione 10.000-40.000 € per imbarcazione da 12-18 m; canone annuo 1.500-6.000 €; pontile galleggiante 300-800 €/m lineare.",
 casi_real_world="Marine turistiche della costa adriatica e tirrenica con i servizi integrati; cantieri con sistemi di sabbiatura a chiusura e riciclo.",
 normative="DPR 498/1992 (regolamento di disciplina delle attività marittime di diporto) come quadro; normativa ambientale sulle acque di rifiuto nautiche; autorizzazioni paesaggistiche per le opere in mare.",
 note_cantiere="La sabbiatura a vista è finita: i cantieri nautici con i sistemi a chiusura e la raccolta dei residui sono l'unico modello conforme e difendibile."),

dict(categoria="Difesa costiera", nome="Opere di difesa costiera: frangiflutti, ricariche e arretramento",
 descrizione="Il mare che avanza: la difesa delle coste tra opere dure, ricariche e adattamento.",
 tecnologia="Frangiflutti sommersi ed emergenti in massi (rip-rap) o cls (tetrapodi, X-block, caissons) che dissipano l'energia dell'onda prima della riva; ricariche sabbiosi con rete di sostegno dei profili (geotubi, gabbioni) che reintegrano le spiagge erose; briglie e pennelli costieri (groynes) che trattenono la deriva longitudinale del sedimento; dune artificiali e rinforzo con opere a basso impatto; arretramento gestito (managed retreat) con la rilocazione delle opere vulnerabili; ripristino degli ambienti dunali e delle posidonia come difesa naturale; monitoraggio della linea di costa con rilievi LiDAR e droni.",
 applicazioni="Litorali erosi ad alta densità turistica, coste basse con insediamenti, spiagge balneari da tutelare, porti con sedimentazione dovuta alle opere.",
 vantaggi="Protezione di beni turistici e insediativi, ricostruzione delle spiagge come valore economico, integrazione tra opere dure e gestione del sedimento.",
 limiti="L'erosione si sposta lungo la costa (effetti a scafo), i frangiflutti alterano la dinamica dei litorali, le ricariche sono periodiche e costose, il cambiamento climatico alza il livello marino.",
 costi_e_economia="Ordini di grandezza indicativi: frangiflutti sommerso 3.000-10.000 €/m lineare; ricarica sabbiosa 15-50 €/m³ posato; gestione pluriennale del litorale con i piani costieri.",
 casi_real_world="Piani di difesa costiera con ricariche sabbiosi dei litorali adriatici; frangiflutti sommersi delle coste turistiche.",
 normative="Piani di assetto del territorio costiero e normativa sulla fascia demaniale marittima; valutazioni ambientali per le opere in mare (D.Lgs 152/2006); linee guida per la difesa costiera in adattamento al cambiamento climatico.",
 note_cantiere="La difesa costiera si progetta col moto ondoso di progetto E con la gestione del sedimento dell'intero litorale: l'opera che salva una spiaggia ne uccide un'altra se pensata da sola."),

dict(categoria="Dragaggi", nome="Dragaggi portuali e gestione dei sedimenti marini",
 descrizione="Tenere aperto il canale: dragaggi di manutenzione e di nuovo canale, gestione delle terre emerse.",
 tecnologia="Dragaggi con draghe a cucchiaio (dredging), aspiranti con disgregatore (cutter suction) o a scuotitore (trailing suction hopper dredge); capienze delle draghe da centinaia a decine di migliaia di m³; smaltimento dei materiali dragati: ricollocazione in mare (se inquinamento contenuto), riempimento, realizzazione di aree umide o isole; caratterizzazione dei sedimenti per la destinazione (trace analysis per i metalli pesanti); manutenzione dei canali di accesso con i piani di dragaggio pluriennali; gestione dei materiali contaminati con il confinamento o il trattamento; monitoraggio ambientale durante le operazioni con rilevamento della torbidità.",
 applicazioni="Canali portuali e di accesso, bacini portuali, canali navigabili interni, ripascimento delle spiagge con i sedimenti compatibili.",
 vantaggi="Navigabilità garantita con i piani di manutenzione, disponibilità di materiali per le ricariche (se compatibili), gestione integrata dei sedimenti del sistema portuale.",
 limiti="Costi continui di manutenzione, i sedimenti contaminati vanno caratterizzati e gestiti come rifiuti, l'impatto della torbidità sui prati di posidonia, l'opinione pubblica sensibile.",
 costi_e_economia="Ordini di grandezza indicativi: dragaggio di manutenzione 5-20 €/m³; dragaggi con smaltimento 20-80 €/m³ secondo la destinazione; piani pluriennali da decine di migliaia a milioni di euro l'anno.",
 casi_real_world="Piani di dragaggio dei porti adriatici con la ricollocazione dei sedimenti; caratterizzazione dei fanghi portuali prima della destinazione.",
 normative="D.Lgs 152/2006 per la gestione dei sedimenti marini e le destinazioni; normativa sulle acque di scarico e il monitoraggio marino; convenzioni internazionali (Convention of London) per la ricollocazione in mare.",
 note_cantiere="La destinazione dei sedimenti si decide in laboratorio, non in cantiere: la caratterizzazione prima del dragaggio evita di bloccare i lavori con le analisi."),

dict(categoria="Demanio", nome="Concessioni demaniali marittime e pratiche per le opere in mare",
 descrizione="La gabbia amministrativa del mare: chi può costruire, dove e con quali autorizzazioni.",
 tecnologia="Demanio marittimo dello Stato e dei porti: concessioni per le opere fisse (banchine, pontili, frangiflutti) con le procedure del Codice della Navigazione; autorizzazioni per le opere temporanee di cantiere (piattaforme, scafi) e per le attività; le concessioni demaniali del demanio marittimo (spiaggia e mare) con i canoni; il rilascio delle aree di cantiere con il ripristino dell'ambiente; gli iter con la Capitaneria di Porto (comando della Guardia Costiera) per le interferenze con la navigazione; le valutazioni ambientali per le opere in mare; la disciplina delle aree marine protette dove le opere sono vietate o limitate.",
 applicazioni="Nuove opere portuali, pontili e piattaforme, cantieri in mare, stabilimenti balneari, opere di difesa costiera.",
 vantaggi="Iter riconoscibili con gli enti chiave (Demani, Capitanerie, ARPA), chiarezza sui limiti delle aree protette, tutela della navigazione con gli accordi operativi.",
 limiti="Iter lunghi e multisoggetto, i canoni demaniali incidono sull'economia, i cambiamenti di destinazione d'uso richiedono varianti, la sensibilità ambientale crescente.",
 costi_e_economia="Ordini di grandezza indicativi: i canoni demaniali e le pratiche incidono 1-5% sul costo dell'opera; i tempi di autorizzazione di 6-24 mesi da pianificare.",
 casi_real_world="Concessioni portuali pluriennali con gli investimenti di terminalistica; pratiche per i pontili turistici con le autorizzazioni ambientali.",
 normative="Codice della Navigazione per le acque marittime; normativa demaniale (concessioni, canoni); D.Lgs 152/2006 (valutazioni ambientali e aree marine protette); regolamenti per le attività marittime.",
 note_cantiere="Il cantiere in mare è un'attività marittima: le comunicazioni alla Capitaneria, le boe di segnalazione e i piani di emergenza anti-inquinamento sono parte del cantiere, non un optional."),

dict(categoria="Clima marino", nome="Il clima marino: onde, maree e classificazione ambientale delle opere",
 descrizione="Le forze del mare che progettano le opere: moto ondoso, maree e la classificazione ambientale dei materiali.",
 tecnologia="Moto ondoso con altezza significativa (Hs) e periodo (Tp) come azioni di progetto; le onde di tempesta con i ritorni di 50-200 anni per le opere portuali; la marea astronomica con gli estremi (sacca di marea nell'Adriatico 0,5-1,5 m, Mediterraneo 0,2-0,4 m); le mareggiate con i transfer functions per la trasmissione oltre i frangiflutti; la corrosione marina accelerata (cicli di marea, salinità, ossigeno) che classifica gli ambienti come C5-M/CX secondo ISO 12944; i materiali per il mare: cls con basso rapporto a/c e copriferro elevato, acciaio con zincatura pesante + duplex o acciai speciali; le biocorrosioni e le incrostazioni; le prove di laboratorio per la resistenza al sale.",
 applicazioni="Ogni opera in mare (porti, dighe, frangiflutti, pontili), le sovrastrutture metalliche marine, i cantieri nautici.",
 vantaggi="Azioni di progetto definite con le serie storiche dei dati ondametrici, materiali selezionati per la durabilità marina, manutenzione programmabile.",
 limiti="La variabilità del clima marino in cambiamento (onde estreme più frequenti), i costi dei materiali marini, il degrado nascosto delle strutture sommerse.",
 costi_e_economia="Ordini di grandezza indicativi: premium dei materiali marini +20-60%; ispezioni subacquee 5.000-30.000 €/campaign; cicli di verniciatura duplex ogni 10-20 anni.",
 casi_real_world="Strutture portuali con classificazione CX e sistemi duplex; frangiflutti dimensionati sulle onde di ritorno 200 anni.",
 normative="ISO 12944 (classificazione ambientale e protezione anticorrosiva); norme tecniche per il calcolo delle opere marittime con le azioni ondametriche; linee guida CNR-DT 207/2008 per le costruzioni in zona sismica e ambienti particolari.",
 note_cantiere="In mare la manutenzione costa il doppio: la zincatura ritoccata male sotto l'acqua si stacca in pezzi; le ispezioni subacquee certificate documentano lo stato prima che la struttura lo dichiari da sola."),

dict(categoria="Economia", nome="Economia portuale e logistica marittima: investimenti e catene del valore",
 descrizione="I numeri del porto: investimenti, occupazione e integrazione con la logistica terrestre.",
 tecnologia="Modelli di governance dei porti: autorità di sistema portuale con i bacini portuali; investimenti infrastrutturali pubblici e investimenti terminalistici privati in concessione; le revenue portuali: tasse di ancoraggio, canoni demaniali, concessioni; il collegamento con le reti terrestri (port gates, interporti, connessioni ferroviarie); le externalità: indotto occupazionale e valore del transito; le catene logistiche internazionali con i principali operatori (carrier, terminalisti, spedizionieri); la digitalizzazione: piattaforme Port Community System per la dematerializzazione delle pratiche; la competitività dei porti italiani sulle rotte del Mediterraneo.",
 applicazioni="Piani strategici portuali, valutazioni di investimento terminalistica, dossier di raccordo intermodale.",
 vantaggi="Chiarezza dei modelli di business pubblico-privato, integrazione porto-terra che amplia i bacini di utenza, digitalizzazione che riduce i tempi amministrativi.",
 limiti="La competizione tra porti sullo stesso bacino, gli investimenti infrastrutturali lunghi, le inefficienze dei collegamenti terrestri che penalizzano il porto, la stagionalità di alcuni traffici.",
 costi_e_economia="Ordini di grandezza indicativi: investimenti terminalistici 50-500 M€ per gli hub; indotto occupazionale stimato per i porti commerciali da migliaia a decine di migliaia di posti.",
 casi_real_world="Riforma delle autorità di sistema portuale con i bacini del nord e del centro-sud; i piani di sviluppo con le connessioni ferroviarie portuali.",
 normative="Codice della Navigazione e normativa sulle autorità di sistema portuale; D.Lgs 36/2023 per le concessioni e gli appalti; regolamenti UE sulla concorrenza portuale.",
 note_cantiere="Il porto è un sistema: l'investimento più costoso fallisce se il gate terrestre resta a due corsie; i progetti si valutano con la catena logistica completa."),

dict(categoria="Cantieri marini", nome="Cantieri marittimi: navi-cantiere, piattaforme e lavorazioni subacquee",
 descrizione="Come si costruisce in mare: le tecniche, le imbarcazioni e la sicurezza del cantiere marino.",
 tecnologia="Navi-cantiere (floating cranes) per i posamenti di grandi elementi; barche-gru e pontoni per i getti marini; piattaforme di lavoro autoscandenti per i paramenti delle dighe; cassoni realizzati in banchina, varati e posati con i sistemi di traino e affondamento controllato; il cls marino gettato con tubi a perdere (tremie) e miscela autosistemante; le lavorazioni subacquee con i sommozzatori commerciali certificati per le ispezioni e i lavori leggeri; i sistemi di posa dei rivestimenti subacquei; la meteorologia marina come vincolo di pianificazione con le finestre di posa; i piani di emergenza anti-inquinamento con le barriere galleggianti.",
 applicazioni="Costruzione e manutenzione di opere portuali, dighe foranee, fondazioni marine, condotte sottomarine, cantieri di ripascimento.",
 vantaggi="Possibilità di lavorare oltre la costa e nei fondali profondi, precisione dei posamenti con il gps marino, lavorazione protetta dalle condizioni del mare con le piattaforme.",
 limiti="Costi giornalieri elevati delle attrezzature marine, dipendenza totale dalle condizioni meteomarine, la sicurezza dei lavoratori in mare (overboarding), la logistica dei materiali dalla banchina.",
 costi_e_economia="Ordini di grandezza indicativi: noleggio barca-gru 5.000-30.000 €/giorno; operazioni subacquee certificate 1.000-5.000 €/giornata; getto marino +30-80% rispetto al getto aereo.",
 casi_real_world="Posamento dei cassoni delle dighe foranee con le finestre meteomarine; interventi subacquei di riparazione delle banchine.",
 normative="Normativa sulla sicurezza dei lavoratori in mare (formazione, DPI, procedure); convenzioni IMO per la prevenzione dell'inquinamento (MARPOL); norme per le attrezzature di lavoro galleggianti.",
 note_cantiere="Il mare comanda il cantiere: le finestre di posa si prenotano sulle previsioni e si perdono col mare mosso; ogni imprevisto costa giornate intere di noleggio."),

dict(categoria="Sostenibilità", nome="Porti sostenibili: shore power, elettrodomestici e gestione ambientale dei bacini",
 descrizione="Il futuro del porto: navi altra-ormeggio alimentate da terra, acque pulite e gestione delle risorse.",
 tecnologia="Shore power (Cold Ironing): le navi in banchina si alimentano con l'energia elettrica da terra (onshore power supply) eliminando le emissioni dei generatori di bordo; requisiti tecnici di potenza (0,5-2 MW per nave), connessioni automatiche e standard internazionali; la gestione ambientale dei bacini: raccolta delle acque di rifiuto nautiche, monitoraggio della qualità delle acque, tutela delle praterie di posidonia; i pannelli fotovoltaici su capannoni portuali e le colonnine per le auto; l'idrogeno e i combustibili marini alternativi (metanolo, ammoniaca) nelle fasi di sperimentazione; le certificazioni ambientali dei porti (ECOPORTS) e i piani di gestione ambientale; la gestione dei rifiuti portuali e la rigenerazione dei sedimenti.",
 applicazioni="Porti con bacini urbani vicini, terminal crociere con le grandi navi, porti in aree sensibili ambientalmente.",
 vantaggi="Riduzione immediata delle emissioni in banchina (NOx, SOx, PM), immagine ambientale del porto, conformità alle normative UE sulle emissioni marittime in anticipo.",
 limiti="Investimenti elettrici pesanti, standard tecnici in evoluzione (connessioni diverse per le flotte), il costo dell'energia, la disponibilità dei combustibili alternativi ancora limitata.",
 costi_e_economia="Ordini di grandezza indicativi: impianto shore power per postazione 0,5-3 M€; il premio del metanolo verde 2-4 volte il MDO; FV portuali 600-1.000 €/kWp installato.",
 casi_real_world="Porti con shore power operativo per le crociere; i progetti UE di combustibili marini alternativi nei porti del nord Europa.",
 normative="Normativa UE sulle emissioni marittime (sulphur directive) e sugli obblighi di shore power; regolamenti IMO sulle emissioni delle navi; la normativa ambientale dei bacini portuali.",
 note_cantiere="Lo shore power cambia il quadro elettrico del porto: i sottostazioni, i cavidotti e la gestione delle potenze di punta vanno dimensionati prima di installare la prima banchina elettrificata."),
]

write_pack("PORTI_E_OPERE_MARITTIME_PACK",
 "Porti e opere marittime", "FACOLTA_INGEGNERIA", "L2-L3",
 "Dighe foranee e banchine, terminal container e Ro-Ro, porti turistici, difesa costiera, dragaggi, demanio marittimo, clima marino, economia portuale, cantieri marini, sostenibilità.",
 """# PORTI_E_OPERE_MARITTIME_PACK

**Porti e opere marittime**

Dighe foranee, moli e banchine, terminal container e Ro-Ro, porti turistici e cantieri nautici, opere di difesa costiera, dragaggi e gestione dei sedimenti, concessioni demaniali marittime, clima marino e classificazione ambientale, economia portuale, cantieri marittimi e lavorazioni subacquee, porti sostenibili con shore power.

Schede: 10 (formato JSONL, un oggetto per riga).
""", porti)

# =====================================================================
# PACK 3 — EMERGENZE E RICOSTRUZIONE POST-SISMA
# =====================================================================
emergenze = [
dict(categoria="Protezione civile", nome="Il sistema della protezione civile: ruoli, livelli e codice",
 descrizione="Come l'Italia organizza l'emergenza: il codice della protezione civile e la catena del comando.",
 tecnologia="Codice della protezione civile (D.Lgs 1/2018) con i quattro livelli operativi: comunale, provinciale/regionale, statale (opera in connessione organica); i Centri Operativi Comunali (COC) e i Centri Funzionali con la valutazione dei rischi; le componenti operative: Vigili del Fuoco (soprintendenze speciali), Dipartimento della Protezione Civile nazionale, servizi sanitari, forze dell'ordine, volontariato organizzato; i moduli di intervento nazionali (USAR, soccorso sanitario, trasporti); il piano comunale di emergenza con le zone di raccolta e le vie di fuga; l'attivazione dei centri operativi con le fasi: segnalazione, valutazione, dichiarazione dello stato di emergenza.",
 applicazioni="Terremoti, alluvioni, frane, incendi boschivi, emergenze industriali; ogni comune e impresa deve conoscere il sistema per operare nella fase di risposta.",
 vantaggi="Catena di comando definita che evita il caos, risorse modulari attivabili per scala, la normativa chiarisce i ruoli di comuni, regioni e Stato.",
 limiti="La complessità del sistema richiede esercitazioni continue, le risorse locali sono spesso insufficienti, la comunicazione pubblica è critica nei primi minuti.",
 costi_e_economia="Ordini di grandezza indicativi: esercitazioni nazionali 0,5-5 M€; attrezzature USAR di squadra 100-500 k€; la fase di risposta costa 1-10% del danno totale secondo l'evento.",
 casi_real_world="La risposta ai terremoti del 2016 con il coordinamento dei moduli nazionali; le esercitazioni nazionali annuali del sistema di protezione civile.",
 normative="D.Lgs 1/2018 (Codice della protezione civile) con i decreti attuativi; direttiva del Presidente del Consiglio sui criteri di gestione delle emergenze; piani comunali e provinciali di protezione civile.",
 note_cantiere="L'impresa che lavora in zona sismica o idrogeologica fa parte del sistema: i piani di emergenza aziendali si coordinano con il COC comunale e i cantieri dichiarano i mezzi e le sostanze disponibili."),

dict(categoria="Prima fase", nome="Le prime 72 ore dopo il sisma: ricerca, soccorso e messa in sicurezza",
 descrizione="La fase dorata del soccorso: USAR, esercitazioni e la logistica dell'emergenza.",
 tecnologia="Le 72 ore 'dorate' con la ricerca e soccorso urbano (USAR, Urban Search and Rescue) con i cani da ricerca, le squadre di scavo tecnico e le attrezzature di sollevamento; le esercitazioni di protezione civile con i campi base, le aree di triage e le unità cinofile; le valutazioni di agibilità rapida (FAST: scheda di primo livello tipo AeDES) per la classificazione A-B-C-E degli edifici; le opere di messa in sicurezza d'emergenza: puntellamenti, reti paramassi, chiusura delle vie; la logistica: campi accoglienza, cucine da campo, generatori, ponti radio; la gestione delle macerie con la ricerca di dispersi prima del movimento terra; la psicologia dell'emergenza con gli interventi di supporto alla popolazione.",
 applicazioni="Terremoti di ogni scala, crolli di edifici, eventi che lasciano la popolazione senza casa.",
 vantaggi="Sopravvissuti recuperati grazie alla rapidità e alla preparazione, classificazione che libera le strutture non danneggiate, la logistica che sostiene la popolazione nei giorni critici.",
 limiti="Il traffico dei mezzi privati che blocca i soccorsi, la disinformazione che allarma, la stanchezza delle squadre dopo 48 ore, l'incompatibilità dei volontari non coordinati.",
 costi_e_economia="Ordini di grandezza indicativi: squadra USAR attrezzata 200-800 k€; campo accoglienza 50-200 €/posto/giorno; il costo non monetizzabile è la vita dei soccorritori.",
 casi_real_world="L'integrazione delle squadre USAR internazionali nei terremoti italiani; la 'marcia' delle autoparco per liberare le strade di accesso.",
 normative="Linee guida USAR nazionali e standard INSARAG internazionali; il codice della protezione civile per le fasi della risposta; le schede di valutazione rapida del danno (AeDES).",
 note_cantiere="Le prime ore appartengono ai soccorritori: l'impresa edile che entra troppo presto con i mezzi rischia di diventare vittima e di bloccare i soccorsi; si entra quando il settore è dichiarato sicuro."),

dict(categoria="Ricostruzione privata", nome="La ricostruzione privata dopo il sisma: flussi, contributi e iter",
 descrizione="Come si ricostruiscono le case: contributi, ricostruzione agevolata e la filiera dei cantieri post-sisma.",
 tecnologia="Contributi per la ricostruzione: contributo alla ricostruzione privata sulla base dei danni (percentuali di danno da perizia), contributo per l'agibilità temporanea e il consolidamento; la ricostruzione agevolata con pratiche semplificate e sportelli unici; la perizia di danno con le schede AeDES di secondo livello per gli edifici con danno strutturale; il progetto di miglioramento sismico o ricostruzione con i requisiti delle NTC; il sismabonus e le agevolazioni fiscali per la ricostruzione (regole in evoluzione, verifica vigente); i cantieri di ricostruzione privata con le verifiche intermedie e i collaudi; il ruolo dei Centri di Assistenza Tecnica Contabile (CAT-C) per le pratiche degli aventi diritto.",
 applicazioni="Ricostruzione dopo i terremoti del 2009 (Aquila), 2012 (Emilia), 2016 (centro Italia); eventi futuri con il modello consolidato.",
 vantaggi="Flussi consolidati che velocizzano la ricostruzione rispetto al passato, contributi che coprono gran parte del danno, la ricostruzione è l'occasione del miglioramento sismico.",
 limiti="Iter burocratici ancora lunghi per i privati, la discrepanza tra i contributi e i costi reali di ricostruzione, i ritardi dei pagamenti bloccano le famiglie, il rischio di speculazione edilizia da controllare.",
 costi_e_economia="Ordini di grandezza indicativi: contributi per la ricostruzione secondo le delibere del commissario (da verificare per l'evento specifico); la ricostruzione privata di un comune terremotato vale decine di milioni di euro.",
 casi_real_world="La ricostruzione del centro Italia con i commissari straordinari e i flussi consolidati; l'esperienza aquilana come primo grande banco di prova.",
 normative="D.Lgs 1/2018; le ordinanze del Commissario straordinario per la ricostruzione (decreto istitutivo vigente per l'evento); le NTC 2018 per la ricostruzione con miglioramento sismico; la normativa fiscale del sismabonus (verifica vigente).",
 note_cantiere="La ricostruzione privata è una filiera di pratiche: il tecnico abilitato all'accesso ai contributi guida il cliente attraverso CAT-C, perizie e contributi; chi salta i passi perde soldi e tempo."),

dict(categoria="Ricostruzione pubblica", nome="La ricostruzione pubblica: scuole, ospedali e opere strategiche",
 descrizione="Il cantiere della ripresa pubblica: come si ricostruiscono le opere essenziali dopo il sisma.",
 tecnologia="La ricostruzione pubblica con i commissari straordinari e le ordinanze che semplificano gli appalti (procedure speciali d'urgenza); la priorità alle scuole (mappatura dei danni, container scolastici, ricostruzione con edilizia temporanea); gli ospedali: verifica di agibilità, evacuazione dei reparti, i moduli sanitari temporanei, la ricostruzione con standard ospedalieri moderni; le strutture strategiche: ponti, viadotti, strade con le verifiche di emergenza e i ponti provvisori (Bailey, Mabey); la pianificazione triennale della ricostruzione con i cantieri diffusi sul territorio; il monitoraggio dei cantieri con i centri di coordinamento; la conservazione dei beni culturali danneggiati (cupole, campanili, chiese) con i cantieri di restauro d'emergenza.",
 applicazioni="Ricostruzione pubblica dei territori colpiti: scuole, ospedali, municipi, ponti, beni culturali.",
 vantaggi="Priorità definite che mettono in sicurezza i servizi essenziali, procedure accelerate che riducono i tempi della ricostruzione pubblica, la ricostruzione come occasione di miglioramento delle opere.",
 limiti="La competizione tra le opere per le risorse, i cantieri pubblici post-sisma hanno costi maggiorati (+15-30%), la ricostruzione dei beni culturali è lentissima per la delicatezza dei beni.",
 costi_e_economia="Ordini di grandezza indicativi: scuola temporanea 1.000-2.500 €/m²; ospedale temporaneo 2.000-4.000 €/m²; il premio di urgenza sui lavori pubblici +15-30%.",
 casi_real_world="Le scuole temporanee dei comuni terremotati; i ponti provvisori di collegamento dei paesi isolati.",
 normative="Ordinanze del commissario straordinario con le procedure speciali; D.Lgs 36/2023 per gli appalti (con le semplificazioni d'urgenza); D.Lgs 42/2004 per i beni culturali danneggiati.",
 note_cantiere="La ricostruzione pubblica post-sisma è un esercito di cantieri: il coordinamento dei lavori, delle viabilità e delle risorse umane decide il successo più delle singole opere."),

dict(categoria="Messa in sicurezza", nome="Messa in sicurezza e prevenzione del costruito sismico",
 descrizione="Prevenire invece che curare: il piano nazionale di messa in sicurezza e le schede di valutazione.",
 tecnologia="Classificazione sismica nazionale dei comuni (zone 1-4) e i periodi di ritorno di riferimento; il piano nazionale di prevenzione sismica (PNPS) e la mappatura del rischio; le schede di valutazione del danno: FAST (primo livello) per la valutazione rapida, AeDES (secondo livello) per la perizia, e le schede per i beni culturali (chiese e palazzi storici); la valutazione della vulnerabilità con le metodologie a scala territoriale; i piani di emergenza dei comuni sismici con le mappe dei rischi; le verifiche di agibilità con i livelli: agibile, inagibile parzialmente, inagibile; il ruolo del tecnico comunale nella stima dei danni; le tecniche di intervento rapido (puntellamenti, tiranti, reti).",
 applicazioni="Prevenzione sismica dei centri storici, gestione dell'emergenza post-sisma, pianificazione della messa in sicurezza degli edifici pubblici.",
 vantaggi="La prevenzione che riduce i danni futuri con costi contenuti, la classificazione rapida che orienta i soccorsi, la conoscenza del rischio che guida le politiche di piano.",
 limiti="La mappatura del rischio è in corso da decenni, le schede richiedono formazione specifica dei tecnici, i costi della prevenzione sono visibili mentre i benefici sono invisibili.",
 costi_e_economia="Ordini di grandezza indicativi: censimenti territoriali dei rischi da progetto; il rapporto costi-benefici della prevenzione è 1:4-1:7 secondo gli studi internazionali.",
 casi_real_world="La scheda AeDES come standard nazionale di valutazione del danno; il censimento dei centri storici sismici con le mappe del rischio.",
 normative="NTC 2018 e la classificazione sismica nazionale (zone sismiche dei comuni); linee guida con le schede di valutazione rapida del danno (AeDES e aggiornamenti); PNPS e la normativa sulla prevenzione del rischio sismico.",
 note_cantiere="La valutazione di agibilità si fa con la scheda giusta al primo livello: il FAST in strada, l'AeDES in sede; saltare i livelli genera revisioni e perdite di tempo."),

dict(categoria="Temporaneo", nome="Edilizia temporanea di emergenza: SAE, map e soluzioni rapide",
 descrizione="Le case di emergenza: moduli abitativi, container e i villaggi della ricostruzione.",
 tecnologia="Soluzioni Abitative di Emergenza (SAE): moduli abitativi in legno, acciaio o cls alleggerito con i servizi di base (8-40 m²), installabili in giorni; i moduli container (map) con le predisposizioni impiantistiche; i villaggi temporanei con le infrastrutture (strade, reti, servizi igienici, aree comuni); i tempi di installazione (SAE entro 30-60 giorni dall'evento); la gestione dei villaggi con gli enti locali e le associazioni; la dismissione e il riuso dei moduli alla ricostruzione; le verifiche sanitarie e abitative dei moduli con la certificazione dei materiali; la pianificazione dei siti con le distanze dai centri, i servizi e la sicurezza.",
 applicazioni="Terremoti e alluvioni con popolazione sfollata, ricostruzione lenta dei centri colpiti, emergenze abitative di ogni tipo.",
 vantaggi="Risposta rapida con la casa pronta in giorni, standard abitativi garantiti con servizi, riuso dei moduli in altre emergenze o come edilizia temporanea scolastica.",
 limiti="L'impatto paesaggistico e sociale dei villaggi, i costi di gestione continuativi, la stigmatizzazione dei residenti nei 'campi', la manutenzione dei moduli nel tempo.",
 costi_e_economia="Ordini di grandezza indicativi: SAE 400-1.200 €/m²; villaggio completo con infrastrutture 15.000-40.000 €/posto; gestione 2.000-6.000 €/posto/anno.",
 casi_real_world="I villaggi SAE del centro Italia con la gestione pluriennale; i moduli riusati come aule temporanee dopo la ricostruzione.",
 normative="D.Lgs 1/2018 per la gestione della fase di assistenza alla popolazione; le ordinanze commissariali per l'installazione delle SAE; requisiti igienico-sanitari dei moduli abitativi.",
 note_cantiere="La SAE si installa su platee predisposte con i servizi: la fretta non giustifica i siti senza fognatura e acqua; il villaggio senza servizi diventa un problema invece di una soluzione."),

dict(categoria="Strutture provvisorie", nome="Ponti e strutture provvisorie d'emergenza",
 descrizione="Ricostruire i collegamenti in giorni: ponti Bailey, passerelle e opere di emergenza.",
 tecnologia="Ponti provvisori metallici tipo Bailey (modulari in acciaio, montabili in giorni, luci 10-60 m, portate 20-40 t) e le evoluzioni moderne (Mabey, Acrow); passerelle pedonali e ciclabili d'emergenza in legno o acciaio; piazzali e cordoli di cls gettati d'emergenza; la posa con le gru o il lancio a sbalzo per i ponti modulari; le fondazioni provvisorie su pali infissi o su piastre; la verifica di carico con i collaudi rapidi; i tempi di installazione (48-96 ore per un ponte Bailey); la convivenza con la ricostruzione definitiva; la manutenzione dei ponti provvisori per anni di esercizio.",
 applicazioni="Strade e ponti crollati dal sisma o dalle alluvioni, collegamenti di paesi isolati, accessi ai cantieri di ricostruzione.",
 vantaggi="Ricollocamento dei collegamenti in giorni con standard industriali, riutilizzabili in altre emergenze, il traffico riparte mentre si progetta la ricostruzione definitiva.",
 limiti="Portate e luci limitate rispetto ai ponti definitivi, la durata 'provvisoria' diventa spesso anni con manutenzione crescente, l'impatto estetico nelle aree di pregio.",
 costi_e_economia="Ordini di grandezza indicativi: ponte Bailey installato 1.500-4.000 €/m lineare; passerella pedonale 500-1.500 €/m; il canone di noleggio rende conveniente il riuso per più eventi.",
 casi_real_world="I ponti provvisori del centro Italia che hanno tenuto per anni; i ponti Bailey storici riutilizzati in ogni emergenza.",
 normative="Verifiche di collaudo rapido secondo le procedure d'emergenza; normativa sulle strutture provvisionali nei cantieri (D.Lgs 81/2008); le specifiche dei produttori di ponti modulari.",
 note_cantiere="Il ponte provvisorio si collauda a carico prima dell'apertura: la fretta di riaprire non giustifica i carichi non verificati; i campi base dei costruttori stanno spesso sui ponti provvisori."),

dict(categoria="Filiera", nome="La filiera della ricostruzione: cantieri diffusi, personale e logistica",
 descrizione="L'industria della ricostruzione: come migliaia di cantieri piccoli diventano un sistema produttivo.",
 tecnologia="La ricostruzione come mercato: migliaia di cantieri privati simultanei che richiedono materiali, tecnici e manodopera coordinati; i poli di produzione: pannelli prefabbricati, laterizi, cls nelle aree colpite; il personale: maestranze locali formate e integrate da squadre esterne; la logistica: depositi di materiali, strade di cantiere, gestione dei flussi; la sicurezza nei cantieri di ricostruzione diffusi (cantieri domestici, lavori su edifici in quota); il coordinamento con i centri di raccolta dei rifiuti da demolizione; il ruolo delle imprese generali locali e delle catene nazionali; il controllo dei prezzi con le verifiche dell'ufficio speciale.",
 applicazioni="Ricostruzione post-sisma di ogni scala, programmi di riqualificazione diffusa dei centri storici.",
 vantaggi="La ricostruzione come locomotiva economica dei territori colpiti, l'indotto occupazionale che ferma l'emorragia demografica, la diffusione delle competenze tecniche.",
 limiti="L'impennata dei prezzi nei territori colpiti, la scarsità di tecnici e maestranze, la concorrenza sleale e l'abusivismo, la stanchezza dei cantieri dopo anni.",
 costi_e_economia="Ordini di grandezza indicativi: il premio prezzi nelle aree terremotate +10-25%; la ricostruzione di un comune medio vale 100-500 M€ di lavori in 5-10 anni.",
 casi_real_world="Le reti di imprese locali ricostruite dopo il sisma; i prezzi dei materiali monitorati dagli uffici speciali.",
 normative="Le ordinanze commissariali con le verifiche sui prezzi; D.Lgs 36/2023 per gli appalti con le deroghe d'emergenza; normativa sulla sicurezza nei cantieri.",
 note_cantiere="La ricostruzione premia chi è organizzato: le imprese con quadri, scorte e uffici tecnici locali vincono su quelle che improvvisano; la reputazione si costruisce nei cantieri diffusi."),

dict(categoria="Benessere", nome="La ricostruzione come rilancio: rigenerazione urbana, sociale ed economica",
 descrizione="Dopo le macerie: la ricostruzione come opportunità di rinascita dei territori.",
 tecnologia="La ricostruzione integrata con la rigenerazione urbana: nuovi standard di edilizia pubblica, riqualificazione energetica dei ricostruiti, riorganizzazione degli spazi pubblici con la partecipazione dei cittadini; il rilancio economico: incentivi per le imprese che tornano, distretti produttivi ricostruiti, turismo della memoria e della ricostruzione; la cura del tessuto sociale: centri aggregativi, sportelli psicologici, scuole come poli di comunità; le infrastrutture di connessione: banda larga, trasporti, cammini della ricostruzione; la comunicazione della ricostruzione: i cantieri aperti, le mostre, la trasparenza sui tempi e sui costi; il passaggio alla normalità: la dismissione degli uffici speciali e la restituzione alla gestione ordinaria.",
 applicazioni="Riqualificazione dei centri storici colpiti, programmi di rilancio post-emergenza, piani di rinascita dei territori in declino.",
 vantaggi="La ricostruzione come salto di qualità rispetto al pre-evento, il rafforzamento del tessuto sociale, la visibilità che attrae investimenti e visitatori.",
 limiti="Il rischio della 'ricostruzione dimezzata' che non cura la sostanza, i conflitti tra ricostruzione identica e innovazione, la fatica della governance pluriennale.",
 costi_e_economia="Ordini di grandezza indicativi: i programmi integrati di ricostruzione valgono il 20-40% in più dei soli lavori (servizi, infrastrutture, sociale).",
 casi_real_world="I centri storici ricostruiti con nuovi standard energetici e sismici; i percorsi turistici della memoria e della rinascita.",
 normative="La normativa sulla rigenerazione urbana e sui contratti di riqualificazione; le ordinanze commissariali con i programmi integrati; gli strumenti di sviluppo locale e dei borghi.",
 note_cantiere="La ricostruzione più alta è quella che rispetta la memoria e guarda avanti: il centro identico prima e dopo è una ricostruzione mancata, non un successo."),

dict(categoria="Alluvioni", nome="Emergenze idrauliche e alluvioni: risposta, ricostruzione e adattamento",
 descrizione="La risposta alle alluvioni: soccorso, ripristino e la ricostruzione che tiene conto dell'acqua.",
 tecnologia="La risposta all'alluvione: evacuazione delle persone nelle aree isolate, i centri di coordinamento con la protezione civile; la messa in sicurezza delle opere idrauliche (argini danneggiati, briglie ostruite); il ripristino d'emergenza di strade, ponti e reti (acqua, luce, fognature); la pulizia dei centri abitati con i fanghi e i rifiuti speciali (amianto, elettrodomestici); la verifica delle abitazioni allagate: umidità, impianti elettrici, strutture; la ricostruzione con l'adattamento: rialzamento delle quote, opere di laminazione, ripristino con miglioramento; il piano nazionale di adattamento ai cambiamenti climatici; i bandi di ricostruzione post-alluvione con i contributi per le attività produttive.",
 applicazioni="Alluvioni di fiumi e torrenti, esondazioni in pianura, mareggiate costiere con danni diffusi.",
 vantaggi="La risposta strutturata che riduce le vittime e i danni secondari, la ricostruzione con l'adattamento che riduce il rischio futuro, i bandi che sostengono la ripresa produttiva.",
 limiti="La recidività delle alluvioni nello stesso territorio, la ricostruzione 'identica' che ignora l'acqua, i tempi lunghi dei contributi, la fatica delle popolazioni colpite più volte.",
 costi_e_economia="Ordini di grandezza indicativi: i danni da alluvione valgono 0,5-5 miliardi per gli eventi maggiori; il ripristino delle opere idrauliche 10-30% del danno totale.",
 casi_real_world="Le alluvioni dell'Emilia-Romagna con la ricostruzione e l'adattamento delle opere; le mareggiate della costa adriatica con i ripristini ciclici.",
 normative="D.Lgs 1/2018 per la gestione dell'emergenza idraulica; il piano nazionale di adattamento ai cambiamenti climatici e gli strumenti di gestione del rischio alluvioni; le ordinanze per i contributi post-alluvione.",
 note_cantiere="Dopo l'alluvione si ricostruisce con l'acqua in mente: il piano casa rialzato, la centrale termica al piano alto, i servizi elettrici sopra la quota di piena."),

dict(categoria="Prevenzione", nome="La prevenzione strutturale: piani di emergenza aziendali e ruolo delle imprese",
 descrizione="L'impresa come soggetto di prevenzione: piani aziendali, continuità operativa e il ruolo nelle emergenze.",
 tecnologia="Piano di emergenza aziendale (PEA) con l'analisi dei rischi (sismico, idraulico, incendio, chimico), le procedure di evacuazione e il piano di continuità operativa (BCP); i gruppi di emergenza aziendali con la formazione del personale (incaricati, addetti antincendio, primo soccorso); le scorte di emergenza: generatori, acqua, DPI, ponti radio; la mappatura dei punti deboli dell'impresa (fornitori unici, dati, mezzi); le esercitazioni aziendali con la protezione civile; il ruolo dell'impresa edile nella fase di previsione e prevenzione (verifiche degli edifici, consolidamenti); la gestione assicurativa del rischio catastrofale per le imprese.",
 applicazioni="Imprese edili, stabilimenti produttivi, cantieri in zona a rischio, organizzazioni di ogni dimensione.",
 vantaggi="La continuità operativa dopo l'evento, i dipendenti protetti con le procedure, l'impresa che supporta la protezione civile con mezzi e competenze.",
 limiti="I piani che restano nei cassetti senza esercitazioni, i costi di prevenzione visti come improduttivi, la complessità delle piccole imprese senza uffici dedicati.",
 costi_e_economia="Ordini di grandezza indicativi: PEA e BCP 2.000-20.000 € secondo dimensione; generatori di emergenza 10-100 k€; le esercitazioni 500-5.000 €/anno.",
 casi_real_world="Le imprese con BCP che hanno ripreso in giorni dopo il sisma; i cantieri che hanno prestato mezzi e personale alla protezione civile.",
 normative="D.Lgs 81/2008 per i piani di emergenza aziendali; D.Lgs 1/2018 per il coordinamento con la protezione civile; la normativa assicurativa e fiscale per la continuità operativa.",
 note_cantiere="Il piano senza esercitazione non esiste: la carta non spegne incendi né evacua cantieri; un giorno all'anno di esercitazione vale più di dieci faldoni."),
]

write_pack("EMERGENZE_E_RICOSTRUZIONE_PACK",
 "Emergenze e ricostruzione post-sisma", "FACOLTA_GESTIONE_SISTEMA", "L2-L3",
 "Protezione civile, prime 72 ore, ricostruzione privata e pubblica, messa in sicurezza, edilizia temporanea, ponti provvisori, filiera, rilancio, alluvioni, prevenzione aziendale.",
 """# EMERGENZE_E_RICOSTRUZIONE_PACK

**Emergenze e ricostruzione post-sisma**

Sistema di protezione civile e Codice (D.Lgs 1/2018), le prime 72 ore e il soccorso USAR, ricostruzione privata con contributi e flussi, ricostruzione pubblica di scuole e ospedali, messa in sicurezza e schede AeDES, edilizia temporanea SAE, ponti e strutture provvisorie, la filiera della ricostruzione, la rigenerazione dei territori, emergenze idrauliche e adattamento, prevenzione aziendale e continuità operativa.

Schede: 11 (formato JSONL, un oggetto per riga).
""", emergenze)

print("OK giro N")
