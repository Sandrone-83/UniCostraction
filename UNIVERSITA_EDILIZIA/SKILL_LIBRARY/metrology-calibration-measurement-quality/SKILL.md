---
name: metrology-calibration-measurement-quality
description: Governa idoneità, calibrazione, tracciabilità, incertezza e uso dei risultati di misura in costruzione, senza sostituire laboratorio, organismo di accreditamento o giudizio tecnico.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: metrologia, calibrazione e qualità delle misure
---

# Metrologia, calibrazione e qualità delle misure

## Attivazione e input

Attiva questa skill quando una decisione di qualità, sicurezza, SAL, collaudo, monitoraggio o accettazione dipende da misure e serve dimostrarne idoneità allo scopo. È distinta da construction-quality-itp-nonconformity, che governa ITP e NCR, e da mep-testing-commissioning, che governa la sequenza dei test MEP.

Raccogli measurand e requisito, range e tolleranza, strumento e seriale, risoluzione, classe, software/firmware, ambiente, operatore, metodo, taratura, riferibilità, incertezza, data e condizioni d'uso, laboratorio, campioni, regole di decisione, risultati precedenti e impatto su lavori già rilasciati. Se grandezza, uso previsto o criterio di accettazione non sono definiti, lo stato è blocked.

## Workflow

1. **Gate della misura:** definisci grandezza, unità, punto, metodo, range, frequenza e decisione che il risultato deve supportare; separa misura, osservazione e stima.
2. **Gate dell'attrezzatura:** verifica identità, stato, campo, risoluzione, compatibilità ambientale, firmware e idoneità allo scopo prima dell'impiego.
3. **Gate della conferma metrologica:** valuta calibrazione o verifica, riferibilità, incertezza, errore massimo, regolazione, sigillo, etichetta e data di scadenza; non confondere calibrazione con conformità del prodotto.
4. **Gate del metodo:** congela istruzioni, preparazione, punti, campionamento, ripetizioni, operatore, condizioni e regola di decisione; controlla bias, drift, deriva e outlier.
5. **Gate dell'acquisizione:** registra raw data, timestamp, unità, ambiente, strumento, operatore e anomalie; conserva dati non modificabili prima di trasformazioni o arrotondamenti.
6. **Gate dell'interpretazione:** calcola o riporta incertezza, confronta con requisito e regola dichiarata, separa pass/fail dal valore e analizza l'impatto di strumenti fuori tolleranza.
7. **Gate della revisione:** ritira, correggi o rivaluta risultati potenzialmente influenzati; approva ripresa, accettazione condizionata o NCR con owner e audit trail.

## Output

Produci un measurement_quality_record con measurand, requisito, strumento, metodo, taratura, riferibilità, raw/processed data, incertezza, regola di decisione, risultato, impatto e stato fit_for_purpose, conditional o blocked. Collega ogni strumento a un uso, non solo a una data di calibrazione.

## Quality gates

- Measurand, unità, tolleranza, metodo e intended use sono espliciti.
- Strumento, seriale, range, risoluzione, ambiente, operatore e firmware sono tracciati.
- Certificato o rapporto contiene riferibilità, risultati, incertezza, condizioni e scope pertinenti.
- La calibrazione è valida per l'uso e non viene usata come prova automatica della conformità del manufatto.
- Raw data, trasformazioni, arrotondamenti, outlier e regola di decisione sono riproducibili.
- Un fuori-taratura produce impact assessment su misure precedenti e comunicazione ai responsabili.

## Evidenza e provenienza

Conserva requisiti, metodi, inventario strumenti, certificati, rapporti laboratorio, riferibilità, uncertainty budget, check pre/post uso, raw data, ambientali, operatori, software, foto, revisioni e decision log. Marca misurato, calcolato, interpolato, dichiarato e approvato. Mantieni versioni e privacy per dati di persone o luoghi sensibili.

## Fonti ufficiali e diritti

- [ISO 10012:2026](https://www.iso.org/standard/10012): sistema di gestione della misura e affidabilità dei risultati, edizione corrente da verificare.
- [ISO/IEC 17025 — pagina ISO](https://www.iso.org/standard/66912.html): competenza e imparzialità dei laboratori di prova e taratura.
- [BIPM — International Vocabulary of Metrology](https://www.bipm.org/en/committees/jc/jcgm/wg2): terminologia metrologica istituzionale.
- [Accredia](https://www.accredia.it/): accreditamento italiano e banche dati dei soggetti, da verificare per scope e validità.

La procedura, i record e le regole di gate sono originali. Diritti: official_reference_only_no_text_reproduced; ISO, VIM, certificati e rapporti di laboratorio sono soggetti ai diritti dei titolari. La presenza di un certificato non autorizza la redistribuzione del suo contenuto o del marchio.

## Confini professionali e legali

La skill non emette certificati, non accredita laboratori, non determina da sola la conformità di un'opera, non firma collaudi e non sostituisce metrologo, laboratorio, direttore lavori, collaudatore, organismo di accreditamento o autorità. L'incertezza non può essere rimossa con arrotondamento e una misura valida non sana un metodo o un requisito errato.

## Failure modes

- **Calibrazione valida ma strumento fuori range:** blocca il risultato e rivaluta l'idoneità d'uso.
- **Certificato senza scope o riferibilità:** tratta l'evidenza come insufficiente e chiede chiarimento.
- **Unità o conversione errata:** conserva raw data, correggi la trasformazione e ripeti il gate.
- **Media che nasconde variabilità:** riporta ripetizioni, dispersione, picchi e condizioni.
- **Fuori-taratura scoperto tardi:** delimita il periodo, identifica decisioni impattate e apre NCR.
- **Pass/fail senza regola:** separa valore, incertezza, tolleranza e autorizzazione decisionale.

## Strumenti

Usa metrology register, calibration schedule, certificate parser, method sheet, uncertainty workbook, raw-data repository, environmental log, decision-rule matrix e NCR/impact tracker. Automatizza scadenze, identificativi, unità e controlli di completezza; non certificare, alterare raw data o chiudere un impatto senza riesame competente.
