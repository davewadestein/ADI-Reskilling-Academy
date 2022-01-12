import random

list_of_words = 'banana zipper solitude coconut journal quarantine dolphin intensity radiation'.split() # Pythonic way to make a list
word = random.choice(list_of_words)
letter_list = list(word.upper()) # list-ift the word into constituent letters
random.shuffle(letter_list)
num_hints = 0
num_reshuffles = 0

while True:
    print('-' * len(word)) # print a line before
    print(''.join(letter_list)) # print the word by smashing together the letters
    print('-' * len(word)) # print a line after
    # prompt user
    response = input("Enter your guess or 'h' for hint/'q' to quit/'s' to reshuffle: ")
    if response == 'q': # quit
        break
    # ask for a hint
    elif response == 'h': 
        # print the n'th letter of the word as a hint (recall: index starts at 0)
        print(f'Letter number {num_hints + 1} is "{word[num_hints].upper()}"')
        num_hints += 1
        if num_hints == len(word): # they got all the hints, and still didn't guess the word
            print('Sorry, the word was', word.upper())
            break
        continue
    # ask for a shuffle
    elif response == 's': 
        random.shuffle(letter_list) # re-shuffles the letters
        num_reshuffles += 1 # we might want to say something below about how many shuffles
        continue
    # they got it right, so congratulate them
    if response.lower() == word.lower():
        hint_string = 'no' # default case, they asked for no hints
        plural = 's'
        if num_hints > 0: # they asked for 1+ hints
            if num_hints == 1:
                plural = ''
            hint_string = f'only {num_hints}'
        print(f'You got it right, with {hint_string} hint{plural}!')
        break
    print("Good guess, but that is not the word. Remember you can type 'h' to ask for a hint.")
    
print('PROGRAM TERMINATED (ode to Grace Hopper).')
