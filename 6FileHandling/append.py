file = open("student.txt", "a")

name = input("Enter additional student name: ")
roll = input("Enter roll number: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")

file.close()

print("Data appended successfully")