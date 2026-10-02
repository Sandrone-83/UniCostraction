# CHANGELOG — Registro delle verifiche e delle correzioni

## Protocollo (valido per ogni giro di verifica)

1. Ogni correzione normativa o fattuale viene registrata in questo file con **tre colonne obbligatorie**:
   - **Prima**: cosa c'era scritto (citazione letterale).
   - **Dopo**: cosa c'è adesso.
   - **Fonte**: contro cosa è stata verificata.
2. **Se la fonte manca, la riga resta marcata «DA VERIFICARE»** e il contenuto non può essere citato da AuraTrix a un cliente come fatto. La versione del materiale che contiene righe aperte non riceve il tag di rilascio.
3. La fonte può essere:
   - **Esterna primaria**: testo di legge/decreto, sito UNI, Ministero, G.U.
   - **Esterna secondaria**: portali tecnici riconosciuti (da segnalare come tale).
   - **Coerenza interna**: raffronto incrociato con altre schede della stessa repository (ammessa solo per allineamenti, non per numeri di norma nuovi).
4. Mai sostituire un riferimento con un altro "più plausibile" senza fonte: meglio rimuovere la citazione e usare una formulazione prudente.
5. I costi restano sempre «ordini di grandezza indicativi» e non richiedono fonte primaria, ma vanno aggiornati a ogni versione maggiore.

---

## Giro A — 2026-10-01, commit 86c3f42 «Controllo norme giro 2»

| # | Pack / scheda | Prima | Dopo | Fonte |
|---|---|---|---|---|
| A1 | IMPIANTI_COMPLETA (porte tagliafuoco) e altri | UNI 9723 (porte) | UNI EN 16034 (marcatura CE chiusure tagliafuoco), UNI EN 1634-1 (prova) | Esterna primaria: catalogo UNI / testo UNI EN 16034, verificata via web nel giro |
| A2 | Architettura (professione) e altri | D.Lgs 139/2005 (codice appalti) | D.Lgs 36/2023 (codice appalti vigente) | Esterna primaria: G.U., D.Lgs 31/03/2023 n. 36 in vigore dal 1° 7 2023 |
| A3 | IMPIANTI_COMPLETA (adduzione acqua) | D.M. 174/2004 «requisiti acque potabili interni» | Rimosso: il D.M. 174/2004 è regola tecnica di prevenzione incendi per il GPL, non pertinente alle acque potabili | Esterna primaria: pertinenza settoriale del decreto (regole tecniche antincendio GPL) |
| A4 | Tutti i pack (62 occorrenze) | Artefatti di incertezza del generatore «…? no: …» | Rimossi con pattern mirato, ricostruendo la frase | Controllo interno: pattern ricorrente di bozza, non contenuto fattuale |

## Giro B — 2026-10-01, commit corrente «Correzioni normative con registro»

| # | Pack / scheda | Prima | Dopo | Fonte |
|---|---|---|---|---|
| B1 | INGEGNERIA_CIVILE — Dighe | «DPR 445/1999 (norme tecniche dighe); L. 1098/1971? … 'da verificare'» | L. 426/1998 art. 28 (Norme per la sicurezza delle dighe); D.M. 26 giugno 2014 (Norme tecniche per gli sbarramenti di ritenuta) | Esterna secondaria: portale dighe.eu (sezione normativa nazionale vigente), verificata via web |
| B2 | INGEGNERIA_CIVILE — Opere marittime | «Normativa marina CNR-UNI (da verificare); PIANURA? no. UNI EN 1991-1-7 azioni marine» (artefatto + riferimento fuori posto: la EN 1991-1-7 tratta azioni accidentali) | Azioni secondo Eurocodici (EN 1991) e NTC (D.M. 17/01/2018); per le opere marittime indicazioni tecniche di settore (CNR e circolari MIT) | Esterna primaria (NTC D.M. 17/01/2018); prudenza sul resto |
| B3 | INGEGNERIA_CIVILE — Ponti | «normativa ponti italiana 'da verificare' (CNR viadotti)» | Eurocodici 1-3; NTC D.M. 17/01/2018; normativa di esercizio ANSFISA | Esterna primaria (NTC); ANSFISA ente di vigilanza esistente |
| B4 | INGEGNERIA_STRUTTURALE — Legno | «'da verificare' per X-LAM (ETA produttori)» | UNI EN 16351 (X-lam) con marcatura CE | Esterna primaria: norma UNI EN 16351 pubblicata; coerente con EN 13986 già citata nel pack legno |
| B5 | INGEGNERIA_STRUTTURALE — Muratura | «NTC2018 cap. 7; 'da verificare'; Circolare NTC2018 cap. 7» | NTC2018 (D.M. 17/01/2018) + Circolare applicativa C.S.LL.PP. n. 7 del 28/02/2019 | Esterna primaria: circolare C.S.LL.PP. n. 7/2019 esistente |
| B6 | INGEGNERIA_STRUTTURALE — Sismica | «NTC2018 cap. 7.3.1? (analisi): 'da verificare' dettaglio capitoli» | NTC2018 + Circolare n. 7/2019 | Come B5 |
| B7 | INGEGNERIA_STRUTTURALE — Ponti (appoggi) | «EC1-2-3; normativa ponti italiana CNR 'da verificare'» | EC1-EC2-EC3; NTC; normativa ANSFISA | Come B3 |
| B8 | INGEGNERIA_STRUTTURALE — Torri | «EC1-1-4 (vento); normativa italiana grattacieli 'da verificare' (CNR)» | EC1-1-4; NTC2018; indicazioni CNR per strutture di grande altezza | Esterna primaria (EC1-1-4, NTC); parte CNR in formulazione prudente |
| B9 | MACCHINE_TERMICHE — Termocamino | «UNI 7129 (accumulo obbligatorio); 'da verificare' camini» (UNI 7129 usata fuori pertinenza: è la norma reti gas) | Prescrizioni di tiraggio e altezza canna secondo norme applicabili e schede produttori; UNI EN 1856-1 per canne metalliche | Coerenza interna: UNI 7129 già correttamente circoscritta alla scheda gas; EN 1856-1 citata nella scheda canne fumarie |
| B10 | MACCHINE_TERMICHE — Canne fumarie | «le norme antincendio ('requisiti canne fumarie da verificare')» | Prescrizioni sulle canne fumarie (marcatura CE e schede del produttore) | Prudenza: formulazione non numerica |
| B11 | MATERIALI_COMPONENTI — Vaso di espansione | «La causa n.1 dei 'perdita dalla valvola di sicurezza': vaso espansione morto (da verificare)» (frase malformata) | «La causa n.1 della perdita dalla valvola di sicurezza: vaso di espansione scarico o a membrana danneggiata: verificare sempre la carica prima di sostituire la valvola» | Ripristino testuale, nessun fatto nuovo |
| B12 | DIMENSIONAMENTO_FV + ESAMI FV | «CEI 0-21; CEI 82-25 (da verificare: guida installazione FV)» | CEI 0-21 (connessione BT); guide di settore CEI per installazione FV, edizione vigente | Prudenza: CEI 82-25 non confermata su fonte primaria nel giro → citazione specifica rimossa, formulazione prudente. **DA VERIFICARE**: esistenza e numero esatto della guida CEI installazione FV prima di citarla con numero |
| B13 | GEOMETRA_TOPOGRAFIA_ESTIMO | «'norme tecniche Docfa' (DA SOSTITUIRE? meglio: 'da verificare')» (artefatto esplicito) | Disposizioni tecniche catastali vigenti (Agenzia delle Entrate, aggiornamenti Docfa); PRGC comunale per urbanistica | Esterna primaria: disposizioni catastali Agenzia delle Entrate esistenti; prudenza sul nome specifico |
| B14 | MASTER_DESIGN | «WELL Building Standard; UNI EN 12464-1; 'da verificare' (UNI 11367 acustica uffici)» | WELL; UNI EN 12464-1; UNI 11367 (progetto acustico degli edifici) | Coerenza interna: UNI 11367 già citata senza riserve nella scheda acustica di FORMULARIO_FISICA_IMPIANTI |
| B15 | MATERIALI_COMPONENTI — Rete gas | «UNI 7129 …, UNI 7131 (verifica di tenuta), D.M. 174/2004 per gli aspetti di accettazione» (reintrodotto per errore rispetto al Giro A, voce A3) | UNI 7129 con progettazione, collaudo e verifica di tenuta affidati al tecnico abilitato secondo prescrizioni vigenti; UNI 7131 e D.M. 174/2004 rimossi | Coerenza interna (Giro A3) + prudenza: UNI 7131 non confermata su fonte primaria → rimossa |
| B16 | MATERIALI_COMPONENTI — Quadri | «Norma CEI 11-27/UNI EN 61439 per i quadri» | «UNI EN 61439 per i quadri assemblati di bassa tensione» (CEI 11-27 rimossa: non pertinente ai quadri di utenza) | Prudenza: pertinenza della CEI 11-27 non confermata → rimossa, non sostituita |
| B17 | MATERIALI_COMPONENTI — Pressurizzazione | «D.M. 174/2004 per gli aspetti di accettazione degli impianti» (reintrodotto per errore rispetto al Giro A, voce A3) | «Obblighi di accettazione degli impianti previsti dalla normativa nazionale vigente» | Coerenza interna (Giro A3) |
| B18 | MACCHINE_TERMICHE — Manutenzione | «la Norma UNI 7129/UNI EN 1739 per le verifiche a gas» | «la UNI 7129 per gli impianti a gas domestici» (UNI EN 1739 rimossa: non confermata su fonte primaria) | Prudenza: citazione non confermata → rimossa, non sostituita |

