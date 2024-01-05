def sum_of_three(s):
    # if float(s) != int(s):
    #     return False

    # snum = int(s)
    # if snum % 3 == 0 and snum >= 3:
    #     return True

    # return False
    return float(s) % 3 == 0

# Tại sao là return float(s) % 3 == 0 ?


print(sum_of_three(33))
