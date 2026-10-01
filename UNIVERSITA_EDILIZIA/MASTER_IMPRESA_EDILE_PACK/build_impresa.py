# -*- coding: utf-8 -*-
"""MASTER_IMPRESA_EDILE_PACK: gestione d'impresa per costruttori e imprenditori edili."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Struttura", "L'impresa edile: forme giuridiche e scelta consapevole",
 "La forma giuridica decide tasse, responsabilità e accesso ai lavori: ditta individuale, società a responsabilità limitata (Srl), srl semplificata, società tra professionisti, cooperativa edile; la scelta corretta dipende da fatturato, rischio, numero di soci, accesso a gare (requisiti di fatturato).",
 "Criteri: responsabilità patrimoniale (la Srl isola il patrimonio personale), costi di gestione (commercialista più oneroso per le società), requisiti per la qualificazione SOA (fatturato medio ponderato), possibilità di trasformazione nel tempo (ditta → Srl quando il rischio cresce).",
 "Avvio di impresa, crescita, ingresso in gare pubbliche, ingresso di soci.",
 "La forma giusta protegge l'imprenditore e sblocca commesse: la Srl qualificata SOA accede a lavori dove la ditta individuale non può entrare.",
 "La forma 'di moda' senza analisi costa: una Srl con 80.000 € di fatturato paga più costi fissi di quanto guadagna in protezione.",
 "Costo costituzione Srl: 2.500-6.000 €; gestione contabile annua: 1.500-4.000 € in più della ditta individuale; ditta individuale: quasi zero.",
 "Impresa di ristrutturazioni passata da ditta individuale a Srl dopo un danno da infiltrazione: la società ha isolato il patrimonio familiare da un risarcimento da 180.000 €.",
 "Codice civile artt. 2110 e ss. (imprenditore); legge 1423/1956 (forme societarie); registro imprese.",
 "La forma giuridica si rivede a ogni scalino di fatturato: non è un matrimonio, è un abito da cambiare quando cresci."),
s("Organizzazione", "L'organizzazione aziendale: ruoli, organigramma, deleghe",
 "L'impresa edile che cresce deve passare dal 'tutto dal titolare' a una struttura con funzioni: produzione (cantieri), acquisti, amministrazione, sicurezza, commerciale; ogni ruolo ha compiti, autorità e responsabilità scritte.",
 "Strumenti: organigramma semplice (anche 5 scatole), mansionari per ruolo, procedure scritte (ordine acquisto > conferma > ricevimento > fattura), riunione settimanale di produzione con cantieri, tabellone dei cantieri attivi con stato avanzamento e margine.",
 "Imprese da 5 a 50 dipendenti: il passaggio dove nascono o muoiono la maggior parte delle imprese edili.",
 "Il titolare smette di spegnere incendi e inizia a dirigere: la delega con controllo libera tempo per il commerciale, che è l'unica funzione che porta soldi dentro.",
 "Le deleghe senza controllo producono furti, errori e dipendenti 'stato nell'ombra'; il controllo di gestione mensile è il contrappeso.",
 "Costo zero strumentale: carta, Excel, disciplina; un gestionale leggero: 50-150 €/mese.",
 "Impresa di 12 persone con tabellone cantieri e riunione settimanale di 45 minuti: i ritardi sui cantieri scesi da 'sempre' a 1 in un anno, e il titolare ha riaperto il commerciale.",
 "Nessuna norma cogente; buona pratica di gestione.",
 "Regola: chi non ha scritto il proprio organigramma non ha un'azienda, ha un gruppo di persone che spera."),
s("Acquisizione", "L'acquisizione delle commesse: ricerca, offerta, gare private",
 "Trovare lavoro è la prima funzione dell'impresa: ricerca commesse su portali (bandi, subentri, privati), rete di collaboratori (architetti, studi, immobiliaristi), presenza digitale; per ogni commessa: analisi fattibilità economica PRIMA di offrire.",
 "Metodo: filtro commessa (chi paga? progetto pronto? margine atteso?), sopralluogo con lista di controllo, richiesta documenti (tavole, relazioni, capitolato), computo delle proprie voci con listino interno aggiornato, offerta scritta con validità, condizioni di pagamento (acconto, SAL a stati avanzamento, ritenute).",
 "Imprese artigiane e medie che vogliono smettere di lavorare 'al ribasso di chi non sa contare'.",
 "L'offerta con margine dichiarato evita il lavorare gratis: 'vinto il lavoro' e 'perso i soldi' sono la stessa frase se il prezzo è sbagliato.",
 "La paura di perdere la commessa spinge a prezzi senza margine: il lavoro peggiore è quello che perdi facendo.",
 "Costo acquisizione: tempo del titolare (il costo vero); offerta tecnica di una gara privata media: 1-3 giorni/uomo.",
 "Impresa che ha introdotto la regola 'nessuna offerta sotto il 18% di margine lordo': ha perso 6 commesse su 10 e ha raddoppiato l'utile netto in 18 mesi, con cantieri dimezzati.",
 "Codice appalti per la parte pubblica (in coda al corso appalti); per il privato: codice civile (appalto).",
 "Frase da inculcare al LLM: l'impresa che offre sempre sotto costo sta trasferendo il proprio patrimonio ai clienti."),
s("Preventivo", "Il preventivo edile: costi, margine, prezzo",
 "Il preventivo trasforma il progetto in un numero: costi diretti (materiali, manodopera, mezzi, subappalti), costi indiretti (ufficio, sicurezza, generali 8-15%), rischi (5-10%), margine netto target (8-15% sano); il prezzo = somma + IVA.",
 "Metodo: misurare le quantità dal computo o dal sopralluogo, applicare i propri listini (non quelli 'sentiti'), aggiornare i prezzi dei materiali a giornata, prevedere voci di rischio (sconnessioni, smaltimenti, imprevisti nel privato), verifica finale 'il numero mi sembra ragionevole?' contro analoghi passati.",
 "Ogni offerta: ristrutturazioni, manutenzioni, nuove costruzioni, subentri.",
 "Il preventivo giusto rende il cantiere sereno: chi ha margine può fare il lavoro bene e onorare le garanzie.",
 "La sottostima di voce singola (es. smaltimento calcinacci a 30 €/m³ invece di 90) puze annullare il margine di un'intera commessa.",
 "Tempo: preventivo semplice 2-4 ore, commessa completa 1-3 giorni; software di computo: vedi corsi dedicati.",
 "Preventivo di un bagno senza voce 'ripristino impianti a sorpresa': il cantiere ha trovato tubi marci dietro le piastrelle: 3.500 € non preventivati, margine azzerato.",
 "Nessuna norma sul prezzo; disciplina: listini interni aggiornati almeno trimestralmente.",
 "Controllo qualità del preventivo: qualcuno che NON l'ha scritto lo rilegge col metro e le voci mancanti più comuni (umidità, smaltimento, trasporti, IVA su alcune voci)."),
s("Produzione", "La produzione: pianificazione e gestione del cantiere come impresa",
 "Il cantiere è una fabbrica temporanea: va pianificato come produzione (sequenze, risorse, consegne materiali), non amministrato come successione di emergenze; il capocantiere è il primo manager dell'impresa.",
 "Strumenti: cronoprogramma semplice (anche Excel) con le 10-15 attività principali e le loro dipendenze, piano consegne materiali (just-in-time per evitare furti e doppi trasporti), cantiere organizzato (deposito, segnaletica, area taglio), diario di cantiere quotidiano (meteo, persone, lavori, note).",
 "Cantieri di ristrutturazione e nuova costruzione, grandi manutenzioni.",
 "Il cantiere pianificato costa meno: meno giorni uomo persi in attesa materiali, meno doppi lavori, meno contestazioni.",
 "La pianificazione rigida muore al primo imprevisto: serve la revisione settimanale, non la pianta fissa.",
 "Costo: tempo di pianificazione (ore); ritorno: 5-15% di riduzione dei giorni cantiere nelle imprese che introducono la pianificazione (stima pratica di settore).",
 "Cantiere ristrutturazione con piano consegne settimanale: zero furti di materiale (prima 3 furti a cantiere) e consegna 3 settimane prima, con bonus del cliente.",
 "DM 81/2008 (organizzazione cantiere); diario di cantiere come prova in contenzioso.",
 "Il diario di cantiere quotidiano è la polizza assicurativa dell'impresa: chi non scrive, non esiste."),
s("Controllo gestione", "Il controllo di gestione: SAL, consuntivi, scostamenti",
 "Il controllo di gestione misura se il cantiere sta producendo margine: contabilità interna per commessa (ricavi, costi maturati, margine), confronto preventivo/consuntivo a voci, analisi degli scostamenti (perché il costo manodopera è al 130%?).",
 "Metodo: chiusura SAL mensile con il cliente, rilevazione interna dei costi reali (buste paga cantieri, fatture materiali allocate alla commessa), report mensile per cantiere: fatturato, costo, margine, % avanzamento, stima a finire; l'indice salvavita è la stima a finire: quanto margine resta realisticamente.",
 "Imprese con più cantieri contemporanei: è il solo modo di sapere quale cantiere sta morendo PRIORA che sia finito.",
 "Il cantiere in rosso si vede al terzo mese, non alla consegna: c'è tempo di correre ai ripari (riorganizzazione, contenzione, trattativa).",
 "Richiede dati interni puliti: chi non alloca i costi alle commesse (buste paga, mezzi) non può controllare nulla.",
 "Costo: amministrazione che lavora per commessa (1-2 ore/cantiere/mese in più); software: 50-200 €/mese.",
 "Impresa con report mensile per commessa: scoperto al 40% di avanzamento che un cantiere da 400.000 € avrebbe chiuso in perdita di 35.000 €; rinegoziati i subappalti e chiuso a -8.000 €, salvando il margine degli altri cantieri.",
 "Nessuna norma; buona pratica di amministrazione industriale.",
 "Domanda mensile del titolare: 'dove siamo davvero su ogni cantiere?' — chi non sa rispondere sta guidando al buio."),
s("Finanza", "Finanza agevolata e incentivi per l'impresa edile",
 "L'impresa edile può accedere a risorse pubbliche: bandi regionali e nazionali per investimenti (macchinari, digitalizzazione), crediti d'imposta (transizione energetica, formazione, occupazione giovanile), finanziamenti agevolati (Mediocredito Centrale, Invitalia, Europa), garanzie sui finanziamenti.",
 "Metodo: monitoraggio bandi (sportelli camerali, portali regionali, Invitalia, sito incentivi), verifica dei requisiti PRIORA di investire (molti bandi premiano spese già pianificate ma non ancora sostenute), rendicontazione puntuale (fatture, prove di pagamento), supporto di consulenti abilitati con percentuale sul risultato.",
 "Investimenti in macchinari, software, formazione del personale, assunzioni.",
 "Il bando giusto finanzia il 30-50% di un investimento: la differenza tra comprare il macchinario quest'anno o fra tre.",
 "La rendicontazione approssimativa fa perdere agevolazioni già concesse: la burocrazia premia la precisione e punisce la fretta.",
 "Costo consulenza bandi: 1.000-5.000 € o 5-15% dell'agevolazione; i portali di bandi base sono gratuiti.",
 "Impresa che ha ottenuto un contributo regionale del 40% su un software di cantiere e formazione: investimento di 60.000 €, esborso reale 36.000 €, con produttività che ha ripagato il resto in 14 mesi.",
 "Regolamenti dei singoli bandi (Regione, MIMIT, Invitalia); normativa fiscale annuale (crediti d'imposta).",
 "La finanza agevolata è un mestiere: chi la cura come hobby lascia soldi sul tavolo ogni anno."),
s("Personale", "Il personale: CCNL, artigiani, appalti interni e crescita delle competenze",
 "La manodopera è il cuore e il rischio maggiore dell'impresa edile: contrattualistica (CCNL edilizia e industria, part-time, somministrazione), gestione dei rapporti (assunzioni, dimissioni, malattie, infortuni), sviluppo delle competenze (formazione obbligatoria e strategica).",
 "Strumenti: contratti conformi CCNL con mansioni coerenti col lavoro svolto (una delle prime verifiche in caso di contenzioso), libretto professionale del lavoratore edile (obbligo formazione 80 ore base), valutazione annuale semplice, piano di successione del capocantiere; attenzione al lavoro irregolare: in edilizia l'illecito amministrativo è sanzionato pesantemente (sospensione lavori).",
 "Imprese con operai dipendenti: dalla seconda persona in poi la gestione del personale è una funzione piena.",
 "Il personale stabile formato è un vantaggio competitivo: la qualità della posa dipende dalle mani, non dalle macchine.",
 "La gestione del personale è il punto dove le imprese edili sono più fragili: infortuni, contenziosi, dimissioni improvvise.",
 "Costo onere medio operaio edile: 28-38 €/ora di costo aziendale (busta paga + oneri), molto variabile per qualifica e CCNL; consulente del lavoro: 100-300 €/mese.",
 "Impresa che ha formato un operaio a muratore-specializzato (corso posa cappotto certificato): il dipendente è diventato il riferimento tecnico di 4 cantieri, con zero errori di posa da quando.",
 "CCNL Edilizia (ultimo rinnovo da verificare annualmente); D.Lgs 81/2008 (formazione sicurezza); normativa lavoro irregolare (D.Lgs 124/2004? pacchetto sicurezza cantieri).",
 "Regola: l'operaio formato costa meno dell'operaio improvvisato, anche se il secondo chiede meno all'ora."),
s("Marketing impresa", "Il marketing dell'impresa edile: reputazione, referral, digital",
 "L'impresa edile vende fiducia: il marketing efficace è la somma di reputazione (cantieri fatti bene e visibili), referral (clienti e professionisti che raccomandano), presenza digitale (sito, foto cantieri prima/dopo, recensioni), identità riconoscibile (mezzi curati, divise, cantiere ordinato).",
 "Strumenti: Google Business Profile con recensioni gestite (rispondere a TUTTE), portfolio fotografico professionale (una sessione fotografica a cantiere finito: 300-800 €), casi studio scritti (problema → soluzione → risultato), partnership ricorrenti con studi di progettazione, social con contenuti di cantiere reali (non stock).",
 "Imprese che vogliono scegliere le commesse invece di accettarle tutte.",
 "La reputazione digitale riduce il costo di acquisizione: chi trova 50 recensioni a 4,9 stelle chiama già convinto.",
 "Il marketing senza il prodotto (cantieri fatti male) amplifica il danno: le recensioni negative sono permanenti.",
 "Budget marketing per impresa edile: 1-3% del fatturato; sito vetrina: 1.000-3.000 €; gestione social: 300-800 €/mese interno/esterno.",
 "Impresa di ristrutturazioni con 120 recensioni Google gestite: il 70% dei nuovi clienti dichiara di aver scelto loro per le recensioni; prezzi medi in crescita perché la domanda qualificata è sovrabbondante.",
 "Nessuna norma specifica; deontologia commerciale (pubblicità non ingannevole, codice del consumismo).",
 "Il miglior marketing edile è il cantiere pulito in una strada frequentata: il cartello con il numero di telefono vale più di mille volantini."),
s("Qualità impresa", "Qualità e certificazioni d'impresa: ISO 9001, SOA, credito",
 "Le certificazioni d'impresa sono requisiti di accesso e fattori di fiducia: ISO 9001 (qualità dei processi), SOA (qualificazione per lavori pubblici sopra soglia), attestazione di qualità ambientale e sicurezza (ISO 14001, ISO 45001), rating di legalità, visure camerali pulite, bilanci ordinati per l'accesso al credito.",
 "Metodo: ISO 9001 con ente certificatore accreditato (audit annuale), SOA con categoria e classifica coerenti col fatturato (le classifiche si mantengono con il fatturato medio ponderato), rating di legalità richiesto da molte stazioni appaltanti; mantenere il rating di credito pulito: pagamenti fornitori puntuali, bilanci in regola.",
 "Gare pubbliche, grandi committenti privati, accesso a fidi bancari.",
 "Le certificazioni aprono porte: senza SOA non esisti per la pubblica amministrazione; con ISO 9001 molte gare private ti prequalificano d'ufficio.",
 "Le certificazioni 'solo da esposizione' (procedura scritta mai seguita) saltano al primo audit e costano caro in reputazione.",
 "Costi: ISO 9001 da 1.500-4.000 €/anno (ente + consulente), SOA da 2.000-6.000 € di mantenimento annuo, più il requisito patrimoniale per le classifiche.",
 "Impresa che ha ottenuto la SOA categoria OG2 classifica III: è passata da subappalti a commesse dirette da 800.000 €, con margine medio raddoppiato.",
 "Legge 1423/1956 (SOA); norme UNI EN ISO 9001/14001/45001; D.Lgs 159/2011 (anti-mafia, requisiti di affidabilità).",
 "Le certificazioni vanno curate come i cantieri: chi le tiene 'a batteria' trova la scadenza l'ultimo giorno utile."),
s("Rischio", "Gestione del rischio: contrattuale, assicurativo, finanziario",
 "L'impresa edile vive di rischi: il mestiere dell'imprenditore è selezionarli, prezzarli e assicurarli; i rischi principali: contenziosi (vizi, ritardi, varianti), infortuni e danni a terzi, insolvenze dei committenti, oscillazione prezzi materiali, cambiamenti normativi a cantiere aperto.",
 "Strumenti: contratti scritti SEMPRE (anche la piccola manutenzione, con voci chiare su cosa ESCLUDE), polizze RCT/RCO e all risk cantiere, fideiussione e garanzie richieste dai committenti benestanti (valutarne il costo nel prezzo), clausole di revisione prezzi sui materiali per commesse lunghe (legge 1082/1971), credito commerciale controllato (nessun anticipo fornitore senza caparra a garanzia).",
 "Ogni impresa edile, dal monoposto alla general contractor.",
 "La gestione del rischio non elimina gli imprevisti ma li rende sopravvivibili: l'impresa assicurata e contrattualizzata può sbagliare una commessa senza fallire.",
 "L'assicurazione 'perché tanto non succede niente' è la prima voce tagliata nelle crisi: errore classico che trasforma un incidente in un fallimento.",
 "Polizza RCT/RCO: 1.500-6.000 €/anno; all risk cantiere: 0,3-1% del valore lavori; consulente assicurativo specializzato: a provvigione.",
 "Impresa colpita da un danno a un appartamento confinante per una perdita d'acqua: la RCT ha coperto 85.000 € di danni e ricostruzione rapporti col vicino; senza polizza, la fine dell'azienda.",
 "Codice civile (appalto, responsabilità); CCNL (responsabilità verso dipendenti); normativa assicurativa (IVASS).",
 "Principio: il rischio non assicurato e non prezzato è un regalo del proprio patrimonio al destino."),
s("Digitalizzazione", "La digitalizzazione dell'impresa: gestionale, personale, cantiere 4.0",
 "La trasformazione digitale dell'impresa edile parte dalla contabilità e arriva al cantiere: gestionale contabile integrato, fatturazione elettronica, ordini e magazzino digitali, presenze cantieri via app, documenti di cantiere digitali (diario, verbali, foto georeferenziate), collaborazione con modelli BIM quando richiesto.",
 "Percorso graduale: 1) contabilità e fatture digitali (obbligo), 2) presenze e costi di cantiere via app (es. timbrature smartphone + fogli ore digitali), 3) archivio documentale condiviso (foto cantiere per commessa), 4) gestionale produzione (commesse, SAL, acquisti), 5) integrazione BIM quando il mercato lo chiede; ogni passo deve eliminare carta e doppi inserimenti.",
 "Imprese che vogliono scalare senza ingrossare l'ufficio.",
 "La digitalizzazione giusta fa lavorare l'impresa con meno amministrazione per fatturato: i dati entrano una volta e si usano ovunque.",
 "Il software sbagliato o introdotto senza formazione diventa costo e resistenza: il migliore è quello che il personale usa davvero.",
 "Gestionale: 50-300 €/mese per modulo; app presenze: 2-5 €/dipendente/mese; formazione interna: giorni iniziali poi routine.",
 "Impresa che ha digitalizzato presenze, diario e foto cantieri: il tempo dell'amministratore su ogni cantiere è sceso del 60%, e due vertenze su fasi lavorative si sono chiuse in giorni perché il diario digitale fotografico era incontestabile.",
 "Nessuna norma cogente sulla digitalizzazione interna; fatturazione elettronica (obbligo); GDPR per i dati del personale (foto cantieri, presenze).",
 "La domanda per il LLM consulente: 'quale processo della mia impresa dipende ancora dalla memoria di una persona?' — quello è il prossimo da digitalizzare."),
]

README = """# MASTER_IMPRESA_EDILE_PACK — Gestione d'impresa per costruttori e imprenditori edili

**Facoltà:** FACOLTA_GESTIONE_SISTEMA · **Livello:** L3 (master imprenditoriale) · **Schede:** {n}

## Contenuto
Il ramo gestionale dell'università: forme giuridiche, organizzazione e deleghe,
acquisizione commesse e politica dei prezzi, preventivo con margine, produzione
di cantiere come fabbrica, controllo di gestione per commessa, finanza agevolata
e bandi, personale e CCNL, marketing dell'impresa edile, certificazioni (ISO, SOA)
e gestione del rischio contrattuale/assicurativo, digitalizzazione graduale.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza manageriale per imprese edili, business coaching, analisi di
prezzi e margini, gestione del personale, strategia di crescita. I valori economici
sono fasce indicative 2025 da verificare su CCNL e mercato aggiornati.
""".format(n=len(DATA))

COURSE = """corso: "Master in gestione d'impresa edile"
facolta: "FACOLTA_GESTIONE_SISTEMA"
livello: "L3"
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
