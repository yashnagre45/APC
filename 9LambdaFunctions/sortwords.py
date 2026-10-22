words = ["python", "cat", "computer", "book", "apple"]

words.sort(key=lambda word: len(word))

print("Words sorted by length:", words)