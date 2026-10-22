student = {
    "name": "Yash",
    "marks": 85
}

try:
    key = input("Enter key (name/marks): ")
    print("Value:", student[key])

except KeyError:
    print("Error: Key not found.")