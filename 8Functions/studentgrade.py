def calculate_percentage(marks):
    return sum(marks) / len(marks)


def calculate_grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    else:
        return "D"


marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

per = calculate_percentage(marks)

print("Total Marks:", sum(marks))
print("Percentage:", per)
print("Grade:", calculate_grade(per))