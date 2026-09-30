# -*- coding: utf-8 -*-
"""Due corpus: metodo di cantiere avanzato (Edilizia) + cultura del pensiero (Fondamenti)."""
import json, os

# ============ METODO DI CANTIERE AVANZATO (8) ============
M = []

M.append(("lean_construction",
"LEAN CONSTRUCTION: TAKT TIME, LAST PLANNER E FLUSSO DI VALORE",
"""La lean production applicata al cantiere elimina gli sprechi:

1. SPRECHI (muda): sovrapproduzione (getti prematuri), attese (approvvigionamenti), trasporti (doppie movimentazioni), sovralavorazione (finiture non richieste), scorte (materiali fermi), difetti (rifacimenti), movimenti inutili degli operai; il lean cerca il flusso continuo di valore dal progetto alla consegna.

2. TAKT TIME: ritmo di produzione = tempo disponibile / numero di unità da produrre (es. un bagno ogni 2 giorni); il cantiere viene organizzato in fasi a ritmo costante con 'takt plan' che sincronizza squadre e forniture.

3. LAST PLANNER SYSTEM (LPS): i capisquadra (last planners) pianificano settimanalmente gli impegni (make ready, weekly work plan) e alimentano il sistema con i 'piani pull' retro-dati dalla fine; la percentuale di impegni rispettati (PPC - Percent Plan Complete) misura la qualità della pianificazione.

4. PULL PLANNING E BIM: la pianificazione si costruisce dagli obiettivi (consegna) a ritroso; il BIM 4D supporta la simulazione del flusso.

5. RISULTATI: riduzione tempi (10-30%), riduzione difetti, maggiore affidabilità delle consegne, clima collaborativo."""))
M.append(("procurement_logistica",
"PROCUREMENT, APPROVVIGIONAMENTI E LOGISTICA DI CANTIERE",
"""L'approvvigionamento efficiente e' un vantaggio competitivo:

1. PROCUREMENT: processo di acquisto dei materiali e servizi (requisiti, gara/selezione fornitori, contratto, gestione ordini, ricevimento, pagamento); per i grandi progetti procurement strategico con categorie (categorie A critiche, B leverage, C routine).

2. LOGISTICA DI CANTIERE: lay-out (aree di stoccaggio, percorsi, gru, recinzioni), just-in-time delivery (consegne programmate in sincrono con il consumo per ridurre scorte e spazi), gestione dei materiali (magazzino digitale, codici a barre/RFID), tracciabilita' (DPP - Digital Product Passport).

3. SCHEDA TECNICA DI APPALTO (ITA): per materiali complessi (facciate, impianti) la scheda tecnica vincola le prestazioni richieste; collaudi di primo impianto, campionature, mock-up.

4. RISCHI: ritardi forniture (cause esterne: lockdown, guerra, dazi), qualita' variabile, monopolio fornitore; mitigazioni: doppie fonti, scorte di sicurezza per i lunghi lead time, clausole penali e bonus, ispezioni in produzione.

5. CONTRATTI DI APPALTO FORNITURA: EPC, fornitura chiavi in mano, contratti quadro (frame agreements) per multi-progetto; Incoterms per le consegne internazionali (EXW, FOB, DDP)."""))
M.append(("megaprogetti",
"MEGAPROGETTI E PROGRAM MANAGEMENT",
"""Le grandi opere (infrastrutture, grandi edifici, complessi) richiedono gestione programmativa:

1. DEFINIZIONE: megaprogetto (costo > 1 miliardo, durata > 5 anni, interdisciplinare, stakeholder multipli); esempi: TAV, terzo valico, stadi olimpici, EXPO.

2. ORGANIZZAZIONE: project sponsor (committente), project director, project management office (PMO), work package managers; matrice organizzativa (forte/mattoncino) con controllo tecnico, economico, temporale.

3. PROGRAM MANAGEMENT: coordinamento di piu' progetti correlati con benefici sinergici; gestione delle interfacce, delle risorse condivise, del rischio complessivo; direttive PRINCE2, PMBOK, ISO 21500.

4. CONTROLLI: earned value management (EVM - EV, PV, AC, SPI, CPI), milestone tracking, gestione configurazione (change control board), risk register, contingency management.

5. CRITICITA' DEI MEGAPROGETTI (Flyvbjerg): sovrastima benefici, sottostima costi (optimism bias), complessita' delle interfacce, gestione politica; rimedi: reference class forecasting, allocazione dei rischi, fasi di fattibilita' indipendenti."""))
M.append(("claim_dispute",
"CLAIM, CONTENZIOSI E RISOLUZIONE ALTERNATIVA DELLE DISPUTE",
"""I conflitti di cantiere si gestiscono con metodo prima che con il giudice:

1. CLAIM: richiesta di risarcimento/variazione da parte di un contraente per cause non imputabili (ritardi del committente, varianti, condizioni meteorologiche eccezionali, scioperi, inflation); struttura del claim: fatto, causa, conseguenza economica, giustificativo contrattuale.

2. DOCUMENTAZIONE: lettera di notifica tempestiva (entro i termini contrattuali, tipicamente 14-28 giorni dall'evento), registrazione dei fatti (diari di cantiere, foto, verbali), quantificazione (computo analitico dei costi aggiuntivi), difesa delle riserve.

3. ESTENSIONE DI TEMPO (EOT): valutazione dell'impatto dei ritardi sul completamento (metodi: windows analysis, time impact analysis, as-planned vs as-built); liquidazione dei costi di prosecuzione (site overheads).

4. ALTERNATIVE DISPUTE RESOLUTION (ADR): negoziazione diretta, mediazione, conciliazione (Ente Nazionale per la Conciliazione dei Conflitti in Edilizia), arbitrato (collegio arbitrale, Camera Arbitrale di Milano), dispute board (DB - comitato permanente di tre membri che decide in corso d'opera); vantaggi: velocità, riservatezza, tecnicalita'.

5. CAUSE GIUDIZIARIE: arbitrato ex art. 806 c.p.c. o giudizio ordinario; in edilizia pubblica, giustizia amministrativa per gli atti."""))
M.append(("qualita_collaudo",
"GESTIONE QUALITA', PROVE E COLLAUDO AVANZATO",
"""La qualità in cantiere e' un sistema documentato:

1. PIANO DI QUALITA' (PQ): documento che definisce responsabilità, procedure, ispezioni, prove, registrazioni; in italiano spesso 'piano di gestione della qualita' (ISO 10005 per i piani di qualità, ISO 9001 per i sistemi).

2. PUNTI DI ISPEZIONE (ITP - Inspection and Test Plan): elenco delle verifiche per ogni lavorazione (ricevimento materiali, posa, prove intermedie, collaudo) con criteri di accettazione, responsabili, documentazione; hold points (fermi obbligatori) e witness points.

3. PROVE NON DISTRUTTIVE: ultrasuoni (cercafessure, spessori), radiografie (giunti), magnetoscopia, liquidi penetranti, termografia, risonanza (impulse response), estrazione carote, sclero, rebound hammer; prove distruttive: carote, trazioni su campioni.

4. COLLUDO AVANZATO: prove di carico (solai, ponti), prove di tenuta (coperture, facciate con test a spruzzo), taratura strumentale, verifica geometrica (laser scanner), collaudi funzionali (impianti).

5. NON CONFORMITA': gestione delle deviazioni (NCR - Non Conformity Report), analisi delle cause, azioni correttive, verifica di chiusura; il ciclo PDCA (plan-do-check-act) e' la spina dorsale."""))
M.append(("sicurezza_cantiere_avanzata",
"SICUREZZA DI CANTIERE AVANZATA: DVR TECNICO E RISCHI GRAVI",
"""La sicurezza si gestisce con strumenti tecnici oltre che organizzativi:

1. DVR TECNICO E ANALISI RISCHI: per i cantieri complessi, il DVR analizza i rischi specifici (ponteggi, scavi, ponteggi sospesi, lavori in quota, inquinamento atmosferico in galleria, LAVORI SUBACQUEI, confinati); metodi: HAZID, risk matrix, bow-tie.

2. RISCHI GRAVI: caduta dall'alto (misure collettive prioritarie: ponteggi, piattaforme, parapetti; DPI anticaduta come integrazione), sepolture in scavi (banchinamento, scavo a scala, sorveglianza geotecnica), folgorazione (distanze da linee elettriche, messa a terra), incendio (estintori, vie di fuga, autorizzazioni), sostanze pericolose (fibra amianto, quarzo cristallino, formaldeide - procedure, DPI, monitoraggio ambientale), lavori in quota e su coperture (linee vita, ancoraggi certificati EN 795).

3. COORDINAMENTO TECNICO: elaborati di coordinamento (PSC), piani di montaggio/smontaggio ponteggi, piani di sicurezza scavi, procedure di emergenza specifiche; il CSP esegue l'analisi preliminare (fase progettazione), il CSE coordina in esecuzione.

4. TECNOLOGIA: sensori di inclinazione ponteggi, droni per ispezioni, RFID per tracciabilita' DPI e formazione, realta' virtuale per formazione rischi.

5. CULTURA: indicatori di performance (indice di frequenza, gravita'), premi per comportamenti sicuri, stop work authority (diritto/dovere di fermare i lavori pericolo)."""))
M.append(("manutenzione_patrimonio",
"MANUTENZIONE DEL PATRIMONIO: PIANI, CONTRATTI E COSTO DEL CICLO",
"""La manutenzione programmata preserva il valore dell'immobile:

1. TIPOLOGIE: manutenzione ordinaria (pulizia, piccoli ritocchi, es. 0,5-1% del valore/anno), straordinaria (rifacimenti parziali, impianti), straordinaria straordinaria (struttura); preventiva (programmata), predittiva (sui monitoraggi), correttiva (a guasto).

2. PIANO DI MANUTENZIONE: inventario delle componenti (edilizia, impianti, facciate, coperture), scheda di manutenzione per ciascuna (frequenza, operazioni, responsabili, costi), calendario pluriennale; il costo del ciclo di vita (LCC - Life Cycle Cost) confronta le alternative di progetto.

3. CONTRATTI DI MANUTENZIONE: global service (appalto integrato di manutenzione con SLA - Service Level Agreement), contratti di appalto di manutenzione (art. 1670 c.c. - conguagli annuali), contratti di servizio energetico (vedi EPC).

4. DIAGNOSTICA: ispezioni periodiche (facciate ogni 2-3 anni, coperture annuali), monitoraggio strutturale (sensori, dati), energy audit per la parte energetica; il fascicolo del fabbricato (art. 93 DPR 380/2001) documenta tutto.

5. GESTIONE CONDOMINIALE: il regolamento condominiale, l'amministratore, la delibera di manutenzione straordinaria; risparmio energetico nelle parti comuni (detrazioni incentivate)."""))
M.append(("esco_epc",
"ENERGY PERFORMANCE CONTRACTING, ESCO E CONTRATTI ENERGETICI",
"""Il contratto di rendimento energetico trasferisce il rischio all'ESCo:

1. MODELLO EPC (Energy Performance Contracting): l'Energy Service Company (ESCo) finanzia ed esegue gli interventi di efficienza energetica e viene pagata con i risparmi ottenuti (shared savings o guaranteed savings); il rischio di performance e' dell'ESCo (garanzia di risparmio), il cliente paga dal cash-flow generato.

2. STRUTTURA: audit energetico di baseline, progetto finanziario (leasing, project financing), misurazione e verifica dei risparmi (IPMVP - International Performance Measurement and Verification Protocol), durata 5-15 anni, trasferimento finale dell'impianto.

3. ESCO IN ITALIA: qualificazione (UNI CEI 11339), registrazione (GSE), ricaduta su edilizia pubblica (art. 11 D.Lgs 115/2008 obbligo per PA), riqualificazione energetica di edifici pubblici con contratti EPC (PAC - Piattaforma Accordi per la Contrattualizzazione? no, piattaforma GSE), bandi PNRR.

4. VARIANTI: chauffage (servizio di fornitura di calore a canone), comfort contracting, EPC 'light' per piccoli interventi; contratti di gestione dell'energia (CEM).

5. VANTAGGI: investimento zero per il cliente, certezza dei risparmi, manutenzione integrata, aggiornamento tecnologico; criticita': durata lunga, baseline contestabile, necessita' di M&V rigoroso."""))

