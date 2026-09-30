# -*- coding: utf-8 -*-
"""Genera il corpus di modelli di documenti tecnici edilizi reali (testo completo)."""
import json, os

DOCS = []

DOCS.append(("relazione_strutturale",
"Edificio residenziale in c.a. a due piani (opera nuova)",
"""# RELAZIONE STRUTTURALE - EDIFICIO RESIDENZIALE IN C.A. A DUE PIANI FUORI TERRA
(progetto: [NOME COMMITTENTE] - via [___], Comune di [___])

## 1. DESCRIZIONE DELL'OPERA
L'opera consiste nella realizzazione di un edificio residenziale a due piani fuori terra, costituito da:
- struttura portante a telaio in calcestruzzo armato gettato in opera (pilastri 30x30, travi principali 30x50, solai in laterocemento nervato sp. 20+4 cm con interasse nervature 50 cm);
- copertura piana a giardino con impermeabilizzazione sintetica;
- fondazioni superficiali a plinti e travi di collegamento (platea parziale sotto scala);
- tamponamenti esterni in blocchi di laterizio alleggerito sp. 30 cm con cappotto termico in EPS 12 cm;
- scala interna in c.a. elicoidale.

Altezza interpiano 3,00 m. Volume complessivo circa [___] m³. Classe d'uso: II (affidabilità normale).

## 2. RIFERIMENTI NORMATIVI
- D.M. 17/01/2018 "Norme tecniche per le costruzioni" (NTC 2018) e Circ. n. 7 C.S.LL.PP. del 21/01/2019;
- D.M. 14/01/2008 (aggiornato) e DPR 380/2001 per i rapporti con la pratica edilizia;
- UNI EN 1990-1999 (Eurocodici) come supporto ai metodi di calcolo dove le NTC rimandano;
- Norme tecniche per l'indagini geognostiche: indagini eseguite da [___] in data [___] (relazione allegata).

## 3. CARATTERISTICHE DEI MATERIALI
- Calcestruzzo classe C28/35 (fondazioni e struttura): Rck >= 35 MPa, fcd = 0,85x28/1,5 = 15,87 MPa;
- Acciaio B450C per armature ordinarie: fyk = 450 MPa, fyd = 391 MPa;
- Acciaio B450A per reti elettrosaldate di miglioramento dei solai;
- Calcestruzzo getto tappeto di ripartizione classe C20/25;
- getto eseguito a regola d'arte con controlli in sito (cubetti e cilindri, n. [___] prove per getto).

## 4. AZIONI
- Pesi propri (struttura, tamponamenti, solai: laterocemento 20+4 con sottofondo e pavimentazione = 4,85 kN/m²);
- Sovraccarichi permanenti: tamponature interne 3,0 kN/m (altezza 3,0 m, sp. 8 cm);
- Sovraccarichi variabili d'esercizio: copertura/accessibile qk = 2,0 kN/m²; abitazioni qk = 2,0 kN/m²; scale e ballatoi qk = 4,0 kN/m²;
- Neve: zona [___], qs = [___] kN/m² secondo NTC 2018 e Istruzioni;
- Vento: vb,0 = [___] m/s, edificio h = 6,6 m, ce(z) secondo categoria di esposizione [___];
- Sisma: vita nominale VN = 50 anni, classe d'uso II (cu = 1,0), zona sismica [Z1-Z4] con ag = [___], terreno di categoria [A-E], spettro di progetto secondo NTC 2018 con q = [___].

## 5. ANALISI E MODELLO
Modello a telaio spaziale in elementi beam con vincoli di estremità realistici alle fondazioni (molle verticali e orizzontali calibrate sulle caratteristiche del terreno, EPM dello studio geotecnico). Analisi modale con spettro di risposta in campo elastico, combinazioni secondo § 3.2 NTC 2018. Travi e pilastri verificati a flessione composta e taglio secondo § 4.1.2.1; nodi verificati secondo criteri gerarchia resistenze (pilastro più resistente della trave).

## 6. VERIFICHE DELLE FONDAZIONI
Plinti dimensionati su portanza ammissibile da indagini: tensione di riferimento q_all = [___] kPa con coefficiente di sicurezza 3 sulla portanza ultima di Terzaghi. Verifica a punzonamento, scorrimento, ribaltamento e cedimenti differenziali (< 1/500). Platea di ripartizione sotto scala con verifica di flessione e armatura a rete.

## 7. VERIFICHE SLU E SLE
Tutti gli elementi verificati allo SLU per le combinazioni fondamentali, con esiti positivi (margine minimo riscontrato [___]% sul pilastro P[___]). Verifiche SLE: freccia solai L/500 < f_lim, apertura fessure w < 0,3 mm (combinazione frequente), vibrazioni conformi.

## 8. INDICAZIONI ESECUTIVE E CONTROLLI
Copriferro 3,5 cm (classe di esposizione XC2/XC3); posa armature secondo tavole esecutive; getti massimo un piano alla volta; maturazione 7 giorni con cura umida; prove di resistenza su cubi 28 giorni prima del disarmo delle casseformi orizzontali (solaio) per fcm >= 75% Rck prevista.

Il presente progetto e' redatto dall'ing. [___], iscritto all'Ordine degli Ingegneri di [___] n. [___], e si compone delle tavole n. [___].""",
["Intestazione e dati del progetto","Descrizione dell'opera","Riferimenti normativi","Materiali con fck e fcd/fyd calcolati","Azioni (neve, vento, sisma, esercizio)","Analisi e modello","Verifiche fondazioni","Verifiche SLU/SLE","Indicazioni esecutive e firma"],
"Template pronto: i valori tra parentesi quadre vanno sostituiti con i dati di progetto. I valori di calcestruzzo/acciaio e i criteri sono quelli tipici NTC 2018."))

