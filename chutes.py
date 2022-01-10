import random

# This dictionary maps the squares on the board to where they will send
# you if you land on them. The keys are squares you land on, and the values
# are where you go from that square. For example, if you land on square 1,
# you'll climb to 38, and if you land on 49, you'll slide down to 11, etc.

chutes_and_ladders = {  1:38,  4:14,  9:31,  16:6,  21:42, 28:84,
                       36:44, 47:26, 49:11,  51:67, 56:53, 62:19,
                       64:60, 71:91, 80:100, 87:24, 93:73, 95:75, 98:78}

player_position = 0

while player_position < 100:
    # The user can enter a roll if desired, which will help with
    # testing the program. Otherwise, the computer will pick a
    # random number between 1 and 6.
    roll = input('Hit return or a roll (or enter a roll): ')

    if roll == '': # user hit return
        roll = random.randint(1, 6)
    else:
        roll = int(roll) # user entered a roll for testing

    print('You rolled a', roll)

    if player_position + roll > 100:
        print('Your roll would put you past 100, try again.')
        continue

    player_position += roll
    print('You moved to position', player_position)

    # Check to see if the current square is in the dictionary. If so,
    # it means we need to move up or down, depending on the value that
    # the key is mapped to.

    if player_position in chutes_and_ladders:
        old_position = player_position
        player_position = chutes_and_ladders[player_position]
        if player_position > old_position:
            print('LADDER up to', player_position)
        else:
            print('CHUTE down to', player_position)

print('You won!')
