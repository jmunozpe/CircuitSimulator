from circuit_simulator.components import Resistor, Inductor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLSeriesCircuit
from circuit_simulator.plotting import plot_rl_series
import matplotlib.pyplot as plt


def main():
    source = DCSupply(5.0)  # 5 V
    R = Resistor("R1", 100)      # 100 Ω
    L = Inductor("L1", 10e-3)    # 10 mH

    circuit = RLSeriesCircuit(source, R, L)
    result = circuit.simulate(t_end=0.1, dt=1e-5)

    plot_rl_series(result)
    plt.show()


if __name__ == "__main__":
    main()
