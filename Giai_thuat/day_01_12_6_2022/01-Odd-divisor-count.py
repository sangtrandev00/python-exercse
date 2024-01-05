
def timUoc(a):
    i = 1
    list = []
    while(i <= a):
        if a % i == 0:
            list.append(i)
        i += 1
    return list

# print(timUoc(12))


def solve(a, b):
    count = 0
    for i in range(a, b + 1):
        if(len(timUoc(i)) % 2 != 0):
            count += 1
    return count


# print(solve(1, 9))
