# 2019 - 02 -12
# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            return True
        else:
            return False
    else:
        if (a < 0 and not b < 0) or (b < 0 and not a < 0):
            return True
        else:
            return False

if __name__ == '__main__':
    print(pos_neg(1, -1, False)) # -> True
    print(pos_neg(-1, 1, False)) # -> True
    print(pos_neg(-4, 5, True)) # -> True