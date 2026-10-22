import numpy as np

marks = np.array([
    45, 60, 75, 80, 90,
    55, 65, 70, 85, 95,
    50, 68, 78, 88, 92,
    40, 58, 72, 82, 98
])

average = np.mean(marks)

above_average = marks[marks > average]

print("Student Marks:", marks)
print("Average Marks:", average)
print("Marks Above Average:", above_average)
print("Number of Students:", len(above_average))