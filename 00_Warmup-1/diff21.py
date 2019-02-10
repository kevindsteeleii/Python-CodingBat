# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  absolute = abs(21 - n)
  if n > 21:
    return 2 * absolute
  else:
    return absolute

if __name__ == '__main__':
    print(diff21(25))
