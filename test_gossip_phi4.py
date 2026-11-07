#!/usr/bin/env python3
"""Tests del hueso Global Mind. Solo stdlib. Sin red, sin secretos.

Ejecutar: python3 test_gossip_phi4.py
"""
import os
import random
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import gossip_phi4_repro as g  # noqa: E402


def test_seed_42_reproduce_el_valor_registrado():
    """Con seed(42), gossip_phi4 = 2869.460517705751, dígito a dígito el
    Phi_global de gossip_result.json (SÉ, SUELOS_FERTILES.md §5,
    2026-11-07 ~05:30Z; re-verificado en esta siembra)."""
    r = g.gossip_phi4(g.construir_nodos(semilla=42))
    assert r == 2869.460517705751, r


def test_seed_42_es_determinista():
    """Dos corridas con seed(42) dan el mismo número."""
    a = g.gossip_phi4(g.construir_nodos(semilla=42))
    b = g.gossip_phi4(g.construir_nodos(semilla=42))
    assert a == b


def test_sin_semilla_varia():
    """Sin semilla, dos sorteos del mismo N=140 difieren (SÉ, §5:
    2869.4520 vs 2869.3445; gossip_scale_test.json 2869.6743).
    Cada sorteo se re-siembra desde entropía del SO: sin ese
    random.seed() previo, un seed(42) anterior en este mismo proceso
    (p. ej. de test_es_media_ponderada_no_integracion) haría los dos
    sorteos descendientes deterministas de la semilla 42 — distintos
    entre sí, pero idénticos en cada corrida del test (defecto
    encontrado en verificación independiente, 2026-11-07; EVOLUCION.md)."""
    random.seed()
    a = g.gossip_phi4(g.construir_nodos())
    random.seed()
    b = g.gossip_phi4(g.construir_nodos())
    assert a != b


def test_sin_semilla_varia_entre_procesos():
    """Regresión del defecto anterior: dos ejecuciones del script como
    procesos separados deben imprimir pares 'sin semilla' distintos.
    Sin el re-sembrado, ambas imprimían 2869.6818 / 2868.4741."""
    def par_sin_semilla():
        r = subprocess.run([sys.executable, os.path.join(AQUI, "gossip_phi4_repro.py")],
                           capture_output=True, text=True)
        assert r.returncode == 0, r.stdout + r.stderr
        m = re.search(r"sin semilla: ([\d.]+) / ([\d.]+)", r.stdout)
        assert m, r.stdout
        return (m.group(1), m.group(2))
    assert par_sin_semilla() != par_sin_semilla()


def test_es_media_ponderada_no_integracion():
    """El resultado cae entre el min y el max de los Phi de entrada:
    es una media ponderada, no una medida de integración entre nodos.
    Con entradas constantes, el resultado ES la constante."""
    nodos = g.construir_nodos(semilla=42)
    r = g.gossip_phi4(nodos)
    assert min(n.Phi for n in nodos) <= r <= max(n.Phi for n in nodos)
    fijos = [g.NodoGlobalMind(i, 100.0) for i in range(140)]
    assert abs(g.gossip_phi4(fijos) - 100.0) < 1e-9  # media exacta salvo redondeo float


def test_constantes_del_codigo():
    """sigma y RAIZ_X son los literales del código fuente v150."""
    assert g.SIGMA == 3.427050983124843
    assert g.RAIZ_X == 137.03449824893602


def test_script_repro_pasa():
    """gossip_phi4_repro.py termina en 0 e imprime la coincidencia."""
    r = subprocess.run([sys.executable, os.path.join(AQUI, "gossip_phi4_repro.py")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "coincide:  True" in r.stdout


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    fallos = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
        except AssertionError as e:
            fallos += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"{len(tests) - fallos}/{len(tests)} tests OK")
    raise SystemExit(1 if fallos else 0)
