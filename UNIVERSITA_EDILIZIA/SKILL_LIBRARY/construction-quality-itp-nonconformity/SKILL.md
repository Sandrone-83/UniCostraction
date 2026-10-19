---
name: construction-quality-itp-nonconformity
description: Costruisce ITP, punti hold/witness, registri di ispezione e ciclo delle non conformità in costruzione, separando controllo qualità, accettazione contrattuale e collaudo.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: gestione qualità, ITP e nonconformità
---

# Gestione qualità, ITP e nonconformità di costruzione

## Attivazione e input

Attiva questa skill prima di una lavorazione, di una fornitura o di una fase che richiede prove, ispezioni, approvazioni o tracciabilità, oppure quando emerge una deviazione e serve governarne contenimento, disposizione e causa. È una faccetta di controllo esecutivo distinta da mep-testing-commissioning, che tratta prove di sistemi MEP, e da sal-progress-quantity-reconciliation, che tratta quantità e avanzamento.

Raccogli contratto e specifiche, elaborati approvati, requisiti CAM o legislativi pertinenti, WBS, submittal, method statement, matrice materiali-lotti, ITP proposta, criteri accettazione, punti hold/witness, ruoli e poteri, strumenti, laboratori, condizioni di rilascio, NCR aperte e sistema di revisione. Se requisito, elemento o autorità di accettazione non sono identificati, lo stato è blocked.

## Workflow

1. **Gate dei requisiti:** traduci requisiti contrattuali e di progetto in record verificabili, mantenendo fonte, revisione, unità, tolleranza e criterio pass/fail.
2. **Gate dell'ITP:** associa a ogni attività precondizioni, controllo, frequenza/campionamento, test, documento, responsabile, hold, witness, notifica e rilascio.
3. **Gate della readiness:** prima di iniziare verifica disegni, materiali, approvazioni, attrezzature, competenza, ambiente e punti di controllo; un hold non può essere saltato per urgenza non autorizzata.
4. **Gate dell'esecuzione:** registra osservazione, misura, lotto, posizione, data, strumento, operatore, foto e riferimento al requisito; separa test, ispezione documentale e accettazione.
5. **Gate della NCR:** descrivi fatto e requisito violato, contiene il difetto, valuta estensione e rischio, assegna responsabile e termine, quindi scegli correzione, rework, scarto, use-as-is o concessione autorizzata.
6. **Gate della causa:** usa evidenza e trend per causa contribuente e radice, definisci CAPA proporzionata e verifica efficacia su un campione indipendente.
7. **Gate del rilascio:** chiudi solo con evidenza sufficiente, approvazione competente, aggiornamento as-built e collegamento a test, manutenzione o accettazione finale quando necessario.

## Output

Produci un itp_quality_record con requisito, attività, precondizioni, controlli, punti, prove, risultati, rilascio e revisioni; e un ncr_record con descrizione, contenimento, impatto, disposizione, CAPA, owner, scadenze, approvazioni e chiusura. Stati ammessi: planned, ready, hold, nonconforming, conditional_release, verified_closed o blocked.

## Quality gates

- Ogni controllo ha requisito, revisione, criterio, evidenza, owner e stato.
- Hold point ha notifica e autorizzazione documentate; witness point registra presenza o mancata presenza senza inventare un'approvazione.
- Materiale, lotto, posizione, metodo, strumento e rapporto di prova sono riconciliabili.
- NCR non viene chiusa da una fotografia o da una dichiarazione senza verifica del requisito.
- Use-as-is, concessioni e deroghe sono approvate dal soggetto con potere contrattuale e non cancellano l'evidenza.
- CAPA verifica efficacia e propagazione a lavori o lotti analoghi.

## Evidenza e provenienza

Conserva specifiche e disegni revisionati, submittal, certificati di origine e conformità, lotti, delivery records, ITP, pre-job check, rapporti laboratorio, calibrazioni, foto georeferenziate o localizzate, verbali hold/witness, NCR, concessioni, CAPA e audit trail. Marca originale, copia controllata, misura, dichiarazione e decisione. Non alterare un record chiuso: correggi con addendum versionato.

## Fonti ufficiali e diritti

- [ISO 10005:2018 — quality plans](https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/07/03/70398.html): riferimento ufficiale per piani qualità, consultato senza riprodurre lo standard.
- [ISO 9001 — pagina ufficiale](https://www.iso.org/standard/9001.html): quadro del sistema qualità; verificare l'edizione corrente applicabile al contratto.
- [Normattiva — D.Lgs. 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2023-03-31%3B36%21vig=): ruoli e disciplina dei contratti pubblici, quando pertinenti.
- [ANAC](https://www.anticorruzione.it/): atti e indicazioni istituzionali per contratti pubblici, da verificare per stazione appaltante e data.

ITP, record e criteri di workflow sono originali. Diritti: official_reference_only_no_text_reproduced; standard ISO, specifiche del committente, certificati e moduli di terzi non vengono copiati né redistribuiti. Le fonti pubbliche devono essere ricontrollate alla data della decisione.

## Confini professionali e legali

La skill non accetta lavori per conto della direzione lavori, non firma collaudi, non concede deroghe, non interpreta unilateralmente il contratto e non sostituisce progettista, direttore lavori, ispettore, laboratorio, RUP, collaudatore o responsabile qualità. Un ITP completo non dimostra da solo conformità dell'opera, sicurezza o idoneità all'uso.

## Failure modes

- **Requisito vago:** blocca il punto e chiede criterio misurabile o decisione autorizzata.
- **Hold saltato:** registra l'evento, conserva stato e coinvolge l'autorità; non retrodata il witness.
- **NCR cosmetica:** riscrivi il fatto con posizione, requisito, estensione e rischio, senza colpe personali non provate.
- **Lotto non tracciabile:** quarantena/rilascio condizionato solo con autorità, ricostruendo i confini.
- **Concessione scambiata per conformità:** mantieni separati deviazione, accettazione condizionata e requisito originario.
- **CAPA non efficace:** riapri la NCR o una preventiva correlata e amplia il campionamento.

## Strumenti

Usa WBS, requirement matrix, ITP, submittal register, hold/witness calendar, test register, NCR/CAPA tracker, lot map, calibration register e dashboard trend. Automatizza notifiche, completezza e collegamenti tra record; non automatizzare pass/fail definitivo, concessione o chiusura senza approvazione e verifica.
