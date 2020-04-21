

# Бинарный-Двоичный поиск

# Исполнение благодаря while

def binary_search1(list, x):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low+high)//2
        if list[mid] == x:
            return list[mid]
        if list[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return 'Your number not found'


a = list(range(1, 129))
try:
    x = int(input('Say number\n--> '))
    print(binary_search1(a, x))
except:
    print('ERROR')

# Исполнение благодаря рекурсии


def binary_search2(list, x, low, high):
    mid = (low+high)//2
    if low > high:
        return 'Not found'
    else:
        if list[mid] == x:
            return mid
        if list[mid] < x:
            return binary_search2(list, x, mid+1, high)
        else:
            return binary_search2(list, x, low, mid-1)


list = [1, 2, 5, 7, 8, 12, 15, 17, 27, 31, 35, 38, 50]
high = len(list) - 1
low = 0
x = int(input('Say number\n--> '))
print(binary_search2(list, x, low, high))


# Линейный поиск

# Исполнение благодаря рекурсии

def local_search1(x, list, start):
    if start == len(list):
        return 'Faild'
    if list[start] == x:
        return start
    else:
        return local_search1(x, list, start+1)


x = 22
list = [1, 2, 4, 6, 8, 9, 9, 10, 12, 15, 17, 18, 22]
start = 0
print(local_search1(x, list, start))


# Исполнение благодаря while

def local_search2(list, x):
    start = 0
    while start < len(list):
        if list[start] == x:
            return start
        else:
            start += 1
    return 'Not Found'


x = 1
list = [1, 2, 3, 4, 6, 8, 9, 11, 12, 22, 33, 44, 55]
print(local_search2(list, x))


def local_search3(list, x):
    
    for i in list:
        if i == x:
            return i
        elif i == list[len(list)-1]:
            return 'Not found'


x = int(input('Say your number:\n--> '))
list = [1, 2, 3, 4, 6, 8, 9, 11, 12, 22, 33, 44, 55]
print(local_search3(list, x))