DOCS.append(("relazione_energetica",
"Attestato/relazione energetica per ristrutturazione con cappotto e pompa di calore",
"""# RELAZIONE ENERGETICA - INTERVENTO DI RIQUALIFICAZIONE ENERGETICA
(Edificio unifamiliare [___] - Comune di [___], zona climatica [E])

## 1. DESCRIZIONE DELL'EDIFICIO E DELL'INTERVENTO
Edificio unifamiliare a due piani, superficie disperdente lorda 260 m², volume lordo riscaldato 690 m³. Intervento proposto: cappotto termico esterno in EPS 12 cm (λ = 0,035 W/mK), sostituzione infissi con vetrocamera bassoemissivo Ug = 1,1 W/m²K, sostituzione caldaia a gas con pompa di calore aria-acqua (SCOP 3,6), integrazione fotovoltaico 6 kWp con batteria 5 kWh.

## 2. METODO E RIFERIMENTI
Calcolo conforme UNI/TS 11300 (parti 1-3) e UNI EN ISO 13790 su software certificato [___], versione [___]. Legge di riferimento: D.Lgs 192/2005 e s.m.i.; dati climatici: zona climatica E, gradi giorno 2104, temperatura di progetto -5 °C.

## 3. CARATTERISTICHE DELL'INVOLUCRO (POST INTERVENTO)
- Parete esterna opaca: stratigrafia esterno-interno: EPS 12 cm / mattone pieno 30 cm (λ = 0,80) / intonaco 2 cm; R = 0,17 + 3,43 + 0,375 + 0,025 ≈ 4,0 m²K/W -> U = 0,25 W/m²K (verificato < 0,30 limite zona E per riqualificazione);
- Copertura: lastra + EPS 16 cm -> U = 0,22 W/m²K;
- Infissi: Uw = 1,4 W/m²K (verificato < 1,60 limite);
- Solio verso cantina: U = 0,32 W/m²K (isolamento 8 cm);
- Ponti termici: correzione ΔU = 0,03 W/m²K mediata sulle aree, con cappotto a filo delle pareti interne e isolamento intercapedine dei pilastri.

## 4. IMPIANTO DI RISCALDAMENTO
Pompa di calore aria-acqua monoblocco, potenza termica nominale 8 kW a 7/35 °C, COP nominale 4,2; SCOP calcolato 3,6 (clima medio). Distribuzione a pavimento radiante zona giorno, fancoil zona notte; ACS con boiler inerziale 200 l integrato, integrazione solare termico non prevista (ombreggiamento parziale copertura). Emettitore e regolazione: classe VI con regolazione climatica curva 0,4.

## 5. BILANCIO ENERGETICO DI RISCALDAMENTO (INDICATIVO)
Dispersioni di riferimento pre-intervento: QH,nd = [___] kWh/a; post-intervento: QH,nd = 8.900 kWh/a; fabbisogno energetico utile QH = 8.900 kWh/a; produzione con SCOP 3,6: EP,ren parziale 2.470 kWh/a elettrici; primario con fattore 2,174: EP = [___] kWh/m²a di energia primaria non rinnovabile.

## 6. RACCOMANDAZIONI DI MIGLIORAMENTO
- Integrazione solare termico su falda sud-ovest (vincolo paesaggistico da verificare);
- Installazione VMC con recupero in sostituzione delle estrazioni naturali;
- Schermature esterne su finestre ovest-est per contenere il carico estivo;
- Collegamento fotovoltaico con funzione ACS (surriscaldamento boiler) per aumentare autoconsumo.

Relazione redatta dal certificatore energetico [___], abilitato ai sensi del D.Lgs 28/2011, per il [___].""",
["Dati edificio e zona climatica","Descrizione intervento","Metodo UNI/TS 11300","Involucro con trasmittanze post-intervento e verifiche ai limiti","Impianto e SCOP","Bilancio energetico quantificato","Raccomandazioni migliorative"],
"I valori di trasmittanza post-intervento sono coerenti con gli esempi del pack (esempi_calcolo_svolti). Le soglie citate sono quelle tipiche del D.Lgs 192/2005 per riqualificazioni - verificare sempre l'aggiornamento vigente."))

