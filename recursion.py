def hello(x):
    if x == 1:
        return 1
    return x + hello(x-1)
a = int(input('Say number:\n--> '))
print(hello(a))
