string = input("Enter a string: ")
result = ""
for char in string:
    if char != " ":
        result += char
print("String without spaces:", result)