# -*- coding: utf-8 -*-
"""Corpus Impresa Edile e Appalti: gestione dell'impresa dal artigiano alla GC."""
import json, os

S = []

S.append(("costituzione_impresa",
"COSTITUZIONE E ORGANIZZAZIONE DELL'IMPRESA EDILE",
"""Le forme d'impresa nell'edilizia, dal singolo artigiano alla societa' di grandi opere:

1. FORME GIURIDICHE: impresa individuale (semplice, con patrimonio dedicato), societa' a responsabilita' limitata (S.r.l. / S.r.l.s.), societa' per azioni per i grandi gruppi, consorzi e GEIE per le grandi opere.

2. ADESIONI OBBLIGATORIE: Camera di Commercio (registro imprese), albo artigiano (per le imprese artigiane ex L. 845/1977) o albo nazionale imprese di costruzioni, cassa edile (Cassa Edile) per il personale, gestione separata INPS, INAIL.

3. REQUISITI PROFESSIONALI: per i lavori pubblici sopra le soglie, l'iscrizione all'Albo delle Societa' di Qualificazione (SOA) con categorie e classifiche (OG1 edilizia civile e industriale, OS servizi). Per i privati non e' richiesta la qualificazione ma e' fortemente consigliata.

4. ORGANIGRAMMA MINIMO: amministratore/titolare, ufficio tecnico (ingegnere o geometra), ufficio sicurezza (RSPP), addetti contabili, capocantiere, manodopera.

5. AVVIO PRATICO: scelta forma giuridica, attivita' partita IVA, SCIA inizio attivita', adesioni Cassa Edile e INAIL, valutazione dei requisiti per lavori pubblici."""))

S.append(("certificazioni",
"CERTIFICAZIONI E QUALIFICAZIONI DELL'IMPRESA",
"""Le certificazioni dimostrano la capacita' dell'impresa e aprono i mercati:

1. CERTIFICAZIONE SOA (D.Lgs 81/2008, L. 120/2011): abilita' all'esecuzione di lavori pubblici, con categorie (OG1, OG2... OS) e classifiche (I-VIII) che limitano l'importo dei contratti. Requisiti: capacita' tecnica, patrimonio, organizzazione, lavori eseguiti, assenza di condanne. Rinnovo quinquennale con collaudo tecnico.

2. SISTEMI DI GESTIONE: ISO 9001 (qualita'), ISO 14001 (ambiente), ISO 45001 (sicurezza e salute), SA 8000 (responsabilita' sociale). Non obbligatorie ma richieste sempre piu' spesso nei grandi appalti e da committenti attenti.

3. QUALIFICAZIONI REGIONALI: regioni e province autonome mantengono elenchi di imprese abilitate per lavori finanziati con fondi pubblici.

4. CERTIFICAZIONI DI PRODOTTO: marchi CE, ETA (European Technical Assessment), certificazioni di materiali e sistemi costruttivi.

5. RATING DI LEGALITA': per i lavori pubblici, il possesso di requisiti di onorabilita' e l'assenza di infiltrazioni criminali (valutazione ANAC per gare sopra soglia)."""))

S.append(("contratto_appalto",
"IL CONTRATTO DI APPALTO PRIVATO",
"""Il contratto di appalto (artt. 1655 ss. c.c.) regola i rapporti tra committente e impresa nelle opere private:

1. ELEMENTI ESSENZIALI: oggetto (opere definite), corrispettivo (a corpo, a misura, misto), tempi di esecuzione, modalita' di pagamento, responsabilita' dell'appaltatore e del committente.

2. CLAUSOLE FONDAMENTALI:
   - Obbligo del risultato: l'appaltatore risponde anche per i vizi occulti (art. 1667 c.c., garanzia decennale);
   - Collaudo (art. 1665 c.c.): accertamento di regolare esecuzione, con garanzia decennale sui difetti gravi;
   - Penale per ritardo (art. 1662 c.c.): puo' essere ridotta dal giudice se sproporzionata;
   - Riserve di proprietà e caparre di garanzia;
   - Clausole penali per inadempimento.

3. VARIANTI IN CORSO D'OPERA: regolate per iscritto, con computo e preventivo allegati; chi non documenta perde la possibilita' di richiedere il pagamento.

4. SUBAPPALTO: consentito se autorizzato dal committente (art. 1676 c.c.); il subappaltatore risponde verso il committente entro un anno dal pagamento del committente al appaltatore.

5. RISOLUZIONE: per inadempimento grave (art. 1671 c.c.) con risarcimento del danno; la risoluzione va sempre comunicata per iscritto."""))

