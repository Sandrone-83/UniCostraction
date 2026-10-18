---
name: construction-site-safety
description: Organizza preparazione, controllo e documentazione di cantieri e sicurezza, arrestando le conclusioni quando ruoli, rischi, misure o autorizzazioni non sono verificati.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: sicurezza cantiere
---

# Cantiere e sicurezza

## Attivazione

Usa la skill per piano di avvio, POS/PSC come supporto alla raccolta, matrice rischi, coordinamento imprese, sopralluoghi, non conformità, briefing e chiusura lavori. Non usarla per sostituire RSPP, CSP/CSE, datore di lavoro, medico competente o autorità.

## Input minimo

Identifica committente, impresa e lavoratori, ruoli formalizzati, fase e luogo, lavorazioni, attrezzature, interferenze, accessi, emergenze, sottoservizi, condizioni meteo, documenti applicabili e segnalazioni pregresse.

## Workflow

1. Mappa attività, sequenza, interfacce, persone esposte e condizioni di stop.
2. Collega ogni pericolo a rischio, misura, responsabile, evidenza e data di controllo.
3. Verifica che piano, procedure operative, formazione, DPI, attrezzature e autorizzazioni siano pertinenti alla fase.
4. Prepara briefing con linguaggio comprensibile; registra presenze e domande, senza inventare attestati.
5. Durante il sopralluogo separa osservazione, valutazione e azione correttiva; fotografa solo con base autorizzativa.
6. Classifica le non conformità per gravità e urgenza; per un rischio grave o non controllato proponi sospensione dell'attività e escalation al responsabile.
7. Chiudi solo con evidenza dell'azione, responsabile, data e verifica dell'efficacia.

## Output

Produci registro rischi e interferenze, lista documenti mancanti, verbale di sopralluogo, piano azioni, briefing sintetico, evidenze con data/luogo e rapporto di chiusura. In ogni output indica il soggetto che deve approvare o eseguire.

## Quality gates

- Nessuna lavorazione entra in stato "controllata" senza evidenza attuale.
- Ruoli e responsabilità sono nominativi e non dedotti dall'organigramma implicito.
- Le misure sono attuabili nella fase reale e non solo prescrizioni generiche.
- Le emergenze includono accessi, comunicazione, primo soccorso e coordinamento.
- Le foto e i dati personali hanno base di uso e conservazione dichiarata.

## Evidenza e provenienza

Registra versione del piano, sopralluogo, fonte dell'osservazione, nominativi autorizzati, data/ora e catena di approvazione. Conserva l'originale e una copia di lavoro; usa hash per verbali firmati o allegati critici.

## Confini professionali e legali

Il D.Lgs. 81/2008 e le prescrizioni applicabili devono essere verificati nella versione vigente. Non dichiarare conformità, idoneità o assenza di rischio; una checklist non sostituisce valutazione dei rischi, formazione, sorveglianza sanitaria o coordinamento obbligatorio. Per pericolo immediato privilegia messa in sicurezza, allontanamento e chiamata dei responsabili/servizi competenti.

## Failure modes

- **POS/PSC mancante o incoerente:** blocca l'uso come evidenza di autorizzazione.
- **Foto senza contesto:** aggiungi data, fase e posizione oppure declassa l'osservazione.
- **DPI usato come unica misura:** riesamina eliminazione, protezione collettiva e organizzazione.
- **Checklist copiata:** adatta i rischi alla lavorazione reale e documenta l'adattamento.
- **Incidente:** preserva fatti e sicurezza, non attribuire colpe né alterare prove.

## Strumenti

Usa moduli controllati, registro versioni, fotocamera autorizzata, foglio azioni, QR/ID per attrezzature e repository con permessi. Gli strumenti digitali aiutano la tracciabilità ma non sostituiscono il sopralluogo.

## Fonti ufficiali e diritti

- [Normattiva — D.Lgs. 81/2008](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): testo vigente da verificare; nessun testo riprodotto.
- [EU-OSHA — legislation](https://osha.europa.eu/en/legislation): quadro europeo istituzionale; usare come riferimento e verificare l'attuazione italiana.
- [INAIL — portale istituzionale](https://www.inail.it/portale/it.html): guide e orientamenti; copyright e condizioni d'uso da verificare.

La skill non è un DVR, POS, PSC, verbale ispettivo o parere legale.
