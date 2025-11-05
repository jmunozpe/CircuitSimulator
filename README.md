# CircuitSimulator
Simulador de circuitos RC, RL y RLC en Python 

**Alternativa 4 – Simulación de circuitos RC, RL y RLC simples con fuente DC**

El proyecto consiste en desarrollar una aplicación en **Python** que simule circuitos **RC**, **RL** y **RLC** simples con una **fuente de tensión DC.  
El programa calculará y mostrará las **gráficas de tensión y corriente** en cada componente del circuito.

La implementación se basa en la programacion orientada a objetos, donde cada componente eléctrico (resistor, capacitor e inductor) es una clase con sus propios atributos físicos y métodos para calcular su comportamiento.

**Objetivos específicos:**
- Aplicar POO para modelar componentes eléctricos básicos.
- Simular el comportamiento transitorio en circuitos RC, RL y RLC en DC.
- Graficar la respuesta temporal de cada componente.
---

## 🧠 Diagrama de clases

```mermaid
classDiagram
    class Component {
        +get_impedance(frequency: float): complex
    }
    class Resistor {
        +resistance: float
        +power: float
        +get_impedance(frequency): complex
    }
    class Capacitor {
        +capacitance: float
        +voltage_rating: float
        +get_impedance(frequency): complex
    }
    class Inductor {
        +inductance: float
        +current_rating: float
        +get_impedance(frequency): complex
    }
    class RCCircuit { +simulate() }
    class RLCircuit { +simulate() }
    class RLCCircuit { +simulate() }

    Resistor ..|> Component
    Capacitor ..|> Component
    Inductor ..|> Component
```
