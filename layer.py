import numpy
from utils import g_function, h_function, alpha_function, gamma_function


def read_nk_file(file_name):
    """Read file of 3 columns, (wave_lengthm, n, k) from 
    ./Materials directory"""
    route = "./Materials/"
    if not file_name:
        route += input("File Name:")
    else:
        route += file_name
    data = numpy.loadtxt(route, dtype=float)  # , skiprows=1)
    data = data.T
    if len(data) != 3:
        print("3 cols with Wavelength(nm) n k. Try again!")
        raise ValueError("Can't upload data")
    else:
        wl, n, k = data
        step = 0.5
        new_wl = numpy.arange(280.0, wl.max() + 0.5, step, dtype=float)
        new_n = numpy.interp(new_wl, wl, n)
        new_k = numpy.interp(new_wl, wl, k)
        new_data = numpy.array([list(new_wl), list(new_n), list(new_k)], dtype=float)
        return new_data


class Layer:
    """Layer Object, input: the file name of file in 
    Materials directory and name of layer"""

    def __init__(self, name, new=True, file_name=False):
        self.name = name
        if new:
            data = read_nk_file(file_name)
            self.lambd, self.n, self.k = data[0], data[1], data[2]
        else:
            raise "Buscar name en la base, no sé cómo :v"

    def use(self, t, first=False, bottom=False, scnd=False):
        self.thickness = t
        self.alpha = alpha_function(self)
        self.gamma = gamma_function(self)
        if first:
            self.first = first
            self.bottom = bottom
            self.scnd = scnd
            self.g = g_function(self.n, self.k)
            self.h = h_function(self.n, self.k)
        else:
            self.first = first
            self.bottom = bottom
            self.scnd = scnd
            self.g = None
            self.h = None
        return self
