import random # make use of the built-in random module

# Step 1: generate a random number for the user to guess
number = random.randint(1, 100)

# Step 2: keep asking the user for a guess until they get it right
for guesses in range(10): # "do this 10 times" (for a maximum of 10 guesses)
    # Step 3: get the guess and convert to int
    guess = int(input('Enter your guess 1-100 (or 0 to quit): '))
    # Step 3a: check to see if user gave up
    if guess == 0:
        print("Sorry you're giving up, I was enjoying this game!")
        break
    # Step 4: give feedback
    if guess > number:
        print('Too high!')
    elif guess < number:
        print('Too low!')
    else: # guess == number
        print('Congratulations! You guessed the number!')
        break
else: # only if we did not break...i.e., they used all of their guesses
    print('Sorry, all your guesses r belong to us!')
