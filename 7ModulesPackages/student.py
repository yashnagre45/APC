def total_marks(marks):
    return sum(marks)


def percentage(marks):
    return sum(marks) / len(marks)


def grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"