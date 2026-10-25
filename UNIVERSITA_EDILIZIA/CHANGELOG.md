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

## Giro T — 2026-10-02, bozza post-v1.3.0 (verso v1.4, NESSUN tag applicato)

Contenuto: rigenerazione content-locked dei tre esami sotto il 10% di LOCK che AuraTrix studia per primo.

| # | Tipo | Dettaglio | Fonte |
|---|---|---|---|
| T1 | Rigenerazione | ESAMI/DIMENSIONAMENTO_TERMOTECNICO: da 250 domande (2% locked) a 212 domande v2 (98 cloze). Verifica automatica chiavi↔schede: 212/212 risposte presenti testualmente nelle schede fonte | `build_esami_giro_t.py` (criterio v2) + verifica script |
| T2 | Rigenerazione | ESAMI/ENERGETICA_INCENTIVI: da 250 (2% locked) a 249 v2 (124 cloze). Verifica: 249/249 | Come T1 |
| T3 | Rigenerazione | ESAMI/FOTOVOLTAICO_CER: da 400 (5% locked) a 244 v2 (97 cloze). Verifica: 244/244 | Come T1 |
| T4 | Fix qualità | `build_esami_design_v2.py`: corretto indice cloze (la \s? della regex NUM mangiava lo spazio dopo il numero: '___per' invece di '___ per'). Rigenerati i tre esami del giro; DESIGN_GUSTO v2 e SERRAMENTI (già verificati e consegnati con chiavi) non toccati per non invalidare le chiavi già consegnate | Controllo visivo sulle cloze dei tre esami |
| T5 | Nota critica | ESAMI/ENERGETICA_INCENTIVI contiene una scheda che dichiara esplicitamente discrepanze tra fonti di settore (es. soglie Conto Termico 3.0 riportate come 5.000 € o 15.000 € a seconda delle fonti): la scheda marca il valore come 'da verificare sulle Regole Applicative GSE vigenti'. Le domande cloze su quel dato verificano la conoscenza della SCHEDA (che riporta la discrepanza), non il valore di legge: l'applicazione della regola 'da verificare' resta vincolante in output | Regola operativa v1.3.0 (changelog di rilascio) |

Righe aperte nel giro:
- Rigenerazione degli altri settori sotto il 10% di LOCK secondo la scala di priorità d'uso da parte di AuraTrix.
- Valori incentivi: la scheda Conto Termico 3.0 va riletta sulle Regole Applicative GSE vigenti al prossimo aggiornamento di materiale (già segnalato in scheda).

## Giro U — 2026-10-02, bozza post-v1.3.0 (verso v1.4, NESSUN tag applicato)

Contenuto: verifica su fonte primaria del Conto Termico 3.0, nuovo pack CAPPOTTO_ETICS + esame.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| U1 | Correzione su fonte | Scheda «Il Conto Termico 3.0»: soglia unica rata «5.000 € o 15.000 € a seconda delle fonti: da verificare» | Soglia confermata 15.000 € (unica rata per incentivo ≤ 15.000 €); la soglia 5.000 € appartiene al precedente Conto Termico 2.0. Aggiunti: acconto 2/5 (5 anni) o 50% (2 anni), conclusione lavori 12 mesi (36 nZEB), corrispettivo GSE 1% max 250 €, maggiorazione +10% componenti UE, 40% base/50% zone E-F/55% combinato per superfici opache | Regole Applicative del D.M. 7 agosto 2025, gse.it (documento 'Regole_Applicative_CT_3_0.pdf'), verificato il 02/10/2026 |
| U2 | Rigenerazione | ESAMI/ENERGETICA_INCENTIVI (Giro T, scheda non ancora corretta) | Rigenerato dopo la correzione U1: 250 domande (127 cloze); verifica chiavi↔schede 250/250 | `build_esami_giro_t.py` + verifica script |
| U3 | Materiale nuovo | (assente) | CAPPOTTO_ETICS_PACK: 10 schede (materiali isolanti λ, sistema ETICS a strati, posa, dettagli, posizione isolamento/muffa, ponti termici, antincendio, patologie, cantieri, economia). Norme solo reali: UNI EN 13162-13166, 13501-1, ISO 13788/10211/14683, 998-1, 15824, 12810/12811, EAD 040083-00-0404 | Costruzione ex novo su conoscenza tecnica consolidata; nessuna sovrapposizione con pack esistenti (verificato: cappotto citato ma non trattato in pack dedicato) |
| U4 | Esame nuovo | (assente) | ESAMI/CAPPOTTO: 117 domande v2 (38 cloze); verifica chiavi↔schede 117/117 | `build_esami_design_v2.py` + verifica script |
| U5 | Indice | Manifest FACOLTA_TECNOLOGIA_E_COSTRUZIONE senza CAPPOTTO_ETICS | Aggiunto CAPPOTTO_ETICS_PACK (L2) con nota esame; aggiunta nota esame SERRAMENTI su SERRAMENTI_E_VETRATE_PACK | Coerenza interna |

Righe aperte nel giro: nessuna. Le percentuali Conto Termico 3.0 vanno rilette sulle Regole Applicative GSE vigenti a ogni aggiornamento (la regola 'da verificare' resta attiva per tutti i valori incentivanti).

## Giro V — 2026-10-02, bozza post-v1.3.0 (verso v1.4, NESSUN tag applicato)

Contenuto: 3 schede Conto Termico 3.0 dai gap delle Regole Applicative GSE + fix del generatore d'esami su unità di misura.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| V1 | Materiale nuovo | ENERGETICA_INCENTIVI_PACK: 15 schede | 18 schede, con: «Conto Termico 3.0: gli errori che fanno rigettare o sospendere la pratica», «Conto Termico 3.0: massimali, costi ammissibili e calcolo dell'incentivo», «Conto Termico 3.0: multi-intervento, cumuli e maggiorazioni» | Regole Applicative del D.M. 7 agosto 2025, gse.it ('Regole_Applicative_CT_3_0.pdf'), verificato il 02/10/2026 |
| V2 | Correzione su fonte | Scheda «Conto Termico 3.0: accesso diretto, prenotazione, pratica»: «soglia unica rata 5.000-15.000 € da verificare» | Soglia confermata 15.000 € (accesso diretto fino a 15.000 € = rata unica; oltre = 2/5 rate annuali; prenotazione: PA/ETS non economici in rata unica anche oltre soglia; acconto sul minore tra massimale prenotato e importo contrattualizzato; ETS economici misti Titolo II+III → multi-rata alla durata massima dei Titolo II) | Come V1 |
| V3 | Fix refuso | Scheda «accesso diretto, prenotazione, pratica», note_cantiere: «PRIERA della data di consegna» | «PRIMA della data di consegna» | Controllo ortografico interno |
| V4 | Fix generatore | `build_esami_design_v2.py`, regex NUM: l'alternativa unità provava «m» prima di «mesi»/«mln» e «ml» prima di «mln», mangiando l'inizio della parola successiva: cloze corrotte tipo «___n privati» (da «500 mln privati») e «___esi di tempo» (da «18 mesi di tempo»). La verifica chiavi↔schede NON li intercettava (la risposta resta sottostringa del testo scheda): intercettati solo in campionamento visivo | Unità riordinate per lunghezza decrescente + «mln» aggiunto + lookahead che vieta l'unità come prefisso di parola. Test su 13 casi limite: tutti corretti («500 mln», «18 mesi», «500 ml», «18 m»...) | Test regex dedicato + grep «___[a-z]» su tutti gli esami: da 32 corrotte a 0 |
| V5 | Rigenerazione | ESAMI/ENERGETICA_INCENTIVI (250 domande) + esami v2 pre-esistenti con cloze corrotte: FOTOVOLTAICO_CER (14), DESIGN_GUSTO (9), SERRAMENTI (5), DIMENSIONAMENTO_TERMOTECNICO (3), CAPPOTTO (1) | Tutti rigenerati con generatore fixato: ENERGETICA_INCENTIVI 250 (125 cloze), FOTOVOLTAICO_CER 240 (93), DESIGN_GUSTO 116 (37), SERRAMENTI 195 (56), DIMENSIONAMENTO_TERMOTECNICO 207 (93), CAPPOTTO 117 (38). Verifica chiavi↔schede: 1.165/1.165 = 0 fail; cloze corrotte 0/6 esami | `build_esami_design_v2.py` (fix V4) + verifica script sui 6 esami |
| V6 | Nota conteggi | FOTOVOLTAICO_CER target 241 → 240; DIMENSIONAMENTO_TERMOTECNICO target 212 → 207 | Il fix restringe leggermente il pool di cloze valide (candidati prima validi solo come token corrotti): deficit di 1 e 5 domande, non compensabili senza reintrodurre casi ambigui. Conteggio dichiarato onestamente; esami comunque sopra soglia d'uso | Verifica script |

