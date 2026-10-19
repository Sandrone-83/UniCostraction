---
name: energy-certification-ape-technical-report
description: "Gestione controllata del fascicolo energetico per APE e relazione tecnica di progetto, dalla raccolta degli input alla consegna al certificatore e al registro regionale."
metadata:
  library: "UNIVERSITA_EDILIZIA/SKILL_LIBRARY"
  version: "G31.1"
  domain: "certificazione energetica, APE e relazione tecnica"
---

# Certificazione energetica, APE e relazione tecnica

Questa skill governa il passaggio da dati edilizi e impiantistici verificabili a un fascicolo pronto per il soggetto competente che calcola, firma e deposita l'Attestato di Prestazione Energetica (APE) o la relazione tecnica richiesta dal procedimento. E' una skill di controllo del fascicolo e del modello, non un servizio di certificazione automatica.

## Attivazione e input

Attivare la skill quando il caso riguarda un APE per vendita, locazione, nuova costruzione o ristrutturazione, una relazione energetica di progetto, la registrazione regionale o la verifica di coerenza tra APE e stato dell'immobile. Richiedere almeno:

- identificativo dell'edificio o dell'unita, indirizzo, dati catastali disponibili, destinazione d'uso, zona climatica e data di riferimento;
- elaborati approvati e as-built, superfici e volumi, stratigrafie, serramenti, ponti termici assunti e fonti delle geometrie;
- schede e libretti degli impianti, generatori, distribuzione, regolazione, ventilazione, rinnovabili e acqua calda sanitaria;
- stato dei lavori, eventuali varianti, manutenzioni, rilievi fotografici e dichiarazioni del proprietario o del direttore dei lavori;
- regione o provincia autonoma di deposito, incarico, ruolo del certificatore e software/metodo di calcolo previsto.

Se mancano identita dell'immobile, geometria utile o sistema impiantistico, lo stato deve essere `blocked`, non una classe energetica stimata.

## Workflow

1. Aprire un registro di configurazione con immobile, unita, data di sopralluogo, versione delle fonti, regione e scopo del documento. Separare sempre APE, relazione tecnica di progetto, diagnosi energetica e attestato di qualificazione.
2. Riconciliare piante, sezioni, superfici disperdenti, orientamenti, volumi climatizzati e confini dell'unita. Annotare ogni misura ricostruita, assunta o non disponibile con un codice di evidenza.
3. Inventariare involucro e impianti: per ogni elemento associare fonte, anno, stato, rendimento o trasmittanza, ipotesi sostitutiva e impatto atteso. Non trasformare una bolletta in una proprieta fisica del componente.
4. Selezionare metodo, norma tecnica, dati climatici e versione del software ammessi dal quadro nazionale e regionale applicabile. Congelare la configurazione prima del calcolo e conservare report, file nativi e interscambio.
5. Eseguire un controllo indipendente del modello: bilancio delle superfici, servizi inclusi, potenze, vettori energetici, rinnovabili, fattori di conversione, classe e raccomandazioni. Segnalare la sensibilita alle ipotesi invece di occultarla.
6. Preparare il pacchetto di consegna: bozza APE o relazione marcata come non firmata, allegati, fotografie/sopralluogo, registro input, dichiarazione di ruolo e lista dei rilievi aperti. Il certificatore abilitato decide se i dati sono sufficienti.
7. Dopo firma e deposito, registrare identificativo, data, validita, catasto regionale/SIAPE se previsto, ricevute e versione consegnata. In caso di variazione edilizia o impiantistica, riaprire il fascicolo e non riutilizzare automaticamente il vecchio APE.

## Output

Produrre un `energy_certificate_record` con:

- `status`: `screened`, `model_ready`, `ready_for_certifier`, `submitted` o `blocked`;
- identita e perimetro dell'immobile, scopo, regione, data di sopralluogo e data di calcolo;
- matrice input-evidenza con `observed`, `documented`, `assumed` o `missing`;
- metodo, software e versioni, file di calcolo/hash se disponibili, esiti dei controlli e sensitivita;
- elenco dei deliverable, ruolo del firmatario, esito deposito, numero e scadenza dell'APE quando realmente disponibile;
- rilievi aperti, decisioni del professionista e log di ogni revisione.

## Quality gates

