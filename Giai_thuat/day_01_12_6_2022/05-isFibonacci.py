

def isFibonacci(k):
    f_0 = 1
    f_1 = 1
    f_n = f_0 + f_1
    if k == 1 or k == 2:
        return True

    while f_n <= k:
        f_n = f_0 + f_1  # 2
        f_0 = f_1  # 1
        f_1 = f_n  # 2
        if(f_n == k):
            return True
    return False


print(isFibonacci(13))
