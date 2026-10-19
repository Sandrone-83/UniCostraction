---
name: construction-site-privacy-personal-data
description: Governa minimizzazione, ruoli, informative, accessi e conservazione dei dati personali raccolti in cantiere, senza sostituire DPO, garante, datore di lavoro o valutazione giuridica.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: privacy e dati personali in cantiere
---

# Privacy e dati personali in cantiere

## Attivazione e input

Attiva questa skill quando cantiere, CDE, app, badge, GPS, drone, foto, videosorveglianza, biometrici, report incidenti, registri formazione o sistemi IoT raccolgono dati riferibili a lavoratori, visitatori, conducenti o terzi. È distinta da bim-cde-information-security, che tratta sicurezza informativa e governance del CDE, e da construction-site-safety, che tratta il rischio HSE.

Raccogli finalità, titolare/responsabile, categorie e soggetti, base giuridica, necessità, proporzionalità, informative, tempi, accessi, destinatari, trasferimenti, DPIA/assessment, diritti, sicurezza, contratto con fornitore, retention, immagini/audio, geolocalizzazione, dati sanitari e canali di incidente. Se finalità, ruolo, base o retention non sono definiti, lo stato è blocked.

## Workflow

1. **Gate della finalità:** descrivi lo scopo concreto e separa sicurezza, accesso, produttività, prova lavori, formazione, videosorveglianza e marketing; vieta riuso incompatibile.
2. **Gate del dato:** minimizza campi, frequenza, precisione, immagini e durata; separa dato personale, anonimizzato, pseudonimizzato, tecnico e sanitario.
3. **Gate dei ruoli:** identifica titolare, responsabile, autorizzati, contitolari, fornitori e destinatari; collega ogni flusso a istruzioni e accordi.
4. **Gate dell'informazione:** prepara informative comprensibili, segnaletica, canali di richiesta e registro trattamenti; non usare consenso come rimedio automatico nel rapporto di lavoro.
5. **Gate della sicurezza:** applica minimo privilegio, segregazione, cifratura, log, backup, masking e gestione dispositivi; separa telemetria e identità.
6. **Gate della retention:** fissa cancellazione o anonimizzazione per finalità e obbligo, legal hold autorizzato, accesso alle immagini e gestione delle copie.
7. **Gate dell'incidente:** registra perdita, accesso, invio errato o ripresa impropria, limita diffusione e instrada valutazione e notifica al titolare/DPO secondo procedura.

## Output

Produci un site_privacy_record con trattamento, finalità, dati, ruoli, base, informativa, accessi, retention, misure, DPIA/assessment, diritti, incidenti e stato mapped, conditional, approved_by_privacy_owner o blocked. Non includere dati personali non necessari nel report tecnico.

## Quality gates

- Finalità, base giuridica, titolare/responsabile e categorie di dati sono documentati.
- Raccolta e precisione sono proporzionate; dati sanitari, biometrici e immagini hanno gate dedicati.
- Informative, segnaletica, autorizzazioni, accordi fornitore e trasferimenti sono verificati.
- Accessi, log, copie, retention e cancellazione sono testati e assegnati.
- DPIA o valutazione di impatto è eseguita quando richiesta; il rischio non è dichiarato basso senza analisi.
- Incidenti e richieste degli interessati hanno canale, tempi e owner; nessuna divulgazione automatica.

## Evidenza e provenienza

Conserva registro trattamenti, data map, informative, cartelli, contratti, autorizzazioni, DPIA, access matrix, retention schedule, log accessi, backup/restore, vendor assessment, richieste e incident records. Marca dati grezzi, derivati, anonimizzati e pubblicati. Minimizza immagini, volti, targhe, coordinate, badge e dati sanitari e limita l'accesso per ruolo.

## Fonti ufficiali e diritti

- [EUR-Lex — GDPR, Regolamento UE 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj): principi, basi, diritti e responsabilità.
- [Garante Privacy — videosorveglianza e lavoro](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10226611): provvedimenti e indicazioni istituzionali per immagini e lavoratori.
- [Normattiva — D.Lgs. 196/2003](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-06-30;196!vig=): Codice privacy e modifiche, da verificare alla data.
- [EDPB — linee guida](https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en): indirizzi europei ufficiali, da selezionare per trattamento e giurisdizione.

Mappe dei flussi, checklist e record sono originali. Diritti: official_reference_only_no_text_reproduced; GDPR, Codice privacy, provvedimenti, immagini, sistemi e policy del titolare mantengono diritti, riservatezza e condizioni d'uso.

## Confini professionali e legali

La skill non determina la base giuridica definitiva, non approva videosorveglianza, biometria, GPS, controllo a distanza o trasferimenti, non svolge DPIA come consulenza legale e non sostituisce titolare, DPO, consulente privacy, datore di lavoro, sindacato, Garante o autorità. Non raccoglie dati sanitari o biometrici oltre un incarico autorizzato.

## Failure modes

- **Fotografie pubblicate con volti/targhe:** blocca condivisione, limita accessi e applica masking/cancellazione secondo titolare.
- **GPS usato per produttività senza base:** sospendi trattamento e riapri finalità, proporzionalità e consultazione.
- **Dati sanitari nel report:** rimuovi, separa e instrada a medico competente/titolare.
- **Fornitore cloud non mappato:** blocca trasferimento e verifica ruolo, contratto, localizzazione e sub-responsabili.
- **Retention infinita:** definisci scadenza, legal hold e cancellazione verificabile.
- **Incidente minimizzato:** preserva log, contenimento e valutazione tempestiva da parte del titolare/DPO.

## Strumenti

Usa data map, processing register, privacy-by-design checklist, DPIA tracker, access matrix, retention/deletion register, image/GPS register, vendor assessment, incident log e rights-request tracker. Automatizza reminder e anonimizzazione controllata; non pubblicare, sorvegliare o decidere notifiche in autonomia.
