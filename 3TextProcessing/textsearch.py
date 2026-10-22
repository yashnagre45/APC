file = open("sample.txt", "r")

text = file.read()
word = input("Enter word to search: ")

if word.lower() in text.lower().split():
    print("Word found in file")
else:
    print("Word not found in file")

file.close()