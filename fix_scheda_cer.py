import json, io

p = r'UNIVERSITA_EDILIZIA/FOTOVOLTAICO_CAMPI_AGRIVOLTAICO_CER_PACK/schede/schede.jsonl'
rows = [json.loads(l) for l in open(p, encoding='utf-8').read().splitlines() if l.strip()]
r = rows[11]
assert 'incentivi delle CER' in r['nome'], r['nome']

OLD_T = ("CHIUSO a nuove domande dal 30/11/2025 (accordi di finanziamento entro il 30/6/2026, "
         "erogazione entro il 31/8/2026): resta pienamente attiva la tariffa incentivante, "
         "che non ha scadenza a bando;")
NEW_T = ("CHIUSO a nuove domande: risorse esaurite gia' il 21/11/2025 al raggiungimento della soglia "
         "di 795,5 milioni di euro comunicata dal MASE (il termine ordinario era il 30/11/2025); "
         "con il DL 19/2026, art. 27, gli accordi di concessione andavano firmati entro il 30/6/2026 "
         "e la realizzazione degli impianti e' ammessa entro 24 mesi dall'accordo, con limite "
         "invalicabile al 31/12/2027, con il GSE quale soggetto attuatore unico; resta pienamente "
         "attiva la tariffa incentivante, ammessa a sportello entro il contingente complessivo di "
         "5 GW di potenza e comunque non oltre il 31/12/2027;")
assert OLD_T in r['tecnologia'], 'pattern tecnologia non trovato'
r['tecnologia'] = r['tecnologia'].replace(OLD_T, NEW_T)

OLD_N = "DL 19 febbraio 2026 n. 19 art. 27 (programmi facility CACER)."
NEW_N = "DL 19/2026, art. 27 (programmi facility CACER), convertito con L. 50/2026."
assert OLD_N in r['normative'], 'pattern normative non trovato'
r['normative'] = r['normative'].replace(OLD_N, NEW_N)

out = io.open(p, 'w', encoding='utf-8', newline='\n')
for row in rows:
    out.write(json.dumps(row, ensure_ascii=False) + '\n')
out.close()

rows2 = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
assert len(rows2) == 15
print('OK: scheda 11 aggiornata, JSON valido, 15 righe')
t = rows2[11]['tecnologia']
i = t.find('contributo PNRR')
print()
print(t[i:i+760])
print()
print('NORM:', rows2[11]['normative'])
