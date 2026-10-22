import re

text = input("Enter text: ")

text = text.lower()
text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\s+', ' ', text)

print("Normalized text:", text.strip())