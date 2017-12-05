def count_words(sentence):
    sentence = sentence.split(' ')
    d = {}
    
    for word in sentence:
        word = word.lower()
        if word in d:
            d[word]+=1
        else:
            d[word] = 1
    return d

# count_words("oh what a day what a lovely day")

# COMMENTS:
# took about 30 min to solve
# had to find out dictionary syntax
# excited to start 