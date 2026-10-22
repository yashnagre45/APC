from array import array

numbers = array('i', [])

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

print("Array elements:")

for value in numbers:
    print(value)