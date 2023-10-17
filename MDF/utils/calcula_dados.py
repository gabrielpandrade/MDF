import numpy as np


def calcula_dados(L0: float, Ln: float, T: float, nx: int, nt: int, a: float):
    """
    Função que calcula os dados iniciais necessários para a discretização

    :param L0: float
        Posição inicial no espaço
    :param Ln: float
        Posição final no espaço
    :param T: float
        Tempo
    :param nx: int
        Número de pontos no espaço
    :param nt: int
        Número de pontos no tempo
    :param a: float
        Coeficiente de difusão

    Retorno
    -------
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
        a : float
            Coeficiente de difusão
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
            Matriz nt x nx contendo zeros para preencher com a solução numérica ponto a ponto
        fx : numpy.ndarray
            Vetor contendo as condições de fronteira na esquerda
        gx : numpy.ndarray
            Vetor contendo as condições de fronteira na direita
    """
    dados = {"L0": L0,
             "Ln": Ln,
             "T": T,
             "nx": nx,
             "nt": nt,
             "a": a,
             "L": Ln - L0,
             "fx": np.zeros(nt-1),
             "gx": np.zeros(nt-1)
             }
    dados["dx"] = dados["L"] / (nx - 1)
    dados["dt"] = dados["T"] / (nt - 1)
    dados["sigma"] = dados["dt"] * dados["a"] / (dados["dx"]**2)
    dados["x"] = np.linspace(dados["L0"], dados["Ln"], dados["nx"])
    dados["t"] = np.linspace(0, dados["T"], dados["nt"])
    dados["u"] = np.zeros((dados["nt"], dados["nx"]))
    return dados