---
name: soil-contaminant-management
description: Organizza screening, caratterizzazione, segregazione e gestione di suolo e contaminanti in scavo o demolizione, senza qualificare giuridicamente materiali o autorizzare bonifiche.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: gestione suolo e contaminanti
---

# Gestione suolo e contaminanti

## Attivazione e input

Attiva questa skill quando scavi, demolizioni, serbatoi, sversamenti, riusi o terre/rocce fanno emergere un possibile contaminante e serve mantenere separati lotti, evidenze, percorsi e decisioni. È distinta da construction-waste-soil-management, che tratta soprattutto classificazione e movimento dei rifiuti/terre, e da geotechnical-foundation-data-gating, che tratta dati geotecnici e fondazioni.

Raccogli sito e uso attuale/futuro, storia attività e serbatoi, mappa scavi e stratigrafia, sorgente sospetta, lotti e volumi, odori/colori, acque, recettori, utilities, analiti e limiti applicabili, piano di campionamento, laboratorio, catena di custodia, autorizzazioni, terre da scavo, rifiuti misti, destinazioni e responsabili. Se origine, lotto, rischio o regime materiale sono incerti, lo stato è blocked.

## Workflow

1. **Gate del contenimento:** sospendi scavo o movimentazione rischiosa, delimita area, proteggi persone e recettori e previeni miscelazione, dilavamento e accesso non autorizzato.
2. **Gate della storia:** ricostruisci usi, serbatoi, incidenti, riempimenti, demolizioni, materiali e fonti geografiche con documenti e sopralluoghi, marcando ipotesi.
3. **Gate dei lotti:** definisci unità stratigrafiche e operative, volume, coordinate, profondità, omogeneità, segregazione e bilancio di massa.
4. **Gate del campionamento:** prepara piano rappresentativo, analiti, profondità, QA/QC, bianchi, laboratorio, catena di custodia, limiti e incertezza; un campione opportunistico non chiude il sito.
5. **Gate della qualifica:** separa suolo naturale, materiale di riporto, rifiuto, sottoprodotto, acqua e contaminante; instrada la qualificazione giuridica alla disciplina e all'autorità corrette.
6. **Gate della decisione:** confronta concentrazioni e rischio con uso e recettori, definisci caratterizzazione, messa in sicurezza, rimozione, trattamento, riuso o ulteriore indagine solo con soggetto autorizzato.
7. **Gate della tracciabilità:** conserva bilancio lotti, viaggi, impianti, autorizzazioni, analisi, certificati e chiusura; aggiorna piano dopo nuova evidenza o cambio destinazione.

## Output

Produci un soil_contaminant_record con storia, mappa lotti, sorgente, recettori, piano campioni, catena di custodia, risultati, limiti/versioni, volumi, regime condizionato, destinazioni, azioni e stato screened, characterized, controlled o blocked. Non assegnare un codice o una destinazione definitiva senza base documentale e autorità.

## Quality gates

- Storia, uso, sorgente, lotti, volumetria e recettori sono documentati.
- Campionamento, laboratorio, analiti, QA/QC e catena di custodia sono adeguati e tracciabili.
- Risultati, limiti, unità, data e versione sono confrontati senza occultare non-detect, outlier o gap.
- Lotti sospetti sono segregati e il bilancio di massa riconcilia scavo, deposito, trasporto e destino.
- Suolo, rifiuto, sottoprodotto, acqua e bonifica restano decisioni distinte.
- Autorità, progettista ambientale, laboratorio e responsabili approvano le decisioni che richiedono firma o autorizzazione.

## Evidenza e provenienza

Conserva titoli e uso sito, mappe, foto localizzate, sondaggi, stratigrafia, campioni, chain-of-custody, rapporti laboratorio, blank/duplicate, volumi, pesate, FIR o documenti ammessi, trasportatori, impianti, autorizzazioni, verbali e bilanci. Marca osservato, dichiarato, analizzato, stimato e approvato. Limita dati sensibili del sito e non modificare le analisi originali.

## Fonti ufficiali e diritti

- [Normattiva — D.Lgs. 152/2006](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2006-04-03;152!vig=): disciplina ambientale e siti contaminati, da verificare nella versione vigente.
- [Normattiva — DPR 120/2017](https://www.normattiva.it/eli/id/2017/08/07/17G00135/CONSOLIDATED/20210730): terre e rocce da scavo, con verifica di applicabilità temporale e materiale.
- [EUR-Lex — Direttiva 2004/35/CE, responsabilità ambientale](https://eur-lex.europa.eu/eli/dir/2004/35/oj): responsabilità per danno ambientale e contaminazione.
- [ISPRA](https://www.isprambiente.gov.it/it): dati e indirizzi istituzionali ambientali da usare come contesto verificato.

La matrice lotti, il workflow e i record sono originali. Diritti: official_reference_only_no_text_reproduced; testi normativi, rapporti di laboratorio, dati catastali, mappe e moduli di terzi mantengono diritti e condizioni. La skill non concede licenze o autorizzazioni.

## Confini professionali e legali

La skill non qualifica definitivamente rifiuto/sottoprodotto, non certifica assenza di contaminazione, non approva un piano di bonifica, non autorizza trasporto o riuso e non sostituisce geologo, chimico, laboratorio, progettista ambientale, responsabile del procedimento o autorità. Un risultato analitico non equivale da solo a conformità del sito o sicurezza per ogni uso.

## Failure modes

- **Campione singolo per grande lotto:** blocca la qualifica e ridisegna lotti e campionamento.
- **Terre miste a demolizione:** separa fisicamente e giuridicamente i flussi prima della movimentazione.
- **Limite errato per uso o matrice:** sospendi confronto e verifica norma, uso, unità e data.
- **Catena di custodia incompleta:** tratta il risultato come condizionato e ripeti secondo laboratorio.
- **Bilancio di massa non torna:** congela destino, riconcilia pesi/volumi e apri issue.
- **Riutilizzo deciso da foto:** richiedi caratterizzazione, autorizzazioni e revisione competente.

## Strumenti

Usa historical land-use register, GIS/lot map, sampling plan, chain-of-custody, lab register, soil volume ledger, weighbridge log, destination/authorization matrix e incident tracker. Automatizza coordinate, versioni, gap e bilanci; non classificare, autorizzare o dichiarare bonificato il materiale in autonomia.
