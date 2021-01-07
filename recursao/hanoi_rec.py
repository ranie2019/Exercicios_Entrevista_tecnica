def hanoi(n, origem='A', auxiliar='B', destino='C'):
    """
    Solucao Recursiva para a Torre de Hanoi
    t(n) = 1 + 2(t(n-1))
    t(n) = 1 + 2 + 4(t(n-2))
    t(n) = 1 + 2 + 4 + 8(t(n-3))
    t(n) = 1 + 2 + 4 + 8 + 16(t(n-4))
    t(n) = 1 + 2 + 4 + 8 + 16 +32 ... 2**(n+1)

    t(n)=2**(n+1)-1 => 0(2**n)
    m(n) = 1 + m(n-1)
    """
    if n >= 1:
        hanoi(n - 1, origem, destino, auxiliar)
        print(f'{origem} -> {destino} : {n}')
        hanoi(n - 1, auxiliar, origem, destino)

for i in range(1, 4):
    print('################# Hanoi %s' % i)
    hanoi(i)
