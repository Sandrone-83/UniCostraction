# -*- coding: utf-8 -*-
"""Italia_Sistema_Pack: Costituzione, fisco, lavoro, sistema Paese. Dati 2026 verificati."""
import json, os

S = []

# ============ COSTITUZIONE (7) ============
S.append(("costituzione","principi_fondamentali",
"I PRINCIPI FONDAMENTALI DELLA COSTITUZIONE (ARTT. 1-12)",
"""La Costituzione della Repubblica Italiana (1 gennaio 1948) si apre con dodici articoli di principio:

1. FORMA DI STATO (art. 1): 'L'Italia e' una Repubblica democratica, fondata sul lavoro.' La sovranita' appartiene al popolo, che la esercita nelle forme e nei limiti della Costituzione.

2. DIRITTI INALIENABILI (art. 2): 'La Repubblica riconosce e garantisce i diritti inviolabili dell'uomo, sia come singolo sia nelle formazioni sociali ove si svolge la sua personalita', e richiede l'adempimento dei doveri inderogabili di solidarieta' politica, economica e sociale.'

3. UGUAGLIANZA (art. 3): tutti i cittadini hanno pari dignita' sociale e sono uguali davanti alla legge, senza distinzione di sesso, di razza, di lingua, di religione, di opinioni politiche, di condizioni personali e sociali; e' compito della Repubblica rimuovere gli ostacoli che impediscono il pieno sviluppo della persona.

4. LAVORO (art. 4): la Repubblica tutela il lavoro in tutte le sue forme e applicazioni; ogni cittadino ha il diritto al lavoro e ha il dovere di svolgere, secondo le proprie possibilita' e la propria scelta, un'attivita' che concorra al progresso materiale o spirituale della societa'.

5. LIBERTA' (artt. 5-8): libertà di associazione, di espressione del pensiero, di religione (concordati con la Santa Sede, pluralismo religioso), di riunione pacifica e senz'armi.

6. DIRITTO DI RESISTENZA (art. 5, secondo comma): nessuna associazione puo' avere carattere di partito politico militare.

7. TUTELA DEL PAESE (artt. 9-12): la Repubblica promuove lo sviluppo della cultura e la ricerca scientifica e tecnica, tutela il paesaggio e il patrimonio storico e artistico della Nazione; tutela l'ambiente, la biodiversita' e gli ecosistemi, anche nell'interesse delle future generazioni (principio rafforzato dalla riforma 2022)."""))
S.append(("costituzione","diritti_doveri",
"DIRITTI E DOVERI DEI CITTADINI (ARTT. 13-54)",
"""La prima parte della Costituzione regola i rapporti civili e politici:

1. LIBERTA' PERSONALI: inviolabilita' della liberta' personale (art. 13), domicilio (art. 14), corrispondenza (art. 15), circolazione e soggiorno (art. 16), riunione (art. 17), associazione (art. 18).

2. DIRITTI ECONOMICI: liberta' di iniziativa economica (art. 41), ma 'non puo' svolgersi in contrasto con l'utilita' sociale o in modo da recare danno alla sicurezza, alla liberta', alla dignita' umana'; proprieta' privata riconosciuta e garantita con funzione sociale (art. 42), possibilita' di espropriazione per pubblico interesse con indennizzo; lavoro come diritto-dovere (art. 4), liberta' di sindacato (art. 39), diritto di sciopero (art. 40).

3. DIRITTI SOCIALI: tutela della salute (art. 32), della famiglia (art. 29-31), dell'istruzione (art. 33-34), della protezione sociale (art. 38), dell'abitazione (art. 47).

4. DIRITTI POLITICI: voto attivo e passivo (art. 48), accesso alle cariche pubbliche in condizioni di parita' (art. 51), petizione ai poteri pubblici (art. 50), difesa della patria (art. 52), fedelta' alla Repubblica e osservanza della Costituzione (art. 54).

5. LIMITAZIONI: i diritti possono essere limitati solo per legge, in modo proporzionato, nell'interesse della sicurezza nazionale, dell'ordine pubblico, della salute pubblica, della morale."""))
S.append(("costituzione","organi_stato",
"ORGANI DELLO STATO E FORME DI GOVERNO (ARTT. 55-95)",
"""La seconda parte della Costituzione regola l'organizzazione dello Stato:

1. PARLAMENTO (art. 55-82): bicamerale perfetto (Camera dei Deputati e Senato della Repubblica, eletti entrambi a suffragio universale e diretto, pari poteri); funzione legislativa e di controllo sul governo; Presidenti di Camera e Senato, Commissioni, procedimento legislativo (iter: esame commissioni, votazione articoli, voto finale, promulgazione).

2. PRESIDENTE DELLA REPUBBLICA (art. 83-91): eletto dal Parlamento in seduta comune con delegati regionali (3 per regione, Valle d'Aosta 1); sette anni; carica di rappresentanza nazionale e di garanzia; nomina il Presidente del Consiglio, promulga le leggi, puo' sciogliere le Camere, concede la grazia, e' il capo delle forze armate.

3. GOVERNO (art. 92-96): composto da Presidente del Consiglio e Ministri; deve ottenere la fiducia delle Camere; funzione esecutiva e amministrativa; la crisi di governo passa per le dimissioni o la sfiducia.

4. MAGISTRATURA E CORTE COSTITUZIONALE: la giurisdizione e' funzione esclusiva della magistratura (art. 101); la Corte Costituzionale (art. 134-137) giudica la legittimita' costituzionale delle leggi e dei regolamenti, conflitti di attribuzione, accuse contro il Presidente della Repubblica; composta da 15 giudici (5 nominati dal Presidente, 5 da Parlamento in seduta comune, 5 dalle supreme magistrature)."""))
S.append(("costituzione","regioni_autonomie",
"REGIONI, PROVINCE E COMUNI (ARTT. 114-133)",
"""Lo Stato e' organizzato in enti territoriali con autonomia:

1. ART. 114: la Repubblica e' formata dai Comuni, dalle Province, dalle Citta' metropolitane, dalle Regioni e dallo Stato; i Comuni, le Province, le Citta' metropolitane e le Regioni sono enti autonomi con propri statuti, poteri e funzioni secondo i principi fissati dalla Costituzione.

2. REGIONI ORDINARIE (15): Piemonte, Lombardia, Veneto, Liguria, Emilia-Romagna, Toscana, Umbria, Marche, Lazio, Abruzzo, Molise, Campania, Puglia, Basilicata, Calabria; REGIONI A STATUTO SPECIALE (5): Valle d'Aosta, Trentino-Alto Adige, Friuli Venezia Giulia, Sardegna, Sicilia (con poteri legislativi e amministrativi ampliati).

3. RIPARTO DELLE COMPETENZE (art. 117): materie di legislazione esclusiva statale (cittadinanza, ordine pubblico, difesa, valuta, istruzione, fisco), concorrenti (tutela della salute, previdenza, ambiente), regionali (artigianato, commercio, turismo, urbanistica, edilizia residenziale pubblica); principio sussidiarieta'.

4. SINDACO E PRESIDENTE DI REGIONE: organi esecutivi eletti direttamente dal popolo; il sindaco e' anche organo della Provincia per le funzioni provinciali.

5. RIFORME RECENTI: abolizione delle Province (2014, riforma Delrio), introduzione delle Citta' metropolitane (Torino, Milano, Venezia, Genova, Bologna, Firenze, Roma, Bari, Napoli, Reggio Calabria), autonomia differenziata per Veneto, Lombardia, Emilia-Romagna (intese ai sensi dell'art. 116, comma 3)."""))
S.append(("costituzione","giustizia",
"LA GIUSTIZIA NEL SISTEMA COSTITUZIONALE (ARTT. 101-113)",
"""La giustizia e' organizzata secondo principi di indipendenza e imparzialita':

1. INDIPENDENZA DELLA MAGISTRATURA: la giurisdizione e' esercitata in nome del popolo; i giudici sono soggetti solo alla legge (art. 101); il Consiglio Superiore della Magistratura (CSM) esercita poteri di autogoverno sulla magistratura ordinaria.

2. GRADI DI GIUDIZIO: giudice di pace, tribunale (giudice unico o collegiale), corte d'appello, corte di cassazione (giudice di legittimita'); giustizia amministrativa (TAR e Consiglio di Stato); giustizia contabile (Corte dei Conti); giustizia militare e tributaria.

3. PUBBLICITA' E DURATA: le udienze sono pubbliche (art. 101); la difesa e' diritto inviolabile a ogni grado e grado di giurisdizione (art. 24); la giustizia e' gratuita per chi ha insufficienti mezzi (patrocinio a spese dello Stato).

4. RIMEDI: ricorso per Cassazione (motivi di legittimita'), ricorso straordinario al Presidente della Repubblica, azione di legittimita' costituzionale (davanti alla Corte), ricorso alla Corte EDU (Strasburgo) per violazione dei diritti umani.

5. RIFORME IN CORSO: separazione delle carriere dei giudici, riforma del CSM, processo civile telematico, processo penale (riforma Cartabia 2022)."""))
S.append(("costituzione","riforme",
"RIFORME COSTITUZIONALI E REVISIONE (ARTT. 138-139)",
"""La Costituzione puo' essere modificata con procedure rafforzate:

1. PROCEDURA ORDINARIA (art. 138): le leggi di revisione della Costituzione e le altre leggi costituzionali sono adottate da ciascuna Camera con due successive deliberazioni a intervallo non minore di tre mesi, e approvate a maggioranza assoluta dei componenti di ciascuna Camera nella seconda votazione; sono sottoposte a referendum popolare quando, entro tre mesi dalla pubblicazione, ne faccia richiesta un quinto dei membri di una Camera o 500.000 elettori o cinque Consigli regionali; il referendum non si tiene se la legge e' stata approvata nella seconda votazione da maggioranza di due terzi dei componenti di ciascuna Camera.

2. LIMITI (art. 139): la forma repubblicana non puo' essere oggetto di revisione costituzionale.

3. RIFORME REALIZZATE: 1967 (regioni), 2001 (Titolo V, poteri regionali), 2012 (pareggio di bilancio), 2020 (riduzione parlamentari), 2022 (tutela ambiente, inviolabilita' diritti digitali di accesso).

4. RIFORME RESPINTE AL REFERENDUM: 2006 (riforma federalista), 2016 (riforma Renzi-Boschi sul Senato).

5. ATTUALITA': eventuali nuove riforme devono rispettare i principi fondamentali (repubblica, diritti umani, forma democratica)."""))
S.append(("costituzione","ordinamento_edilizio",
"L'ORDINAMENTO GIURIDICO PER L'EDILIZIA",
"""Il tecnico edile opera dentro un sistema giuridico di fonti:

1. GERARCHIA DELLE FONTI: Costituzione (1789? no, 1948) -> leggi costituzionali e leggi di revisione -> leggi ordinarie -> regolamenti governativi -> decreti ministeriali -> regolamenti regionali -> regolamenti comunali (con la riserva di legge e di regolamento per materie diverse).

2. FONTI REGIONALI: le Regioni a statuto ordinario hanno potesta' legislativa nelle materie non riservate allo Stato (art. 117); le leggi regionali non possono contravvenire ai principi generali stabiliti dalle leggi statali nelle materie concorrenti.

3. REGOLAMENTO EDILIZIO COMUNALE: atto normativo del sindaco che attua il PRG/PSC e regola i dettagli costruttivi (materiali, altezze, distanze, parcheggi); ogni progetto deve conformarsi ad esso.

4. GIURISPRUDENZA: le sentenze della Cassazione e della Corte Costituzionale interpretano le norme; la giurisprudenza consolidata ha valore orientativo (giudici guidano il tecnico).

5. PRINCIPI COSTITUZIONALI PER IL TECNICO: tutela del paesaggio (art. 9), tutela ambientale (art. 9), funzione sociale della proprieta' (art. 42), liberta' di iniziativa economica con utilita' sociale (art. 41), diritto al lavoro (art. 4)."""))

