from random import shuffle


def max_min(lst):
    """
    calcule o maximo e o minimo de uma lista lts
    :param lst: lista
    :return: tuple: (max, min)
    """
    n = len(lst)
    if n == 0:
        raise ValueError('Lista Vazia')
    max_valor = min_valor = lst[-1]

    def max_min_rec(cursor):
        """
        t(n) = 1 + t(n-1)
        t(n) = 1 + 1 + t(n-2)
        t(n) = 1 + 1 + 1 + t(n-3)
        t(n) = 1 + 1 + 1 + ...t(n-1)
        t(n) = n + 1 => 0(n)

        m(m)
        :param cursor:
        :return:
        """
        nonlocal max_valor, min_valor
        if cursor < 0:
            return max_valor, min_valor
        corrente = lst[cursor]
        if corrente > max_valor:
            max_valor = corrente
        if corrente < min_valor:
            min_valor = corrente
        return max_min_rec (cursor - 1)

    return max_min_rec(n - 1)

print(max_min([1])) # 1, 1
print(max_min([1, 2])) # 2, 1
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min((random_list)))
print(max_min([]))
