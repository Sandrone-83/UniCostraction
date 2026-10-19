---
name: workplace-accessibility-barrier-management
description: Gestisce audit e remediation dell'accessibilità nei luoghi di lavoro per lavoratori, visitatori e soccorritori, collegando barriere, uso, sicurezza e responsabilità senza sostituire progettista, datore di lavoro o autorità.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: accessibilità e barriere nei luoghi di lavoro
---

# Accessibilità e barriere nei luoghi di lavoro

## Attivazione e input

Attiva questa skill quando un luogo di lavoro, cantiere, ufficio, stabilimento o spazio di servizio deve essere verificato per accesso, uso, orientamento, evacuazione e adattamento ragionevole di persone con disabilità. È distinta da accessibility-universal-design, che tratta principi generali di uso inclusivo, e da construction-site-safety e occupational-health-exposure-hygiene, che trattano sicurezza e salute dei lavoratori.

Raccogli uso e popolazione, lavoratori/visitatori, mansioni, percorsi, ingressi, parcheggi, ascensori, rampe, porte, servizi, spogliatoi, postazioni, segnaletica, illuminazione, acustica, allarmi, vie di esodo, accesso soccorritori, cantiere/fasi, emergenze, edificio esistente, titolo, vincoli, accomodamenti richiesti, DVR/PEE pertinenti e responsabili. Se uso, barriera, percorso, misura o scenario di emergenza non sono verificabili, lo stato è blocked.

## Workflow

1. **Gate del perimetro:** mappa persone, compiti, orari, accessi, servizi, aree interdette, lavorazioni e visitatori; separa accessibilità permanente, temporanea e di emergenza.
2. **Gate del percorso:** rileva catena continua da arrivo a posto di lavoro, servizi e uscita con larghezze, dislivelli, pendenze, manovre, porte, pavimenti, ostacoli, segnaletica e alternative.
3. **Gate dell'uso:** prova con scenari diversi di mobilità, vista, udito, cognizione e fatica; verifica che la soluzione non renda insicuro il lavoro o il soccorso.
4. **Gate normativo:** collega ogni requisito a norma edilizia, sicurezza sul lavoro, prevenzione incendi, vincolo, contratto o accommodation individuale; separa requisito cogente, buona pratica e preferenza.
5. **Gate della remediation:** ordina eliminazione barriera, soluzione tecnica, organizzazione, ausilio, formazione e manutenzione con owner, costo, priorità e misura temporanea sicura.
6. **Gate della verifica:** controlla misura installata, fruibilità, segnalazione, manutenzione, allarmi, esodo, test con utenti e aggiornamento di planimetrie, procedure e valutazione rischi.
7. **Gate della continuità:** riesamina cambi di layout, macchine, personale, cantiere, appaltatori, emergenza e feedback; chiudi solo con evidenza e accettazione del responsabile.

## Output

Produci un workplace_accessibility_record con utenti/scenari, mappa percorsi, barriere, requisiti, evidenze, rischio, remediation, accomodamenti, responsabili, priorità, test, manutenzione e stato screened, conditional, remediation_in_progress, accessible_for_defined_scenario o blocked. Non usare accessible come garanzia universale.

## Quality gates

- Percorso, destinazione, uso, emergenza e popolazione sono definiti, non solo fotografati.
- Misure, pendenze, spazi, soglie, porte, servizi, segnaletica, allarmi e vie di esodo hanno evidenza.
- Accessibilità, adattabilità, visitabilità, sicurezza antincendio e accommodation individuale sono distinte.
- La soluzione non crea un nuovo rischio di inciampo, incendio, evacuazione, privacy o interferenza lavorativa.
- Ogni barriera ha owner, priorità, data, misura provvisoria, chiusura e manutenzione.
- La verifica include utenti o competenze pertinenti e non trasforma una checklist in certificazione.

## Evidenza e provenienza

Conserva rilievi, foto, misure, planimetrie, percorso, scenari, interviste, segnalazioni, norme applicate, DVR/PEE pertinenti, ordini, installazioni, test, manutenzione e approvazioni. Marca osservazione, misura, requisito, feedback, valutazione e assunzione. Minimizza dati sanitari o di disabilità, separa le informazioni individuali dal report tecnico e limita accesso a chi ne ha bisogno.

## Fonti ufficiali e diritti

- [Normattiva - D.M. 14 giugno 1989, n. 236](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=089G0298&atto.dataPubblicazioneGazzetta=1989-06-23&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=19%2F03%2F2026&generaTabId=true&qId=&tabID=&tipoDettaglio=singolavigenza&title=lbl.dettaglioAtto): prescrizioni tecniche di accessibilità, adattabilità e visitabilità, da applicare nel perimetro pertinente.
- [Normattiva - D.Lgs. 9 aprile 2008, n. 81](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): salute e sicurezza nei luoghi di lavoro, valutazione dei rischi e gestione dell'emergenza.
- [Normattiva - D.P.R. 1 agosto 2011, n. 151](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=011G0193&atto.dataPubblicazioneGazzetta=2011-09-22): raccordo con esodo e prevenzione incendi quando l'accessibilità riguarda attività soggette.
- [Normattiva - Legge 18/2009](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2009-03-03;18): ratifica della Convenzione ONU sui diritti delle persone con disabilità, come contesto da non trasformare in testo copiato o parere.

La procedura, la matrice barriera-rimedio e i test sono originali. Diritti: `official_public_legal_text_verify_current_consolidation` per norme e `official_reference_only_no_text_reproduced` per pagine ufficiali; disegni, fotografie, dati di lavoratori, consulenze e software restano soggetti a licenza, privacy e accesso.

## Confini professionali e legali

La skill non certifica accessibilità, agibilità, sicurezza, accommodation o assenza di barriere, non ordina lavori e non decide idoneità individuale al lavoro. Non sostituisce progettista, datore di lavoro, RSPP, medico competente, professionista antincendio, disability/accessibility expert, rappresentante dei lavoratori o autorità. Una misura conforme a un parametro non garantisce da sola uso sicuro per ogni persona o scenario.

## Failure modes

- **Rampa conforme ma percorso interrotto:** verifica la catena completa e le alternative.
- **Universal design usato come certificazione:** separa principio, requisito e atto professionale.
- **Accomodamento individuale pubblicato:** minimizza e protegge dati sanitari/disabilità.
- **Accessibilità confusa con esodo:** coordina antincendio, emergenza, lavoro e manutenzione.
- **Misure provvisorie senza owner:** assegna durata, controllo e chiusura.
- **Barriera eliminata creando rischio:** ripeti test con utenti, macchine, allarmi e soccorso.

## Strumenti

Usa user/scenario register, route map, measurement sheet, barrier register, requirement-source matrix, risk and accommodation log, remediation backlog, temporary-control register, test/witness sheet e maintenance calendar. Automatizza misure e scadenze; non pubblicare dati individuali o dichiarare conformità senza revisione competente.