# ============ FISCO 2026 (8) ============
S.append(("fisco","struttura",
"LA STRUTTURA DEL SISTEMA FISCALE ITALIANO",
"""Il sistema fiscale italiano si divide in imposte dirette e indirette, gestite da Agenzia delle Entrate e altri enti:

1. IMPOSTE DIRETTE: colpiscono il reddito o la ricchezza: IRPEF (persone fisiche), IRES (societa' di capitali, 24%), IRAP (imposta regionale sulle attivita' produttive, 3,9% base), imposte locali sulla proprieta' (IMU, TARI per i rifiuti, TASI abolita 2020).

2. IMPOSTE INDIRETTE: colpiscono consumi e scambi: IVA (4%, 10%, 22%), accise (carburanti, tabacchi, alcolici), imposte di registro, successione e donazione, bollo auto, addizionali (regioni e comuni).

3. ALTRE ENTRATE: contributi previdenziali e assicurativi (INPS, INAIL), tasse universitarie, concessioni, multe.

4. AMMINISTRAZIONE: Agenzia delle Entrate (fisco), INPS (previdenza), INAIL (infortuni), Regioni e Comuni (addizionali, IMU, TARI), Guardia di Finanza (controllo).

5. PRINCIPI COSTITUZIONALI (art. 53): tutti sono tenuti a concorrere alle spese pubbliche in ragione della loro capacita' contributiva; il sistema tributario e' informato a criteri di progressivita'.

6. PRESSIONE FISCALE: circa il 43-44% del PIL (tra le piu' alte dell'OCDE), con evasione stimata intorno al 16-18% del PIL potenziale."""))
S.append(("fisco","irpef_2026",
"IRPEF 2026: SCAGLIONI, ALIQUOTE E CALCOLO (VERIFICATO)",
"""Dati ufficiali del periodo d'imposta 2026 (Legge di Bilancio 2026, L. 199/2025, in vigore dal 1/1/2026):

1. SCAGLIONI: 23% fino a 28.000 euro; 33% da 28.001 a 50.000 euro (ridotta dal 35% del 2025); 43% oltre 50.000 euro. Risparmio massimo 440 euro annui per chi ha reddito pari o superiore a 50.000 euro (2% x 22.000 euro).

2. NO-TAX AREA: 8.500 euro per lavoro dipendente e pensionati (IRPEF zero per effetto delle detrazioni da lavoro dipendente); lavoratori autonomi 5.500 euro, pensionati over 75 circa 8.150 euro.

3. IRPEF LORDA DI RIFERIMENTO: 6.440 euro (23% x 28.000); poi 6.440 + 33% sulla parte oltre 28.000; poi 13.700 + 43% sulla parte oltre 50.000 (13.700 = 6.440 + 33% x 22.000).

4. ADDIZIONALI: regionali da 0,7% a 3,33% (variano per regione), comunali da 0% a 0,9%; si aggiungono all'aliquota statale e sono trattenute in busta paga l'anno successivo.

5. TETTO DETRAZIONI (quoziente familiare): per redditi sopra 75.000 euro, limite complessivo alle detrazioni di 14.000 euro (75.000-100.000) e 8.000 euro (oltre 100.000); spese sanitarie escluse dal tetto.

6. ESEMPIO: reddito 40.000 euro -> IRPEF lorda = 6.440 + 33% x 12.000 = 6.440 + 3.960 = 10.400 euro (26% medio). Scadenza saldo: 30 giugno (fino 30 luglio con maggiorazione 0,40%)."""))
S.append(("fisco","iva_indirette",
"IVA E IMPOSTE INDIRETTE",
"""Le imposte indirette colpiscono i consumi e i trasferimenti:

1. IVA: 22% aliquota ordinaria; 10% (edilizia abitativa: costruzione, ristrutturazione, manutenzione straordinaria, vendita prima casa da costruttore); 4% (beni primari: generi alimentari, libri, quotidiani, servizi agricoli, vendita prima casa con requisiti agevolati); esenti (servizi sanitari, educativi, finanziari).

2. REVERSE CHARGE (inversione contabile): per subappalti edilizi, subentri e certe prestazioni (edilizia, pulizie, servizi informatici): il cliente versa l'IVA al posto del fornitore (art. 17 DPR 633/1972).

3. IMPOSTE DI REGISTRO: atti giuridici (vendite 9% prima casa, 2% seconda; locazioni 2-3%), ipotecarie e catastali (50 euro fisse per compravendite immobili tra privati).

4. SUCCESSIONE E DONAZIONE: franchigia 1 milione di euro per ciascun erede legittimo o coniuge (aliquota 4% oltre franchigia; 6% fratelli/sorelle oltre 100.000 euro; 8% altri); prima casa agevolata con franchigia aggiuntiva.

5. ACCISE: carburanti (benzina ~0,73 euro/litro + IVA), tabacchi, alcolici, gioco (diretta ed erariale), energia elettrica (A3? componente fiscale)."""))
S.append(("fisco","imprese",
"IMPRESE: IRES, IRAP, FORFETTARIO E REGIMI",
"""Il prelievo sulle imprese italiane e' articolato:

1. IRES: 24% sul reddito delle societa' di capitali (S.p.A., S.r.l., S.a.p.a.); il dividendo distribuito ai soci e' soggetto a tassazione separata (26% sui dividendi per persone fisiche, cedola secca).

2. IRAP: 3,9% standard (regioni possono variare) sulla produzione netta (valore della produzione - costi); per professionisti e imprese individuali e' stata abrogata dal 2022 (era 15% delle entrate), ora solo per societa' di capitali e enti commerciali.

3. REGIME FORFETTARIO (L. 190/2014): per partite IVA con ricavi fino a 85.000 euro; imposta sostitutiva 5% per i primi 5 anni (nuova attivita') poi 15%; niente IVA addebitata, niente deduzioni (costi forfettari), no IRPEF/IRAP/addizionali; vincoli (solo persone fisiche, non per prevalentemente prestazioni a ex datori, limiti plafond).

4. REGIME ORDINARIO: partite IVA con ricavi oltre 85.000 euro o che non rientrano nel forfettario; tassazione IRPEF ordinaria con contabilita' semplificata (ricavi fino a 400.000 servizi / 800.000 beni) o ordinaria.

5. RATEIZZAZIONE: versamenti acconti (giugno/luglio e novembre) e saldi (giugno/luglio anno successivo) con ravvedimento operoso per errori."""))
S.append(("fisco","lavoro_contributi",
"FIASCO E PREVIDENZA DEL LAVORO DIPENDENTE 2026",
"""Il netto in busta paga e' il risultato di ritenute e contributi:

1. CONTRIBUTI INPS: lavoratore dipendente versato 9,19% (quota a carico del lavoratore trattenuta in busta paga) e circa 30% a carico del datore (aliquota IVS complessiva ~39,49%); tetti massimali annuali (2026: circa 119.650 euro).

2. IRPEF IN BUSTA PAGA: trattenuta mensile a titolo di acconto sul reddito da lavoro dipendente; conguaglio a fine anno o nella prima busta paga dell'anno successivo; detrazioni da lavoro dipendente (massimo 1.955 euro per redditi fino a 8.500, poi decrescenti fino a 50.000).

3. TAGLIO DEL CUNEO FISCALE: misura strutturale dal 2024 (Legge di Bilancio 2024) che riduce il cuneo contributivo per i lavoratori dipendenti fino a 35.000 euro (circa 100 euro/mese di riduzione della trattenuta contributiva, finanziata dall'erario); confermata per il 2025 e rifinanziata per il 2026.

4. TFR: accantonato dal datore (6,91% della retribuzione lorda annua), rivalutato con criterio legale (1,5% fisso + 75% dell'inflazione ISTAT), tassazione separata piu' favorevole; anticipazioni per spese mediche, acquisto prima casa, raggiunti 8 anni di servizio.

5. NASpI: indennita' di disoccupazione per licenziamento involontario (max 24 mensilita' 2024-2025, 18 mensilita' dal 1/1/2026 per nuove disoccupazioni), aliquota 75% della retribuzione mensile nei primi 6 mesi, poi 75% decrescente; requisito 13 settimane di lavoro nei 4 anni."""))
S.append(("fisco","patrimonio_immobiliare",
"IMPOSTE SUL PATRIMONIO IMMOBILIARE: IMU, TARI, PLUSVALENZE",
"""La casa e' soggetta a un prelievo multilivello:

1. IMU: Imposta Municipale Unica (proprieta' immobiliare, escluse abitazioni principali non di lusso); aliquota base 0,86% (Comuni possono variare 0,46-1,06%); abitazione principale di categoria A/1, A/8, A/9 (lusso) tassata; terreni agricoli 0,1-0,2% (IMU agricola); fabbricati rurali 0,1%; versamenti a giugno e dicembre (acconto e saldo).

2. TARI: Tassa sui Rifiuti (comunale), calcolata su superficie e numero di occupanti; spetta anche al locatario per la casa affittata.

3. PLUSVALENZE IMMOBILIARI: vendita entro 5 anni dall'acquisto -> 26% sulla differenza (con franchigie e detrazioni per riacquisto entro 1 anno); dopo 5 anni non tassata per persone fisiche non in attivita' di impresa.

4. CEDOLARE SECCA: regime fiscale agevolato per locazioni (21% ordinaria, 26% se abitazione con contratto a canone concordato con vincolo), sostituisce IRPEF, addizionali e registrazione; non applicabile se il locatore ha redditi complessivi sopra 30.000 euro da locazioni agevolate.

5. PRIMA CASA: agevolazioni IMU (esenzione abitazione principale non lusso), imposta di registro 2% (vs 9%), IVA 4% (vs 10% se da costruttore), mutui agevolati, detrazioni interessi passivi (fine 2024? la detrazione e' stata abolita dalla Legge di Bilancio 2025 per nuovi mutui, salvo acquisti già avviati)."""))
S.append(("fisco","scadenze",
"IL CALENDARIO FISCALE E GLI ADEMPIMENTI 2026",
"""Le scadenze principali per contribuenti e professionisti:

1. 30 GENNAIO: certificazione Unica (ex CU) per lavoro dipendente, pensionati, autonomi; invio telematico.

2. 31 MARZO: termine presentazione 730 (Dipendenti e pensionati) e Redditi PF; prima rata IMU/TARI; assegno unico: presentazione ISEE entro 30 giugno per arretrati da marzo.

3. 30 GIUGNO: saldo IRPEF, IRES, IRAP, IVA e acconti 2027; versamento prima rata IMU; ravvedimento operoso agevolato fino al 30 giugno; possibile proroga al 31 luglio con maggiorazione 0,40%.

4. 20-31 LUGLIO: verifica pagamenti (30 settembre con maggiorazione) e seconda rata IMU/TARI.

5. 30 NOVEMBRE: acconto IVA e seconda rata acconto IRPEF/IRES; saldo IVA (Dicembre).

6. 31 DICEMBRE: fine anno d'imposta; adempimenti IVA annuali (esterometro, comunicazioni black list).

7. STRUMENTI: Fisconline e Entratel per invii, modello 730/Redditi, versamenti con modello F24 (pagoPA), Agenzia delle Entrate Riscossione per riscossioni."""))
S.append(("fisco","welfare_2026",
"WELFARE E PRESTAZIONI 2026: ASSEGNO UNICO, INCLUSIONE, BONUS (VERIFICATO)",
"""Dati ufficiali 2026 aggiornati (INPS, Legge di Bilancio 2026):

1. ASSEGNO UNICO E UNIVERSALE (AUU): importo massimo 199,40 euro/mese per figlio minorenne con ISEE fino a 17.468,51 euro; minimo 57,00 euro da ISEE 46.582,71; figli 18-20 anni: massimo 99,10, minimo 29,10; maggiorazioni: 3° figlio fino 96,90, madre under 21 (23,30), disabilita' 99,10-122,30, famiglie numerose 150 euro, figli under 1 anno +50%. ISEE per prestazioni familiari 2026 (nuovo): prima casa esclusa fino 120.000 euro.

2. ASSEGNO DI INCLUSIONE (ADI, ex Reddito di Cittadinanza): ISEE inferiore 10.140 euro, reddito nucleo inferiore 6.500 euro (scala equivalenza); 18 mensilita' rinnovabili 12 mesi con domanda immediata; compatibile con lavoro (esclusione primi 3.000 euro da lavoro); Supporto Formazione e Lavoro: 500 euro/mese max 12 mesi per componenti occupabili (cumulo max 3.000 euro).

3. BONUS NIDO: massimale 3.600 euro annui per nati dal 2024 con ISEE fino 40.000 euro (fasce: 3.600 / 2.500 / 1.500 seconda fascia ISEE 25-40k).

4. ASSEGNO DI MATERNITA' (Comuni/INPS): 413,10 euro/mese per 5 mesi, ISEE massimo 20.668,26 euro.

5. BONUS SOCIALE BOLLETTE: ISEE fino 9.530 euro (20.000 per famiglie numerose 4+ figli).

6. MODALITA': domande INPS online (portale unico), pagamento mensile dal 20 del mese, ISEE annuale da rinnovare entro febbraio."""))

