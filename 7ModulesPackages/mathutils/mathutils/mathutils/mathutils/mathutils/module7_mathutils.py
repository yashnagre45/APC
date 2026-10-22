from mathutils import basic, number, statistics

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", basic.add(a, b))
print("Subtraction:", basic.subtract(a, b))
print("Multiplication:", basic.multiply(a, b))
print("Division:", basic.divide(a, b))

print("Square of first number:", number.square(a))
print("Cube of first number:", number.cube(a))
print("Is first number even?", number.is_even(a))

numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)
print("Average:", statistics.average(numbers))
print("Maximum:", statistics.maximum(numbers))
print("Minimum:", statistics.minimum(numbers))