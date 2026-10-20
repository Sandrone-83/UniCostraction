import json, io

p = r'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'
lines = open(p, encoding='utf-8').read().splitlines()
rows = [json.loads(l) for l in lines if l.strip()]
r = rows[5]
assert r['nome'].startswith('Le detrazioni fiscali'), r['nome']

OLD_TEC = ("restano agevolabili la nuova installazione (non in sostituzione), "
           "i sistemi ibridi di fabbrica caldaia+pompa di calore (requisiti del D.M. 6/8/2020), "
           "i microcogeneratori, le caldaie a biomasse e le pompe di calore ad assorbimento a gas;")
NEW_TEC = ("secondo l'interpretazione di settore basata sulla definizione EPBD di 'installazione' "
           "(che include acquisto, assemblaggio e messa in funzione), l'esclusione si estende anche "
           "alla NUOVA installazione di caldaia unica a condensazione a combustibile fossile: "
           "interpretazione in evoluzione, verificare la prassi AdE vigente prima di applicarla al caso concreto; "
           "restano agevolabili i sistemi ibridi di fabbrica caldaia+pompa di calore (requisiti del D.M. 6/8/2020), "
           "i microcogeneratori, le caldaie a biomasse e le pompe di calore ad assorbimento a gas;")
assert OLD_TEC in r['tecnologia'], 'pattern tecnologia non trovato'
r['tecnologia'] = r['tecnologia'].replace(OLD_TEC, NEW_TEC)

OLD_NORM = ("TUIR art. 16-bis; L. 199/2025 (Legge di Bilancio 2026); Circolare Agenzia delle Entrate 8/E del 19 giugno 2025; "
            "prassi ENEA per le piattaforme delle detrazioni energetiche (versione vigente).")
NEW_NORM = ("TUIR art. 16-bis; L. 199/2025 (Legge di Bilancio 2026); Circolare Agenzia delle Entrate 8/E del 19 giugno 2025; "
            "prassi ENEA per le piattaforme delle detrazioni energetiche (versione vigente). "
            "NOTA DI AGGIORNAMENTO (verifica ottobre 2026): dal 1/1/2027 il TUIR (DPR 917/1986) e' sostituito dal nuovo "
            "Testo Unico delle imposte sui redditi, D.Lgs 19 giugno 2026 n. 117 (GU n. 152 del 3/7/2026, in vigore dal 4/7/2026, "
            "applicazione dal 1/1/2027), che ricolloca le disposizioni sui bonus edilizi: aggiornare i riferimenti alla numerazione "
            "vigente dal 2027; la Legge di Bilancio 2027 (in discussione ottobre-dicembre 2026) puo' modificare aliquote e limiti "
            "dal 2027: verificare il testo definitivo prima dell'applicazione.")
assert OLD_NORM == r['normative'], 'normative non coincide'
r['normative'] = NEW_NORM

out = io.open(p, 'w', encoding='utf-8', newline='\n')
for row in rows:
    out.write(json.dumps(row, ensure_ascii=False) + '\n')
out.close()

# re-validate
rows2 = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
assert len(rows2) == 18
print('OK: scheda 5 aggiornata, JSON valido, 18 righe')
print()
print('--- tecnologia (estratto caldaie) ---')
t = rows2[5]['tecnologia']
i = t.find('ESCLUSIONE')
print(t[i:i+700])
print()
print('--- normative ---')
print(rows2[5]['normative'])