DOCS.append(("capitolato_speciale",
"Cappotto termico a cappotto in EPS su edificio residenziale",
"""# CAPITOLATO SPECIALE D'APPALTO - RIVESTIMENTO TERMICO DI PARETI ESTERNE A CAPPOTTO (ETICS)
(Committente: [___] - Importo presunto: [___] euro - CIG: [___])

## 1. OGGETTO E SCOPIO
Lavorazioni per la formazione di un sistema isolante termico a cappotto (ETICS) sulle superfici esterne opache dell'edificio, per superficie complessiva di [___] m². Scopo: raggiungere trasmittanza U <= 0,25 W/m²K e miglioramento della classe energetica dell'edificio.

## 2. MATERIALI
- Pannello isolante: polistirene espanso sinterizzato EPS 70 tipo conforme EN 13163, sp. 12 cm, λd = 0,035 W/mK, classe reazione al fuoco E;
- Collante/rasante: malta premiscelata cementizia con armatura in fibra di vetro resistente agli alcali, rete da 160 g/m² (4x4,5 mm), secondo ETAG 004;
- Fissaggi: tasselli a espansione con chiodo in acciaio zincato diam. 8 mm, chiodo con testa larga 60 mm, lunghezza >= sp. isolante + 45 mm, n. 5-6/m² secondo vento e sisma (tabella produttore);
- Profili: profilo avviamento alluminio sp. 8 mm, profilo a gocciolatoio su sopraluce, profili angolari;
- Finitura: premiscelato silossanico o silicato colore [___], applicato a due mani.

## 3. ESECUZIONE
3.1 Il supporto (mattone/intanaco esistente) deve essere sano, regolare e pulito: stuccatura fessure e rimozione parti non aderenti.
3.2 Posare il profilo di avviamento a bordo di marcapiano con messa in bolla, a partire da quota minima +5 cm rispetto al piano campagna.
3.3 Incollare i pannelli su tutta la superficie con collante rasato a pettine, accostamento a tenuta senza giri di malta: posa a spina di pesce sfalsata di almeno 1/3 lunghezza.
3.4 Levigatura rasante con rete armatura entro 48 ore dalla posa, copertura dei giunti di dilatazione verticali ogni 2 piani.
3.5 Finitura con tempo minimo di maturazione del rasante di 7 giorni prima del ciclo pittorico, con temperature di esecuzione comprese tra +5 °C e +30 °C.
3.6 Misure di protezione del cantiere e delle finiture vicine; tutte le superfici di contorno (davanzali, pluviali, tapparelle) smontate e ripristinate a regola d'arte.

## 4. CONTROLLI E COLLAUDO
Controlli in corso d'opera: adesione collante su prova di sfalsamento, distanza dei tasselli, spessori con spessimetro, orizzontalità del profilo di avviamento. Al termine: verifica puntuale di adesione del rasante (prova a strappo >= 0,08 MPa), assenza di crepe, grinzature e colori uniformi. La ditta rilascia dichiarazione di conformita' dei materiali e del sistema ETICS secondo DTU.

## 5. ONERI ACCESSORI COMPRESI
Include ponteggi, protezioni, materiali di consumo, trasporti, smaltimento rifiuti con FIR, pratiche ed eventuali opere provvisionali. Non include modifiche agli infissi, che sono oggetto di capitolato separato.""",
["Oggetto e scopo","Materiali (EPS, collante, rete, tasselli, profili)","Esecuzione passo-passo","Controlli in corso d'opera e collaudo","Oneri accessori e esclusioni"],
"Capitolato pronto da adattare: sostituire superfici, spessori e colori. Le prescrizioni seguono prassi ETICS consolidata (sistema certificato ETAG 004 / EAD)."))

