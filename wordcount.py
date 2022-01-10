wordcount = {}

# read each line of hamlet
for line in open('hamlet.txt'):
    wordlist = line.lower().split()
    for word in wordlist:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
            
# an idiom for sorting a dictionary by VALUE rather than key
for word in sorted(wordcount, key=wordcount.get, reverse=True)[:10]:
    print(word, wordcount[word])
