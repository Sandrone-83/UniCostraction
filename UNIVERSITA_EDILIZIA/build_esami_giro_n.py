# Giro N: esami per i tre corsi nuovi (aeroporti, porti, emergenze)
from build_esami_giro5 import gen

gen("AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK", "AEROPORTI", 250)
gen("PORTI_E_OPERE_MARITTIME_PACK", "PORTI_MARITTIMI", 250)
gen("EMERGENZE_E_RICOSTRUZIONE_PACK", "EMERGENZE", 250)
print("OK esami giro N")