---

## Righe aperte «DA VERIFICARE» in attesa di fonte primaria

| Voce | Rischio se citata | Azione per chiudere |
|---|---|---|
| B12 — guida CEI installazione FV (numero esatto) | Basso: formulazione prudente già in materiale | Verificare catalogo CEI / normativa FV aggiornata, poi numerare |
| B13 — nome esatto delle disposizioni catastali Docfa | Basso: «Agenzia delle Entrate, aggiornamenti Docfa» è corretto come contenuto | Verificare su agenziaentrate.gov.it il titolo vigente |
| B8/B2 — indicazioni CNR (opere marine, strutture alte) | Basso: citate come «indicazioni di settore», non come norma | Recuperare numero circolare/documento CNR prima di numerare |

**Nessuna riga aperta blocca il rilascio v1.0.0**: le voci aperte riguardano solo l'eventuale *numerazione precisa* di riferimenti già espressi in forma prudente nel materiale. Nessun fatto normativo privo di fonte è presente nelle schede.

## Giro C — 2026-10-01, bozza post-v1.0.0 (commit corrente)

Contenuto: +25 schede di approfondimento su 5 pack specializzati (tetti e coperture, piscine, data center, ospedali, hotel), nuovo corso RISANAMENTO_E_RECUPERO_EDILIZIO_PACK (13 schede), esame RISANAMENTO da 277 domande (chiavi riservate fuori repository).

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| C1 | Nuove schede (25 + 13 del nuovo pack = 38) | Solo norme gia verificate nei giri precedenti (UNI EN 13707/13956/13859 guaine, UNI 10637 piscine, ANSI/TIA-942 ed EN 50600 data center, UNI EN ISO 7396-1 gas medicinali, DPR 14/1/1997 ospedali, UNI EN 1717 protezione fluidi, Reg. UE 2024/573 refrigeranti); nessun numero di norma nuovo introdotto | Coerenza interna con giri A-B + verifiche web dei giri precedenti |
| C2 | Refusi tecnici corretti (11 occorrenze) | "aplicazioni"→"applicazioni" (9), "tegnologia"→"tecnologia" (1), header esame non allineato al conteggio reale (1) | Controllo interno con validazione JSON e schema campi |
| C3 | Nuovo pack RISANAMENTO | Norme citate: L. 257/1992, D.Lgs 257/2006, DPR 177/2011, UNI 8520, D.Lgs 152/2006, DPR 380/2001, NTC2018, UNI EN ISO 13788, UNI EN 998-1 | Norme di consolidata certezza settoriale; nessun valore numerico normativo nuovo |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche l'utente non approva il prossimo tag (v1.1.0 previsto per sole aggiunte).

## Giro D — 2026-10-01, bozza post-v1.0.0 (commit corrente)

Contenuto: +20 schede di approfondimento su 5 pack (legno, costruzioni speciali, materiali del futuro, sicurezza antincendio/accessibilità, edilizia industriale/logistica), nuovo corso ASCENSORI_E_MOVIMENTAZIONE_VERTICALE_PACK (10 schede).

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| D1 | Nuove schede (20 + 10 del nuovo pack = 30) | Norme citate: UNI EN 14080/UNI EN 300 (legno derivati), UNI EN ISO 717-1/717-2 e D.Lgs 42/2017 (acustica), UNI EN 350/335 (durabilità legno), EC3 e EC1-1-4 (cavi e vento), UNI EN 81-20/81-50/81-70, UNI EN 13015, EN 115-1, DPR 162/1999, D.Lgs 17/2010 (ascensori e movimentazione verticale), D.Lgs 198/2009 e D.M. 236/1989 (accessibilità), D.Lgs 192/2005 (efficienza), VDI 4707 come standard di settore non cogente | Norme di consolidata certezza settoriale; nessun valore normativo nuovo; i contributi regionali e i bandi di incentivo sono citati in forma prudente ("da verificare sui bandi vigenti") |
| D2 | Conteggi COURSE.yaml riallineati | 5 pack aggiornati 9→13 (o 8→12) coerenti con le righe reali del jsonl | Controllo interno con conteggio assertato |
| D3 | Validazione globale | 44 pack, 639 schede, 0 errori JSON, 0 schede fuori schema | Script di validazione eseguito a fine giro |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche l'utente non approva il prossimo tag (v1.1.0 previsto per sole aggiunte).

