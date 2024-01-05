import math


def is_prime(n):
    i = 2
    check = 0
    if(n < 2):
        return False
    while i <= math.sqrt(n):
        if n % i == 0:
            check = 1
            break
        i += 1

    if check == 0:
        return True
    else:
        return False


n = int(input())
print(is_prime(n))
