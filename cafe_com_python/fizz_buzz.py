def fizz_buzz(n: int):
    """
    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz


    :param n:
    :return:
    """
    for i in range(1, n + 1):  #i=2 n=6
        resultado = ''

        if i % 2 == 0:
            resultado = 'Fizz'
        if i % 3 == 0:
            resultado += "Buzz"

        print(resultado if resultado != '' else i)  #1 Fizz 3 Fizz 5 fizz