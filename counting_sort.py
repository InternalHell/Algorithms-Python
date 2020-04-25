from random import *
def counting_sort(list):
    arr = [0] * (max(list)+1)
    for i in list:
        arr[i] += 1
    position = 0
    for i in range(len(arr)):
        for x in range(arr[i]):
            list[position] = i
            position += 1
    return list
list = [randint(1,100) for i in range(100)]
print(f'This is COUNTING SORT\n\n\nYour list: {list}\nSortin list: {counting_sort(list)}')