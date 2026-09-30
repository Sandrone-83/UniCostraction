# MATERIALEDILE_PACK — Materiale da costruzione per training LLM

Pacchetto di conoscenza strutturata sui **materiali da costruzione**, dal
fissaggio alla struttura portante, per l'addestramento/fine-tuning di un LLM
specializzato in edilizia (es. Auratrix).

## Contenuto

- `schede/materiale_edile_schede.jsonl` — una scheda per riga, in JSON.
- `tabelle_prezzi.md` — tabelle riepilogative per categoria (nome, uso tipico, costo indicativo).

## Numero schede per categoria

- **Fissaggi**: 10 schede
- **Leganti e malte**: 12 schede
- **Calcestruzzi**: 7 schede
- **Laterizi e blocchi**: 8 schede
- **Metalli**: 11 schede
- **Legno e derivati**: 8 schede
- **Isolanti**: 10 schede
- **Isolanti acustici**: 3 schede
- **Impermeabilizzanti**: 9 schede
- **Pitture e finiture**: 12 schede
- **Pavimenti**: 11 schede
- **Rivestimenti**: 4 schede
- **Cartongesso e sistemi a secco**: 7 schede
- **Idraulica**: 10 schede
- **Elettrico**: 8 schede
- **Coperture**: 6 schede
- **Serramenti**: 7 schede
- **Stradali**: 4 schede
- **Geotecnica**: 4 schede
- **Speciali**: 7 schede
- **Chimici di cantiere**: 4 schede

Totale: **162 schede**.

## Schema dei campi (ogni scheda)

| Campo | Significato |
| --- | --- |
| id | Identificativo univoco MAT-XXX |
| categoria | Categoria merceologica |
| nome | Nome del materiale |
| tipo | Famiglia/tecnologia del prodotto |
| descrizione | Descrizione sintetica |
| composizione | Di cosa è fatto |
| proprieta | Caratteristiche funzionali chiave |
| tipologie | Principali varianti di mercato |
| quando_usarlo | Casi d'uso corretti |
| posa_applicazione | Come si mette in opera |
| costo_indicativo | Fascia di prezzo orientativa 2025 |
| normativa_riferimento | Norme EN/UNI di riferimento |
| vantaggi | Punti di forza |
| limiti | Punti di debolezza / attenzioni |
| abbinamenti | Materiali con cui lavora bene |
| note_cantiere | Suggerimenti pratici da cantiere |

## Uso per il training

- Ideale per: fine-tuning supervisionato, RAG (una scheda = un documento),
  generazione di quiz, valutazione del modello su costi e scelte materiali.
- I campi `quando_usarlo`, `vantaggi`, `limiti`, `abbinamenti` sono pensati
  per insegnare al modello **lo spirito critico** nella scelta dei materiali.

## ⚠️ Disclaimer sui prezzi

I valori in `costo_indicativo` sono **fasce orientative al 2025** espresse in
euro con la relativa unità di misura. Non sono quotazioni di mercato:
aggiornarle periodicamente con listini di produttori e rivenditori prima di
usarle in produzione.
