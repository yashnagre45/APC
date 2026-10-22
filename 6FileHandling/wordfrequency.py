file = open("student.txt", "r")

data = file.read().lower()
words = data.split()

frequency = {}

for word in words:
    word = word.strip(".,!?;:")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("Word Frequencies:")

for word, count in frequency.items():
    print(word, ":", count)

file.close()