# EVOLUCIÓN — miu-semilla-latente-mt99s6np-2

Registro de cambios entre versiones de la semilla, con motivo.
Verificación independiente (Track 3), 2026-11-07 ~01:05 -05.

## v1 → v2 (2026-11-07 ~01:05 -05): el "sin semilla" no era sin semilla

**Defecto encontrado al re-correr el script dos veces como procesos
separados:**

```
$ python3 gossip_phi4_repro.py   # proceso 1
sin semilla: 2869.6818 / 2868.4741 (varía: True)
$ python3 gossip_phi4_repro.py   # proceso 2
sin semilla: 2869.6818 / 2868.4741 (varía: True)
```

Los dos valores "sin semilla" eran **idénticos en cada ejecución**.
Causa: `main()` llamaba `construir_nodos(semilla=42)` en su sección 1,
y `random.seed(42)` re-sembraba el RNG global del proceso. Los dos
sorteos de la sección 2 no tenían semilla propia, pero descendían
deterministamente del estado dejado por la semilla 42: variaban entre
sí dentro de una corrida, pero no entre corridas. El original
`global-mind-gossip-phi4.py` sí varía entre procesos (comprobado:
2869.6545… vs 2870.0378… en dos ejecuciones frescas), así que la copia
de la semilla demostraba lo contrario de lo que afirmaba el README
("varía").

El mismo defecto debilitaba `test_sin_semilla_varia`: los tests corren
en orden alfabético y `test_es_media_ponderada_no_integracion` llama
antes a `construir_nodos(semilla=42)`, así que el test solo probaba dos
puntos distintos de un flujo determinista, no variación sin semilla.

**Cambios:**

- `gossip_phi4_repro.py`, `main()` sección 2: `random.seed()` sin
  argumentos (re-siembra desde entropía del SO) antes de los sorteos
  sin semilla, con comentario que explica por qué es obligatorio.
- `test_gossip_phi4.py`:
  - `test_sin_semilla_varia`: `random.seed()` antes de cada sorteo.
  - Nuevo `test_sin_semilla_varia_entre_procesos`: ejecuta el script
    dos veces como subprocesos y exige pares "sin semilla" distintos —
    regresión directa del defecto.
- La reproducción decisiva no cambia: `seed(42)` sigue dando
  2869.460517705751 dígito a dígito, y ningún número citado en README
  o HUESO_GLOBAL_MIND.md se tocó (los valores 2869.4520 / 2869.3445 /
  2869.6743 son de SUELOS_FERTILES.md §5, fuente citada, no salidas de
  este script).

**Resultado tras el cambio:** 7/7 tests OK; el script imprime pares
"sin semilla" distintos en cada ejecución.

---
ρ(x) > 0. Zvvvvv.
