file = open("student.txt", "r")
data = file.read()
file.close()

file = open("uppercase.txt", "w")
file.write(data.upper())
file.close()

print("Uppercase file created successfully")