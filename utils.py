import numpy


def g_function(ni, ki, n_back=1.0, k_back=0):
    """Function defined to summary some calculations. For more information,
    please consult http://bdigital.unal.edu.co/65682/1/1053830848.2018.pdf,
    pag. 26.
    """
    ans = (n_back ** 2 - ni ** 2 + k_back ** 2 - ki ** 2) / (
        (n_back + ni) ** 2 + (k_back + ki) ** 2
    )
    return ans


def h_function(ni, ki, n_back=1.0, k_back=0):
    """Function defined to summary some calculations. For more information,
    please consult http://bdigital.unal.edu.co/65682/1/1053830848.2018.pdf,
    pag. 26.
    """
    ans = 2 * (n_back * ki - ni * k_back) / ((n_back + ni) ** 2 + (k_back + ki) ** 2)
    return ans


def alpha_function(layer):
    """Function defined to summary some calculations. For more information,
    please consult http://bdigital.unal.edu.co/65682/1/1053830848.2018.pdf,
    pag. 26.
    """
    ans = (2 * numpy.pi * layer.k * layer.thickness) / layer.lambd
    return ans


def gamma_function(layer):
    """Function defined to summary some calculations. For more information,
    please consult http://bdigital.unal.edu.co/65682/1/1053830848.2018.pdf,
    pag. 26.
    """
    ans = (2 * numpy.pi * layer.n * layer.thickness) / layer.lambd
    return ans


def pqtu_function(up, layer):
    """Function defined to summary some calculations. For more information,
    please consult http://bdigital.unal.edu.co/65682/1/1053830848.2018.pdf,
    pag. 26.
    """
    p = numpy.exp(up.alpha) * numpy.cos(up.gamma)
    q = numpy.exp(up.alpha) * numpy.sin(up.gamma)
    t = numpy.exp(-up.alpha) * (
        layer.g * (numpy.cos(up.gamma)) + layer.h * (numpy.sin(up.gamma))
    )
    u = numpy.exp(-up.alpha) * (
        layer.h * (numpy.cos(up.gamma)) - (layer.g) * (numpy.sin(up.gamma))
    )
    return p, q, t, u


def rsvw_function(top, up):
    """Function defined to summary some calculations. For more information,
    please consult http://bdigital.unal.edu.co/65682/1/1053830848.2018.pdf,
    pag. 26.
    """
    r = numpy.exp(top.alpha) * (
        up.g * (numpy.cos(top.gamma)) - up.h * (numpy.sin(top.gamma))
    )
    s = numpy.exp(top.alpha) * (
        up.h * (numpy.cos(top.gamma)) + up.g * (numpy.sin(top.gamma))
    )
    v = numpy.exp(-top.alpha) * numpy.cos(top.gamma)
    w = -numpy.exp(-top.alpha) * numpy.sin(top.gamma)
    return r, s, v, w
