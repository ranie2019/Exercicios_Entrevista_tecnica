from collections import Counter


def contar_letras(s: str):
    """
    >>> contar_letras('ranie')
    {'r': 1, 'a': 1, 'n': 1, 'i': 1, 'e': 1}
    >>> contar_letras('Rranie')
    {'R': 1, 'r': 1, 'a': 1, 'n': 1, 'i': 1, 'e': 1}
    >>> contar_letras('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s:
    :return:
    """

    dct = {}
    for letras in s:
        dct[letras] = dct.get(letras, 0) + 1

    return dct