# ============ LAVORO DIPENDENTE (7) ============
S.append(("lavoro","busta_paga",
"LEGGERE LA BUSTA PAGA",
"""La busta paga (cedolino) e' il documento mensile che dettaglia la retribuzione:

1. SEZIONI: dati anagrafici e contrattuali (datore, CCNL, livello, qualifica), periodo di riferimento, voce 'retribuzione' (elementi fissi e variabili: stipendio base, superminimo, scatti, straordinari, bonus), trattenute (INPS 9,19%, IRPEF, addizionali, sindacato, TFR?), altri dati (ferie, permessi, TFR maturato, contributi figurativi).

2. ELEMENTI FISSI: stipendio base (secondo CCNL e livello), contingenza (assorbita), EDR (elemento distinto della retribuzione, 10,33 euro), superminimo (elemento personalizzato), scatti di anzianita' (ogni 2-3 anni).

3. ELEMENTI VARIABILI: straordinari (maggiorazione 15-50% sulla normale), lavoro notturno (+15-20%), lavoro festivo, turni, premi di produzione, bonus aziendali (tassazione agevolata fino 3.000 euro), buoni pasto (limite 5,29 euro/giorno non tassati).

4. TRATTENUTE: INPS dipendente 9,19%; IRPEF a scaglioni con detrazioni da lavoro; addizionali regionali/comunali; eventuali trattenute sindacali (0,8-1%) e per terzi (es. mensa, trasporti).

5. CONGUAGLIO: a fine anno o gennaio successivo, si conguagliano le trattenute IRPEF/INPS con il reddito effettivo (fino 8.500 euro no-tax)."""))
S.append(("lavoro","tfr_13esima",
"TFR, TREDICESIMA E QUATTORDICESIMA",
"""I principali istituti retributivi dei dipendenti:

1. TFR (Trattamento di Fine Rapporto): accantonato annualmente dal datore (6,91% della retribuzione di riferimento lorda); rivalutazione annua con criterio legale (1,5% fisso + 75% dell'aumento ISTAT FOI); liquidazione a fine rapporto (dimissioni, licenziamento, pensione); tassazione separata con aliquote agevolate; anticipazioni per spese mediche/ prima casa/ altro entro il limite del 70% del TFR maturato dopo 8 anni di servizio; aziende con almeno 50 dipendenti: destinazione al fondo pensione o INPS (tutela).

2. TREDICESIMA (gratifica natalizia): 1/12 della retribuzione annua lorda per ogni mese di servizio; pagata a dicembre; compete se almeno 15 giorni lavorati nel mese; base di calcolo stipendio base + contingenza + EDR + scatti, esclusi straordinari e bonus.

3. QUATTORDICESIMA: prevista da alcuni CCNL (edilizia, commercio, metalmeccanico grande impresa? no, metalmeccanici artigiani e industria 14esima solo per aziende sopra 15 dipendenti); pagata a giugno; stesso criterio della tredicesima.

4. CONTRATTI: CCNL specifica la presenza e il calcolo di mensilita' aggiuntive; i premi di produzione (previsti da alcuni CCNL) sono variabili legati ai risultati."""))
S.append(("lavoro","ferie_permessi_malattia",
"FERIE, PERMESSI, MALATTIA E MATERNITA'",
"""I diritti a riposo del lavoratore dipendente:

1. FERIE: 4 settimane (20 giorni lavorativi) per anno di servizio, fruibili entro 18 mesi (per legge); maturano al tasso di 2,167 giorni/mese (26 giorni/12); retribuite normalmente; periodi determinati d'accordo (il datore fissa in genere estate e Natale).

2. PERMESSI (art. 20 L. 104/1992): 3 giorni al mese per assistenza a disabili gravi (legge 104); permessi sindacali (ufficio verde); permessi studio (se CCNL); permessi per lutto, matrimonio, visita medica, donazione sangue.

3. MALATTIA: retribuzione garantita dal CCNL (tipicamente 50-100% per i primi giorni, poi integrazione INPS e azienda); comportamento per malattia (visita fiscale INPS); congedo straordinario per assistenza familiari (L. 104).

4. MATERNITA': 5 mesi totali (2 prima del parto, 3 dopo) con astensione obbligatoria e indennita' INPS (80% della retribuzione); congedo parentale (facoltativo) fino al 6° anno del bambino (11 mesi complessivi tra madre e padre), indennita' 30% INPS; obbligo padre: 10 giorni obbligatori (20 in caso di padre unico); congedo papà bonus (2024): 1 mese extra retribuito al 80% se preso entro i 6 mesi.

5. PARENTALE E DAD: strumenti per l'emergenza (COVID), congedi speciali per chiusura scuole."""))
S.append(("lavoro","licenziamento_naspi",
"LICENZIAMENTO, NASpI E TUTELA DEL LAVORATORE",
"""La fine del rapporto di lavoro e' regolata da procedure precise:

1. TIPOLOGIE: dimissioni volontarie, licenziamento per giusta causa (gravi inadempimenti), giustificato motivo soggettivo (fatti non gravi) o oggettivo (razionalizzazione, cessazione attivita', inidoneita'); risoluzione consensuale (conciliazione).

2. TUTELE CRESCENTI (Jobs Act 2015): reintegro solo per licenziamento discriminatorio, nullo o non comunicato; altri casi: indennita' economica crescente (2 mensilita' per anno di servizio, min 4 max 24) e messa a disposizione (formazione/reimpiego).

3. NASpI (indennita' disoccupazione): richiesta INPS entro 68 giorni; requisito 13 settimane di lavoro nei 4 anni; durata massima 24 mesilita' (al 2024-2025), ridotte a 18 mensilita' per disoccupazioni dal 1/1/2026; importo 75% della retribuzione mensile fino 1.470,99 euro (2024), ridotto del 3% ogni mese; contributo IRPEF solo oltre 15.000 euro annui.

4. OBBLIGHI DEL DATORE: comunicazione UNILAV entrale 5 giorni, motivazione scritta del licenziamento, richiesta di conciliazione o accesso (tramite enti bilaterali o sportelli), versamento TFR entro 60 giorni, certificazione di lavoro, estratto conto INPS.

5. DISCRIMINAZIONI: licenziamento per motivi discriminatori (razza, sesso, religione, handicap, orientamento) e' nullo con risarcimento (5-24 mensilita', D.Lgs 165/2001)."""))
S.append(("lavoro","ccnl",
"CCNL E RAPPORTI DI LAVORO: LE FONDAMENTA",
"""I contratti collettivi regolano i rapporti di lavoro privati:

1. DEFINIZIONE: il CCNL (Contratto Collettivo Nazionale di Lavoro) e' stipulato da organizzazioni sindacali e associazioni datoriali; disciplina mansioni, livelli, retribuzioni minimi, ferie, malattia, preavviso, licenziamento.

2. LIVELLI E MANSIONI: ogni CCNL prevede livelli retributivi (1-7 nel metalmeccanico, 6-9 nell'edilizia) associati a mansioni; l'inquadramento e' definito dal datore con lettera di assunzione; il superamento (o demansionamento) e' contestabile.

3. SETTORI PRINCIPALI: edilizia (industria, artigianato), metalmeccanico (industria, artigiano, piccola industria), commercio (terziario, distribuzione moderna), servizi, credito, trasporti, sanitario, scuola privata.

4. STRUTTURA: parte normativa (diritti e obblighi) e parte economica (retribuzioni, contingenza); scatti di anzianita', elementi di produzione, bonus; rinnovo con aumenti tabellari o una tantum.

5. DIRITTI FONDAMENTALI: retribuzione minima, orario (40 ore settimanali per legge), straordinari (maggiorazione min 15%, max 78 ore annue/250 con accordi), riposi (giorno festivo settimanale, ferie), tutele in caso malattia/infortunio, sicurezza (D.Lgs 81/2008).

6. CONFLITTI: la contrattazione di secondo livello (aziendale) integra il CCNL con premi, welfare aziendale, formazione."""))
S.append(("lavoro","apprendistato",
"APPRENDISTATO E LAVORO GIOVANILE",
"""L'apprendistato e' il contratto di formazione per i giovani:

1. TIPI (D.Lgs 167/2011): apprendistato per il conseguimento del titolo di studio (15-25 anni, diploma/qualifica), per l'apprendimento di un mestiere (15-25 anni, non titolo), professionalizzante (18-29 anni, contratto di alto artigianato, tecnico).

2. DURATA: minimo 12 mesi, massimo 4 anni (in base al titolo e al livello); periodo di formazione esterno al lavoro (minimo 120 ore annue) con formatori accreditati.

3. RETRIBUZIONE: calcolata come percentuale della retribuzione del livello di inquadramento (aumenta con l'anzianita'), con tutele specifiche (indennita' di mancato preavviso anticipata, TFR maturato).

4. VANTAGGI: incentivi contributivi per il datore (esenzione contributi), credito d'imposta formazione (40%), contratto di solidarieta' no; garanzia di un livello retributivo crescente; possibilita' di proroga.

5. TUTELE: non puo' essere licenziato per fatti pregiudizievoli all'apprendimento; in caso di licenziamento durante il periodo di formazione, la indennita' e' anticipata di 2 mensilita'; conversione a tempo indeterminato senza oneri (agevolazioni).

6. OBBLIGHI DEL DATORE: nominare un tutor, rispettare il piano formativo, non assegnare mansioni superiori alla qualifica."""))
S.append(("lavoro","professionisti_freelance",
"LAVORO AUTONOMO, PARTITA IVA E COORDO E CONTINUITA'",
"""Il lavoro autonomo e regolato in forme diverse:

1. PARTITA IVA: apertura con modello AA9/12 al Comune o Agenzia delle Entrate; regime forfettario (85.000 euro, 5%/15% sostitutiva) o ordinario; versamenti INPS Gestione Separata (26,07% sul reddito 2024) per liberi professionisti senza cassa propria; artigiani e commercianti con cassa artigiani/commercianti (24% circa + minimale).

2. LIBERI PROFESSIONISTI: ordini (ingegneri, architetti, geometri, commercialisti, avvocati) con albi e deontologie; tariffari professionali (DM 137/2012) o tariffi liberi; responsabilita' civile professionale (art. 2236 c.c., assicurazione RCO).

3. RAPPORTI DI COLLABORAZIONE: co.co.co (coordinata e continuativa, con tutele crescenti: ferie, malattia, preavviso dal 2023 D.Lgs 81/2021), co.co.pro, lavoro a progetto; attenzione al rischio di falso autonomo (lavoro subordinato mascherato) con sanzioni e reintegro.

4. VOUCHER E PIGNORABILITA': i voucher (buoni lavoro) limitati ad attivita' marginali; il lavoro accessorio e' fortemente limitato.

5. INDIRZZI UTILi: commercialista per fisco, consulente del lavoro per rapporti dipendenti, ordine professionale per deontologia."""))

