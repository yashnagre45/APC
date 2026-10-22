file = open("student.txt", "r")

data = file.read()

print("File Contents:")
print(data)

file.close()