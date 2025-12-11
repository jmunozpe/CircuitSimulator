from circuit_simulator.components import Resistor, Inductor, Capacitor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLCSeriesCircuit
from circuit_simulator.plotting import plot_rlc_series
import matplotlib.pyplot as plt


def main():
    source = DCSupply(5.0)   # 5 V

    R = Resistor("R1", 50)          # 50 Ω
    L = Inductor("L1", 10e-3)       # 10 mH
    C = Capacitor("C1", 100e-6)     # 100 µF

    circuit = RLCSeriesCircuit(source, R, L, C)
    result = circuit.simulate(t_end=0.1, dt=1e-5)

    plot_rlc_series(result)
    plt.show()


if __name__ == "__main__":
    main()
