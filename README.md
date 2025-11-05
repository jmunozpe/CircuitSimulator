# CircuitSimulator
Simulador de circuitos RC, RL y RLC en Python 

**Alternativa 4 – Simulación de circuitos RC, RL y RLC simples con fuente DC**
<img width="1536" height="1024" alt="circuit simulator logo" src="https://github.com/user-attachments/assets/5b8f8beb-b4ef-4917-9e38-d663c794d446" />


El proyecto consiste en desarrollar una aplicación en **Python** que simule circuitos **RC**, **RL** y **RLC** simples con una fuente de tensión DC.  
El programa calculará y mostrará las **gráficas de tensión y corriente** en cada componente del circuito.

La implementación se basa en la programacion orientada a objetos, donde cada componente eléctrico (resistor, capacitor e inductor) es una clase con sus propios atributos físicos y métodos para calcular su comportamiento.

**Objetivos específicos:**
- Aplicar POO para modelar componentes eléctricos básicos.
- Simular el comportamiento transitorio en circuitos RC, RL y RLC en DC.
- Graficar la respuesta temporal de cada componente.
---

##  Diagrama de clases

```mermaid
classDiagram
direction TB

    class Component {
        <<abstract>>
        + name: str
        + value: float
        + get_impedance(frequency: float): complex
    }

    class Resistor {
        + resistance: float
        + power_rating: float
        + get_impedance(frequency: float): complex
    }

    class Capacitor {
        + capacitance: float
        + voltage_rating: float
        + get_impedance(frequency: float): complex
    }

    class Inductor {
        + inductance: float
        + current_rating: float
        + get_impedance(frequency: float): complex
    }

    class Circuit {
        + components: list[Component]
        + V_in: float
        + simulate()
        + plot_response()
    }

    class RCCircuit {
        + simulate()
    }

    class RLCircuit {
        + simulate()
    }

    class RLCCircuit {
        + simulate()
    }

    Component <|-- Resistor
    Component <|-- Capacitor
    Component <|-- Inductor
    Circuit <|-- RCCircuit
    Circuit <|-- RLCircuit
    Circuit <|-- RLCCircuit

```
---

## como funciona?

##1. Clase abstracta ##

Es la clase base (abstracta) que define el comportamiento general de cualquier componente eléctrico.

Contiene atributos comunes:

name: nombre del componente 

value: valor físico 

Tiene un método abstracto get_impedance(frequency: float) que debe ser implementado por cada componente, ya que la impedancia depende del tipo (R, L o C).

##2. Clases derivadas de Component##

Cada una hereda de Component y define su propio comportamiento físico.

 Resistor

Atributos:

resistance: valor de la resistencia (Ω).

power_rating: potencia máxima soportada (W).

Método:

get_impedance(frequency): devuelve una impedancia real constante, Z = R.

Capacitor

Atributos:

capacitance: valor del condensador (F).

voltage_rating: tensión máxima (V).

Método:

get_impedance(frequency): devuelve Z = 1 / (j·2π·f·C), una impedancia inversamente proporcional a la frecuencia.

Inductor

Atributos:

inductance: valor de la inductancia (H).

current_rating: corriente máxima (A).

Método:

get_impedance(frequency): devuelve Z = j·2π·f·L, una impedancia directamente proporcional a la frecuencia.

##3. Clase Circuit##

Representa un circuito genérico, compuesto por una lista de objetos Component.

Atributos:

components: lista con resistores, capacitores e inductores.

V_in: tensión de entrada 

Métodos principales:

simulate(): ejecuta la simulación del circuito según las ecuaciones diferenciales del sistema.

plot_response(): genera las gráficas de tensión y corriente en el tiempo usando matplotlib.
