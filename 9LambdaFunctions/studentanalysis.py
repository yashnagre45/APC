students = [
    ("Amit", 70),
    ("Yash", 90),
    ("Rahul", 80),
    ("Priya", 95)
]

average = sum(map(lambda s: s[1], students)) / len(students)

above_average = list(
    filter(lambda s: s[1] > average, students)
)

above_average.sort(key=lambda s: s[1])

print("Average marks:", average)
print("Students above average:")

for student in above_average:
    print(student)