class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        print("Destructor called")


name = input("Enter student name: ")
age = int(input("Enter student age: "))

s = Student(name, age)

s.display()

del s