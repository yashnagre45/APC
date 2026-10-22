try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Error: Enter a valid integer.")