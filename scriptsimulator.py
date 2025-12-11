import sys
import subprocess
from pathlib import Path

# --- asegurar que la raíz del proyecto esté en sys.path ---
this_file = Path(__file__).resolve()
# busca hacia arriba hasta encontrar la carpeta que contiene 'circuit_simulator'
root = this_file
for _ in range(6):
    if (root / "circuit_simulator").exists():
        break
    root = root.parent
else:
    root = this_file.parent  # fallback

sys.path.insert(0, str(root))

# --- asegurar matplotlib disponible (intenta instalar si falta) ---
try:
    import matplotlib.pyplot as plt
except Exception:
    print("matplotlib no encontrado. Intentando instalar...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt

import numpy as np
from circuit_simulator.components import Resistor, Inductor
from circuit_simulator.sources import DCSupply
from circuit_simulator.circuits import RLSeriesCircuit

def main():
    V = 5.0
    R_value = 100.0
    L_value = 10e-3
    tau = L_value / R_value

    source = DCSupply(V)
    R = Resistor("R1", R_value)
    L = Inductor("L1", L_value)
    circuit = RLSeriesCircuit(source, R, L)
    result = circuit.simulate(t_end=5 * tau, dt=1e-5)

    t = np.asarray(result["t"])
    i = np.asarray(result["i"])
    if np.iscomplexobj(i):
        i = i.real

    i_exact = (V / R_value) * (1 - np.exp(-t / tau))

    plt.figure(figsize=(8,4))
    plt.plot(t, i, label="Simulado", linewidth=2)
    plt.plot(t, i_exact, "--", label="Analítico", linewidth=1.2)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Corriente (A)")
    plt.title("Respuesta escalón RL serie")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    out = root / "rl_step.png"
    plt.savefig(out, dpi=150)
    print(f"Imagen guardada en: {out}")
    plt.show()

if __name__ == "__main__":
    main()