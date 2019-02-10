# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    string = ''
    for i in range(len(str)):
        string += str[:i]
    return string+str

if __name__ == '__main__':
    print(string_splosion('Code'))