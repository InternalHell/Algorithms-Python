from random import randint
def bubble_sort(list):
    last = len(list)-1
    a = 0
    for i in range(last):
        for x in range(last):
            if list[x] > list[x+1]:
                list[x],list[x+1] = list[x+1],list[x]
            a += 1
    return print(f'Отсортированный массив:\n{list}\nВыполнен за {a} шагов')
#list = [10,75,43,15,25,-4,27]
#print('start:',list)
#end_list = bubble_sort(list)
#print('end:',end_list)
a = [randint(1,100) for i in range(5)]
bubble_sort(a)
