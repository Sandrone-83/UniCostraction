# -*- coding: utf-8 -*-
"""Digitale_Marketing_Pack: marketing edile e fondamenti di informatica/coding."""
import json, os

M = []

# ============ MARKETING EDILE (12) ============
M.append(("brand","brand_identity",
"BRAND IDENTITY EDILE: NOME, LOGO, POSIZIONAMENTO",
"""Il marchio di un'impresa edile e' una promessa di fiducia:

1. POSIZIONAMENTO: scegliere il posto nella mente del cliente: economico (preventivi bassi), qualità (finiture e garanzie), specialista (restauri, energia, lusso), velocità (chiavi in mano rapido), locale (radicamento territoriale). Il posizionamento guida tutto: servizi offerti, prezzi, tono della comunicazione, tipo di cliente.

2. NAMING: nome breve (2-3 sillabe), pronunciabile, memorizzabile, disponibile come dominio .it/.com e sui social; evitare nomi generici ('Costruzioni Rossi') se si punta a crescere; tipologie: founder name (Rossi Building), descrittivo (BioCasa), evocativo (Auratrix: matrice+aurum), inventato.

3. LOGO E VISUAL: semplice, riconoscibile in piccolo (favicon, avatar social), funziona in bianco e nero; colori: blu (fiducia), verde (sostenibilità), arancio/rosso (energia cantiere), antracite (eleganza); tipografia sans-serif per i digital, evitare troppi effetti; usare simboli costruttivi riconoscibili (tetti, gru, livelle) ma con twist distintivo.

4. BRAND STORYTELLING: la storia dell'impresa (fondazione, valori, cantieri simbolo, persone) raccontata in modo autentico; 'dal 1987' funziona se vero; foto del team reale, non stock.

5. COERENZA: brand book minimo (colori esadecimali, font, tono voce) applicato a tutto: carta intestata, magliette, mezzi (i furgoni sono pubblicità mobile), cartelli cantiere, social, sito."""))
M.append(("brand","brand_creazione",
"COME SI CREA UN MARCHIO: PROCESSO E COSTI",
"""Dal concept al marchio registrato:

1. PROCESSO: ricerca (analisi competitor e naming disponibili) -> concept (posizionamento, valori, personalità) -> naming e slogan -> visual identity (logo, colori, font) -> brand book -> applicazioni (sito, social, stampa, cantiere) -> lancio.

2. STRUMENTI: naming (brainstorming, dizionari, verifica disponibilità su Agenzia delle Entrate-DEM, PEC, social), logo (designer professionista 500-3.000 euro, piattaforme 99designs/Fiverr, AI generative come bozza), colori (Adobe Color, Coolors), font (Google Fonts gratuiti).

3. COSTI INDICATIVI: brand completo da studio 3.000-15.000 euro; budget basso: 500-2.000 euro con freelancer + strumenti online; budget zero: Canva + AI + tempo proprio (risultato mediocre).

4. REGISTRAZIONE MARCHIO: UIBM (Ufficio Italiano Brevetti e Marchi) o EUIPO per l'Europa (marchio comunitario ~850 euro); classi di riferimento: 19 (materiali da costruzione), 37 (costruzioni), 42 (servizi tecnici); verifica precedenti per non infrangere.

5. ERRORE TIPICO: cambiare logo ogni anno (diluisce il riconoscimento); il brand si costruisce con la coerenza nel tempo: 3-5 anni prima di valutare restyling."""))
M.append(("digital","sito_seo",
"SITO WEB E SEO LOCALE PER IMPRESE EDILI",
"""Il sito e' la vetrina che converte: obiettivo = contatti (preventivi), non solo visite:

1. STRUTTURA MINIMA: home (chi siete, cosa fate, perché voi, CTA 'Richiedi preventivo'), servizi (ristrutturazioni, cappotto, nuove costruzioni - una pagina per servizio per SEO), portfolio/progetti (foto prima/dopo con dettagli), chi siamo (storia, team, certificazioni), recensioni, contatti (form, telefono, WhatsApp, mappa).

2. SEO LOCALE (fondamentale per edilizia): ottimizzare per 'impresa edile [città]', 'ristrutturazione bagno [zona]'; Google Business Profile (ex My Business) completo con foto cantieri, recensioni, post; citazioni coerenti (Nome-Indirizzo-Telefono identici ovunque); pagine per zona servita.

3. TECNICA: sito veloce (immagini compresse WebP, hosting italiano, HTTPS), responsive (mobile-first), schema markup LocalBusiness; dominio .it con nome brand; CMS: WordPress (flessibile), Webflow/Squarespace (più semplici), o sviluppato su misura.

4. CONTENUTI CHE RANKEANO: guide utili ('Quanto costa ristrutturare un bagno a [città] 2026', 'Detrazione 50%: cosa sapere'), portfolio dettagliati, FAQ; aggiornare il blog mensilmente.

5. CONVERSIONE: ogni pagina con CTA chiara (form preventivo, bottone WhatsApp, telefono cliccabile); tracking (Google Analytics 4, Search Console, Meta Pixel)."""))
M.append(("social","social_edile",
"SOCIAL MEDIA MARKETING PER L'EDILIZIA",
"""I social giusti per un'impresa edile: Instagram e Facebook primi, YouTube/TikTok in crescita, LinkedIn per il B2B:

1. INSTAGRAM: il canale principale (visivo). Content pillar: prima/dopo (i renaissance dei cantieri), time-lapse lavorazioni, dietro le quinte (team, camion, cantiere al tramonto), educativo (consigli, errori da evitare, materiali), social proof (recensioni, clienti soddisfatti), reveal (consegne chiavi in mano). Formati: Reel (30-60 sec, hook nei primi 2 secondi), carosello (prima/dopo swipe), Storie (giornata di cantiere, sondaggi).

2. FACEBOOK: community locale + ads; gruppi di quartiere (partecipare, non solo pubblicizzare), pagina con recensioni, eventi (open house cantieri).

3. YOUTUBE: video lunghi (10-20 min) per SEO: 'Come costruiamo una casa in 200 giorni', 'Ristrutturazione completa: tutti i passaggi'; Shorts per discovery; YouTube e' il secondo motore di ricerca.

4. TIKTOK: time-lapse, ASMR edile, trend adattati; pubblico più giovane ma sempre più acquirenti di prima casa.

5. LINKEDIN: per committenti business (uffici, retail, PA): case history, certificazioni, articoli tecnici."""))
M.append(("video","video_marketing",
"VIDEO MARKETING: DAL CANTIERE AL REEL VIRALE",
"""Il video e' il formato che converte di più nel settore costruzioni:

1. FORMULA DEL REEL EDILE: hook visivo (2 sec: il cantiere peggiore o il risultato finale), trasformazione (before/after), processo (time-lapse o step), prova sociale (cliente che parla), CTA ('commenta PREVENTIVO'). Durata ideale: 15-45 secondi; vertical 9:16 per Reel/TikTok/Shorts.

2. STRUMENTI: smartphone recente + gimbal (DJI OM) + luce portatile; editing: CapCut (gratuito, mobile), DaVinci Resolve (gratuito, desktop), Premiere Pro; musica trend da libreria Instagram/TikTok; sottotitoli sempre (80% guarda senza audio).

3. TIPOLOGIE CHE FUNZIONANO: time-lapse completi (giorni compressi in 30 sec), '3 errori che fanno alzare il preventivo', 'come installiamo il cappotto passo-passo', 'un giorno in cantiere con il drone', reaction del cliente alla consegna, timelapse demolizione.

4. PUBLICITA' VIDEO (ADS): video testimonianza 30-60 sec per Meta Ads (targeting per zona, età 30-55, interessi casa/ristrutturazione); video portfolio per retargeting; YouTube Ads su ricerca locale.

5. CALENDARIO: 3-4 contenuti a settimana per i social; 1 video lungo al mese per YouTube; batching: girare un pomeriggio = 2 settimane di contenuti."""))
M.append(("ads","paid_ads",
"PUBBLICITA' A PAGAMENTO: META ADS, GOOGLE ADS E LEAD GENERATION",
"""Gli ads comprano visibilità immediata: il punto e' il costo per lead:

1. META ADS (Facebook/Instagram): campagne lead generation con modulo integrato (nome, telefono, servizio richiesto, zona) o traffico verso WhatsApp; targeting per località (raggio 20-40 km), età 30-60, interessi; budget indicativo 10-30 euro/giorno; creatività: video before/after con hook forte.

2. GOOGLE ADS: campagne Search ('ristrutturazioni [città]', 'impresa edile [zona]') con keyword locali; budget 15-50 euro/giorno; Quality Score; landing page dedicata per servizio (non la home!).

3. LOCAL SERVICE ADS (Google): per artigiani/PMI: si paga per contatto telefonico verificato; badge 'Google Guaranteed'; ottimo per emergenze (idraulica, elettrico) e ristrutturazioni.

4. MISURAZIONE: costo per lead (CPL) indicativo edilizia: 15-80 euro; tasso conversione lead->sopralluogo 30-50%, sopralluogo->contratto 20-40%; quindi il CPL sostenibile dipende dal valore medio del contratto (margine per acquisizione 3-8%).

5. ERRORI DA EVITARE: boostare post a caso (senza targeting), senza pixel/tracking, senza rispondere in 5 minuti ai lead (la velocità di risposta converte 10 volte di più), landing lenta o senza recensioni."""))
M.append(("contenuti","content_strategy",
"CONTENT MARKETING EDILE: EDUCARE PER VENDERE",
"""Chi insegna, vende: il contenuto posiziona l'esperto:

1. PILLAR E CLUSTER: 4 pilastri (ristrutturazione, energia/risparmio, normative/bonus, dietro le quinte) con articoli/video specifici (cluster) che rimandano al servizio; esempio: pilar 'Bonus casa' -> articoli su detrazione 50%, conto termico, cappotto -> CTA preventivo.

2. FORMATI: articoli SEO sul sito (1500+ parole), guide scaricabili (checklist 'Come scegliere l'impresa edile' in cambio dell'email), webinar gratuiti ('Ristrutturare senza errori 2026'), newsletter mensile, podcast (interviste a fornitori e clienti).

3. CALENDARIO EDITORIALE: mese 1: bonus e detrazioni (Q1), mese 2: manutenzione primavera, mese 3: case study; sincronizzare con la stagionalità del settore (gennaio: ripresa, primavera: cantieri, settembre: ristrutturazioni pre-inverno).

4. RICICLARE I CONTENUTI: un video YouTube -> reel Instagram -> articolo sito -> carosello LinkedIn -> email -> citazione per ads; massimo rendimento dal materiale girato in cantiere.

5. AUTORITA': citare fonti normative (NTC, DPR 380, ENEA), dati (ISTAT), certificazioni proprie; rispondere alle domande dei clienti (le FAQ diventano contenuti)."""))
M.append(("cliente","recensioni_referral",
"RECENSIONI, REFERRAL E REPUTAZIONE ONLINE",
"""Nel settore edile la parola di bocca e' ancora la regina — ma ora e' digitale:

1. GOOGLE REVIEWS: obiettivo minimo 50 recensioni con media 4,6+; chiedere la recensione a fine lavoro (QR code sul cantiere, messaggio WhatsApp con link diretto); rispondere a TUTTE le recensioni (grazie + dettaglio del progetto); gestire le negative con professionalità (offerta di soluzione, non discussione pubblica).

2. PORTALI: Tripadvisor? no. Trustpilot, Habitissimo, Edilnet, Houzz: presenza selettiva, risposta rapida ai preventivi richiesti (entro 1 ora), profilo completo con portfolio.

3. REFERRAL PROGRAM: incentivare i clienti soddisfatti a presentare amici (sconto 500-1.000 euro o buono Amazon per referente e referrato); il referral ha il tasso di conversione più alto (60-70%) e costo quasi zero.

4. TESTIMONIANZE VIDEO: 60 secondi di cliente che racconta il progetto, il problema risolto, perché ha scelto voi; usare in ads, sito, social.

5. REPUTAZIONE DI CRISI: prontuario per emergenze (difetto post-consegna, recensione negativa, incidente): rispondere in 2 ore, assumere il problema, proporre soluzione concreta e tempi; la trasparenza protegge il brand."""))
M.append(("fiere","fiere_eventi",
"FIERE, EVENTI E OPEN HOUSE DI CANTIERE",
"""Il marketing offline funziona ancora, integrato col digitale:

1. FIERE DI SETTORE: SAIE (Bologna), MADE Expo (Milano), Restructura (Torino), Klimahouse (Bolzano); obiettivi: lead (badge scanner), brand, contatti fornitori; budget stand 3.000-30.000 euro; preparare: video loop, mock-up materiali, iPad con portfolio, contatto rapido dei lead (email in 24h).

2. OPEN HOUSE (CANTIERE APERTO): trasformare un cantiere in vetrina: giornata dedicata per clienti potenziali e progettisti (weekend), visite guidate dal titolare, brochure e preventivi sul posto, social e ads locali per promuovere l'evento.

3. EVENTI LOCALI: sponsorizzazioni squadre di calcio, sagre, associazioni di quartiere (brand awareness locale); parlare a convegni e ordini professionali (posizionamento esperto).

4. PARTNERSHIP: studi di architettura, studi tecnici, showroom materiali (bagno, cucine), agenzie immobiliari: reciproco passaggio clienti, eventi congiunti, co-marketing.

5. MATERIALE: cartellini cantiere professionali (logo, recensione Google QR, 'Cantiere aperto su appuntamento'), brochure, biglietti da visita di qualità, gadget utili (metro, livella con logo)."""))
M.append(("agenti","agenti_ai",
"AGENTI AI E AUTOMATION PER L'IMPRESA EDILE",
"""Gli agenti artificiali lavorano per l'impresa: il nuovo 'impiegato digitale':

1. COSA PUÒ FARE UN AGENTE AI: rispondere alle richieste di preventivo sul sito/WhatsApp (qualificando il lead: zona, servizio, budget, tempi), inviare preventivi pre-compilati da template, fare follow-up automatici sui lead freddi, gestire il calendario dei sopralluoghi, redigere offerte e computi preliminari, monitorare scadenze (DURC, visite mediche, gare), analizzare i preventivi perdenti.

2. STRUMENTI: chatbot con LLM (ChatGPT/Claude API, Voiceflow, Botpress, GPT integrato in sito WhatsApp Business), automazioni (Make/Zapier/n8n), CRM con AI (HubSpot, Pipedrive + AI), agenti verticali per settore.

3. COME COSTRUIRE UN AGENTE SEMPLICE (no-code): definire il flusso conversazionale -> connettere LLM con prompt di sistema (ruolo: 'sei l'assistente di Auratrix...') -> integrare WhatsApp/sito -> testare con domande reali -> misurare tasso di qualificazione -> iterare; piattaforme: Stack AI, Relevance AI, n8n.

4. LIMITI E ATTENZIONE: l'agente qualifica e risponde, non sostituisce il preventivista tecnico; privacy GDPR (consenso per trattamento dati); sempre un umano nel loop per le trattative complesse.

5. ROI: un agente che risponde 24/7 qualifica 30-50% in più di lead rispetto al 'rispondiamo domani'."""))
M.append(("kpi","kpi_marketing",
"KPI, BUDGET E MISURAZIONE DEL MARKETING EDILE",
"""Solo ciò che si misura si migliora:

1. FUNNEL EDILE: visitatori sito/social -> contatti (form, telefonate, WhatsApp) -> sopralluoghi -> preventivi -> contratti; ogni passaggio ha un tasso di conversione da monitorare.

2. KPI ESSENZIALI: lead per mese, costo per lead (per canale), tasso di risposta (entro 5 minuti), tasso sopralluogo->preventivo (obiettivo 80%+), tasso preventivo->contratto (obiettivo 25-40%), valore medio contratto, CAC (costo acquisizione cliente) = spesa marketing / clienti acquisiti, margine medio per contratto, ROI marketing = (margine - spesa) / spesa.

3. ATTRIBUZIONE: chiedere sempre al cliente 'come ci ha trovati?' (anche con campo nel form); Google Analytics per il sito; numeri di telefono diversi per campagne; CRM che traccia la fonte del lead.

4. BUDGET INDICATIVO: impresa piccola (fatturato <1M): 2-5% del fatturato; media (1-10M): 1-3%; con focus crescita aggressiva: 5-8%; ripartizione tipo: 40% ads, 25% contenuti/video, 15% sito/SEO, 10% fiere/eventi, 10% materiali.

5. DASHBOARD: foglio semplice o Looker Studio con i KPI mensili; revisione mensile: cosa ha portato lead qualificati, cosa tagliare, cosa raddoppiare."""))
M.append(("casi","casi_studio_marketing",
"CASI STUDIO: COME CRESCONO LE IMPRESE EDILI PIÙ VISIBILI",
"""Schemi ricorrenti di successo osservabili:

1. L'IMPRESA 'INFLUENCER': un titolare che documenta tutto su YouTube/Instagram (Mr. Build It? no - esempi italiani: 'Ristrutturiamo', 'Cantiere Facile'); schema: video settimanale costante per 2+ anni, trasparenza sui costi, lead che arrivano da soli; svantaggio: richiede tempo e capacità comunicative.

2. IL PORTFOLIO CHE VENDE: impresa che investe nella fotografia professionale di ogni progetto finito (prima/dopo con drone); il sito diventa il venditore; ads minimi, conversione altissima.

3. IL REFERRAL ENGINE: nessun ads, solo recensioni Google (200+) e referral incentivati; crescita lenta ma solida e margine alto (zero costi di acquisizione).

4. LA SPECIALIZZAZIONE: 'l'impresa del cappotto' o 'il restauro del legno': dominano una nicchia con contenuti educativi; quando il cliente cerca quello specifico, sono i primi.

5. LA COMBINAZIONE VINCENTE (per chi parte ora): Google Business Profile ottimizzato + recensioni attive + Instagram con 3 reel/settimana + Google Ads su keyword locali + risposta ai lead in 5 minuti con WhatsApp. Budget 1.000-2.000 euro/mese, risultati visibili in 3-6 mesi."""))
M.append(("errori","errori_marketing",
"I 15 ERRORI DI MARKETING PIÙ COSTOSI NELL'EDILIZIA",
"""Gli errori che fanno perdere soldi e clienti:

1. NON RISPONDERE o rispondere dopo ore (il lead e' andato al concorrente); 2. non chiedere la recensione a fine lavoro; 3. sito obsoleto o assente; 4. foto fatte male (cantiere sporco in foto); 5. pubblicizzare il prezzo basso (attrae clienti peggiori); 6. dire 'facciamo tutto' (nessuno ricorda); 7. boostare post senza strategia; 8. non tracciare da dove arrivano i clienti; 9. cambiare logo/nome ogni anno; 10. parlare solo di se stessi ('noi dal 1980') invece che dei problemi del cliente; 11. ignorare le recensioni negative; 12. non avere preventivi scritti professionali (il marketing muore nel momento del preventivo); 13. farsi pagare solo a fine lavoro senza acconti (cash flow che blocca il marketing); 14. non aggiornare il portfolio (il cantiere finito e' la prova); 15. delegare il marketing a chi non conosce il settore edile.

LA REGOLA D'ORO: il miglior marketing per un'impresa edile e' un cliente soddisfatto che parla di voi — tutto il resto amplifica questa voce."""))

