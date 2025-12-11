from circuit_simulator.components import Resistor, Inductor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLSeriesCircuit
from circuit_simulator.plotting import plot_rl_series
import matplotlib.pyplot as plt


source = DCSupply(5.0)
R = Resistor("R1", 100)
L = Inductor("L1", 10e-3)

circuit = RLSeriesCircuit(source, R, L)
result = circuit.simulate(t_end=0.1, dt=1e-5)

plot_rl_series(result)
plt.show()
