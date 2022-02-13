import random

options = {
        'r': 'rock',
        's': 'scissors',
        'p': 'paper',
}

options_list = list(options)

"""There are 3 x 3 = 9 combinations and 3 of those occur when each player
picks the same result, so we can easily identify those cases. The dict below
maps the other 6 cases to a string indicating who won the round.
"""
result = {
        ('rock',     'scissors'): 'rock smashes scissors–you win!',
        ('scissors', 'rock'):     'rock smashes scissors–I win!',
        ('paper',    'rock'):     'paper covers rock–you win!',
        ('rock',     'paper'):    'paper covers rock–I win!',
        ('scissors', 'paper'):    'scissors cuts paper–you win!',
        ('paper',    'scissors'): 'scissors cuts paper–I win!',
}

# Use Python 3.10 walrus operator to make the looping easier...
while (your_choice := input('(r)ock, (s)cissors, (p)aper, or (q)uit? ')) != 'q':
    if your_choice not in options:
        print('Unknown choice:', your_choice)
        continue
    your_choice = options[your_choice] # convert 's' to 'scissors', etc.
    my_choice = options[random.choice(options_list)]
    print(f'You picked {your_choice}; I picked {my_choice}', end='...')
    if your_choice == my_choice:
        print('tie!')
    else:
        print(result[your_choice, my_choice])
