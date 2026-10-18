---
name: survey-geospatial-topography-control
description: Gating operativo di rilievi topografici e geospaziali, dalla definizione del sistema di riferimento alla riconciliazione tra nuvola, punti di controllo e modello; non certifica confini o precisione senza tecnico abilitato.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: rilievo, geospaziale e topografia
---

# Controllo operativo di rilievo geospaziale e topografico

## Attivazione e input

Attiva questa skill quando una nuvola di punti, un rilievo GNSS/total station, un ortofoto o un modello terreno deve diventare una base controllata per CAD, BIM, computo, cantiere o confronto as-built. È una faccetta di controllo della catena di misura distinta da cad-autocad-freecad, bim-ifc-openbim e dalle skill di progettazione: non disegna il progetto e non attribuisce valore legale al confine.

Prima raccogli commessa, area e scopo, sistema di riferimento orizzontale/verticale, epoca e geoid model, unità, tolleranza richiesta, metodo e strumenti, certificati/calibrazioni, punti di controllo e verifica, datum locali, formato, coordinate note, autorizzazioni di accesso e data del rilievo. Se CRS, quota di riferimento, epoca o tolleranza non sono dichiarati, lo stato è blocked.

## Workflow

1. **Gate del brief:** separa precisione necessaria per progetto, quantità, monitoraggio o confine; scrivi una matrice uso -> tolleranza -> evidenza e non dedurre accuratezza dal numero di decimali.
2. **Gate geodetico:** registra CRS, EPSG o identificativo equivalente, datum verticale, geoid/griglia, epoca, trasformazioni e convenzioni degli assi. Mantieni coordinate originali e trasformate, con parametri e residui.
3. **Gate della misura:** acquisisci inventario strumento, firmware, calibrazione, operatore, metodo, stazioni, altezza antenna/prisma, condizioni e log grezzi. Non sostituire osservazioni grezze con un export già filtrato.
4. **Gate dei controlli:** distribuisci punti indipendenti dentro e ai margini dell'area; calcola residui orizzontali/verticali e statistiche per sottoarea. Un punto usato per l'allineamento non è anche prova indipendente.
5. **Gate di densità e rumore:** classifica terreno, fabbricati, vegetazione, oggetti mobili e artefatti; misura buchi, sovrapposizioni, outlier e occlusioni. Ogni rimozione ha regola, versione e conteggio prima/dopo.
6. **Gate di riconciliazione:** sovrapponi nuvola, punti di controllo, ortofoto e CAD/BIM con stesso CRS; verifica scale, rotazioni, quote, sezioni campione, superfici e disallineamenti sistematici. Se l'errore è sistematico, riapri trasformazione e non correggere graficamente a mano.
7. **Gate della consegna:** genera pacchetto con dati grezzi, derivati, report dei controlli, manifest degli hash, CRS/epoca, limitazioni e firma o revisione del tecnico responsabile. pass vale solo per lo scopo dichiarato.

## Output

Consegna un survey_control_record con brief, area, CRS/epoca, strumenti, controlli indipendenti, tolleranze, residui, regole di filtraggio, trasformazioni, hash dei file e stato pass, conditional o blocked. Includi tavole di controllo, sezioni campione e una lista di anomalie non risolte; non consegnare solo un DWG o una mesh priva di provenienza.

## Quality gates

- CRS orizzontale e verticale, epoca, unità e trasformazione sono espliciti e riproducibili.
- Esiste almeno un controllo indipendente dalla fase di registrazione/allineamento.
- Tolleranza e metodo sono dichiarati per ogni uso; densità non viene confusa con accuratezza.
- Ogni filtro conserva input, regola, versione e quantità rimossa.
- Le quote e le superfici sono confrontate su sezioni e punti, non solo su una vista colorata.
- L'uso catastale, di confine, strutturale o di monitoraggio è bloccato senza verifica e responsabilità professionale appropriate.

## Evidenza e provenienza

Registra file grezzi e derivati, hash, timestamp con fuso, operatore, strumento/seriale, calibrazione, log, CRS/EPSG, griglia/geoid, epoca, parametri di trasformazione, controlli, residui, software/versione e decisioni di filtraggio. Una mappa o uno screenshot è evidenza illustrativa, non sostituisce osservazioni e report. Conserva solo ciò che la commessa e i diritti consentono; dati di persone, proprietà e sicurezza sono minimizzati e accessibili per ruolo.

## Fonti ufficiali e diritti

- [OGC Standards](https://www.ogc.org/standards/): standard per servizi e dati geospaziali; verificare versione e termini prima di incorporare specifiche o schemi.
- [INSPIRE Knowledge Base](https://knowledge-base.inspire.ec.europa.eu/): metadati, temi e specifiche applicative dell'infrastruttura europea; usare come riferimento di interoperabilità, non come certificazione della misura.
- [Istituto Geografico Militare](https://www.igmi.org/): riferimenti e prodotti cartografici ufficiali italiani; condizioni d'uso e licenze del singolo prodotto restano da controllare.

I link e gli identificativi sono provenance di ricerca. Il procedimento, i record di controllo e le checklist sono originali; non copiare testi, dataset o tavole protette. Lo stato diritti della skill è reference_only: citazione e interoperabilità non autorizzano redistribuzione di dati o specifiche complete.

## Confini professionali e legali

La skill non esegue rilievi, non certifica precisione, quote, confini, volumetrie, agibilità o conformità catastale/urbanistica. Non sostituisce topografo, geometra, ingegnere, autorità cartografica o responsabile della sicurezza. Un risultato pass significa soltanto adeguato allo scopo e alla tolleranza registrati; dati senza CRS, epoca, controlli o autorizzazione sono inutilizzabili per decisioni.

## Failure modes

- **CRS o quota impliciti:** blocca la consegna e richiedi datum, geoid, epoca e trasformazione.
- **Allineamento circolare:** separa i punti di fitting dai check point indipendenti e ricalcola residui.
- **Decimali scambiati per precisione:** riporta tolleranza misurata e incertezza, non la formattazione.
- **Filtraggio distruttivo:** ripristina il grezzo, versiona la regola e calcola l'impatto su superfici e quantità.
- **Occlusioni coperte da interpolazione:** marca le zone non osservate e non usarle per confini o quantità certe.
- **Uso catastale o strutturale implicito:** cambia stato in blocked e indirizza al professionista abilitato.

## Strumenti

Usa software di elaborazione con log e versionamento, calcolo indipendente dei residui, visualizzatore 2D/3D e un manifest degli artefatti. Ogni automatismo deve produrre anche report numerico e non solo colore, mesh o screenshot.
