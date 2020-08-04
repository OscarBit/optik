import numpy
import optik2 as optik


def test_legos():
    layer = optik.lego("test_layer", file_name="Si.txt")
    data = numpy.genfromtxt("./Materials/Si.txt")
    data = data.T
    "Test with Si.txt file already prepare"
    assert numpy.allclose(data[0], layer.lambd)
    assert numpy.allclose(data[1], layer.n)
    assert numpy.allclose(data[2], layer.k)
