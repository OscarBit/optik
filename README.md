# optik
* Project by: Santiago Torres 
* Collaborator: Me

Calculate Reflectance and Transmitance of cell using Python OOP.

## Simulación del modelo óptico en Python 3+

Se utilizó programación orientada a objetos (POO) y la librería numpy, definiendo las clases bulk y layer, que tienen atributos propios de sus características físicas y métodos necesarios para el cálculo de sus parámetros ópticos. La clase layer se declara con tres parámetros, nombre, grosor de la película y la ubicación del archivo que contiene la data de los parámetros óticos n y k, para este material. La clase bulk recibe las capas (layer) y simula un material multicapa. Después de declarar las capas y componer el material multicapa se ejecuta el método para calcular R y T.
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
├── optik.ipynb
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
Para solucionar el sistema de ecuaciones se usan las funciones de `./src/utils.py` embebidas en los métodos de la clase bulk. Este código esta disponible en este repositorio público como proyecto open source.

En el objeto bulk simula la celda, a este objeto se le definieron 4 métodos. Inicializador o `__init__`, que se ejecuta automáticamente al declarar una nueva celda, `update_gh_layers` que carga la información de las capas que la conforman y solo es ejecutado al final del método `__init__`, `calc_R` calcula la Reflectancia del material en bulk y lo devuelve, por último `RT` este método devuelve los datos de Reflectancia y Transmitancia de la celda haciendo uso de `calc_R`. El método más útil para obtener resultados inmediatos es `RT`, los demás fueron definidos en esta clase para facilitar la simulación.

Hay diferentes formas de utilizar este código, se recomienda crear un entorno virtual `$ pip install virtualenv && python3 -m venv optik`, descargar el código e instalar los requerimientos con el comando `pip install -r requirements_dev.txt`. Una vez configurado el ambiente virutal puede usar los archivos dicsponibles en el repositorio en la carpeta `./optik/src/` o el notebook `optik.ipynb` que puede ser usado con el software de [Jupyter](https://jupyter.org/) o cargando el notebook y los archivos a [Colab](https://colab.research.google.com/) u otros servicios similares disponibles en la web.

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
