class Student:
    def __init__(self, name, age, roll_no, course):
        self.__name = name
        self.__age = age
        self.__roll_no = roll_no
        self.__course = course

    def __display_personal_details(self):
        print("Name:", self.__name)
        print("Age:", self.__age)

    def __display_academic_details(self):
        print("Roll No:", self.__roll_no)
        print("Course:", self.__course)

    def show_details(self):
        self.__display_personal_details()
        self.__display_academic_details()


name = input("Enter student name: ")
age = int(input("Enter age: "))
roll_no = input("Enter roll number: ")
course = input("Enter course: ")

s = Student(name, age, roll_no, course)

print("\nStudent Details:")
s.show_details()