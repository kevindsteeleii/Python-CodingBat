# Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
    return n*str

if __name__ == '__main__':
    print(string_times('hello', 3))