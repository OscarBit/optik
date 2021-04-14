import numpy
from layer import Layer
from bulk import Bulk


def test_old_results():
    layers = [
        Layer(name="MgF2", thickness=100.0, filename="../Materials/Al2.txt"),
        Layer(name="ZnS", thickness=200.0, filename="../Materials/Si.txt"),
        Layer(name="InGaP", thickness=300.0, filename="../Materials/Al2.txt"),
        Layer(name="GaAs", thickness=400.0, filename="../Materials/Si.txt"),
    ]
    cell2 = Bulk(*layers)
    v1, v2 = cell2.RT()
    #v1_expected = numpy.loadtxt("./txt_files/v1.txt")
    #v2_expected = numpy.loadtxt("./txt_files/v2.txt")
    #assert numpy.allclose(v1, v1_expected)
    #assert numpy.allclose(v2, v2_expected)
