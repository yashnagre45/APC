file = open("sample.txt", "r")

text = file.read()
words = text.split()

print("Total number of words:", len(words))

file.close()