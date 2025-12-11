import matplotlib.pyplot as plt
import numpy as np


def _plot_voltages(t: np.ndarray, voltages: dict, title: str):
    plt.figure()
    for label, v in voltages.items():
        plt.plot(t, v, label=label)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Tensión [V]")
    plt.title(title)
    plt.legend()
    plt.grid(True)


def _plot_current(t: np.ndarray, i: np.ndarray, title: str):
    plt.figure()
    plt.plot(t, i, label="i(t)")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Corriente [A]")
    plt.title(title)
    plt.legend()
    plt.grid(True)


def plot_rc_series(result: dict):
    t = result["t"]
    _plot_voltages(t, {"v_R": result["v_R"], "v_C": result["v_C"]}, "RC Serie")
    _plot_current(t, result["i"], "Corriente RC")


def plot_rl_series(result: dict):
    t = result["t"]
    _plot_voltages(t, {"v_R": result["v_R"], "v_L": result["v_L"]}, "RL Serie")
    _plot_current(t, result["i"], "Corriente RL")


def plot_rlc_series(result: dict):
    t = result["t"]
    _plot_voltages(t, {"v_R": result["v_R"], "v_L": result["v_L"], "v_C": result["v_C"]}, "RLC Serie")
    _plot_current(t, result["i"], "Corriente RLC")

