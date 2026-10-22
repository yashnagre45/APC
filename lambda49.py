students = [
    ("Amit", 70),
    ("Priya", 85),
    ("Rahul", 92),
    ("Sneha", 68),
    ("Neha", 78)
]

def average_marks(students):
    total = 0

    for student in students:
        total = total + student[1]

    return total / len(students)


average = average_marks(students)

print("Average Marks:", average)

print("\nStudents scoring above 75:")

above_75 = list(filter(lambda x: x[1] > 75, students))

for student in above_75:
    print(student[0], student[1])

print("\nStudents sorted according to marks:")

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

for student in sorted_students:
    print(student[0], student[1])