# ============ CULTURA DEL PENSIERO (10) ============
P = []

P.append(("filosofia","antica_medievale",
"PENSIERO ANTICO E MEDIEVALE",
"""Le radici della ragione occidentale:

1. PRESOCRATICI (VI-V a.C.): Thales (acqua come principio), Anassimandro (apeiron), Eraclito (panta rei, divenire), Parmenide (essere, logos), Democrito (atomi); domanda sull'arché (principio) e sul physis (natura).

2. SOCRATE (V sec. a.C.): la conoscenza come ricerca attraverso il dialogo (maieutica), l'etica come scienza (il male e' ignoranza), la cura dell'anima; non scrisse nulla (dialoghi di Platone).

3. PLATONE (IV sec. a.C.): teoria delle idee (il mondo sensibile e' copia del mondo intelligibile), il mito della caverna, il filosofo-re nel Politico, l'amore come ascesa al bello (Simposio).

4. ARISTOTELE: logica (sillogismo, principio di non contraddizione), fisica (atto e potenza, cause materiale/formale/efficiente/finale), etica (eudaimonia, virtu' come giusto mezzo), politica (l'uomo e' animale politico); fondatore della scienza empirica.

5. MEDIOEVO: Agostino (fides quaerens intellectum, tempo e memoria nella Confessioni), Tommaso d'Aquino (sintesi fede-razione, le 5 vie, Summa Theologiae), scolastica; traduzione dei classici arabi (Averroè, Avicenna).

6. RINASCIMENTO: umanesimo (Petrarca, Valla), Platone riscoperto (Ficino, Pico della Mirandola), Machiavelli (virtù e fortuna, la politica autonoma), Bruno (infinito), Galileo (matematizzazione della natura)."""))
P.append(("filosofia","moderna",
"FILOSOFIA MODERNA: DALLA RAGIONE ALL'IDEALISMO",
"""La modernita' pone la soggettivita' al centro:

1. RINASCIMENTO E RIVOLUZIONE SCIENTIFICA: Copernico (eliocentrismo), Keplero (leggi), Galileo (metodo sperimentale, il Saggiatore), Newton (sintesi meccanicistica).

2. RATIONALISMO: Cartesio (dubbio metodico, cogito ergo sum, dualismo mente-corpo, geometric method), Spinoza (Deus sive Natura, Etica dimostrata), Leibniz (monadi, migliore dei mondi possibili, calcolo infinitesimale).

3. EMPIRISMO: Locke (tabula rasa, governo basato su consenso), Berkeley (esse est percipi), Hume (impressioni e idee, critica causa-effetto, induzione come abitudine).

4. ILLUMINISMO: Voltaire (tolleranza), Rousseau (contratto sociale, volonté générale, educazione in Emilio), Montesquieu (separazione dei poteri), Kant (critica della ragion pura: sintesi a priori, fenomeni/noumeni; illuminismo come uscita dall'auto-tutela).

5. IDEALISMO TEDESCO: Fichte (Io assoluto), Schelling (natura come organismo), Hegel (dialettica tesi-antitesi-sintesi, spirito assoluto, filosofia del diritto: Stato etico).

6. POSITIVISMO E OTTOCENTO: Comte (leggi dei tre stadi, sociologia), Stuart Mill (utilitarismo), Marx (materialismo storico, lotta di classe, plusvalore), Schopenhauer (volontà e rappresentazione), Nietzsche (volontà di potenza, morte di Dio, superuomo, genealogia della morale)."""))
P.append(("filosofia","contemporanea",
"FILOSOFIA CONTEMPORANEA: DALL'ESISTENZIALISMO ALLA FILOSOFIA ANALITICA",
"""Il Novecento frammenta il pensiero in correnti:

1. ESISTENZIALISMO: Kierkegaard (angoscia, salto di fede, singolo), Heidegger (Essere e tempo, esserci, esser-per-la-morte), Sartre (l'esistenza precede l'essenza, cattiva fede, libertà angosciosa), Camus (assurdo, Sisifo).

2. PRAGMATISMO: Peirce (significato come effetto pratico), James (verità come ciò che funziona), Dewey (educazione e democrazia).

3. FILOSOFIA ANALITICA: Frege (logica del linguaggio), Russell (teoria dei tipi), Wittgenstein (Tractatus: il linguaggio ritrae il mondo; Ricerche: giochi linguistici, significato come uso), Vienna Circle (verificazione), Quine (critica della distinzione analitico/sintetico), Kripke (nominazione e necessità).

4. FENOMENOLOGIA: Husserl (epoché, intenzionalità, Lebenswelt), Gadamer (verità e metodo, fusione di orizzonti), Ricoeur (ermeneutica del sé).

5. FILOSOFIA CRITICA E POLITICA: Frankfurter Schule (Adorno, Horkheimer, dialettica dell'illuminismo, industria culturale), Habermas (azione comunicativa, società civile), Foucault (potere/sapere, biopolitica, discipline), Derrida (decostruzione), Arendt (banalità del male, agire).

6. FILOSOFIA DELLA SCIENZA: Popper (falsificazionismo), Kuhn (paradigmi e rivoluzioni scientifiche), Lakatos (programmi di ricerca), Feyerabend (contro il metodo)."""))
P.append(("logica","logica_retorica",
"LOGICA, ARGOMENTAZIONE E RETORICA",
"""Strumenti del ragionamento rigoroso e della comunicazione persuasiva:

1. LOGICA FORMALE: proposizioni e connettivi (e, o, se-allora, non), tavole di verità, sillogismi aristotelici (Barbara, Celarent), modi e figure; inferenze valide vs solamente probabili (deduzione, induzione, abduzione di Peirce).

2. FALLACIE COMUNI: petizione di principio (argomento circolare), post hoc ergo propter hoc (correlazione vs causa), falso dilemma, ad hominem (attaccare la persona), straw man (caricare la tesi avversaria), appello all'autorità, generalizzazione affrettata (hasty generalization), slippery slope; riconoscerle difende dal ragionamento ingannevole.

3. ARGOMENTAZIONE: Toulmin (dati, warrants, backing, qualificatori), logica dialogica, burden of proof (onere della prova), principio di carità (interpretare il meglio la tesi altrui).

4. RETORICA (Aristotele): ethos (credibilità del parlante), pathos (emozione del pubblico), logos (logica dell'argomento); dispositio (ordine: exordium, narratio, argumentatio, peroratio); elocutio (stile, figure retoriche: metafora, analogia, iperbole).

5. APPLICAZIONE PRATICA: scrivere relazioni tecniche persuasive ma oneste, negoziare varianti di cantiere, presentare offerte, gestire clienti difficili."""))
P.append(("metodo_scientifico","epistemologia",
"METODO SCIENTIFICO ED EPISTEMOLOGIA",
"""Come si produce conoscenza affidabile:

1. FASI DEL METODO: osservazione -> ipotesi -> predizione -> sperimentazione -> analisi dati -> teoria -> riproducibilità (peer review, replicazione); Galileo (esperimento controllato, misurazione), Bacon (induzione, idola), Newton (ipotesi non fingo).

2. INDUZIONE E PROBLEMA DI HUME: dall'osservazione di casi non segue necessariamente la legge; Popper risponde con la falsificabilità: una teoria e' scientifica se e' falsificabile; la verità si avvicina per congetture e confutazioni (verisimilitude).

3. PARADIGMI (Kuhn): scienza normale (risolvere puzzle nel paradigma), anomalie, crisi, rivoluzione scientifica, cambio di paradigma (Copernico, Einstein); la scienza non progredisce solo cumulativamente.

4. PROBABILITA' E STATISTICA: teoria frequente vs bayesiana (probabilità come grado di credenza, aggiornamento con nuove evidenze: teorema di Bayes P(A|B) = P(B|A)·P(A)/P(B)); distribuzioni (normale, binomiale), media, mediana, varianza, deviazione standard, intervalli di confidenza, p-value e limiti.

5. ERRORI COMUNI: confusione tra correlazione e causalità, cherry picking (selezionare i dati favorevoli), survivor bias, base rate neglect, doppio cieco e controlli nelle sperimentazioni.

6. APPLICAZIONE: testare materiali, valutare dati di cantiere, verificare prestazioni energetiche dichiarate, leggere studi tecnici con spirito critico."""))
P.append(("psicologia","bias_negoziazione",
"PSICOLOGIA PRATICA: BIAS COGNITIVI E NEGOZIAZIONE",
"""Comprendere la mente migliora il giudizio e il rapporto con clienti e team:

1. BIAS COGNITIVI (Kahneman, Tversky): ancoraggio (il primo numero influenza la valutazione), conferma (cercare solo prove della propria tesi), disponibilità (giudicare probabile cio' che viene in mente facilmente), perdita aversione (le perdite pesano il doppio delle vincite), effetto alone (un tratto influenza il giudizio globale), overconfidence (sovrastima delle proprie capacita'), framing (la forma influenza la scelta), sunk cost fallacy (persistente per soldi gia' spesi).

2. SISTEMA 1 E SISTEMA 2: pensiero rapido intuitivo vs lento analitico; i bias nascono quando il sistema 1 decide troppo presto; rimedio: pause, check-list, analisi esterna.

3. NEGOZIAZIONE: principi di Fisher e Ury (separare persone dal problema, interessi non posizioni, opzioni multiple, criteri oggettivi), BATNA (migliore alternativa), ZOPA (zona di accordo possibile), negoziazione principled vs hard bargaining; gestione delle emozioni e del tempo.

4. COMUNICAZIONE: ascolto attivo, feedback non violento (osservazione-senso-bisogno-richiesta), assertività (diritti e doveri), gestione conflitti (competizione, collaborazione, compromesso, evitamento, accomodamento - Thomas-Kilmann).

5. LAVORO DI SQUADRA: dinamiche di gruppo (formare-storming-norming-performing), leadership situazionale, motivazione (Maslow, Herzberg: fattori igiene vs motivanti), delega efficace."""))
P.append(("economia","economia_spiegata",
"MICROECONOMIA E MACROECONOMIA ESSENZIALI",
"""L'economia spiegata per il professionista:

1. MICROECONOMIA: domanda e offerta (legge della domanda: prezzo su, quantità giù), elasticità, equilibrio di mercato, surplus del consumatore/produttore; teoria dell'utilità marginale decrescente; costi fissi e variabili, costo marginale, rendimenti di scala, economie di scala (il settore edilizio ha scale moderate); concorrenza perfetta, monopolio, oligopolio, concorrenza monopolistica; esternalità (inquinamento, in questo caso internaizzate con norme) e beni pubblici.

2. MACROECONOMIA: PIL (valore dei beni finali prodotti), PIL pro capite, inflazione (indice ISTAT FOI, IPCA), disoccupazione (tasso, definizione ISTAT), cicli economici (espansione, recessione), politica fiscale (spesa pubblica, tasse, deficit, debito) e monetaria (BCE, tassi, quantitative easing).

3. SISTEMA FINANZIARIO: banche centrali (BCE, Federal Reserve), tassi di interesse (BCE deposit facility, Euribor), spread BTP-Bund, mercati obbligazionari e azionari, rating (Moody's, S&P, Fitch), crisi finanziarie (2008: derivati, Lehman).

4. IL CASO ITALIA: debito pubblico (~140% PIL), disavanzo, primario, spesa per interessi, PNRR come investimento strutturale, imprese familiari (l'80% dell'edilizia), produttivita' stagnante, dualismo Nord-Sud.

5. APPLICAZIONE: capire il ciclo delle costruzioni (ordini, prezzi materiali, tassi mutui), valutare investimenti immobiliari, leggere il bilancio di un'impresa."""))
P.append(("cultura","scrittura_professionale",
"SCRIVERE BENE: TECNICA E STILE DELLA PAROLA PROFESSIONALE",
"""La scrittura chiara e' una competenza professionale:

1. PRINCIPI: chiarezza (una idea per frase), concisione (togliere il superfluo), coerenza (coesione logica tra parti), correttezza (grammatica, lessico tecnico appropriato); il lettore non ha tempo: la piramide invertita (dati principali prima, dettagli dopo).

2. STRUTTURA DEL TESTO TECNICO: titolo informativo, sommario/abstract, introduzione (contesto-obiettivo), corpo (metodo-risultati), conclusioni (sintesi-raccomandazioni), allegati; paragrafi con prima frase guida (topic sentence).

3. STILE: preferire verbi attivi e concreti, evitare gergo non necessario, usare elenchi puntati per enumerazioni, tabelle per dati, grassetti per concetti chiave; numeri con unita' di misura (SI), formule spiegate; date e quote complete.

4. ERRORI COMUNI: frasi troppo lunghe, burocratese ('si evidenzia la necessità di' -> 'serve'), ambiguita' ('essi' 'suddetti'), eccesso di passivazioni ('è stato effettuato un controllo' -> 'abbiamo controllato'), maiuscole improprie.

5. STRUMENTI: modello di documento (template) per tipologia (relazione, verbale, computo), glossario aziendale, revisione a due livelli (tecnica + editoriale); AI come assistente di prima bozza da verificare sempre."""))
P.append(("cultura","italiano_grammatica",
"GRANMATICA E LESSICO DELL'ITALIANO TECNICO",
"""Le basi della lingua per non sbagliare mai:

1. MORFOLOGIA: generi e numeri (il computo, le analisi), preposizioni articolate (al, dal, nel), pronomi (chiaro il referente), coniugazioni (tempi e modi: indicativo per fatti, condizionale per ipotesi, congiuntivo per dubbio), concordanza (participio con 'avere' + pronome).

2. SINTASSI: periodo vs frase breve, subordinate (causali, condizionali, finali, temporali), implicita con gerundio ('eseguendo i calcoli, si ottiene'), attenzione alle frasi incise.

3. ORTOGRAFIA E PUNTEGGIATURA: accenti (è, perché, qualità), apostrofo (un'altra), trattino per i composti, virgole (elencazioni, incisi), punto e virgola (periodi complessi), due punti prima di elenchi, virgolette per citazioni.

4. LESSICO TECNICO EDILE: distinguere i termini normativi (portata, resistenza, trasmittanza) dai termini commerciali (acconto, ribasso); il falso amico tecnico (es. 'solai' non 'solai'); i prestiti linguistici (capitolato, computo, pratica) e i calchi (rendere 'delivery' -> 'consegna').

5. REGISTRI: formale (lettere al comune, contratti), tecnico (relazioni, computi), colloquiale (email interne); coerenza di registro nel documento; le abbreviazioni tecniche (NTC, SLU, DL, CILA) spiegate alla prima occorrenza."""))