# ============ CODING FONDAMENTI (8) ============
C = []

C.append(("informatica","come_funziona_computer",
"COME FUNZIONA UN COMPUTER: HARDWARE E SISTEMA OPERATIVO",
"""Le basi fisiche e logiche della macchina:

1. HARDWARE: CPU (processore: esegue istruzioni, clock GHz, core), RAM (memoria volatile, veloce, GB), storage (SSD/HDD, persistente), scheda madre (collega tutto), GPU (grafica e calcolo parallelo), alimentatore, periferiche (input: tastiera, mouse; output: monitor, stampante).

2. BINARIO E DATI: tutto e' rappresentato in bit (0/1); 8 bit = 1 byte; i numeri in binario, il testo in codifiche (ASCII, UTF-8: 'A' = 65); immagini (pixel, RGB), suoni (campionamento), video (fotogrammi compressi).

3. SISTEMA OPERATIVO (OS): Windows, macOS, Linux; gestisce hardware, processi (programmi in esecuzione), memoria, file system (gerarchia cartelle, permessi), rete; il kernel e' il cuore, la shell e' l'interfaccia (grafica o terminale).

4. SOFTWARE: sistemi (OS), applicativi (browser, editor), linguaggi (interpretati come Python/JS vs compilati come C++/Rust); i programmi sono istruzioni che la CPU esegue ciclo per ciclo (fetch-decode-execute).

5. TERMINALE/COMMAND LINE: navigazione (cd, ls/dir, mkdir), file, processi (task manager, ps, kill); conoscere il terminale e' il superpotere di ogni programmatore."""))
C.append(("coding","linguaggi_paradigmi",
"LINGUAGGI DI PROGRAMMAZIONE E PARADIGMI",
"""I linguaggi sono strumenti con filosofie diverse:

1. TIPI: compilati (C, C++, Rust: tradotti in eseguibile veloce), interpretati (Python, JavaScript: eseguiti riga a riga, più lenti ma flessibili), a macchina virtuale (Java, C#: bytecode portabile), dichiarativi (SQL, HTML).

2. PARADIGMI: procedurale (funzioni e sequenze: C, Python), a oggetti (classi, istanze, ereditarieta', incapsulamento: Java, C#, Python), funzionale (funzioni pure, immutabilita': Haskell, parti di JS/Python), event-driven (risposta a eventi: JS nei browser).

3. LINGUAGGI CHIAVE: Python (semplice, data science, AI, backend), JavaScript (il linguaggio del web, frontend e Node.js backend), Java/C# (enterprise, app), C++ (performance, giochi, sistemi), SQL (database), Go/Rust (sistemi moderni).

4. SINTASSI DI BASE (concetti comuni): variabili, tipi (stringhe, numeri, booleani), operatori, condizioni (if/else), cicli (for, while), funzioni (parametri, return), liste/array, dizionari/map (chiave-valore), classi e oggetti.

5. COME IMPARARE: partire da Python o JavaScript; scrivere piccoli programmi subito (calcolatrice, gestione lista); progetti reali piccoli; documentazione ufficiale e community."""))
C.append(("coding","algoritmi_strutture",
"ALGORITMI, STRUTTURE DATI E PENSIERO COMPUTAZIONALE",
"""Il pensiero computazionale risolve problemi in modo sistematico:

1. PENSIERO COMPUTAZIONALE: scomposizione (dividere in sotto-problemi), riconoscimento pattern, astrazione (ignorare i dettagli non necessari), progettazione algoritmi (passi precisi per risolvere).

2. ALGORITMI FONDAMENTALI: ricerca (lineare, binaria - halving log n), ordinamento (bubble, selection, merge sort, quicksort - O(n log n)), complessita' (notazione O grande: O(1), O(n), O(n²), O(log n), O(n log n)).

3. STRUTTURE DATI: array/liste (indicizzate), pile (LIFO: push/pop), code (FIFO: enqueue/dequeue), liste collegate, alberi (gerarchie, ricerca binaria), grafi (nodi e archi: reti sociali, mappe), tabelle hash (ricerca O(1)).

4. RICORSIONE: funzione che chiama se stessa (fattoriale, fibonacci, tree traversal); caso base e caso ricorsivo.

5. DEBUGGING: leggere errori, stampare variabili intermedie, debugger (breakpoint, step), rubber duck (spiegare il codice a un'anatra di gomma), dividere il problema."""))
C.append(("web","internet_reti_api",
"INTERNET, RETI E API: COME LE APP COMUNICANO",
"""Le fondamenta del web e delle app:

1. INTERNET: rete di reti; protocollo TCP/IP (pacchetti, indirizzi IP, routing); DNS (traduzione nomi dominio -> IP); World Wide Web (HTTP/HTTPS su TCP, HTML come documenti ipertestuali); client-server (browser chiede, server risponde).

2. HTTP: metodi (GET leggere, POST creare, PUT aggiornare, DELETE), status code (200 OK, 301 redirect, 404 non trovato, 500 errore server), header, body; HTTPS = HTTP criptato (TLS/SSL, certificati).

3. API REST: l'app espone endpoint (URL) per operazioni su risorse (GET /preventivi/123); formato JSON per scambio dati; autenticazione (API key, token JWT, OAuth2); API di terzi (Google Maps, Stripe pagamenti, OpenAI).

4. FRONTEND VS BACKEND: frontend (HTML struttura, CSS stile, JavaScript interattività: React, Vue, Angular) vs backend (logica, database, API: Node.js, Python/Django/Flask, PHP/Laravel, Java/Spring).

5. SICUREZZA BASE: password hashate (bcrypt), HTTPS, SQL injection (parametrizzare query), XSS (sanitizzare input), CSRF token, principio del minimo privilegio."""))
C.append(("database","database_sql",
"DATABASE: SQL, MODELLI E DESIGN",
"""I database sono il cuore delle applicazioni:

1. RELAZIONALI (SQL): tabelle con righe e colonne, chiave primaria (ID univoco), chiavi esterne (collegamenti tra tabelle); SQL: SELECT, INSERT, UPDATE, DELETE, JOIN (INNER, LEFT), WHERE, GROUP BY, ORDER BY; ACID (atomicità, consistenza, isolamento, durabilità); MySQL, PostgreSQL, SQLite, SQL Server.

2. MODELLAZIONE: entità (cliente, preventivo, cantiere) e relazioni (1-n, n-n); normalizzazione (1NF, 2NF, 3NF) per evitare ridondanze; ERD (diagrammi entità-relazione).

3. NON RELAZIONALI (NoSQL): documenti (MongoDB: JSON flessibile), chiave-valore (Redis: cache veloce), colonne (Cassandra), grafi (Neo4j); usati per scalabilità e dati non strutturati.

4. OPERAZIONI: CRUD (Create, Read, Update, Delete), transazioni, backup, indici (velocizzare ricerche), viste, stored procedure; ORM (Object-Relational Mapping: SQLAlchemy, Prisma) traducono oggetti in query.

5. ESEMPIO EDILE: tabelle Clienti(ID, nome, telefono), Preventivi(ID, cliente_id, importo, stato), Cantieri(ID, preventivo_id, data_inizio, stato); query: 'SELECT c.nome, p.importo FROM Clienti c JOIN Preventivi p ON p.cliente_id = c.id WHERE p.stato = \"accettato\"'."""))
C.append(("devops","git_cloud_devops",
"GIT, CLOUD E DEVOPS: GESTIRE IL SOFTWARE",
"""Come si sviluppa e mantiene software in team:

1. VERSION CONTROL (Git): repository (cartella tracciata), commit (istantanee con messaggio), branch (linee parallele di sviluppo), merge (unione), push/pull con repository remoto (GitHub, GitLab, Bitbucket); workflow: feature branch -> pull request -> review -> merge su main; comandhi base: git init, add, commit, push, pull, checkout, merge.

2. CLOUD COMPUTING: IaaS (macchine virtuali: AWS EC2, Azure VM), PaaS (piattaforme gestite: Heroku, Vercel, Firebase), SaaS (software pronto: Google Workspace); scalabilità (su/giù), pay-per-use; container (Docker: pacchetto con codice + dipendenze), orchestrazione (Kubernetes).

3. DEVOPS E CI/CD: integrazione continua (test automatici a ogni commit), deployment continuo (pubblicazione automatica); pipeline (GitHub Actions, GitLab CI): build -> test -> deploy; ambienti (development, staging, production).

4. TESTING: unit test (funzioni singole), integration test (componenti insieme), E2E test (flussi utente: Playwright, Cypress); TDD (Test Driven Development: prima il test, poi il codice).

5. MONITORAGGIO: log (registri eventi), error tracking (Sentry), analytics, uptime monitoring; gestione incidenti."""))
C.append(("metodo","agile_progetti_software",
"METODOLOGIE AGILE, SCRUM E GESTIONE PROGETTI SOFTWARE",
"""Come si organizza lo sviluppo:

1. WATERFALL VS AGILE: cascata (requisiti -> design -> sviluppo -> test, rigido) vs iterativo/incrementale (flessibile, feedback frequente); manifesto Agile (2001): individui e interazioni > processi; software funzionante > documentazione esaustiva; collaborazione col cliente > contratto negoziazione; rispondere al cambiamento > seguire il piano.

2. SCRUM: ruoli (Product Owner: cosa e perche'; Scrum Master: facilita; Team: sviluppa); sprint (iterazioni 1-4 settimane); cerimonie (planning, daily standup 15 min, review/demo, retrospettiva); artifact (product backlog, sprint backlog, increment).

3. KANBAN: lavagna visiva con colonne (Da fare, In corso, Test, Fatto) e limiti di lavoro in corso (WIP); flusso continuo, no iterazioni fisse; adatto a manutenzione e ops.

4. USER STORY E MVP: 'Come [ruolo] voglio [funzione] per [beneficio]' (come cliente voglio richiedere un preventivo online per risparmiare tempo); MVP (Minimum Viable Product): la versione minima da testare sul mercato; prototipo -> feedback -> iterazione.

5. STRUMENTI: Jira, Trello, Notion, GitHub Projects; documentazione tecnica (README, API docs), code review tra pari."""))
C.append(("no_code","no_code_ai_coding",
"NO-CODE, LOW-CODE E AI CODING: COSTRUIRE SENZA (QUASI) CODICE",
"""La democratizzazione dello sviluppo:

1. NO-CODE: strumenti visuali per creare app senza programmare: siti (Webflow, Wix, Framer, Squarespace), app mobili (Glide, Adalo, Bubble), automazioni (Zapier, Make, n8n), database (Airtable), form (Typeform); limiti: personalizzazione, scalabilità, lock-in del fornitore.

2. LOW-CODE: piattaforme per sviluppare con pochissimo codice (OutSystems, Mendix, Microsoft Power Apps); usate dalle aziende per accelerare.

3. AI CODING (pair programming con AI): GitHub Copilot, Cursor, Claude, ChatGPT scrivono codice da descrizione in linguaggio naturale; usi: generare bozze, spiegare codice, scrivere test, debugging, tradurre tra linguaggi; workflow umano-in-the-loop: l'AI propone, il programmatore verifica (i modelli allucinano API e generano bug).

4. PROMPT EFFICACE PER CODING: contesto (linguaggio, librerie, obiettivo), esempio input/output, vincoli (gestire errori, sicurezza), chiedere test; iterare per rifiniture.

5. QUANDO USARE COSA: MVP veloce -> no-code; prototipo AI -> AI coding + revisione; prodotto core di business -> sviluppo tradizionale (controllo, performance, proprietà del codice); per l'impresa edile: CRM cantieri in Airtable, sito in Webflow, preventivatore con AI assistita in Python."""))

