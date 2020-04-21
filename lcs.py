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
list = [1,2,3,4,5,6,7,8,9,10]
array = [1,2,3,4,5,6,7,8,9,10]
print(f'start: {list,array}\nend: {lcs(list,array)}')
