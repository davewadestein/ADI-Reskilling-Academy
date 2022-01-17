import random

chutes_and_ladders = { 
      1:  38,  4: 14,  9: 31, 16:  6, 21: 42, 28: 84, 36: 44, 
     47:  26, 49: 11, 51: 67, 56: 53, 62: 19, 64: 60, 71: 91,
     80: 100, 87: 24, 93: 73, 95: 75, 98: 78
}

def move(position, roll, pronoun):
    # if the roll would make our position > 100, we need to adjust
    if position + roll > 100:
        position = 101 - roll # Sourabh's rules
        print('Current position + roll exceeds 100, so you backtrack')
    else: # we need to move our piece to the new position
        position += roll
          
    # is the place we moved to a chute or a ladder?
    if position in chutes_and_ladders:
        # we either hit a chute or a ladder
        new_position = chutes_and_ladders[position]
        if new_position > position:
            print('LADDER UP TO', new_position)
        else:
            print('CHUTE DOWN TO', new_position)
        position = new_position
    
    if position == 100:
        print(pronoun, 'won!')
    else:
        print('Current position is', position)
    return position

def roll(pronoun):
    roll = (random.randint(1, 6))
    print(pronoun, 'rolled a', roll)
    return roll

player_position, computer_position = 0, 0

while True:
    player_roll = input('Hit return to roll, or enter a specific roll: ')
    if not player_roll:
        player_roll = roll('You')
    else:
        player_roll = int(player_roll)
        
    player_position = move(player_position, player_roll, 'You')
    if player_position == 100:
        break
    computer_roll = roll('I')
    computer_position = move(computer_position, computer_roll, 'I')
    if computer_position == 100:
        break
