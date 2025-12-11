import numpy as np
from circuit_simulator.components import Resistor, Capacitor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RCSeriesCircuit


def test_rc_series_step_response_close_to_analytic():
    V = 5.0
    R_value = 1000.0
    C_value = 100e-6
    tau = R_value * C_value

    source = DCSupply(V)
    R = Resistor("R1", R_value)
    C = Capacitor("C1", C_value)

    circuit = RCSeriesCircuit(source, R, C)
    result = circuit.simulate(t_end=5 * tau, dt=1e-4)

    t = result["t"]
    v_c = result["v_C"]
    i = result["i"]

    v_c_exact = V * (1 - np.exp(-t / tau))
    i_exact = (V / R_value) * np.exp(-t / tau)

    assert np.allclose(v_c, v_c_exact, atol=1e-2)
    assert np.allclose(i, i_exact, atol=1e-4)

