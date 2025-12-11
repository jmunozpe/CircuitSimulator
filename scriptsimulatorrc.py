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
from circuit_simulator.components import Resistor, Capacitor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RCSeriesCircuit

# parámetros
V = 5.0
R_value = 1e3        # 1 kΩ
C_value = 1e-6       # 1 μF
tau = R_value * C_value

# montar y simular
source = DCSupply(V)
R = Resistor("R", R_value)
C = Capacitor("C", C_value)
circuit = RCSeriesCircuit(source, R, C)
res = circuit.simulate(t_end=5 * tau, dt=tau/2000)

t = np.asarray(res["t"])
i = np.asarray(res["i"])
vc = np.asarray(res.get("vc", V - R_value * np.asarray(res["i"])))  # si el sim devuelve vc usarlo

# analítico
vc_exact = V * (1 - np.exp(-t / tau))
i_exact = (V / R_value) * np.exp(-t / tau)

# limpiar partes complejas si existieran
if np.iscomplexobj(i):
    i = i.real
if np.iscomplexobj(vc):
    vc = vc.real

# graficar
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(t, vc, label="vc sim")
plt.plot(t, vc_exact, "--", label="vc analítico")
plt.xlabel("Tiempo (s)"); plt.ylabel("Voltaje (V)"); plt.title("Vc en RC serie")
plt.legend(); plt.grid(True)

plt.subplot(1,2,2)
plt.plot(t, i, label="i sim")
plt.plot(t, i_exact, "--", label="i analítico")
plt.xlabel("Tiempo (s)"); plt.ylabel("Corriente (A)"); plt.title("i en RC serie")
plt.legend(); plt.grid(True)

out = root / "rc_step.png"
plt.tight_layout()
plt.savefig(out, dpi=150)
print(f"Imagen guardada en: {out}")
plt.show()