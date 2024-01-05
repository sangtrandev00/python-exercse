def max3(a, b, c):
    max = a
    if(max < b):
        max = b
    if(max < c):
        max = c
    return max


a = int(input())
b = int(input())
c = int(input())
print(max3(a, b, c))
