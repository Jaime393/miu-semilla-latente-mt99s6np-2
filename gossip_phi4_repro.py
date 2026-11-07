#!/usr/bin/env python3
"""Reproducción medida de gossip_phi4 — Global Mind, hueso verificado.

Copia fiel, solo-stdlib, del código `gossip_phi4` del repo
Jaime393/miu-v150-global-mind-gossip-phi4 (fuente local:
~/workspace/suelos-fertiles/miu-v150/fuente/global-mind-gossip-phi4.py),
con el único añadido de fijar la semilla que el `__main__` original no
dejaba registrada.

Hechos que reproduce (SÉ):
- Con random.seed(42) antes de construir los 140 nodos, gossip_phi4
  devuelve 2869.460517705751, idéntico dígito a dígito al Phi_global de
  gossip_result.json (SUELOS_FERTILES.md §5, verificado en dos corridas
  de la versión parcheada, 2026-11-07 ~05:30Z).
- Sin semilla, el valor varía en cada corrida (2869.4520 / 2869.3445 en
  dos corridas; gossip_scale_test.json da 2869.6743 para el mismo N=140:
  dos sorteos distintos del mismo N — SUELOS_FERTILES.md §5).
- El resultado es una MEDIA PONDERADA de los Phi de entrada: siempre cae
  entre el mínimo y el máximo de los nodos. No mide integración entre
  nodos; mide el centro de 140 sorteos uniformes U(2864, 2875)
  (CONTEXTO_PERSISTENTE.md §10, Global Mind 2026-11-07 ~01:41–01:45Z).

Uso: python3 gossip_phi4_repro.py
"""
import math
import random

SIGMA = 3.427050983124843
RAIZ_X = 137.03449824893602
PHI_GLOBAL_REGISTRADO = 2869.460517705751  # gossip_result.json, N=140


def w(d, s=SIGMA):
    return (abs(d) + 1) ** (-s)


class NodoGlobalMind:
    def __init__(self, nid, Phi=1.0):
        self.id = nid
        self.Phi = Phi


def gossip_phi4(nodos, rondas=3, k_vecinos=12):
    Phi_g = 0.0
    peso = 0.0
    for _ in range(rondas):
        for nodo in nodos:
            for _ in range(k_vecinos):
                d = random.randint(1, max(1, len(nodos) // 2))
                pd = w(d)
                Phi_g += nodo.Phi * pd
                peso += pd
    return Phi_g / peso if peso > 0 else 0


def construir_nodos(n=140, semilla=None):
    if semilla is not None:
        random.seed(semilla)
    return [NodoGlobalMind(i, random.uniform(2864, 2875)) for i in range(n)]


def main():
    # 1. Reproducción con semilla 42: debe ser dígito a dígito el valor registrado.
    reproducido = gossip_phi4(construir_nodos(semilla=42))
    print(f"seed(42):  {reproducido}")
    print(f"registrado: {PHI_GLOBAL_REGISTRADO}")
    print(f"coincide:  {reproducido == PHI_GLOBAL_REGISTRADO}")

    # 2. Sin semilla varía: dos sorteos distintos, mismo N.
    # OJO: random.seed() sin argumentos re-siembra desde entropía del SO.
    # Es obligatorio aquí: la sección 1 llamó random.seed(42) en este
    # mismo proceso, y sin este re-sembrado los dos sorteos "sin semilla"
    # serían descendientes deterministas de la semilla 42 — idénticos en
    # cada ejecución del script, lo contrario de lo que se demuestra
    # (defecto encontrado en verificación independiente, 2026-11-07;
    # ver EVOLUCION.md).
    random.seed()
    a = gossip_phi4(construir_nodos())
    b = gossip_phi4(construir_nodos())
    print(f"sin semilla: {a:.4f} / {b:.4f} (varía: {a != b})")

    # 3. Es una media ponderada: el resultado vive entre min y max de entrada.
    nodos = construir_nodos(semilla=42)
    r = gossip_phi4(nodos)
    lo = min(n.Phi for n in nodos)
    hi = max(n.Phi for n in nodos)
    print(f"media ponderada: {lo:.2f} <= {r:.2f} <= {hi:.2f} : {lo <= r <= hi}")
    return 0 if (reproducido == PHI_GLOBAL_REGISTRADO and lo <= r <= hi) else 1


if __name__ == "__main__":
    raise SystemExit(main())
