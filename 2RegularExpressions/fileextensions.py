import re

filename = input("Enter filename: ")

match = re.search(r'\.([A-Za-z0-9]+)$', filename)

if match:
    print("File extension:", match.group(1))
else:
    print("No file extension found")