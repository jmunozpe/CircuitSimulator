from __future__ import annotations

from typing import Dict, List, Tuple

import numpy as np
import matplotlib.pyplot as plt

from circuit_simulator.components import Resistor, Capacitor, Inductor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RCSeriesCircuit, RLSeriesCircuit, RLCSeriesCircuit
from circuit_simulator.plotting import plot_rc_series, plot_rl_series, plot_rlc_series


def input_float(msg: str) -> float:
    return float(input(msg))


def input_int(msg: str) -> int:
    return int(input(msg))


def leer_resistencias() -> Tuple[List[float], str, float]:
    print("\n--- Configuración de resistencias ---")
    n = input_int("Número de resistencias: ")
    valores: List[float] = []
    for i in range(n):
        valores.append(input_float(f"R{i+1} (ohmios): "))
    modo = input("Configuración de las resistencias (s = serie, p = paralelo): ").strip().lower()
    if modo == "p":
        req = 1.0 / sum(1.0 / r for r in valores)
    else:
        req = sum(valores)
        modo = "s"
    return valores, modo, req


def pedir_componentes() -> Dict[str, object]:
    datos: Dict[str, object] = {}
    print("\n--- Fuente ---")
    V = input_float("Voltaje de la fuente DC (V): ")
    datos["V"] = V
    resistencias, modo, req = leer_resistencias()
    datos["R_values"] = resistencias
    datos["R_mode"] = modo
    datos["R_eq"] = req
    print("\n--- Componentes reactivos ---")
    usar_c = input("¿Desea incluir un capacitor? (s/n): ").strip().lower() == "s"
    if usar_c:
        C = input_float("Valor del capacitor C (faradios): ")
    else:
        C = None
    usar_l = input("¿Desea incluir una bobina (inductor)? (s/n): ").strip().lower() == "s"
    if usar_l:
        L = input_float("Valor del inductor L (henrios): ")
    else:
        L = None
    datos["C"] = C
    datos["L"] = L
    print("\n--- Parámetros de simulación ---")
    t_end = input_float("Tiempo total de simulación (s): ")
    dt = input_float("Paso de tiempo dt: ")
    datos["t_end"] = t_end
    datos["dt"] = dt
    return datos


def postprocesar_resistencias(
    result: Dict[str, object],
    resistencias: List[float],
    modo: str,
    r_eq: float,
) -> Dict[str, object]:
    i_total = result["i"]
    v_r_total = result.get("v_r")
    if v_r_total is None:
        v_r_total = i_total * r_eq
    extra: Dict[str, object] = {}
    if modo == "s":
        for idx, r in enumerate(resistencias, start=1):
            v = i_total * r
            extra[f"v_R{idx}"] = v
            extra[f"i_R{idx}"] = i_total
    else:
        for idx, r in enumerate(resistencias, start=1):
            v = v_r_total
            i_branch = v / r
            extra[f"v_R{idx}"] = v
            extra[f"i_R{idx}"] = i_branch
    result.update(extra)
    return result


def graficar_resistencias(
    result: Dict[str, object],
    resistencias: List[float],
    titulo: str,
) -> None:
    t = result["t"]
    plt.figure()
    for idx, _ in enumerate(resistencias, start=1):
        v = result[f"v_R{idx}"]
        plt.plot(t, v, label=f"v_R{idx}")
    plt.xlabel("t (s)")
    plt.ylabel("Voltaje (V)")
    plt.title(titulo + " - Voltaje en cada resistencia")
    plt.legend()
    plt.figure()
    for idx, _ in enumerate(resistencias, start=1):
        i = result[f"i_R{idx}"]
        plt.plot(t, i, label=f"i_R{idx}")
    plt.xlabel("t (s)")
    plt.ylabel("Corriente (A)")
    plt.title(titulo + " - Corriente en cada resistencia")
    plt.legend()


