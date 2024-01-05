s = str(input())
finalStr = s[0:2] + s[-2:]
if len(s) < 2:
    finalStr = ""
print(finalStr)
