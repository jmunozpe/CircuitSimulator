from dataclasses import dataclass
import numpy as np


@dataclass
class DCSupply:
    voltage: float

    def value(self, t: np.ndarray) -> np.ndarray:
        return self.voltage * np.ones_like(t)

