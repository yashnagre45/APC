sentence = input("Enter a sentence: ")
words = sentence.split()
if len(words) > 0:
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    print("Shortest word:", shortest)
else:
    print("No words found")