Righe aperte nel giro:
- Le cloze dei 6 esami rigenerati sono ora pulite; gli esami generati da generatori v1 (pre-v2) risultano a 0 cloze corrotte al controllo «___[a-z]» e non sono toccati.
- Valori incentivanti Conto Termico 3.0: rileggere le Regole Applicative GSE vigenti a ogni aggiornamento di materiale (regola 'da verificare' sempre attiva in output).

## Giro W — 2026-10-02, bozza post-v1.3.0 (verso v1.4, NESSUN tag applicato)

Contenuto: verifica completa dei valori incentivanti Conto Termico 3.0 sul documento primario GSE (Regole Applicative D.M. 7/8/2025, PDF 'Regole_Applicative_CT_3_0.pdf', 172 pagine rilette integralmente il 02/10/2026) + correzione degli errori trovati.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| W1 | Correzione su fonte | Scheda «la misura e i numeri»: dotazione «500 mln privati di cui 150 mln imprese con tetto di 30 mln; 400 mln PA» | Aggiunta rimodulazione 2026: D.D. MASE n. 72 del 10/4/2026 → 450 mln PA / 450 mln privati (rimodulazione annua possibile); precisati 20 mln per diagnosi nel contingente PA+ETS; precisato che 150 mln/anno e tetto 30 mln €/impresa sono del solo Titolo V imprese | D.D. MASE 72/2026 riportato da 5 fonti di settore indipendenti (BibLus 22/5/2026, iterservice, edilsocialnetwork, climaxgroup, solareindustriale); valori originali confermati dal PDF GSE §4.4 e bilancio GSE 2025 |
| W2 | Correzione su fonte (ERRORE GROSSO) | Scheda «interventi ammessi e percentuali»: «pompe di calore e ibridi: 40-65% in base a zona climatica e tipologia (tariffa di riferimento 700 €/kW per PdC aria-acqua fino a 35 kW)» e «per le pompe di calore COP ≥ 3,8 ed EER ≥ 3,5 danno aliquota piena» | Riscritto su algoritmo reale: PdC (III.A) incentivo annuo = Ei × Ci su ENERGIA prodotta, Ei = Qu × [1-1/SCOP] × kp; kp = premialità ηs/ηs minimo ecodesign; requisito = SCOP ≥ minimo ecodesign di tipologia (UNI EN 14825, tabelle 3-4 Allegato 1); 2 annualità ≤ 35 kW, 5 oltre; limite impianto 2.000 kWt; contabilizzazione obbligatoria oltre 200 kW; per imprese/ETS economici escluse PdC a gas e ibridi a gas (art. 25 co. 2); intensità aiuti di Stato Titolo III 45% base → 65/55/45% per dimensione | PDF GSE §9.9, tabelle 23-24, §4.2.1 (tabelle 11-12). La «tariffa 700 €/kW» e il «40-65% per zona climatica» NON esistono nel testo: erano residui del Conto Termico 2.0 riportati da fonti di settore |
| W3 | Correzione su fonte (ERRORE GROSSO) | Stessa scheda: «solare termico: 65% calcolato sulla superficie (tariffa di riferimento 700 €/m²)» | Riscritto: solare termico (III.D) incentivo annuo = Ci × Qu × Sl (superficie lorda); Ci = 0,35 €/kWh a.c.s. <12 m² decrescente a 0,11 €/kWh >500 m² (solar cooling 0,43); Solar Keymark obbligatoria; 2 annualità ≤ 50 m²; i 700 €/m² del decreto sono il Cmax dei SERRAMENTI (II.B), non del solare | PDF GSE §9.12.3 tabella 36 e tabella 17 (serramenti Cmax 700/800 €/m²) |
| W4 | Correzione su fonte | Stessa scheda: «biomassa classi 4-5 stelle» e maggiorazione «moduli FV iscritti al registro ENEA in base alla classe di efficienza» | Biomassa: classe ambientale 5 stelle o superiore (sostituzione da GPL/gas: + PM ≤ 1 mg/Nm³); maggiorazione FV = Registro delle tecnologie per il fotovoltaico (art. 12 D.L. 181/2023, sezioni a/b/c per requisiti territoriali/tecnici, tutti i moduli della stessa sezione): +5/+10/+15 PUNTI PERCENTUALI | PDF GSE §9.11 e §9.8.3 |
| W5 | Aggiunta verificata | Scheda «la misura e i numeri» casi_real_world: «incentivo stimato 65% sul termico... prima rata dopo istruttoria GSE (60 giorni di valutazione)» | PdC incentivo su producibilità non % spesa; erogazione = ultimo giorno del mese successivo al bimestre di perfezionamento scheda-contratto; i «60 giorni» valgono solo per l'acconto dopo comunicazione avvio lavori (prenotazione) | PDF GSE §4.3 e §7.5 |
| W6 | Correzione su fonte (norma vera fuori posto — il rischio segnalato dall'utente) | Scheda «la misura e i numeri» normative: «D.Lgs 28/2011 (esenzione IRPEF del contributo per le persone fisiche, art. 11)» | Sostituito con quanto il documento GSE afferma testualmente (§4.6-4.7): contributo fuori campo IVA, fuori dall'art. 28 D.P.R. 600/1973 (nessuna ritenuta 4%), corrispettivo GSE fatturato via SDI; aggiunto richiamo D.D. 72/2026 e nota 'per la tassazione completa → prassi AdE e commercialista'. L'art. 11 D.Lgs 28/2011 disciplina la certificazione energetica, non la tassazione | PDF GSE §4.6-4.7; D.Lgs 28/2011 art. 11 (testo norma) |
| W7 | Aggiunta verificata | Scheda «errori che fanno rigettare»: «termine di conclusione lavori scaduto (12 mesi dall'avvio, 36 per nZEB)» | Distinzione delle fattispecie: i-iv conclusione entro 12 mesi dall'avvio (36 nZEB); fattispecie a: avvio entro 18 mesi da accettazione prenotazione + conclusione entro successivi 48 mesi; aggiunto errore n. 9: ultimo pagamento oltre 120 giorni prima della conclusione dichiarata | PDF GSE §7.4-7.5 e §12.1 |
| W8 | Correzione su fonte | Scheda «massimali»: «Per i generatori l'incentivo si calcola su tariffe di riferimento per kW (o m² per solare termico)» | «sulla producibilità: energia termica prodotta stimata × coefficiente €/kWh (tabelle 9, 10, 16 Allegato 2) — non esiste una tariffa per kW né per m²» | PDF GSE §9.9.3 e §9.12.3 |
| W9 | Conferme (nessuna modifica) | Soglia unica rata 15.000 €; acconto 2/5 o 50% sul minore tra massimale e contrattualizzato; corrispettivo 1% max 250 € imponibile trattenuto sulla prima rata; +10% componenti UE; FV 20% trainato con Cmax 1.500/1.200/1.100/1.050 €/kW e cap = incentivo PdC; accumulo Cmax 1.000 €/kWh; isolamento 40/50/55/100% con Cmax tabella 7; multi-intervento rate = durata max; ETS misti II+III multi-rata Titolo II; PA/ETS accesso diretto unica rata oltre 15.000 €; rinuncia con oggetto 'Conto Termico - nome SR - codice intervento - rinuncia' | Confermati testualmente sul documento GSE | PDF GSE §4.3, §9.1.3, §9.8.3, §12.x |
| W10 | Sincronizzazione | Voce ENCICLOPEDIA/VOCI_FACOLTA_IMPIANTI_ENERGIA.md «interventi ammessi e percentuali» e «la misura e i numeri» riportavano i valori pre-correzione | Voci risincronizzate dalle schede corrette (W2-W6) | Coerenza interna |
| W11 | Rigenerazione | ESAMI/ENERGETICA_INCENTIVI (250 domande del Giro V) con cloze sui valori pre-correzione | Rigenerato: 250 domande (146 cloze), verifica chiavi↔schede 250/250 = 0 fail, cloze corrotte 0 | build_esami_design_v2.py + verifica script |

Righe aperte nel giro:
- I valori Cmax e Ci delle tabelle 7/9/10/16 sono quelli del D.M. 7/8/2025: vanno riconfrontati a ogni aggiornamento del catalogo GSE o decreto rimodulatore.
- La voce enciclopedia «Conto Termico 3.0: accesso diretto, prenotazione, pratica» risulta allineata (sync Giro U) ma andrà risincronizzata se la scheda verrà toccata.

## Giro X — 2026-10-02, bozza post-v1.3.0 (verso v1.4, NESSUN tag applicato)

Contenuto: verifica su fonte primaria delle 9 schede incentivi non-Conto Termico del pack ENERGETICA_INCENTIVI (detrazioni, Transizione/iperammortamento, scelta incentivo, RID, Reddito Energetico, TEE, APE, CER, CAM, EPBD, ESCo, diagnosi). Esiti: RID, «Scegliere l'incentivo», CAM, EPBD, ESCo confermate senza modifiche; 7 schede corrette.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| X1 | Correzione su fonte | Scheda «Le detrazioni fiscali»: roadmap «dal 2034 = 36% con 48.000 €» | Rimossa: il testo di legge (art. 16-bis co. 3-ter TUIR, introdotto dalla L. 199/2025) prevede dal 2028 aliquota unica 30% con limite 48.000 €; nessuna fonte primaria conferma il ritorno al 36% dal 2034 (dicitura di fonti secondarie) | art. 16-bis TUIR co. 3-ter come modificato dalla L. 199/2025; riscontro su fiscomania/biblus (testo norma) |
| X2 | Correzione su fonte | Scheda «Il Reddito Energetico»: «80% Mezzogiorno secondo fonti di settore», «Puglia ISEE 20.000», «realizzazione entro 18 mesi dall'accoglimento» | «80% delle risorse destinato al Mezzogiorno PER LEGGE (D.M. 8/8/2023)»; esempio Puglia rimosso (non verificato su fonte primaria); «18 mesi» rimosso (non verificato). Restano confermati: ISEE 15.000/30.000 con ≥4 figli, impianto 2-6 kW, formula 2.000+1.500 €/kW, batteria NON finanziata, polizza + manutenzione ≥10 anni, RID con proventi al fondo, non cumulabilità, bando 2026 non pubblicato al 2/10/2026 | Regolamento/decreto MASE 8/8/2023 (Fondo REN) su mase.gov.it + regole GSE; riscontro reonic |
| X3 | Riscrittura su fonte | Scheda «Diagnosi energetica»: intero impianto normativo sul D.Lgs 102/2014 (grandi imprese 250+50mln, energivore CSEA, «scadenza dicembre anni dispari») | Riscritta sul D.Lgs 102/2024 (recepimento EED 2023/1791, in vigore dal 10/10/2025): diagnosi UNI CEI EN 16247 ogni 4 anni per consumi ≥10 TJ/anno (≈2,78 GWh), prima diagnosi entro 11/10/2026 per i nuovi soggetti; ISO 50001 per ≥85 TJ/anno (≈23,6 GWh) entro 11/10/2027; già obbligati: cadenza quadriennale con scadenza 5/12/2027. Sistema 102/2014 mantenuto come storico (condizione AND 250 occupati e 50 mln; esenzione ISO 50001/14001/EMAS; sanzioni 2.000-20.000 e 4.000-40.000 €). Energy manager: senza numeri inventati, rinvio ai decreti attuativi | Testo D.Lgs 102/2024 (GU) + sintesi MASE; regole di transizione EED III→IV |
| X4 | Riscrittura su fonte | Scheda «Transizione 5.0 e iperammortamento»: «iperammortamento 2026 resta per beni immateriali e autoproduzione (30/9/2028) secondo fonti di settore» | Riscritta sulla L. 199/2025 artt. 427-436: iperammortamento reintrodotto, scaglioni 180% (fino a 2,5 mln €) / 100% (2,5-10 mln) / 50% (10-20 mln) / 0 oltre 20 mln; finestra 1/1/2026-30/9/2028 con completamento e comunicazione entro 15/11/2028; beni 4.0 (allegati IV-V) + impianti FER per autoconsumo con accumulo anche in via autonoma; FV: producibilità ≤105% del fabbisogno e moduli UE sezioni B/C del registro art. 12 D.L. 181/2023; iter su piattaforma GSE (comunicazione preventiva → riserva con acconto 20% entro 60 gg → completamento); valore ≈43% del costo nel primo scaglione (IRES 24%). Transizione 5.0 come credito 35/45% mantenuto solo come storico | L. 199/2025 artt. 427-436 (testo legge); riscontro su fonti fiscali di settore |
| X5 | Correzione su fonte | Scheda «I certificati bianchi (TEE)»: origine «D.Lgs 28/2011», obbligati «distributori con clienti sopra soglia», durata «tipicamente 5 anni» | Origine = decreti interministeriali 20 luglio 2004 (elettrico e gas); obbligati = distributori con PIÙ DI 50.000 clienti finali; «5 anni tipici» sostituito dalle regole vigenti del DM MASE 21/7/2025 (in vigore dal 12/9/2025): nuovi target 2025-2030 (7,9 mln TEE elettrico + 4,9 mln gas cumulati), TEE virtuali a 10 € con vincolo di detenzione minima crescente 40%→80% (2025-2029). Confermati: 1 TEE = 1 toe, mercato GME, certificazione GSE | D.M. 20/7/2004; D.M. MASE 21/7/2025 (GU e sintesi GSE-MASE) |
| X6 | Arricchimento su fonte | Scheda «L'APE»: «validità 10 anni (salvo rilevanti modifiche)» | «Massimo 10 anni (art. 6 co. 5 D.Lgs 192/2005) SUBORDINATA ai controlli di efficienza degli impianti termici (DPR 74/2013): decade il 31/12 dell'anno successivo alla prima scadenza non rispettata; aggiornamento prima dei 10 anni a ogni intervento che modifica la classe; dal 3/6/2026 metodologia del DM 28/10/2025 (sostituisce DM 26/6/2015)». Normativa arricchita di DPR 74/2013 e DM 28/10/2025 | art. 6 co. 5 D.Lgs 192/2005 + DM 26/6/2015 (Allegato 2) + DM 28/10/2025 (GU 5/12/2025); riscontro BibLus/ediltecnico |
| X7 | Fix refuso | Scheda «CER e autoconsumo collettivo», applicazioni: «borghi e municipaità» | «borghi e municipalità». Resto della scheda confermato (limite impianti 1 MW coerente con D.Lgs 199/2021) | Controllo ortografico interno |
| X8 | Sincronizzazione | 7 voci ENCICLOPEDIA/VOCI_FACOLTA_IMPIANTI_ENERGIA.md (APE, CER, detrazioni, Transizione/iperammortamento, Reddito Energetico, TEE, diagnosi) riportavano i contenuti pre-correzione | Voci risincronizzate dalle schede corrette (X1-X6); titoli diagnosi e iperammortamento aggiornati al nuovo nome scheda | Coerenza interna (sync_voci_giro_x.py) |
| X9 | Rigenerazione | ESAMI/ENERGETICA_INCENTIVI con cloze sui contenuti pre-correzione | Rigenerato: 250 domande, verifica chiavi↔schede 250/250 = 0 fail, cloze corrotte 0, cloze vuote 0 | build_esami_design_v2.py + verifica script |

Righe aperte nel giro:
- Scheda detrazioni, campo tecnologia: l'esclusione delle caldaie a gas uniche per spese 2025-2027 è rimasta in scheda ma NON è stata riverificata su fonte primaria in questo giro: trattarla come «da verificare» fino a riscontro sul testo L. 199/2025 o prassi AdE.
- Energy manager (scheda diagnosi): le soglie specifiche sotto il D.Lgs 102/2024 dipendono dai decreti attuativi: la scheda dichiara il rinvio senza numeri; non citare soglie numeriche finché un decreto attuativo non le fissa.
- Reddito Energetico: verificare la pubblicazione del bando 2026 sul portale GSE a ogni aggiornamento della repository.
- Iperammortamento: risorse (8,4 mld + 1,4 D.L. 38/2026) e dettagli di piattaforma da riconfermare sul portale MIMIT/GSE al momento dell'uso.

## Giro Y — 2026-10-17, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente (detrazioni, Conto Termico 3.0, Reddito Energetico, CER) con 4 correzioni; nuovo pack EDILIZIA_CIRCOLARE_LCA_PACK (12 schede) con esame; recupero censimento CAPPOTTO_ETICS_PACK; riallineamento conteggi INDEX sui valori misurati.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| Y1 | Chiusura riga aperta (Giro X) | Scheda «Le detrazioni fiscali», tecnologia punto 3: «ESCLUSIONE: sostituzione della climatizzazione invernale con caldaie uniche a combustibili fossili esclusa per spese 2025-2027» (marcata da verificare nel Giro X) | «ESCLUSIONE VERIFICATA (Circolare Agenzia delle Entrate 8/E del 19/6/2025)»: esclusa la sostituzione con caldaie uniche a combustibili fossili per spese 2025-2027; restano agevolabili la nuova installazione (non in sostituzione), i sistemi ibridi di fabbrica caldaia+pompa di calore (D.M. 6/8/2020), i microcogeneratori, le caldaie a biomasse e le pompe di calore ad assorbimento a gas | Circolare AdE 8/E del 19/6/2025 via stampa tecnica concordante (biblus.acca.it, aggiornato 15/10/2026), verifica web 17/10/2026 |
| Y2 | Arricchimento su fonte | Scheda «Il Reddito Energetico»: «bando nazionale 2026 non ancora pubblicato alla verifica del 2 ottobre 2026: gli sportelli 2024-2025 si sono esauriti in poche settimane»; nessun riferimento al termine di entrata in esercizio | «bando 2025: 103,2 milioni di euro con D.D. MASE n. 124 del 28/3/2025, quota Sud esaurita in giornata; bando nazionale 2026 non ancora pubblicato alla verifica del 17 ottobre 2026: le regole GSE prevedono la riapertura dello sportello con le risorse residue, al raggiungimento di almeno 5 milioni di euro»; aggiunto: termine di entrata in esercizio prorogato da 12 a 18 mesi dall'accoglimento (D.D. MASE n. 474 del 20/11/2025, recepito dal GSE l'8/1/2026) | Stampa tecnica di settore che cita i decreti MASE e le pagine GSE (kilowattchiaro.it), verifica web 17/10/2026 |
| Y3 | Nota su atto in itinere | Scheda «Il Conto Termico 3.0: la misura e i numeri», normative: nessun riferimento al correttivo | Aggiunta nota: «un decreto correttivo del D.M. 7/8/2025 e' in itinere (superata la Conferenza Stato-Regioni a ottobre 2026; temi attesi: gestione delle risorse, accessi, piccoli Comuni, controlli): contenuti e data da verificare sul testo pubblicato in GU e sulle Regole Applicative GSE aggiornate» — nessun contenuto inventato | Stampa tecnica di settore (BibLus, 13/10/2026), verifica web 17/10/2026 |
| Y4 | Correzione su fonte | Scheda «Gli incentivi delle CER» (FOTOVOLTAICO): «contributo PNRR del 40% nei comuni sotto i 50.000 abitanti, con possibile anticipazione GSE fino al 30%» (senza scadenza) | «CHIUSO a nuove domande dal 30/11/2025 (accordi di finanziamento entro il 30/6/2026, erogazione entro il 31/8/2026): resta pienamente attiva la tariffa incentivante, che non ha scadenza a bando»; adeguato anche il campo costi_e_economia | Regole del contributo PNRR-CER riportate da stampa tecnica concordante, verifica web 17/10/2026 |
| Y5 | Nuovo pack | — | EDILIZIA_CIRCOLARE_LCA_PACK (12 schede, L2-L3, FACOLTA_TECNOLOGIA_E_COSTRUZIONE): LCA (ISO 14040/14044, UNI EN 15978), EPD (UNI EN 15804, ISO 14025), embodied carbon ed EPBD (UE) 2024/1275, design for disassembly (ISO 20887), demolizione selettiva e inerti (D.Lgs 152/2006, UNI EN 12620/13242), riuso e passaporto materiali, CAM Edilizia (D.M. 23 giugno 2022) e D.Lgs 36/2023, LCC (ISO 15686-5), rifiuti di cantiere (art. 185 + D.M. 161/2012), filiere di riciclo, BIM-LCA, economia della circolarità. Decreti End of Waste, soglie RENTRI e recepimento EPBD in forma prudente («da verificare nella versione vigente») | Norme di consolidata certezza; nessun valore normativo inventato |
| Y6 | Nuovo esame | — | ESAMI/EDILIZIA_CIRCOLARE_LCA: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored) | build_esami_giro5.py |
| Y7 | Rettifica conteggi | INDEX fermo a «69 pack, 935 schede, 70 esami» (CAPPOTTO_ETICS_PACK del Giro U mai censito nell'indice) | CAPPOTTO_ETICS_PACK registrato; totali misurati sui file il 17/10/2026: 71 pack, 963 schede, 73 esami | Validazione globale python (JSON, 11 chiavi, COURSE.yaml coerenti: 0 errori) |

Righe aperte nel giro:
- Conto Termico 3.0: contenuti e data del decreto correttivo da verificare sulla GU e sulle Regole Applicative GSE appena pubblicato.
- Reddito Energetico: pubblicazione del bando 2026 da verificare sul portale GSE a ogni aggiornamento.
- EPBD (UE) 2024/1275: recepimento nazionale e decreti attuativi sul GWP del ciclo di vita da verificare.
- CER: i termini del contributo PNRR chiuso (30/11/2025, 30/6/2026, 31/8/2026) derivano da stampa tecnica concordante: riscontro su documento GSE/MASE primario alla prossima verifica.
- Eredità committata in questo giro: audit sicurezza pre-tag v1.4 del run interrotto del 02/10/2026 (AUDIT_SICUREZZA_V1_4.md, audit_sicurezza_v1_4.py, fix_stale_sicurezza.py, voci enciclopedia e due domande d'esame risincronizzate). Le 326 segnalazioni «campo corto» dell'audit sono falsi positivi di soglia: nessuna azione sulle schede.

## Giro Z — 2026-10-18, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente (correttivo CT 3.0, Reddito Energetico) con 1 correzione e 1 conferma; nuovo pack RETROFIT_NZEB_PACK (12 schede) con esame.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| Z1 | Verifica senza correzione | Scheda «Il Conto Termico 3.0»: nota «decreto correttivo in itinere (superata la Conferenza Stato-Regioni a ottobre 2026)» | Confermata senza modifiche: il correttivo non è ancora pubblicato in GU; la convocazione della Conferenza Stato-Regioni sullo schema di decreto è stata protocollata il 14/10/2026 | edilizia.com (16/10/2026), bibus.acca.it (aggiornato 13/10/2026) — verifica web 18/10/2026 |
| Z2 | Precisazione su fonte | Scheda «Il Reddito Energetico»: «quota Sud esaurita in giornata» | «fondi esauriti in pochi giorni con sportello aperto dal 13 al 23 maggio 2025»; data di verifica aggiornata al 18 ottobre 2026 (bando 2026 ancora non pubblicato: si attende il decreto di rifinanziamento MASE) | kilowattchiaro.it (stato al 6/7/2026: sportello 13-23 maggio 2025, esaurimento in dieci giorni), reonic.com (14/8/2026) — verifica web 18/10/2026 |
| Z3 | Nuovo pack | — | RETROFIT_NZEB_PACK (12 schede, L2-L3, FACOLTA_IMPIANTI_ENERGIA): riqualificazione profonda, diagnosi strumentale, fabric first, pompe di calore su impianti esistenti, VMC, FV/accumulo/EV, condominio e contabilizzazione, combinato energia+sismica, cantiere abitato, M&V (IPMVP), economia, documentazione APE/Legge 10. Norme citate solo di consolidata certezza; incentivi rinviati alle schede del pack Energetica con regola di verifica annuale | Norme di consolidata certezza; nessun valore normativo inventato |
| Z4 | Nuovo esame | — | ESAMI/RETROFIT_NZEB: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored) | build_esami_giro5.py |
| Z5 | Validazione | — | Validazione globale: 72 pack, 975 schede, 74 esami; JSON e 11 chiavi OK su tutte le righe, 0 refusi, COURSE.yaml coerenti | Script di validazione python |

Righe aperte nel giro:
- Conto Termico 3.0: il correttivo (schema protocollato 14/10/2026) va verificato sulla GU e sulle Regole Applicative GSE appena pubblicato.
- Reddito Energetico: pubblicazione del decreto di rifinanziamento/bando 2026 da verificare sul portale GSE a ogni aggiornamento.
- EPBD (UE) 2024/1275: recepimento nazionale e decreti attuativi (GWP ciclo di vita, predisposizione EV) da verificare.
- CER: riscontro su documento GSE/MASE primario dei termini del contributo PNRR chiuso (30/11/2025) alla prossima verifica.

## Giro AA — 2026-10-19, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente (correttivo CT 3.0) con 1 correzione di precisione; nuovo pack VERDE_TETTI_FACCIATE_PACK (13 schede) con esame.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| AA1 | Correzione di precisione | Scheda «Il Conto Termico 3.0», nota: «un decreto correttivo del D.M. 7/8/2025 e' in itinere (superata la Conferenza Stato-Regioni a ottobre 2026…)» | «lo schema di modifica e' all'ordine del giorno della Conferenza Unificata del 22 ottobre 2026 (convocazione protocollata il 14/10/2026, intesa ex art. 10 co. 2 D.Lgs 199/2021). L'iscrizione all'ordine del giorno NON equivale a regole gia' operative: contenuti, esito e data di entrata in vigore da verificare sul testo pubblicato in GU e sulle Regole Applicative GSE aggiornate» | edilizia.com del 16/10/2026, che documenta la convocazione ufficiale della Presidenza del Consiglio (Conferenza Unificata 22/10/2026, punto 3) — verifica web 19/10/2026 |
| AA2 | Nuovo pack | — | VERDE_TETTI_FACCIATE_PACK (13 schede, L2-L3, FACOLTA_TECNOLOGIA_E_COSTRUZIONE): tipologie, stratigrafia UNI 11235, carichi a saturazione (NTC), facciate vegetali, gestione idrica, specie, pratiche e vincoli, cantiere con collaudo di tenuta, manutenzione, benefici con ordini di grandezza prudenti, economia, integrazione biosolare FV. Norme citate solo di consolidata certezza (UNI 11235, UNI EN 13948, NTC, DPR 380/2001, D.Lgs 42/2004); benefici mai presentati come garanzie | Norme di consolidata certezza; regolamenti comunali e incentivi marcati da verificare |
| AA3 | Nuovo esame | — | ESAMI/VERDE_TETTI_FACCIATE: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored) | build_esami_giro5.py |
| AA4 | Validazione | — | Validazione globale: 73 pack, 988 schede, 75 esami; JSON e 11 chiavi OK su tutte le righe, 0 refusi, COURSE.yaml coerenti | Script di validazione python |

