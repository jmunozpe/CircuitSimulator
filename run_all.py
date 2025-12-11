import sys, subprocess, os
from pathlib import Path
root = Path(__file__).resolve().parent
# aquí pongo los nombres que realmente tienes
scripts = ["scriptsimulator.py", "scriptsimulatorrc.py", "scriptsimulatorrlc.py"]
for name in scripts:
    path = root / name
    if not path.exists():
        print(f"{name}: no existe")
        continue
    print(f"Ejecutando {name} ...")
    env = dict(os.environ)
    env["MPLBACKEND"] = "Agg"
    res = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, env=env)
    log = root / f"{name}.run.log"
    with open(log, "w", encoding="utf-8") as f:
        f.write("STDOUT:\n"+res.stdout+"\n\nSTDERR:\n"+res.stderr)
    print(f"{name}: código {res.returncode}, log -> {log}")