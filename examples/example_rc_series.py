from circuit_simulator.components import Resistor, Capacitor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RCSeriesCircuit
from circuit_simulator.plotting import plot_rc_series
import matplotlib.pyplot as plt


def main():
    source = DCSupply(5.0)  # 5 V
    R = Resistor("R1", 1000)      # 1 kΩ
    C = Capacitor("C1", 100e-6)   # 100 µF

    circuit = RCSeriesCircuit(source, R, C)
    result = circuit.simulate(t_end=0.5, dt=1e-4)

    plot_rc_series(result)
    plt.show()


if __name__ == "__main__":
    main()