S.append(("gare_pubbliche",
"LE GARE PUBBLICHE E IL CODICE DEI CONTRATTI",
"""Il D.Lgs 36/2023 (Codice dei contratti pubblici) regola l'affidamento dei lavori pubblici:

1. PROCEDURE: aperta (bando pubblico), ristretta, qualificazione, negoziata, affidamento diretto sotto soglia.

2. CRITERI DI AGGIUDICAZIONE: prezzo piu' basso o offerta economicamente piu' vantaggiosa (OEPV con punteggi tecnico-economici). Le gare complesse usano l'OEPV con graduatorie.

3. FASI: indizione (bando o lettera di invito) -> offerta -> apertura -> aggiudicazione provvisoria -> verifica requisiti -> aggiudicazione definitiva -> contratto -> esecuzione -> collaudo.

4. ELEMENTI DELL'OFFERTA: offerta tecnica (progetto esecutivo, cronoprogramma, organigramma, misure di sicurezza, piano di gestione), offerta economica (computo, prezzi unitari, ribasso), documentazione amministrativa (DURC, certificazioni, visure).

5. PORTALI: i bandi sopra soglia comunitaria sono pubblicati sui portali nazionali e europei; i lavori sotto soglia sui portali regionali e sull'albo fornitori dei committenti.

6. OSTACOLI E SANZIONI: offerte anomale (valutazione di congruita'), clausole sociali, divieto di subappalto non autorizzato, responsabilita' per false dichiarazioni."""))

S.append(("personale",
"GESTIONE DEL PERSONALE DI CANTIERE",
"""La manodopera e' il cuore dell'impresa edile e il suo costo piu' delicato:

1. CCNL EDILIZIA: contratto collettivo nazionale (artigiano, industria, cooperative), con mansioni (operaio comune, qualificato, specializzato, capocantiere, direttore di cantiere), livelli e minimi retributivi. Aggiornato con rinnovi periodici.

2. POSIZIONE GIURIDICA: assunzione con lettera di assunzione (tempo indeterminato, determinato, a tempo parziale), Distacco ai sensi del D.Lgs 136/2016 per i lavoratori distaccati transnazionali, appalti interni.

3. ADESIONI: iscrizione Cassa Edile (come previsto dai CCNL), versamenti contributivi, denunce Unilav/Uniemens, DURC (Documento Unico di Regolarita' Contributiva) obbligatorio per i lavori pubblici e spesso richiesto dai privati.

4. FORMAZIONE SICUREZZA: formazione generale (4 ore), specifica (8 ore per rischio basso, 12 medio, 16 alto), aggiornamento (6 ore/5 anni), formazione conduzione macchine (carrellisti, gruisti, piattaforme), abilitazioni elettriche (CEI 11-27).

5. CONTROLLI: ispezioni INL (Ispettorato Nazionale del Lavoro) su contratti, sicurezza, contributi; sanzioni pesanti per lavoro in nero e irregolarita' contributive."""))

S.append(("sicurezza_organizzativa",
"SICUREZZA ORGANIZZATIVA DELL'IMPRESA",
"""La sicurezza non e' solo cantiere: e' sistema aziendale:

1. SOGGETTI AZIENDALI: datore di lavoro (responsabile ultimo), RSPP (responsabile servizio prevenzione e protezione, interno o esterno), RLS (rappresentante lavoratori sicurezza), addetti emergenze e primo soccorso, medico competente (sorveglianza sanitaria).

2. DOCUMENTI OBBLIGATORI: DVR (Documento di Valutazione dei Rischi) aggiornato almeno ogni 3 anni, piano di emergenza ed evacuazione, programma di formazione, verbali di riunione periodica (almeno annuale), registro infortuni e prevenzione.

3. FORMAZIONE CONTINUA: aggiornamenti normativi, procedure, uso DPI, gestione emergenze. La formazione va documentata (verbali, firme, programmi).

4. SORVEGLIANZA SANITARIA: visita medica periodica in funzione del rischio, giudizi di idoneita' (idoneo, idoneo con prescrizioni, inidoneita' temporanea o permanente), libretto sanitario.

5. D.LGS 81/2008: il Testo Unico stabilisce l'organizzazione minima; le sanzioni penali colpiscono datore, RSPP e delegati secondo la catena delle responsabilita'.

6. CULTURA DELLA SICUREZZA: il sistema funziona se e' parte del processo produttivo, non un adempimento burocratico: check-list pre-cantiere, briefing quotidiani, analisi degli infortuni."""))

S.append(("assicurazioni",
"ASSICURAZIONI DELL'IMPRESA EDILE",
"""Le coperture assicurative proteggono l'impresa, i lavoratori e i terzi:

1. RC PROFESSIONALE (RCO/RCT): copre i danni causati da errori professionali di progettisti e direzione lavori; massimali tipici 500.000 - 2.000.000 €. Obbligatoria per molte categorie (ingegneri, architetti per pratiche pubbliche).

2. RC IMPRESA (RC generale): copre i danni a terzi causati dall'attivita' (danni a cose e persone fuori dal cantiere); massimali tipici 1-5 milioni €.

3. DECENNALE POSTUMA (All Risk): copre i danni al manufatto per 10 anni dalla consegna, incluse le opere realizzate dall'impresa (garanzia decennale ex art. 1667 c.c.). Obbligatoria per molti lavori pubblici e sempre piu' richiesta nei privati.

4. INFORTUNI E MALATTIE: assicurazione INAIL obbligatoria integrata da polizze integrative per i rischi professionali (invalidita' permanente, decesso).

5. CAUZIONI E FIDEJUSSIONI: per lavori pubblici (cauzione provvisoria 2%, definitiva 10%) e per i contratti privati (garanzie per acconti, garanzie a garanzia del contratto).

6. CARICO CANTIERE: copertura dei materiali, delle macchine e dei mezzi di cantiere (furto, incendio, danni da trasporto)."""))

