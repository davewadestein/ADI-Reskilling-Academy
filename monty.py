import random

def func1():
    pass

## outline 1
num_doors = input('How many doors (3)? ')
num_doors = 3 if num_doors == '' else int(num_doors)

runs = input('How many runs (1000)? ')
runs = 1000 if runs == '' else int(runs)

wins = 0

for count in range(1, int(runs) + 1):
    prize = random.randint(1, num_doors) # prize door
    guess = random.randint(1, num_doors) # guess a door

    # Create a set of doors, then remove door which hides
    # the prize and also remove door that we guessed. That
    # way we have a set of all doors we flip over and show
    # the player.

    doors = set(range(1, num_doors + 1))

    # Now, doors will be a set like {1, 2, 3}. So now we
    # remove door which hides the prize. e.g., if prize is
    # behind door 1, we'll remove it, and the doors set will 
    # look like this–{2, 3}.

    doors.remove(prize)

    # If player guessed wrong, we remove the door that player 
    # chose (e.g., perhaps 2, in this example, leaving the
    # doors set to be {3}). Then host will show player what's 
    # behind door 3 and player will switch to the door which
    # hides the prize.

    if guess != prize:
        doors.remove(guess)
        switch = prize

    # The other case is that player guessed right, and will
    # switch to a non-prize door, which in this case will be
    # the last door from the set above, i.e., 3.

    else:
        switch = doors.pop()

    # If we have > 3 doors, the host will open up ALL the
    # doors except for the player's original choice and the
    # one hiding the prize. If there are more than 10 doors,
    # this leads to voluminous output, so we'll just write
    # 'all others'.

    if num_doors > 10:
            doors = '[all others]'

    print('\nRun', count)
    print('Prize is behind door', prize)
    print('...You picked', guess)
    print("...I showed what's behind door(s)", str(doors))
    print('...You switched to door', switch, end='...')

    if guess != prize:
        wins += 1
        print('WIN!')
    else:
        print('LOSE')

print(f'\nSwitching yielded {wins} wins / {count} attempts = {wins / count:.3f}')

