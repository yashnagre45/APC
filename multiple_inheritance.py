class Father:
    def father_info(self):
        print("Father: Engineer")

class Mother:
    def mother_info(self):
        print("Mother: Teacher")

class Child(Father, Mother):
    def child_info(self):
        print("Child: Student")

c = Child()

c.father_info()
c.mother_info()
c.child_info()
