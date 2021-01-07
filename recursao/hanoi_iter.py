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
    stack = [(False, n, origem, auxiliar, destino)]

    while stack:
        print_flag, n, origem, auxiliar, destino = stack.pop()
        if n < 1:
            continue
        if not print_flag:
            stack.append((True, n, origem, auxiliar, destino))
            stack.append((False, n - 1, origem, auxiliar, destino))
        else:
            print(f'{origem} -> {destino} : {n}')
            stack.append((False, n - 1, auxiliar, origem, destino))


for i in range(1, 4):
    print('################# Hanoi %s' % i)
    hanoi(i)
