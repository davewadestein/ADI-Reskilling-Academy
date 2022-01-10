import random

# open up wordlist.txt and read all of the words in
wordfile = open('wordlist.txt')
word_list = wordfile.read().split()
# choose a word from the list at random and make it upper case
word = random.choice(word_list).upper()
letter_list = list(word)
random.shuffle(letter_list)
shuffled_word = ''.join(letter_list)
hint_letter = 0
guess = ''

while guess != word:
    guess = input(shuffled_word + '? ').upper()
    if guess == 'HINT':
        #print("Letter %d is %s"' % (hint_letter + 1, word[hint_letter]))
        print('Letter', hint_letter + 1, 'is', word[hint_letter])
        hint_letter += 1
    elif guess == 'QUIT':
        print('Word was', word)
        break
    elif guess == 'SHUFFLE':
        random.shuffle(letter_list)
        shuffled_word = ''.join(letter_list)
else:
    print('You got it!')

