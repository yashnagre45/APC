a = [10, 20, 30]
b = [1, 2, 3]

result = list(map(lambda x, y: x + y, a, b))

print("First list:", a)
print("Second list:", b)
print("Sum:", result)