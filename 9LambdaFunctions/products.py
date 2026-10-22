products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 10),
    ("Keyboard", 1000, 5)
]

total_values = list(
    map(lambda p: (p[0], p[1] * p[2]), products)
)

total_values.sort(key=lambda p: p[1])

print("Product total values:")

for product in total_values:
    print(product)