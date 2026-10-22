class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nStudent Details:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


try:
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    s = Student(name, roll_no, marks)
    s.display()

except ValueError as e:
    print("Error:", e)