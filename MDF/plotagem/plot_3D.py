from matplotlib import pyplot as plt
import numpy as np


def plot_3D(titulo, x, t, u, xlabel="x", ylabel="y", zlabel="z"):
    """
    Plota em 3 dimensões

    :param titulo: Título do gráfico
    :param x: Valores de x
    :param t: Valores de t
    :param u: Valores de u
    :param xlabel: Nome do eixo x
    :param ylabel: Nome do eixo y
    :param zlabel: Nome do eixo z
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, T = np.meshgrid(x, t)
    surf = ax.plot_surface(X, T, u, cmap='hot')
    fig.colorbar(surf)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(titulo)
    plt.show()