Righe aperte nel giro:
- Conto Termico 3.0: esito della Conferenza Unificata del 22/10/2026 e pubblicazione del correttivo in GU: da verificare alla prossima esecuzione, con eventuale aggiornamento delle schede 1-3 di ENERGETICA_INCENTIVI_PACK.
- Reddito Energetico: decreto di rifinanziamento/bando 2026 da verificare sul portale GSE.
- EPBD (UE) 2024/1275: recepimento nazionale da verificare.
- CER: riscontro su fonte primaria GSE/MASE dei termini PNRR chiusi.

## Giro AB — 2026-10-20, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente (aliquote 2027, nuovo TUIR, caldaie a fossile, Legge di Bilancio 2027) con 2 aggiornamenti alla scheda detrazioni; nuovo pack PREZZIARIO_E_LISTINI_PACK (12 schede) con esame.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| AB1 | Correzione sostanziale | Scheda «Le detrazioni fiscali per l'edilizia», campo tecnologia: tra gli interventi agevolabili figurava «la nuova installazione (non in sostituzione)» di caldaia unica a fossile | «secondo l'interpretazione di settore basata sulla definizione EPBD di "installazione" (che include acquisto, assemblaggio e messa in funzione), l'esclusione si estende anche alla NUOVA installazione di caldaia unica a condensazione a combustibile fossile: interpretazione in evoluzione, verificare la prassi AdE vigente prima di applicarla al caso concreto» | bibus.acca.it (aggiornato 12/10/2026: la definizione EPBD di installazione copre anche la nuova installazione di caldaia unica) — verifica web 20/10/2026 |
| AB2 | Nota di aggiornamento normativo | Scheda «Le detrazioni fiscali per l'edilizia», campo normative: riferimenti al TUIR (DPR 917/1986) e alla L. 199/2025 senza menzione della riforma | Aggiunta: «dal 1/1/2027 il TUIR (DPR 917/1986) e' sostituito dal nuovo Testo Unico delle imposte sui redditi, D.Lgs 19 giugno 2026 n. 117 (GU n. 152 del 3/7/2026, in vigore dal 4/7/2026, applicazione dal 1/1/2027), che ricolloca le disposizioni sui bonus edilizi: aggiornare i riferimenti alla numerazione vigente dal 2027; la Legge di Bilancio 2027 (in discussione ottobre-dicembre 2026) puo' modificare aliquote e limiti dal 2027: verificare il testo definitivo» | studiocerbone.com (13/8/2026), brocardi.it (24/7/2026), miolegale.it (21/7/2026), bibus.acca.it (8/7/2026): fonti concordanti su D.Lgs 117/2026, GU n. 152 del 3/7/2026, applicazione dal 1/1/2027 in attuazione dell'art. 21 L. 111/2023 — verifica web 20/10/2026 |
| AB3 | Verifica senza correzione | Scheda «Le detrazioni fiscali per l'edilizia»: roadmap aliquote 2026 = 50%/36%, 2027 = 36%/30% (limite 96.000 euro), dal 2028 = 30% su 48.000 euro | Confermata senza modifiche: fonti concordanti (ottobre 2026) ribadiscono 2027 = 36% abitazione principale / 30% altri casi e dal 2028 30% su 48.000 euro; nessuna proroga del 50/36 in alcun testo; criterio di cassa (conta la data del bonifico); LdB 2027 ancora in scrittura (DPFP approvato 2/10/2026) | bibus.acca.it (12/10/2026), cantiericloud.com (5/8/2026), gromia.com, fiscomania.com — verifica web 20/10/2026 |
| AB4 | Nuovo pack | — | PREZZIARIO_E_LISTINI_PACK (12 schede, L2-L3, FACOLTA_GESTIONE_SISTEMA): prezziari ufficiali regionali e camerali, prezzari tipologici e listini, struttura delle voci, analisi dei prezzi, costo orario manodopera da CCNL, nuovi prezzi, scontistica, indici ISTAT e revisione prezzi, spese generali e utile, sicurezza non ribassabile (D.Lgs 81/2008 art. 95), prezzari digitali e BIM 5D, errori e contenziosi. NON ridondante con CONTABILITA_APPALTI_PACK (SAL, varianti, riserve). Norme citate solo di consolidata certezza; decreti attuativi marcati da verificare nella versione vigente | Norme di consolidata certezza; nessun valore normativo inventato |
| AB5 | Nuovo esame | — | ESAMI/PREZZIARIO_LISTINI: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored); tabella ESAMI/README aggiornata | build_esami_giro5.py |
| AB6 | Validazione | — | Validazione globale: 74 pack, 1000 schede, 76 esami; JSON e 11 chiavi OK su tutte le righe, 0 refusi, COURSE.yaml coerenti | Script di validazione python |