- **Identita**: indirizzo, unita, catasto disponibile e perimetro coincidono in tutti i documenti.
- **Geometria**: superfici e volumi riconciliati con elaborati o sopralluogo; ogni assunzione e dichiarata.
- **Sistemi**: generatori, servizi, regolazione, combustibili e rinnovabili hanno fonte e stato temporale.
- **Metodo**: normativa, metodo, software, librerie e clima sono fissati e compatibili con regione e data.
- **Calcolo**: il modello chiude i controlli di coerenza e non contiene input critici `missing` non accettati dal certificatore.
- **Consegna**: documento, allegati, firma, deposito e ricevuta sono distinti; `model_ready` non equivale a APE valido.
- **Aggiornamento**: ogni modifica successiva a lavori o impianti produce una nuova revisione e rivaluta la validita.

## Evidenza e provenienza

Per ogni dato conservare titolo del documento, autore o soggetto che lo ha fornito, data, pagina/posizione, versione, hash opzionale, livello di affidabilita e trasformazioni applicate. Preferire elaborati approvati, sopralluogo documentato, schede del fabbricante, libretti e dichiarazioni firmate. Le fonti normative e le guide sono citazioni di riferimento: non copiare testi protetti e non usare un URL senza registrare data e versione consultata. Il file nativo del software resta evidenza tecnica, non prova di firma o di deposito.

## Fonti ufficiali e diritti

I contenuti della skill sono originali e sintetici: rispettare copyright, licenze, termini d'uso dei portali e diritti sugli asset; non redistribuire testi o allegati protetti.

- [D.Lgs. 192/2005 su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2005%3B192~art1): quadro nazionale della prestazione energetica; `official_public_legal_text_verify_current_consolidation`.
- [D.P.R. 75/2013 su Normattiva](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=13G00115&atto.dataPubblicazioneGazzetta=2013-06-27): qualificazione e indipendenza del certificatore; `official_public_legal_text_verify_current_consolidation`.
- [D.M. 26 giugno 2015 e linee guida APE](https://www.apecampania.enea.it/doc/dm_26062015.pdf): linee guida, format e metodi; `official_public_legal_text_verify_current_consolidation` con verifica della vigenza regionale/nazionale.
- [ENEA SIAPE](https://www.efficienzaenergetica.enea.it/servizi-per/pubblica-amministrazione/per-le-regioni/sistema-informativo-sugli-attestati-di-prestazione-energetica.html): contesto del sistema informativo; `official_reference_only_no_text_reproduced`.
- Norme UNI/CTI e manuali software sono identificati per codice ed edizione ma non riprodotti; `official_standard_paid_or_restricted_reference_only`.

I testi ufficiali sono usati come riferimenti e non vengono redistribuiti. Prima di una pratica reale verificare consolidato, regole regionali, portale e requisiti del soggetto certificatore alla data di deposito.

## Confini professionali e legali

La skill non rilascia APE, non assegna una classe con valore legale, non firma relazioni, non deposita pratiche e non sostituisce certificatore, progettista, direttore dei lavori o autorita regionale. Non determina incentivi, conformita urbanistica/catastale o convenienza economica. Una bozza o una simulazione deve essere marcata come tale; qualsiasi dichiarazione verso terzi richiede revisione e firma del professionista competente.

## Failure modes

- APE precedente riferito a unita, geometria o stato diverso: bloccare la riutilizzazione e aprire una nuova revisione.
- Relazione tecnica confusa con APE: separare scopo, momento procedurale, firmatario e allegati.
- Classe prodotta da input mancanti o da software/versione non verificata: ritornare a `blocked`.
- Scheda commerciale usata come dato certificato: richiedere scheda tecnica, dichiarazione o misura idonea.
- Firma o deposito presunti dal solo PDF: chiedere ricevuta, identificativo e portale regionale.
- Norma o procedura regionale aggiornata dopo il calcolo: congelare la versione, rivalutare e registrare il delta.

## Strumenti

Usare repository documentale con versioning, foglio di riconciliazione geometrica, checklist, calcolatore o software energetico dichiarato, viewer PDF/DWG/IFC, estrattore metadati, hashing, registro decisioni e portale regionale/SIAPE solo con utenza autorizzata. L'automazione puo preparare dati e controlli, ma non deve firmare, inviare o sovrascrivere un APE senza approvazione umana.
