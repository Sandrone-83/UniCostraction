# VERSIONE — Punto di riferimento per AuraTrix

## Versione corrente: **v1.1.0** — 2026-10-01

**Stato: RILASCIATA (tag Git `v1.1.0`)**

## Cosa contiene v1.1.0 rispetto a v1.0.0 (da leggere prima di agganciare AuraTrix)

- **7 corsi nuovi (73 schede nuove)**: ascensori e movimentazione verticale (10),
  fotovoltaico campi/agrivoltaico/CER con dati incentivi verificati 10/2026 (15),
  sicurezza di cantiere D.Lgs 81/08 (13), murature intonaci e finiture (12),
  facility management e manutenzione programmata (12), fisco e tributi dell'impresa
  edile (11)
- **+20 schede di approfondimento** su 5 corsi esistenti (legno, costruzioni
  speciali, materiali del futuro, sicurezza antincendio/accessibilità, edilizia
  industriale)
- **47 esami nuovi**: copertura completa — ogni corso (49/49) ha il proprio esame;
  11.385 domande in formato standard + 3.000 legacy dei primi giri; chiavi riservate
  fuori repository
- **Risultato**: 49 corsi, 702 schede, 50 esami (14.385 domande totali)
- **Correzioni**: 4 COURSE.yaml privi del conteggio `schede:` completati; nessuna
  correzione normativa (sole aggiunte) — coerente con incremento minor
- CHANGELOG: voci Giri C, D, E, F, G con protocollo Prima/Dopo/Fonte; le tre righe
  «DA VERIFICARE» ereditate da v1.0.0 restano aperte ma non bloccanti (riguardano
  solo la numerazione precisa di riferimenti già espressi in forma prudente)

## Come funziona il versionamento di questa repository

1. Il materiale cresce di continuo sulla branch `main`: ogni giro di ricerca e
   approfondimento aggiunge schede, esami e voci di enciclopedia.
2. **Solo il materiale con un tag di versione è «approvato» per AuraTrix.**
   Tutto ciò che sta sulla branch `main` dopo l'ultimo tag è bozza di lavoro:
   utilizzabile per sperimentazione, mai citato a un cliente come fatto.
3. Quando un giro di verifica si chiude (correzioni registrate in
   [CHANGELOG.md](CHANGELOG.md), validazione JSON di tutti i pack superata,
   enciclopedia rigenerata), si crea un nuovo tag:

   | Tipo di cambiamento | Incremento | Esempio |
   |---|---|---|
   | Aggiunta schede/esami, nessuna correzione normativa | minor | v1.1.0 |
   | Correzione normativa o fattuale, anche su una sola riga | patch | v1.0.1 |
   | Ristrutturazione architetturale della repository | major | v2.0.0 |

4. AuraTrix deve dichiarare sempre la versione con cui sta lavorando, ad esempio
   nelle risposte a cliente: «secondo UniCostraction v1.0.0».
5. Per passare a una versione nuova si decide **a monte**: si aggiorna AuraTrix
   solo dopo aver letto il CHANGELOG tra la versione agganciata e quella nuova.

## Criteri di rilascio (tutti obbligatori)

- [x] Tutti i file `schede.jsonl` validano come JSON (script di controllo eseguito a ogni giro).
- [x] Nessun riferimento normativo privo di fonte nelle schede (le sole righe «DA VERIFICARE» del
      changelog riguardano numerazioni precise già espresse in forma prudente nel materiale).
- [x] CHANGELOG.md aggiornato con le tre colonne Prima / Dopo / Fonte.
- [x] Enciclopedia, glossario e mappa rigenerati dalle schede corrette.
- [x] Conteggi `schede:` nei `COURSE.yaml` allineati al numero reale di righe.

## Storico versioni

| Tag | Data | Contenuto |
|---|---|---|
| v1.1.0 | 2026-10-01 | Sole aggiunte: 7 corsi nuovi (73 schede), +20 approfondimenti, 47 esami nuovi (copertura 49/49 corsi, 14.385 domande totali). Nessuna correzione normativa |
| v1.0.0 | 2026-10-01 | Prima versione rilasciata: 42 corsi pack, enciclopedia con glossario (250+ termini), esami, CHANGELOG con 18 voci di correzione registrate (Giri A e B), licenza Auratrix |
