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