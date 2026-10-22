text = input("Enter text: ")

dictionary = {
    "python", "is", "a", "popular", "programming",
    "language", "hello", "world", "learn", "easy"
}

words = text.lower().split()
misspelled = []

for word in words:
    word = word.strip(".,!?;:")
    if word and word not in dictionary:
        misspelled.append(word)

print("Misspelled words:", misspelled)