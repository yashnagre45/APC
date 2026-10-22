def unique_elements(numbers):
    unique = []

    for n in numbers:
        if n not in unique:
            unique.append(n)

    return unique


numbers = [10, 20, 10, 30, 20, 40]

print("Original list:", numbers)
print("Unique elements:", unique_elements(numbers))