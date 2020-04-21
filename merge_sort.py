from random import *
def merge_sort(list):
    if len(list) <= 1:
        return list 
    result = []
    middle = len(list) // 2
    l = merge_sort(list[:middle])
    r = merge_sort(list[middle:])
    while len(l) > 0 and len(r) > 0:
        if l[0] < r[0]:
            result.append(l[0])
            l.pop(0)
        else:
            result.append(r[0])
            r.pop(0)
    if l:
        result += l
    if r:
        result += r
    return result
array = [randint(1,100) for i in range(10)]
print(f'lenght array: {len(array)}\nStart list: {array}\nEnd list: {merge_sort(array)}\nlength array end: {len(merge_sort(array))}')
