def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count


def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


def count_words(text):
    return len(text.split())


def remove_spaces(text):
    return text.replace(" ", "")