def insertion_sort(list):
    for index in range(1,len(list)):
        while index > 0 and list[index] < list[index-1]:
            list[index],list[index-1] = list[index-1], list[index]
            index -= 1
a = [123,55,212,612,63,1,6,7,3,323,44,12,16,15,17,18,256,77,22,33,31,35,99]
insertion_sort(a)
print(a)