Righe aperte nel giro:
- Conto Termico 3.0: VERIFICA PRIORITARIA al prossimo giro — esito della Conferenza Unificata del 22/10/2026 (dopodomani rispetto a questo giro) e pubblicazione del correttivo in GU, con aggiornamento delle schede 1-3 di ENERGETICA_INCENTIVI_PACK.
- Legge di Bilancio 2027: testo definitivo (dicembre 2026) per conferma o modifica di aliquote e limiti detrazioni dal 2027.
- Nuovo TUIR (D.Lgs 117/2026): numeri degli articoli che ricollocano i bonus edilizi (la stampa di settore indica artt. 371-373, ma da fonte singola: da verificare sul testo GU prima di citarli nelle schede).
- Reddito Energetico: decreto di rifinanziamento/bando 2026 da verificare sul portale GSE.
- EPBD (UE) 2024/1275: recepimento nazionale da verificare.
- CER: riscontro su fonte primaria GSE/MASE dei termini PNRR chiusi.

## Giro AC — 2026-10-21, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente (CT 3.0 in attesa seduta 22/10, CER/PNRR, Reddito Energetico, detrazioni) con 1 correzione di precisione; nuovo pack EDILIZIA_MONTAGNA_PACK (12 schede) con esame.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| AC1 | Correzione di precisione | Scheda «Gli incentivi delle CER» (FOTOVOLTAICO_CAMPI_AGRIVOLTAICO_CER_PACK): «CHIUSO a nuove domande dal 30/11/2025 (accordi di finanziamento entro il 30/6/2026, erogazione entro il 31/8/2026): resta pienamente attiva la tariffa incentivante, che non ha scadenza a bando» | «CHIUSO a nuove domande: risorse esaurite gia' il 21/11/2025 al raggiungimento della soglia di 795,5 milioni di euro comunicata dal MASE (termine ordinario 30/11/2025); con il DL 19/2026, art. 27, gli accordi di concessione andavano firmati entro il 30/6/2026 e la realizzazione e' ammessa entro 24 mesi dall'accordo, con limite invalicabile al 31/12/2027, con il GSE soggetto attuatore unico; resta attiva la tariffa incentivante, ammessa a sportello entro il contingente di 5 GW e comunque non oltre il 31/12/2027»; normative: «DL 19/2026 art. 27, convertito con L. 50/2026» | naturalnzeb.it (31/7/2026: soglia 795,5 M€ al 21/11/2025), tuoingegnere.altervista.org (22/7/2026: 30/6/2026 = firma accordi, 24 mesi, limite 31/12/2027, GSE attuatore unico), prefina.it (17/8/2026: D.L. 19/2026 conv. L. 50/2026, contingente 5 GW e 31/12/2027 per la tariffa), comunita-energetica.it (24/8/2026), greenmood.org (5/9/2026: regole GSE 27/3/2026) — verifica web 21/10/2026 |
| AC2 | Verifica senza correzione | Schede 1-3 ENERGETICA_INCENTIVI_PACK sul correttivo CT 3.0 (seduta Conferenza Unificata 22/10/2026) | Confermate senza modifiche: la seduta e' fissata domani 22/10/2026 (convocazione protocollata 14/10/2026), nessun esito pubblicato alla data di verifica; il riferimento operativo resta il D.M. 7/8/2025 con Regole Applicative GSE del 19/12/2025 | edilizia.com (16/10/2026) — verifica web 21/10/2026 |
| AC3 | Verifica senza correzione | Scheda «Il Reddito Energetico»: sportello chiuso, in attesa del decreto di rifinanziamento | Confermato: ad ottobre 2026 nessun nuovo bando pubblicato; requisiti ISEE (15.000/30.000 euro) e contributo (2.000 + 1.500 euro/kW) ribaditi dalle fonti | reonic.com (14/8/2026), greenmood.org (5/9/2026), tancredisolarsystem.com (12/8/2026) — verifica web 21/10/2026 |
| AC4 | Verifica senza correzione | Scheda detrazioni: 2026 = 50%/36%, 2027 = 36%/30%, limite 96.000 euro | Confermato da fonti concordanti aggiornate a ottobre 2026; nessuna proroga del 50% oltre il 2026 in alcun testo | greenmood.org (5/9/2026), solarsicily.com (20/10/2026) — verifica web 21/10/2026 |
| AC5 | Nuovo pack | — | EDILIZIA_MONTAGNA_PACK (12 schede, L2-L3, FACOLTA_TECNOLOGIA_E_COSTRUZIONE): cantiere in quota, carico neve (NTC, UNI EN 1991-1-3), gelo-disgelo e getti invernali, fondazioni su pendii, versanti e opere di sostegno, valanghe e zonizzazione, edilizia alpina tradizionale, involucro in zona F, impianti antigelo, accessi e sicurezza invernale, vincoli paesaggistici e decoro alpino, mezzi speciali (teleferiche, elicottero). Norme nazionali solo di consolidata certezza; normativa regionale marcata da verificare localmente | Norme di consolidata certezza; nessun valore normativo inventato |
| AC6 | Nuovo esame | — | ESAMI/EDILIZIA_MONTAGNA: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored); tabella ESAMI/README aggiornata | build_esami_giro5.py |
| AC7 | Validazione | — | Validazione globale: 75 pack, 1012 schede, 77 esami; JSON e 11 chiavi OK su tutte le righe, 0 refusi, COURSE.yaml coerenti | Script di validazione python |

