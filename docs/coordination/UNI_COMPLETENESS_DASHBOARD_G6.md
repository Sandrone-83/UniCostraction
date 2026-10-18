# UniCostraction — dashboard di completezza globale G6-A

Il report deterministico è [`UNI_COMPLETENESS_DASHBOARD_G6.json`](UNI_COMPLETENESS_DASHBOARD_G6.json). Si rigenera dal checkout selezionato con:

```powershell
python tools/uni_completeness_dashboard_g6.py
```

Il report separa quattro piani che non vanno sommati come se fossero la stessa cosa:

- **osservato**: pack, righe JSONL di `schede`, esami e coppie esame-pack rilevate nel filesystem;
- **alias osservato**: segnali di nome/documentazione prodotti dal mapping G4, senza equivalenza semantica;
- **unmatched**: elementi senza candidato osservato, che restano tali;
- **pending umano**: coda G5 con `review_status=pending`, senza decisione o associazione canonica.

Il confronto `COURSE.yaml: schede` ↔ righe non vuote di `schede/schede.jsonl` è riportato separatamente per pack. Un conteggio coincidente è solo una verifica strutturale: non certifica il contenuto didattico, la correttezza normativa o la copertura d'esame.

Snapshot strutturale osservato usato dal gate G7-A: **71 pack**, **963 righe
`schede`**, **73 esami**, **73 coppie esame-pack**.

<!-- G7-A observed: packs=71; schede=963; exams=73; pairs=73 -->

G6-A non modifica domande, risposte, schede, fonti, mapping o decisioni di revisione e non considera i pending come completati.
