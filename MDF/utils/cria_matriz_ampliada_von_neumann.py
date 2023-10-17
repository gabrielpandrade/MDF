from MDF.utils.cria_matriz_tridiagonal import cria_matriz_tridiagonal


def cria_matriz_ampliada_von_neumann(dsub: float, dprinc: float, dsup: float, asim: float, nx: int):
    """
     Função para criar matriz ampliada para fronteira dupla de von neumann

    :param dsub: Elementos da diagonal inferior
    :param dprinc: Elementos da diagonal principal
    :param dsup: Elementos da diagonal superior
    :param asim: Elemento assimétrico
    :param nx: Tamanho da matriz

    :return: A matriz ampliada para fronteira dupla de von Neumann
    """
    A = cria_matriz_tridiagonal(dsub, dprinc, dsup, nx)
    A[0][1] = asim
    A[-1][-2] = asim
    return A