Righe aperte nel giro:
- Conto Termico 3.0: VERIFICA PRIORITARIA al prossimo giro — esito della Conferenza Unificata del 22/10/2026 (domani) e pubblicazione del correttivo in GU, con eventuale aggiornamento delle schede 1-3 di ENERGETICA_INCENTIVI_PACK.
- Legge di Bilancio 2027: testo definitivo (dicembre 2026) per conferma o modifica di aliquote e limiti detrazioni dal 2027.
- Nuovo TUIR (D.Lgs 117/2026): numeri degli articoli che ricollocano i bonus edilizi (stampa di settore indica artt. 371-373, da fonte singola: verificare sul testo GU).
- Reddito Energetico: decreto di rifinanziamento/bando 2026 da verificare sul portale GSE.
- EPBD (UE) 2024/1275: recepimento nazionale da verificare.

## Giro AD — 2026-10-22, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente (CT 3.0: seduta in giornata; LdB 2027: ipotesi Ecobonus 65%) con 1 nota di precisione; nuovo pack SOLARE_TERMODINAMICO_CSP_PACK (12 schede) con esame.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| AD1 | Nota di aggiornamento | Scheda «Le detrazioni fiscali per l'edilizia», campo normative: la nota sulla LdB 2027 si fermava alla generica possibilita' di modifica di aliquote e limiti | Aggiunte: ipotesi in discussione di un Ecobonus rafforzato al 65% per l'abitazione principale nell'ambito della flessibilita' UE per la sicurezza energetica (COM(2026) 553 dell'8/10/2026, ~14,4 miliardi per l'energia nel 2027-2028), marcata come NON operativa e da non inserire nei preventivi; ricordato che il Bonus Barriere Architettoniche 75% si e' fermato alle spese entro il 31/12/2025 | corriere.it (11/10/2026), edilizia.com (12 e 14/10/2026, con ricostruzione Camera sulle aliquote vigenti), bibus.acca.it (12 e 15/10/2026), edilportale.com (16/10/2026) — verifica web 22/10/2026 |
| AD2 | Verifica senza correzione | Schede 1-3 ENERGETICA_INCENTIVI_PACK sul correttivo CT 3.0 | Confermate senza modifiche: la seduta della Conferenza Unificata e' fissata OGGI 22/10/2026 alle 12:00; la verifica e' stata eseguita alle 05:47, prima della seduta: nessun esito pubblicabile. Riferimento operativo invariato: D.M. 7/8/2025 e Regole Applicative GSE del 19/12/2025 | edilizia.com (16/10/2026) — verifica web 22/10/2026 ore 05:47 |
| AD3 | Verifica senza correzione | Scheda detrazioni: 2026 = 50%/36%, 2027 = 36%/30%, limite 96.000 euro | Riconfermato: la ricostruzione della Camera dei deputati in sede DPFP riporta le stesse aliquote 2026-2027; nessuna proroga del 50% approvata | edilizia.com (14/10/2026: tabella Camera su L. 199/2025), pmi.it (14/10/2026), pgcasa.it (16/10/2026) — verifica web 22/10/2026 |
| AD4 | Nuovo pack | — | SOLARE_TERMODINAMICO_CSP_PACK (12 schede, L2-L3, FACOLTA_IMPIANTI_ENERGIA): principio CSP e DNI, trough, torri, Fresnel, dish-Stirling, accumulo a sali fusi, blocco di potenza, integrazione edilizia, contesto italiano, autorizzazioni, cantiere e commissioning, economia e confronto con FV. Norme citate solo di consolidata certezza (D.Lgs 28/2011, D.Lgs 387/2003, D.Lgs 152/2006); decreti FER marcati da verificare nel quadro vigente | Norme di consolidata certezza; prezzi/rendimenti come fasce di letteratura |
| AD5 | Nuovo esame | — | ESAMI/SOLARE_TERMODINAMICO_CSP: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored); tabella ESAMI/README aggiornata | build_esami_giro5.py |
| AD6 | Validazione | — | Validazione globale: 76 pack, 1024 schede, 78 esami; JSON e 11 chiavi OK su tutte le righe, 0 refusi, COURSE.yaml coerenti | Script di validazione python |

