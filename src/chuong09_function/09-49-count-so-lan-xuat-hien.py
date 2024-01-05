from unittest.result import failfast


def get_unique_values(lst):
    finalList = []
    for i in lst:
        if(i not in finalList):
            finalList.append(i)
    return finalList


n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(get_unique_values(lst))
