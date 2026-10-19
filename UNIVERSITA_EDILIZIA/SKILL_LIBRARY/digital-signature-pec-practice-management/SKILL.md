---
name: digital-signature-pec-practice-management
description: Gestisce pacchetto documentale, firme digitali, PEC, ricevute e fascicolo per pratiche edilizie o contrattuali, senza sostituire il firmatario, il conservatore o l'ente destinatario.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: documento informatico, firme digitali e PEC
---

# Gestione documentale, firme digitali e PEC per pratiche

## Attivazione e input

Attiva questa skill quando un fascicolo tecnico o amministrativo deve essere formato, firmato, trasmesso via PEC e conservato con prova di integrità, identità, versione e ricezione. È distinta da controlled-official-document-lifecycle, che governa il ciclo generale del documento ufficiale, e da current-law-pa-source-gating, che governa la ricerca di fonti vigenti.

Raccogli procedimento e destinatario, titolare e firmatari, poteri/deleghe, scadenze, formati accettati, moduli, allegati, lingua, metadati, certificati e stato, indirizzi PEC verificati, ricevute, marca temporale se richiesta, regole di conservazione, privacy, protocollazione e canale alternativo autorizzato. Se destinatario, firma, formato o scadenza non sono verificati, lo stato è blocked.

## Workflow

1. **Gate dell'identità:** identifica pratica, soggetto, ruolo, potere di firma, destinatario e base del procedimento; separa preparatore, firmatario e trasmittente.
2. **Gate del pacchetto:** congela elenco documenti, allegati, formati, versioni, hash, dimensioni e relazioni; verifica che il PDF firmato sia quello approvato e non una copia renderizzata diversa.
3. **Gate della firma:** controlla certificato, titolare, validità, revoca/sospensione, tipo di firma, profilo e sequenza di firme; non firmare al posto dell'autore.
4. **Gate della PEC:** verifica indirizzo su fonte autorizzata, oggetto, corpo, allegati, dimensioni, delega e destinatari; esegui il controllo finale prima dell'invio.
5. **Gate della ricevuta:** conserva accettazione, consegna, errori, allegati e timestamp; distingue invio, consegna, protocollazione dell'ente e accettazione del contenuto.
6. **Gate del fascicolo:** collega pratica, documento, firma, PEC, ricevute, versione e conservazione; non sostituire un documento già trasmesso senza nuova traccia.
7. **Gate della chiusura:** registra esito, termine, richiesta integrazione e azione successiva; per errore di destinatario, allegato o firma attiva contenimento e consulenza competente.

## Output

Produci un digital_practice_record con pratica, ruoli, manifest documentale, hash/versioni, firme, PEC, ricevute, scadenze, privacy, conservazione e stato prepared, signed, sent, delivered, accepted_by_authority, conditional o blocked. La consegna non è dichiarata perfezionata solo perché il messaggio è partito.

## Quality gates

- Procedimento, destinatario, firmatari, deleghe, formato e scadenza sono verificati.
- Manifest, allegati, versioni e hash coincidono con il pacchetto sottoscritto.
- Certificato e firma sono validi per soggetto, documento, momento e uso previsto.
- Indirizzo PEC, oggetto, allegati e canale sono controllati da fonte attendibile.
- Ricevute e protocolli sono conservati senza confondere consegna con accettazione amministrativa.
- Conservazione, accessi, dati personali e copie di lavoro sono governati con policy applicabile.

## Evidenza e provenienza

Conserva documento sorgente, file firmato, manifest, hash, certificato e validazioni, deleghe, indirizzo PEC e fonte, messaggio, ricevute, protocollo, integrazioni, timestamp, log e decisioni. Marca bozza, copia di lavoro, originale informatico, copia conforme, trasmesso e conservato. Minimizza dati personali e non lasciare chiavi private o password nel fascicolo.

## Fonti ufficiali e diritti

- [AgID — documento informatico e linee guida](https://www.agid.gov.it/it/piattaforme/sistema-gestione-procedimenti-amministrativi/documento-informatico): CAD, documento informatico, formati e gestione/conservazione.
- [AgID — elenco gestori PEC](https://www.agid.gov.it/en/piattaforme/posta-elettronica-certificata/elenco-gestori-pec): verifica del circuito e dei gestori.
- [Normattiva — D.Lgs. 82/2005 CAD](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2005-03-07%3B82): documento informatico, firma e procedimenti digitali.
- [EUR-Lex — eIDAS, Regolamento UE 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj): identificazione elettronica e servizi fiduciari.

Manifest, controlli, record e procedure sono originali. Diritti: official_reference_only_no_text_reproduced; CAD, eIDAS, linee guida AgID, moduli dell'ente, certificati e sistemi PEC conservano diritti e condizioni proprie.

## Confini professionali e legali

La skill non firma, non dichiara conformità, non presenta pratiche a nome di terzi, non attribuisce poteri, non certifica copie, non conserva con valore legale autonomo e non decide se un atto sia tempestivo o ricevibile. Non sostituisce firmatario, responsabile del procedimento, professionista, conservatore accreditato, legale, ente o gestore PEC.

## Failure modes

- **Firmatario errato:** blocca e verifica identità, delega e potere.
- **Firma scaduta/revocata:** non trasmettere; sostituire solo tramite firmatario autorizzato.
- **PEC partita ma non consegnata:** conserva errore e attiva canale previsto, senza dichiarare adempimento.
- **Allegato diverso dalla versione firmata:** congela il fascicolo e ricostruisci hash e nuova trasmissione autorizzata.
- **Ricevuta confusa con protocollo:** separa eventi e attendi evidenza dell'ente.
- **Password o chiave nel fascicolo:** revoca accesso, elimina la copia esposta secondo procedura e segnala incidente.

## Strumenti

Usa document manifest, hash/checksum, validatore firme, certificati pubblici, PEC client, ricevute, timestamp register, protocol/filing log, conservazione autorizzata e deadline tracker. Automatizza completezza, hash e reminder; non inviare, firmare o alterare documenti in autonomia.
