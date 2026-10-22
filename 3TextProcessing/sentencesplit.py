import re

text = input("Enter a paragraph: ")

sentences = re.split(r'[.!?]+', text)

print("Sentences:")

for sentence in sentences:
    sentence = sentence.strip()
    if sentence:
        print(sentence)