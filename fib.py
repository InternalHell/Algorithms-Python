def fib(n):
    fib = [0,1] + [0] * (n - 1)
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
a = int(input('Напиши любое число для просчёта числа фибоначи:\n-->'))
print(f'Твоё число: {a}\nИндекс числа фибоначи: {fib(a)}')
