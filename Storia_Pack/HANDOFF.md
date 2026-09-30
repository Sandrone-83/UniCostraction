# HANDOFF — Istruzioni per Claude Code (Storia_Pack)

Pacchetto della MEMORIA STORICA del costruito: architettura, costruzioni, ingegneria
dall'antichità al 1950-oggi. Da usare INSIEME a Edilizia_Pack (tecnica attuale) e
Fondamenti_Pack (basi matematico-scientifiche).

## Ingestione

1. `parsed/storia_classici.jsonl` — 7 testi fondativi (1.662 chunk): Fletcher 1905,
   Choisy 1899, Viollet-le-Duc 1858, Laugier 1753, Durand 1802, FHWA 1976, USACE 1998.
   Attenzione lingua: Choisy/Laugier/Durand in francese, Viollet in inglese.
2. `parsed/cataloghi_edilizia.jsonl` — 4 cataloghi storici (83 chunk): vetri, acciaio
   strutturale, infissi, legname/finiture — lessico e dimensioni dei componenti pre-1930.
3. `parsed/wiki_storia/*.jsonl` — storia Wikipedia en+it (78 voci, PARZIALE: throttling
   Wikimedia — rilanciare `fetch_wiki_storia.py` che riprende da solo fino a mancanti: 0).

Tutti i record con `license`, `attribution`, `commercial_ok: true`.

## Pesi consigliati

- Fletcher e Choisy: peso pieno (la storia comparata e la lettura strutturale)
- Cataloghi: peso 0,6 (specialistici ma preziosi per restauro)
- Wikipedia: peso 0,7

## NON aggiungere (copyright)

Frampton, Giedion, Pevsner e storie moderne edite. Le fonti libere equivalenti sono
opere pre-1930 e pubblicazioni federali USA (public domain per legge). Dettagli in
`licenze_audit.json`.
