# Giro AH (2026-10-26): append aggiornamento CT 3.0 alla scheda 1 (riga 0)
# di ENERGETICA_INCENTIVI_PACK. Fonte: infobuildenergia.it 26/10/2026 (letto integralmente).
import json, io, sys

PATH = 'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'

APPEND = (" Aggiornamento 26/10/2026 (infobuildenergia.it, letto integralmente): "
"l'intesa della Conferenza Unificata del 22/10/2026 e' registrata come Repertorio atti n. 144/CU; "
"le osservazioni delle Regioni sono espressamente NON vincolanti; il testo definitivo non e' ancora "
"pubblicato (neanche sul sito della Conferenza): contenuti da confermare sul decreto in GU. "
"Iter documentato: trasmissione 6/8/2026, osservazioni Regioni 17/9, ANCI 5/10, nuova versione MASE "
"19/10 con controdeduzioni, parere del Coordinamento 20/10. Dettagli tecnici dello schema: "
"schermature solari con range del fattore solare gtot del Prospetto 1 della UNI/TR 12003 "
"(calcolo secondo UNI EN 410:2011) al posto delle classi 3-4 della UNI EN 14501; "
"illuminazione con verifiche fotometriche di laboratori accreditati ISO/IEC 17025 e rinvii a "
"Reg. UE 2024/1781 e Reg. UE 2017/1369 e idoneita' BACS; biomasse: soppressione del requisito di "
"rendimento >85% (Regioni contrarie); comma 8 art. 3: possibile quota del plafond destinata ad aste "
"per grandi impianti FER termici. Richieste delle Regioni: riserve di 400 M€ per categoria, minimo "
"200 M€ per le prenotazioni PA, eliminazione del comma 8, incentivo al 100% per un intervento annuo "
"dei piccoli Comuni, eliminazione della soglia dei 50.000 euro per il pagamento in unica soluzione. "
"Regime vigente fino alla pubblicazione in GU: D.M. 7/8/2025 + Regole Applicative GSE 19/12/2025 + "
"D.D. MASE 72/2026 (plafond 450+450 M€, di cui 150 M€ imprese dentro la quota privati), "
"Portaltermico in solo accesso diretto dal 13/4/2026 (FAQ KB0017802: proroga 40 giorni).")

with io.open(PATH, encoding='utf-8') as f:
    lines = f.read().split('\n')

rows = [json.loads(l) for l in lines if l.strip()]
r0 = rows[0]
old = r0['normative']
assert old.endswith("generatori a biomassa (parametri di particolato)."), "ancora non trovata: " + repr(old[-120:])
assert "Repertorio atti n. 144/CU" not in old, "aggiornamento gia' presente"
r0['normative'] = old + APPEND

with io.open(PATH, 'w', encoding='utf-8', newline='\n') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

print("OK: normative riga 0 aggiornato,", len(old), "->", len(r0['normative']), "caratteri;", len(rows), "righe totali")
