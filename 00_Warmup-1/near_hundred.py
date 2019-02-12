# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    near = abs(100-n)
    if near <= 10 or (abs(100 - near) <= 10 and n > 100):
        return True
    else:
        return False

if __name__ == '__main__':
    print(near_hundred(0))