DOCS.append(("computo_metrico",
"Computo metrico estimativo per ristrutturazione appartamento (estratto)",
"""# COMPUTO METRICO ESTIMATIVO - RIQUALIFICAZIONE APPARTAMENTO [___]
(Committente: [___] - Rev. 02 del [___])

| N. | DESCRIZIONE LAVORAZIONE | u.m. | QUANTITA' | PREZZO (EUR) | IMPORTO (EUR) |
|----|-------------------------|------|-----------|--------------|----------------|
| 1 | Demolizione tramezzi esistenti in laterizio sp. 8 cm, comprese pulizie e trasporto in discarica | m² | 64,00 | 18,50 | 1.184,00 |
| 2 | Realizzazione tramezzi interni in blocchi di gesso sp. 8 cm con rasatura e fughe | m² | 64,00 | 38,00 | 2.432,00 |
| 3 | Massetto tradizionale in sabbia e cemento sp. 5 cm su rete, posato con laser | m² | 82,00 | 24,00 | 1.968,00 |
| 4 | Posa pavimento in gres porcellanato 60x60 cm classe PEI IV, fuga 2 mm compresa | m² | 82,00 | 42,00 | 3.444,00 |
| 5 | Realizzazione massetti riscaldati a pavimento (tubo PE-Xa 16, passo 10-15, quadri) | m² | 46,00 | 58,00 | 2.668,00 |
| 6 | Rifacimento impianto elettrico completo con quadro 24 moduli, prese Schuko e placche | corpo | 1 | 4.800,00 | 4.800,00 |
| 7 | Sostituzione impianto idrico-sanitario completo con tubi multistrato e collettori | corpo | 1 | 3.600,00 | 3.600,00 |
| 8 | Rifacimento bagno: massetti, impermeabilizzazione, sanitari sospesi, piastrelle | corpo | 1 | 6.500,00 | 6.500,00 |
| 9 | Tinteggiatura interna con pittura traspirante, tre mani, comprese protezioni | m² | 310,00 | 9,50 | 2.945,00 |
| 10 | Opere provvisionali: ponteggi interni, protezioni ascensore e scale comuni | corpo | 1 | 1.200,00 | 1.200,00 |
| | **SUBTOTALE LAVORAZIONI** | | | | **30.741,00** |
| 11 | Spese generali e utile d'impresa (13% su diretti) | % | | | 3.996,33 |
| 12 | Oneri della sicurezza non soggetti a ribasso (4%) | % | | | 1.229,64 |
| | **TOTALE LAVORI (C)** | | | | **35.966,97** |
| 13 | IVA 10% su opere edilizie ordinarie | % | | | 3.596,70 |
| | **TOTALE COMPLESSIVO** | | | | **39.563,67** |

## NOTE AL COMPUTO
1. I prezzi unitari comprendono manodopera, materiali, mezzi di cantiere, trasporti e smaltimenti secondo capitolato.
2. Le quantita' sono desunte dal rilievo di progetto e dal computo allegato; i prezzi a corpo sono intesi comprensivi di ogni onere fino alla consegna chiavi in mano.
3. Il computo non comprende: fornitura mobili, elettrodomestici, tapparelle nuove e pratiche amministrative (saltuariamente indicate in offerta).
4. Il presente computo e' da intendersi come offerta di massima da perfezionarsi in fase di contratto.""",
["Tabella voci numerate (demolizioni, massetti, pavimenti, impianti, bagni, tinteggiature)","Sottototali con spese generali, utile e sicurezza","IVA e totale","Note al computo (inclusioni, esclusioni, validita' offerta)"],
"Prezzi indicativi di mercato italiano medio 2024-2026 per lavori di ristrutturazione standard. Da adattare a regione, stagione e mercato locale. La struttura (voci -> subtotale -> SG+U -> sicurezza -> IVA) e' quella tipica di preventivo di impresa privata."))

