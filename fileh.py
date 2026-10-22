import string

file = open("input.txt", "r")
text = file.read()
file.close()

text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))

words = text.split()

print("Total number of words:", len(words))

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")

for word in frequency:
    print(word, ":", frequency[word])

print("\nTop 10 most frequent words:")

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words[:10]:
    print(word, ":", count)