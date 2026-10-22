numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda n: n % 2 == 0, numbers))

print("Original list:", numbers)
print("Even numbers:", even)