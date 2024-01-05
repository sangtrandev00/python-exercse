n = int(input())


def sumOfAll(n):
    list = []
    i = 1
    sum = 0
    while i <= n:
        if n % i == 0:
            # print(i)
            list.append(i)
            sum += i
        i += 1
    return sum - n


print(sumOfAll(n))
