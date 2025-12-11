from circuit_simulator.components import Resistor, Capacitor, Inductor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RCSeriesCircuit, RLSeriesCircuit, RLCSeriesCircuit
from circuit_simulator.plotting import plot_rc_series, plot_rl_series, plot_rlc_series
import matplotlib.pyplot as plt


def input_float(msg):
    return float(input(msg))


def simulate_rc():
    V = input_float("Voltaje de la fuente (V): ")
    R = input_float("Valor de la resistencia R (ohmios): ")
    C = input_float("Valor del capacitor C (faradios): ")
    t_end = input_float("Tiempo total de simulación (s): ")
    dt = input_float("Paso de tiempo dt: ")

    source = DCSupply(V)
    r = Resistor("R1", R)
    c = Capacitor("C1", C)

    circuit = RCSeriesCircuit(source, r, c)
    result = circuit.simulate(t_end=t_end, dt=dt)

    plot_rc_series(result)
    plt.show()


def simulate_rl():
    V = input_float("Voltaje de la fuente (V): ")
    R = input_float("Valor de la resistencia R (ohmios): ")
    L = input_float("Valor del inductor L (henrios): ")
    t_end = input_float("Tiempo total de simulación (s): ")
    dt = input_float("Paso de tiempo dt: ")

    source = DCSupply(V)
    r = Resistor("R1", R)
    l = Inductor("L1", L)

    circuit = RLSeriesCircuit(source, r, l)
    result = circuit.simulate(t_end=t_end, dt=dt)

    plot_rl_series(result)
    plt.show()


def simulate_rlc():
    V = input_float("Voltaje de la fuente (V): ")
    R = input_float("Valor de la resistencia R (ohmios): ")
    L = input_float("Valor del inductor L (henrios): ")
    C = input_float("Valor del capacitor C (faradios): ")
    t_end = input_float("Tiempo total de simulación (s): ")
    dt = input_float("Paso de tiempo dt: ")

    source = DCSupply(V)
    r = Resistor("R1", R)
    l = Inductor("L1", L)
    c = Capacitor("C1", C)

    circuit = RLCSeriesCircuit(source, r, l, c)
    result = circuit.simulate(t_end=t_end, dt=dt)

    plot_rlc_series(result)
    plt.show()


def main():
    print("\n--- Simulador de Circuitos RC, RL y RLC ---\n")
    print("1. Simular circuito RC en serie")
    print("2. Simular circuito RL en serie")
    print("3. Simular circuito RLC en serie")
    print("4. Salir")

    choice = input("\nSeleccione una opción: ")

    if choice == "1":
        simulate_rc()
    elif choice == "2":
        simulate_rl()
    elif choice == "3":
        simulate_rlc()
    else:
        print("Saliendo...")
        return


if __name__ == "__main__":
    while True:
        main()
        again = input("\n¿Desea realizar otra simulación? (s/n): ")
        if again.lower() != "s":
            break
