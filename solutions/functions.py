def max3(num1, num2, num3):
    # find the maximum of 3 numbers, assuming the built-in max() only works for 2
    max1 = max(num1, num2) # step 1: find larger of first two
    return max(max1, num3) # step 2: find larger of the number above and the third number

print(max3(1, 2, 3))
print(max3(-4, 17, -8))
print(max3(13, 12, 11))

def sum_list(the_list):
    result = 0 # step 1: initialize result to 0 (we don't do this in our brains)
    # step 2: for each item in the list, add it to the result
    for item in the_list:
        result += item
    
    return result

sum_list([-4, 5, -5, 4, 13, -8, 8, 1, 2, -3])

def remove_dupes(the_list):
    new_list = [] # step 1: create a new empty list to hold the resulting list which has no dupes
    # step 2: for each item in the original list...
    for item in the_list:
        # step 2a: if the item is NOT in the new list, add it to the NEW list
        if item not in new_list: # if not item in new_list:
            new_list.append(item)
            
    return new_list

remove_dupes([3, 1, 2, 3, 1, 3, 3, 4, 1])

import string

def is_pangram(sentence):
    # step 1: create a dictionary to keep track of every letter we've seen
    # (we could use a list too, but then we'd have to keep track of duplicates)
    check_letters = {} 
    check_list = []
    # (or, we can use a list of all the letters, removing them as we see them...)
    letter_list = list(string.ascii_lowercase) # 'abcdef...xyz'
    # step 2: for each letter in the sentence (i.e., non-spaces), add it to the dict
    for letter in sentence.lower():
        if letter != ' ': # if the letter is not a space
            check_letters[letter] = 1 # value does not matter, as we will see
            if letter not in check_list:
                check_list.append(letter)
            if letter in letter_list: # 3rd solution
                letter_list.remove(letter)
    
    return (len(check_letters) == 26) and (len(check_list) == 26) and (len(letter_list) == 0)

print(is_pangram('The Wizard quickly jinxed the gnomes before they vaporized'))
print(is_pangram('this is not a pangram, the letter z is missing'))

def is_palindrome(string):
    # radar, noon, racecar ... 'a man a plan a canal panama'
    # if we are not worried about spaces and punctuation, we can check if...
    # the string is equal to the reverse of the string, i.e, 'root' != 'toor', but 'noon' == the reverse of 'noon'
    return string.lower() == string[::-1].lower()

print(is_palindrome('Racecar'))
print(is_palindrome('roof'))
print(is_palindrome('AmanaplanacanalPanama'))
