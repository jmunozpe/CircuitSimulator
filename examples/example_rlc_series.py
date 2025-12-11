from circuit_simulator.components import Resistor, Inductor, Capacitor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLCSeriesCircuit
from circuit_simulator.plotting import plot_rlc_series
import matplotlib.pyplot as plt

source = DCSupply(5.0)

R = Resistor("R1", 20)
L = Inductor("L1", 0.5)
C = Capacitor("C1", 50e-6)

circuit = RLCSeriesCircuit(source, R, L, C)
result = circuit.simulate(t_end=2.0, dt=1e-4)

plot_rlc_series(result)
plt.show()
