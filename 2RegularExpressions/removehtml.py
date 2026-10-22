import re

html = input("Enter HTML text: ")

text = re.sub(r'<[^>]*>', '', html)

print("Text without HTML tags:", text)