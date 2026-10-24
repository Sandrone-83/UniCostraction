# -*- coding: utf-8 -*-
# Giro AF (2026-10-24): aggiorna la nota LdB 2027 della scheda detrazioni con il
# capitolo «casa» della manovra 2027 ricostruito da idealista.it del 22/10/2026.
import json, io

P = r'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'
rows = [json.loads(l) for l in open(P, encoding='utf-8') if l.strip()]

target = 5  # riga 6 (0-based 5): «Le detrazioni fiscali per l'edilizia: il sistema e i suoi limiti»
s = rows[target]
assert 'detrazioni fiscali' in s['nome'], s['nome']
assert '31/12/2025' in s['normative'], 'ancora non trovata'

OLD_TAIL = 'si ricorda inoltre che il Bonus Barriere Architettoniche 75% si e\' fermato alle spese sostenute entro il 31/12/2025.'
NEW_TAIL = OLD_TAIL + (
    " Aggiornamento 24/10/2026 (manovra 2027, capitolo «casa», da stampa di settore: NON approvato): "
    "il pacchetto casa allo studio nella Legge di Bilancio 2027 vale circa 1 miliardo; il capitolo "
    "«detrazioni per i lavori in casa» e' stimato in 550 milioni e punterebbe a PROROGARE l'assetto "
    "vigente nel 2026 (50% abitazione principale / 36% altri casi, limite 96.000 euro) oltre il 2026 — "
    "in assenza di interventi dal 2027 scatterebbe il calo gia' legislativamente previsto (36%/30%) — "
    "confermando anche il bonus mobili (circa 500 milioni la proroga, circa 50 milioni/anno il "
    "ripristino del vecchio Ecobonus 65% per pompe di calore, sistemi ibridi e cappotti termici); "
    "sul Conto Termico si studia un potenziamento a 700-800 milioni con copertura a parte in "
    "extradeficit (flessibilita' UE). Tutte ipotesi subordinate alle coperture e all'iter "
    "parlamentare (approvazione entro il 31/12/2026): NON inserirle nei preventivi come benefici "
    "certi finche' non convertite in legge; verificare il testo definitivo in GU."
)
assert OLD_TAIL in s['normative']
s['normative'] = s['normative'].replace(OLD_TAIL, NEW_TAIL)

out = io.open(P, 'w', encoding='utf-8', newline='\n')
for r in rows:
    out.write(json.dumps(r, ensure_ascii=False) + '\n')
out.close()

# verifica
check = [json.loads(l) for l in open(P, encoding='utf-8') if l.strip()]
assert len(check) == len(rows)
assert 'PROROGARE' in check[target]['normative']
print('OK: scheda', target + 1, 'aggiornata;', len(check), 'righe, JSON valido')
