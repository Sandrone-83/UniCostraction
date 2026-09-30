# -*- coding: utf-8 -*-
"""Seconda ondata del Digitale_Marketing_Pack: approfondimento marketing + coding."""
import json, os

BASE = r"C:\Users\alessandro\Documents\kimi\tasks\2026-09-26\15-14-07-e3d653af\Digitale_Marketing_Pack\parsed"

LIC = "Sintesi didattica originale Kimi (pubblico dominio)"

SRC = {"MAR": "marketing_edile_kimi", "COD": "coding_fondamenti_kimi", "WEB": "sviluppo_web_app_kimi"}

def rec(id_, cat, tema, title, text, source=""):
    if not source:
        source = SRC[id_.split("-")[0]]
    return {"id": id_, "categoria": cat, "tema": tema, "title": title, "text": text,
            "source": source, "license": LIC, "commercial_ok": True,
            "attribution": "Corpus marketing edile a cura di Kimi", "url": ""}

marketing = [
rec("MAR-014","vendita","funnel_vendita","FUNNEL DI VENDITA EDILE: DALLA RICHIESTA AL CANTIERE",
"Il cliente edile non compra un muro: compra sicurezza, rispetto dei tempi e zero pensieri. Il funnel e' il percorso che lo porta da uno che 'chiede un preventivo' a uno che firma.\n\n"
"1. ATTRAZIONE (top): contenuti, ads, passaparola. L'obiettivo non e' vendere ma farsi trovare: 'impresa ristrutturazioni + citta'' deve restituire l'azienda.\n"
"2. INTERESSE (mid): il cliente confronta 3-5 imprese. Qui si vince con: sito con foto reali dei cantieri, recensioni Google visibili, risposta entro 2 ore alla richiesta, un sopralluogo professionale. Il preventivo gratuito e' uno strumento di qualificazione: meglio 'sopralluogo e preventivo dettagliato a pagamento, scalato in caso di conferma' per filtrare i curiosi.\n"
"3. DECISIONE (bottom): il cliente decide in base a fiducia > prezzo. Strumenti di chiusura: preventivo chiaro a voci (materiali, manodopera, tempi, capitolato), referenze dirette da chiamare, garanzie scritte (DECENNALE), piano di pagamento legato a stati di avanzamento.\n"
"4. FIDELIZZAZIONE (post-vendita): il 70% del lavoro di un'impresa sana arriva da clienti e referenze. A fine cantiere: foto professionali del risultato, richiesta recensione dopo 15 giorni, manutenzione programmata, biglietto di auguri annuale.\n\n"
"REGOLA D'ORO: misurare ogni passaggio. Quante richieste arrivano, quanti sopralluoghi, quanti preventivi inviati, quanti firmati. Il collo di bottiglia si vede dai numeri, non dalle sensazioni."),

rec("MAR-015","vendita","email_marketing","EMAIL MARKETING E NUTRIZIONE DEI LEAD EDILI",
"L'email non e' morta: e' il canale con il ROI piu' alto in assoluto perche' chi e' nella lista ha gia' incontrato l'impresa.\n\n"
"1. RACCOLTA: ogni sopralluogo che non chiude, ogni visita al sito, ogni contatto in fiera deve finire in una lista con consenso (GDPR: doppio opt-in consigliato).\n"
"2. SEGMENTAZIONE: 'ristrutturazione bagno' e 'villa nuova' non vogliono gli stessi contenuti. Almeno 3 liste: privati piccole opere, privati grandi opere, professionisti/aziende.\n"
"3. CONTENUTI: una newsletter mensile con 1 cantiere documentato (foto prima/dopo), 1 consiglio tecnico utile ('come capire se un muro e' portante'), 1 risposta a una domanda frequente. Non vendere sempre: il 80% valore, 20% offerta.\n"
"4. AUTOMATIZZAZIONE: sequenza automatica per chi richiede il preventivo ma non risponde: giorno 3 email 'e' tutto chiaro? domande?', giorno 10 'ecco un cantiere simile al suo', giorno 30 'ultimo sollecito + foto lavori recenti'. Tool: MailerLite, Brevo, Mailchimp (da 0 a 30 euro/mese).\n\n"
"METRICA CHIAVE: tasso di apertura > 25% e click > 3% per una lista edile ben tenuta."),

rec("MAR-016","brand","personal_branding","PERSONAL BRANDING DEL TITOLARE: L'ARTIGIANO CHE DIVENTA VOCE",
"Nell'edilizia la gente compra persone, non loghi. Il titolare che si mette in gioco batte il marchio anonimo.\n\n"
"1. PERCHE': il cliente affida casa e risparmi a uno sconosciuto: vedere il volto, sentire la voce, capire il modo di lavorare riduce la percezione di rischio piu' di qualsiasi brochure.\n"
"2. COSA RACCONTARE: il cantiere quotidiano (senza sceneggiare), gli errori e come li si risolve (massima fiducia), le scelte tecniche spiegate semplice ('perche' qui mettiamo il cartongesso e non il mattone'), i materiali e perche' quelli.\n"
"3. DOVE: un canale principale dove eccellere (di solito Instagram o YouTube) + presenza minima ovunque. Meglio 3 video a settimana buoni che 7 scarsi.\n"
"4. ERRORI DA EVITARE: volti volontari in cantiere senza liberatorie, parlare male della concorrenza, finte perfezioni, politica e religioni, promesse non mantenibili ('finito in una settimana').\n\n"
"EFFETTO COMPOSTO: dopo 12-18 mesi di costanza, il personal brand genera richieste spontanee e alza il prezzo percepito: chi ti segue da mesi non ti tratta come il preventivo piu' economico."),

rec("MAR-017","strategia","segmentazione","MARKETING PER RISTRUTTURAZIONE VS NUOVA COSTRUZIONE",
"Sono due mercati con psicologie diverse: chi ristruttura ha fretta e paura dei sopraggiunti; chi costruisce nuovo ha un progetto e un mutuo.\n\n"
"RISTRUTTURAZIONE (bagno, cucina, impianti, cappotto):\n- Dolore principale: disguidi, polvere, tempi, imprevisti alzati a cantiere aperto.\n- Messaggio vincente: 'preventivo chiuso', 'tempi garantiti con penale', 'cantiere pulito giornalmente', 'sopraggiunti concordati per iscritto'.\n- Canali: Google (chi cerca e' gia' deciso), Instagram prima/dopo, passaparolo del quartiere.\n- Tempo di decisione: 2-8 settimane. Chiudere in fretta con garanzie.\n\n"
"NUOVA COSTRUZIONE E GRANDI OPERE:\n- Dolore principale: la sfiducia verso il costruttore, la paura che il mutuo venga eroso da varianti.\n- Messaggio vincente: 'capienza tecnica' (chiavi in mano con capitolato), referenze visitabili, struttura societaria solida, assicurazioni.\n- Canali: B2B con studi di progettazione, fiere, PR locali, content tecnico.\n- Tempo di decisione: mesi/anni. Serve un CRM e nutrizione lunga.\n\n"
"REGOLA: non usare lo stesso tono. La ristrutturazione si vende con calore e rassicurazione, la nuova costruzione con competenza e solidita'."),

rec("MAR-018","partnership","rete_partner","PARTNERSHIP E RETI: ARCHITETTI, GEOMETRI, RIVENDITORI, CONSULENTI",
"Il canale piu' redditizio e' spesso gratis: le persone che incontrano il cliente PRIMA dell'impresa.\n\n"
"CHI SONO I PARTNER IDEALI:\n- Architetti e geometri: propongono 2-3 imprese ai propri clienti.\n- Rivenditori materiali e show room cucine/bagni: vedono chi sta ristrutturando prima di tutti.\n- Amministratori di condominio e agenzie immobiliari: soprattutto per manutenzioni e piccole opere.\n- Consulenti energetici e CAF: per chi arriva con il Conto Termico o le detrazioni.\n\n"
"COME COSTRUIRE LA RETE:\n1. Lista di 30 potenziali partner della zona, con ricerca mirata.\n2. Incontro o caffa' senza vendere nulla: capire cosa serve a loro (preventivi rapidi? affidabilita'? zero richieste di retrocessioni scomode?).\n3. Dare prima di ricevere: passare loro lavori di manutenzione piccoli, informazioni di cantiere, visibilita' sui propri canali.\n4. Rendi l'invio reciproco un'abitudine: gruppo WhatsApp, evento annuale, aggiornamenti su lavori finiti.\n\n"
"ATTENZIONE: le retrocessioni economiche (kickback) sono una pratica controversa e a rischio legale/etico: meglio costruire la rete su reciprocita' e qualita', non su commissioni occulte."),

rec("MAR-019","vendita","pricing_comunicazione","PRICING EDILE: COME COMUNICARE IL PREZZO SENZA PERDERE IL CLIENTE",
"Il prezzo nel settore edile non e' un numero: e' una storia di cosa include e di quali rischi toglie.\n\n"
"1. MAI UN PREZZO SENZA CONTESTO: '20.000 euro' spaventa; '20.000 euro comprensivi di materiali, manodopera certificata, smaltimento, collaudi, 10 anni di garanzia e piano di pagamento a stati di avanzamento' e' un'altra cosa.\n"
"2. L'ANCORA: presentare 3 livelli (base/comfort/premium) sposta il confronto da 'io contro la concorrenza' a 'base contro premium'. La maggior parte sceglie il centro.\n"
"3. IL PREZZO ORARIO E' IL NEMICO: il cliente non puo' verificare le ore. Vendere a corpo o a misura con capitolato: trasferisce il rischio dell'imprevisto dove deve stare (chi ha visibilita' tecnica) e giustifica il valore.\n"
"4. SOPRAGGIUNTI: regola scritta nel preventivo — 'lavori aggiuntivi solo con conferma scritta entro 24h, con prezzo gia' definito a listino'. Il cliente che sa che non ci saranno sorprese firma piu' volentieri.\n"
"5. SCONTARE SOLO SCAMBIANDO: mai sconti incondizionati. Se il cliente chiede di ridurre, togliere una voce (es. i sanitari che si compra da solo), non abbassare il prezzo della stessa voce.\n\n"
"PRINCIPIO: chi e' il piu' economico attira i clienti peggiori; chi spiega meglio il valore lavora meglio e fattura di piu'."),

rec("MAR-020","contenuti","fotografia_cantiere","FOTOGRAFIA DI CANTIERE: LA MATERIALE PRIMA DEL MARKETING EDILE",
"Nell'edilizia le foto vendono piu' delle parole: il cantiere ben fotografato e' la fonte di ogni altro contenuto (social, sito, ads, fiere).\n\n"
"COME FARE FOTO CHE VENDONO:\n1. PRIMA/DOPO: stesso punto di ripresa, stessa luce se possibile. E' il formato piu' potente di tutto il marketing edile.\n"
"2. DURANTE: il dietro le quinte (impianti a vista, isolamento, struttura) dimostra competenza tecnica: e' il contenuto che gli altri imprenditori e i professionisti apprezzano e condividono.\n"
"3. DETTAGLI: fughe perfette, giunzioni, materiali. Il dettaglio ben fatto parla di cura.\n"
"4. REGOLE TECNICHE: pulire la scena prima di scattare, luce naturale, orizzontali dritti (usare la griglia del telefono), non usare flash in cantiere, formato verticale 9:16 per i reel.\n\n"
"DIRITTI E PRIVACY:\n- liberatoria scritta per ogni persona riconoscibile;\n- attenzione alla privacy della casa del cliente (indirizzo, interni identificabili);\n- foto da cantiere pubblici: verificare i vincoli del committente.\n\n"
"FLUSSO OPERATIVO: chiudere ogni cantiere con un set fotografico professionale (anche un fotografo paga per un lavoro importante), archiviare per tipologia (bagni, facciate, strutture), riusare per anni."),

rec("MAR-021","local","google_business","GOOGLE BUSINESS PROFILE: LA VETRINA CHE DECIDE CHI TI CHIAMA",
"Per l'impresa locale il profilo Google e' piu' importante del sito: chi cerca 'impresa edile vicino a me' decide in 10 secondi dalla scheda.\n\n"
"OTTIMIZZAZIONE COMPLETA:\n1. CATEGORIE: primaria 'Impresa edile' + secondarie (Ristrutturazione bagno, Impiantista, Pittore edile...). Le categorie pesano piu' delle parole.\n"
"2. FOTO: minimo 30 foto reali (cantieri, squadra, mezzi, sede), aggiornate ogni mese. I profili con foto ricevono molte piu' richieste di contatto.\n"
"3. POST E AGGIORNAMENTI: pubblicare come un social: cantiere finito, assunzioni, promozioni stagionali. Segnala attivita' a Google.\n"
"4. RECENSIONI: chiedere a ogni cliente soddisfatto, con link diretto. Rispondere a TUTTE, anche alle negative (con calma, offrendo soluzione). 4,7+ stelle e volume costante battono qualsiasi ads.\n"
"5. DOMANDE E RISPONDE: rispondere a tutte; inserire anche le proprie FAQ piu' frequenti.\n"
"6. SERVIZI, ORARI, AREA, SITO, PREVENTIVO: compilare tutto, inserire attributi ('offre preventivi online').\n\n"
"KPI: chiamate, richieste di indicazioni stradali e clic sul sito dal pannello statistiche di Google. E' il dato marketing piu' onesto che un'impresa locale abbia."),

rec("MAR-022","strategia","marketing_b2b","MARKETING B2B: GRANDI OPERE, GENERAL CONTRACTOR E COMMITTENTI PUBBLICI",
"Vendere a un general contractor o a una stazione appaltante e' un gioco diverso dal privato: meno emozione, piu' requisiti.\n\n"
"1. IL PROCESSO DI ACQUISTO B2B: commissioni di valutazione, gare a cui si accede con referenze e prequalifiche, cicli di 6-24 mesi. Chi non e' nel radar PRIMA della gara non esiste.\n"
"2. PREQUALIFICA: portfolio lavori analitico (ruolo, valore, committente, referenze), bilanci in ordine, certificazioni (ISO 9001, 14001, 45001, SOA per pubblico), DURC, gestione sicurezza documentata.\n"
"3. CANALI B2B: LinkedIn (la piattaforma B2B in Italia), fiere di settore (SAIE, Made Expo), PR su testate di settore, relationship con direttori lavori e progettisti, portali gare.\n"
"4. CONTENUTI CHE FUNZIONANO: case study tecnici ('come abbiamo risolto X problema su Y tipologia'), white paper, webinar tecnici, partecipazione a tavole di confronto. Il contenuto tecnico serio e' l'equivalente B2B del prima/dopo del privato.\n"
"5. PUBBLICO: per lavorare con PA serve la SOA (classifiche OG/OS), requisiti antimafia, personale con patentini; il marketing diventa documentale: una documentazione impeccabile VENDE.\n\n"
"ERRORE TIPICO: presentarsi in gara con il prezzo piu' basso senza costruire relazione e reputazione prima. Il B2B premia chi e' noto, affidabile e gia' stato verificato da altri."),

rec("MAR-023","contenuti","community_passaparola","COMMUNITY E PASSAPAROLA DIGITALE NEL QUARTIERE",
"Il passaparola e' sempre stato il motore dell'impresa edile: ora avviene nei gruppi Facebook del quartiere, nei condomini digitali e nei commenti.\n\n"
"1. GRUPPI LOCALI: essere presenti (con trasparenza, dichiarando di essere dell'impresa) nei gruppi 'segnalazioni' del Comune/quartiere: rispondere a chi cerca 'muratore bravo' con gentilezza e senza spammare link.\n"
"2. IL CLIENTE COME AMBASSADORE: a cantiere finito, oltre alla recensione, chiedere di poter essere nominati: 'se qualcuno nel palazzo/in famiglia ha bisogno...'. Offrire uno sconto manutenzione annuale in cambio di presentazioni.\n"
"3. CANTIERE VISIBILE: il cantiere e' un cartellone: insegna ordinata con logo e contatti, recinzione pulita, il vicino che guarda = il vicino che un giorno chiama. I vicini vedono come lavori ogni giorno per settimane: sono il pubblico piu' convinto.\n"
"4. EVENTI MICRO: un aperitivo/caffa' nella casa appena finita con i vicini interessati; la 'cantiere aperto' il sabato mattina per chi sta valutando lavori simili.\n\n"
"REGOLA: il passaparola digitale si costruisce con la stessa lentezza di quello vero — mesi di lavoro ben fatto, recensioni vere, presenza gentile — e si perde in una risposta stizzita a un commento negativo. Mai rispondere male in pubblico."),
]

