import math
from circuit_simulator.components import Resistor, Capacitor, Inductor


def test_resistor_impedance():
    R = Resistor("R", 100.0)
    assert R.get_impedance(0) == complex(100.0, 0.0)


def test_capacitor_impedance_dc_infinite():
    C = Capacitor("C", 1e-6)
    z = C.get_impedance(0)
    assert math.isinf(z.real)


def test_inductor_impedance_zero_at_dc():
    L = Inductor("L", 1e-3)
    z = L.get_impedance(0)
    assert abs(z) == 0.0

