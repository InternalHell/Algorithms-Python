def radix_sort(list, radix=10): # radix - система счисления
    """
    :param arr: Iterable of elements to sort.
    :param radix: Base of input numbers
    :return: Sorted list of input.
    Time complexity: O(d * (n + b))
    Space complexity: O(n + k)
    where, k is the range of input.
    """
    max = False
    digit = 1
    while not max:
        max = True # Значит цикл идёт 1-ин раз
        # Создаём список в списке с индексами, от 0 до 9
        a = [[] for i in range(radix)]
        # Добавляем в созданные списки числа, если же tmp при делении будет выдовать 0, то цикл после продолжения закончится
        for i in list:
            tmp = i // digit # какой разряд смотрим, если делит на 1, то 1-ый разряд
            a[tmp % radix].append(i)
            if max and tmp > 0:
                max = False
        # Обновляем список с отсортированными разрядами
        add = 0
        for b in range(radix):
            a_copy_index = a[b]
            for i in a_copy_index:
                list[add] = i
                add += 1
        # После окончания итерации с 1-ым разрядом, переходим ко 2-ому, * на 10
        digit *= radix
    return list

def main():
    """
    Test radix sort
    """
    test = [int(i) for i in input().split()]
    print('Sorted array:', radix_sort(test))
    
if __name__ == '__main__':
    main()