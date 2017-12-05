import string

def count_words(sentence):
    for char in string.punctuation:
        if char != '\'':
            sentence = sentence.replace(char, "")

    sentence = sentence.split(' ')

    counts = dict()
    for word in sentence:
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    return counts
