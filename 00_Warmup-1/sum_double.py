# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    sum = a + b
    if a == b:
        return sum * 2
    else:
        return sum


if __name__ == '__main__':
    print(sum_double(13, 12))