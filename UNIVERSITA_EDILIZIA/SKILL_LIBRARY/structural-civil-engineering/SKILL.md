---
name: structural-civil-engineering
description: Imposta e controlla analisi strutturali e opere civili a partire da dati tracciati, senza sostituire progettazione, calcolo, collaudo o firma del professionista abilitato.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: strutture e opere civili
---

# Ingegneria strutturale e civile

## Attivazione e input

Usa la skill per schema statico, azioni, combinazioni, modello numerico, dettagli costruttivi, opere geotecniche o controlli di coerenza. Richiedi destinazione d'uso, geometria e rilievo, materiali, terreno, sismicità, vita nominale, classe d'uso, condizioni esistenti, elaborati e norma/edizione applicabile.

Marca ogni input come misurato, documentato, assunto o da prove. Se manca un dato che può cambiare il modello, non inventarlo.

## Workflow

1. Definisci sistema resistente, vincoli, fasi costruttive, durabilità e stato limite.
2. Costruisci registro delle azioni: origine, intensità, combinazione, unità, verso e fonte.
3. Controlla unità, assi, segni, eccentricità, vincoli e congruenza tra geometria e modello.
4. Scegli metodo e strumento proporzionati; registra versione, impostazioni e semplificazioni.
5. Esegui controlli indipendenti di ordine di grandezza e, quando possibile, un secondo percorso.
6. Collega risultati a sezioni, armature, collegamenti, fondazioni e dettagli eseguibili.
7. Documenta risultati, limiti, sensibilità e punti che richiedono revisione del progettista.

## Output

Fornisci relazione di ipotesi, tabella azioni/combinazioni, modello o estratto riproducibile, risultati con unità, elaborati di dettaglio, registro delle verifiche e elenco delle decisioni aperte. Non consegnare numeri senza contesto di modello e norma.

## Quality gates

- Geometria, materiali, unità e vincoli sono dichiarati e coerenti.
- Le combinazioni citano la fonte e distinguono valori caratteristici, di progetto e risultati.
- Almeno un controllo manuale o alternativo intercetta errori di scala e ordine di grandezza.
- Le condizioni del terreno e dell'esistente non sono dedotte da una sola foto.
- La revisione finale è firmata o approvata dal soggetto competente quando richiesta.

## Evidenza e provenienza

Conserva input, versione della norma, versione del software, file di modello, log di calcolo, impostazioni, grafici, controlli indipendenti e data. Usa hash dei file e un registro delle modifiche. Una simulazione non prova da sola la sicurezza dell'opera.

## Confini professionali e legali

Non rilasciare certificazioni, asseverazioni, collaudi o dichiarazioni di sicurezza. NTC, Eurocodici, regole regionali e autorizzazioni sismiche devono essere interpretati e applicati dal professionista responsabile. In presenza di rischio immediato, indicare la necessità di mettere in sicurezza e coinvolgere il tecnico/autorità, senza dare istruzioni operative pericolose.

## Failure modes

- **Scala errata:** confronta una quota nota con il modello e sospendi i risultati.
- **Vincoli artificiali:** confronta reazioni e deformate con lo schema statico atteso.
- **Materiale non provato:** usa scenario dichiarato e chiedi campagna di indagini.
- **Modello "nero":** richiedi input, log e output leggibili prima di accettare il risultato.
- **Norma obsoleta:** verifica Gazzetta, Normattiva e prescrizioni locali prima della conclusione.

## Strumenti

Usa foglio di calcolo controllato, script numerici, software FEM autorizzato, visualizzatore di modelli e strumenti di confronto documentale. Ogni automatismo deve produrre log, unità e versione; non usare un export grafico come unico audit.

## Fonti ufficiali e diritti

- [Gazzetta Ufficiale — DM 17 gennaio 2018, NTC](https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.codiceRedazionale=18A00716&atto.dataPubblicazioneGazzetta=2018-02-20): testo ufficiale; verificare aggiornamenti e circolari, nessun testo riprodotto.
- [European Commission JRC — Eurocodes](https://eurocodes.jrc.ec.europa.eu/): riferimento istituzionale e tecnico; i testi normativi possono avere diritti/licenze proprie.
- [Normattiva — edilizia](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=0&atto.codiceRedazionale=001G0429&atto.dataPubblicazioneGazzetta=2001-10-20): fonte legislativa pubblica; controllare il consolidato vigente.

La skill è una procedura originale di controllo e non costituisce progetto strutturale o parere professionale.
