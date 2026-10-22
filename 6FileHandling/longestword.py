file = open("student.txt", "r")

data = file.read()
words = data.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("File is empty")

file.close()