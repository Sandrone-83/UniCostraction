---
name: road-infrastructure-bridge-engineering
description: Organizza censimento, ispezione, rischio e verifica operativa di strade, ponti e opere d'arte senza sostituire il progettista, il gestore o l'autorità stradale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: infrastrutture stradali e ponti
---

# Infrastrutture stradali e ponti: conoscenza e rischio operativo

## Attivazione e input

Attiva questa skill quando una strada, un ponte, un viadotto, un rilevato, un cavalcavia o una loro interfaccia deve passare da dati dispersi a censimento, ispezione, classe di attenzione, piano di monitoraggio o priorità di intervento. È una faccetta di conoscenza e gestione del rischio distinta da structural-civil-engineering e construction-site-safety: non calcola la sicurezza ultima, non apre/chiude una strada e non firma un progetto.

Prima raccogli gestore e proprietà, identificativi e coordinate, geometria, schema statico noto, traffico e carichi, ambiente e idraulica, frane, sismica, storia manutentiva, ispezioni, difetti, limitazioni, incidenti, sensori, accessibilità e obiettivo decisionale. Registra data, versione delle linee guida, livello di conoscenza e criterio di accettazione. Se opera, gestore, data o uso non sono identificati, lo stato è blocked.

## Workflow

1. **Gate del corridoio:** collega opera, strada, nodo, percorsi alternativi, utenti vulnerabili, sottoservizi, corsi d'acqua e vincoli di cantiere; separa rete, manufatto e ambiente.
2. **Gate del censimento:** assegna ID stabile, coordinate, luci, materiali noti, elementi, giunti, appoggi, drenaggi, barriere, impianti e immagini; mantieni stato rilevato e stato documentale distinti.
3. **Gate dell'ispezione:** pianifica ispezione ordinaria/speciale con accesso, sicurezza, griglia dei difetti, severità, estensione, evoluzione, cause ipotizzate e foto localizzate. Un difetto non localizzato non è una misura ripetibile.
4. **Gate degli agenti di rischio:** valuta traffico, sovraccarico, acqua, frane, corrosione, fatica, urti, incendio, sismica e perdita di ridondanza in base all'evidenza; non sommare punteggi senza rendere visibili le motivazioni.
5. **Gate della sicurezza:** separa screening, classe di attenzione, monitoraggio, verifica strutturale e misura urgente; ogni soglia ha responsabile, tempo di risposta, accesso al dato e azione autorizzata.
6. **Gate del monitoraggio:** definisci sensore, posizione, frequenza, baseline, allarme, calibrazione, perdita dati e validazione con ispezione. Un grafico senza baseline e condizioni ambientali non dimostra evoluzione.
7. **Gate della decisione:** ordina interventi per rischio, urgenza, rete, costo, reversibilità e disponibilità; prepara limitazioni di traffico o messa in sicurezza solo per decisione del gestore e delle autorità.

## Output

Consegna un infrastructure_asset_record con ID, posizione, inventario, difetti, ispezioni, agenti di rischio, evidenze, classe o screening, monitoraggio, priorità, limitazioni e stato observed, conditional o blocked. Ogni priorità conserva la ragione, la data e il soggetto che deve decidere.

## Quality gates

- Opera, gestore, coordinate, uso, data e linea guida applicabile sono identificati.
- Censimento, difetto, foto, misura e intervento hanno posizione e versione tracciabili.
- Screening, verifica strutturale, monitoraggio e decisione gestionale sono separati.
- Difetti e segnali sono valutati per evoluzione, cause concorrenti e condizioni ambientali.
- Ogni allarme ha soglia, responsabile, reperibilità, risposta e prova di funzionamento.
- Nessun report presenta classe di attenzione o screening come certificazione di sicurezza o autorizzazione al traffico.

## Evidenza e provenienza

Conserva rilievi, schede, fotografie con coordinate/data, disegni, rapporti di ispezione, prove, sensori, calibrazioni, serie temporali, log di accesso, manutenzioni, restrizioni, incidenti e hash. Marca osservato, riferito, calcolato, ipotizzato e approvato. Planimetrie di sicurezza, vulnerabilità e dati del gestore sono accessibili per ruolo.

## Fonti ufficiali e diritti

- [MIT — Decreto ministeriale 578 del 17 dicembre 2020](https://mit.gov.it/index.php/normativa/decreto-ministeriale-numero-578-del-17122020): linee guida per classificazione, gestione del rischio, valutazione e monitoraggio dei ponti esistenti.
- [MIT — sicurezza delle infrastrutture stradali](https://www.mit.gov.it/documentazione/il-decreto-legislativo-n-352011-adozione-delle-linee-guida-per-la-gestione-della): linee guida e quadro per controlli e ispezioni di sicurezza stradale.
- [Codice della strada su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1992-04-30;285!vig=): disciplina nazionale da verificare per competenza, versione e tratto.

Gli atti e le linee guida sono riferimenti ufficiali: non si riproducono schede, allegati o manuali protetti oltre i diritti applicabili. Il record, la matrice di difetti e la procedura di triage sono originali. Stato diritti: official_reference_only_no_text_reproduced; dati del gestore e rilievi restano soggetti a contratto e riservatezza.

## Confini professionali e legali

La skill non certifica la sicurezza, non esegue calcoli strutturali, non dichiara agibilità, non impone limiti di traffico, non firma ispezioni e non sostituisce gestore, ingegnere, ispettore, coordinatore, autorità o soccorso. Un livello di screening non è una verifica di sicurezza; un difetto grave richiede escalation immediata secondo il piano del gestore.

## Failure modes

- **Censimento senza coordinate o ID stabile:** blocca confronto ed evoluzione e richiedi riconciliazione.
- **Punteggio usato come verità strutturale:** esplicita dati, pesi, incertezza e invia a verifica professionale.
- **Foto senza scala o data:** marca evidenza debole e ripeti con localizzazione e riferimento.
- **Sensore senza baseline:** non generare allarme conclusivo e valida con ispezione.
- **Rischio idraulico o frana ignorato:** riapri il gate ambientale e l'interfaccia con il territorio.
- **Restrizione proposta senza autorità:** prepara opzioni e inoltra al gestore/autorità competente.

## Strumenti

Usa GIS, asset register, app di ispezione con foto localizzate, modello strutturale solo se autorizzato, sensori con log, dashboard di trend e issue tracker. Automatizza ID, completezza, georeferenziazione e priorità documentale; non automatizzare il giudizio di sicurezza o la chiusura della strada.
