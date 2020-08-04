from matplotlib import pyplot

from bulk import Bulk
from layer import Layer


def main():
    capa_MgF = Layer("MgF2")
    capa_ZnS = Layer("ZnS")
    capa_InGaP = Layer("InGaP")
    capa_GaAs = Layer("GaAs")

    cell2 = Bulk(capa_MgF, capa_ZnS, capa_InGaP, capa_GaAs)

    cell2.RT()

    pyplot.figure(figsize=(8, 6), dpi=300, facecolor="w", edgecolor="k")
    pyplot.plot(capa_GaAs.lambd, cell2.R, linewidth=0.5)
    pyplot.xlabel("Wave length (nm)", {"fontsize": 15})
    pyplot.ylabel("Reflectance (%)", {"fontsize": 15})
    pyplot.title("Reflectance", {"fontsize": 15})
    pyplot.grid(True)
    pyplot.savefig("reflectane.pdf")
    pyplot.close()

    pyplot.figure(figsize=(8, 6), dpi=300, facecolor="w", edgecolor="k")
    pyplot.plot(capa_GaAs.lambd, cell2.T, linewidth=0.5)
    pyplot.xlabel("Wave length (nm)", {"fontsize": 15})
    pyplot.ylabel("Transmitance (%)", {"fontsize": 15})
    pyplot.title("Transmitance", {"fontsize": 15})
    pyplot.grid(True)
    pyplot.savefig("transmitance.pdf")
    pyplot.close()


if __name__ == "__main__":
    main()
