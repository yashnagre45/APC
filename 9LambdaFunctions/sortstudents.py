students = [
    ("Amit", 75),
    ("Yash", 90),
    ("Rahul", 82),
    ("Priya", 95)
]

students.sort(key=lambda student: student[1])

print("Students sorted by marks:")

for student in students:
    print(student)