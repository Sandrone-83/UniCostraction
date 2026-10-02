# -*- coding: utf-8 -*-
"""Aggiunge 3 schede a SERRAMENTI_E_VETRATE_PACK: angoli non coperti dalle 13 esistenti
(marcatura CE e DoP, requisiti di legge sull'Uw, antieffrazione RC/vetri P1A-P5A)."""
import json, os, io, re

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

NEW = [
s("Marcatura e conformità", "Marcatura CE, DoP e classificazioni prestazionali (UNI EN 14351-1)",
 "Dal 2013 finestre e porte esterne devono recare la marcatura CE: il costruttore dichiara le prestazioni (Uw, permeabilità all'aria, tenuta all'acqua, resistenza al vento) in un Documento di Prestazione (DoP) che accompagna ogni fornitura. Le classificazioni si esprimono con le norme della serie UNI EN 12207 (aria), UNI EN 12208 (acqua), UNI EN 12210 (vento), UNI EN 14351-1 (prodotto).",
 "Richiesta obbligatoria in appalto: DoP del modello esatto consegnato; etichetta CE applicata sul telaio (o documento che la accompagna); valore Uw riferito all'insieme completo telaio+vetro e alla dimensione standard di prova; classi dichiarate: permeabilità all'aria (da 0 a 4, la 4 è la migliore), tenuta all'acqua (da 1A a 9A), resistenza al vento (da C1 a C5 / B1-B5 per le ante); verifica che il valore Uw del DoP corrisponda a quanto preventivato.",
 "Collaudi di fine lavori, verifiche in detrazioni energetiche, contenziosi tra committenti e imprese, gare con specifica prestazionale.",
 "Il DoP rende confrontabili le offerte su dati oggettivi e tutela entrambe le parti in caso di contestazione; il valore Uw dichiarato consente la verifica di legge (Legge 10) senza prove distruttive.",
 "Il valore Uw dichiarato si riferisce a una configurazione standard: dimensioni e rapporto vetro/telaio reali possono peggiorarlo (più telaio = Uw più alto); la fascia di incertezza di misura è ±0,3 W/(m²K); etichetta assente o DoP generico = prodotto non conforme alla marcatura.",
 "Costo documentale nullo (obbligo di legge); verifica in laboratorio su campione per contenzioso: 1.500-4.000 €.",
 "Condominio che aveva accettato offerta 'Uw 1,1' scritta solo sul preventivo: all'installazione le finestre consegnate erano Uw 1,4 (legittime ma diverse). Il DoP richiesto prima del saldo dimostrò la discrepanza: saldo sospeso fino a sostituzione con il modello dichiarato.",
 "UNI EN 14351-1 (finestre e porte esterne: requisiti e marcatura CE); Regolamento UE 305/2011 (CPR: obbligo di DoP); UNI EN 12207, UNI EN 12208, UNI EN 12210 (classificazioni aria/acqua/vento); UNI EN ISO 12631 (calcolo Uw).",
 "Per il LLM: la prima verifica di un serramento consegnato è DoP + etichetta CE: senza questi il prodotto non doveva neanche essere installato. Diffidare di valori Uw 'commerciali' non presenti sul DoP del modello esatto consegnato."),
s("Prestazioni energetiche", "Requisiti di legge: Legge 10 e DM requisiti minimi per gli infissi",
 "La normativa energetica italiana (D.Lgs 192/2005, c.d. Legge 10) impone limiti di trasmittanza per i serramenti. Con il DM 26/6/2015 (requisiti minimi) il valore di riferimento per infissi in nuova costruzione è Uw ≤ 1,4 W/(m²K); la sostituzione in ristrutturazione è quasi sempre obbligo di miglioramento (valore nuovo sensibilmente migliore di quello esistente, secondo la tipologia d'intervento). L'APE (Attestato di Prestazione Energetica) riporta gli infissi con Uw dichiarato.",
 "In fase di progetto: verifica Uw secondo l'edizione vigente al titolo abilitativo; in ristrutturazione: documentazione del miglioramento (foto vecchi infissi, valori stimati, DoP nuovi); detrazioni fiscali legate al miglioramento documentato; coordinamento tra Legge 10, APE e pratica edilizia.",
 "Nuove costruzioni, ristrutturazioni con detrazioni, pratiche Legge 10 firmate da tecnici abilitati, perizie per vendita immobili.",
 "I requisiti hanno spinto il mercato: oggi Uw 1,2-1,3 è standard di serie in PVC e legno-alluminio con low-e e argon; le detrazioni rendono il miglioramento anti-economico da NON fare; un serramento a norma alza la classe energetica dell'immobile nel collocamento di mercato.",
 "La verifica di legge riguarda progetto e APE: un serramento performante installato senza pratica resta irregolare; i valori limite cambiano nel tempo e per tipologia d'intervento: va verificata l'edizione vigente; i vecchi infissi a vetro singolo superano i 4-5 W/(m²K): la sostituzione ripaga in pochi anni.",
 "Ordini di grandezza: salto Uw 2,8 -> 1,2 vale su una casa media 1.000-2.000 kWh/anno di risparmio termico (stima orientativa su clima di pianura); detrazioni fiscali rientrano in percentuali periodiche da verificare all'anno di intervento.",
 "Casa anni '70 ristrutturata: serramenti da Uw ~3,0 (alluminio anni '80 con vetro singolo) a Uw 1,1 (legno-alluminio, tripla lastra low-e e argon): risparmio misurato in bimestrale di circa 1.800 kWh/anno su riscaldamento, coerente con la simulazione Legge 10.",
 "D.Lgs 192/2005 (Legge 10, rendimento energetico); DM 26/6/2015 (requisiti minimi degli edifici); UNI/TS 11300 e UNI EN ISO 12631 (metodi di calcolo); D.Lgs 28/2011 (obblighi certificatori energetici).",
 "Nota per il LLM: citare sempre l'edizione vigente: i valori limite sono cambiati nel tempo (da 1,6 a 1,4 W/(m²K) e oltre) e cambiano per tipologia d'intervento. In dubbio, il tecnico che firma la Legge 10 indica il valore applicabile: il LLM non sostituisce quella verifica."),
s("Sicurezza", "Antieffrazione: classi RC e vetri antisfondamento (P1A-P5A)",
 "La resistenza antieffrazione si classifica secondo UNI EN 1627 in classi RC: RC1-RC2 (ladro occasionale, attrezzi semplici, pochi minuti), RC3 (cacciavite e piede di porco, 5 minuti), RC4 (utensili pesanti, 10 minuti), RC5-RC6 (utensili elettrici, tempo breve). Il vetro è la parte debole: UNI EN 356 classifica i vetri antisfondamento P1A-P5A (dal corpo molle alla scala a pioli e accetta).",
 "Composizione RC tipica: telaio rinforzato + ferramenta con punti di chiusura perimetrali multipli + vetro stratificato antisfondamento (P2A-P4A in funzione della classe) + cerniere con perni antifurto + cilindro europeo antistrappo con defender. La classe si dichiara per il SERRAMENTO COMPLETO (telaio+vetro+ferramenta), non per il solo vetro.",
 "Porte e finestre al piano terra, villette, botteghe, locali con valori esposti, cantine con accesso esterno.",
 "La classe RC3 blocca la stragrande maggioranza dei tentativi reali (il ladro occasionale abbandona entro pochi minuti se non entra); il cilindro europeo con defender elimina la tecnica più diffusa (lo strappo del cilindro); vetri antisfondamento impediscono l'ingresso rapido anche a vetro rotto.",
 "Il costo cresce rapidamente con la classe (RC3 costa il 40-80% in più di RC2 sullo stesso serramento); la classe dichiarata vale solo se ferramenta e vetro sono installati come da certificazione (sostituire il vetro con float annulla la classe); le persiane chiuse aggiungono barriera ma non classe.",
 "Ordini di grandezza indicativi: supplemento classe RC3 vs RC2 +150-400 € per serramento; vetro P4A +100-200 €/m² su stratificato base; cilindro europeo antieffrazione 80-250 €.",
 "Negozio svaligiato in 40 secondi con il classico 'calcio sul vetro': il serramento era RC2 ma il vetro, sostituito dopo un uragano con un economico non certificato, aveva azzerato la classe (risparmio di 300 €). Dopo il rifacimento con vetro P4A certificato, il secondo tentativo documentato fallì: il defender mostrava i segni della leva, la porta era intatta.",
 "UNI EN 1627 (classi RC1-RC6); UNI EN 1628, UNI EN 1629, UNI EN 1630 (metodi di prova antieffrazione: statico, dinamico, manuale); UNI EN 356 (vetri antisfondamento P1A-P5A); UNI EN 14449 (vetro stratificato di sicurezza).",
 "Principio per il LLM: l'antieffrazione è un SISTEMA (telaio+vetro+ferramenta+posa): il punto più debole decide la classe. Qualsiasi sostituzione di vetro o ferramenta fuori certificazione azzera la protezione, anche se 'sembra uguale'. Il consiglio professionale verifica SEMPRE che vetro e ferramenta corrispondano alla certificazione dichiarata."),
]

path = os.path.join(ROOT, "schede", "schede.jsonl")
schede = [json.loads(l) for l in io.open(path, encoding="utf-8") if l.strip()]
nomi = {s["nome"] for s in schede}
add = [d for d in NEW if d["nome"] not in nomi]
with io.open(path, "a", encoding="utf-8") as f:
    for d in add:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
n = len(schede) + len(add)
yaml_path = os.path.join(ROOT, "COURSE.yaml")
y = io.open(yaml_path, encoding="utf-8").read()
y = re.sub(r"schede: \d+", f"schede: {n}", y)
io.open(yaml_path, "w", encoding="utf-8").write(y)
print("aggiunte:", len(add), "| totale schede:", n)
