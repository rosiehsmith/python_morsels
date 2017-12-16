def with_previous(input):
    previous = None
    for word in input:
        yield word, previous
        previous = word