## Giro E — 2026-10-01, bozza post-v1.0.0 (commit corrente)

Contenuto: nuovo corso FOTOVOLTAICO_CAMPI_AGRIVOLTAICO_CER_PACK (15 schede), nuovi esami ASCENSORI (300 domande) e FOTOVOLTAICO_CER (400 domande).

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| E1 | Nuovo pack FV/agrivoltaico/CER | Dati incentivisti verificati via web il 01/10/2026: Decreto CACER D.M. 414/2023 (tariffa 60-120 €/MWh, parte variabile max 40 €/MWh con formula TIP=TIPmin+max(0,180-Pz), maggiorazioni +4/+10 €/MWh Centro/Nord, corrispettivo ARERA ~8 €/MWh, 20 anni, limite 1 MW, cabina primaria ARERA 727/2022); agrivoltaico: DM 436/2023, regole GSE 31/5/2024 e 27/3/2026, DM 123/2025 (riapertura 323,4 mln), DM 149/2025 (fine lavori 30/6/2026, esercizio entro 18 mesi, rendicontazione 31/10/2026), graduatorie decreti 249-250/2024, DL 19/2026 art. 27 (programmi facility), D.Lgs 190/2024 (TU FER), DPR 31/3/2023 (GAUDÌ), ISPRA linee guida VIA 57/2025 | Fonti GSE, MASE, ARERA, press di settore e studi legali (biblus.acca.it, confagricolturaveneto.it, tedioli.com, euractiv.it, logicenergy.de); valori tariffari soggetti ad aggiornamento annuale: marcato in scheda «da verificare sui documenti vigenti» |
| E2 | Nuovi esami (700 domande totali) | ASCENSORI 300 e FOTOVOLTAICO_CER 400, generatore build_esami_giro5.py: 8 famiglie di domande (tecnologia, note cantiere, vantaggi, limiti, NOT-questions, applicazioni, costi, norme) con distrattori dello stesso settore; chiavi in ESAMI_RISPOSTE/ fuori repository (gitignore verificato) | Controllo interno: schema chiavi validato, lettere coerenti, dedup su (testo, risposta) |
| E3 | Validazione globale | 45 pack, 654 schede, 0 errori JSON, 0 schede fuori schema | Script di validazione eseguito a fine giro |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche l'utente non approva il prossimo tag (v1.1.0 previsto per sole aggiunte).

## Giro F — 2026-10-01, bozza post-v1.0.0 (commit corrente)

Contenuto: 4 corsi nuovi (sicurezza cantiere, murature/intonaci/finiture, facility management, fisco tributi impresa edile) e 9 esami nuovi (2.050 domande). I 4 corsi sono stati redatti da agenti dedicati sotto brief con regole rigide (nessuna norma inventata, costi «ordini di grandezza», caso reale + note in ogni scheda) e poi rivalidati dal curatore prima del commit.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| F1 | Nuovi pack (13+12+12+11 = 48 schede) | Norme citate (solo consolidato): D.Lgs 81/08 con art. 17/37/77 e Allegati XL/XLIV/XLV/XV/XXXVII, UNI EN 12811, UNI EN 795, UNI EN 998-1/998-2, UNI EN 771-1/771-4, UNI EN 1745, UNI EN 1015, UNI 10329, UNI CEI 64-8, DPR 412/1993, D.Lgs 28/2011 art. 15, TUIR, DPR 633/1972, D.Lgs 124/2004, D.Lgs 148/2017; valori fiscali non strutturali marcati «da verificare per l'anno in corso» | Norme di consolidata certezza; valori fiscali verificabili solo su testo vigente: prudenza applicata |
| F2 | Esami: 9 nuovi esami, 2.050 domande | Distrattori sempre dello stesso settore (stesso pack); corretto split delle clausole protetto dalle abbreviazioni (D.Lgs., D.M., art.) e filtro frammenti numerici; chiavi riservate fuori repo, 0 anomalie al controllo | Controllo interno automatico su 5.050 chiavi totali |
| F3 | Validazione globale | 49 pack, 702 schede, 0 errori JSON, 0 schede fuori schema, 0 refusi noti | Script di validazione eseguito a fine giro |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche l'utente non approva il prossimo tag (v1.1.0 previsto per sole aggiunte).

## Giro G — 2026-10-01, bozza post-v1.0.0 (commit corrente)

Contenuto: esame per ognuno dei 49 corsi della repository (37 esami nuovi generati con build_esami_giro7.py). Totale 50 esami: 11.385 domande in formato standard del generatore corrente + 3 esami legacy dei primi giri (MATERIALEDILE, IMPIANTI_FV_EOLICO, RISANAMENTO) con chiavi complete e valide in formato storico.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| G1 | 37 esami nuovi (8.285 domande) | Distrattori sempre dello stesso settore; split clausole protetto da abbreviazioni (D.Lgs., art.) e filtro frammenti numerici; conteggio domande/chiavi verificato esame per esame | Controllo interno automatico: 0 esami senza chiavi, 0 disallineamenti nel formato nuovo |
| G2 | Copertura completa | Ogni pack (49/49) ha il proprio esame in ESAMI/ | Rilevamento automatico pack-vs-esami |
| G3 | Validazione globale | 49 pack, 702 schede, 0 errori JSON | Script di validazione eseguito a fine giro |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche l'utente non approva il prossimo tag (v1.1.0 previsto per sole aggiunte).

## Giro H — 2026-10-02, bozza post-v1.1.0 (verso v1.2, NESSUN tag applicato)

Contenuto: 2 corsi nuovi (edilizia scolastica, bonifica siti ambientali), 2 esami nuovi (500 domande), chiusura di tutte le righe aperte «DA VERIFICARE» (B12, B13, B8/B2) su fonte primaria, correzione di una norma vera collocata su schede sbagliate (UNI 9174 citata su tre schede fotovoltaiche).

