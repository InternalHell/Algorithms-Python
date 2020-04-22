def r(m, v, n):
    list = [[0]*(n+1) for i in range(10+1)]
    for i in range(1, n):
        for k in range(1, 10+1):
            if m[i] <= k:
                list[k][i] = max(list[k][i-1], v[i] + list[k-m[i]][i-1])
            else:
                list[k][i] = list[k][i-1]
    return list


m = [3, 4, 4, 3]
v = [4, 4, 6, 3]
print(r(m, v, len(m)))