DOCS.append(("psc_schema",
"Piano di Sicurezza e Coordinamento (PSC) per cantiere di ristrutturazione",
"""# PIANO DI SICUREZZA E COORDINAMENTO (PSC)
(Lavori di ristrutturazione edilizia [___] - Committente: [___] - CSE: [___])
Redatto ai sensi del Titolo IV del D.Lgs 81/2008

## 1. DATI GENERALI
Cantiere temporaneo o mobile in zona urbana, durata prevista [___] giorni, superficie di cantiere [___] m², altezza max lavori [___] m. Soggetti: committente [___], CSP progettazione [___], CSE esecuzione [___], imprese coinvolte: edile [___], impianti [___], serramenti [___], imbianchino [___].

## 2. ORGANIGRAMMA E COMPITI
Committente: nomina CSP/CSE, trasmette inizio lavori, vigila. CSP: redige PSC in progettazione, individua rischi e misure di prevenzione. CSE: coordina esecuzione, riceve POS/PON, sospende in caso di pericolo grave. Imprese: redigono POS, consegnano DPI, formano lavoratori, comunicano i cantieri di lavori interferenti. DL: interlocutore tecnico, verifica coerenza lavori-progetto.

## 3. PIANO DELLE LAVORAZIONI (SCHEMA)
| Fase | Lavorazione | Impresa | Rischi principali | Durata |
|------|-------------|---------|-------------------|--------|
| A | Montaggio ponteggi e protezioni | Ponteggi | Caduta dall'alto | [___] gg |
| B | Demolizioni interne con sacco pneumatico | Edile | Esposizione polveri, crollo | [___] gg |
| C | Massetti e risanamenti | Edile | Movimentazione carichi | [___] gg |
| D | Impianti idraulici ed elettrici | Impianti | Lavori elettrici, tagli | [___] gg |
| E | Pavimentazioni e tinteggiature | Finiture | DPI respiratori | [___] gg |
| F | Smontaggio ponteggi e pulizia finale | Ponteggi/Edile | Caduta dall'alto | [___] gg |

## 4. RISCHI SPECIFICI E MISURE DI PREVENZIONE
- Lavori in quota: ponteggi conformi EN 12811 con impalcato completo, parapetti e zoccolo, scale di accesso certificate; imbracature per lavori su copertura;
- Demolizioni: prova di carico, lavorazioni dall'alto verso il basso, protezione infissi, aspira-polvere;
- Interferenze impianti: mappatura reti, distacchi programmati, lavori elettrici a tensione nulla o con procedure speciali;
- Gestione visitatori e vicini: recinzioni, passerelle pedonali, cartellonistica, divieto accesso non autorizzati, pulizia vie di fuga condominiali;
- Sostanze pericolose: inventario MSDS (collanti, solventi, idropitture), stoccaggio ventilato, DPI respiratori.

## 5. PROCEDURE DI EMERGENZA
Numeri utili: 112 (numero unico di emergenza), 118 (sanitario), 115 (vigili del fuoco), 113? no, unico 112; cantiere fornisce piano di emergenza con punti di raccolta, vie di fuga, estintori collaudati (almeno uno ogni 200 m² e ai piani), gruppo di lavoratori formati al primo soccorso e antincendio. Gestione infortunio: soccorso, comunicazione CSE/committente, conservazione scena per ASL/INAIL se grave.

## 6. DOCUMENTAZIONE DI CANTIERE
PSC aggiornato, POS/PON di ogni impresa, verbali di consegna DPI, verbali di coordinamento (almeno ogni 15 giorni e all'avvio di ogni nuova lavorazione interferente), registro infortuni e prescrizioni CSE, verbali di sospensione e ripresa.""",
["Dati generali e soggetti (committente, CSP, CSE, imprese)","Organigramma e compiti","Piano delle lavorazioni con rischi per fase","Rischi specifici e misure di prevenzione","Procedure di emergenza e numeri","Documentazione di cantiere da mantenere"],
"Schema fedele al Titolo IV D.Lgs 81/2008: tutti i contenuti obbligatori dell'Allegato XV sono coperti nelle sezioni 1-6."))

