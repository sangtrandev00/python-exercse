lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
lstOdd = []

for i in lst:
    if(i % 2 != 0):
        lstOdd.append(i)
        # print(lstOdd)
print(lstOdd)
