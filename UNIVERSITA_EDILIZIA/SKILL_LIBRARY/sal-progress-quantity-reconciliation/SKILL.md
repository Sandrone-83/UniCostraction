---
name: sal-progress-quantity-reconciliation
description: Riconcilia SAL, libretti misure, computi, ordini e pagamenti per quantità e avanzamento con formule, versioni e scarti espliciti; non valida o approva il SAL.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: SAL e riconciliazione quantitativa
---

# Riconciliazione SAL, avanzamento e quantità

## Attivazione e input

Attiva questa skill quando occorre confrontare quantità eseguite, computo/contratto, libretti, contabilità, fotografie, ordini, verbali, fatture o pagamenti tra due date. È più stretta di `documents-pdf-computo-sal-due-diligence` e `public-procurement-company-contracts`: calcola e riconcilia, ma non approva il SAL né esprime parere contabile/contrattuale.

Richiedi contratto e quadro economico vigenti, elenco prezzi e revisione, computo baseline, libretti/verbali firmati, periodi e data di cut-off, unità, quantità precedenti, correnti e cumulative, percentuali, ritenute, varianti, anticipazioni, IVA, fatture/pagamenti, foto georiferite e ruolo del certificatore. Definisci se il lavoro è pubblico o privato e quale registro è autoritativo.

## Procedura originale

1. Crea una chiave stabile per ogni voce: contratto/variante, codice, descrizione, unità, prezzo, revisione e WBS; non unire righe simili senza mappatura.
2. Congela il cut-off e normalizza solo formati dichiarati. Conserva unità originarie, conversione, arrotondamento e autore; una conversione non è una misurazione.
3. Calcola `precedente + periodo = cumulativo` e `cumulativo <= quantità autorizzata`, con separazione tra quantità fisica, importo maturato, importo richiesto, importo approvato e importo pagato.
4. Riconcilia quantità con misure, elaborati, foto, verbali, consegne e stato reale; registra scarto numerico e ragione classificata (`fonte_mancante`, `unità`, `duplicato`, `variante`, `periodo`, `errore`).
5. Applica controlli indipendenti su subtotali, percentuali, arrotondamenti, prezziari, ritenute, IVA e varianti; non compensare uno scarto senza decisione autorizzata.
6. Produci un pacchetto di eccezioni con owner, soglia, evidenza e azione; chiedi conferma a DL/committente/contabilità secondo ruolo prima di cambiare lo stato.
7. Congela output e manifest: ogni nuova misura o documento riapre la riconciliazione della voce e il registro di revisione.

## Output

Consegna matrice voce/WBS, registro fonti e versioni, foglio formule, confronto precedente-periodo-cumulativo, scarti e soglie, lista mancanti/contraddizioni, riconciliazione economica distinta da quella fisica, report grafico, pacchetto evidenze e stato `calcolato/non verificabile/in attesa di approvazione`.

## Quality gates

- Ogni quantità ha unità, periodo, fonte e responsabile; ogni importo ha prezzo/revisione e formula.
- Le quantità cumulative non superano baseline/variante senza issue autorizzata.
- Fisico, contabile, fiscale e pagamento sono colonne diverse, mai una percentuale unica.
- Le somme sono ricalcolate con un metodo indipendente e le tolleranze sono dichiarate.
- Un documento mancante produce `non verificabile`, non una quantità zero o una stima presentata come misurata.
- Il report non usa `approved`, `validato` o `certificato` se il ruolo competente non lo ha attestato.

## Evidenza e provenienza

Conserva hash dei documenti, data di ricezione, pagine/righe, foto e coordinate, versioni del computo/prezziario, script o foglio, formule, arrotondamenti, soglie e log. Per ogni scarto conserva valore sorgente, valore riconciliato, criterio e decisione; registra chi ha approvato la correzione e quando.

## Confini professionali e diritti

Una riconciliazione automatica non è validazione del SAL, collaudo, certificato di pagamento, revisione contabile o parere legale. Non alterare libretti, firme, verbali o registri autoritativi; non inviare richieste di pagamento né attestare lavori senza autorizzazione e competenza. Tratta dati economici, personali e contrattuali come riservati.

## Failure modes

- **Voce rinominata tra revisioni:** usa mapping approvato e conserva la vecchia chiave.
- **Prezzo senza revisione/data:** congela l'importo e segnala la base non determinabile.
- **Quantità cumulativa che riparte da zero:** confronta periodi e non sommare silenziosamente.
- **Foto senza data/posizione:** usale come indizio, non come misura certificata.
- **Scarto nascosto in arrotondamento:** mostra valore prima/dopo e soglia applicata.
- **SAL pubblico trattato come privato:** ferma l'output e verifica disciplina, ruoli e registro ufficiale.

## Strumenti e fonti ufficiali

Usa foglio o script deterministico con test sulle formule, parser PDF, manifest, viewer immagini e repository con audit. Per i profili pubblici verifica sempre release e applicabilità:

- [Normattiva — D.Lgs. 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2023-03-31%3B36%21vig=): Codice dei contratti pubblici nel testo vigente.
- [ANAC — Banca dati nazionale dei contratti pubblici](https://www.anticorruzione.it/-/banca-dati-nazionale-contratti-pubblici): dati e tracciabilità istituzionale da verificare per il caso concreto.
- [Gazzetta Ufficiale](https://www.gazzettaufficiale.it/): pubblicazione originaria e atti ufficiali.
- [ISO — ISO 19650](https://www.iso.org/standard/68078.html): gestione informativa come riferimento separato, a pagamento/restricted.

## Stato dei diritti

Normattiva, ANAC e Gazzetta sono fonti istituzionali da verificare per versione e contesto; ISO è riferimento ufficiale a pagamento/restricted. La matrice, le formule e il workflow di riconciliazione sono originali e non sostituiscono l'attestazione del ruolo competente.
