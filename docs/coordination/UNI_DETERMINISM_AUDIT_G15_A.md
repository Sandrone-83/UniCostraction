# UniCostraction — audit deterministico e integrità G15-A

G15-A riesegue G10-A, G11-A, G12-A, G13-A e G14-A in una directory temporanea.
Confronta gli output rigenerati con gli artefatti pubblicati tramite hash SHA-256,
contenuto JSON e guide generate, poi verifica le invarianti operative:

- conteggi file/unità e classificazioni G10-A;
- candidate pair, componenti connesse, unità e ranking G11-A;
- componenti pending/decise e decisioni null G12-A;
- cluster, lotti e copertura del packet G13-A;
- conteggi e stati `open`, `in_review`, `decided` G14-A.

Il comando non scrive negli artefatti G10-A–G14-A e non modifica card o esami.
Per default produce il report su stdout; `--output` è opzionale e viene rifiutato
se punta a un artefatto protetto.

```powershell
python tools/uni_determinism_audit_g15_a.py --root .
python tools/uni_determinism_audit_g15_a.py --root . --output $env:TEMP\uni-g15.json
```

Exit code `0` significa che hash, JSON, guide, invarianti e integrità dei file
sono invariati. Exit code `1` segnala il drift con categorie esplicite nel campo
`drift`; il report G15 non costituisce approvazione didattica, normativa, legale o
di licenza.
