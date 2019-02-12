# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    first3 = str[0:3]
    if first3 != 'not':
        return 'not '+str
    else:
        return str

if __name__ == '__main__':
    print(not_string('not negative')) # -> prints itself
    print(not_string('positive')) # -> prints 'not positive'