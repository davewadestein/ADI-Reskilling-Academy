import random

pronouns = {
    'player': 'You',
    'computer': 'I'
}

possessives = {
    'player': 'Your',
    'computer': 'My'
}

positions = {
    'player': 0,
    'computer': 0
}

chutes_and_ladders = { 
      1:  38,  4: 14,  9: 31, 16:  6, 21: 42, 28: 84, 36: 44, 
     47:  26, 49: 11, 51: 67, 56: 53, 62: 19, 64: 60, 71: 91,
     80: 100, 87: 24, 93: 73, 95: 75, 98: 78
}


def indent(player):
    if player == 'computer':
        print('\t\t\t\t', end='')

def take_a_turn(player): # either 'computer'
    # print('It is', possessives[player].lower(), 'turn...')
    roll = roll_the_die(player)
    positions[player] = move(positions[player], roll, player)
    return positions[player]
    

def roll_the_die(player):
    roll = (random.randint(1, 6))
    indent(player)
    print(pronouns[player], 'rolled a', roll)
    return roll


def move(position, roll, person):
    # if the roll would make our position > 100, we need to adjust
    if position + roll > 100:
        position = 200 - (position + roll) # Sourabh's rules
        indent(person)
        print('Current position + roll exceeds 100, so you backtrack')
    else: # we need to move our piece to the new position
        position += roll
          
    # is the place we moved to a chute or a ladder?
    if position in chutes_and_ladders:
        # we either hit a chute or a ladder
        new_position = chutes_and_ladders[position]
        indent(person)
        if new_position > position:
            print('LADDER UP TO', new_position)
        else:
            print('CHUTE DOWN TO', new_position)
        position = new_position
    
    if position == 100:
        indent(person)
        print(pronouns[person], 'won!')
    else:
        if person == 'computer':
            print('\t\t\t\t', end='')
        print(possessives[person], 'current position is', position)
    return position


while True:
    response = '' #input("Hit return to roll, 'q' to quit: ")
    if response == 'q':
        print('Thanks for playing!')
        break
    if take_a_turn('player') == 100:
        break
    if take_a_turn('computer') == 100:
        break
