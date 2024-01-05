# n = int(input())
# # Nhập n số nguyên từ bàn phím
# lst = []
# for i in range(n):
#     # print("Nhap: ")
#     lst.append(input())
# number = int("".join(lst))
# print(number)
# print(type(number))


# Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    n = str(n)
    res.append(n)

print(int("".join(res)))
