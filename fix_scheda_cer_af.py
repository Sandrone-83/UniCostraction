# -*- coding: utf-8 -*-
# Giro AF (2026-10-24): nota fiscale IVA sulle trattenute CER (Risposta AdE n. 22/2026,
# da stampa di settore: marcata da verificare sul testo ufficiale).
import json, io

P = r'UNIVERSITA_EDILIZIA/FOTOVOLTAICO_CAMPI_AGRIVOLTAICO_CER_PACK/schede/schede.jsonl'
rows = [json.loads(l) for l in open(P, encoding='utf-8') if l.strip()]

target = 11  # riga 12 (0-based 11): «Gli incentivi delle CER...»
s = rows[target]
assert 'incentivi delle CER' in s['nome'], s['nome']
assert 'L. 50/2026' in s['normative'], 'ancora non trovata'

OLD = 'DL 19/2026, art. 27 (programmi facility CACER), convertito con L. 50/2026.'
NEW = OLD + (
    " Fiscalita': secondo la Risposta n. 22/2026 dell'Agenzia delle Entrate (riportata dalla stampa "
    "di settore a ottobre 2026; verificare il testo ufficiale su agenziaentrate.gov.it), le somme "
    "che la CER trattiene dagli incentivi GSE per i costi di gestione non costituirebbero "
    "corrispettivi di servizio e resterebbero fuori campo IVA."
)
assert OLD in s['normative']
s['normative'] = s['normative'].replace(OLD, NEW)

out = io.open(P, 'w', encoding='utf-8', newline='\n')
for r in rows:
    out.write(json.dumps(r, ensure_ascii=False) + '\n')
out.close()

check = [json.loads(l) for l in open(P, encoding='utf-8') if l.strip()]
assert len(check) == len(rows)
assert '22/2026' in check[target]['normative']
print('OK: scheda', target + 1, 'aggiornata;', len(check), 'righe, JSON valido')
