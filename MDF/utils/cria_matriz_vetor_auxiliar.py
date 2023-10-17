import numpy as np


def cria_matriz_vetor_auxiliar(sigma: float, fx: np.ndarray, gx: np.ndarray, nx: int, nt: int):
    """
    Função para criar a matriz de vetores auxiliares

    :param sigma: sigma
    :param fx: fronteira esquerda
    :param gx: fronteira direita
    :param nx: número de pontos no espaço
    :param nt: número de pontos no tempo
    :return: matriz de vetores auxiliares
    """
    c = np.zeros((nt, nx))
    for i in range(nt):
        c[i][0] = sigma * fx[i]
        c[i][-1] = sigma * gx[i]
    return c