coding = [
rec("COD-009","pratica","debugging","DEBUGGING: IL METODO PER RIPARARE QUALSIASI PROGRAMMA",
"Riparare software e' un'abilita' che si impara con un metodo, non con l'intuizione.\n\n"
"IL CICLO DI DEBUGGING:\n1. RIPRODURRE IL PROBLEMA: se non si sa come far accadere il bug, non si puo' verificare la riparazione. Documentare: input, azioni, risultato atteso, risultato ottenuto.\n"
"2. LEGGERE L'ERRORE: gli errori sembrano criptici ma dicono file, riga e tipo di problema. Imparare a leggerli e' il 50% del lavoro.\n"
"3. ISOLARE: commentare o spezzare il codice fino a trovare la porzione colpevole. La tecnica del 'commentare a meta'': disattivare meta' delle istruzioni e vedere se il bug sparisce.\n"
"4. STRUMENTI: debugger integrato (breakpoint, esecuzione passo-passo, ispezione variabili) e print/logging strategici. Un log ben posizionato vale ore di tentativi.\n"
"5. VERIFICA: dopo la correzione, eseguire il caso che generava l'errore + i casi vicini. Senza verifica la 'riparazione' spesso sposta il problema.\n\n"
"BUG TIPICI DA CONOSCERE: off-by-one nei cicli, variabili non inizializzate, confusione tra stringhe e numeri, problemi di concorrenza (due operazioni insieme), dipendenze obsolete, errori di copia-incolla.\n\n"
"DEBUGGING CON L'AI: dare all'assistente il messaggio d'errore completo + il codice della funzione + cosa ci si aspettava. Non incollare migliaia di righe: il contesto mirato da risposte migliori."),

rec("COD-010","pratica","testing","TESTING: GARANTIRE CHE IL SOFTWARE FUNZIONI SEMPRE",
"Testare significa verificare il comportamento prima che a farlo sia il cliente.\n\n"
"PIRAMIDE DEI TEST:\n1. UNIT TEST: verificano la singola funzione (es. 'calcola_cerchiaio(4.5) deve dare 28.27'). Veloci, numerosi, automatizzati. Framework: Jest (JS), pytest (Python), JUnit (Java).\n"
"2. TEST DI INTEGRAZIONE: verificano che le parti parlino bene tra loro (database + applicazione, API + frontend).\n"
"3. TEST END-TO-END: simulano l'utente reale (apre la pagina, clicca, compila il form). Tool: Playwright, Cypress.\n"
"4. TEST MANUALE ESPLORATIVO: l'occhio umano su cio' che non e' prevedibile.\n\n"
"TDD (TEST DRIVEN DEVELOPMENT): si scrive prima il test, poi il codice che lo soddisfa. Obbliga a pensare all'interfaccia prima dell'implementazione e garantisce un paracadute a ogni modifica futura.\n\n"
"PERCHE' CONVIENE: ogni modifica successiva (nuova funzione, aggiornamento libreria) rischia di rompere cio' che funzionava. Con i test automatizzati, un comando riesegue tutte le verifiche in secondi. Il costo del testing e' una frazione del costo di un guasto in produzione — in ambito edile, pensare a un software di computo che sbaglia le quantita': il test e' l'equivalente del collaudo.\n\n"
"MINIMO VIABLE PER UN PROGETTO PICCOLO: test solo per le funzioni critiche (calcoli, soldi, dati dei clienti)."),

rec("COD-011","architettura","design_pattern","ARCHITETTURA SOFTWARE E DESIGN PATTERN",
"L'architettura e' come si organizza un programma grande per restare comprensibile e modificabile.\n\n"
"STRUTTURE FONDAMENTALI:\n- MONOLITICA: tutto in un'unica applicazione. Giusta per partire: piu' semplice da sviluppare e distribuire.\n"
"- A MICROSERVIZI: l'applicazione e' spezzata in servizi indipendenti (uno per utenti, uno per preventivi, uno per notifiche). Potente ma complesso: solo quando il monolite stringe.\n"
"- A STRATI: presentazione (interfaccia) / logica (regole) / dati (database). Separare i livelli permette di cambiarne uno senza toccare gli altri.\n\n"
"PATTERN RICORRENTI (soluzioni gia' inventate a problemi comuni):\n- MVC: Modello (dati) / Vista (interfaccia) / Controller (logica). Base di quasi ogni web framework.\n"
"- SINGLETON: una sola istanza di un oggetto (es. la connessione al database).\n"
"- OBSERVER: quando qualcosa cambia, chi e' interessato viene avvisato (es. il cliente riceve una mail quando il preventivo e' pronto).\n"
"- FACTORY: creare oggetti complessi in modo standardizzato.\n\n"
"PRINCIPI GUIDA: 'non ripeterti' (DRY), 'ogni cosa deve avere un solo motivo per cambiare' (responsabilita' unica), 'dipendi da astrazioni, non da dettagli' (per poter sostituire componenti).\n\n"
"REGOLA PRATICA: per i primi progetti contano poco i pattern e molto la chiarezza. Un codice semplice e' meglio di un codice elegante incomprensibile."),

rec("COD-012","architettura","performance","PERFORMANCE: VELOCITA' E OTTIMIZZAZIONE DEL SOFTWARE",
"Il software lento perde utenti e denaro: ogni 100 ms in piu' di caricamento riduce le conversioni.\n\n"
"DOVE GUARDARE PRIMA:\n1. MISURARE, NON INDOVINARE: strumenti come Lighthouse (web), profiler (codice) dicono dove il tempo va davvero. L'80% dei guadagni viene dal 20% dei problemi.\n"
"2. DATABASE: quasi sempre il collo di bottiglia. Indici sulle colonne cercate di frequente, query che portano solo i dati necessari, connessioni riutilizzate.\n"
"3. RETE E FRONTEND: immagini compresse e in formati moderni (WebP/AVIF), caricamento 'lazy' (solo quando visibili), caching del browser e della CDN.\n"
"4. CODICE: evitare cicli dentro cicli dove possibile (notazione O grande), non fare lavoro ripetuto dentro i loop, cache per risultati costosi.\n\n"
"SCALABILITA': quando gli utenti crescono:\n- VERTICALE: macchina piu' potente. Semplice ma ha limiti fisici.\n"
"- ORIZZONTALE: piu' macchine che dividono il carico (load balancer). E' come passare da un muratore bravissimo a una squadra.\n"
"\n"
"ASINCRONIA: le operazioni lente (invio email, generazione PDF, chiamate esterne) non devono bloccare l'utente: vanno in coda e completate in background.\n\n"
"PRINCIPIO: l'ottimizzazione prematura e' la radice di ogni problema: prima farlo funzionare correttamente, poi misurare, poi ottimizzare solo cio' che misura dice."),

rec("COD-013","pratica","oop_pratica","PROGRAMMAZIONE A OGGETTI APPLICATA: DALLA TEORIA AL CODICE",
"L'OOP organizza il codice in oggetti che combinano dati e comportamenti — come in cantiere: un 'Ponteggio' ha proprieta' (altezza, metri lineari, certificazione) e azioni (monta, smonta, verifica).\n\n"
"CONCETTI CHIAVE CON ESEMPI EDILI:\n- CLASSE vs OGGETTO: la classe e' il progetto ('Muratura'), l'oggetto e' il reale (il muro del bagno di via Roma).\n"
"- INCAPSULAMENTO: i dati sensibili si proteggono (il prezzo interno del preventivo non e' accessibile a chiunque: metodi pubblici solo per leggere il totale).\n"
"- EREDITARIETA': 'ImpresaEdile' eredita da 'Impresa' (ragione sociale, P.IVA) aggiungendo SOA e categorie. Evita di riscrivere cio' che esiste gia'.\n"
"- POLIMORFISMO: la stessa operazione si comporta diversamente — 'computa' su una 'VoceMuratura' fa un calcolo, su una 'VoceImpianto' ne fa un altro: chi la chiama non deve sapere quale.\n\n"
"QUANDO CONVIENE: modelli di dominio complessi (preventivi, capitolati, computi) dove i concetti del mondo reale diventano classi. Un computo metrico e' naturalmente orientato agli oggetti: Voce, Categoria, Prezzo, Sovrapprezzo.\n\n"
"QUANDO NO: script brevi, trasformazioni dati semplici: la programmazione funzionale (funzioni pure) e' piu' diretta. Usare l'OOP dove il dominio lo richiede, non per abitudine.\n\n"
"CODICE PULITO: nomi che dicono cosa sono ('prezzo_al_mq' non 'pp'), funzioni corte che fanno una cosa, commenti che spiegano il perche' non il cosa."),

rec("COD-014","pratica","esercizi","PROBLEMI DA RISOLVERE CON CODICE (CULTURA PRATICA PER AURATRIX)",
"Per sapere costruire software bisogna aver risolto problemi veri. Raccolta di esercizi progressivi con utilita' edile.\n\n"
"LIVELLO 1 — BASI:\n1. Calcolatrice del preventivo: dato listino materiali e metri quadri, calcolare il costo base con IVA.\n2. Convertitore unita' di cantiere: mq in numero di cartongesse/pannelli/smalti (con resa al litro).\n3. Conteggio giorni cantiere: data inizio + giorni lavorativi (senza festivi) = data fine stimata.\n\n"
"LIVELLO 2 — STRUTTURE DATI:\n4. Gestore anagrafica clienti: aggiungere, cercare, aggiornare record in un file JSON.\n5. Lista lavori da fare in cantiere: ordinare per priorita', segnare completati, salvare stato.\n6. Analisi preventivi: data una lista di voci con importi, calcolare totale, media, voce piu' costosa.\n\n"
"LIVELLO 3 — API E DATI REALI:\n7. Prezzo medio materiali: leggere dati da un CSV di listino e calcolare statistiche.\n8. Bot Telegram di cantiere: comando che registra una nota di cantiere con data e foto.\n9. Verifica CAP: data una provincia, restituire i CAP validi tramite un servizio online.\n\n"
"LIVELLO 4 — PROGETTI COMPLETI:\n10. Mini-computo: voci con quantita', prezzo unitario, automaticamente totale e report stampabile.\n11. Gestionale turni squadra: chi lavora dove, ore, straordinari, export mensile.\n12. Dashboard lavori: una pagina web che mostra lo stato di tutti i cantieri aperti.\n\n"
"METODO: risolvere a mano prima (pseudocodice), poi in codice, poi chiedere a un AI di revisionare la soluzione e imparare dall confronto. Scrivere sempre 3 varianti dello stesso problema con vincoli diversi."),
]

