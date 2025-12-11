from circuit_simulator.components import Resistor, Inductor, Capacitor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLCSeriesCircuit
from circuit_simulator.plotting import plot_rlc_series
import matplotlib.pyplot as plt


source = DCSupply(5.0)
R = Resistor("R1", 50)
L = Inductor("L1", 10e-3)
C = Capacitor("C1", 100e-6)

circuit = RLCSeriesCircuit(source, R, L, C)
result = circuit.simulate(t_end=0.1, dt=1e-5)

plot_rlc_series(result)
plt.show()
