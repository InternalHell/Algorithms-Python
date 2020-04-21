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
a = 'asdasddsasddassaaddsasddsasdasdafasddsadddsaaasddasdssdasadasddsad'
b = 'sad'
search_substring(a,b)