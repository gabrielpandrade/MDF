import numpy as np


def cria_matriz_tridiagonal(dsub: float, dprinc: float, dsup: float, n: int):
    """
    Função para criar matriz tridiagonal

    :param dsub: Elementos da diagonal inferior
    :param dprinc: Elementos da diagonal principal
    :param dsup: Elementos da diagonal superior
    :param n: Tamanho da matriz

    :return: A matriz tridiagonal
    """
    A = np.zeros((n, n))
    np.fill_diagonal(A, dprinc)
    for i in range(n):
        for j in range(n):
            if i == j+1:
                A[i][j] = dsub
            if i == j-1:
                A[i][j] = dsup
    return A