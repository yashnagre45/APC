text = input("Enter a paragraph: ")

stopwords = ["is", "am", "are", "the", "a", "an", "and", "in", "on", "Of", "to"]

words = text.split()

result = []

for word in words:
    if word.lower() not in stopwords:
        result.append(word)

cleaned_text = " ".join(result)

print("Text after removing stopwords:")
print(cleaned_text)