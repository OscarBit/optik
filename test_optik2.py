import numpy
from layer import Layer
from bulk import Bulk


# def test_layer():
#     layer = Layer("test_layer", file_name="Si.txt")
#     data = numpy.genfromtxt("./Materials/Si.txt")
#     data = data.T
#     "Test with Si.txt file already prepare"
#     assert numpy.allclose(data[0], layer.lambd)
#     assert numpy.allclose(data[1], layer.n)
#     assert numpy.allclose(data[2], layer.k)


def test_old_results():
    layers = [
        Layer(name="MgF2", thickness=100.0, filename="./Materials/Al2.txt"),
        Layer(name="ZnS", thickness=200.0, filename="./Materials/Si.txt"),
        Layer(name="InGaP", thickness=300.0, filename="./Materials/Al2.txt"),
        Layer(name="GaAs", thickness=400.0, filename="./Materials/Si.txt"),
    ]
    cell2 = Bulk(*layers)
    v1, v2 = cell2.RT()
    v1_expected = numpy.loadtxt("v1.txt")
    v2_expected = numpy.loadtxt("v2.txt")
    assert numpy.allclose(v1, v1_expected)
    assert numpy.allclose(v2, v2_expected)

