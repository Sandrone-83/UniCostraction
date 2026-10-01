# VERSIONE — Punto di riferimento per AuraTrix

## Versione corrente: **v1.0.0** — 2026-10-01

**Stato: RILASCIATA (tag Git `v1.0.0`)**

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
| v1.0.0 | 2026-10-01 | Prima versione rilasciata: 42 corsi pack, enciclopedia con glossario (250+ termini), esami, CHANGELOG con 18 voci di correzione registrate (Giri A e B), licenza Auratrix |
