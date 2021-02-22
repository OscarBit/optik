# optik
* Project by: Santiago Torres 
* Collaborator: Me

Calculate Reflectance and Transmitance of cell using Python OOP.

## Simulación del modelo óptico en Python 3+

Se utilizó la librería numpy, mediante una estructura de programación orientada a objetos (POO), definiendo las clases bulk y layer, que tienen atributos propios de sus características físicas y métodos necesarios para el cálculo de sus parámetros ópticos. La clase layer se declara con tres parámetros, nombre, grosor de la película y la ubicación del archivo que contiene la data de los parámetros óticos n y k, para este material. La clase bulk recibe las capas (layer) y simula un material multicapa. Después de declarar las capas y componer el material multicapa se ejecuta el método para calcular R y T.
La estructura del código contiene una carpeta "Materials", en la que se almacena la información de cada material.
```console
├── LICENSE
├── Materials
│   ├── Al2.txt
│   ├── AlGaAs.txt
│   ├── Al.txt
│   ├── GaAs.txt
│   ├── InGaP.txt
│   ├── MgF2.txt
│   ├── SiN.txt
│   ├── Si.txt
│   └── ZnS.txt
├── README.md
├── requirements_dev.txt
└── src
    ├── bulk.py
    ├── layer.py
    ├── main.py
    ├── test_optik2.py
    ├── txt_files
    │   ├── v1.txt
    │   └── v2.txt
    └── utils.py
```
Este código esta disponible en este repositorio como proyecto público con el fin recibir contribuciones externas y tener una mejora continua con apoyo de otros desarrolladores y/o cientificos interesados en la simulación del modelo óptico de celdas solares.

Hay diferentes formas de utilizar este código, se recomienda crear un entorno virtual e instalar los requerimientos con el comando `pip install -r requirements_dev.txt`.

```python
from src.bulk import Bulk
from src.layer import Layer


def main():
    layers = [
        Layer(name="MgF2", thickness=100.0, filename="./Materials/Al2.txt"),
        Layer(name="ZnS", thickness=200.0, filename="./Materials/Si.txt"),
        Layer(name="InGaP", thickness=300.0, filename="./Materials/Al2.txt"),
        Layer(name="GaAs", thickness=400.0, filename="./Materials/Si.txt"),
    ]
    cell = Bulk(*layers)
    v1, v2 = cell.RT()
    print(f"Bulk of layers {[layer.name for layer in layers]}: \nR: {v1}\nT: {v2}")


if __name__ == "__main__":
    main()
```
