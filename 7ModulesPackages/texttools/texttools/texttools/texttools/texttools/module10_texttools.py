from texttools import cleaning, tokenization, frequency

text = input("Enter a sentence: ")

cleaned_text = cleaning.clean_text(text)
words = tokenization.tokenize(cleaned_text)
word_count = frequency.word_frequency(words)

print("Cleaned Text:", cleaned_text)
print("Words:", words)
print("Word Frequency:")

for word, count in word_count.items():
    print(word, ":", count)