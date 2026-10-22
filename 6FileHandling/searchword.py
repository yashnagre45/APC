file = open("student.txt", "r")

search_word = input("Enter word to search: ").lower()
count = 0
line_numbers = []

for line_number, line in enumerate(file, start=1):
    words = line.lower().split()

    for word in words:
        word = word.strip(".,!?;:")
        if word == search_word:
            count += 1
            line_numbers.append(line_number)

file.close()

print("Total occurrences:", count)
print("Line numbers:", sorted(set(line_numbers)))

if count == 0:
    print("Word not found")