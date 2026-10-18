---
name: fire-engineering-performance-verification
description: Imposta verifiche prestazionali antincendio e tracciabilità di scenari, esodo, compartimentazione, fumo e impianti senza sostituire il professionista antincendio o l'autorità competente.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: fire engineering e prevenzione incendi
---

# Fire engineering e verifica prestazionale antincendio

## Attivazione e input

Attiva questa skill quando una soluzione antincendio deve essere dimostrata con scenari, modelli, calcoli, prove o misure invece che con una semplice prescrizione. È una faccetta di impostazione e audit dell'evidenza distinta da construction-site-safety, structural-civil-engineering e mep-energy-systems: non redige una pratica firmata, non approva un'attività e non sostituisce il professionista antincendio.

Prima raccogli attività e assoggettabilità, destinazione e occupanti, geometria e compartimenti, carico d'incendio e sorgenti, strutture e involucro, vie d'esodo, ventilazione e controllo fumo, impianti di protezione, accesso dei soccorritori, fasi e uso previsto. Registra autorità, versione normativa, obiettivo prestazionale, scenari credibili e criterio di accettazione. Se uso, autorità, geometria o scenario non sono definiti, lo stato è blocked.

## Workflow

1. **Gate dell'ambito:** identifica attività, regime applicabile, confini dell'opera e interfacce con edifici o impianti confinanti; separa requisito cogente, assunzione di progetto e preferenza del committente.
2. **Gate della base geometrica:** congela planimetrie, sezioni, quote, compartimenti, aperture, affollamento, porte e percorsi con revisione e coordinate; controlla che il modello usato nella verifica corrisponda a quello progettato.
3. **Gate degli scenari:** costruisci matrice sorgente-localizzazione-crescita-ventilazione-occupanti-soccorso e seleziona scenari rappresentativi, inclusi guasti o condizioni sfavorevoli motivati. Non scegliere lo scenario solo perché produce l'esito migliore.
4. **Gate dei sottosistemi:** collega ogni ipotesi a esodo, tenuta al fuoco, fumo, strutture, rivelazione, spegnimento, controllo accessi e soccorso; definisci dipendenze, alimentazioni, tempi di intervento e condizioni di indisponibilità.
5. **Gate del metodo:** dichiara formule, modello, mesh o discretizzazione, dati di input, sensibilità, criteri di convergenza, qualità delle misure e versione del software. Un risultato numerico senza dominio di validità è non dimostrato.
6. **Gate della prova:** pianifica prove, commissioning o misure indipendenti con precondizioni, strumento, calibrazione, durata, witness e pass/fail. Simulazione, prova di laboratorio e comportamento in esercizio restano evidenze diverse.
7. **Gate della decisione:** prepara matrice requisito-evidenza-scarto, limitazioni, misure compensative e condizioni di esercizio; sottoponi relazione, firma e dialogo con i VVF all'autorità e al professionista responsabile.

## Output

Consegna un fire_performance_record con base normativa e versione, geometria, assunzioni, scenari, modello, input, risultati, sensibilità, prove, issue, misure compensative, condizioni operative e stato demonstrated, conditional o blocked. Ogni conclusione riporta lo scenario e il limite oltre il quale non vale.

## Quality gates

- Attività, autorità, versione normativa e obiettivo della verifica sono identificati.
- Geometria, occupanti, compartimenti, esodo e interfacce sono coerenti tra elaborati e modello.
- Ogni requisito ha evidenza, criterio, responsabile e stato, inclusi gli aspetti non verificabili.
- Gli scenari coprono variabilità e guasti plausibili e non sono selezionati per convenienza.
- Input, software, unità, calibrazioni, convergenza e sensibilità sono registrati.
- Nessun risultato viene presentato come certificazione, SCIA, approvazione o agibilità senza firma e iter autorizzato.

## Evidenza e provenienza

Conserva revisioni di disegni e modelli, fonti normative consultate, inventario occupanti e materiali, dati di prova, certificati di laboratorio, strumenti e calibrazioni, script/modelli di calcolo, log, hash, fotografie contestualizzate e verbali. Marca ciò che è osservato, assunto, simulato, misurato o approvato. Dati di sicurezza, planimetrie sensibili e informazioni sugli occupanti sono minimizzati e accessibili per ruolo.

## Fonti ufficiali e diritti

- [Corpo Nazionale dei Vigili del Fuoco — Codice di prevenzione incendi](https://www.vigilfuoco.it/codice-di-prevenzione-incendi): portale e chiarimenti istituzionali sul DM 3 agosto 2015; verificare testo coordinato e aggiornamenti.
- [Regole tecniche coordinate dei Vigili del Fuoco](https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/prevenzione-incendi/testi-coordinati-di-prevenzione/testi-coordinati-prevenzione-regole-tecniche-suddivise-per-attivita?page=9): archivio ufficiale per attività e regole tecniche applicabili.
- [Gazzetta Ufficiale — DM 3 agosto 2015](https://www.gazzettaufficiale.it/eli/gu/2015/08/20/192/so/51/sg/pdf): pubblicazione ufficiale e allegati da verificare nella versione vigente.

Le fonti normative sono riferimenti ufficiali: non si riproducono testi protetti o manuali coordinati oltre quanto consentito. Il workflow, la matrice degli scenari e il record di evidenza sono originali. Stato diritti della skill: official_reference_only_no_text_reproduced; standard tecnici e software di simulazione restano soggetti a licenza.

## Confini professionali e legali

La skill non certifica la sicurezza antincendio, non determina l'assoggettabilità definitiva, non firma relazioni, non presenta pratiche e non ordina evacuazioni o modifiche d'impianto. Non sostituisce professionista antincendio, progettista, responsabile dell'attività, manutentore, laboratorio, VVF o autorità. Un esito numerico vale solo per input, scenario, modello e condizioni registrati; non è garanzia di comportamento reale.

## Failure modes

- **Scenario scelto per ottenere pass:** riapri la matrice e documenta scenari alternativi e sensibilità.
- **Modello non aggiornato:** sospendi l'esito, confronta revisioni e ricalcola gli elementi interessati.
- **Calcolo scambiato per certificato:** cambia stato in blocked e instrada a professionista e autorità.
- **Impianto dichiarato disponibile senza prova:** richiedi commissioning, alimentazione, manutenzione e test di indisponibilità.
- **Affollamento o tempi di esodo inventati:** separa dati osservati e ipotesi, richiedendo fonte e approvazione.
- **Misura non calibrata o non ripetibile:** scarta il risultato, registra l'incertezza e ripeti con strumento idoneo.

## Strumenti

Usa matrice requisiti-scenari, modello geometrico versionato, foglio di calcolo riproducibile, software di simulazione con report, registro prove e issue tracker. Automatizza controlli di coerenza, unità, versioni e copertura; non automatizzare firma, certificazione o giudizio dell'autorità.
