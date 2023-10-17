import numpy as np

from MDF.funcoes.distribuicao_normal import distribuicao_normal
from MDF.plotagem.plot_2D import plot_2D
from MDF.plotagem.plot_3D import plot_3D
from MDF.utils.calcula_dados import calcula_dados


class ExplicitoDirichlet:
    """
    Classe para realizar discretização pelo método de Euler Explícito

    Atributos
    ---------
    dados : dict
        L0 : float
            Posição inicial no espaço
        Ln : float
            Posição final no espaço
        T : float
            Tempo
        nx : int
            Número de pontos no espaço
        nt : int
            Número de pontos no tempo
        L : float
            Tamanho do espaço Ln - L0
        dx : float
            Passo no espaço L / (nx - 1)
        dt : float
            Passo no tempo T / (nt - 1)
        sigma : float
            Coeficiente calculado por dt / dx^2
        x : numpy.ndarray
            Vetor contendo todos os valores do espaço
        t : numpy.ndarray
            Vetor contendo todos os valores do tempo
        u : numpy.ndarray
            Matriz (nt x nx) contendo zeros para preencher com a solução numérica ponto a ponto

    Métodos
    -------
    set_dados(L0, Ln, T, nx, nt, cont, fronte, frontd)
        Muda os dados para a discretização
    set_condicao_inicial(cond)
        Muda a condição inicial para a discretização
    set_fronteira_esquerda(fronte)
        Muda a fronteira esquerda
    set_front_direita(frontd)
        Muda a fronteira direita
    calcula()
        Aplica a discretização
    plota_2D(plots)
        Plota o resultado no formato de evoluções em 2D
    plota_3D()
        Plota o resultado em um gráfico de distribuição 3D
    """
    def __init__(self, L0: float, Ln: float, T: float, nx: int, nt: int, a: float):
        """
        Função para iniciaizar a discretização

        :param L0: Posição inicial em x
        :param Ln: Posição final em x
        :param T: Tempo total
        :param nx: Número de pontos no espaço
        :param nt: Número de pontos no tempo
        :param a: Coeficiente de difusão
        """
        self.dados = None
        self.set_dados(L0, Ln, T, nx, nt, a)

    def set_dados(self, L0: float, Ln: float, T: float, nx: int, nt: int, a: float, cond="dist_norm", fronte="zeros",
                  frontd="zeros"):
        """
        Função para mudar os dados para a discretização

        :param L0: Posição inicial em x
        :param Ln: Posição final em x
        :param T: Tempo total
        :param nx: Número de pontos no espaço
        :param nt: Número de pontos no tempo
        :param a: Coeficiente de difusão
        :param cond: (opcional) Condição inicial
        :param fronte: (opcional) Fronteira esquerda
        :param frontd: (opcional) fronteira direita
        """
        self.dados = calcula_dados(L0, Ln, T, nx, nt, a)
        self.set_condicao_inicial(cond)
        self.set_fronteira_esquerda(fronte)
        self.set_fronteira_direita(frontd)
        self.calcula()

    def set_condicao_inicial(self, cond):
        """
        Função para mudar a condição inicial

        :param cond: Condição inicial
        """
        if cond == "dist_norm":
            self.dados["u"][0] = distribuicao_normal(self.dados["x"], 1.5, 0.3)

    def set_fronteira_esquerda(self, fronte):
        """
        Função que muda a fronteira esquerda

        :param fronte: Fronteira esquerda
        """
        if fronte == "zeros":
            self.dados["fx"] = np.zeros(self.dados["nt"]-1)

    def set_fronteira_direita(self, frontd):
        """
        Função que muda a fronteira direita

        :param frontd: Fronteira direita
        """
        if frontd == "zeros":
            self.dados["gx"] = np.zeros(self.dados["nt"] - 1)

    def calcula(self):
        """
        Função que realiza os cálculos da discretização

        u[i+1][0] = fx[i]\n
        u[i+1][j] = u[i][j] + sigma * (u[i][j-1] - 2u[i][j] + u[i][j+1])\n
        u[i+1][nt-1] = gx[i]
        """
        for i in range(self.dados["nt"] - 1):
            self.dados["u"][i + 1][0] = self.dados["fx"][i]
            for j in range(1, self.dados["nx"] - 1):
                self.dados["u"][i + 1][j] = self.dados["u"][i][j] + self.dados["sigma"] * (
                            self.dados["u"][i][j - 1] - 2 * self.dados["u"][i][j] + self.dados["u"][i][j + 1])
            self.dados["u"][i + 1][-1] = self.dados["gx"][i]

    def plota_2D(self, plots: int):
        """
        Função que plota o resultado no formato de evoluções em 2D

        :param plots: Número de plotagems
        """
        plot_2D("Evolução do Método Explícito",
                self.dados["nt"],
                int(self.dados["nt"] / plots),
                self.dados["x"],
                self.dados["t"],
                self.dados["u"]
                )

    def plota_3D(self):
        """
        Função que plota o resultado em um gráfico de distribuição 3D
        """
        plot_3D("Evolução do Método Explícito",
                self.dados["x"],
                self.dados["t"],
                self.dados["u"]
                )