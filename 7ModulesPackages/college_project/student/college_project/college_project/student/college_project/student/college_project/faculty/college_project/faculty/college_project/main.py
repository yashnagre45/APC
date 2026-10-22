from student import details, marks
from faculty import details as faculty_details

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")

student_marks = []

for i in range(3):
    mark = int(input("Enter subject marks: "))
    student_marks.append(mark)

print("\n--- Student Details ---")
details.student_details(name, roll, branch)

print("Total Marks:", marks.calculate_total(student_marks))
print("Percentage:", marks.calculate_percentage(student_marks))

print("\n--- Faculty Details ---")
faculty_name = input("Enter faculty name: ")
subject = input("Enter faculty subject: ")

faculty_details.faculty_details(faculty_name, subject)