S.append(("contabilita_impresa",
"CONTABILITA', FISCALITA' E CASH FLOW DI CANTIERE",
"""La gestione economica dell'impresa edile e' diversa da quella industriale per la durata dei cicli:

1. REGIMI FISCALI: forfettario (per imprese con ricavi sotto la soglia, con coefficiente di redditivita' e obblighi ridotti), regime ordinario (partita IVA con IVA, IRPEF/IRAP, contabilita' semplificata o ordinaria).

2. IVA IN EDILIZIA: ordinaria 22% (beni), 10% (lavori di costruzione, ristrutturazione, manutenzione straordinaria), 4% (prima casa), con reverse charge per subappalti e subentri.

3. CASH FLOW DI CANTIERE: il diagramma dei flussi (incassi vs esborsi) mostra il fabbisogno finanziario: gli acconti coprono i materiali, i SAL coprono le lavorazioni, il saldo copre il margine. Il capocantiere e l'ufficio tecnico devono allineare produzione, contabilita' e incassi.

4. RITENUTE E RIVALSE: ritenuta d'acconto 8% (per prestazioni a privati non abituali), rivalsa INPS 4% sui contratti di appalto (art. 28 L. 1338/1962).

5. GESTIONE DEL CREDITO: il recupero crediti e' il punto critico dell'edilizia (pagamenti medi 90-180 giorni); strumenti: fideiussioni, cambiali, pignoramenti, decreto ingiuntivo.

6. BILANCIO D'ESERCIZIO: per le societa' di capitali, il bilancio rileva il patrimonio, il conto economico e la nota integrale; gli indici di bilancio (ROE, ROA, current ratio) guidano la valutazione di banche e committenti."""))

S.append(("costruzione_costi",
"I COSTI DI COSTRUZIONE PER TIPOLOGIA EDILIZIA",
"""I costi di costruzione variano notevolmente per tipologia, standard e zona. Valori indicativi italiani 2024-2026 (€/m² di superficie lorda, chiavi in mano):

1. RESIDENZIALE: edilizia economica 900-1.200; standard 1.200-1.700; medio-alto 1.700-2.300; lusso 2.300-3.500+.

2. COMMERCIALE: uffici standard 1.200-1.800; direzionali 1.800-2.500; retail 800-1.200.

3. INDUSTRIALE: capannoni prefabbricati 400-700; con uffici 600-900; complessi logistici 500-800.

4. PUBBLICI: scuole 1.500-2.200; ospedali 2.500-3.500; palestre 1.200-1.800.

5. COMPONENTI DEL COSTO: struttura 15-25%, tamponamento e copertura 20-30%, impianti 20-35%, finiture 15-25%, oneri generali e utile 10-20%.

6. FATTORI DI VARIAZIONE: zona (Nord > Centro > Sud per costi di manodopera), stagionalita', accessibilita' del cantiere, standard dei materiali, vincoli (sismici, paesaggistici, culturali).

7. SOVRAPPREZZI: demolizioni 30-80 €/m²; bonifica amianto 20-50 €/m²; rinforzo antisismico 150-400 €/m²."""))

S.append(("sviluppo_commerciale",
"SVILUPPO COMMERCIALE E MARKETING TECNICO DELL'IMPRESA",
"""L'impresa edile cresce con un marketing tecnico che valorizza la competenza:

1. PORTAFOGLIO ORDINI: il mix tra piccoli lavori (cash flow rapido) e grandi opere (margine) bilancia i rischi; il target e' avere 6-12 mesi di produzione coperta.

2. REFERENZE E CANTIERI APERTI: i cantieri di qualita' visitabili sono il miglior biglietto da visita; organizzare open-house con clienti e progettisti.

3. MARKETING TECNICO: schede di dettaglio dei lavori eseguiti (foto, computi, tempi), articoli tecnici, presenza a fiere del settore (Made Expo, Saie), partnership con progettisti e rivenditori di materiali.

4. OFFERTA COMMERCIALE: preventivi dettagliati con computo, capitolato, tempi, condizioni; trasparenza come strategia di vendita; follow-up sistematico.

5. DIGITALE: sito con portfolio, gestione recensioni, presenza sui portali di gara e sui social tecnici (LinkedIn, Instagram per i cantieri).

6. FEDELTA' DEL CLIENTE: post-cantiere (visita di controllo a 12 mesi, manutenzione programmata) trasforma il cliente in promotore."""))

os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "impresa_appalti_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus impresa edile e appalti a cura di Kimi",
    "url": "",
}
out = []
for i, (tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"IMP-{i:02d}", "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = os.path.join('Edilizia_Pack', 'parsed', 'impresa_appalti.jsonl')
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede impresa -> {os.path.abspath(path)}")
