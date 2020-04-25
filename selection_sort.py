from random import *


def selection_sort(list):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
    return list


list = [randint(1, 1000) for i in range(10)]
print(f'Your start list: {list}\nSorting list: {selection_sort(list)}')
