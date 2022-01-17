players = []

while True:
    player = input('Enter the name of the next player (hit return to stop entering players): ')
    if player:
        players.append(player)
    else:
        if not players: #...empty list, i.e., no players
            print('What?')
            break
        if len(players) == 1:
            players.append('computer') # only 1 player, so must be playing against computer
        else:
            response = input('Do you want me to play as well? ')
            if response.startswith('y'):
                players.append('computer')
        break
