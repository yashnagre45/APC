file = open("student.txt", "r")

data = file.read().lower()

vowels = 0
consonants = 0

for char in data:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Total vowels:", vowels)
print("Total consonants:", consonants)

file.close()