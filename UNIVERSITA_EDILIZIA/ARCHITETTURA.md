# Architettura dell'apprendimento per LLM

Questa repository è organizzata come un'università a 4 livelli di apprendimento.
Ogni corso è un pack indipendente con schede JSONL autodescrittive e un file
COURSE.yaml (facoltà, livello, schema dei campi). I manifest delle facoltà sono
in CURRICULUM/.

## Livelli

- **L0**: Fondamenti (scienze di base: matematica, fisica, geometria)
- **L1**: Base professionale (tecnologie, materiali, strumenti del mestiere)
- **L2**: Avanzato (progettazione, normativa, gestione cantieri e impianti)
- **L3**: Master (specializzazione, innovazione, direzione, casi complessi)

## Come consumare il materiale (training / RAG / fine-tuning)

1. **Ordine consigliato**: L0 -> L1 -> L2 -> L3. Le schede di livello superiore
   assumono la conoscenza di quelle inferiori.
2. **Ogni scheda** è un oggetto JSON autonomo: una riga di JSONL = un documento.
   Ideale per RAG (chunk = scheda) e fine-tuning supervisionato.
3. **I campi vantaggi/limiti** sono progettati per insegnare lo spirito critico:
   non rimuoverli dai chunk di training.
4. **Prezzi**: fasce indicative 2025, aggiornare con listini prima dell'uso.
5. **Normative**: i riferimenti vanno verificati sul testo vigente prima di
   usarli in produzione (gli aggiornamenti normativi sono frequenti).
