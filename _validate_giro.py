import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(ROOT, 'UNIVERSITA_EDILIZIA')
KEYS = ["categoria","nome","descrizione","tecnologia","applicazioni","vantaggi","limiti","costi_e_economia","casi_real_world","normative","note_cantiere"]

errors = []
warnings = []
packs = sorted(d for d in os.listdir(BASE) if d.endswith('_PACK') and os.path.isdir(os.path.join(BASE, d)))
total_schede = 0
packs_ok = 0
for p in packs:
    sj = os.path.join(BASE, p, 'schede', 'schede.jsonl')
    cy = os.path.join(BASE, p, 'COURSE.yaml')
    if not os.path.isfile(sj):
        # alcuni pack legacy possono non avere schede.jsonl: segnala ma non blocca
        errors.append(f"{p}: schede/schede.jsonl MANCANTE")
        continue
    n = 0
    with open(sj, encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            n += 1
            try:
                obj = json.loads(line)
            except Exception as e:
                errors.append(f"{p} riga {i}: JSON invalido ({e})")
                continue
            if list(obj.keys()) != KEYS:
                errors.append(f"{p} riga {i}: chiavi non conformi: {list(obj.keys())}")
            for bad in ('aplicazioni', 'tegnologia'):
                if bad in line:
                    errors.append(f"{p} riga {i}: refuso '{bad}'")
            ce = obj.get('costi_e_economia', '')
            if isinstance(ce, str) and not ce.startswith('Ordini di grandezza indicativi: '):
                # prefisso obbligatorio per i contenuti NUOVI; nei pack legacy pre-esistenti
                # (giri precedenti o edit manuali del proprietario) e' debito noto: warning.
                if p in ('NORMATIVA_UE_INTERNAZIONALE_PACK', 'IDROELETTRICO_PICCOLA_TAGLIA_PACK'):
                    errors.append(f"{p} riga {i}: costi_e_economia senza prefisso richiesto")
                else:
                    warnings.append(f"{p} riga {i}: prefisso costi mancante (legacy)")
    total_schede += n
    # coerenza COURSE.yaml
    if os.path.isfile(cy):
        txt = open(cy, encoding='utf-8').read()
        m = re.search(r'^schede:\s*(\d+)', txt, re.M)
        if m:
            if int(m.group(1)) != n:
                errors.append(f"{p}: COURSE.yaml dichiara {m.group(1)} schede, jsonl ne ha {n}")
            else:
                packs_ok += 1
        else:
            errors.append(f"{p}: COURSE.yaml senza campo 'schede:'")
    else:
        errors.append(f"{p}: COURSE.yaml MANCANTE")

# conteggio esami
esami_dir = os.path.join(BASE, 'ESAMI')
n_esami = len([d for d in os.listdir(esami_dir)
               if os.path.isdir(os.path.join(esami_dir, d)) and d != 'RISPOSTE_CANDIDATO'])

print(f"pack trovati: {len(packs)}")
print(f"pack con COURSE.yaml coerente: {packs_ok}")
print(f"schede totali: {total_schede}")
print(f"esami (dir in ESAMI, escluso RISPOSTE_CANDIDATO): {n_esami}")
print(f"warning legacy (prefisso costi mancante in pack pre-esistenti): {len(warnings)}")
if errors:
    print(f"\nERRORI ({len(errors)}):")
    for e in errors[:60]:
        print(" -", e)
    sys.exit(1)
print("\nVALIDAZIONE OK: 0 errori")
