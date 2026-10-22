words = ["apple", "banana", "cat", "computer", "book", "python"]

lengths = list(map(lambda word: (word, len(word)), words))

filtered = list(filter(lambda item: item[1] > 4, lengths))

filtered.sort(key=lambda item: item[1])

print("Words with length greater than 4:")

for item in filtered:
    print(item)