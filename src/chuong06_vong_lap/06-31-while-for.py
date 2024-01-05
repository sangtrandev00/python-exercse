i = 1
n = int(input())
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)
# Dùng for in range()
n2 = int(input())
sum2 = 0
for i in range(1, n2):
    sum2 += i

sum2 += n2
print(sum2)
