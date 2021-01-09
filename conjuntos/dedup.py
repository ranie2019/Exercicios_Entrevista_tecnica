def dedup(lst):
    """Remova listas duplicadas

    :param lst: a list
    :return: nem list whithout duplicated elements

    linear para o tempo e espaco
    """
    result = []
    repeated = set()

    for ele in lst:
        if ele in result:
            result.append(ele)
            repeated.add(ele)
    return set(lst)

print(dedup(['banana', 'banana', 'banana', 'abacaxi', 'caqui']))
