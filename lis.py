def lis(list):
    F = [0] * (len(list) + 1)
    for i in range(1,len(list) + 1):
        m = 0
        for j in range(0,i):
            if list[i-1] > list[j-1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return F
    for i in F:
        print(i)

array = 'hhll'
print(array)
print(lis(array))