web = [
rec("WEB-008","pratica","backend","BACK-END, AUTENTICAZIONE E DATABASE APPLICATI",
"Il back-end e' la parte invisibile: riceve le richieste, applica le regole, parla col database.\n\n"
"COMPONENTI:\n- API: gli endpoint ('/preventivi', '/clienti/42') che il frontend chiama. REST con JSON e' lo standard.\n"
"- AUTENTICAZIONE: chi sei (login con email+password cifrata — mai in chiaro!) e AUTORIZZAZIONE: cosa puoi fare (il cliente vede solo i propri preventivi). Pattern standard: JWT (token) o sessioni.\n"
"- DATABASE: applicato (Cod.005): tabelle con relazioni. Un gestionale edile: clienti(id, nome...), preventivi(id, cliente_id, stato...), voci(id, preventivo_id, descrizione, quantita', prezzo). Le chiavi esterne collegano i mondi.\n\n"
"ESEMPIO CONCRETO — 'salva preventivo':\n1. Il frontend invia i dati del form a POST /api/preventivi con il token di sessione.\n2. Il back-end verifica chi sei, valida i campi (importi numerici, date valide).\n3. Scrive nella tabella preventivi e nelle voci correlate.\n4. Risponde '201 creato' con l'id del nuovo preventivo.\n5. Un job invia l'email di conferma.\n\n"
"ERRORI DA EVITARE: fidarsi dei dati che arrivano dal client (validare SEMPRE lato server), interrogazioni che girano in ciclo (la N+1 query problem), chiavi segrete hardcoded nel codice (usare variabili d'ambiente), log che registrano password e dati sensibili."),

rec("WEB-009","progetti","configuratore","PROGETTO: CONFIGURATORE/PREVENTIVATORE ONLINE PER L'IMPRESA EDILE",
"Il configuratore online e' il tool di marketing piu' potente per l'impresa edile: il visitante inserisce caratteristiche del lavoro e riceve una stima istantanea, lasciando i contatti.\n\n"
"FUNZIONALITA':\n- Wizard in 4-6 passi: tipo di intervento (bagno/cucina/facciata/cappotto), metri quadri, stato attuale, opzioni (impianti, materiali).\n- Calcolo a fasce: non il prezzo esatto (impossibile senza sopralluogo) ma un RANGE credibile ('da 6.500 a 9.000 euro') con la spiegazione di cosa lo muove.\n- Lead capture: email/telefono obbligatori PRIMA di mostrare la stima. E' lo scambio: valore in cambio di contatto.\n- Invio automatico: mail all'impresa (avviso istantaneo) + email al cliente con il riepilogo e la promessa di sopralluogo.\n\n"
"STACK PRATICO: form con validazione (React/Next.js), logica di calcolo in funzioni pure e testabili, salvataggio lead su Supabase, email via Resend, tutto su Vercel.\n\n"
"REGOLE DI PRUDENZA: dichiarare sempre 'stima indicativa, non vincolante, da confermare con sopralluogo'; aggiornare i prezzi ogni 6 mesi; non promettere sconti nel configuratore.\n\n"
"VARIANTE AVANZATA: collegare l'AI — il cliente descrive il lavoro in linguaggio naturale ('devo rifare il bagno di 5 mq al terzo piano senza ascensore') e l'LLM restituisce la fascia di prezzo e le domande mancanti per affinare."),

rec("WEB-010","progetti","gestionale_cantiere","PROGETTO COMPLETO: GESTIONALE DI CANTIERE (SPECIFICA)",
"Un gestionale di cantiere e' il progetto software che un'impresa edile puo' realizzare (o far realizzare) per digitalizzare l'operativita'. Qui la specifica completa.\n\n"
"MODULI:\n1. ANAGRAFICHE: clienti, fornitori, subappaltatori, mezzi e attrezzature (con scadenze certificazioni).\n"
"2. CANTIERI: schede con dati (indirizzo, committente, CSE/CSP, valore), stato (aperto/chiuso), documenti (POS, PSC, contratto, DURC fornitori), diario di cantiere con foto.\n"
"3. PIANIFICAZIONE: squadre assegnate ai cantieri, calendario, ore lavorate, presenze, straordinari.\n"
"4. MAGAZZINO: materiali in entrata/uscita per cantiere, residui, ordini a fornitori.\n"
"5. CONTABILITA' DI CANTIERE: costi effettivi vs preventivati (il saldo vero dell'impresa), stati di avanzamento, fatture di acconto e SAL.\n"
"6. DOCUMENTALE: generazione PDF (lettere, verbali, registri), scadenziario (appalti, assicurazioni, visite mediche).\n\n"
"ARCHITETTURA CONSIGLIATA: web app responsive (in cantiere si usa il telefono), database PostgreSQL, autenticazione con ruoli (titolare, site manager, ufficio), upload file su storage cloud.\n\n"
"PERCORSO REALISTICO: partire dal MODULO 3 (presenze + diario) che risolve subito un dolore; poi documentale; poi contabilita'. Mai il big bang: il software adottato per gradi resta, quello imposto tutto insieme viene abbandonato."),

rec("WEB-011","pratica","api_ai","API E AI: COME AURATRIX PARLA CON GLI ALTRI SOFTWARE",
"Un LLM che lavora da solo ha mezzo valore: il valore pieno arriva quando dialoga con gestionali, database e strumenti.\n\n"
"MODELLI DI INTEGRAZIONE:\n1. API REST: il software chiama l'LLM come un servizio (prompt in, risposta strutturata out). Con function calling l'LLM puo' chiedere al sistema di eseguire azioni ('calcola il preventivo', 'salva il cliente').\n"
"2. RAG (Retrieval Augmented Generation): i documenti dell'impresa (capitolati, norme, listini) vengono indicizzati in un database vettoriale; quando arriva una domanda, si recuperano i pezzi rilevanti e si danno all'LLM come contesto. Cosi' il modello risponde sui DATI DELL'AZIENDA, non solo su cio' che sa di suo.\n"
"3. AGENTI: un ciclo in cui l'LLM decide i passi: riceve la richiesta, consulta strumenti (database preventivi, calendario, listino), compone la risposta. Framework: LangChain, LlamaIndex, o agenti nativi delle API moderne.\n"
"4. WEBHOOK: gli eventi di altri sistemi scatenano azioni dell'AI (arriva una mail di richiesta preventivo -> l'agente la classifica e propone una bozza di risposta).\n\n"
"REGOLE DI SICUREZZA: mai esporre la chiave API nel codice client; limitare i dati che l'AI puo' vedere per utente (un cliente non deve vedere i dati di altri); loggare tutte le chiamate; costi controllati (le API si pagano a consumo: misurare)."),

rec("WEB-012","pratica","pubblicazione","DOMINI, HOSTING, PUBBLICAZIONE E MANUTENZIONE",
"Portare un sito o un'app online e mantenerlo vivo sono competenze di base.\n\n"
"1. DOMINIO: il nome (www.aziendaedile.it). Registrazione presso registrar (es. ~10-15 euro/anno per un .it). Regole: corto, scrivibile dettandolo al telefono, meglio .it per impresa locale. Attivare WHOIS privacy.\n"
"2. HOSTING: dove vive il sito. Opzioni: statico gratuito (GitHub Pages, Cloudflare Pages), piattaforme managed (Vercel, Netlify), server virtuale (VPS, piu' controllo piu' responsabilita'). Per un'impresa edile: Vercel/Netlify sono piu' che sufficienti.\n"
"3. HTTPS: il certificato di sicurezza e' gratuito (Let's Encrypt) e obbligatorio: senza il lucchetto Google penalizza e i browser avvisano.\n"
"4. EMAIL PROFESSIONALE: info@aziendaedile.it batte aziendaedile@gmail.com in credibilita'. Spesso inclusa nell'hosting o via Google Workspace (~6 euro/mese).\n"
"5. MANUTENZIONE: aggiornamenti di sicurezza, backup automatici (regola 3-2-1: 3 copie, 2 supporti, 1 offsite), monitoraggio uptime, rinnovo dominio (perderlo per scadenza e' un classico disastro).\n\n"
"CHECKLIST DI PUBBLICAZIONE: dominio attivo e rinnovo automatico, HTTPS ok, backup attivo, analytics installata (GA4), Google Business Profile collegato al sito, email professionale funzionante, pagina privacy/cookie conforme."),

rec("WEB-013","pratica","analytics","DATA ANALYTICS: CAPIRE COSA FUNZIONA CON I NUMERI",
"Il marketing senza dati e' superstizione: l'analitica dice quali azioni portano clienti e quali soldi sprecati.\n\n"
"STRUMENTI DI BASE (gratuiti):\n- GOOGLE ANALYTICS 4: chi visita il sito, da dove arriva, cosa guarda, quanti compilano il form di contatto. Impostare gli EVENTI CHIAVE (click sul telefono, invio form, download preventivo): sono le conversioni vere.\n"
"- GOOGLE SEARCH CONSOLE: come Google vede il sito: quali ricerche portano visite, errori di indicizzazione.\n"
"- STRUMENTI SOCIAL: Instagram Insights, Meta Business Suite (copertura, interazioni, follower).\n"
"- PANNELLO GOOGLE BUSINESS: chiamate e richieste dirette dal profilo.\n\n"
"IL SISTEMA MINIMO DI MISURAZIONE PER UN'IMPRESA EDILE: foglio (o CRM) dove ogni richiesta arriva con: DATA, FONTE (Google, Instagram, passaparola, cartellone), LAVORO RICHIESTO, ESITO (sopralluogo, preventivo, firmato), FATTURATO. Una riga a richiesta. Dopo 6 mesi i numeri dicono dove investire.\n\n"
"LE METRICHE CHE CONTANO: non i like, ma: richieste al mese, tasso di risposta, preventivi inviati, tasso di conversione preventivo->lavoro, costo per lead per canale, fatturato per canale. Tutto il resto e' vanita.\n\n"
"RISPETTO PRIVACY: GA4 con mascheramento IP, banner cookie conforme, niente dati medici o sensibili nei form."),
]

def append(fname, records):
    path = os.path.join(BASE, fname)
    with open(path, "a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    total = sum(1 for _ in open(path, encoding="utf-8"))
    print(f"{fname}: +{len(records)} schede -> {total} totali")

append("marketing_edile.jsonl", marketing)
append("coding_fondamenti.jsonl", coding)
append("sviluppo_web_app.jsonl", web)
print("fatto")
