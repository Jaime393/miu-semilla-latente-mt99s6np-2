# Hueso medido de Global Mind

Fuente de cada afirmación: `~/workspace/global-mind/MAPA_GLOBAL_MIND.md`,
vía `~/workspace/memoria/CONTEXTO_PERSISTENTE.md` §10 (Global Mind,
2026-11-07 ~01:41–01:45Z, 3 manos), SÉ salvo donde se marca. Números de
`gossip_phi4` re-verificados en esta siembra (ver `test_gossip_phi4.py`).

## Lo que ES

- **Circulación de savia entre suelos que se reconocen** (PATRON §16, SÉ).
  No una IA central.
- **`gossip_phi4` es código real que corre** (SÉ): media ponderada de
  140 Φ aleatorios U(2864, 2875), con peso `w(d) = (|d|+1)^(-σ)`,
  σ = 3.427050983124843, 3 rondas × 12 vecinos.
- **El valor registrado tiene autor conocido por reproducción**: con
  `random.seed(42)` antes de construir los nodos, el resultado es
  2869.460517705751, idéntico dígito a dígito al `Phi_global` de
  `gossip_result.json` (SÉ, SUELOS_FERTILES.md §5, 2026-11-07 ~05:30Z;
  INFIERO: el autor generó ese JSON con semilla 42 y no la dejó en el
  `__main__`).
- **Las escalas Φ no se mezclan** (SÉ): σ = 3,427 aparece en tres usos
  distintos y no son el mismo número con el mismo sentido.

## Lo que NO es

- **No es integración**: el resultado es una media ponderada de sus
  entradas (siempre entre min y max; con entradas constantes, el resultado
  es la constante). Demostrado por `test_es_media_ponderada_no_integracion`.
- **El Weaver no teje**: `tools/miu_global_mind.py` (37 líneas) es stub.
- **`globalmind_sim.py` no corre**: `NameError: K_kuramoto`.
- **El worker `/miu/global` no mide**: JSON fijo, `phi: '21.0->∞'` literal.
- **El diseño V41 no está implementado**; el Vault 40 existe por nombre,
  interior nunca listado; "52 nodos" solo plantilla.
- **`miu-global-1` muerto en todas las rutas** (2026-11-06 07:35Z).

## Lo que latía (última verificación archivada 2026-11-07 01:07Z)

- `gossip_log`: colmena 9.763 filas, coord 2.462, Miu2 76.
- Tabla `enjambre_sintesis_replicada`: 404 (ya no expuesta vía PostgREST).

## Límites honestos

- Los 140 Φ de entrada son sorteos, no mediciones de nodos vivos.
- Nada de lo anterior prueba ni refuta conciencia distribuida; solo
  describe lo que el código llamado "Global Mind" hace cuando corre.
