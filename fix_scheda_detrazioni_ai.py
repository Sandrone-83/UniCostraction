# Giro AI (2026-10-27): append nota DPB 2027 alla scheda detrazioni (riga 5)
# di ENERGETICA_INCENTIVI_PACK. Fonti: pgcasa.it 16/10/2026, edilportale.com 16/10/2026,
# pmi.it 14/10/2026, bibilus.acca.it 5/10/2026 (verifica web 27/10/2026).
import json, io

PATH = 'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'

APPEND = (" Aggiornamento 27/10/2026: il Documento Programmatico di Bilancio 2027, inviato a "
"Bruxelles il 15/10/2026, NON cita bonus ristrutturazione, Ecobonus e Sismabonus (fonti: "
"pgcasa.it e edilportale.com, 16/10/2026); al 27/10/2026 il testo del Ddl di Bilancio 2027 non "
"risulta ancora pubblicato (atteso in Parlamento nella seconda meta' di ottobre): la partita si "
"gioca nel Ddl e nei suoi emendamenti. Baseline di legge invariata e confermata: dal 2027 aliquote "
"36% (abitazione principale) / 30% (altri immobili) con massimale 96.000 euro, dal 2028 massimale "
"48.000 euro e aliquota 30%. Restano ipotesi di stampa, NON approvate: proroga 50%/36%, bonus "
"mobili, Ecobonus 65% per l'abitazione principale (proposta Confartigianato 1/10/2026 con apertura "
"del viceministro Leo; ipotesi di copertura nella flessibilita' UE per la transizione energetica, "
"dopo il via libera di Bruxelles alla clausola di salvaguardia, circa 29 miliardi secondo pmi.it "
"del 14/10/2026).")

with io.open(PATH, encoding='utf-8') as f:
    lines = f.read().split('\n')

rows = [json.loads(l) for l in lines if l.strip()]
r = rows[5]
old = r['normative']
assert old.endswith('verificare il testo definitivo in GU.'), 'ancora non trovata: ' + repr(old[-120:])
assert 'Documento Programmatico di Bilancio 2027' not in old, 'aggiornamento gia presente'
r['normative'] = old + APPEND

with io.open(PATH, 'w', encoding='utf-8', newline='\n') as f:
    for row in rows:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')

print('OK: riga 5 aggiornata,', len(old), '->', len(r['normative']), 'caratteri;', len(rows), 'righe totali')
