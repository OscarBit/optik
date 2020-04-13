import unittest
import numpy as np
import optik2 as optik

class TestOptik(unittest.TestCase):

    def test_legos(self):
        layer = optik.lego('test_layer',filename='Si.txt')
        data = np.genfromtxt("./Materials/Si.txt")
        data = data.T
        "Test with Si.txt file already prepare"
        self.assertEqual(data[0], layer.lambd)
        self.assertEqual(data[1], layer.n)
        self.assertEqual(data[2], layer.k)

if __name__ == '__main__':
    unittest.main()