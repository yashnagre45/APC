text = input("Enter a string: ")

text = text.lower().replace(" ", "")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")