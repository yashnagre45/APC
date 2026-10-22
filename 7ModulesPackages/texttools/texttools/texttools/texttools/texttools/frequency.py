def word_frequency(words):
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency