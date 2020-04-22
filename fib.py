def fib(n):
    assert n >= 0, 'Error'
    fib = [None] * (n + 1)
    fib[:2] = [0,1]
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
a = int(input('Напиши любое число для просчёта числа фибоначи:\n-->'))
print(f'Твоё число: {a}\nЧисло фибоначи: {fib(a)}')


def fac(n):
    assert n >= 0, 'Error'
    list = [1] + [None] * n
    for i in range(1, n+1):
        list[i] = list[i-1] * i
    return list[n]
print('\n',fac(12))
