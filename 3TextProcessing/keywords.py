text = input("Enter text: ")

stopwords = {"is", "the", "a", "an", "and", "in", "of", "to", "for"}

words = text.lower().split()
keywords = []

for word in words:
    word = word.strip(".,!?;:")
    if word and word not in stopwords:
        keywords.append(word)

print("Keywords:", keywords)