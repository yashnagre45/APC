text = input("Enter the text: ")

search = input("Enter the word to search: ")

count = text.lower().count(search.lower())

highlighted = text.replace(
    search,
    "**" + search + "**"
)

print("Number of occurences:", count)

print("Highlighted text:")
print(highlighted)