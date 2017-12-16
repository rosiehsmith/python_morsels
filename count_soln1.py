from collections import Counter
import re

def count_words(sentence):
    # return Counter(re.findall(r"[\w'-]+", sentence.lower()))
    words = []
    for word in sentence.lower().split():
        words.append(word.strip('?!,.()'))
    return Counter(words)