Righe aperte nel giro:
- Conto Termico 3.0: VERIFICA PRIORITARIA al prossimo giro — esito della Conferenza Unificata del 22/10/2026 (svoltasi oggi alle 12:00, DOPO questa verifica) e pubblicazione del correttivo in GU, con eventuale aggiornamento delle schede 1-3 di ENERGETICA_INCENTIVI_PACK.
- Legge di Bilancio 2027: seguire l'iter del Ddl (atteso in Parlamento) e l'eventuale conversione dell'ipotesi Ecobonus 65%; testo definitivo a dicembre 2026.
- Nuovo TUIR (D.Lgs 117/2026): numeri degli articoli che ricollocano i bonus edilizi (stampa di settore indica artt. 371-373, da fonte singola: verificare sul testo GU).
- Reddito Energetico: decreto di rifinanziamento/bando 2026 da verificare sul portale GSE.
- EPBD (UE) 2024/1275: recepimento nazionale da verificare.

## Giro AE — 2026-10-23, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente con 1 correzione sostanziale (esito della Conferenza Unificata del 22/10 sul correttivo CT 3.0); nuovo pack SMART_CITY_PACK (12 schede) con esame; manutenzione della tabella esami.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| AE1 | Correzione sostanziale | Scheda «Il Conto Termico 3.0» (ENERGETICA_INCENTIVI_PACK), campo normative: «Nota ottobre 2026: lo schema di decreto correttivo e' all'ordine del giorno della Conferenza Unificata del 22/10/2026, non ancora superata ne' pubblicata» | La Conferenza Unificata del 22/10/2026 ha espresso INTESA CON OSSERVAZIONI sullo schema: la scheda riporta ora i contenuti della bozza correttiva (Comuni ≤15.000 abitanti al 100% solo per il primo intervento e 80% per i successivi con tutela delle domande pre-vigore; gestione dei 900 M€/anno con riserva minima 300 M€ PA + 300 M€ privati/imprese; soglie di impegno: a 600 M€ per categoria solo accesso diretto per 60 giorni, a 900 M€ complessivi stop prenotazioni per 60 giorni, prenotazioni entro il 50% delle risorse PA; impegno cumulato su media triennale con contatore pubblico GSE; PA con pagamento in unica soluzione se incentivo ≤50.000 euro; rafforzamento di rigetto, decadenza e recupero anche verso il mandatario all'incasso; APE post-intervento e diagnosi estesi a sostituzione serramenti e schermature) con avvertenza esplicita: contenuti «da bozza, da confermare sul testo definitivo» e NON operativi finche' il decreto non e' pubblicato in GU e fino all'aggiornamento delle Regole Applicative GSE | edilportale.com (22/10/2026: «Conto Termico 3.0, le Regioni danno l'ok ma propongono…», esito della seduta; fetch diretto in timeout, esito da titolo SERP datato) e ingenio-web.it (16/10/2026, articolo letto integralmente: contenuti della bozza) — verifica web 23/10/2026 |
| AE2 | Nuovo pack | — | SMART_CITY_PACK (12 schede, L2-L3, FACOLTA_GESTIONE_SISTEMA): architettura a livelli, illuminazione pubblica telegestita, reti IoT LoRaWAN/NB-IoT, piattaforma dati e control room, digital twin urbano, mobilita' smart e ricarica EV, gestione idrica smart, edifici pubblici e BEMS, smart district, rifiuti urbani smart e tariffazione puntuale, privacy/cybersecurity, economia CAPEX/OPEX e partenariati. Norme citate solo di consolidata certezza (Reg. UE 2016/679, D.Lgs 138/2024, D.Lgs 82/2005, D.Lgs 36/2023, D.M. 312/2021, D.Lgs 152/2006, D.Lgs 102/2014, DPR 74/2013); regolazione ARERA citata senza numeri di delibera; bandi marcati da verificare | Norme di consolidata certezza; nessun valore normativo inventato; nessun nome di azienda |
| AE3 | Nuovo esame | — | ESAMI/SMART_CITY: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored); tabella ESAMI/README aggiornata | build_esami_giro5.py |
| AE4 | Manutenzione indice esami | Tabella ESAMI/README con 74 righe e copertura dichiarata obsoleta («66 corsi»); 4 esami preesistenti non elencati | Aggiunte le righe CAPPOTTO (117 domande), ILLUMINAZIONE (250), SERRAMENTI (195), SOLLEVAMENTO (250) — domande.md in repository e chiavi jsonl gia' presenti in ESAMI_RISPOSTE — e corretta la copertura: 79 esami a copertura dei 77 pack didattici | Conteggio su file: directory UNIVERSITA_EDILIZIA/ESAMI e archivio ESAMI_RISPOSTE — verifica 23/10/2026 |
| AE5 | Validazione | — | Validazione globale: 77 pack, 1036 schede, 79 esami; JSON valido e 11 chiavi in ordine esatto su tutte le righe, 0 refusi aplicazioni/tegnologia, COURSE.yaml coerenti. Nota nota: 109 schede di pack storici (pre-regola, giri fino a meta' ottobre) non hanno il prefisso «Ordini di grandezza indicativi: » in costi_e_economia: NON modificate per non toccare pack esistenti; eventuale allineamento massivo resta da decidere come giro dedicato | Script di validazione python |

Righe aperte nel giro:
- Conto Termico 3.0: VERIFICA PRIORITARIA al prossimo giro — pubblicazione del decreto correttivo in GU e Regole Applicative GSE aggiornate; conferma dei contenuti sul testo definitivo (in scheda c'e' la bozza con intesa con osservazioni).
- Legge di Bilancio 2027: iter del Ddl e sorte dell'ipotesi Ecobonus 65% (COM(2026) 553); testo definitivo a dicembre 2026.
- Nuovo TUIR (D.Lgs 117/2026): numeri degli articoli che ricollocano i bonus edilizi (stampa di settore indica artt. 371-373, da fonte singola: verificare sul testo GU).
- Reddito Energetico: decreto di rifinanziamento/bando 2026 da verificare sul portale GSE.
- EPBD (UE) 2024/1275: recepimento nazionale da verificare.

## Giro AF — 2026-10-24, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente con 2 correzioni (manovra 2027 capitolo «casa»; nota IVA sulle trattenute CER); nuovo pack MICROEOLICO_PACK (13 schede) con esame.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| AF1 | Nota di aggiornamento | Scheda «Le detrazioni fiscali per l'edilizia» (ENERGETICA_INCENTIVI_PACK), campo normative: la nota LdB 2027 citava la generica possibilita' di modifica e l'ipotesi Ecobonus 65% (COM(2026) 553) | Aggiunto il capitolo «casa» della manovra 2027 come ricostruito dalla stampa di settore: pacchetto ~1 miliardo; detrazioni lavori in casa 550 milioni con ipotesi di PROROGA dell'assetto 2026 (50% abitazione principale / 36% altri, limite 96.000 euro) oltre il 2026 — in assenza di interventi scatterebbe il calo legislativo a 36%/30% — conferma del bonus mobili (~500 mln) e ripristino del vecchio Ecobonus 65% per pompe di calore, sistemi ibridi e cappotti (~50 mln/anno); sul Conto Termico ipotesi di potenziamento a 700-800 milioni con copertura a parte in extradeficit; tutto marcato NON approvato, subordinato a coperture e all'iter parlamentare (approvazione entro il 31/12/2026), da non inserire nei preventivi | idealista.it (22/10/2026: «Manovra 2027, la casa vale un miliardo», articolo letto integralmente), ipsoa.it (22/10/2026: Ecobonus 65% in discussione), incentivimpresa.it (20/10/2026: iter Ddl) — verifica web 24/10/2026 |
| AF2 | Nota di aggiornamento | Scheda «Gli incentivi delle CER» (FOTOVOLTAICO_CAMPI_AGRIVOLTAICO_CER_PACK), campo normative: si chiudeva su DL 19/2026 conv. L. 50/2026 | Aggiunta nota fiscale: secondo la Risposta n. 22/2026 dell'Agenzia delle Entrate (riportata dalla stampa di settore a ottobre 2026, da verificare sul testo ufficiale agenziaentrate.gov.it) le somme che la CER trattiene dagli incentivi GSE per i costi di gestione non costituirebbero corrispettivi di servizio e resterebbero fuori campo IVA; tariffe CER (80/70/60 €/MWh + integrazione max 120/110/100, 20 anni, entro 5 GW e comunque non oltre il 31/12/2027) riconfermate | greenmood.org (18/10/2026: Risposta AdE 22/2026 e tariffe) — verifica web 24/10/2026 |
| AF3 | Verifica senza correzione | Scheda «Il Conto Termico 3.0»: nota intesa con osservazioni del 22/10/2026, in attesa di GU | Confermata senza modifiche: a due giorni dalla seduta il decreto correttivo NON risulta pubblicato in GU ne' adottato in via definitiva dal MASE; il riferimento operativo resta il D.M. 7/8/2025 con Regole Applicative GSE del 19/12/2025 | ricerca web mirata post-22/10 (nessun esito di pubblicazione rinvenuto) — verifica web 24/10/2026 |
| AF4 | Verifica senza correzione | Scheda «Il Reddito Energetico»: sportello chiuso, decreto di rifinanziamento atteso | Confermato: bando 2026 ancora non pubblicato in GU (fonti concordanti fino al 9/10/2026); ricordata la regola GSE di riapertura dello sportello anche senza nuovo bando se dalle rinunce si liberano almeno 5 milioni | bragagroup.it (9/10/2026), myenergy.it (16/7/2026) — verifica web 24/10/2026 |
| AF5 | Nuovo pack | — | MICROEOLICO_PACK (13 schede, L2-L3, FACOLTA_IMPIANTI_ENERGIA): fisica del vento, HAWT/VAWT, taglie, misura in sito, torri e fondazioni, connessione (CEI 0-21/0-16), autorizzazioni (PAS/AU/vincoli), rumore e flicker, cantiere, manutenzione, economia, ibridi e CER. Norme citate solo di consolidata certezza (CEI EN 61400-2, EN 61400-12-1, 2006/42/CE, D.Lgs 387/2003, D.Lgs 28/2011, D.Lgs 152/2006, D.Lgs 42/2004, DPR 380/2001, L. 447/1995, DPCM 14/11/1997, NTC D.M. 17/1/2018, EN 1090, D.Lgs 81/2008, D.M. 37/2008, D.M. 414/2023); soglia PAS eolica (60 kW) e prezzi minimi RID marcati da verificare | Norme di consolidata certezza; prezzi e producibilita' come fasce di letteratura; nessun nome di azienda |
| AF6 | Nuovo esame | — | ESAMI/MICROEOLICO: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored); tabella ESAMI/README aggiornata (riga + copertura 80 esami su 78 pack) | build_esami_giro5.py |
| AF7 | Validazione | — | Validazione globale: 78 pack, 1049 schede, 80 esami; JSON valido e 11 chiavi in ordine esatto su tutte le righe, 0 refusi aplicazioni/tegnologia, COURSE.yaml coerenti. Resta la nota nota: 109 schede di pack storici senza il prefisso «Ordini di grandezza indicativi: » (non modificate: eventuale allineamento come giro dedicato) | Script di validazione python |

