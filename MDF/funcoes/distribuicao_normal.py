import numpy as np


def distribuicao_normal(x, media, desvio_padrao, escalar=1):
    temp = []
    for p in x:
        temp.append(escalar * ((2 / (np.sqrt(2 * np.pi * (desvio_padrao ** 2)))) * np.exp((-1 * (p - media) ** 2) / (2 * (desvio_padrao ** 2)))))
    return temp