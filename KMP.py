def prefix_function(list):
    p = [0 for i in range(len(list))]
    j = 0
    i = 1
    while i != len(list):
        if list[i] == list[j]:
            p[i] = j + 1
            j += 1
            i += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j-1]
    return p


def prefix_function1(list):
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


a = 'abcdefgrtyuioplkjh'
b = 'grte'
print(kmp(b, a))
