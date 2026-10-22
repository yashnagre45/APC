import re

text = input("Enter a paragraph: ")

sentences = re.split(r'[.!?]+', text)

for sentence in sentences:
    sentence = sentence.strip()
    if sentence:
        print("Summary:", sentence)
        break