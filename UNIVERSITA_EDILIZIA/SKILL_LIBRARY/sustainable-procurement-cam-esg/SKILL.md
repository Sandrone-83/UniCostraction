---
name: sustainable-procurement-cam-esg
description: Trasforma CAM, requisiti ESG e claim di filiera in criteri, prove, scoring e controlli di esecuzione senza sostituire stazione appaltante, legale, auditor o responsabile ambientale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: procurement sostenibile, CAM ed ESG
---

# Procurement sostenibile, CAM ed ESG

## Attivazione e input

Attiva questa skill quando una gara, acquisto, subappalto o gestione di fornitura deve integrare criteri ambientali minimi, clima, circolarità, lavoro, diritti umani, governance e tracciabilità. È una faccetta di specifica e verifica della sostenibilità distinta da public-procurement-company-contracts, circular-materials-lca-inventory e construction-business-operations: non scrive un bando definitivo, non certifica ESG e non decide l'aggiudicazione.

Prima raccogli oggetto, settore, stazione appaltante/azienda, regime contrattuale, CAM applicabile e data, requisiti tecnici, criteri premianti, soglie, catena di fornitura, rischi, dati ESG, certificazioni, EPD, audit, diritti di verifica, condizioni di esecuzione e ruoli. Registra giurisdizione, versione dei documenti, periodo di rendicontazione e criterio pass/fail. Se oggetto, CAM, periodo o autorità non sono chiari, lo stato è blocked.

## Workflow

1. **Gate dell'oggetto:** descrivi bisogno, funzione, durata, quantità e ciclo di vita; separa requisito minimo, criterio premiante, obiettivo ESG e claim volontario.
2. **Gate normativo:** identifica CAM, Codice appalti, obblighi ambientali/sociali, tassonomia/ESRS eventualmente applicabili e versione; registra fonti, transitorio, campo e prove ammesse.
3. **Gate della catena:** mappa produttore, distributore, subfornitore, materia prima, sito, trasporto, energia, lavoro e fine vita; identifica punti di rischio e auditability.
4. **Gate dell'evidenza:** collega ogni criterio a dichiarazione, certificato, EPD, prova laboratorio, registro, audit, contratto o dato primario; verifica soggetto, prodotto, validità, scope e catena di custodia.
5. **Gate dello scoring:** definisci pesi, soglie, fattori di normalizzazione, evidenza minima, gestione incompleta e conflitti; non attribuire punti a un claim non dimostrato o comparare offerte con basi diverse.
6. **Gate dell'esecuzione:** traduci criteri in clausole, deliverable, controlli, campioni, audit, KPI, non conformità, rimedio e sospensione; separa verifica gara e verifica del contratto.
7. **Gate della comunicazione:** prepara matrice claim-prova-versione-periodo, limiti e approvazione; non usare “green”, “net zero”, “etico” o “CAM compliant” senza scope e verificatore.

## Output

Consegna un sustainable_procurement_record con oggetto, criteri, fonti, versione, matrice supplier-chain, prove, scoring, gap, controlli in esecuzione, claim e stato evidenced, conditional o blocked. Ogni risultato riporta il soggetto che dichiara, il soggetto che verifica, il periodo e il diritto di audit.

## Quality gates

- Oggetto, funzione, giurisdizione, CAM applicabili, versione e periodo sono identificati.
- Requisiti minimi, premianti, ESG e volontari sono distinti.
- Certificazioni e claim hanno titolare, scope, prodotto, sito, validità e fonte.
- Filiera, subfornitura, materia prima, lavoratori, dati e audit sono tracciabili.
- Scoring, soglie, incompleti, conflitti e controlli di esecuzione sono riproducibili.
- Nessun output dichiara aggiudicazione, conformità CAM o certificazione ESG senza autorità/verificatore competente.

## Evidenza e provenienza

Conserva capitolato, criteri, fonti, versioni, dichiarazioni, EPD, certificati, audit, test, catena di custodia, dati di filiera, registri di consegna, non conformità, rimedi, approvazioni e hash. Marca dato primario, autodichiarato, verificato, proxy e non dimostrato. Dati commerciali, lavorativi e personali sono minimizzati e accessibili per ruolo; rispetta licenze e riservatezza dei fornitori.

## Fonti ufficiali e diritti

- [ISO 20400:2017](https://www.iso.org/standard/63026.html): guida ufficiale per integrare sostenibilità nelle politiche e nei processi di procurement.
- [CAM edilizia — MASE](https://gpp.mase.gov.it/sites/default/files/2024-08/allegato-tecnico-CAM-edilizia-07-06-2022-rev-correttivo.pdf): criteri ambientali minimi e indicazioni per lavori edilizi e gestione del cantiere; verificare versione e ambito.
- [D.Lgs. 36/2023 su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2023-03-31%3B36%21vig=): Codice dei contratti pubblici e disciplina da verificare per procedura e ruolo.
- [Direttiva CSRD 2022/2464 su EUR-Lex](https://eur-lex.europa.eu/eli/dir/2022/2464/oj): obblighi europei di rendicontazione societaria di sostenibilità, da applicare solo ai soggetti e periodi pertinenti.

Norme ISO, CAM, ESRS, certificati e documenti di terzi sono soggetti a diritti, licenze e versioni: non si copiano testi, marchi o attestazioni. Matrici, scoring, gate e procedure sono originali. Stato diritti: official_reference_only_no_text_reproduced.

## Confini professionali e legali

La skill non emette certificati, non verifica legalmente dichiarazioni, non decide gara, non firma bando o contratto, non accerta violazioni del lavoro e non sostituisce stazione appaltante, RUP, buyer, auditor, legale, commercialista o responsabile ambientale. Un claim ESG o CAM è valido solo per oggetto, periodo, scope, fonte e verificatore indicati.

## Failure modes

- **Certificato fuori scope:** marca non applicabile e verifica prodotto, sito, validità e titolare.
- **CAM copiato da versione vecchia:** riapri data, appalto, transitorio e criterio vigente.
- **Autodichiarazione usata come prova indipendente:** separa dichiarazione, verifica e diritto di audit.
- **Punteggio ESG non comparabile:** allinea confini, denominatore, periodo, metodo e dati mancanti.
- **Filiera indiretta invisibile:** mappa subfornitori, materia prima e sito e assegna controlli.
- **Claim verde assoluto:** blocca comunicazione e sostituisci con claim circoscritto e verificabile.

## Strumenti

Usa procurement requirements matrix, supplier questionnaire, chain-of-custody register, evidence repository, scoring model, audit plan, non-conformity tracker e claim register. Automatizza scadenze, validità, completeness e confronto; non automatizzare aggiudicazione, certificazione o giudizi su diritti e persone.
