# putting it all together
# (...) is "optional"
# (allow more than one player against computer or w/o computer)
# 
# 1. player's position starts at 0
# computer's position starts at 0 (off the board)
# (figure out who goes first by each person rolling and highest roll goes first)
# 2. until no player on square 100 or no player quits, keep doing the following:
#.   2a. indicate which player's turn it is (we are keeping track of whose turn)
#.   2b. each player rolls or tells us what their roll is for testing
#.   2c. if die roll added to current position + die roll <= 100:
#.      check to see if new position in the dict and if so:
#.         grab the value and display it as new position
#          indicate whether player climbed a ladded or slide down a chute
#.   2d. if new position is 100:
#.      then player wins

import sys
    
# global var
# chute_ladders maps board positions to final board positions via chute/ladder
chute_ladders = {  1: 38,  4: 14,  9: 31,  16: 6,  21: 42, 28: 84, 36: 44,
                  47: 26, 49: 11,  51: 67, 56: 53, 62: 19, 64: 60, 71: 91,
                  80: 100, 87: 24, 93: 73, 95: 75, 98: 78
                }

# player_names/info is a dict where keys are player names and vals are player positions
player_info = {}
player_names = [] # just a list of the names (keys in player_info) to make things easier
current_player = 0 # indicates who the current player is

# until we've identified all of the players
# (while some people still want to play...)
    # get the name of a player
    # store it somewhere
# if there are 2+ players, ask if computer should join
# otherwise computer plays against the player
# return the players

def get_player_names():
    """Get the names of all players and enter them into the global dictionary. All positions start at 0."""
    global player_info, player_names
    
    while True:
        name = input('Enter name of next player (RETURN/ENTER when all players have been named): ')
        if not name: # name == ''
            break
        elif name == 'computer':
            print('"computer" is my name. Please choose a different name.')
        else:
            if name in player_info:
                print(name, 'is already a player!')
            else:
                player_info[name] = 0 # add name to dictionary, and set position to 0
            
    computer = 'y' # prepare to append 'computer' to the list, unless they entered 2+ names
    
    if not player_info: # they entered ZERO names
        player_info['Player One'] = 0
    elif len(player_info) >= 2: # if there are at least 2 players        
        while True:
            computer = input('Should I play too (y/n)? ')
            if computer == 'y' or computer == 'n':
                break
            #if computer in ('y', 'n'): # equivalent: if the string computer is in the tuple/list
                #break
        
    if computer == 'y':
        player_info['computer'] = 0
    
    player_names = list(player_info.keys()) # dict will not be changed after this, but underscores we just want a list...
    

def die_roll(player):
    """Roll the die or let player specify the roll for testing purposes."""
    # get input from user
    # if no input, generate a random number 1..6
    # otherwise, use their number
    # perhaps 0 means quit, and if so there is nothing do here
    from random import randint
    roll = ''
    
    if player == 'computer': # computer just gets a die roll and returns
        return randint(1, 6)
    
    roll = input('Enter your roll or "quit" to quit or hit ENTER to roll the die: ')
    
    if roll == 'quit': # remember this won't work in the notebook
        sys.exit(0) # sys.exit() is a function that quits a program immediately
        
    # what remains is either they entered a number or they ENTER (or any string)
    if roll == '': # not roll
        roll = randint(1, 6)
    else:
        # if we're here...they entered a string (which could be a number)
        try:
            roll = int(roll)
        except ValueError: # so they didn't a number
            print("I don't understand what you entered...will roll the die for you.")
            roll = randint(1, 6)

    return roll

  
def determine_position(current_pos, roll):
    """Determine new position from current position along with dice roll."""
    # this is a function that will take the current position and the current roll
    # and tell us the final position
    # 1. new position is current position plus die roll (2 + 1)
    # 1a. if new position > 100 just use current_position
    # else
    # 2. if new position puts us on a square that is a chute or a ladder
    #    3. indicate whether we go up or down
    #    4. new position will be the target of the chute or ladder
    # 5. return new position
    new_pos = current_pos + roll # step 1
    if new_pos > 100: # step 1a
        print('Your roll of', roll, 'would put you off the board.')
        return current_pos
    # step 2: check if new position is a chute or a ladder
    if new_pos in chute_ladders: # the current position is a chute or a ladder because it's IN the dict
        final_pos = chute_ladders[new_pos] # 11 
        if final_pos > new_pos: # step 3
            print('...LADDER UP TO', final_pos)
        else:
            print('...CHUTE DOWN TO', final_pos)
        new_pos = final_pos # step 4
        
    return new_pos # step 5


def print_positions():
    """Print out all player positions."""
    global player_names, player_info
    
    for player in player_names:
        print(player, 'is at position', player_info[player])
    

get_player_names() # sets up the global dict

while not 100 in player_info.values(): # step 2: while no player is on position 100
    print_positions() # for clarity, tell us where everybody on the board
    player = player_names[current_player] # get name of current player from list
    print(f"{player}'s turn...") # step 2a
    roll = die_roll(player)
    print(f'\t{player} rolled a', roll)
    
    player_info[player] = determine_position(player_info[player], roll)
    
    if player_info[player] == 100:
        print(player, 'won!')

    # increment to "point to" next player–if we hit the end start at beginning
    current_player += 1
    if current_player == len(player_names): # or use % len(player_names)
        current_player = 0
