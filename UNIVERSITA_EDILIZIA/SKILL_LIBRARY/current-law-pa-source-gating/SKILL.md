---
name: current-law-pa-source-gating
description: Ricerca fonti normative e amministrative correnti applicando giurisdizione, efficacia, versione, data e gerarchia della fonte; non produce pareri o citazioni definitive senza verifica competente.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: fonti normative correnti e pubblica amministrazione
---

# Lookup di legge vigente e fonti della pubblica amministrazione

## Attivazione e input

Attiva questa skill quando una risposta dipende da legge, regolamento, atto amministrativo, bando, prassi o fonte PA che può cambiare. È una faccetta di ricerca e gating distinta da `italian-urban-planning-cadastre-pa` e `contracts-compliance-legal-drafting`: non interpreta definitivamente il caso e non scrive o deposita atti.

Prima raccogli domanda precisa, materia, Stato/Regione/Provincia/Comune o ente, settore e destinatario, data dell'evento e data alla quale serve la regola, procedimento, ruolo dell'utente, versione già citata, livello di urgenza e output autorizzato. Se la giurisdizione, il territorio o la data di efficacia non sono noti, lo stato deve essere `blocked`.

## Workflow

1. **Gate di giurisdizione:** separa UE, Stato, Regione, ente locale, autorità indipendente e fonte interna; non usare un atto nazionale per colmare una competenza locale.
2. **Gate di identificazione:** registra tipo, numero, data, titolo, articolo/allegato, ELI/CELEX/URL, autorità emanante e atto modificatore; cerca anche la fonte originaria quando serve.
3. **Gate temporale:** fissa `data_evento`, `data_consultazione`, `data_entrata_in_vigore`, `data_efficacia` e, se rilevante, la disciplina transitoria. Non chiamare "vigente" un testo solo perché il risultato di ricerca è recente.
4. **Gate di versione:** confronta testo vigente/consolidato e pubblicazione ufficiale; registra modifiche, abrogazioni, rinvii, sospensioni e regime transitorio. Per un atto PA controlla versione del modulo, pagina ufficiale e data di ultimo aggiornamento.
5. **Gate di autorità:** classifica fonte primaria, regolamento/atto applicativo, linee guida, FAQ, prassi, sentenza o commento. Usa FAQ e blog per orientare la ricerca, mai come unica base per un obbligo.
6. **Gate di applicabilità:** collega norma e fatto solo come ipotesi verificabile; segnala definizioni, eccezioni, soggetti, territorio, soglie, termini e autorizzazioni mancanti.
7. **Gate di consegna:** restituisci tabella fonte/versione/evidenza/confidenza, estratto minimo consentito o parafrasi, domande aperte, data di scadenza della ricerca e necessità di revisione professionale. Blocca parere, firma, deposito o comunicazione automatica.

## Output

Consegna una scheda di ricerca con quesito, giurisdizione, cronologia, gerarchia, registro URL/ELI/CELEX, data e versione consultate, modifiche rilevanti, stato `verified/current_as_of/date/blocked`, evidenze e limiti. Se la fonte è non accessibile o non consolidata, dichiaralo e non ricostruire il testo da memoria.

## Quality gates

- Ogni conclusione ha almeno una fonte ufficiale e un riferimento preciso all'atto/articolo/pagina o identificativo.
- La data "oggi" è sostituita da data e fuso registrati; l'efficacia è distinta dalla pubblicazione.
- La fonte regionale/comunale prevale solo nel proprio ambito e non viene confusa con la norma statale.
- Versione, modifiche e transitorio sono controllati prima di usare parole come `vigente`, `obbligatorio` o `scaduto`.
- Un URL istituzionale senza contenuto, atto identificato o data non è evidenza sufficiente.
- La risposta distingue testo ufficiale, interpretazione, ipotesi e indicazione prudenziale al professionista/ente.

## Evidenza e provenienza

Salva URL canonico, identificativo atto, autorità, data di pubblicazione/accesso, versione o consolidamento, pagina/articolo, hash del download quando possibile, query usata e screenshot solo come supporto. Registra l'atto modificatore e la ragione per cui una fonte è stata preferita. Non archiviare copie di testi oltre i diritti e le policy applicabili.

## Confini professionali e legali

La ricerca non è parere legale, interpretazione autentica, attestazione urbanistica, consulenza amministrativa o sostituzione dell'ufficio competente. Non inventare articoli, termini, sanzioni o prassi; non compilare, firmare, inviare o depositare moduli senza autorizzazione. Rispetta copyright, termini dei portali, dati personali e licenze; il testo normativo e il commento possono avere regimi diversi.

## Failure modes

- **Atto vigente confuso con atto originario:** affianca pubblicazione e testo multivigente, marcando entrambe.
- **Regione/comune errati:** blocca e richiedi territorio, ente e procedimento.
- **Modifica futura o transitorio ignorati:** riapri il gate temporale e indica la data di efficacia.
- **FAQ usata come legge:** retrocedi la fonte a orientativa e cerca atto primario.
- **URL cambiato o pagina non autenticata:** cerca l'archivio ufficiale e registra il nuovo identificativo.
- **Richiesta di "certezza" su fatti incompleti:** consegna una matrice di verifica, non una conclusione assoluta.

## Strumenti

Usa ricerca avanzata, identificativi ELI/CELEX, archivi ufficiali, download con hash e un registro versioni. Per l'Italia e l'UE parti da:

- [Normattiva](https://www.normattiva.it/): banca dati della legislazione vigente e multivigente; controllare data, consolidamento e territorio.
- [Gazzetta Ufficiale](https://www.gazzettaufficiale.it/): pubblicazione ufficiale e testo originario degli atti italiani; verificare la nota di autenticità del formato elettronico.
- [EUR-Lex](https://eur-lex.europa.eu/homepage.html?locale=it): atti UE, testi consolidati, CELEX e Gazzetta UE.
- [ANAC](https://www.anticorruzione.it/): atti e dati istituzionali per contratti pubblici; verificare ambito e aggiornamento.
- [AgID — linee guida](https://www.agid.gov.it/it/linee-guida): linee guida e indirizzi PA, da distinguere dagli atti normativi.

## Fonti ufficiali e diritti

Normattiva e Gazzetta Ufficiale: https://www.normattiva.it/

Normattiva, Gazzetta Ufficiale, EUR-Lex, ANAC e AgID sono riferimenti istituzionali: si usano per ricerca e citazione responsabile, non come licenza generale di ripubblicazione. Le norme ISO, quando consultate, sono riferimenti ufficiali a pagamento/restricted. Il protocollo a cancelli e il registro delle evidenze sono originali; la verifica professionale resta obbligatoria per l'uso decisionale.
