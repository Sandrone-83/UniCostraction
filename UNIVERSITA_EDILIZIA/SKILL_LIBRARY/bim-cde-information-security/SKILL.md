---
name: bim-cde-information-security
description: Governa CDE, scambi informativi BIM, accessi, versioni, backup e incidenti con controllo di riservatezza e integrità senza sostituire il responsabile sicurezza o il gestore della commessa.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: gestione BIM/CDE e sicurezza informativa
---

# Gestione BIM/CDE e sicurezza informativa

## Attivazione e input

Attiva questa skill quando informazioni BIM, documenti, modelli, issue, dati di asset o deliverable devono passare tra team e fasi attraverso un Common Data Environment. È una faccetta di governance, sicurezza e continuità dell'informazione distinta da bim-ifc-openbim e ifc-ids-bcf-validation: non valida il modello tecnico, non concede accessi e non sostituisce il responsabile della sicurezza informativa o il gestore del CDE.

Prima raccogli asset e commessa, attori, requisiti informativi, contratti, classificazione, uso, stato e destinatario dei dati, CDE e aree, ruoli, identità, MFA, federazione, retention, backup, recovery, interfacce, fornitori e obblighi privacy/cyber. Registra owner, custodian, autorità, versione ISO/contrattuale, RTO/RPO e criterio di accettazione. Se dati, ruoli o confini sono ignoti, lo stato è blocked.

## Workflow

1. **Gate dell'informazione:** inventaria modelli, documenti, issue, attributi, revisioni e link; assegna owner, classificazione, fase, scopo, destinatari e durata.
2. **Gate dell'ambiente:** separa work in progress, condiviso, pubblicato e archivio; congela convenzioni, naming, status code, revision, transmittal e regole di approvazione.
3. **Gate dell'identità:** applica minimo privilegio, ruoli, separazione dei compiti, MFA, account di servizio, scadenza e revisione accessi; non usare link pubblici o credenziali condivise per comodità.
4. **Gate dello scambio:** verifica destinatario, formato, versione, integrità, metadati, virus/macro, dati personali, licenza e autorizzazione prima di ogni transmittal; registra hash e ricevuta.
5. **Gate della continuità:** definisci backup, immutabilità, restore test, RTO/RPO, dipendenze, export leggibile e piano per indisponibilità del CDE. Un backup mai ripristinato non dimostra continuità.
6. **Gate dell'incidente:** rileva accesso anomalo, perdita, modifica, ransomware o invio errato; preserva log, limita propagazione, notifica ai ruoli competenti e non cancellare evidenza.
7. **Gate del rilascio:** riconcilia requisiti, modello/documento, approvatori, destinatari, diritti, archiviazione e revoca; separa pubblicazione informativa da approvazione progettuale.

## Output

Consegna un cde_information_security_record con inventario, classificazione, ruoli, matrice accessi, stato delle aree, transmittal, hash, backup/restore, incidenti, retention, issue e stato controlled, conditional o blocked. Ogni rilascio conserva chi, cosa, quando, perché, versione, destinatario e autorizzazione.

## Quality gates

- Asset informativi, owner, classificazione, destinatari e scopo sono identificati.
- Aree CDE, status/revisioni, approvazioni e transmittal sono distinguibili e auditabili.
- Accessi, account, MFA, privilegi, scadenze e segregazione sono verificati.
- Integrità, malware, privacy, licenze, backup e restore test sono documentati.
- Incidenti e invii errati hanno piano di contenimento, log, responsabile e obblighi di notifica da verificare.
- Nessun controllo CDE viene presentato come certificazione ISO, conformità cyber o approvazione tecnica del modello.

## Evidenza e provenienza

Conserva EIR/air, matrici ruoli, registro asset, log, hash, transmittal, approvazioni, configurazione CDE, versioni software, backup, restore test, incident report e revisioni. Marca fonte, trasformazione, approvatore e diritto d'uso. Dati personali, segreti, chiavi, planimetrie sensibili e log sono minimizzati e accessibili per ruolo; non inserire password nei report.

## Fonti ufficiali e diritti

- [ISO 19650](https://www.iso.org/standard/68078.html): riferimento ufficiale per gestione dell'informazione nel ciclo di vita di edifici e opere civili.
- [ISO/IEC 27001:2022](https://www.iso.org/standard/27001?archive=all): requisiti ufficiali per sistema di gestione della sicurezza delle informazioni.
- [Direttiva NIS2 su EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2555/oj): quadro europeo di sicurezza delle reti e dei sistemi informativi, da verificare per soggetto e recepimento.

Norme ISO, contratti, manuali CDE e schemi di sicurezza sono restricted o soggetti a licenza: si citano identificativi e scopo senza copiare clausole. Matrici, gate, registri e procedure sono originali. Stato diritti: official_reference_only_no_text_reproduced.

## Confini professionali e legali

La skill non approva sistemi di sicurezza, non esegue incident response forense, non determina obblighi privacy o NIS2 nel caso concreto, non concede accessi, non firma EIR/BE P e non sostituisce CISO, DPO, responsabile CDE, owner, legale o autorità. Un hash o un log prova integrità/attività limitata, non verità del contenuto o conformità generale.

## Failure modes

- **Link pubblico a modello sensibile:** revoca, preserva log e avvia contenimento con il responsabile.
- **Versione pubblicata sovrascritta:** congela revisioni, recupera audit trail e ristabilisci approvatore.
- **Backup senza restore:** esegui test isolato e registra RTO/RPO e perdita accettabile.
- **Account di servizio condiviso:** sospendi uso, ruota credenziali e assegna identità tracciabili.
- **CDE sicuro ma licenza assente:** blocca transmittal e verifica diritto di copia, export e destinatario.
- **Log cancellati dopo incidente:** preserva evidenze e instrada a incident response e obblighi da verificare.

## Strumenti

Usa CDE con versioning e audit log, IAM/MFA, classificazione, checksum, scanner, backup immutabile, restore sandbox, registro transmittal e issue tracker. Automatizza access review, scadenze, hash e completezza; non automatizzare concessione privilegi, dichiarazioni di conformità o notifica legale.
