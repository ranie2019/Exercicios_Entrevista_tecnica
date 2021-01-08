def binary_sum(n, n2):
    """n  e n2 nao sao numero negativos binarios
    '0001010101010101010101010101010010101010'
    """
    n = int(n, 2)
    n2 = int(n2, 2)
    last_d_sum = 0
    return format(n + n2, 'b')

print(binary_sum('111110', '1100')) #1001010
