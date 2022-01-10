import string

wordcount = {}
for line in open('hamlet.txt'):
    charlist = list(line.lower()) # with punctuation
    
    # re-form the line w/o punctuation
    # iterate thru every character, and drop the ones that
    # are punctuation
    charlist_minus_punct = []
    for char in charlist:
        if char not in string.punctuation:
            charlist_minus_punct.append(char)
    
    for word in ''.join(charlist_minus_punct).split():
        if word in wordcount:
            wordcount[word] = wordcount[word] + 1
        else:
            wordcount[word] = 1
            
for word in sorted(wordcount, key=wordcount.get, reverse=True)[:10]:
    print(word, wordcount[word])
