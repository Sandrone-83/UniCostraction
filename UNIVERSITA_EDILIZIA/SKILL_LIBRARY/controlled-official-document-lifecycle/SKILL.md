---
name: controlled-official-document-lifecycle
description: Genera PDF e documenti ufficiali da dati approvati con versioni, firme, accessi, conversioni e ritiro controllati; non attribuisce autenticità o efficacia senza il titolare competente.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: generazione PDF e lifecycle documentale
---

# Generazione PDF e lifecycle controllato del documento ufficiale

## Attivazione e input

Attiva questa skill per produrre fascicoli, verbali, report, capitolati, atti interni, allegati tecnici o PDF/A da dati e template approvati. È distinta da `documents-pdf-computo-sal-due-diligence`: qui il focus è il ciclo di vita dell'output, non l'estrazione o la due diligence.

Prima raccogli tipo di documento, titolare/autore, destinatario, giurisdizione, modello dati, template e versione, lingua, classificazione, metadati obbligatori, numerazione, approvatori, firma elettronica richiesta, scadenza/ritiro, formato, accessibilità, canale di pubblicazione e diritti su font/logo/allegati. Se manca il proprietario dell'approvazione, prepara una bozza marcata e non un documento ufficiale.

## Workflow

1. Congela un `document_spec` con schema, fonti approvate, template hash, versione, ruoli, data di riferimento e regole di numerazione.
2. Acquisisci dati in sola lettura e crea una matrice campo -> fonte -> trasformazione -> responsabile; ogni valore mancante resta placeholder esplicito.
3. Genera un artefatto intermedio verificabile e poi PDF/PDF-A secondo il requisito. Non usare il PDF come database né convertire un file firmato per correggerne il contenuto.
4. Esegui controlli di contenuto e forma: pagine, intestazioni/piè di pagina, numerazione, allegati, link, font incorporati, metadati, accessibilità, testo estraibile e rendering di pagine campione.
5. Applica il gate di approvazione: revisore tecnico, titolare del documento, firma/sigillo se richiesti, data e canale. La generazione automatica non equivale a firma o protocollazione.
6. Pubblica solo la revisione approvata in repository con permessi e audit; assegna stato `draft/review/approved/published/superseded/withdrawn`.
7. Per una correzione crea nuova revisione collegata, conserva l'originale e registra motivo, autorizzatore, effetto sui destinatari e ritiro/avviso della precedente.

## Output

Consegna specifica, input manifest, template e versioni, sorgente editabile quando autorizzato, PDF/PDF-A, report di validazione, hash, registro approvazioni/firma, log pubblicazione, lista destinatari e stato di conservazione/ritiro. Se è una bozza, il watermark e il nome file devono renderlo evidente.

## Quality gates

- I dati critici hanno fonte, data e responsabile; nessun placeholder arriva in `approved` senza decisione.
- Il PDF si apre in viewer indipendente, mantiene pagine/allegati e non perde firme o metadati dichiarati.
- La revisione, la data di efficacia e il documento superseded sono collegati.
- Firma, marca temporale, protocollo e pubblicazione sono separati dalla mera esportazione.
- La conservazione e l'accesso sono proporzionati a dati personali, riservati e professionali.
- Il controllo di leggibilità include una pagina con tabelle, allegati e link quando presenti.

## Evidenza e provenienza

Conserva hash di dati, template, sorgente e output; versione del generatore, font, librerie, configurazione, log, timestamp, ruoli, approvazioni e destinatari. Registra ogni trasformazione, inclusi OCR, flattening, conversione PDF/A, redazione e firma. Per una copia pubblicata salva URL/canale e prova di pubblicazione senza confonderla con autenticità giuridica.

## Confini professionali e legali

Un PDF ben formato non dimostra veridicità, autenticità, validità amministrativa, firma, conformità o conservazione a norma. Non firmare, protocollare, inviare, pubblicare o ritirare senza autorizzazione esplicita del ruolo competente. Non rimuovere protezioni, firme, metadati o filigrane di terzi. Verifica diritti su contenuti, font, loghi e allegati.

## Failure modes

- **Template vecchio:** blocca la pubblicazione e identifica la revisione approvata.
- **Fonte cambiata durante la generazione:** congela gli input e rigenera con nuovo manifest.
- **Firma invalidata da conversione:** conserva l'originale firmato e non sostituirlo con un PDF "riparato".
- **Numero documento duplicato:** invalida la bozza, assegna un nuovo numero tramite il titolare e conserva l'evento.
- **PDF visivo corretto ma testo/OCR errato:** confronta contenuto e rendering; segnala la pagina critica.
- **Pubblicazione senza ritiro del precedente:** tratta il rischio come incidente di lifecycle e registra destinatari/azioni.

## Strumenti

Usa generatori documentali tracciati, parser PDF, validatori PDF/A, viewer indipendente, strumenti di firma e repository con audit. Riferimenti ufficiali da verificare per edizione e applicabilità:

- [ISO — PDF 2.0 (ISO 32000-2)](https://www.iso.org/standard/75839.html): specifica del formato, accesso/licenza propri.
- [ISO — PDF/A (ISO 19005-1)](https://www.iso.org/standard/38920.html): riferimento per conservazione, non testo da copiare.
- [AgID — linee guida](https://www.agid.gov.it/it/linee-guida): quadro istituzionale italiano da verificare per il tipo di documento e il periodo.
- [Normattiva — Codice dell'amministrazione digitale](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-03-07;82!vig=): testo vigente da controllare per firma, documento e procedimento.

## Fonti ufficiali e diritti

AgID e Normattiva: https://www.agid.gov.it/it/linee-guida

ISO è riferimento ufficiale a pagamento/restricted; Normattiva e AgID sono fonti istituzionali da usare senza assumere che ogni logo, template o allegato sia riutilizzabile. La procedura di lifecycle è originale e non conferisce valore legale all'output.
