file = open("input.txt", "r")
text = file.read()
file.close()

target = input("Enter the word to replace: ")
replacement = input("Enter the replacement word:")

text = text.replace(target, replacement)

file = open("output.txt", "w")
file.write(text)
file.close()

print("Replacement completed successfully.")
print("Modified text saved in output.txt")
