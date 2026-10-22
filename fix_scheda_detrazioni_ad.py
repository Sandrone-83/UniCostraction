import json, io

p = r'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'
rows = [json.loads(l) for l in open(p, encoding='utf-8').read().splitlines() if l.strip()]
r = rows[5]
assert r['nome'].startswith('Le detrazioni fiscali'), r['nome']

OLD = ("la Legge di Bilancio 2027 (in discussione ottobre-dicembre 2026) puo' modificare aliquote e limiti "
       "dal 2027: verificare il testo definitivo prima dell'applicazione.")
NEW = ("la Legge di Bilancio 2027 (in discussione ottobre-dicembre 2026) puo' modificare aliquote e limiti "
       "dal 2027: verificare il testo definitivo prima dell'applicazione. In discussione anche l'ipotesi di un "
       "Ecobonus rafforzato al 65% per l'abitazione principale nell'ambito della flessibilita' UE per la "
       "sicurezza energetica (COM(2026) 553 dell'8/10/2026, ~14,4 miliardi per l'energia nel 2027-2028): "
       "ipotesi NON operativa, da non inserire nei preventivi come beneficio certo finche' non convertita in legge; "
       "si ricorda inoltre che il Bonus Barriere Architettoniche 75% si e' fermato alle spese sostenute entro il 31/12/2025.")
assert OLD in r['normative'], 'pattern non trovato'
r['normative'] = r['normative'].replace(OLD, NEW)

out = io.open(p, 'w', encoding='utf-8', newline='\n')
for row in rows:
    out.write(json.dumps(row, ensure_ascii=False) + '\n')
out.close()

rows2 = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
assert len(rows2) == 18
print('OK: scheda 5 aggiornata, JSON valido, 18 righe')
print()
print(rows2[5]['normative'][-420:])
