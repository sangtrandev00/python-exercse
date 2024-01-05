
# Thuật toán bị quá hạn thời gian!

def findSequence(num):
    if num >= 0 and num < 10:
        return True

    arr = list(str(num))
    i = 0
    while i < len(arr) - 1:
        distance = int(arr[i + 1]) - int(arr[i])
        if distance != 1:
            return False
        i += 1
    return True


def sequenceNumber(l, r):
    list = []
    for i in range(l, r+1):
        if findSequence(i):
            list.append(i)

    return list


# print(findSequence(890))
print(sequenceNumber(2334, 2132384))
