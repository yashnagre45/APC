numbers = [10, 25, 55, 70, 40, 90, 15]

result = list(filter(lambda n: n > 50, numbers))

print("Original list:", numbers)
print("Numbers greater than 50:", result)