string = input("Enter a string: ")
old_char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")
result = ""
for char in string:
    if char == old_char:
        result += new_char
    else:
        result += char
print("Result:", result)