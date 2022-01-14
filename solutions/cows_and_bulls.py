import string

def generate_code():
    import random

    digits = list('0123456789')
    random.shuffle(digits)
    
    return ''.join(digits[:4])
 

    # validate their guess?
    # - if any letter is not 0-9, complain
    # - if response was not exactly 4 characters
    # - if any digits are repeated
    # let's put this in a function
    def is_valid_guess(guess):
        # returns True if string is 
        # 1. length 4
        # 2. only digits
        # 3. no repeated digits
        def no_repeated_letters(): # Function to check if any repeated characters
            newlist = []
            for digit in guess:
                if digit not in newlist:
                    newlist.append(digit)
            if len(newlist) == 4:
                return True
            else:
                return False

    # step 1
    if len(guess) != 4:
        print('Your guess does not have the correct number of digits')
        return False
    
    # step 2
    if not guess.isdigit():
        print('Your guess contains a non-digit!')
        return False
    
    '''
    for character in guess:
        if character not in string.digits:
            print('bad character in your guess:', character)
            return False
    '''
              
    # step 3
    if not no_repeated_letters():
        print('You guess has repeated digits! Try again.')
        return False
              
    return True
  
  
 def compute_bulls(answer, guess):
    bulls = 0
    for index in range(4):
        if answer[index] == guess[index]: # does the i'th character in answer equal the i'th in guess
            bulls += 1
    
    return bulls
  
  
  def compute_cows(answer, guess):
    # count all matches, regardless of position
    # technically the cows number is inflated
    # by the number of bulls
    cows = 0
    
  
code = generate_code()
no_of_guesses = 0

while True:
    print('secret code is', code)
    guess = input('Enter your 4-digit guess: ')
    if not is_valid_guess(guess):
        continue # just ask them again...
    no_of_guesses += 1
    bulls = compute_bulls(code, guess)
    cows = compute_cows(code, guess) - bulls
    if bulls == 4:
        print('Congrats! You guessed the code!')
        break # we are done
    print(f'{cows} cows, {bulls} bulls')
    for answer_index in range(4):
        for guess_index in range(4):
            if answer[answer_index] == guess[guess_index]:
                print('match', answer_index, guess_index)
                cows += 1
                
    return cows
 
