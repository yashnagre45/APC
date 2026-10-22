text = input("Enter a sentence: ")

stopwords = {"is", "the", "a", "an", "and", "in", "of", "to"}

words = text.lower().split()
result = []

for word in words:
    if word not in stopwords:
        result.append(word)

print("Text after removing stopwords:", " ".join(result))