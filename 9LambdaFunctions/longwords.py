words = ["apple", "banana", "python", "cat", "computer", "book"]

result = list(filter(lambda word: len(word) > 5, words))

print("Original words:", words)
print("Long words:", result)