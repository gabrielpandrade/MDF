def cria_vetor_coeficientes_g(alfa: float, nx: int):
    """
    Gera vetor dos coeficientes G para discretização de Grunwald-Letnikov

    :param alfa: Ordem da derivada
    :param nx: Número de pontos no espaço
    :return: O vetor com os coeficientes G
    """
    g = [1]
    for i in range(1, nx):
        g.append((1 - ((alfa + 1) / i)) * g[i - 1])
    return g