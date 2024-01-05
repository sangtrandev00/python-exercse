s = str(input())


def format(s):
    if len(s) >= 3:
        if "ing" in s[-3:]:
            s = s + "ly"
            return s
        else:
            s += "ing"
            return s
    else:
        return s


print(format(s))
