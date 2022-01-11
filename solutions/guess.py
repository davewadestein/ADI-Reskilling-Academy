import random # make use of the built-in random module

# Step 1: generate a random number for the user to guess
number = random.randint(1, 100)

# This will hold the user's guess. "Prime the pump" by
# setting it to 0...
guess = 0

# Step 2: keep asking the user for a guess until they get it right
while guess != number: # "while the user's guess is not equal to the number we picked"
    # Step 3: get the guess and convert to int
    guess = int(input('Enter your guess 1-100 (or 0 to quit): '))
    # Step 3a: check to see if user gave up
    if guess == 0:
        print("Sorry you're giving up, I was enjoying this game!")
        break
    # Step 4: give feedback
    if guess > number:
        print('Too high!')
    if guess < number:
        print('Too low!')    
# did user guess it right (i.e., loop terminated normally)
else:
    print('Congratulations! You guessed the number!')  
