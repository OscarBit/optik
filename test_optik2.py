import unittest
import numpy as np
import optik2 as optik


class TestOptik(unittest.TestCase):
    def test_legos(self):
        layer = optik.lego("test_layer", file_name="Si.txt")
        data = np.genfromtxt("./Materials/Si.txt")
        data = data.T
        "Test with Si.txt file already prepare"
        assert np.allclose(data[0], layer.lambd)
        assert np.allclose(data[1], layer.n)
        assert np.allclose(data[2], layer.k)


if __name__ == "__main__":
    unittest.main()
