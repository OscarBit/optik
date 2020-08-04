import numpy as np
import matplotlib.pyplot as plt
import optik2 as optik


def main():
    capa_MgF = optik.lego("MgF2")
    capa_ZnS = optik.lego("ZnS")
    capa_InGaP = optik.lego("InGaP")
    capa_GaAs = optik.lego("GaAs")

    cell2 = optik.lego_tower(capa_MgF, capa_ZnS, capa_InGaP, capa_GaAs)

    cell2.RT()

    plt.figure(figsize=(8, 6), dpi=300, facecolor="w", edgecolor="k")
    plt.plot(capa_GaAs.lambd, cell2.R, linewidth=0.5)
    plt.xlabel("Wave length (nm)", {"fontsize": 15})
    plt.ylabel("Reflectance (%)", {"fontsize": 15})
    plt.title("Reflectance", {"fontsize": 15})
    plt.grid(True)
    plt.savefig("reflectane.pdf")
    plt.close()

    plt.figure(figsize=(8, 6), dpi=300, facecolor="w", edgecolor="k")
    plt.plot(capa_GaAs.lambd, cell2.T, linewidth=0.5)
    plt.xlabel("Wave length (nm)", {"fontsize": 15})
    plt.ylabel("Transmitance (%)", {"fontsize": 15})
    plt.title("Transmitance", {"fontsize": 15})
    plt.grid(True)
    plt.savefig("transmitance.pdf")
    plt.close()


if __name__ == "__main__":
    main()
