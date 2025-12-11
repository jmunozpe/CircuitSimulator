from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


@dataclass
class Component(ABC):
    name: str
    value: float

    @abstractmethod
    def get_impedance(self, frequency: float) -> complex:
        raise NotImplementedError


@dataclass
class Resistor(Component):
    power_rating: float | None = None

    @property
    def resistance(self) -> float:
        return self.value

    def get_impedance(self, frequency: float) -> complex:
        return complex(self.resistance, 0.0)


@dataclass
class Capacitor(Component):
    voltage_rating: float | None = None

    @property
    def capacitance(self) -> float:
        return self.value

    def get_impedance(self, frequency: float) -> complex:
        if frequency == 0:
            return complex(float("inf"))
        omega = 2 * math.pi * frequency
        return 1 / (1j * omega * self.capacitance)


@dataclass
class Inductor(Component):
    current_rating: float | None = None

    @property
    def inductance(self) -> float:
        return self.value

    def get_impedance(self, frequency: float) -> complex:
        omega = 2 * math.pi * frequency
        return 1j * omega * self.inductance

