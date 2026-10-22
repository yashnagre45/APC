employees = [
    ("Amit", 30000),
    ("Yash", 50000),
    ("Rahul", 40000)
]

updated = list(
    map(lambda e: (e[0], e[1] * 1.10), employees)
)

above_50000 = list(
    filter(lambda e: e[1] > 50000, updated)
)

above_50000.sort(key=lambda e: e[1])

print("Employees with updated salary above Rs. 50000:")

for employee in above_50000:
    print(employee)