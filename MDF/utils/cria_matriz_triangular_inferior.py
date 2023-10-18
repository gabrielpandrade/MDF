import numpy as np


def cria_matriz_triangular_inferior(g: np.ndarray, n: int, sigma: float):
    """
    Gera matriz triangular para a disretização de Grunwald-Letnikov

    :param g: Vetor dos coeficientes G
    :param n: Tamanho da matriz
    :param sigma: Sigma
    :return: Matriz triangular
    """
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if (i - j) == -1:
                A[i][j] = -sigma * g[0]
            elif i == j:
                A[i][j] = 1 - sigma * g[1]
            elif (i - j) > 0:
                A[i][j] = -sigma * g[(i - j) + 1]
    return A