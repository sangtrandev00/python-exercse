n = int(input())
# Nhập n số nguyên từ bàn phím
lst = []
for i in range(n):
    # print("Nhap: ")
    lst.append(int(input()))


# Tìm số nguyên nhỏ nhất!
min = lst[0]
for i in lst:
    if(min > i):
        min = i
print(min)
