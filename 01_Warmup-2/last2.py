# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    count = 0
    last2 = str[len(str) - 2:]
    print(last2)
    for i in range(len(str)-2):
        if last2 == str[i:i+2]:
            count += 1
    return count

if __name__ == '__main__':
    print(last2('rdword'))