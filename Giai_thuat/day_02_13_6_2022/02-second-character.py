# Chua giai quyet duoc!
def secondChar(s):
    arr = list(str(s))
    dict = {

    }

    for i in range(len(arr)):
        # dict[arr[i]] = i
        if arr[i] not in dict:
            dict[arr[i]] = 1
        else:
            dict[arr[i]] += 1
    mydict = dict.copy()
    for x, y in mydict.items():
        # print(x, y)
        # 3 == max --> tim max
        if y == 3:
            dict.pop(x)

    return dict


print(secondChar("trannhatsang"))
