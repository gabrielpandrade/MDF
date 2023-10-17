import numpy as np


def cria_matriz_vetor_auxiliar_von_neumann(dx: float, fx: np.ndarray, gx: np.ndarray, nx: int, nt: int):
    """
    Função para criar a matriz de vetores auxiliares para condições de fronteira de von Neumann

    :param dx: passo no espaço
    :param fx: fronteira esquerda
    :param gx: fronteira direita
    :param nx: número de pontos no espaço
    :param nt: número de pontos no tempo
    :return: matriz de vetores auxiliares
    """
    c = np.zeros((nt, nx))
    for i in range(nt):
        c[i][0] = -2*dx*fx[i]
        c[i][-1] = -2*dx*gx[i]
    return c