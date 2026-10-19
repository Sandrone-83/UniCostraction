---
name: building-energy-decarbonization
description: Costruisce baseline, roadmap e verifica operativa di efficienza e decarbonizzazione degli edifici separando energia misurata, risparmio previsto, emissioni e conformità.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: energia e decarbonizzazione degli edifici
---

# Energia e decarbonizzazione degli edifici

## Attivazione e input

Attiva questa skill quando un edificio o portafoglio deve misurare consumi, definire interventi, integrare rinnovabili, elettrificare carichi o verificare riduzione energetica ed emissiva. È una faccetta di baseline, misura, scenario e gestione del cambiamento distinta da mep-energy-systems, environmental-resilience-lca-diagnostics e construction-business-operations: non progetta impianti, non rilascia APE, non garantisce carbon neutrality.

Prima raccogli confini dell'edificio, uso e occupazione, clima, involucro, impianti, vettori, contatori, tariffe, dati orari, comfort, manutenzione, autorizzazioni, fattori emissivi, anno base, obiettivo, orizzonte, costi e vincoli. Registra qualità, periodo, normalizzazione climatica e responsabile. Se contatori, confini, uso o anno base sono incerti, lo stato è blocked.

## Workflow

1. **Gate del perimetro:** separa edificio, utenze comuni, locatari, generazione in sito, mobilità e processi; assegna contatori, responsabili e confini energetici/emissivi.
2. **Gate della baseline:** riconcilia bollette, contatori, letture, BMS, clima, occupazione e orari; misura buchi, stime, cambi tariffari e anomalie prima di calcolare indicatori.
3. **Gate della prestazione:** costruisci mappa end-use di riscaldamento, raffrescamento, ACS, ventilazione, illuminazione, plug load e produzione; separa consumo, domanda, rendimento e comfort.
4. **Gate delle opzioni:** confronta involucro, regolazione, pompe, generazione, accumulo, rinnovabili, combustibili e comportamento con energia primaria/finale, emissioni, costo, picco, manutenzione e lock-in.
5. **Gate dello scenario:** definisci anno base, clima, uso, prezzi, fattori emissivi, durata, rebound, degrado e interazioni; non sommare risparmi indipendenti quando si sovrappongono.
6. **Gate della misura e verifica:** predefinisci baseline aggiustata, periodo, KPI, normalizzazione, qualità dati, contatore virtuale e soglia di successo; confronta previsione, misura e incertezza dopo l'intervento.
7. **Gate della roadmap:** ordina interventi per sicurezza, comfort, carbonio, costo, fattibilità, manutenzione e dipendenze; registra owner, investimento, trigger, revisione e stato di attuazione.

## Output

Consegna un energy_decarbonization_record con perimetro, baseline, contatori, indicatori, qualità dati, end-use, opzioni, scenari, costi, emissioni, misura e verifica, roadmap e stato measured, conditional o blocked. Ogni risparmio riporta formula, periodo, normalizzazione, fattore emissivo e incertezza.

## Quality gates

- Confini, anno base, uso, clima, vettori, contatori e fattori emissivi sono dichiarati.
- Consumo misurato, domanda calcolata, risparmio previsto e riduzione verificata restano distinti.
- Dati mancanti, stime, cambi uso, comfort e normalizzazione sono visibili.
- Interventi interdipendenti, rebound, picchi, manutenzione e degradazione sono considerati.
- Misura e verifica sono progettate prima dell'intervento e hanno responsabile e periodo.
- Nessun output presenta carbon neutrality, conformità, APE o incentivo come risultato automatico.

## Evidenza e provenienza

Conserva bollette, letture, curve di carico, dati meteo, BMS, contatori e tariffe, audit, schede, fattori emissivi, modelli, formule, script, commissioning, foto e hash. Marca dato primario, proxy, stima, normalizzazione e decisione. Dati di consumatori, impianti e sicurezza hanno accesso per ruolo; le licenze dei dataset e dei fattori restano tracciate.

## Fonti ufficiali e diritti

- [Direttiva (UE) 2024/1275 su EUR-Lex](https://eur-lex.europa.eu/eli/dir/2024/1275/oj/eng): prestazione energetica degli edifici e traiettoria verso edifici a emissioni zero, da verificare per recepimento e applicabilità nazionale.
- [ISO 50001:2018](https://www.iso.org/standard/69426.html): quadro ufficiale per sistemi di gestione dell'energia e miglioramento della prestazione.
- [ENEA](https://www.enea.it/it): dati, strumenti e riferimenti istituzionali italiani per efficienza energetica e decarbonizzazione, da verificare per misura e programma.

Le direttive, norme ISO, dataset e fattori emissivi possono essere restricted o avere condizioni d'uso proprie; non si copiano testi o tabelle protette. Baseline, formule, roadmap e procedure di misura sono originali. Stato diritti: official_reference_only_no_text_reproduced.

## Confini professionali e legali

La skill non progetta o collauda impianti, non rilascia APE, non certifica emissioni, non garantisce risparmi, non approva incentivi e non sostituisce energy manager, progettista, certificatore, manutentore, gestore o autorità. Un modello economico o emissivo è valido solo per confini, fattori, dati e scenario dichiarati.

## Failure modes

- **Bollette senza contatori o uso:** marca baseline debole e non attribuire risparmi per end-use.
- **Risparmi sommati due volte:** esplicita interazioni e ricalcola scenario integrato.
- **Fattore emissivo senza anno/geografia:** blocca confronto e registra fonte/versione.
- **Comfort sacrificato per kWh:** aggiungi temperatura, umidità, qualità aria e reclami al criterio.
- **Produzione rinnovabile confusa con riduzione del fabbisogno:** separa domanda, consumo, export e fattore di rete.
- **Forecast presentato come verifica:** pianifica M&V post-intervento e considera incertezza e degrado.

## Strumenti

Usa contatori e BMS, data quality log, normalizzazione climatica, modello end-use, calcolo di scenari, registro interventi, dashboard KPI e repository versionato. Automatizza acquisizione, unità, anomalie, formule e grafici; non automatizzare APE, claim emissivi, approvazioni o decisioni professionali.
