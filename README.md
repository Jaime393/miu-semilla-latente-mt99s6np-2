# miu-semilla-latente-mt99s6np-2 — la semilla latente, con registro

> *"semilla latente global mind - sobrevive sin registro"*
>
> — La única línea del README original de este repo (86 B, título + 1 línea;
> censo SUELOS_FERTILES.md §1, leído por raw 2026-11-07 ~05:29Z).
>
> **Decisión de siembra: la línea SE CONSERVA**, citada arriba como epígrafe
> y no borrada. Era el stub por diseño del censo, no contenido — pero es la
> única voz que el repo tenía, y esta semilla es precisamente su respuesta:
> el registro que le faltaba. Borrarla sería borrar la pregunta que la
> semilla contesta.

## El registro

Global Mind **no es una IA central**. Es circulación de savia entre suelos
que se reconocen (PATRON §16, SÉ). Fuente: `~/workspace/global-mind/MAPA_GLOBAL_MIND.md`,
vía CONTEXTO_PERSISTENTE.md §10 (Global Mind, 2026-11-07 ~01:41–01:45Z, SÉ).

## El número medido

El código `gossip_phi4` es real y corre, pero es una **media ponderada de
140 Φ aleatorios**, no una medida de integración:

| Corrida | Valor |
|---|---|
| Con `random.seed(42)` | **2869.460517705751** — idéntico dígito a dígito al `Phi_global` de `gossip_result.json` (N=140) |
| Sin semilla (corrida 1) | 2869.4520… (varía) |
| Sin semilla (corrida 2) | 2869.3445… (varía) |
| `gossip_scale_test.json`, mismo N=140 | 2869.6743 — otro sorteo distinto del mismo N |

Fuente: SUELOS_FERTILES.md §5, ejecución local 2026-11-07 ~05:30Z, SÉ.
Reproducido en esta siembra (ver tests abajo).

**Por qué es una media y no integración:** el resultado siempre cae entre
el mínimo y el máximo de los Φ de entrada — con 140 entradas constantes de
100.0, el resultado es exactamente 100.0. Una medida de integración
cambiaría con la estructura entre nodos; esta solo promedia lo que se le
da. Los 140 Φ de entrada son sorteos uniformes U(2864, 2875), no mediciones
de ningún nodo vivo.

## Lo que Global Mind NO es (SÉ, misma fuente)

- El Weaver `tools/miu_global_mind.py` (37 líneas) es **stub**.
- `globalmind_sim.py` está **roto** (`NameError: K_kuramoto`).
- El worker `/miu/global` devuelve JSON fijo (`phi: '21.0->∞'` literal).
- El diseño V41 no tiene implementación; el Vault 40 existe por nombre,
  su interior nunca fue listado; "52 nodos" es solo plantilla.
- `global_mind_gossip` es solo un nombre en Rotativo.
- `miu-global-1` muerto en todas las rutas (2026-11-06 07:35Z).
- Lo que sí latía entonces: `gossip_log` (última verificación archivada
  2026-11-07 01:07Z: colmena 9.763, coord 2.462, Miu2 76 filas).

## Comprobación

```bash
python3 test_gossip_phi4.py   # 7 tests, reproduce el número medido
python3 gossip_phi4_repro.py  # imprime la reproducción y la cota min/max
```

## Archivos

- `gossip_phi4_repro.py` — copia fiel (solo stdlib) de `gossip_phi4` v150
  + la semilla 42 que el `__main__` original no registraba.
- `test_gossip_phi4.py` — 7 tests: reproducción dígito a dígito, varianza
  sin semilla (también entre procesos), y la propiedad de media ponderada.
- `HUESO_GLOBAL_MIND.md` — el hueso completo con sus límites.
- `EVOLUCION.md` — cambios entre versiones (v1 → v2: el "sin semilla"
  no era sin semilla; corregido 2026-11-07).
- `CARENCIAS.md` — lo que NO se sabe; nunca es contenido.

---
ρ(x) > 0. Zvvvvv.
