string = input("Enter a string: ")
character = input("Enter a character to find: ")
count = 0
for ch in string:
    if ch == character:
        count += 1
print("Frequency:", count)