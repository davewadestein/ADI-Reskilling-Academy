
import random
# wordlist can be downloaded from goo.gl/PTSR0T
# Grab a random word from wordlist.txt (which is
# in this folder)
wordlist = open("wordlist.txt").read().splitlines()
word = random.choice(wordlist).upper()

# Create a list of dashes, one per letter
dash_string = '-' * len(word)
letter_list = list(dash_string)
# letter_list = ['-'] * len(word)

# We keep going as long as the user has not made 7
# incorrect guesses. When the user guesses a letter
# correctly that does not count as an incorrect guess.

incorrect_guesses = 0
max_incorrect_guesses = 7
guesses_so_far = []

while incorrect_guesses < max_incorrect_guesses:
    print(max_incorrect_guesses - incorrect_guesses, 'guesses remaining')
    # Check to see if all letters have been guessed,
    # i.e., all dashes have been flipped to their letters
    if '-' not in letter_list:
        print('Congrats, you got all the letters! The word was', word)
        break
    print(' '.join(letter_list), end='\n')
    guess = input('Your guess? ').upper()
    # User could enter a single letter, e.g., 'A'
    # ...OR a whole word. 
    # First we will compare the user's guess against
    # the word. If it's equal, they won.
    if guess == word:
        print('Congrats, you guessed the word!')
        break
    # At this point, whatever they typed was NOT the
    # word. So it is either an incorrect word, or it
    # is a single letter. So we check the length, and
    # if it's a word (i.e., length > 1), it must be
    # wrong.
    elif len(guess) > 1:
        if guess not in guesses_so_far:
            print("That's not the right word.")
            incorrect_guesses += 1
            guesses_so_far.append(guess)
        else:
            print('You already guessed', guess)
        continue
    # What do we know about guess here?
    # It is a single letter.
    # If that letter is NOT IN the word, 
    # then it's a wrong guess and we try again.
    if guess not in word:
        if guess not in guesses_so_far:
            incorrect_guesses += 1
            guesses_so_far.append(guess)
        else:
            print('You already guessed "', guess, '"', sep="")
        continue
    # At this point, they have guessed a single letter
    # and it IS in the word...
    position = 0
    for letter in word:
        if guess == letter:
            letter_list[position] = letter
        position += 1
# At this point I either exited the loop via a break
# (which means the user got it right), or normally, 
# which means the user did not.
else:
    print('Sorry, the word was', word) 
