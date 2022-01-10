def palin(string):
    '''Return True is the string is a palindrome.'''
    string = string.lower().replace(' ', '')

    return string == string[::-1]