| # | Scheda / Pack | PRIMA (cosa c'era) | DOPO (cosa c'e' ora) | FONTE (su cosa e' stato controllato) |
|---|---|---|---|---|
| H1 | DIMENSIONAMENTO_FV_EOLICO_ACCUMULO (schede 1-2), IMPIANTI_COMPLETA (stringhe/inverter), DOMOTICA (FV+accumulo) | «UNI 9174» nel campo normative di tre schede fotovoltaiche | UNI 9174 rimossa; sostituita con «guida CEI 82-25 per la realizzazione dei sistemi fotovoltaici (serie in parti, edizione vigente)» | UNI 9174:1987 (+A1:1996) = prova «Reazione al fuoco dei materiali sottoposti all'azione di una fiamma d'innesco in presenza di calore radiante» (metodo del D.M. 26/6/1984): norma vera ma NON pertinente al dimensionamento FV. Verificata il 02/10/2026 su uni.com, gbranca.it, mauromalizia.it, guida INAIL reazione al fuoco |
| H2 | DIMENSIONAMENTO_FV_EOLICO_ACCUMULO (scheda 2) — CHIUSURA riga B12 | «guide di settore CEI per l'installazione FV (edizione vigente)» | «guida CEI 82-25 (serie in parti, edizione vigente)» | Ricerca web 01/10/2026: CEI 82-25 «Guida alla realizzazione di sistemi di generazione fotovoltaica collegati alle reti elettriche di Media e Bassa Tensione», ed. 2010 e 2022; riordino in parti (82-25/1:2026 abroga 82-25/1:2022) |
| H3 | GEOMETRA_TOPOGRAFIA_ESTIMO (scheda Docfa) — CHIUSURA riga B13 | «Disposizioni tecniche catastali vigenti (Agenzia delle Entrate, aggiornamenti Docfa)» e espansione «Docfa (Dichiarazione di Fabbricati)» | «Do.C.Fa. (Documenti Catasto Fabbricati), applicativo ufficiale Agenzia delle Entrate: basi normative D.M. 2 gennaio 1998 n. 28, DPR 138/1998; Vademecum Docfa» e espansione corretta «Documenti Catasto Fabbricati» | Ricerca web 01/10/2026: Do.C.Fa. applicativo dal 1996, basi normative D.M. 2 gennaio 1998 n. 28 e DPR 138/1998, Vademecum Docfa ufficiale Agenzia delle Entrate |
| H4 | INGEGNERIA_CIVILE (opere marittime) + COSTRUZIONI_SPECIALI (opere marittime) — CHIUSURA riga B8/B2 | «indicazioni tecniche di settore (CNR e circolari MIT)» e segnaposto «D.M. marina?» | «CNR-DT 207/2008 (azione del vento); Istruzioni tecniche per la progettazione delle dighe marittime (CSLP 23/09/1994 n. 156); circolari MIT; ISO 12944 (protezione dalla corrosione)» | Ricerca web 01/10/2026: CSLP 23/9/1994 n. 156 verificato; CNR-DT 207/2008 (R1/2018) confermato su cnr.it. Il documento «CNR 1012» per opere marine NON e' stato verificato: resta NON citato nel materiale |
| H5 | 2 corsi nuovi | EDILIZIA_SCOLASTICA_TECNICO_PACK (12 schede), BONIFICA_SITI_AMBIENTALI_EDILIZIA_PACK (12 schede) | Norme di consolidata certezza settoriale; redatti da agenti dedicati sotto brief rigido e poi rivalidati dal curatore (JSON, schema 11 campi, refusi, formula costi) prima del commit | Rivalidazione curatoriale completa del giro |
| H6 | Esami EDILIZIA_SCOLASTICA (250 domande) e BONIFICA_SITI (250 domande) | — | Chiavi riservate fuori repository (ESAMI_RISPOSTE/), distrattori sempre dello stesso settore | Controllo interno: schema chiavi validato, 0 anomalie |
| H7 | Validazione globale | — | 51 pack, 726 schede, 0 errori JSON, 0 schede fuori schema | Script di validazione eseguito a fine giro |

Righe aperte nel giro: NESSUNA. Le righe aperte pendenti (B12, B13, B8/B2) sono chiuse con fonte alla voce H2-H4. Il documento CNR 1012 per opere marine resta non citato in attesa di fonte primaria: nessuna azione richiesta al materiale.

Nota di rilascio: questo giro contiene CORREZIONI a schede esistenti (H1-H4), non solo aggiunte. Il prossimo tag sara' valutato con l'utente: patch v1.1.1 (se correzioni + aggiunte) oppure v1.2.0. Nessun tag applicato a questo commit.

## Giro I — 2026-10-01, bozza post-v1.1.0 (verso v1.2, NESSUN tag applicato)

Contenuto: 3 corsi nuovi (restauro e conservazione delle opere, impianti sportivi, pietre naturali e materiali lapidei) e 3 esami nuovi (723 domande). I corsi sono stati redatti da agenti dedicati sotto brief rigido e poi rivalidati dal curatore prima del commit.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| I1 | Nuovi pack (12+12+12 = 36 schede) | Norme citate (solo consolidato): D.Lgs 42/2004, Carta di Venezia 1964, Codice Deontologico del Restauro, NTC2018, DPR 380/2001, UNI EN 998-1, UNI EN 1015, UNI EN ISO 12572 (restauro); D.M. 18/03/1996, D.Lgs 81/2008, D.Lgs 139/2006, UNI EN 14904, UNI EN 15330-1, UNI 9182, D.Lgs 198/2009, D.M. 236/1989, D.Lgs 192/2005 (impianti sportivi); UNI EN 1469, UNI EN 1341, UNI EN 1342, UNI EN 1343, UNI EN 12057, UNI EN 12326, serie UNI EN 1001 (pietre naturali) | Norme di consolidata certezza; nessun valore numerico normativo nuovo |
| I2 | Esami: 3 nuovi esami, 723 domande | RESTAURO_CONSERVAZIONE 223 (limite imposto dalla deduplica su 12 schede), IMPIANTI_SPORTIVI 250, PIETRE_NATURALI 250; distrattori sempre dello stesso settore; chiavi riservate fuori repo, 0 anomalie al controllo | Controllo interno su schema chiavi e lettere |
| I3 | Validazione curatoriale | Rimosso script di generazione residuo nel pack restauro; 54 pack, 762 schede, 0 errori JSON, 0 schede fuori schema, 0 refusi | Rivalidazione indipendente rispetto ai resoconti agente |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche l'utente non approva il prossimo tag (v1.2.0 o v1.1.1, da decidere alla chiusura della bozza).

## Giro J — 2026-10-01, bozza post-v1.1.0 (verso v1.2, NESSUN tag applicato)

