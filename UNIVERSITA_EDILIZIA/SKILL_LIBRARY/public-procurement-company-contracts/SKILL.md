---
name: public-procurement-company-contracts
description: Supporta qualificazione dell'opportunità, gara, contratto, esecuzione, SAL, varianti e contestazioni di imprese e stazioni appaltanti con ruoli e approvazioni tracciati.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: appalti e contratti
---

# Appalti pubblici, impresa e contratti

## Attivazione

Usa la skill per analisi bando, requisiti, matrice di conformità, offerta tecnica/economica, subappalto, cronoprogramma, contabilità, SAL, riserve, varianti, ordini, fatture e chiusura. Prima identifica stazione appaltante/impresa, ruolo, procedura, CIG/CUP quando applicabili, soglia, fase, scadenza e documenti.

## Workflow

1. Congela bando, disciplinare, capitolato, chiarimenti e allegati con versione e data.
2. Costruisci matrice requisiti: obbligatorio, dimostrabile, responsabile, evidenza, scadenza, rischio.
3. Separa ammissibilità, valutazione tecnica, prezzo, esecuzione e prova di adempimento.
4. Per l'offerta collega ogni promessa a risorsa, costo, tempo, prestazione misurabile e clausola.
5. In esecuzione usa registro ordini, submittal, non conformità, misure, SAL, certificati e pagamenti.
6. Per variante, riserva o contestazione conserva fatto, data, clausola, impatto, autorizzazione e risposta; non retrodatare.
7. Chiudi con stato documentale, collaudo/verifica, garanzie, as-built, formazione e obblighi residui.

## Output

Produci matrice bando, calendario scadenze, lista evidenze, proposta di quesiti, registro contrattuale, controllo SAL, log decisioni, registro rischi e pacchetto di chiusura. Lo stato può essere "da verificare", "dimostrato", "non dimostrato", "approvato" o "contestato".

## Quality gates

- La fonte applicabile è il testo contrattuale vigente e non un riassunto.
- Requisiti e dichiarazioni sono collegati a documenti firmabili e verificabili.
- Importi, quantità, IVA, prezziario, revisione e periodo sono espliciti.
- Ogni approvazione è attribuita al ruolo competente.
- BDNCP/portale e protocolli sono usati secondo il profilo autorizzato.

## Evidenza e provenienza

Conserva bando, chiarimenti, verbali, PEC/protocolli, file firmati, log di piattaforma, versioni e hash. Non trattare una pagina pubblica o un export di piattaforma come completo senza controllare data, filtri e campo di estrazione.

## Confini professionali e legali

Il Codice dei contratti, il contratto, gli atti di gara e le norme societarie richiedono verifica aggiornata e consulenza qualificata. La skill non decide ammissibilità, aggiudicazione, responsabilità, riserve, responsabilità amministrativa o strategia legale; non invia offerte, dichiarazioni, PEC o rinunce senza autorizzazione esplicita.

## Failure modes

- **Bando modificato:** sostituisci il pacchetto solo dopo confronto e changelog.
- **Requisito interpretato in modo estensivo:** chiedi chiarimento formale.
- **Promessa commerciale non prezzata:** segnala rischio di esecuzione e margine.
- **SAL da foto soltanto:** collega misura, verbale, contratto e approvazione.
- **Versione storica usata come vigente:** verifica data di pubblicazione e fase.

## Strumenti

Usa repository con permessi, fogli di matrice, firma digitale, PEC/portale ufficiale, strumenti di confronto PDF e calcolo controllato. Un modello linguistico può preparare bozze e domande, non autenticare documenti o assumere impegni.

## Fonti ufficiali e diritti

- [Normattiva — D.Lgs. 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legge%3A2023-03-31%3B36%21vig=): testo pubblico vigente da verificare.
- [ANAC — BDNCP](https://www.anticorruzione.it/-/banca-dati-nazionale-contratti-pubblici): portale ufficiale e dati pubblici; condizioni d'uso e profili di accesso da rispettare.
- [Normattiva — Codice civile](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262!vig=): riferimento legislativo pubblico; verificare articoli e disciplina speciale.

Non copiare testo dalle fonti: la skill sintetizza procedure originali; dati, bandi, modelli e documenti di gara restano soggetti ai diritti e ai profili di accesso dell'ente.

La skill sintetizza controlli operativi originali e non è consulenza legale, fiscale o di gara.
