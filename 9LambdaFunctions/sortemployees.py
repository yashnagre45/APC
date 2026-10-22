employees = [
    ("Amit", 30000),
    ("Yash", 50000),
    ("Rahul", 40000),
    ("Priya", 60000)
]

employees.sort(key=lambda employee: employee[1])

print("Employees sorted by salary:")

for employee in employees:
    print(employee)