from student import marks, grade, attendance

name = input("Enter student name: ")

m = []
for i in range(5):
    mark = int(input("Enter marks: "))
    m.append(mark)

total = marks.total_marks(m)
per = marks.percentage(m)
g = grade.calculate_grade(per)

present = int(input("Enter lectures attended: "))
total_lectures = int(input("Enter total lectures: "))

att = attendance.attendance_percentage(
    present, total_lectures
)

print("\nStudent Report")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", per)
print("Grade:", g)
print("Attendance:", round(att, 2), "%")