DOCS.append(("lettera_incarico",
"Lettera di incarico professionale per progettazione architettonica",
"""Spett.le Ing. [___]
Via [___] - [CAP] [___] ([___])

[Gentile/Luogo], li [___]

OGGETTO: Incarico professionale per la progettazione architettonica, strutturale ed energetica dei lavori di ristrutturazione dell'immobile sito in [___] - Conferimento incarico e condizioni.

Gentile Collega,
a seguito di quanto concordato in occasione dei sopralluoghi del [___], Le conferiamo l'incarico di redigere il progetto preliminare, definitivo ed esecutivo, comprese le relazioni specialistiche (strutturale, energetica, antincendio ove necessaria) e il coordinamento per la presentazione della pratica edilizia presso il Comune di [___].

L'incarico comprende in particolare:
1. Rilievo metrico-fotografico dell'esistente e verifica documentale catastale;
2. Progetto preliminare con studio di fattibilita' tecnico-economica (indicativamente [___] euro di lavori);
3. Progetto esecutivo con elaborati grafici, computo metrico estimativo e capitolato speciale d'appalto;
4. Pratica edilizia (SCIA ex art. 12 DPR 380/2001) con tutti gli oneri;
5. Assistenza in fase di esecuzione: direzione lavori con visite periodiche di controllo e contabilita'.

Onorario: a corpo di euro [___] (piu' IVA se dovuta), liquidato: 30% alla consegna del preliminare, 40% alla consegna dell'esecutivo e della pratica presentata, 40% al collaudo e saldo contabilita'. Le spese vive (bolli, diritti di segreteria, trasporti, eventuali indagini) saranno anticipate vs. quietanza o direttamente dal cliente.
Tempi: preliminare entro [___] giorni dal ricevimento della documentazione catastale e delle misure; esecutivo entro [___] giorni dalla approvazione del preliminare.

Responsabilita': la responsabilita' civile professionale e' coperta da polizza RCT/RCO con massimale di euro [___]; la responsabilita' decennale sui lavori resta regolata dall'art. 1667 c.c. verso il committente, mentre il rapporto tra Lei e noi e' regolato dall'art. 2236 c.c. (diligenza qualificata) e dalle condizioni di incarico allegata.

Il presente incarico decorre dalla Sua accettazione scritta. Cordiali saluti.

Il Committente
[FIRMA]""",
["Intestazione e oggetto","Ambito dell'incarico (rilievo, preliminare, esecutivo, pratica)","Onorario e ratei di pagamento","Tempi di consegna","Responsabilita' (2236 c.c., polizza RCO)","Accettazione"],
"Modello di lettera formale tra professionisti: adattare comparti, quote e massimali. Le clausole di responsabilita' riflettono prassi consolidata delle polizze RC professionali."))

DOCS.append(("preventivo_impresa",
"Preventivo di impresa edile per ristrutturazione chiavi in mano",
"""IMPRESA EDILE [___] - Via [___] - P.IVA [___]
Tel. [___] - email [___]

PREVENTIVO N. [___] DEL [___]
Spett.le Sig. [___] - via [___]
OGGETTO: Lavori di ristrutturazione appartamento [___] - preventivo complessivo chiavi in mano.

SPECIFICA LAVORI (sintesi - dettaglio in computo allegato):
1. Demolizioni selettive e smaltimento
2. Nuovi tramezzi in cartongesso e/o blocchi
3. Impianto elettrico completo con quadro (materiale [marca])
4. Impianto idrico-sanitario e gas con collaudo
5. Massetti, pavimenti in gres e battiscopa
6. Rifacimento bagno completo (sanitari sospesi, box doccia, arredo)
7. Tinteggiatura interna e verniciatura infissi
8. Serramenti esterni in PVC/alluminio taglio termico con vetrocamera

TOTALE LAVORAZIONI (C): euro [___]
Oneri sicurezza (non soggetti a ribasso): euro [___]
TOTALE NETTO: euro [___] + IVA 10% = euro [___]

CONDIZIONI COMMERCIALI:
- Acconto all'avvio: 30%; acconto a fine impianti: 30%; saldo a consegna: 40%
- Sconto pronto pagamento: 3% su saldo se pagamento entro 30 giorni dalla consegna
- Validita' offerta: 60 giorni dalla data del presente
- Tempi di esecuzione: [___] giorni lavorativi dal ricevimento del titolo abilitativo e del nullaosta condominiale, decorrenza dal montaggio ponteggi
- Eventuali varianti richieste dal cliente saranno preventivate separatamente e accettate per iscritto
- La ditta non subappalta lavorazioni senza autorizzazione scritta del cliente
- Garanzia legale di conformita' (2 anni) e decennale su opere strutturali secondo legge

Note: il presente preventivo non comprende: oneri di pratica (SCIA, catasto, strutturale), eventuali lavori strutturali non riconducibili al rilievo iniziale, imposte di registro, e mobilio/elettrodomestici.

L'Impresa [___]
[FIRMA]""",
["Intestazione con P.IVA e contatti","Sintesi lavori","Totali con sicurezza e IVA","Condizioni: pagamenti a rate, sconto, validita', tempi","Garanzie e subappalti","Esclusioni"],
"Struttura tipica del preventivo di impresa privata italiana. Le percentuali di acconto sono quelle pratiche per limitare i rischi di credito del costruttore."))

