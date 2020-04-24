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
print('\n'+fac(12))

# Функция фибоначчи методом хэширования
list = [None] * 990
def fib_hash(n):
    assert n >= 0 and n <= 990
    if list[n] is None:
        if n <= 1:
            list[n] = n
        else:
            list[n] = fib_hash(n-1) + fib_hash(n-2)
    return list[n]
print(fib_hash(20))
