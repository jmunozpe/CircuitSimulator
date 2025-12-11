from typing import Callable, Tuple
import numpy as np


def euler_solver(f: Callable[[float, np.ndarray], np.ndarray],
                 y0: np.ndarray,
                 t_end: float,
                 dt: float) -> Tuple[np.ndarray, np.ndarray]:

    n_steps = int(t_end / dt) + 1
    t = np.linspace(0, t_end, n_steps)
    y = np.zeros((n_steps, len(y0)), dtype=float)
    y[0, :] = y0

    for k in range(n_steps - 1):
        dy = f(t[k], y[k, :])
        y[k + 1, :] = y[k, :] + dt * dy

    return t, y

