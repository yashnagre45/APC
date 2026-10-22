file = open("source.py", "r")
lines = file.readlines()
file.close()

output = []

for line in lines:
    if not line.lstrip().startswith("#"):
        output.append(line)

file = open("without_comments.py", "w")
file.writelines(output)
file.close()

print("Comments removed successfully")