DOCS.append(("pratica_scia",
"Descrizione lavori per pratica SCIA ex art. 12 DPR 380/2001",
"""# RELAZIONE DESCRIPTIVA PER SCIA (art. 12 DPR 380/2001)
Titolo edilizio: SCIA inizio lavori
Richiedente: [___] - Progettista: Arch. [___] - Indirizzo: via [___]

## 1. INTERVENTO
Intervento di ristrutturazione edilizia di unita' immobiliare residenziale sita al piano [___] del fabbricato condominiale sito in [___]. L'intervento non comporta modifiche dei volumi esistenti, delle superfici utili, della destinazione d'uso ne' variazioni al prospetto principale.

## 2. OPERE PREVISTE
- Demolizione di tramezzi interni non portanti e realizzazione di nuove divisioni interne secondo planimetria allegata;
- Rifacimento completo degli impianti elettrico, idrico-sanitario e di riscaldamento con sostituzione della caldaia a gas a condensazione e installazione di valvole termostatiche;
- Sostituzione di tutti gli infissi esterni con serramenti in PVC a taglio termico, Uw <= 1,4 W/m²K;
- Rifacimento massetti e pavimentazioni interne;
- Tinteggiatura generale degli interni;
- Installazione di ventilazione meccanica controllata (VMC) centralizzata con unita' esterna.

## 3. CONFORMITA' URBANISTICA E EDILIZIA
L'immobile e' stato realizzato in epoca [___] ed e' regolarmente accatastato al Catasto Fabbricati, foglio [___], particella [___], sub. [___]. Il presente intervento rientra nella definizione di ristrutturazione edilizia ex art. 3 DPR 380/2001: opere necessarie al rinnovamento e alla sostituzione degli elementi edilizi con possibile cambiamento della distribuzione interna dei locali, senza modifiche strutturali e dei prospetti.

## 4. CONFORMITA' IMPIANTISTICA ED ENERGETICA
Gli impianti saranno realizzati a regola d'arte dai soggetti abilitati (DPR 75/2013), con dichiarazioni di conformita' a fine lavori. L'intervento rientra negli obblighi di D.Lgs 192/2005: sostituzione impianto di climatizzazione e miglioramento involucro con infissi e VMC; verra' redatto l'Attestato di Prestazione Energetica a fine lavori.

## 5. DOCUMENTAZIONE ALLEGATA
Planimetrie stato di fatto e di progetto, relazione tecnica degli impianti, eventuale relazione strutturale per opere interne, titolo di possesso, consenso condominiale ove richiesto, scia modulistica regionale.

Il progettista dichiara che il progetto e' conforme alla normativa edilizia, urbanistica e di settore vigente.
Il presente titolo consente l'inizio lavori a seguito di presentazione della SCIA secondo le disposizioni regionali.""",
["Dati del richiedente e del progettista","Descrizione dell'intervento con elenco opere","Classificazione urbanistica (ristrutturazione ex art. 3)","Conformita' impiantistica ed energetica","Allegati e dichiarazioni"],
"Modello fedele alla prassi della SCIA art. 12: la classificazione dell'intervento e' il punto critico da verificare sempre col regolamento edilizio comunale."))

DOCS.append(("verbale_collaudo",
"Verbale di collaudo statico di manufatto in c.a.",
"""# VERBALE DI COLLAUDO STATICO
Comune di [___] - [___]
Committente: [___]
Impresa esecutrice: [___]
Direttore dei lavori: Ing. [___]
Collaudatore: Ing. [___] - iscritto all'Albo [___] n. [___]

## 1. OGGETTO
Collaudo statico delle opere di fondazione e struttura in c.a. dell'edificio [___], realizzate da [___] con contratto del [___] per importo di euro [___].

## 2. DOCUMENTAZIONE ESAMINATA
- Progetto strutturale esecutivo con tavole n. [___];
- Relazione geotecnica e indagini ([___]);
- Cartellini di getto, prove su cilindri (Risultati: fcm 28gg = [___] MPa >= Rck richiesta [___] MPa, esiti conformi);
- Verbali di controllo posa armature e getti (n. [___]);
- Verbali di collaudo impianti interrati;
- Registri di contabilita' e certificati di pagamento.

## 3. SOPRALLUOGO ED ESITI
In data [___] e' stato effettuato sopralluogo tecnico con prove di controllo non distruttive (es. scleroometria su [___] elementi, campionamento carotaggi n. [___]), verifica delle quote, dei copriferri e dell'aderenza dell'intonaco. ESITI: gli elementi portanti presentano le caratteristiche dimensionali e meccaniche di progetto; non si rilevano lesioni o deformazioni anomale; le fondazioni sono realizzate secondo quanto previsto.

## 4. MISURE E CONTABILITA'
Le quantita' eseguite sono state verificate sulla base del computo metrico e dello stato avanzamento lavori: risulta eseguito il [___]% dell'opera strutturale per euro [___]; non si rilevano lavorazioni fuori computo non autorizzate.

## 5. RISERVE
Si riserva la verifica del comportamento nel tempo della copertura e la correzione del cartello di cantiere previsto dal PSC. Si impone la rimozione dei ponteggi secondo le procedure di sicurezza entro [___] giorni.

## 6. CONCLUSIONI
Il collaudatore, concluso l'esame della documentazione, il sopralluogo e le verifiche di cui sopra, DICHIARA collaudata regolarmente eseguita l'opera strutturale a condizione del perfezionamento delle riserve puntuali indicate. Il presente verbale costituisce titolo per il pagamento del saldo e per le garanzie di legge.

Luogo e data [___]
Il Collaudatore [FIRMA] - Il DL [FIRMA] - L'Impresa [FIRMA]""",
["Dati dell'opera e dei soggetti","Documentazione esaminata (progetti, prove, verbali)","Sopralluogo con prove non distruttive ed esiti","Misure e contabilita'","Riserve da perfezionare","Dichiarazione finale e firme"],
"Schema conforme alla prassi di collaudo statico: i collaudi civili su opere private sono valutazioni di regolare esecuzione commesse dal committente; quelli di opere pubbliche seguono il D.Lgs 36/2023."))

