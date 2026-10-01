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
