def pang(string):
    '''Returns True is string is a pangram.'''
    letter_set = set()
    for character in string.lower():
        if character.islower():
            letter_set.add(character)
    return len(letter_set) == 26

