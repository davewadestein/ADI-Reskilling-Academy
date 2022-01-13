import random

list_of_words = 'banana zipper solitude coconut journal quarantine dolphin intensity radiation'.split() # Pythonic way to make a list
word = random.choice(list_of_words)
letter_list = list(word.upper()) # list-ift the word into constituent letters
random.shuffle(letter_list)
num_hints = 0
num_reshuffles = 0

while True:
    print('-' * len(word))
    print(''.join(letter_list))
    print('-' * len(word))
    # prompt user
    response = input("Enter your guess or 'h' for hint/'q' to quit/'s' to reshuffle: ")
    if response == 'q': # quit
        break
    # ask for a hint
    elif response == 'h': 
        print(f'Letter number {num_hints + 1} is "{word[num_hints].upper()}"')
        num_hints += 1
        if num_hints == len(word): # they got all the hints 
            print('Sorry, the word was', word.upper())
            break
        continue
    # ask for a shuffle
    elif response == 's': 
        random.shuffle(letter_list) # shuffles the letters
        num_reshuffles += 1
        continue
    # they got it right, so congratulate them
    if response.lower() == word.lower():
        if num_hints == 0:
            print('You got it right, with no hints!')
        else:
            print('You got it right, with', num_hints, 'hint(s)!')
        break
        
    print("Good guess, but that is not the word. Remember you can type 'h' to ask for a hint.")
    
print('PROGRAM TERMINATED.')
