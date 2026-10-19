---
name: building-acoustic-practice-passive-requirements
description: "Impostazione e controllo della pratica acustica edilizia e della matrice dei requisiti passivi, con coordinamento dei dettagli costruttivi prima della verifica in opera."
metadata:
  library: "UNIVERSITA_EDILIZIA/SKILL_LIBRARY"
  version: "G31.1"
  domain: "pratiche acustiche edilizie e requisiti passivi"
---

# Pratiche acustiche edilizie e requisiti passivi

Questa skill traduce destinazioni d'uso, involucro, partizioni e impianti in una pratica acustica tracciabile: requisiti applicabili, assunzioni di progetto, dettagli contro i ponti acustici e gate per la verifica in opera. E' distinta dal controllo metrologico di misure acustiche: prepara il progetto e la pratica, non dichiara da sola la prestazione realizzata.

## Attivazione e input

Attivare per nuova costruzione, ristrutturazione con modifica delle caratteristiche acustiche, cambio d'uso, pratica edilizia con relazione acustica o coordinamento dei requisiti passivi. Richiedere:

- destinazioni d'uso, categorie di ambienti, confini tra unita, ricettori sensibili e classificazione acustica locale;
- piante, sezioni, facciate, stratigrafie, giunti, cavedi, attraversamenti, serramenti e dettagli di posa;
- sorgenti interne o esterne, impianti continui/discontinui, traffico e vincoli di orario;
- regolamento edilizio, norme regionali/comunali, contratto e obiettivi prestazionali;
- relazione geologica/strutturale e impiantistica necessarie a coordinare massa, trasmissioni laterali e vibrazioni.

Se la destinazione d'uso o il regime comunale non sono confermati, lo stato e `screening_only`.

## Workflow

1. Identificare opere, ambienti, ricettori e confini di responsabilita; costruire una matrice requisito-elemento con fonte e data.
2. Distinguere requisiti passivi dell'edificio, clima/impatto acustico esterno, rumore degli impianti, acustica degli ambienti e sicurezza sul lavoro. Non usare un solo limite per tutti i fenomeni.
3. Selezionare il regime applicabile: DPCM 5 dicembre 1997, legge quadro, eventuali regole regionali e comunali, prescrizioni del titolo o del committente. Registrare ogni conflitto e chiedere decisione al tecnico competente.
4. Per pareti, solai, facciate, serramenti e impianti definire prestazione di progetto, dati del sistema, giunti, discontinuita, attraversamenti e modalita di posa. Considerare trasmissioni laterali e tolleranze, non solo il valore di laboratorio.
5. Coordinare architettura, strutture, MEP, antincendio e dettagli di cantiere. Ogni passaggio impiantistico deve avere una soluzione acustica verificabile e un proprietario dell'azione.
6. Redigere relazione/pratica acustica con planimetrie marcate, ipotesi, modello o calcoli, schede delle stratigrafie, note sui limiti e piano di controllo. Separare dichiarazioni di progetto da risultati in opera.
7. Prima dell'esecuzione, emettere un hold point su materiali e dettagli. A fine opera trasferire al team di collaudo il registro delle assunzioni, i punti critici e la procedura di misura da applicare secondo norme vigenti.

## Output

Produrre un `building_acoustic_practice_record` con `status` `screening_only`, `design_basis`, `ready_for_filing`, `hold_point` o `ready_for_test`; matrice ambienti-requisiti; tavole e dettagli; fonti e versioni; calcoli/assunzioni; interferenze aperte; schema di controllo in cantiere; firma e ruolo del tecnico quando presenti.

## Quality gates

- **Perimetro**: usi, ambienti, ricettori e confini tra unita sono completi.
- **Regime**: DPCM, legge, regola locale, titolo e contratto sono citati con data e gerarchia.
- **Progetto**: ogni requisito ha elemento, valore/criterio, fonte dati e dettaglio di posa.
- **Interfacce**: facciate, giunti, cavedi, attraversamenti e impianti hanno controllo dedicato.
- **Costruibilita**: il dettaglio puo essere posato e ispezionato; materiale di brochure non vale come posa.
- **Pratica**: relazione, elaborati, firma del ruolo competente e ricevuta dell'ente sono distinti.
- **Collaudo**: nessuna conformita finale e dichiarata senza misure o attestazioni previste dal procedimento.

## Evidenza e provenienza

Conservare versione di piante e stratigrafie, schede tecniche, rapporti di laboratorio, fotografie dei nodi prima della chiusura, verbali di coordinamento, modello/calcolo, data e ruolo dell'autore. Ogni valore deve distinguere laboratorio, progetto, stima e misura. Le misure in opera devono riportare strumento, taratura, ambiente, condizioni e norma applicata; la skill non li inventa.

## Fonti ufficiali e diritti

I contenuti della skill sono originali e sintetici: rispettare copyright, licenze, termini d'uso dei portali e diritti sugli asset; non redistribuire testi o allegati protetti.

- [Legge 447/1995 su Normattiva](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=095G0477&atto.dataPubblicazioneGazzetta=1995-10-30&bloccoAggiornamentoBreadCrumb=true&dataVigenza=&generaTabId=true&tabID=&tipoDettaglio=vigente&title=lbl.dettaglioAtto): legge quadro sull'inquinamento acustico; `official_public_legal_text_verify_current_consolidation`.
- [DPCM 5 dicembre 1997 in Gazzetta Ufficiale](https://www.gazzettaufficiale.it/eli/id/1997/12/22/97A10190/sg): requisiti acustici passivi degli edifici; `official_public_legal_text_verify_current_consolidation`.
- [D.Lgs. 194/2005 su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2005%3B194): mappatura e gestione del rumore ambientale, solo quando il caso la richiama; `official_public_legal_text_verify_current_consolidation`.
- Norme UNI/ISO per calcolo e misura sono identificate per codice ed edizione ma non riprodotte; `official_standard_paid_or_restricted_reference_only`.

I riferimenti sono usati senza copiare testi protetti. La verifica di applicabilita regionale/comunale e la data del progetto sono obbligatorie.

## Confini professionali e legali

La skill non sostituisce il tecnico competente in acustica, il progettista, il direttore dei lavori, il laboratorio o l'autorita comunale. Non rilascia valutazione di impatto/clima acustico, deroga, certificazione di conformita o collaudo. Non trasforma una previsione in risultato in opera e non autorizza materiali o varianti senza responsabilita professionale assegnata.

## Failure modes

- Requisito passivo confuso con impatto acustico esterno o rumore di cantiere: riaprire la classificazione.
- Valore Rw di laboratorio usato come R'w in opera: inserire trasmissioni laterali, posa e tolleranze.
- Destinazione d'uso o regolamento comunale errato: sospendere la pratica e verificare l'autorita competente.
- Attraversamenti e impianti lasciati fuori dalla matrice: bloccare il dettaglio esecutivo.
- Relazione firmata presunta dal solo file: chiedere firma, ruolo e protocollo.
- Misura finale senza taratura o condizioni: classificare l'evidenza come insufficiente e non dichiarare conformita.

## Strumenti

Usare viewer BIM/CAD/PDF, matrice requisito-elemento, calcolatore acustico o foglio versionato, archivio schede, foto di cantiere, checklist dei nodi, strumenti di misura solo gestiti da personale competente e registro di protocollo. Automatizzare confronto e completezza, mai la firma o la dichiarazione di conformita.
