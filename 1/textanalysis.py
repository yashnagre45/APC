text = "Python is easy and Python is powerful"

words = text.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Text:", text)
print("Total words:", len(words))
print("Word frequency:", frequency)

top_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

print("Top 3 frequent words:")
for word, count in top_words[:3]:
    print(word, ":", count)

vowels = 0

for char in text.lower():
    if char in "aeiou":
        vowels += 1

print("Total vowels:", vowels)