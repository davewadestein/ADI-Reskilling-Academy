wordcount = {} # empty dict
# 0. ask user for filename (hamlet.txt or poem.txt or...)
filename = input('Enter filename to count words in: ')
# 0a. open file
file = open(filename) # assume 'r for reading, also assume it exists (error checking comes later)

# 1. for each line in file
for line in file:
    # 1a. split the lower case line into words
    words = line.lower().split()
    # 2c. for each word in the splitted list
    for word in words:
    # 2d. if it's in the dict, increment count
        if word in wordcount: # word is IN the dict, so we've seen it before
            wordcount[word] += 1 # ...so increment its count
        # else put it in the dict with count of 1
        else:
            wordcount[word] = 1 # set it to 1, i.e., first time we have seen the word
            
# 3. print out words and counts
for word in wordcount:
    print(word, wordcount[word])
    
# because of some things we don't yet know, we're going to get A LOT of output for hamlet.txt
# what we do know how to do is to limit output to words which have been seen a minimum of x times

minimum = 100 # for hamlet, perhaps
for word in wordcount:
    if wordcount[word] >= minimum:
        print(word, wordcount[word])