# ============ SVILUPPO WEB/APP (8) ============
W = []

W.append(("webdev","sito_da_zero",
"COSTRUIRE UN SITO WEB: FRONTEND, BACKEND E DEPLOY",
"""Anatomia di un sito moderno costruito da zero:

1. FRONTEND (quello che vede l'utente): HTML5 (struttura: header, nav, section, form), CSS3 (stile: flexbox, grid, responsive, variabili), JavaScript (interattività: eventi, fetch API, DOM manipulation); framework: React (componenti, stato, virtual DOM), Vue, Svelte; build tool: Vite; design system: Tailwind CSS.

2. BACKEND (il motore nascosto): server (Node.js/Express, Python/FastAPI, PHP/Laravel) che riceve richieste, logica applicativa, collegamento al database (PostgreSQL), autenticazione utenti (sessioni o JWT), API REST.

3. FULLSTACK: combinazione frontend+backend; framework fullstack: Next.js (React), Nuxt (Vue), Django; hosting del backend: Railway, Render, VPS (Hetzner, AWS).

4. DEPLOY: frontend su CDN (Vercel, Netlify - gratuito per progetti piccoli), dominio (registrazione .it ~10 euro/anno), DNS (Cloudflare), HTTPS (certificato gratuito Let's Encrypt); backup del database.

5. CMS (alternativa rapida): WordPress (il 40% dei siti, temi e plugin: Elementor, WooCommerce per e-commerce), gestionale per non-programmatori; headless CMS (Strapi, Sanity) come backend per frontend custom."""))
W.append(("mobile","app_mobile",
"APP MOBILE: NATIVA, IBRIDA E PROGRESSIVE WEB APP",
"""Le strade per un'app sul telefono:

1. NATIVA: Swift (iOS) e Kotlin (Android): massima performance e accesso a tutte le funzionalità del dispositivo (camera, GPS, notifiche); costo alto (due codici da mantenere); usata per app complesse e ad alta interazione.

2. CROSS-PLATFORM: un solo codice per entrambe: Flutter (Google, Dart: UI performanti, molto adottato), React Native (Meta, JavaScript: ecosistema React); performance vicine al nativo per la maggior parte delle app; framework come Expo accelerano lo sviluppo.

3. PROGRESSIVE WEB APP (PWA): sito web che funziona come app (installabile, offline, notifiche push via service worker); vantaggi: un solo codice web, niente store; limiti: accesso ridotto a hardware e notifiche su iOS.

4. NO-CODE MOBILE: Glide, Adalo, FlutterFlow (low-code con Flutter sotto); adatte per MVP e app interne aziendali.

5. PUBBLICAZIONE: App Store (Apple, fee 99 $/anno, review) e Google Play (25 $ una tantum); PWA: nessuna store, link diretto; per un'impresa edile: PWA o FlutterFlow per l'app del cantiere (foto lavori, check-list, report)."""))
W.append(("ai","integrare_ai_app",
"INTEGRARE L'AI NELLE APP: LLM, EMBEDDING E AGENTI",
"""Come aggiungere intelligenza a siti e app:

1. API LLM: chiamate HTTP a modelli come GPT-4, Claude, Gemini (OpenAI API, Anthropic API); pattern: system prompt (ruolo, contesto, regole) + user prompt (domanda) + response; parametri (temperatura: creatività vs precisione); streaming (risposta parola per parola); costi per token.

2. USE CASE EDILI: chatbot preventivi sul sito; redazione automatica di descrizioni computo da dati strutturati; analisi di contratti e capitolati (estrazione clausole); riepilogo verbali; traduzione documenti; generazione FAQ dai documenti aziendali.

3. RAG (Retrieval Augmented Generation): il modello risponde basandosi sui TUOI documenti: suddividere i documenti in chunk -> embedding (vettori numerici del significato, OpenAI text-embedding) -> vector database (Pinecone, Qdrant, pgvector) -> ricerca semantica dei chunk rilevanti -> prompt con contesto + domanda; vantaggio: risposte sui dati privati senza allucinare.

4. AGENTI: LLM + strumenti (tools: ricerca web, calcolatrice, database, email) in loop: l'agente decide di chiamare un tool, legge il risultato, itera; framework: LangChain, LlamaIndex, AutoGen, CrewAI; esempio: agente che legge il bando di gara, redige l'offerta, la invia via email.

5. LIMITI E COSTI: allucinazioni (sempre verificare), privacy GDPR (non mandare dati sensibili a API esterne senza accordi DPA), costi API (scalano con l'uso), latenza."""))
W.append(("progetti","software_edili",
"10 PROGETTI SOFTWARE PRATICI PER L'IMPRESA EDILE",
"""Idee concrete di software da costruire (o far costruire) con il coding:

1. GESTIONALE PREVENTIVI: database clienti + generatori di preventivi da template + PDF; stack: Python/Flask + SQLite + bootstrap; valore: ore risparmiate ogni settimana.

2. APP CANTIERE (PWA): foto georeferenziate, check-list sicurezza giornaliera, note vocali, report PDF settimanale al cliente; stack: React + Firebase (auth + storage).

3. SCADENZIARIO AZIENDALE: DURC, visite mediche, rinnovi polizze, scadenze fiscali; notifiche email/WhatsApp; stack: Airtable + Make o Python + cron.

4. CRM CANTIERI: tracciamento lead (da dove arrivano), stati (contatto->sopralluogo->preventivo->contratto), follow-up automatici; stack: HubSpot free o custom in Notion/Airtable.

5. CONFIGURATORE CAPPOTTO: input (mq, zona climatica, spessore) -> output (materiale, costo indicativo, risparmio energetico, detrazione); stack: React + formule UNI/TS 11300.

6. COMPARATORE PREZZI MATERIALI: scraping (con rispetto dei termini) o inserimento manuale dei listini fornitori -> confronto; stack: Python + Pandas.

7. CHATBOT SITO/WHATSAPP: agente AI che qualifica i lead (servizio, zona, tempi, budget) e prenota il sopralluogo; stack: Botpress o GPT API + WhatsApp Business API.

8. DASHBOARD ENERGETICA: consumi dei cantieri/uffici da bollette, produzione fotovoltaico, CO2 risparmiata; stack: Grafana + InfluxDB o semplici Google Sheets.

9. FIRMA DIGITALE DOCUMENTI: invio contratti/POS da firmare digitalmente (DocuSign API o Firma con SPID), archiviazione; stack: Node.js + API.

10. BANDI TRACKER: monitoraggio gare (scraping portali appalti + filtri per categorie SOA) con alert email; stack: Python + BeautifulSoup + cron; NOTA: rispettare i termini di servizio dei portali."""))
W.append(("carriera","imparare_coding",
"PERCORSO DI STUDIO: IMPARARE A PROGRAMMARE DA ZERO",
"""La roadmap realistica per un professionista dell'edilizia (o chiunque):

1. MESE 1-2 (FONDAMENTA): Python base (variabili, condizioni, cicli, funzioni, liste, dizionari) su freeCodeCamp o Python.org; piccoli script: calcolatrice preventivi, analisi computo CSV; capire il terminale e Git.

2. MESE 3-4 (WEB): HTML/CSS (freeCodeCamp Responsive Web Design), JavaScript base; costruire il sito dell'impresa da zero o con React; capire come funzionano hosting e domini; pubblicare su Vercel/Netlify.

3. MESE 5-6 (DATI E BACKEND): SQL (database preventivi/clienti), API (Python FastAPI), automazioni (Make/Zapier); progetto: mini-CRM o gestionale preventivi funzionante.

4. MESE 7+ (SPECIALIZZAZIONE): AI integration (API LLM, RAG sui propri documenti), oppure app mobile (FlutterFlow/PWA), oppure no-code avanzato (Bubble per SaaS); ogni progetto reale di cantiere diventa un caso software.

5. RISORSE: freeCodeCamp (gratis), The Odin Project (gratis, fullstack), CS50 Harvard (edX, gratis), documentazione ufficiale, YouTube (italiano: 'imparare a programmare'); community: Discord, Stack Overflow, Reddit r/learnprogramming.

6. CONSIGLIO CHIAVE: impara risolvendo problemi REALI dell'impresa (preventivi, scadenziario, cantiere): la motivazione resta alta e il valore e' immediato; 1 ora al giorno per 6 mesi = competenza operativa."""))
W.append(("sicurezza_inf","sicurezza_digitale",
"SICUREZZA INFORMATICA E PRIVACY PER L'IMPRESA",
"""Le minacce digitali e le difese essenziali:

1. MINACCE COMUNI: phishing (email truffa che sembra banca/fornitore: verificare sempre mittente e link), ransomware (cripta i file e chiede riscatto: backup!), malware, furto credenziali, ingegneria sociale (chiama fingendosi tecnico IT).

2. DIFESE BASE: password uniche lunghe (password manager: Bitwarden, 1Password), MFA (autenticazione a due fattori ovunque: app, non SMS), aggiornamenti sistema e software, antivirus/EDR, firewall, backup 3-2-1 (3 copie, 2 supporti, 1 offsite/cloud), VPN per accessi remoti.

3. PRIVACY E GDPR (D.Lgs 196/2003, Reg. UE 2016/679): registro trattamenti, consenso per marketing, informativa, diritti interessati (accesso, cancellazione), notifica breach 72h, DPO se necessario; attenzione a clienti e dipendenti (dati sanitari in sicurezza cantieri).

4. SICUREZZA SITO E APP: HTTPS obbligatorio, aggiornare CMS/plugin (WordPress), WAF (Cloudflare), protezione form (CAPTCHA), backup automatici, non esporre dati sensibili nel codice (chiavi API in variabili ambiente).

5. PER L'IMPRESA EDILE: proteggere i dati dei clienti (contratti, planimetrie catastali), i preventivi (valore commerciale), i progetti; formare i dipendenti al phishing (e' la causa dell'80% delle violazioni)."""))
W.append(("stack","stack_tecnologico_2026",
"LO STACK TECNOLOGICO CONSIGLIATO PER PARTIRE (2026)",
"""Le scelte pragmatiche per costruire software oggi:

1. SITO VETRINA: Next.js (React) o Astro (veloce) + Tailwind CSS + hosting Vercel/Netlify; CMS headless (Sanity) se contenuti frequenti; costo: dominio 10-20 euro/anno + hosting gratuito/sviluppo.

2. WEB APP (gestionale, CRM): Frontend React/Next.js; backend Supabase (database PostgreSQL + auth + storage + realtime, gratuito tier) o Firebase; deploy Vercel; alternativa low-code: Bubble/Glide per MVP.

3. APP MOBILE: FlutterFlow (no-code/low-code) o React Native/Expo se si vuole codice; PWA se si vuole semplicità.

4. AI INTEGRATION: OpenAI API o Anthropic API (GPT-4/Claude); framework: Vercel AI SDK, LangChain; vector DB: pgvector (in Supabase) o Pinecone; pattern RAG per documenti aziendali.

5. AUTOMATION: n8n (self-hosted, gratuito) o Make/Zapier per collegare form, email, CRM, WhatsApp; monitoraggio errori: Sentry; analytics: Plausible/Umami (privacy-friendly).

6. REGOLA D'ORO: scegliere tecnologie con grande community e documentazione; evitare framework troppo nuovi o esoterici; il codice deve poter essere mantenuto anche da altri (o da te fra 2 anni)."""))

