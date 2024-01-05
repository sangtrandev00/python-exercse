n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i/(i+1)
sum = round(sum, 2)
print(sum)
print("Gia tri cua bieu thu la: "+str(sum))