def simular_resistivo(datos: Dict[str, object]) -> None:
    V = datos["V"]
    r_values = datos["R_values"]
    modo = datos["R_mode"]
    r_eq = datos["R_eq"]
    t_end = datos["t_end"]
    dt = datos["dt"]
    t = np.arange(0, t_end + dt, dt)
    I = V / r_eq
    i_total = np.full_like(t, I, dtype=float)
    v_r_total = np.full_like(t, V, dtype=float)
    result: Dict[str, object] = {"t": t, "i": i_total, "v_r": v_r_total}
    result = postprocesar_resistencias(result, r_values, modo, r_eq)
    graficar_resistencias(result, r_values, "Circuito Resistivo Puro")
    plt.show()


def simular_rc(datos: Dict[str, object]) -> None:
    V = datos["V"]
    r_values = datos["R_values"]
    modo = datos["R_mode"]
    r_eq = datos["R_eq"]
    C = datos["C"]
    t_end = datos["t_end"]
    dt = datos["dt"]
    source = DCSupply(V)
    r = Resistor("Req", r_eq)
    c = Capacitor("C1", C)
    circuito = RCSeriesCircuit(source, r, c)
    result = circuito.simulate(t_end=t_end, dt=dt)
    result = postprocesar_resistencias(result, r_values, modo, r_eq)
    plot_rc_series(result)
    graficar_resistencias(result, r_values, "RC")
    plt.show()


def simular_rl(datos: Dict[str, object]) -> None:
    V = datos["V"]
    r_values = datos["R_values"]
    modo = datos["R_mode"]
    r_eq = datos["R_eq"]
    L = datos["L"]
    t_end = datos["t_end"]
    dt = datos["dt"]
    source = DCSupply(V)
    r = Resistor("Req", r_eq)
    l = Inductor("L1", L)
    circuito = RLSeriesCircuit(source, r, l)
    result = circuito.simulate(t_end=t_end, dt=dt)
    result = postprocesar_resistencias(result, r_values, modo, r_eq)
    plot_rl_series(result)
    graficar_resistencias(result, r_values, "RL")
    plt.show()


def simular_rlc(datos: Dict[str, object]) -> None:
    V = datos["V"]
    r_values = datos["R_values"]
    modo = datos["R_mode"]
    r_eq = datos["R_eq"]
    C = datos["C"]
    L = datos["L"]
    t_end = datos["t_end"]
    dt = datos["dt"]
    source = DCSupply(V)
    r = Resistor("Req", r_eq)
    c = Capacitor("C1", C)
    l = Inductor("L1", L)
    circuito = RLCSeriesCircuit(source, r, l, c)
    result = circuito.simulate(t_end=t_end, dt=dt)
    result = postprocesar_resistencias(result, r_values, modo, r_eq)
    plot_rlc_series(result)
    graficar_resistencias(result, r_values, "RLC")
    plt.show()


def main() -> None:
    print("\n--- Simulador de Circuitos R, RC, RL y RLC ---\n")
    print("Este programa le permitirá elegir:")
    print("- Número de resistencias y su configuración (serie/paralelo)")
    print("- Si desea usar capacitor, bobina, ambos o ninguno")
    print("- Parámetros de simulación en el tiempo\n")
    datos = pedir_componentes()
    C = datos["C"]
    L = datos["L"]
    if C is None and L is None:
        print("\nCircuito detectado: SOLO RESISTIVO (R)\n")
        simular_resistivo(datos)
        return
    if C is not None and L is None:
        print("\nCircuito detectado: RC (Resistencia + Capacitor)\n")
        simular_rc(datos)
    elif C is None and L is not None:
        print("\nCircuito detectado: RL (Resistencia + Bobina)\n")
        simular_rl(datos)
    else:
        print("\nCircuito detectado: RLC (Resistencia + Bobina + Capacitor)\n")
        simular_rlc(datos)


if __name__ == "__main__":
    while True:
        main()
        again = input("\n¿Desea realizar otra simulación? (s/n): ").strip().lower()
        if again != "s":
            break
