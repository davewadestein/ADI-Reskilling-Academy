import random

code = []
for times in range(4):
    while True:
        num = random.randint(0, 9)
        if str(num) not in code: # We've NOT already generated this number
            break
    code.append(str(num))

code = ''.join(code)
print('Secret code is', ''.join(code))
bulls = 0
num_guesses = 0

while bulls != 4:
    guess = input('Enter a 4-digit number (or "quit"): ')
    num_guesses += 1
    if guess == 'quit':
        break
    
    # .isdigit() checks if any character is not a digit
    if len(guess) != 4 or not guess.isdigit(): 
        print('I said 4 digits.')
        continue

    if len(set(guess)) != 4:
        print('Your 4 digits must not have duplicates')
        continue

    # find cows...
    cows = 0
    for index1 in range(4): 
        for index2 in range(4):
            if index1 != index2: # don't compare [0] with [0]
                if code[index1] == guess[index2]:
                    print(code[index1], 'is a cow')
                    cows += 1

    # find bulls...
    bulls = 0
    for index in range(4):
        if code[index] == guess[index]:
            print(code[index], 'is a bull')
            bulls += 1

    if bulls < 4:
        print(cows, 'cows,', bulls, 'bulls')
else:
    print('You got it in', num_guesses, 'guesses!')
