file = open("students.csv", "w")
file.write("RollNo,Name,Marks\n")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")
file.close()

file = open("students.csv", "r")
lines = file.readlines()
file.close()

students = []

for line in lines[1:]:
    roll, name, marks = line.strip().split(",")
    students.append((roll, name, int(marks)))

print("Student Records:")

for student in students:
    print(student)

highest = max(students, key=lambda s: s[2])
average = sum(s[2] for s in students) / len(students)

print("Highest Marks:", highest[1], highest[2])
print("Average Marks:", average)

print("Students scoring above 80:")

for student in students:
    if student[2] > 80:
        print(student[1], student[2])