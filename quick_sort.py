from random import randint
def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0];l,m,r = [i for i in list if i < pivot],[i for i in list if i == pivot],[i for i in list if i > pivot]
    return quick_sort(l) + m + quick_sort(r)
a = [randint(1,100) for i in range(90000)]
#print(f'This is you start list: {a}\nThis is new list: {quick_sort(a)}')

