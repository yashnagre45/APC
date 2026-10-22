import student

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

total = student.total_marks(marks)
percent = student.percentage(marks)
result = student.grade(percent)

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percent, "%")
print("Grade:", result)