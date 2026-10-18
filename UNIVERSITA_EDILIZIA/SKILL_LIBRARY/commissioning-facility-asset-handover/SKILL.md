---
name: commissioning-facility-asset-handover
description: Metodo di commissioning, verifica prestazionale e handover controllato verso facility e asset management; non dichiara conformità, collaudo o operatività senza prove e responsabili autorizzati.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: commissioning, facility e asset management
---

# Commissioning e handover di facility e asset

## Attivazione e input

Attiva questa skill quando un edificio, impianto o sistema digitale deve passare da costruzione o riqualificazione a esercizio, manutenzione e gestione dell'asset. È una faccetta di prova, evidenza e trasferimento operativo distinta da bim-ifc-openbim, mep-energy-systems e documents-pdf-computo-sal-due-diligence: non collauda né prende in carico un impianto per conto del gestore.

Prima raccogli requisiti dell'owner, criteri prestazionali, asset register, spazi e sistemi, ruoli, contratto, fasi, scenari di uso, BMS/controlli, manuali, as-built, garanzie, formazione, sicurezza, piano manutenzione, strumenti di misura, test scripts, baseline, witness e criteri di accettazione. Se owner requirements, responsabile, asset identity o criteri misurabili mancano, lo stato è blocked.

## Workflow

1. **Gate dei requisiti:** crea una matrice requisito -> asset/sistema -> test -> evidenza -> responsabile -> criterio pass/fail; separa requisito contrattuale, prestazionale e operativo.
2. **Gate della configurazione:** congela identificativi, ubicazione, versioni firmware/software, interfacce, setpoint, schemi, seriali e dipendenze. Ogni variazione riapre i test toccati.
3. **Gate del test design:** scrivi pre-functional check, test funzionale, test integrato, trend, allarmi, perdita alimentazione e scenario anomalo con precondizioni, strumenti, durata, sicurezza e criteri numerici.
4. **Gate dell'esecuzione:** registra condizioni iniziali, valori grezzi, timestamp, unità, operatore, witness, deviazioni e retest. Uno screenshot BMS senza log o prova indipendente non dimostra il comportamento.
5. **Gate della riconciliazione:** collega esito ai requisiti e all'asset register; classifica open issue, deroga, punch item, responsabilità e data di chiusura. Non usare una percentuale di completamento per nascondere un test critico fallito.
6. **Gate dell'handover:** verifica as-built, manuali, spare parts, garanzie, formazione, accessi, backup, cybersecurity operativa, piano manutenzione e dati per l'operatore. Trasferisci solo versioni approvate e registrane il destinatario.
7. **Gate del periodo iniziale:** definisci seasonal test, performance review, monitoraggio post-occupazione e criteri di uscita. La chiusura del commissioning è diversa dalla scadenza della garanzia.

## Output

Consegna un commissioning_record con requisiti, matrice di copertura, register degli asset, script e log di prova, deviazioni, open issues, documenti consegnati, formazione, approvazioni e stato ready, conditional o blocked. Ogni esito deve essere ripetibile da un tecnico qualificato, con evidenza e data.

## Quality gates

- Ogni requisito critico ha test, criterio pass/fail, responsabile ed evidenza.
- Test funzionale, integrato, allarme e scenario anomalo sono distinti.
- Asset, seriale/versione, posizione e documento sono riconciliati.
- I dati di misura sono grezzi o tracciati alla fonte e hanno unità/timestamp.
- Le issue aperte hanno severità, owner, scadenza, workaround e retest.
- Handover e accettazione sono firme o approvazioni di soggetti autorizzati, non una deduzione automatica.

## Evidenza e provenienza

Conserva requisiti approvati, versioni di disegni e modelli, script, log, trend, foto contestualizzate, strumenti e calibrazioni, verbali, issue, revisioni, hash e destinatari. Marca la fonte di ogni attributo del registro asset: as-built, targa, BMS, manuale o rilievo. Applica controllo accessi a credenziali, mappe di sicurezza e dati personali; non incorporare segreti nei report.

## Fonti ufficiali e diritti

- [ISO 41001](https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/06/80/68021.html): riferimento ufficiale per sistemi di gestione delle facility; acquistare e consultare il testo con licenza.
- [ISO 55001](https://committee.iso.org/sites/tc251/home/projects/published/iso-55001.html): quadro ufficiale per asset management e ciclo di vita; la pagina non sostituisce lo standard.
- [ISO 19650](https://www.iso.org/standard/68078.html): riferimento ufficiale per gestione dell'informazione lungo il ciclo di vita; verificare parte ed edizione applicabile.

Le fonti ISO sono restricted: si citano identificativo, titolo e concetto necessario senza copiare clausole. Matrici, script esemplificativi, record e procedura sono originali. Diritti della skill: reference_only; la consegna di dati di progetto resta soggetta a contratto, riservatezza e ruoli.

## Confini professionali e limiti

La skill non sostituisce collaudatore, direttore lavori, progettista, responsabile sicurezza, manutentore, gestore energetico o owner. Non abilita impianti, non certifica prestazione energetica, antincendio, elettrica, strutturale o cybersecurity e non concede accessi a BMS. Un test superato vale solo per configurazione, condizioni, strumenti e criterio registrati.

## Failure modes

- **Manuale senza prova:** cambia l'evidenza in non dimostrata e pianifica test.
- **BMS simulato o screenshot isolato:** richiedi log, trend, allarme e prova sul campo.
- **Asset duplicate o seriali discordanti:** congela handover, deduplica e riconcilia con targa/as-built.
- **Issue critica chiusa verbalmente:** riapri con owner, evidenza e retest.
- **Credentials trasferite nel report:** revoca il segreto, sostituiscilo con riferimento sicuro e registra l'accesso.
- **Accettazione automatica:** blocca e richiedi firma o approvazione del soggetto autorizzato.

## Strumenti

Usa registro requisiti, asset database, test runner con timestamp, repository versionato e issue tracker. Le automazioni possono controllare completezza, collegamenti e soglie; non possono witnessare una prova o firmare l'handover.
