def count_vowels(thing):
    """Count the number of vowels in the string passed in. If a list is passed in
    instead of a string, that's OK, we will count the vowels in each word in the 
    list and total them up."""
    type_sent_in = type(thing)
    if type_sent_in == str:
        # we expect a string...
        count = 0
        for char in thing.lower(): # we know we can do this, because it's str
            if char in 'aeiou':
                count += 1
    elif type_sent_in == list:
        count = 0
        for word in thing: # for each word in the list
            count += count_vowels(str(word)) # count vowels in that word, str-ify if necessary
    else:
        raise TypeError('Expected string argument, got ' + str(type_sent_in)) 
        
    return count