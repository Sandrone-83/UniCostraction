# UNI QA / Provenance — G1 separazione esami

Data: 2026-10-17
Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`
Base: `c9ce99c6d0c1243972099a2fd1eca7c25454860e`

## Perimetro del controllo

Il controllo QA è intenzionalmente limitato e vive in
`tests/coordination/test_exam_separation_g1.py`. Usa due campioni già pubblici,
uno per formato:

| Campione | Formato | Conteggio atteso | Integrità del campione |
|---|---:|---:|---|
| `ESAMI/ACUSTICA/domande.md` | `## Domanda N` | 220 | SHA-256 atteso nel test |
| `ESAMI/MATERIALEDILE/domande.md` | `**D<n>.**` legacy | 1.000 | SHA-256 atteso nel test |

Gli hash e i conteggi sono metadati di integrità del fixture pubblico; non sono
una chiave di risposta e nel test non compare alcuna lettera corretta, testo
corretto o punteggio atteso.

Il test esegue tre controlli:

1. verifica che i due file siano quelli attesi e che la numerazione sia
   completa per il rispettivo formato;
2. cerca nei blocchi di domanda soltanto campi espliciti di risposta, lasciando
   ammesse le dichiarazioni di riservatezza nella premessa pubblica;
3. verifica che `ESAMI/README.md` e `PROTOCOLLO_VALUTAZIONE.md` indichino
   `ESAMI_RISPOSTE/` come chiave esterna/protetta e che `.gitignore` la escluda.

## Limite del verdetto

Un esito positivo significa soltanto che questo campione pubblico non espone i
campi espliciti cercati e che la separazione è documentata. **Non prova la
correttezza didattica, fattuale o normativa delle domande; non prova la
completezza o l'accuratezza della chiave esterna; non è un esame superato.**

La verifica della chiave reale resta fuori repository e richiede un fixture
protetto controllato dal proprietario, senza committare `ESAMI_RISPOSTE/`.
