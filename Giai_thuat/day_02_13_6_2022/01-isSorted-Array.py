def isSortedArray(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i + 1] < arr[i]:
            return False
        i += 1
    return True


print(isSortedArray([1, 2, 6, 4, 5]))
