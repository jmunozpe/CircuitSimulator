import numpy as np

from circuit_simulator.components import Resistor, Inductor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLSeriesCircuit


def test_rl_series_step_response_close_to_analytic():
    V = 5.0
    R_value = 100.0
    L_value = 10e-3
    tau = L_value / R_value

    source = DCSupply(V)
    R = Resistor("R1", R_value)
    L = Inductor("L1", L_value)

    circuit = RLSeriesCircuit(source, R, L)
    result = circuit.simulate(t_end=5 * tau, dt=1e-5)

    t = result["t"]
    i_num = result["i"]
    i_exact = (V / R_value) * (1 - np.exp(-t / tau))

    assert np.allclose(i_num, i_exact, atol=1e-3)
