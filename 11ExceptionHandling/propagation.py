def divide():
    a = 10
    b = 0
    return a / b

try:
    divide()

except ZeroDivisionError:
    print("Exception handled in main program.")