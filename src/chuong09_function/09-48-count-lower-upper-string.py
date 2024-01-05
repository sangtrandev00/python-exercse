from itertools import count


def show(s):
    countUpper = 0
    countLower = 0
    for i in s:
        # print(i, end=' ')
        if(i.isupper() == True):
            countUpper += 1
        if(i.islower() == True):
            countLower += 1

    print("Given string: "+s)
    print("Number of uppercase letters: "+str(countUpper))
    print("Number of lowercase letters: "+str(countLower))


s = str(input())
show(s)
