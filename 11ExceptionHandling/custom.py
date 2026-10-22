class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Eligible.")

except InvalidAgeError as e:
    print("Error:", e)

except ValueError:
    print("Error: Enter a valid integer.")