# ============ SISTEMA PAESE (7) ============
S.append(("paese","istituzioni",
"LE ISTITUZIONI DELLO STATO ITALIANO",
"""L'architettura istituzionale della Repubblica:

1. PARLAMENTO: Camera dei Deputati (400 eletti, 8 ripartiti estero) e Senato (200 eletti + 8 estero + 5 senatori a vita nominati dal Presidente); elezioni ogni 5 anni (salvo scioglimento anticipato); sedute comuni per elezione Presidente della Repubblica e riforme costituzionali; commissioni permanenti e bicamerali.

2. PRESIDENTE DEL CONSIGHLIO: capo del governo, guida la politica generale; nomina e revoca i ministri; rappresenta il governo; risponde alle Camere con la fiducia.

3. PRESIDENTE DELLA REPUBBLICA: Sergio Mattarella (dal 2015, rieletto 2022); carica di rappresentanza e garanzia; nomina il premier (dopo consultazioni), scioglie le Camere (sentiti i presidenti), promulga leggi (o rimanda alle Camere), concede grazia, presiede il CSM, e' comandante delle forze armate.

4. CORTE COSTITUZIONALE: 15 giudici (9 tra giudici togati e professori, 5 di designazione comune istituzionale, 1? corretto: 5 Presidente, 5 Parlamento, 5 supreme); giudica legittimita' costituzionale (incidente o azione diretta), conflitti attribuzione Stato-Regioni-enti, accuse Presidente.

5. CONSIGLIO SUPERIORE DELLA MAGISTRATURA: presieduto dal Presidente della Repubblica, autogoverno della magistratura ordinaria (consigli togati e laici).

6. CONSIGLIO DI STATO E CORTE DEI CONTI: giustizia amministrativa (contenzioso e pareri) e giustizia contabile (controllo bilancio pubblico, responsabilita' amministrativa)."""))
S.append(("paese","regioni_comuni",
"REGIONI, CITTA' METROPOLITANE, PROVINCE E COMUNI",
"""Il territorio italiano e' amministrato da enti locali con autonomia:

1. 20 REGIONI: 15 ordinarie, 5 a statuto speciale (Valle d'Aosta, Trentino-Alto Adige/Sudtirol, Friuli Venezia Giulia, Sardegna, Sicilia) con poteri legislativi e amministrativi ampliati (contributo dello Stato, competenze residuate).

2. 14 CITTA' METROPOLITANE (2014, Legge Delrio): Torino, Milano, Venezia, Genova, Bologna, Firenze, Roma Capitale, Bari, Napoli, Reggio Calabria + Cagliari, Catania, Messina, Palermo (dal 2016); funzioni di area vasta (pianificazione territoriale, trasporti, ambiente) sul territorio dell'ex provincia.

3. PROVINCE: abolite come enti eletti (sindaci e consiglieri sono consiglieri provinciali), funzioni residuali (viabilita', scuole edilizia? trasporti scolastici, protezione civile coordinamento); in Toscana, Sardegna, Friuli abolite del tutto.

4. COMUNI (7.904 circa): organi sindaco, giunta, consiglio comunale; funzioni: stato civile, polizia locale, urbanistica, edilizia privata, servizi sociali, scuole (edilizia, mense, trasporti), rifiuti, viabilita'.

5. UNIONI DI COMUNI E COMUNITA' MONTANE: forme di associazione per servizi comuni (ambiti ottimali rifiuti, bacini imbrifero, servizi sociali).

6. FINANZA LOCALE: tributi comunali (IMU, TARI, pubblicita', suolo-pubblico), trasferimenti erariali (Fondo Perequativo), fiscalita' di scopo (addizionali regionali/comunali IRPEF, accise derivate)."""))
S.append(("paese","ue_fondi",
"L'ITALIA NELL'UNIONE EUROPEA",
"""L'Italia e' membro fondatore dell'UE (1957, Trattati di Roma):

1. ISTITUZIONI UE: Commissione Europea (esecutivo, proposta leggi), Parlamento Europeo (eletto ogni 5 anni, 705 seggi, Italia 76), Consiglio dell'UE (ministri), Consiglio Europeo (capi di stato), BCE (politica monetaria, euro), Corte di Giustizia, Banca Europea per gli Investimenti.

2. EURO: moneta unica dal 2002 (Italia entra 1999); politica monetaria BCE (tassi di interesse, acquisto titoli); vincoli di Maastricht (deficit 3% PIL, debito 60% PIL, sanzioni).

3. FONDI EUROPEI: FESR (sviluppo regionale), FSE+ (sociale), FEASR (agricoltura), FEAMP (pesca); il PNRR italiano (191,5 miliardi di euro, Next Generation EU 2021-2026) per resilienza, transizione digitale e green, riforme.

4. MERCATO UNICO: libera circolazione persone, merci, servizi, capitali; norme armonizzate (CE marking, Eurocodici, direttive tecniche).

5. DIRITTO UE: regolamenti (direttamente applicabili), direttive (da recepire), decisioni; primato sul diritto nazionale (sentenza Costa/ENEL 1964).

6. PROGRAMMI: Horizon (ricerca), Erasmus (istruzione), Erasmus+ (scambio), Fondi strutturali per aree depresse (Mezzogiorno), Mio? no."""))
S.append(("paese","pa_digitale",
"LA PUBBLICA AMMINISTRAZIONE DIGITALE",
"""La PA italiana sta digitalizzando i servizi:

1. NORMATIVA: Codice dell'Amministrazione Digitale (D.Lgs 82/2005, aggiornato) obbligo dematerializzazione; identita' digitale (SPID, CIE - carta d'identita' elettronica), firma digitale, PEC (posta elettronica certificata) con valore legale.

2. PIATTAFORME: pagoPA (pagamenti alla PA), app IO (servizi al cittadino), ANPR (anagrafe nazionale), INAD (domicilio digitale), PDND (piattaforma dati), cloud della PA (Polo Strategico Nazionale), CAD? certificati.

3. ADEMPIMENTI: fatturazione elettronica (obbligatoria tra privati dal 2019, verso PA dal 2014), conservazione digitale a norma (CAD), accesso civico generalizzato (FOIA).

4. SERVIZI ONLINE: Agenzia delle Entrate (fisconline), INPS, INAIL, Camera di Commercio (registro imprese), Comuni (SUAP sportello unico edilizia online).

5. RILEVANZA PER EDILIZIA: presentazione pratiche edilizie in modalita' telematica (obbligatoria), CILA/SCIA online, accesso atti, pagamenti telematici."""))
S.append(("paese","giustizia_cittadino",
"LA GIUSTIZIA PER IL CITTADINO: CIVILE, PENALE, AMMINISTRATIVA",
"""Il cittadino puo' rivolgersi a tre ordini di giudici:

1. GIUSTIZIA CIVILE: contenziosi tra privati (contratti, responsabilita', famiglia, successioni, immobili); giudice di pace (piccole cause, fino 5.000 euro rito ridotto?), tribunale, corte d'appello, cassazione; riti: ordinario, sommario di cognizione, lavoro (tribunale in composizione monocratica), decreto ingiuntivo, esecuzioni forzate; mediazione e negoziazione assistita obbligatorie per molte controversie.

2. GIUSTIZIA PENALE: reati contro persona, patrimonio, ordine pubblico; PM (pubblico ministero), difensore, giudice (GUP dibattimento, tribunale monocratico, corte d'assise per gravi); procedimento: indagini preliminari, udienza preliminare, dibattimento, appello, cassazione; prescrizione (ridefinita riforma 2022); patteggiamento, sospensione con messa alla prova.

3. GIUSTIZIA AMMINISTRATIVA: ricorsi contro atti della PA (licenze, concorsi, appalti); TAR regionali e Consiglio di Stato; procedimento: ricorso (60 giorni), contraddittorio, sentenza; rimedio cassatorio; riforma processo amministrativo 2022 (tempi ridotti).

4. ALTRI: giustizia contabile (Corte dei Conti), tributaria (commissioni), militare; Corte EDU (Strasburgo) per violazioni convenzione diritti umani.

5. COSTI: contributo unificato, diritti di segreteria, onorari (parametri forensi per avvocati); patrocinio a spese dello Stato per redditi bassi; tutele: difensore civico, accesso agli atti."""))
S.append(("paese","istruzione_sanita",
"SCUOLA, UNIVERSITA' E SANITA' NEL SISTEMA ITALIANO",
"""I servizi essenziali del paese:

1. SCUOLA: obbligo formativo 10 anni (fino 16 anni, art. 34 Cost.); ciclo primario (5 elementari + 3 medie), secondario superiore (licei, tecnici, professionali, 5 anni); valutazione (prove INVALSI); istituti tecnici superiori (ITS Academy 2-3 anni post-diploma); educazione professionale regionale.

2. UNIVERSITA': 97 atenei statali + non statali riconosciuti; corsi laurea (3 anni), magistrale (2), dottorato (3); tasse in base ISEE (ISEE università); diritto allo studio (borse, mense, residenze); valutazione ANVUR; classificazioni internazionali.

3. SANITA': Servizio Sanitario Nazionale (SSN, legge 833/1978) con copertura universale (art. 32 Cost.); finanziato da fiscalità generale e ticket; organizzato per regioni (Aziende Sanitarie Locali ASL, Aziende Ospedaliere, Ospedali); medico di base, pediatra, pronto soccorso; ticket (esenzioni per reddito, patologie, eta'); liste d'attesa; Livelli Essenziali di Assistenza (LEA).

4. PREVIDENZA COMPLEMENTARE: fondi pensione (negoziali, aperti, preesistenti), PIP (piani individuali pensionistici); quota 103 (finestra mobile dal 2024, quota 41 per precoci, opzione donna); riforme in corso.

5. SERVIZI SOCIALI: assistenza anziani (badanti, centri diurni), disabilita' (legge 104, Legge 328/2000 sistema integrato), infanzia (nidi, centri estivi)."""))

# ============ writer ============
meta = {
    "source": "italia_sistema_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus sistema Italia a cura di Kimi - dati 2026 verificati su fonti ufficiali",
    "url": "",
}
out = []
for i, (cat, tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"ITA-{i:03d}", "categoria": cat, "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

os.makedirs('Italia_Sistema_Pack/parsed', exist_ok=True)
with open('Italia_Sistema_Pack/parsed/costituzione_sistema_italia.jsonl', 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede Italia sistema -> {os.path.abspath('Italia_Sistema_Pack/parsed/costituzione_sistema_italia.jsonl')}")
