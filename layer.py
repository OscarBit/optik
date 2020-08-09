import numpy


class Layer:
    """Layer Object, input: the file name of file in 
    Materials directory and name of layer"""

    def __init__(self, name, thickness, filename):
        self.name = name
        self.thickness = thickness
        self.filename = filename

        data = self.read_nk_file(filename)
        self.lambd, self.n, self.k = data

        self.alpha = self._alpha_function()
        self.gamma = self._gamma_function()

        self.first = False
        self.bottom = False
        self.scnd = False
        self.g = None
        self.h = None

    def _alpha_function(self):
        """Function defined to summary some calculations. For more information,
        please consult http://bdigital.unal.edu.co/65682/1/1053830848.2018.pdf,
        pag. 26.
        """
        return (2 * numpy.pi * self.k * self.thickness) / self.lambd

    def _gamma_function(self):
        """Function defined to summary some calculations. For more information,
        please consult http://bdigital.unal.edu.co/65682/1/1053830848.2018.pdf,
        pag. 26.
        """
        return (2 * numpy.pi * self.n * self.thickness) / self.lambd

    @staticmethod
    def read_nk_file(filename, sep=None, has_header=False):
        """Read file of 3 columns, (wavelength, n, k)."""
        skiprows = 1 if has_header else 0
        data = numpy.loadtxt(filename, delimiter=sep, skiprows=skiprows, dtype=float).T
        if len(data) != 3:
            # TODO: Create own exception
            raise Exception("Three numerical columns are required.")

        wavelength, n, k = data
        step = 0.5
        new_wavelength = numpy.arange(280.0, wavelength.max() + 0.5, step, dtype=float)
        new_n = numpy.interp(new_wavelength, wavelength, n)
        new_k = numpy.interp(new_wavelength, wavelength, k)
        return numpy.array(
            [list(new_wavelength), list(new_n), list(new_k)], dtype=float
        )