# ============ writers ============
def write(path, recs, source, attribution):
    meta = {"source": source, "license": "Sintesi didattica originale Kimi (pubblico dominio)",
            "commercial_ok": True, "attribution": attribution, "url": ""}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f"scritti {len(recs)} -> {os.path.abspath(path)}")

out_m = []
for i, (tema, titolo, testo) in enumerate(M, 1):
    rec = {"id": f"MET-{i:02d}", "categoria": "metodo_cantiere", "tema": tema, "title": titolo, "text": testo.strip(),
           "source": "metodo_cantiere_kimi", "license": "Sintesi didattica originale Kimi (pubblico dominio)",
           "commercial_ok": True, "attribution": "Corpus metodo di cantiere avanzato a cura di Kimi", "url": ""}
    out_m.append(rec)
write(os.path.join('Edilizia_Pack', 'parsed', 'metodo_cantiere.jsonl'), out_m, "x", "x")

out_p = []
for i, (cat, tema, titolo, testo) in enumerate(P, 1):
    rec = {"id": f"PEN-{i:03d}", "categoria": cat, "tema": tema, "title": titolo, "text": testo.strip(),
           "source": "cultura_pensiero_kimi", "license": "Sintesi didattica originale Kimi (pubblico dominio)",
           "commercial_ok": True, "attribution": "Corpus cultura del pensiero a cura di Kimi", "url": ""}
    out_p.append(rec)
write(os.path.join('Fondamenti_Pack', 'parsed', 'cultura_pensiero.jsonl'), out_p, "x", "x")
