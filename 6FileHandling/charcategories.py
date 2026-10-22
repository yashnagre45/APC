file = open("student.txt", "r")

data = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for char in data:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    elif char != "\n":
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

file.close()