import numpy as np

marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 82])

print("Student Marks:", marks)

print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Standard Deviation:", round(np.std(marks), 2))