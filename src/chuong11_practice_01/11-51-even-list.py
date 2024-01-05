# Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)


def evenNum(res):
    finalList = []
    for i in res:
        if(i % 2 == 0):
            finalList.append(i)
    return finalList


# evenNum(res)
print(evenNum(res))
