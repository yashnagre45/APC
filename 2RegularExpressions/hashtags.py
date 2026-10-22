import re

text = input("Enter text: ")

hashtags = re.findall(r'#[A-Za-z0-9_]+', text)

print("Hashtags:", hashtags)