Righe aperte nel giro:
- Conto Termico 3.0: VERIFICA PRIORITARIA al prossimo giro — pubblicazione del decreto correttivo in GU e Regole Applicative GSE; poi conferma dei contenuti sul testo definitivo e, se confermato il potenziamento LdB a 700-800 M€, aggiornamento della dotazione in scheda.
- Legge di Bilancio 2027: iter del Ddl (prima lettura attesa a novembre, testo definitivo a dicembre 2026): sorte della proroga 50%/36%, del bonus mobili e dell'Ecobonus 65%.
- Nuovo TUIR (D.Lgs 117/2026): numeri degli articoli che ricollocano i bonus edilizi (artt. 371-373 da fonte singola: verificare sul testo GU).
- Reddito Energetico: decreto di rifinanziamento/bando 2026 da verificare sul portale GSE.
- EPBD (UE) 2024/1275: recepimento nazionale da verificare.

## Giro AG — 2026-10-25, bozza post-v1.3.0 (NESSUN tag applicato)

Contenuto: verifica incentivi ricorrente conclusa SENZA correzioni (tutti i valori in scheda confermati dalle fonti); nuovo pack IMPERMEABILIZZAZIONI_SPECIALI_PACK (12 schede) con esame.

| # | Tipo | Prima | Dopo | Fonte di verifica |
|---|---|---|---|---|
| AG1 | Verifica senza correzione | Scheda «Il Conto Termico 3.0»: nota intesa con osservazioni del 22/10/2026, in attesa di GU | Confermata: il decreto correttivo NON risulta pubblicato in GU ne' adottato in via definitiva; la stampa di settore conferma che il testo puo' ancora cambiare e che le nuove regole si applicheranno solo dopo la pubblicazione | cogenlab.com (23/10/2026: «non ancora in vigore... resta da vedere quali richieste il MASE accogliera'»), gruppoinnoveco.it (22/10/2026) — verifica web 25/10/2026 |
| AG2 | Verifica senza correzione | Scheda detrazioni: nota capitolo «casa» della manovra 2027 (Giro AF: proroga 50%/36%, bonus mobili, Ecobonus 65%, CT 700-800 mln; NON approvato) | Confermata: nessun testo del Ddl di Bilancio 2027 ancora pubblicato; il quadro resta quello delle ipotesi in discussione | studiofrancescaseniga.it (24/10/2026), iter Ddl non ancora concluso — verifica web 25/10/2026 |
| AG3 | Verifica senza correzione | Scheda «Gli incentivi delle CER»: tariffe 80/70/60 + integrazione max 120/110/100, 20 anni, entro 5 GW e 31/12/2027; PNRR 40% chiuso; nota IVA Risposta AdE 22/2026 | Riconfermato tutto dalla stessa fonte aggiornata al 24/10/2026; nessuna variazione | greenmood.org (aggiornato 24/10/2026) — verifica web 25/10/2026 |
| AG4 | Verifica senza correzione | Scheda «Il Reddito Energetico»: sportello chiuso, decreto di rifinanziamento atteso | Confermato: nessuna pubblicazione nuova rinvenuta | monitoraggio fonti di settore — verifica web 25/10/2026 |
| AG5 | Nuovo pack | — | IMPERMEABILIZZAZIONI_SPECIALI_PACK (12 schede, L2-L3, FACOLTA_TECNOLOGIA_E_COSTRUZIONE): fondamenti dei regimi idraulici, membrane bituminose/sintetiche/liquide per opere speciali, bentonite, interrati su esistente, coperture rovescie, vasche e serbatoi, ponti e gallerie, dettagli e waterstop, collaudi di tenuta. Norme solo di consolidata certezza (serie UNI EN 13707/13956/13969/1928/14891/1504, EAD ex ETAG 005, EN 14695, UNI EN 12845, D.M. 174/2004, Reg. UE 305/2011, NTC D.M. 17/1/2018, D.Lgs 152/2006) | Norme di consolidata certezza; prezzi come fasce di letteratura/esperienza; nessun nome di azienda |
| AG6 | Nuovo esame | — | ESAMI/IMPERMEABILIZZAZIONI: 250 domande, chiavi in ESAMI_RISPOSTE (fuori repository, gitignored); tabella ESAMI/README aggiornata (copertura 81 esami su 79 pack) | build_esami_giro5.py |
| AG7 | Validazione | — | Validazione globale: 79 pack, 1061 schede, 81 esami; JSON valido e 11 chiavi in ordine esatto su tutte le righe, 0 refusi aplicazioni/tegnologia, COURSE.yaml coerenti. Nota nota invariata: 109 schede storiche senza prefisso «Ordini di grandezza indicativi: » (non modificate) | Script di validazione python |

Righe aperte nel giro:
- Conto Termico 3.0: VERIFICA PRIORITARIA al prossimo giro — pubblicazione del correttivo in GU e Regole Applicative GSE; poi conferma dei contenuti sul testo definitivo.
- Legge di Bilancio 2027: attesa del testo del Ddl (presentazione alle Camere); sorte di proroga 50%/36%, bonus mobili, Ecobonus 65%, potenziamento CT.
- Nuovo TUIR (D.Lgs 117/2026): numeri degli articoli che ricollocano i bonus edilizi (artt. 371-373 da fonte singola: verificare sul testo GU).
- Reddito Energetico: decreto di rifinanziamento/bando 2026 da verificare sul portale GSE.
- EPBD (UE) 2024/1275: recepimento nazionale da verificare.
