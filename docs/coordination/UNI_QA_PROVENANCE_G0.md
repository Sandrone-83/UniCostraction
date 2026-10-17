# UNI QA / Provenance — G0

Data audit: 2026-10-17
Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`
Base osservata: `afab387d6c36b4dbc60a9facf26677d27fe9092a`

## Esito G0

**NON PASS / audit statico soltanto.** Il corpus non è stato corretto, nessun esame è stato somministrato e nessun test automatico è stato eseguito. Questo documento registra ciò che è osservabile nel checkout e i residui che impediscono un verdetto di qualità.

Il worktree era pulito all'avvio e sul branch assegnato. Il commit di questo documento deve restare locale: **nessun push autorizzato**.

## Matrice test / esame

| Superficie | Evidenza nel checkout | Stato osservato | Rischio / limite |
|---|---|---|---|
| Test trasversale | `TEST_AURATRIX_1000_DOMANDE.md` | 1 banca di 1000 domande aperte; dichiara che le risposte attese sono ricavabili dai pack | Non è un esame sigillato: non esiste una chiave separata né un correttore verificato nel repository; la conoscenza necessaria è esposta dai pack |
| Banche esame | `UNIVERSITA_EDILIZIA/ESAMI/*/domande.md` | 73 file di esame individuati; 16.689 intestazioni `## Domanda N` nella metrica strutturale usata, 66.756 opzioni `A-D` | Il conteggio non include i due formati legacy che non usano `## Domanda N` (`MATERIALEDILE` e `IMPIANTI_FV_EOLICO`); non va confrontato direttamente con il totale storico in `AUDIT_CONTENT_LOCKED.md` |
| Chiavi esame | `UNIVERSITA_EDILIZIA/ESAMI/README.md`, `PROTOCOLLO_VALUTAZIONE.md`, `valuta_esami.py` | La chiave prevista è `ESAMI_RISPOSTE/<SETTORE>_risposte.jsonl`, fuori repository; il correttore legge `lettera` oppure ricava la lettera da `risposta_corretta` | La chiave esterna non è stata resa disponibile né verificata; non è possibile produrre punteggi o controllare completezza/ordine delle chiavi |
| Correttore | `UNIVERSITA_EDILIZIA/valuta_esami.py` | Sono documentati i comandi `template` e `valuta`, singolo settore o `--tutti` | Non eseguito: richiede chiavi esterne e scrive un verbale locale; nessuna dichiarazione di pass |
| Generatori | `build_esami*.py`, `build_test_1000.py` | I generatori calcolano internamente la risposta corretta e scrivono la chiave fuori repo | Riesecuzione non verificata; alcuni script hanno destinazioni assolute storiche fuori dal checkout, quindi la riproducibilità è fragile |

### Esposizione delle risposte corrette

La separazione dichiarata tra domande pubbliche e chiavi private è presente nella documentazione e nei generatori. Nei campioni di `domande.md` ispezionati le opzioni sono presentate senza campo `lettera`/`risposta_corretta`, e l'header dichiara `Risposte NON presenti`.

Questa separazione non equivale ancora a una garanzia verificata:

- `TEST_AURATRIX_1000_DOMANDE.md` dichiara esplicitamente che le risposte sono ricavabili dai pack; quindi non è un fixture a risposta sigillata.
- `build_esami.py`, `build_esami_giro5.py`, `build_esami_design_v2.py` e `build_esami_fv.py` contengono la logica della risposta corretta e generano chiavi esterne. La logica non è una fuga nel file domande, ma rende possibile ricostruire le risposte se il pack e il generatore sono accessibili.
- La scansione lessicale limitata ha trovato 302 righe nei file d'esame che contengono termini generici come `risposta corretta`, `soluzione`, `chiave` o `correct answer`. Il numero include gli header standard e testo didattico; l'adjudication riga-per-riga è residua e non va interpretata come 302 fughe di risposta.
- I due esami legacy richiedono un parser distinto: il correttore usa il formato `**D<n>.**` quando deve confrontare una risposta testuale con le opzioni. Questo percorso non è stato eseguito.

## Matrice asset / provenance

| Asset o corpus | Manifest/licenza osservati | Provenance disponibile | Residuo QA |
|---|---|---|---|
| Repository e pack proprietari | `LICENSE`, `README.md` | Copyright/proprietà Auratrix; uso interno; nessuna licenza open source; avvertenza di verifica professionale e normativa | La licenza proprietaria non sostituisce la verifica dei diritti sulle singole fonti incorporate |
| `Edilizia_Pack` | `Edilizia_Pack/manifest.json` | Record con `file`, `doc`, `records`, `license`, `url`; presenti fonti indicate come Public domain US Gov e atti pubblici italiani | Serve controllo completo di attribuzione, snapshot/versione, trasformazioni e compatibilità con uso commerciale |
| `Fondamenti_Pack` | `Fondamenti_Pack/manifest.json` | Include opere Public domain e materiale wiki indicato come `CC BY-SA 4.0` | Va mantenuto l'obbligo share-alike/attribuzione dove applicabile; non risultano hash per ogni record nel manifest osservato |
| `Storia_Pack` | `Storia_Pack/manifest.json` | Include classici dichiarati Public domain, fonti US Gov e materiale Wikipedia `CC BY-SA 4.0` | La classificazione Public domain va legata a giurisdizione, edizione e snapshot effettivi |
| CAD / corpus tecnico | `CAD_Library/training_corpus/manifest.jsonl`, `CAD_Library/COURSE.yaml`, `CAD_Library/catalog.json`, `CAD_Library/catalog.xlsx` | Il manifest registra sorgente, URL, licenza, `license_class`, file raw/parsed, byte, record, split; esempio LibreDWG: `GPL-3.0`, `license_class: research` | `research` non è autorizzazione commerciale; file di test di provenienza varia richiedono review separata e controllo di redistribuzione |
| Norme/incentivi | `UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/README.md`, `Regole_Applicative_CT_3_0_GSE.pdf` | La README identifica il documento ufficiale GSE, URL gse.it e uso per verifica dei valori incentivanti | Occorrono snapshot, hash e controllo di vigenza per ogni fonte normativa; non è stato fatto un audit giuridico |
| IFC | `Edilizia_Pack/raw/bim_ifc/ifc_models/LICENSE` | Esiste una licenza locale per gli IFC | Il contenuto della licenza e la mappatura file-licenza non sono stati analizzati in questo audit breve |

Non sono stati individuati, nell'inventario limitato per nomi Git, file dedicati a `expected`, `protected fixture`, `sealed fixture` o hash di fixture. Sono presenti hash/importi in codice o metadati di alcuni corpus, ma non una catena di verifica sigillata del sistema d'esame.

## Comandi realmente disponibili e stato di esecuzione

Comandi presenti nella documentazione/codice, **non eseguiti come test**:

```text
python UNIVERSITA_EDILIZIA/valuta_esami.py template <SETTORE>
python UNIVERSITA_EDILIZIA/valuta_esami.py template --tutti
python UNIVERSITA_EDILIZIA/valuta_esami.py valuta <SETTORE>
python UNIVERSITA_EDILIZIA/valuta_esami.py valuta --tutti
```

Controlli locali eseguiti durante questo G0:

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse --abbrev-ref HEAD
git log -1 --format="%H %ad %s" --date=iso-strict
git ls-files ...                 # inventario limitato per test/esami/asset/provenance
Get-Content ...                  # lettura statica dei file di protocollo, generatori e manifest
```

Da eseguire prima di qualunque claim di qualità successivo: `git diff --check` (eseguito dopo la creazione di questo documento), poi test strutturali isolati e infine una prova reale con chiave fixture protetta. In questo G0 **non è stato eseguito alcun test di prodotto** e non va dichiarato alcun pass.

## Piano per fixture sigillate

1. Definire un ID/versione stabile per ogni esame e una fonte di verità esterna al repository con una riga per domanda: numero, lettera corretta, fonte, spiegazione e hash della domanda normalizzata.
2. Conservare chiavi, expected score e fixture di riferimento in un percorso protetto non pubblicabile; nel repository lasciare solo schema, metadati non sensibili e hash di bundle, se approvato dal coordinatore.
3. Generare le domande con seed dichiarato e registrare seed, commit sorgente, hash del file pubblico, numero di domande e numero di opzioni. Bloccare i generatori che usano destinazioni assolute o output impliciti.
4. Aggiungere un controllo di non esposizione: nessun campo `lettera`, `risposta_corretta`, spiegazione, marker di correttezza o testo della chiave nel file pubblico; il controllo deve distinguere header legittimi da leakage reale.
5. Preparare casi protetti minimi: tutte corrette, una errata, una mancante, input duplicato/malformato, domanda legacy e domanda A-D. Verificare punteggio, verbale e mancata mutazione del corpus.
6. Verificare la provenance degli asset con manifest per fonte: autore/ente, URL, versione o snapshot, licenza, attribuzione, share-alike/derivati, note dati personali, stato legale, hash e path raw/parsed.
7. Eseguire il correttore in una directory temporanea controllata, con output candidato separato dal corpus; registrare comando, runtime, commit, fixture hash e risultato. Solo dopo revisione coordinatore si può parlare di pass.

## Residui e fonti

- `UNIVERSITA_EDILIZIA/ESAMI/AUDIT_CONTENT_LOCKED.md` è un audit storico (data 2026-10-02) e riporta 73 esami / 16.388 domande; il conteggio strutturale corrente sopra riportato non coincide e richiede riconciliazione.
- Non è stata verificata l'esistenza della directory esterna `ESAMI_RISPOSTE/`; la sua assenza dal repository è prevista dal protocollo, ma senza di essa il correttore non è collaudabile.
- Non sono stati eseguiti generatori: potrebbero scrivere fuori dal checkout o sovrascrivere artefatti; nessuna loro riproducibilità è stata certificata.
- Non è stata fatta verifica semantica delle risposte, correttezza normativa, validità legale delle licenze o conformità geometrica CAD.
- La scansione è stata interrotta su richiesta dopo l'inventario statico iniziale; il report è quindi un G0 di evidenza, non un collaudo completo.

