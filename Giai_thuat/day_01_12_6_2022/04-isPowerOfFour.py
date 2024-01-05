import math


def isPowerOfFour(n):
    while(n > 1):
        n /= 4
    if n == 1:
        return True
    return False


# print(math.log(64, 4))

print(isPowerOfFour(64))
# print(math.pow(4, 2))
