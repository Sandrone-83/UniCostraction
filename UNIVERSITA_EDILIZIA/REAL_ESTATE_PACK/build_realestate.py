# -*- coding: utf-8 -*-
"""REAL_ESTATE_PACK: mercato immobiliare, valutazione, investimenti, gestione locativa."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Mercato", "Il mercato immobiliare: dinamiche, cicli, indicatori",
 "Il mercato immobiliare è ciclico (cicli lunghi 8-15 anni) e locale: il valore di un appartamento dipende dal micro-mercato (quartiere, città) più che dal trend nazionale; gli indicatori chiave: compravendite, prezzi nominali/reali, tempi di vendita, tassi mutui, dinamica demografica e occupazionale del territorio.",
 "Fonti: ISTAT (catasto compravendite), OMI (Agenzia Entrate: quotazioni zonali ufficiali), portali immobiliari (indici prezzi), banche (osservatori mutui); il metodo professionale: analisi comparativa OMI della zona + osservazione diretta dei comparabili reali (annunci e transazioni).",
 "Decisioni di acquisto/vendita, investimenti, stime rapide.",
 "Chi legge i cicli evita di comprare sul picco 'perché tutti comprano' e vendere nel panico: il timing psicologico è il contrario di quello corretto.",
 "Le quotazioni OMI sono fasce larghe (minime/medie/massime) da interpretare: la media non è il prezzo di un immobile specifico.",
 "Accesso ai dati OMI: gratuito; report privati (Idealista, Immobiliare): gratuiti; consulenza: a tariffa.",
 "Acquisto in periferia 'in ascesa' nel 2007: l'immobile è tornato sopra il prezzo pagato solo nel 2024; lo stesso capitale su zona centrale ha recuperato in 6 anni: la LOCALIZZAZIONE batte il timing.",
 "Normativa OMI (DPR 138/1998); statistiche ISTAT; regolamento Agenzia Entrate.",
 "La prima legge del real estate: si guadagna quando si COMPRA (al giusto prezzo), non quando si vende."),
s("Valutazione", "La valutazione immobiliare: i tre metodi",
 "La stima professionale usa tre metodi: comparativo (da immobili simili venduti — il metodo principe per residenziale), costruttivo (valore = terreno + costo di ricostruzione - deperimento, utile per immobili speciali), reddituale (valore = rendita attesa / tasso di capitalizzazione, obbligatorio per gli immobili a reddito e di uso produttivo).",
 "Comparativo: 3-5 comparabili reali, aggiustamenti per differenze (piano, ascensore, stato, box, esposizione), esito per intervallo; costruttivo: terreno da OMI/comparabili + costo di costruzione a corpo (1.200-2.000 €/m² secondo finiture) - deperimento per età/stato (tabella curvatura); reddituale: V = R / r con r da mercato (immobili residenziali locati: 2,5-4,5% tipico).",
 "Perizie per mutui, successioni, divisioni, contenziosi, decisioni d'investimento.",
 "Il metodo comparativo ben fatto dà un intervallo difendibile: è la base di ogni trattativa seria.",
 "I comparabili 'di annuncio' non sono transazioni: il prezzo di vendita medio è il 5-15% sotto il prezzo richiesto nei mercati normali.",
 "Costo perizia professionale (geometra/perito): 300-1.500 €; perizia asseverata per giudizio: 1.500-4.000 €.",
 "Stima comparativa per un trilocale: 3 comparabili reale tra 178.000 e 195.000 €, aggiustamenti per piano e box: stima 172.000-182.000 €; trattativa conclusa a 176.000 € con venditore e compratore entrambi 'convinti dal metodo'.",
 "Standard OIV (Organismo Italiano di Valutazione) e IVS (International Valuation Standards); prassi UNI.",
 "Regole: mai stimare un solo metodo se i dati consentono il confronto; dichiarare sempre ipotesi e fonti."),
s("Trattativa", "Prezzo, valore e trattativa: come si negozia un immobile",
 "Il prezzo richiesto è un'offerta, il valore di mercato è un intervallo, il prezzo di chiusura è il risultato della trattativa; la negoziazione immobiliare funziona su: informazione (chi sa di più vince), tempistica (chi ha fretta perde), emotività (la casa si 'sente', la trattativa è tecnica).",
 "Strategie: compratore — preparare i comparabili e le voci di miglioramento (ristrutturazione da fare: costi a consuntivo da imprese), presentare offerte motivate (non 'si abbassi'), usare i tempi (offerte a fine trattativa); venditore — quotare entro la fascia OMI, preparare l'immobile (home staging leggero, documenti pronti), valutare l'offerta sul netto (costi e tempi).",
 "Acquisti e vendite tra privati, tramite agenzia, trattative complesse.",
 "La trattativa preparata porta a risparmi/guadagni del 3-10% rispetto all'accettazione immediata: sulla casa media sono decine di migliaia di euro.",
 "La trattativa spinta ('pessimo offerente') rischia di far saltare la trattativa su un immobile giusto: il migliore è nemico del buono.",
 "Costo: tempo e informazione (comparabili gratuiti sui portali); mediazione: vedi scheda agenzia.",
 "Acquisto con offerta motivata da computo ristrutturazione (38.000 € documentati): sconto ottenuto 25.000 €; il venditore ha accettato perché l'offerta era 'tecnica' e non 'capricciosa'.",
 "Nessuna norma cogente; prassi negoziale e deontologia degli agenti.",
 "Regola d'oro: la miglior leva negoziale è l'alternativa concreta (altro immobile, altro compratore) — senza alternativa, la flessibilità è minima."),
s("Agenzia", "L'agenzia immobiliare: ruolo, provvigioni, normativa",
 "L'agente immobiliare (L. 39/1989) è il mediatore professionale iscritto al Ruolo (CAM): mediazione tra venditore e compratore o locatore e locatario, con provvigione (mediazione) dovuta quando conclude l'affare; l'iscrizione al Ruolo e la polizza RC sono obblighi di legge.",
 "Meccanismi: incarico di vendita (esclusivo o non), ricerca acquirenti, visite, proposte, preliminare, rogito; la provvigione: tipicamente 2,5-3% + IVA su compratore e venditore (o come pattuito), dovuta a conclusione dell'affare; l'agente deve verificare la regolarità documentale dell'immobile (visura, abitabilità) e informare entrambe le parti.",
 "Compravendite e locazioni tramite agenzia: la maggioranza del mercato italiano.",
 "L'agente bravo velocizza il mercato: prezzo giusto da subito, filtro delle visite, assistenza documentale.",
 "Il conflitto d'interesse è strutturale (l'agente guadagna chiudendo): la fiducia si costruisce su trasparenza e track record.",
 "Provvigione media: 3% del prezzo per parte (valore medio casa 250.000 €: ~7.500 € + IVA per parte); servizi accessori (perizie, pratiche): a parte.",
 "Vendita con agenzia esclusiva e prezzo corretto da subito: venduta in 6 settimane a pieno prezzo; la stessa casa, 18 mesi prima con 3 agenzie senza esclusiva e prezzo gonfiato: zero offerte e prezzo finale -12%.",
 "L. 39/1989; regolamento attuativo; codice deontologico FIAIP/Confabitare.",
 "Consiglio LLM: valutare l'agenzia come si valuta un fornitore (track record, esclusività, strategia di prezzo), non come un nemico da aggirare."),
s("Mutuo", "Il mutuo immobiliare: tassi, spread, surroga",
 "Il mutuo ipotecario finanzia l'acquisto: a tasso fisso (certezza, in genere più caro inizialmente), variabile (Euribor + spread, rischio/ opportunità), misto; i parametri: LTV (loan to value, max 80% tipico), TAEG (costo totale), spread banca, assicurazioni vincolate (PPI), penali di estinzione.",
 "Meccanismi: istruttoria (busta paga, documenti immobile), perizia bancaria (LIM), delibera, atto notarile con ipoteca; la surroga (portabilità): spostare il mutuo a tasso più basso presso altra banca senza costi notarili (legge 40/2007); la rinegoziazione: ridiscutere spread con la banca attuale; l'estinzione parziale: ridurre rata o durata.",
 "Acquisti residenziali, investimenti, ristrutturazioni (mutui agevolati prima casa con garanzie Consap per giovani, condizioni da verificare annualmente).",
 "Il mutuo giusto sostiene l'acquisto senza strangolarlo: la rata sostenibile è entro 1/3 del reddito familiare netto.",
 "Il tasso 'fisso a vita' comprato sul picco dei tassi costa carissimo nei decenni successivi se il ciclo scende; il variabile in salita può sforare i piani di budget.",
 "Tassi indicativi 2025 (da verificare): fisso ~3-3,8%, variabile Euribor+1,2-1,8%; perizia: 200-400 €; istruttoria: 0-1% (spesso azzerata).",
 "Mutuo variabile preso nel 2022 a Euribor+1,5%: con la salita dei tassi, la rata è passata da 850 a 1.320 € in 18 mesi; la surroga a fisso 3,4% (2024) ha riportato la rata a 980 € con zero spese notarili.",
 "Normativa bancaria (TUB, Testo Unico Bancario); legge 40/2007 (surroga); prassi Banca d'Italia.",
 "Regole: confrontare SEMPRE TAEG e non il tasso nominale; chiedere simulazioni di stress +2% sul variabile; valutare la surroga a ogni calo significativo dei tassi."),
s("Locazione breve", "Locazione breve e affitti turistici: mercato e regole",
 "La locazione breve (affitti turistici, Airbnb-style) è un mercato cresciuto enormemente: rendimenti potenziali superiori alla locazione tradizionale (in zone turistiche anche del doppio), ma con carico gestionale (check-in, pulizie, manutenzione rapida) e regole in continuo stringimento (CIN obbligatoria, limiti comunali e regionali, tassazione dedicata).",
 "Requisiti: Codice Identificativo Nazionale (CIN), comunicazione al Comune, norme igienico-sanitarie, tassazione (cedolare secca 21%/26% su locazioni brevi secondo regimi vigenti); gestione operativa: piattaforme, smart lock, pulizie coordinate, pricing dinamico; il calcolo del rendimento reale: occupazione media (50-75% nelle zone forti) × tariffa notte × 365 - costi (pulizie, utenze, tasse, manutenzione, piattaforma 15-18%).",
 "Investitori, second case, imprese di property management breve.",
 "In zona turistica forte il breve batte il lungo anche del 50-80% di incasso annuo.",
 "La saturazione di molte città (Venezia, Firenze, centro Roma) ha portato stop e limiti: il business dipende dalla regolamentazione locale che cambia.",
 "Ammobiliamento B&B: 15.000-50.000 € per unità; gestione terzi: 20-30% degli incassi.",
 "Monolocale in centro storico gestito in breve: occupazione 68%, incasso 24.000 €/anno vs 13.200 della locazione lunga tradizionale; costi e tasse hanno ridotto il surplus reale a ~6.000 €/anno, con lavoro gestionale notevole.",
 "L. 431/1998 (diversivo turistico); D.Lgs 79/2011 (turismo); ordinanze comunali (sempre da verificare).",
 "Domanda d'investimento: il surplus del breve vs il lungo GIUSTIFICA il lavoro extra? Nelle zone medie spesso non basta."),
s("Aste", "Le aste immobiliari: opportunità e procedure",
 "Le aste giudiziarie vendono immobili pignorati con sconti potenziali del 20-50% rispetto al mercato, ma con rischi: immobili occupati (svuotamento a carico dell'aggiudicatario), vizi e abusi, spese di custodia, riscatto del credito ipotecario, procedura lenta.",
 "Meccanismo: asta telematica (fallimentare o esecutiva), offerta minima (tipicamente 75-80% del prezzo base, ribassabile), deposito cautelativo (10%), aggiudicazione, decreto di trasferimento, liberazione dell'immobile (se occupato: esecuzione forzata che richiede mesi/anni); verifiche pre-offerta: fascicolo di vendita (visura, perizia, stato occupazione, eventuale locazione registrata 'a protezione').",
 "Investitori con pazienza e capitale, chi cerca sconti su immobili da ristrutturare.",
 "Il risparmio vero può superare il 30% anche considerando i lavori: il mercato delle aste premia la competenza.",
 "L'immobile occupato può richiedere anni per essere liberato: il risparmio si mangia in tempo e procedura.",
 "Costi: deposito (restituito se non aggiudicati), imposte ridotte (da verificare per regime), custodia pre-possesso, liberazione.",
 "Aggiudicazione con sconto 35% su appartamento occupato da locatario moroso: liberazione durata 14 mesi; il conto economico finale ha reso il 18% annuo sul capitale investito comunque, ma solo perché il capitale poteva restare fermo.",
 "Codice della crisi (D.Lgs 14/2019) per le aste fallimentari; codice procedura civile esecutiva.",
 "Regola: mai offrire su un'asta senza aver letto TUTTO il fascicolo e stimato costo e tempo della liberazione."),
s("Property management", "Il property management: gestire patrimoni locativi",
 "Il property management professionale gestisce immobili di terzi: locazione (cercare inquilini, contratti, incassi), manutenzione (tecnici di fiducia, pronto intervento), contabilità (cedolare, registrazioni), amministrazione condominiale coordinata; il gestore trasforma il patrimonio immobiliare da secondo lavoro a investimento passivo.",
 "Servizi: sourcing inquilini (visura, garanzie), contrattualistica e registrazione, incasso canoni e solleciti, manutenzione programmata (caldaie, guaine, verniciature), reportistica annuale per il proprietario; il compenso: 8-15% dei canoni annuali (residenziale) o quota fissa + gestione tecnica.",
 "Proprietari con più unità, eredità complesse, investitori non residenti, piccole società patrimoniali.",
 "Il patrimonio gestito professionamente deperisce meno, rende di più e non ruba tempo: il costo del gestore è recuperato in manutenzione preventiva e riduzione sfitto.",
 "Il gestore mediocre è un costo puro: selezionare su reportistica e referenze, non sulla sola percentuale.",
 "Compenso gestione: 8-15% canoni; il risparmio da manutenzione programmata: stime 10-20% dei costi di guasto.",
 "Portafoglio di 6 appartamenti passato da autogestione a gestore professionale: sfitto ridotto da 45 a 12 giorni/anno medi, manutenzioni costate il 15% in meno grazie alla programmazione, e il proprietario ha recuperato ~10 ore/mese.",
 "L. 431/1998; normativa fiscale locazioni; deontologia dei gestori (ordini e associazioni).",
 "Il patrimonio immobiliare è un'azienda: chi lo tratta come hobby ne raccoglie i risultati di hobby."),
s("Investimenti", "Gli investimenti immobiliari: rendite, cash flow, leva",
 "L'immobile come investimento si misura su: rendita lorda (canone/valore), rendita netta (al netto di spese, tasse, vuoto), cash flow mensile (entrata - rata mutuo - costi), plusvalenza (rivalutazione del capitale); la leva finanziaria (mutuo) amplifica sia i guadagni che le perdite.",
 "Calcolo d'investimento: valore d'acquisto + costi (10-15% tra imposte, notaio, ristrutturazione) = capitale investito; rendita netta annua = canone - spese - vuoto - tasse; il ritorno = rendita netta / capitale investito (target sano residenziale: 3-5% netto più rivalutazione); la leva: con il 50% di mutuo a tasso inferiore alla rendita, il ROE si moltiplica; attenzione al cash flow: la rata non deve mangiare la rendita.",
 "Acquisti per affitto, valorizzazioni, BRRRR (buy-renovate-rent-refinance-repeat).",
 "L'immobile con leva e cash flow positivo si ripaga da solo: l'investitore conserva il capitale e accumula patrimonio.",
 "La leva su immobile a rendita bassa è una trappola: il cash flow negativo mangia il patrimonio ogni mese.",
 "Costi accessori d'investimento: 10-15% del valore di acquisto; la rendita netta media residenziale italiana: ~2-4% lordo (dati OMI/mercato).",
 "Trilocale acquistato 160.000 € con 40.000 € di ristrutturazione e costi, locato a 720 €/mese con mutuo che lascia 90 €/mese di cash flow positivo dopo spese: in 15 anni il mutuo è estinto e l'immobile rende 700 €/mese liberi.",
 "Normativa fiscale locazioni; regolamentazione bancaria mutui.",
 "La domanda madre: 'questo immobile, col MIO capitale e QUESTA rata, mi lascia soldi in tasca ogni mese?' — se la risposta è no, è una scommessa, non un investimento."),
s("Marketing immobiliare", "Il marketing immobiliare: vendere l'immobile al meglio",
 "Un immobile venduto bene si presenta bene: fotografie professionali (luce naturale, grandangolo corretto), home staging leggero (sgombro, neutralizzazione, tessili), descrizione onesta e dettagliata, prezzo di lancio corretto (i primi 3 settimani di esposizione concentrano l'interesse), presenza sui portali giusti con annuncio completo.",
 "Checklist vendita: documenti pronti (visura, catastale, abitabilità, APE), foto professionali (300-500 € sessione), home staging (da 500 € leggero a 3.000-8.000 € completo), annuncio con planimetria quotata e certificazioni energetiche, gestione visite (orari, ordine), valutazione feedback dopo 30 giorni (se nessuna offerta: il prezzo parla).",
 "Vendite di privati, sviluppatori, gestori di portafogli.",
 "L'immobile presentato bene vende più in fretta e a prezzo pieno: il mercato premia chi rispetta il tempo del compratore.",
 "Il sovrapprezzo 'tanto trattiamo' si traduce in mesi di esposizione e sconto finale maggiore: il prezzo giusto da subito è la strategia migliore.",
 "Costo marketing vendita: 500-2.000 € (foto, staging leggero, visure); il costo dell'esposizione lunga: mensilità perse + sconto finale.",
 "Appartamento fermo 8 mesi a 265.000 €: ripresentato a 245.000 € con foto professionali e staging leggero: venduto in 5 settimane a 242.000 €; il proprietario ha incassato prima e ha realizzato 23.000 € in più della traiettoria precedente (prezzo pieno - mesi persi).",
 "Nessuna norma cogente (pubblicità veritiera); codice deontologico agenti.",
 "La regola del mercato: il prezzo è la strategia di marketing — tutto il resto ne è la conferma."),
]

README = """# REAL_ESTATE_PACK — Mercato immobiliare, valutazione e investimenti

**Facoltà:** FACOLTA_GESTIONE_SISTEMA · **Livello:** L2 · **Schede:** {n}

## Contenuto
Il ramo immobiliare dell'università: dinamiche e cicli del mercato, i tre metodi di
valutazione (comparativo, costruttivo, reddituale), trattativa e negoziazione,
agenzia immobiliare (L. 39/89), mutui (fisso/variabile/surroga), locazioni brevi
e turistiche, aste giudiziarie, property management, investimenti (rendite, cash
flow, leva finanziaria) e marketing immobiliare.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza su acquisti/vendite, valutazioni rapide, analisi di
investimenti locativi, conversazioni su mutui e aste. I dati di mercato (tassi,
rendimenti, quotazioni) sono puntuali al 2025 e vanno aggiornati con le fonti
ufficiali (OMI, Banca d'Italia) al momento dell'uso.
""".format(n=len(DATA))

COURSE = """corso: "Mercato immobiliare, valutazione e investimenti"
facolta: "FACOLTA_GESTIONE_SISTEMA"
livello: "L2"
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