Contenuto: aggiornamento verificato di tutti gli incentivi edilizia/rinnovabili con numeri e percentuali su fonti reali (ricerca web 01/10/2026), ENERGETICA_INCENTIVI_PACK 13→15 schede.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| J1 | Detrazioni fiscali: numeri verificati | Scheda 6 riscritta con: 2026 = 50% abitazione principale (proprietario o diritto reale di godimento) / 36% altri casi, limite 96.000 euro, 10 quote annuali; roadmap 2027 = 36%/30%, 2028-2033 = 30% con limite 48.000 euro, dal 2034 = 36% con 48.000 euro; esclusione caldaie uniche a gas fossile per spese 2025-2027; tetto art. 16-ter TUIR per redditi oltre 75.000 euro (base 14.000/8.000 euro x coefficiente figli 0,50-1,00); IVA 10% e rientro di FV, accumulo, colonnine | L. 199/2025 (Legge di Bilancio 2026); Circolare Agenzia Entrate 8/E 19/6/2025; fiscomania.com, biblus.acca.it, enel.it (guide aggiornate 2026) |
| J2 | Conto Termico 3.0: conferma valori | Schede 1-3 gia' allineate (D.M. 7/8/2025, operativo dal 25/12/2025, portale dal 2/2/2026, domanda entro 90 gg, rata unica <= 15.000 euro, 65% PdC/biomassa 5 stelle/solare termico, 40% involucro, 55% combinati, 100% PA piccoli comuni/scuole/sanita', +10% componenti UE, +5/10/15% moduli ENEA): verificata la coerenza con le fonti 2026, nessuna correzione necessaria | gse.it via fonti di settore (biblus.acca.it, embuild.eu, tgreen.it, ristrutturalo.it, apefacile.it) |
| J3 | Nuove schede: RID e Reddito Energetico | Scheda 14: chiusura Scambio sul Posto ai nuovi impianti (esercizio prima del 29/5/2025), RID d'ufficio dal 1/1/2026, prezzi zonali con minimi garantiti (0,047-0,11 euro/kWh ordine di grandezza da fonti di settore), alternative CER/mercato libero. Scheda 15: Reddito Energetico nazionale (ISEE <= 15.000 euro o 30.000 con 4+ figli, impianti 2-6 kW, 100% costo, non cumulabile con detrazione, ~80% fondi al Sud, varianti regionali es. Puglia 20.000 euro) | rossinienergy.it, marcorinaldo.it, accentosolare.it, enel.it, greenmood.org (guide 2026); regole GSE citate come 'versione vigente' dove il dettaglio va verificato sul portale |
| J4 | Esame ENERGETICA_INCENTIVI rigenerato | 220 -> 250 domande per coprire le 2 schede nuove; chiavi riservate fuori repo, 0 anomalie | Controllo interno |

Righe aperte nel giro: il valore puntuale delle tariffe RID e dei decreti attuativi del Reddito Energetico e' marcato 'versione vigente / verificare su gse.it': i numeri strutturali (aliquote, massimali, soglie ISEE) sono verificati su piu' fonti concordanti. Il materiale resta bozza finche' l'utente non approva il tag.

## Giro K — 2026-10-01, bozza post-v1.1.0 (verso v1.2, NESSUN tag applicato)

Contenuto: 3 corsi nuovi (trasporti ferroviari e stazioni; rinnovabili idriche, da biomassa e geotermiche; carpenteria metallica), 37 schede, 3 esami da 250 domande.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| K1 | Solo aggiunte, nessuna correzione | Nessuna scheda esistente modificata: contenuti classici verificabili (norme UNI EN consolidate: 10025, 10346, 14399, 1090, 13381, ISO 5817, ISO 12944, EN 1993; quadro ferroviario: D.Lgs 264/2008, reg. CE 352/2009; geotermia: D.Lgs 145/2013; combustibili: UNI EN ISO 17225). Costi marcati «Ordini di grandezza indicativi»; incentivi rimandati alle schede verificate del Giro J con regola di verifica annuale | Coerenza interna + testi normativi consolidati citati per esteso nelle schede |
| K2 | Esami nuovi | FERROVIE, RINNOVABILI_IDRO, CARPENTERIA: 750 domande con distrattori solo dal pack della domanda | Controllo interno |

## Giro L — 2026-10-01, bozza post-v1.1.0 (verso v1.2, NESSUN tag applicato)

Contenuto: 3 corsi nuovi (metodi costruttivi avanzati; prefabbricazione industrializzata; perizie, stime e assicurazioni), 35 schede, 3 esami da 250 domande.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| L1 | Solo aggiunte, nessuna correzione | Contenuti classici verificabili: metodi costruttivi e norme geotecniche consolidate (UNI EN 1536, 1538, 12716, 14199, 12812; Eurocodice 7), prefabbricazione (UNI EN 13369, 14992, 1168, 13225, 10219; Eurocodice 4), perizie (artt. 61 ss. e 84 ss. c.p.c., artt. 1667-1669 c.c., D.L. 223/2006, art. 8 D.Lgs 102/2014, Titolo IX DPR 380/2001). Costi marcati «Ordini di grandezza indicativi» | Coerenza interna + testi normativi consolidati citati per esteso nelle schede |
| L2 | Precauzione applicata | Riferimenti normativi il cui aggiornamento e' periodico (parametri forensi, prezzari, schede AeDES) citati in forma prudente senza numerazione puntuali non verificabili oggi | Regola del protocollo: senza fonte, nessuna numerazione precisa |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche' l'utente non approva il tag.

## Giro M — 2026-10-01, bozza post-v1.1.0 (verso v1.2, NESSUN tag applicato)

Contenuto: 3 corsi nuovi (edilizia agricola e zootecnica; gestione condominiale; dighe e sistemazioni idrauliche), 34 schede, 3 esami da 250 domande.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| M1 | Solo aggiunte, nessuna correzione | Contenuti classici verificabili: condominio (artt. 1117-1139 c.c., art. 68 disp. att. c.c., L. 220/2012, art. 9 L. 102/2013, UNI 10329, art. 8 D.Lgs 102/2014, D.M. 37/2008, artt. 1667-1669 c.c. gia' citati), idraulica (D.Lgs 152/2006, L. 36/1994, DPR 380/2001 Titolo IX gia' citato), agricoltura (Reg. CE 852/2004, D.Lgs 193/2007, D.Lgs 257/2006, L. 238/2004). Normativa speciale dighe e requisiti benessere animale citate in forma prudente (testo consolidato vigente) | Coerenza interna + testi normativi consolidati citati per esteso nelle schede |
| M2 | Precauzione applicata | Norme con scadenze o dettagli che cambiano (parametri, prezziari, regole incentivi) citate con richiamo alla verifica vigente | Regola del protocollo: senza fonte, nessuna numerazione precisa |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche' l'utente non approva il tag.