# ============ writers ============
def write(path, recs):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f"scritti {len(recs)} -> {os.path.abspath(path)}")

out_m = []
for i, (cat, tema, titolo, testo) in enumerate(M, 1):
    out_m.append({"id": f"MAR-{i:03d}", "categoria": cat, "tema": tema, "title": titolo, "text": testo.strip(),
                  "source": "marketing_edile_kimi", "license": "Sintesi didattica originale Kimi (pubblico dominio)",
                  "commercial_ok": True, "attribution": "Corpus marketing edile a cura di Kimi", "url": ""})
write(os.path.join('Digitale_Marketing_Pack', 'parsed', 'marketing_edile.jsonl'), out_m)

out_c = []
for i, (cat, tema, titolo, testo) in enumerate(C, 1):
    out_c.append({"id": f"COD-{i:03d}", "categoria": cat, "tema": tema, "title": titolo, "text": testo.strip(),
                  "source": "coding_fondamenti_kimi", "license": "Sintesi didattica originale Kimi (pubblico dominio)",
                  "commercial_ok": True, "attribution": "Corpus coding fondamenti a cura di Kimi", "url": ""})
write(os.path.join('Digitale_Marketing_Pack', 'parsed', 'coding_fondamenti.jsonl'), out_c)

out_w = []
for i, (cat, tema, titolo, testo) in enumerate(W, 1):
    out_w.append({"id": f"WEB-{i:03d}", "categoria": cat, "tema": tema, "title": titolo, "text": testo.strip(),
                  "source": "sviluppo_web_app_kimi", "license": "Sintesi didattica originale Kimi (pubblico dominio)",
                  "commercial_ok": True, "attribution": "Corpus sviluppo web/app a cura di Kimi", "url": ""})
write(os.path.join('Digitale_Marketing_Pack', 'parsed', 'sviluppo_web_app.jsonl'), out_w)