DOCS.append(("sal_registro",
"Stato Avanzamento Lavori (SAL) e registro di contabilita' di cantiere",
"""# STATO AVANZAMENTO LAVORI (SAL) N. [___]
Data: [___] - Contratto: [___] del [___]
Impresa: [___] - DL: [___]

| Voce computo | Descrizione | Importo contrattuale (EUR) | % eseguito | Importo eseguito (EUR) |
|---|---|---|---|---|
| 1 | Demolizioni | 2.400,00 | 100 | 2.400,00 |
| 2 | Tramezzi | 3.900,00 | 100 | 3.900,00 |
| 3 | Impianto elettrico | 6.200,00 | 85 | 5.270,00 |
| 4 | Impianto idraulico | 4.800,00 | 70 | 3.360,00 |
| 5 | Massetti | 3.300,00 | 60 | 1.980,00 |
| 6 | Pavimenti | 4.100,00 | 0 | 0,00 |
| 7 | Bagno completo | 5.600,00 | 0 | 0,00 |
| 8 | Tinteggiatura | 2.800,00 | 0 | 0,00 |
| 9 | Sicurezza (non ribassabile) | 1.100,00 | 80 | 880,00 |
| | **TOTALE PARZIALE** | **34.200,00** | | **17.790,00** |
| 10 | Spese generali e utile (13%) | 4.446,00 | | 2.312,70 |
| | **STATO AVANZAMENTO LORDO** | **38.646,00** | | **20.102,70** |
| 11 | Ritenuta di garanzia 5% | | | -1.005,14 |
| | **NETTO DA PAGARE SAL n. [___]** | | | **19.097,56** |

## NOTE CONTABILI
1. L'avanzamento e' calcolato sulle lavorazioni ultimandone le quantita' con misure a campione o verifica in sito.
2. La ritenuta di garanzia (5% sui lavori, come da contratto) viene trattenuta fino al collaudo/saldo finale e restituita a garanzia decennale secondo le forme contrattuali.
3. Sono escluse dal SAL le lavorazioni coperte da acconti e le forniture a carico del cliente.
4. Eventuali varianti approvate per iscritto sono evidenziate in registro varianti allegato.""",
["Tabella voci con % eseguito e importi","Totali parziali, spese generali, stato avanzamento","Ritenuta di garanzia e netto da pagare","Note contabili (avanzamento, ritenute, varianti)"],
"Il SAL e' il documento che trasforma il computo in pagamento: la struttura con % di avanzamento e ritenuta di garanzia e' quella tipica dei contratti di appalto privati."))

# ---------------- writer ----------------
os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "documenti_tecnici_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Modelli di documenti tecnici a cura di Kimi",
    "url": "",
}
out = []
for i, (tipo, contesto, testo, sezioni, note) in enumerate(DOCS, 1):
    rec = dict(meta)
    rec.update({
        "id": f"DOC-{i:02d}",
        "doc_type": tipo,
        "contesto": contesto,
        "sezioni": sezioni,
        "testo_completo": testo.strip(),
        "note_redazionali": note,
    })
    out.append(rec)

path = 'parsed/documenti_tecnici.jsonl'
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritti {len(out)} documenti -> {os.path.abspath(path)}")
