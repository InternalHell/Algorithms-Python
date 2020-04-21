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
b = 'aaahello'
a = 'ewqrt'
print(lev(a,b))