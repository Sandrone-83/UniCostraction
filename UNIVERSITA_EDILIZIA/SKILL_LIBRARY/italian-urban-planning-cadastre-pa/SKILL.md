---
name: italian-urban-planning-cadastre-pa
description: Ricostruisce stato urbanistico-catastale, vincoli e procedimenti della pubblica amministrazione italiana usando fonti tracciate e verifica presso l'ente competente.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: urbanistica e catasto
---

# Urbanistica, catasto e pubblica amministrazione italiana

## Attivazione e input

Usa la skill per titoli edilizi, stato legittimo, visure, planimetrie, mappe, particelle, vincoli, SUE/SUAP, accesso agli atti e fascicoli immobiliari. Richiedi comune, indirizzo, foglio/particella/subalterno se disponibili, titolo di disponibilità, delega, periodo storico, documenti e domanda precisa.

## Workflow

1. Identifica immobile, soggetto richiedente, delega e finalità; limita i dati personali.
2. Ricostruisci la catena delle fonti: titolo, varianti, agibilità, elaborati, catasto, strumenti urbanistici e vincoli.
3. Separa stato catastale, stato urbanistico-edilizio, stato di fatto e stato autorizzato: non sono sinonimi.
4. Verifica date, intestazioni, superfici, destinazioni, sagoma, consistenza e collegamenti tra elaborati.
5. Individua l'ufficio competente e la procedura possibile; prepara elenco documenti e quesiti, non una falsa certezza sull'esito.
6. Registra richieste protocollate, ricevute, risposte, termini e documenti mancanti.
7. Produci quadro delle evidenze, difformità apparenti, ipotesi e verifiche necessarie; sottoponi a tecnico o legale quando il caso lo richiede.

## Output

Consegna timeline atti, matrice urbanistica/catastale, indice fascicolo, tavola di confronto se autorizzata, registro vincoli, lista richieste a SUE/SUAP/Agenzia Entrate, stato di verifica e domande per il professionista.

## Quality gates

- La ricerca è legata a un identificativo e a una data, non solo a un indirizzo.
- Ogni affermazione distingue documento originale, copia, dichiarazione e inferenza.
- Una visura non è usata come prova esclusiva della legittimità edilizia.
- Le norme regionali e comunali sono controllate per territorio e periodo.
- Le richieste amministrative sono inviate solo da soggetto autorizzato e nel canale corretto.

## Evidenza e provenienza

Conserva ricevute, protocolli, URL, data di accesso, versione degli strumenti urbanistici, copie ottenute e hash. Annota eventuali portali autenticati e non rendere pubblici credenziali, deleghe o dati eccedenti.

## Confini professionali e legali

La skill non rilascia conformità, stato legittimo, sanatoria, agibilità, certificazione catastale o parere amministrativo. Gli esiti dipendono da comune, regione, uffici, titoli, norme vigenti e responsabilità del tecnico. Non presentare istanze o accessi agli atti senza autorizzazione.

## Failure modes

- **Catasto usato come urbanistica:** separa i registri e indica la fonte mancante.
- **Norma corrente applicata al passato:** ricostruisci vigenza alla data dell'intervento.
- **Portale non accessibile:** registra tentativo e chiedi canale ufficiale; non usare copia non verificata.
- **Subalterno ambiguo:** sospendi l'abbinamento e richiedi documento identificativo.
- **Vincolo dedotto dalla mappa:** verifica atto, perimetro e autorità competente.

## Strumenti

Usa portali istituzionali, viewer cartografico, OCR/PDF, GIS/CAD per overlay documentati e registro di protocollo. Gli overlay visualizzano ipotesi e non sostituiscono il rilievo o l'atto amministrativo.

## Fonti ufficiali e diritti

- [Normattiva — DPR 380/2001](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=0&atto.codiceRedazionale=001G0429&atto.dataPubblicazioneGazzetta=2001-10-20): testo pubblico; verificare consolidato e norme regionali/comunali.
- [Normattiva — DPR 160/2010](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2010-09-07;160): SUAP; verificare procedura e portale competente.
- [Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/): portale ufficiale; servizi, dati e manuali hanno condizioni proprie.

Non è stato copiato testo dalle fonti: la skill usa solo riferimenti ufficiali e richiede verifica della licenza o dei termini di accesso per ogni documento o dato ottenuto.

La skill è una procedura di ricerca e controllo documentale; non produce un titolo o una certificazione.
