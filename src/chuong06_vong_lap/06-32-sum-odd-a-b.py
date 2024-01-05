a = int(input())
b = int(input())
sumOdd = 0
for i in range(a, b+1):
    if(i % 2 !=0): 
        sumOdd += i
print(sumOdd)
