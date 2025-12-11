from circuit_simulator.components import Resistor, Inductor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLSeriesCircuit
from circuit_simulator.plotting import plot_rl_series
import matplotlib.pyplot as plt

source = DCSupply(10.0)

R = Resistor("R1", 50)
L = Inductor("L1", 0.2)

circuit = RLSeriesCircuit(source, R, L)
result = circuit.simulate(t_end=1.0, dt=1e-4)

plot_rl_series(result)
plt.show()