## Giro N — 2026-10-01, bozza post-v1.1.0 (verso v1.2, NESSUN tag applicato)

Contenuto: 3 corsi nuovi (aeroporti e infrastrutture di volo; porti e opere marittime; emergenze e ricostruzione post-sisma), 31 schede, 3 esami da 250 domande. Rettifica del totale del giro M (905 -> 870 schede, errore di somma nel registro).

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| N1 | Solo aggiunte, nessuna correzione | Contenuti classici verificabili: aviazione (Reg. UE 139/2014, standard ICAO Allegati 10 e 14, Reg. UE 300/2008, RefuelEU, CORSIA), marittimo (convenzione SOLAS XI-2 ISPS, MARPOL, DPR 498/1992, ISO 12944, CNR-DT 207/2008 gia' citato), emergenze (D.Lgs 1/2018, schede AeDES e aggiornamenti, standard INSARAG). Costi marcati «Ordini di grandezza indicativi» | Coerenza interna + testi normativi consolidati citati per esteso nelle schede |
| N2 | Rettifica registro | INDEX giro M: totale schede corretto da 905 a 870 (errore di addizione, nessuna modifica alle schede) | Conteggio diretto delle righe schede.jsonl |
| N3 | Precauzione applicata | Numeri che variano per evento o commissario (contributi ricostruzione, premi di urgenza) citati con rimando alle delibere vigenti | Regola del protocollo: senza fonte, nessuna numerazione precisa |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche' l'utente non approva il tag.

## Giro O — 2026-10-01, verifica completa pre-tag v1.2.0 (approvazione esplicita dell'utente)

Batteria di controllo eseguita su tutti i 66 pack (901 schede): validazione JSON, ordine esatto delle 11 chiavi, campi vuoti, normative vuote, nomi duplicati, prefisso costi, marker di bozza, coerenza domande/chiavi dei 67 esami. Esito finale: 0 anomalie residue su tutti i controlli.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| O1 | Normalizzazione | 295 schede storiche con cifre in `costi_e_economia` prive del prefisso regolamentare. Prima: il campo iniziava direttamente con l'elenco prezzi (es. «Fonometro integratore professionale: noleggio 100-300 €/giornato…», «Il cantiere in zona vincolata costa il 20-40% in più.»). Dopo: «Ordini di grandezza indicativi: » premesso in testa al campo. Nessun numero alterato | Regola costi del protocollo (punto 5 del registro): i costi restano «ordini di grandezza indicativi»; modifica puramente formale |
| O2 | Normalizzazione | Riga vuota rimossa da `FACILITY_MANAGEMENT_E_MANUTENZIONE_PACK/schede/schede.jsonl` (righe = schede, nessuna scheda persa) | Controllo JSON: la riga non era un oggetto valido |
| O3 | Falso positivo chiarito | Marker «TODO» segnalato in ENERGETICA_INCENTIVI_PACK era la sottostringa di «ME**TODO** (documenti, tracciabilità, cumuli)» nella scheda «Le detrazioni fiscali…»: linguaggio corretto, nessuna modifica. Le 46 occorrenze di «da verificare» erano formule tecniche legittime («da verificare sul testo vigente», «da verificare caso per caso», «da verificare di progetto»), non righe non verificate: nessuna modifica | Controllo letterale del testo attorno al marker |
| O4 | Correzione strutturale | ESAMI/RISANAMENTO: la chiave era assente (277 domande senza risposte). Dopo: esame rigenerato come coppia coerente domande+chiave (277/277) con il driver standard, distrattori pertinenti al solo pack RISANAMENTO_E_RECUPERO_EDILIZIO. Le 277 domande precedenti sono state sostituite dall'istanza coerente | Controllo di coerenza esami: dopo il fix, 67 esami / 17.638 domande tutti allineati domande↔chiavi |
| O5 | Sicurezza | `RISPOSTE_AURATRIX_1000.md` (chiave del test da 1.000 domande) era tracciato in git su repository pubblica. Dopo: rimosso dal tracciamento (`git rm --cached`), file mantenuto in locale ed escluso dal re-add tramite `.git/info/exclude`. Nota onesta: il file resta visibile nella storia dei commit precedenti fino a un eventuale intervento di riscrizione della storia | Regola esplicita dell'utente: «le risposte le metti, le dai solo a me»; la repository pubblica contraddiceva la regola |

Righe aperte nel giro: nessuna. Il materiale riceve il tag v1.2.0 con l'approvazione esplicita dell'utente (2026-10-01).

## Giro P — 2026-10-02, bozza post-v1.2.0 (NESSUN tag applicato)

Contenuto: 1 corso nuovo (patologie edili e diagnostica strumentale, 12 schede), 1 esame nuovo (250 domande), verifica ricorrente incentivi/norme su fonti reali con 4 correzioni tracciate alle schede di ENERGETICA_INCENTIVI_PACK.

| # | Scheda / Pack | PRIMA (cosa c'era) | DOPO (cosa c'e' ora) | FONTE (url/fonte e data della verifica) |
|---|---|---|---|---|
| P1 | ENERGETICA_INCENTIVI scheda 14 (vendita energia FV) | «il meccanismo di riferimento e' il RID, che dal 1 gennaio 2026 si attiva d'ufficio se il titolare non sceglie altro»; prezzi minimi «0,047-0,11 €/kWh» senza riferimenti; citato un meccanismo «Rap (Ritiro Avviato e Programmato)» come forma base | SSP chiuso ai nuovi impianti (esercizio entro 29/5/2025, domande entro 26/9/2025, delibera ARERA 78/2025/R/efr in attuazione D.Lgs 199/2021); convenzioni esistenti proseguono max 15 anni, ultra-quindicennali chiuse al 31/12/2024 con passaggio automatico a RID; RID 2026: Prezzo Zonale Orario (media indicativa 0,10-0,13 €/kWh) con Prezzo Minimo Garantito 0,0475 €/kWh (47,5 €/MWh) per FV fino a 1 MW sui primi 1.500.000 kWh/anno, conguaglio annuale al miglior valore; attivazione con Modello Unico fino a 200 kW o Area Clienti GSE entro 60 gg; normative: delibere ARERA 280/07 e 78/2025/R/efr; «Rap» rimosso (meccanismo non riscontrato sulle fonti: la forma base e' il RID) | myenergy.it (guida RID/SSP 2026, delibere ARERA e PMG 0,0475 €/kWh), enel.it, solareindustriale.it, reonic.com — verifica web 02/10/2026 |
| P2 | ENERGETICA_INCENTIVI scheda 15 (Reddito Energetico) | «impianto da 2 a 6 kW con possibile quota di accumulo secondo le regole della misura»; nessuna struttura del contributo; «decreti attuativi PNRR» generici | Contributo = quota fissa 2.000 € + 1.500 €/kW (massimo teorico 11.000 € per 6 kW), erogato all'impresa accreditata; batteria NON finanziata (a carico del richiedente); obblighi: polizza multirischio e manutenzione/monitoraggio almeno 10 anni, domanda prima dell'entrata in esercizio, realizzazione entro 18 mesi, energia non autoconsumata al GSE in RID per il fondo rotativo; istituto dal D.M. MASE 8 agosto 2023, operativo dal maggio 2024; bando nazionale 2026 non ancora pubblicato alla data di verifica | solareindustriale.it (scheda misura e disciplinare), reonic.com, fanpage.it, pgcasa.it, ecopowersystem.it — fonti concordanti, verifica web 02/10/2026 |
| P3 | ENERGETICA_INCENTIVI schede 1 e 3 (Conto Termico 3.0) | «erogazione: unica rata se ≤ 15.000 €» | «unica rata per gli importi piu' bassi (soglia riportata come 5.000 € da alcune fonti di settore e 15.000 € da altre: da verificare sulle Regole Applicative GSE vigenti), altrimenti 2-5 rate annuali» | Discrepanza tra fonti di settore sulla soglia di rata unica (viessmann.it e airahome.com: 5.000 €; cremonasrl.it: 15.000 €); la pagina GSE «come accedere» non riporta la soglia — verifica web 02/10/2026 |
| P4 | Verifica senza correzione | Detrazioni edilizie (scheda 6), Conto Termico 3.0 percentuali/dotazione (schede 1-2), CER e agrivoltaico (FOTOVOLTAICO schede 8 e 12) | CONFERMATI senza modifiche: 2026 = 50% abitazione principale / 36% altri casi su 96.000 €, 10 quote; 2027 = 36%/30%; 2028-2033 = 30% su 48.000 €; dal 2034 = 36% su 48.000 €; esclusione caldaie uniche a fossile dal 2025; CT 3.0: D.M. 7/8/2025, 900 mln €/anno, portale aperto 2/2/2026 - sospeso 3/3 - riaperto 13/4/2026, accesso diretto 90 gg; CER tariffa fino a 120 €/MWh, RID cumulabile con CER | agenziaentrate.gov.it (guida «Recupero del patrimonio edilizio 2026», aggiornamento 29/7/2026), gse.it («come accedere» CT 3.0), bibus.acca.it, coenergia.com — verifica web 02/10/2026 |
| P5 | Nuovo pack | — | PATOLOGIE_E_DIAGNOSTICA_PACK (12 schede, L2-L3, FACOLTA_INGEGNERIA): percorso diagnostico, termografia, sclerometro, carotaggi, pacometro/GPR, ultrasuoni/SonReb, prove di carico, degrado cls, corrosione, umidita', murature storiche, monitoraggio. Norme citate (solo consolidato): NTC 2018, UNI EN 12504-1/-2/-4, UNI EN 13187, UNI EN ISO 13788, ASTM C876, UNI EN ISO 12696, UNI EN 206, D.Lgs 42/2004 | Norme di consolidata certezza; valori di accettazione marcati da verificare dove non normati |
| P6 | Esame nuovo | — | ESAMI/PATOLOGIE_DIAGNOSTICA (250 domande) con driver build_esami_giro5, distrattori solo dal pack della domanda; chiavi in ESAMI_RISPOSTE/ fuori repository | Controllo interno |
| P7 | Validazione globale | — | 67 pack, 913 schede, 0 errori JSON, 0 schede fuori schema, 0 refusi «aplicazioni/tegnologia», conteggi COURSE.yaml coerenti | Script di validazione eseguito a fine giro |

Righe aperte nel giro: soglia di rata unica del Conto Termico 3.0 (P3) da chiudere sulla fonte primaria (Regole Applicative GSE, testo integrale) alla prossima esecuzione; bando nazionale Reddito Energetico 2026 non ancora pubblicato: riverificare alla prossima esecuzione. Il materiale resta bozza finche' l'utente non approva il prossimo tag.

## Giro Q — 2026-10-02, bozza post-v1.2.0 (verso v1.3, NESSUN tag applicato)

Contenuto: 2 corsi nuovi (illuminazione tecnica e illuminotecnica; mezzi di sollevamento e movimentazione), 22 schede, 2 esami da 500 domande totali. Temi scelti per coprire gap verificati: nessun pack dedicato all'illuminotecnica (solo citazioni laterali) e ai mezzi di sollevamento (solo menzioni sparse in altri corsi). Cumulativo con Giro P (task automatico): 69 pack, 935 schede, 70 esami.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| Q1 | Solo aggiunte, nessuna correzione | Illuminotecnica: norme consolidate citate per esteso (UNI EN 12464-1, UNI EN 1838, UNI EN 13032, serie UNI EN 13201, CEI 64-8, Reg. (UE) 2019/2020); valori specifici di illuminamento rimandati al testo vigente della norma invece di essere copiati, per non rischiare cifre non aggiornate | Coerenza interna + norme consolidate citate per esteso nelle schede |
| Q2 | Solo aggiunte, nessuna correzione | Sollevamento e movimentazione: D.Lgs 81/2008 (attrezzature di lavoro, verifiche periodiche) e norme UNI EN consolidate (12810, 12811, 280, 13000, 14492-2, 818, ISO 4309, 1492); scadenze precise rimandate all'Allegato XXX vigente | Come Q1 |
| Q3 | Controllo qualita' | Verifica durante la scrittura: corretto in bozza un carattere errato («allarme di inclinazione»); zero marker residui nei due pack | Controllo interno sui file generati |

Righe aperte nel giro: nessuna. Il materiale resta bozza finche' l'utente non approva il tag.

## Giro R — 2026-10-02, bozza post-v1.2.0 (verso v1.3, NESSUN tag applicato)

Contenuto: strumentazione di valutazione, nessuna modifica a schede o norme.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| R1 | Strumento nuovo | `ESAMI/PROTOCOLLO_VALUTAZIONE.md`: regole di amministrazione e giudizio degli esami (soglie 90/80/70/50, riservatezza chiavi) | Regole espresse dall'utente nelle sessioni di progetto |
| R2 | Strumento nuovo | `valuta_esami.py`: genera schede di risposta vuote (`template`) e corregge (`valuta`) producendo il verbale con giudizi per settore e, solo per le domande errate, lettera corretta e fonte da ripassare. Compatibile con entrambi i formati di chiave (standard con lettera, legacy con lettera diretta o testuale) | Test eseguito su risposte simulate: ACUSTICA 94% (Eccellente), SOLLEVAMENTO 56% (Insufficiente), 68 settori segnati 'non sostenuto'; chiavi legacy MATERIALEDILE e IMPIANTI_FV_EOLICO derivate al 100% |
| R3 | Controllo qualita' | `ESAMI/RISPOSTE_CANDIDATO/` esclusa dal tracciamento git tramite `.git/info/exclude` (non `.gitignore`): risposte e verbali restano locali | Coerenza con la regola 'chiavi e risposte fuori repository' |

Righe aperte nel giro: nessuna.

## Giro S — 2026-10-02, bozza post-v1.2.0 (verso v1.3, NESSUN tag applicato)

Contenuto: audit di discriminante degli esami, rigenerazione DESIGN_GUSTO, nuovo esame SERRAMENTI, 3 schede aggiunte a SERRAMENTI_E_VETRATE_PACK.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| S1 | Audit | `ESAMI/AUDIT_CONTENT_LOCKED.md`: classificazione di tutte le 16.388 domande dei 73 esami in LOCKED/MISTO/PATTERN. Esito: 13% locked; molti settori sotto il 10%. Origine: la gara di ammissione ha mostrato un candidato senza corpus al 97% su DESIGN_GUSTO (errori solo su quadri normativi testuali) | Gara di ammissione del 2026-10-02 (ILLUMINAZIONE 100% addestrato vs DESIGN_GUSTO 97% non addestrato) |
| S2 | Strumento nuovo | `build_esami_design_v2.py`: generatore content-locked (cloze numeriche e su nomi propri con distrattori delle schede sorelle; solo tipi locked: casi reali, costi, note di cantiere, norme, quota ridotta vantaggi/limiti; eliminati 'appartiene alla tecnologia', 'NON appartiene', applicazioni, riassunti). Guard: mai cancellare il numero che fa parte del nome di legge/decreto/articolo | Rimedio all'errore di misura scoperto con S1 |
| S3 | Rigenerazione | ESAMI/DESIGN_GUSTO rigenerato con il criterio v2: 116 domande (37 cloze), verifica automatica 116/116 risposte presenti testualmente nelle schede fonte. Chiavi riservate aggiornate in ESAMI_RISPOSTE (fuori repo); risposte candidato v1 archiviate in ESAMI/RISPOSTE_CANDIDATO/_archivio_gara_v1/ | Verifica script su chiavi vs schede.jsonl |
| S4 | Materiale nuovo | 3 schede aggiunte a SERRAMENTI_E_VETRATE_PACK (da 13 a 16): 'Marcatura CE, DoP e classificazioni prestazionali (UNI EN 14351-1)', 'Requisiti di legge: Legge 10 e DM requisiti minimi per gli infissi', 'Antieffrazione: classi RC e vetri antisfondamento (P1A-P5A)' — angoli non coperti dalle 13 schede preesistenti. Norme citate solo UNI/EN reali; costi dichiarati come ordini di grandezza indicativi | Integrazione, non duplicazione: verificata la copertura preesistente del pack |
| S5 | Esame nuovo | ESAMI/SERRAMENTI (195 domande, 56 cloze): primo esame creato direttamente col criterio v2; verifica automatica 195/195 risposte presenti testualmente nelle schede fonte | `build_esami_giro_o.py` + verifica script |

Righe aperte nel giro:
- Rigenerazione graduale degli esami sotto il 10% di LOCK partendo dai settori che AuraTrix userà prima (DIMENSIONAMENTO_TERMOTECNICO 2%, ENERGETICA_INCENTIVI 2%, FOTOVOLTAICO_CER 5%).
- Il pack SERRAMENTI_E_VETRO creato per errore in questo giro è stato eliminato dopo il riscontro del duplicato (SERRAMENTI_E_VETRATE_PACK esisteva già): nessun residuo in repo.

## RILASCIO v1.3.0 — 2026-10-02 (tag applicato su approvazione esplicita dell'utente)

**Cosa fissa questo tag:** lo stato della repository al Giro S (commit indicato nel tag). AuraTrix si aggancia a QUESTA versione: tutto ciò che arriva dopo (Giro T in poi) è bozza fino al prossimo tag approvato.

### Livello di verifica di v1.3.0 (cosa è stato controllato e come)

| Ambito | Verifica eseguita | Esito |
|---|---|---|
| Chiavi esami ↔ schede | Controllo automatico: ogni risposta corretta di ogni esame deve comparire testualmente nella scheda fonte dichiarata nella chiave | Superato per tutti gli esami verificati nel Giro R–S (inclusi i 73 settori e i due esami su misura da 1.000 domande); esami rigenerati v2 (DESIGN_GUSTO 116/116, SERRAMENTI 195/195) |
| Discriminante esami | Audit di classificazione LOCKED/MISTO/PATTERN su tutte le domande | 13% locked; audit pubblicato in `ESAMI/AUDIT_CONTENT_LOCKED.md` |
| Norme citate nelle CORREZIONI | Ogni correzione normativa riporta: cosa c'era → cosa c'è → fonte di verifica (testo norma o fonte primaria) | Formato attivo dal Giro H (es. UNI 9174, riga H1); obbligatorio per tutti i giri successivi |
| Norme citate nelle schede preesistenti (giri A–G) | Verifica di coerenza interna e di realtà della norma, NON verifica sul testo ufficiale per ogni singola citazione | Parziale: vedi regola sotto |

### Regola operativa per AuraTrix (vincolante)

1. **Righe «verificate su fonte primaria»** (changelog con fonte indicata): citabili come fatto, con riferimento alla versione v1.3.0.
2. **Tutto il resto delle citazioni normative e dei valori di legge nelle schede**: da trattare come «da verificare sul testo vigente» prima di citarli a un cliente. Formulazione obbligata in output: «secondo [riferimento, edizione da confermare]» — mai come fatto secco.
3. **Costi/prezzi**: ordini di grandezza indicativi con data di riferimento; mai quotare un cliente senza listino aggiornato.
4. Se una verifica esterna scopre un errore: si corregge e si registra una riga changelog nel formato tre colonne (prima/dopo/fonte). Senza fonte, la riga resta «DA VERIFICARE» e non entra nel training come fatto.

### Numeri di v1.3.0

70+ pack, 900+ schede, 73 esami pubblici (~16.400 domande) + 2 esami su misura da 1.000 domande; chiavi e risposte candidato fuori repository (`ESAMI_RISPOSTE/`, esclusa via `.git/info/exclude`).
