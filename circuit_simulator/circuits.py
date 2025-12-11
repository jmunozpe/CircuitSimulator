from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict
import numpy as np

from .components import Resistor, Capacitor, Inductor
from .sources import DCSupply
from .solver import euler_solver


@dataclass
class Circuit(ABC):
    source: DCSupply

    @abstractmethod
    def simulate(self, t_end: float, dt: float) -> Dict[str, np.ndarray]:
        ...


@dataclass
class RCSeriesCircuit(Circuit):
    R: Resistor
    C: Capacitor

    def simulate(self, t_end: float, dt: float) -> Dict[str, np.ndarray]:
        V = self.source.voltage
        R = self.R.resistance
        C = self.C.capacitance

        def f(t, state):
            v_c = state[0]
            dv_dt = (V - v_c) / (R * C)
            return np.array([dv_dt])

        t, y = euler_solver(f, np.array([0.0]), t_end, dt)
        v_c = y[:, 0]
        i = (V - v_c) / R
        v_r = V - v_c

        return {"t": t, "i": i, "v_R": v_r, "v_C": v_c}


@dataclass
class RLSeriesCircuit(Circuit):
    R: Resistor
    L: Inductor

    def simulate(self, t_end: float, dt: float) -> Dict[str, np.ndarray]:
        V = self.source.voltage
        R = self.R.resistance
        L = self.L.inductance

        def f(t, state):
            i = state[0]
            di_dt = (V - R * i) / L
            return np.array([di_dt])

        t, y = euler_solver(f, np.array([0.0]), t_end, dt)
        i = y[:, 0]
        v_r = R * i
        v_l = V - v_r

        return {"t": t, "i": i, "v_R": v_r, "v_L": v_l}


@dataclass
class RLCSeriesCircuit(Circuit):
    R: Resistor
    L: Inductor
    C: Capacitor

    def simulate(self, t_end: float, dt: float) -> Dict[str, np.ndarray]:
        V = self.source.voltage
        R = self.R.resistance
        L = self.L.inductance
        C = self.C.capacitance

        def f(t, state):
            i, v_c = state
            di_dt = (V - R * i - v_c) / L
            dv_dt = i / C
            return np.array([di_dt, dv_dt])

        t, y = euler_solver(f, np.array([0.0, 0.0]), t_end, dt)
        i = y[:, 0]
        v_c = y[:, 1]
        v_r = R * i
        v_l = V - v_r - v_c

        return {"t": t, "i": i, "v_R": v_r, "v_L": v_l, "v_C": v_c}

