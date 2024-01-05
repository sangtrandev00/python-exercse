a = int(input())
b = int(input())


# def gcd(a, b):
#     while a != b:
#         if(a < b):
#             b = b - a
#         if(a > b):
#             a = a - b
#     return a


# print(gcd(a, b))


def gcdRecursion(a, b):
    if(a == b):
        return a
    if(a < b):
        # b = b - a
        return gcdRecursion(a, b - a)
    if(b < a):
        # a = a - b
        return gcdRecursion(a - b, b)


print(gcdRecursion(a, b))
