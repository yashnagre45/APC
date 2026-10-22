numbers = [10, 20, 30]

try:
    index = int(input("Enter index (0-2): "))
    print("Value:", numbers[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Enter a valid integer.")