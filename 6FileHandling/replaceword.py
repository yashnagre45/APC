file = open("student.txt", "r")
data = file.read()
file.close()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

data = data.replace(old_word, new_word)

file = open("modified.txt", "w")
file.write(data)
file.close()

print("Modified text saved in modified.txt")