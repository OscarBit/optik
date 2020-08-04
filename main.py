from matplotlib import pyplot

from bulk import Bulk
from layer import Layer


def main():
    layers = [
        Layer(name="MgF2", thickness=100.0, filename="./Materials/Al2.txt"),
        Layer(name="ZnS", thickness=200.0, filename="./Materials/Si.txt"),
        Layer(name="InGaP", thickness=300.0, filename="./Materials/Al2.txt"),
        Layer(name="GaAs", thickness=400.0, filename="./Materials/Si.txt"),
    ]
    cell2 = Bulk(*layers)
    v1, v2 = cell2.RT()


if __name__ == "__main__":
    main()
