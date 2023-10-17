from matplotlib import pyplot as plt


def plot_2D(titulo, nt, plots, x, t, u, xlabel="x", ylabel="y"):
    """
    Plota em 2 dimensões

    :param titulo: Titulo do gráfico
    :param nt: Número de pontos no tempo
    :param plots: Intervalo entre os plots
    :param x: Valores de x
    :param t: Valores de t
    :param u: Valores do u
    :param xlabel: Nome do eixo x
    :param ylabel: Nome do eixo y
    """
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for n in range(nt):
        if n % plots == 0:
            plt.plot(x, u[n], label="{:.1f}".format(t[n]))
    plt.legend()
    plt.show()
