from random import shuffle


def max_min(lst):
    """
    calcule o maximo e o minimo de uma lista lts
    :param lst: lista
    :return: tuple: (max, min)
    """
    if len(lst) == 0: # lst = [1, ... 99]
        raise ValueError('Lista Vazia')
    max_valor = min_valor = lst[0]

    for valor in lst:
        if valor > max_valor:
            max_valor = valor
        if valor < min_valor:
            min_valor = valor

    return max_valor, min_valor # 0(n)

print(max_min([1])) # 1, 1
print(max_min([1, 2])) # 2, 1
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min((random_list)))
print(max_min([]))
