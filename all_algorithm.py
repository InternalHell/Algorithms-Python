list = [None] * 990
def fib_hash(n):
    assert n >= 0 and n <= 990
    if list[n] is None:
        if n <= 1:
            list[n] = n
        else:
            list[n] = fib_hash(n-1) + fib_hash(n-2)
    return list[n]
def fac(n):
    assert n >= 0, 'Error'
    list = [1] + [None] * n
    for i in range(1, n+1):
        list[i] = list[i-1] * i
    return list[n]
def fib(n):
    assert n >= 0, 'Error'
    fib = [None] * (n + 1)
    fib[:2] = [0,1]
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
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
def bubble_sort(list):
    last = len(list)-1
    a = 0
    for i in range(last):
        for x in range(last):
            if list[x] > list[x+1]:
                list[x],list[x+1] = list[x+1],list[x]
            a += 1
    return list
def insertion_sort(list):
    for index in range(1,len(list)):
        while index > 0 and list[index] < list[index-1]:
            list[index],list[index-1] = list[index-1], list[index]
            index -= 1
    return list
def selection_sort(list):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
    return list
def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    l = [i for i in list if i < pivot]
    m = [i for i in list if i == pivot]
    r = [i for i in list if i > pivot]  
    return quick_sort(l) + m + quick_sort(r)
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
def radix_sort(list,radix=10):
    max = False
    digit = 1
    while not max:
        max = True
        a = [[] for i in range(radix)]
        for i in list:
            tmp = i//digit
            a[tmp%radix].append(i)
            if max and tmp > 0:
                max = False
        position = 0
        for i in range(radix):
            a_index = a[i]
            for j in a_index:
                list[position] = j
                position += 1
        digit *= radix
    return list
def lcs(list,array):
    F = [[1] * (len(array) + 1) for i in range(len(list) + 1)]
    for i in range(1,len(list)+ 1):
        for j in range(1,len(array)+1):
            if list[i-1] == array[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i][j-1], F[i-1][j])
    for i in F:
        print(i)
def lis(list):
    F = [0] * (len(list) + 1)
    for i in range(1,len(list) + 1):
        m = 0
        for j in range(0,i):
            if list[i-1] > list[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F
def lev(first,second):
    result = [[(i+j) if i*j==0 else 0 for j in range(len(second)+1)]for i in range(len(first)+1)]
    for i in range(1,len(first)+1):
        for j in range(1,len(second)+1):
            if first[i-1] == second[j-1]:
                result[i][j] = result[i-1][j-1]
            else:
                result[i][j] = 1 + min(result[i-1][j-1], result[i-1][j], result[i][j-1])
    for i in result:
        print(i)
def equal(first,second):
    if len(first) != len(second):
        return False
    for i in range(len(first)):
        if first[i] != second[i]:
            return False
    return True
def search_substring(first,second):
    for i in range(len(first)-len(second)+1 ):
        if equal(first[i:len(second)+i],second):
            print(f'index: {i}')
def prefix_function(list):
    p = [0 for i in range(len(list))]
    j = 0
    for i in range(1, len(list)):
        if list[j] == list[i]:
            p[i] = j + 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
            else:
                j = p[j-1]
            if list[j] == list[i]:
                p[i] = j + 1
                j += 1
    return p
def kmp(s, word):
    p = prefix_function(word)
    i = j = 0
    while i != len(word) and j != len(s):
        if word[i] != s[j] and j != 0:
            j = p[j-1]
        if word[i] == s[j]:
            i += 1
            j += 1
        else:
            i += 1
    return j == len(s)
stack = []
def is_bracket_sequence_correct(x: str):
    for i in x:
        if i not in '()[]':
            continue
        if i in '([':
            stack.append(i)
        else:
            assert i in ')]', 'Error:\n' + str(i)
            if len(stack) == 0:
                return False
            left = stack.pop()
            assert left in '[(', 'Error2' + str(left)
            if left == '(':
                right = ')'
            if left == '[':
                right = ']'
            if right != i:
                return False
    return len(stack) == 0
def knapsack_without_repeats(capacity, weight_list):
    cost = 1
    previous = [0] * (capacity + 1)
    for i in range(1, len(weight_list) + 1):
        current = [0]
        for w in range(1, capacity + 1):
            current.append(previous[w])
            if weight_list[i - 1] <= w:
                current[w] = max(current[w], previous[w - weight_list[i - 1]] + cost * weight_list[i - 1])
        previous = current
    return previous[capacity] // cost