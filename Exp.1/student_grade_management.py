students = ["Amit", "Priya", "Rahul"]
grades = [85, 92, 78]


def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print("Student added successfully.")


def update_grade(name, grade):
    if name in students:
        index = students.index(name)
        grades[index] = grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")


def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully.")
    else:
        print("Student not found.")


def display_grades():
    if len(grades) == 0:
        print("No student records available.")
        return

    print("\nStudent Records:")
    for i in range(len(students)):
        print(students[i], ":", grades[i])

    average = sum(grades) / len(grades)
    print("Average Grade:", average)
    print("Highest Grade:", max(grades))
    print("Lowest Grade:", min(grades))


display_grades()

add_student("Sneha", 88)
update_grade("Rahul", 82)
remove_student("Amit")

display_grades()