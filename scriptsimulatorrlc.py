import sys
from pathlib import Path
import subprocess

# asegurar raíz en sys.path
root = Path(__file__).resolve().parent
sys.path.insert(0, str(root))

# instalar matplotlib si falta
try:
    import matplotlib.pyplot as plt
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt

import numpy as np
from circuit_simulator.components import Resistor, Inductor, Capacitor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLCSeriesCircuit

# parámetros
V = 5.0
R_value = 10.0       # resistencia
L_value = 10e-3      # inductancia
C_value = 100e-9     # capacitancia
omega0 = 1.0 / np.sqrt(L_value * C_value)
alpha = R_value / (2 * L_value)
disc = omega0**2 - alpha**2

# montar y simular
source = DCSupply(V)
R = Resistor("R", R_value)
L = Inductor("L", L_value)
C = Capacitor("C", C_value)
circuit = RLCSeriesCircuit(source, R, L, C)
t_end = 10.0 / omega0
res = circuit.simulate(t_end=t_end, dt=1.0/(omega0*5000))

t = np.asarray(res["t"])
i = np.asarray(res["i"])

# analítico (subamortiguado)
if disc > 0:
    omega_d = np.sqrt(disc)
    i_exact = (V / (L_value * omega_d)) * np.exp(-alpha * t) * np.sin(omega_d * t)
else:
    # crítico o sobreamortiguado: usar solución numérica aproximada cuando no subamortiguado
    i_exact = np.zeros_like(t)

# limpiar parte real
if np.iscomplexobj(i):
    i = i.real

# graficar
plt.figure(figsize=(8,4))
plt.plot(t, i, label="i sim")
plt.plot(t, i_exact, "--", label="i analítico" if disc>0 else "analítico no subamort.")
plt.xlabel("Tiempo (s)"); plt.ylabel("Corriente (A)")
plt.title("Respuesta escalón RLC serie")
plt.legend(); plt.grid(True)

out = root / "rlc_step.png"
plt.tight_layout()
plt.savefig(out, dpi=150)
print(f"Imagen guardada en: {out}")
plt.show()