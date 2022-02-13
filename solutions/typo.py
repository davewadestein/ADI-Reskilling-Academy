import random

# Python 3.10 walrus operator
# "while line of input is not empty
while (line := input()):
    for word in line.split(): # split into words
        if len(word) < 4:
            print(word, end=' ')
        else:
            # "shuffle" the middle of the word (all but first and last chars)
            shuffled_middle = list(word[1:-1])
            random.shuffle(shuffled_middle)
            print(word[0] + ''.join(shuffled_middle) + word[-1], end=' ')
    print()
