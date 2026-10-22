def second_largest(numbers):
    unique = []

    for n in numbers:
        if n not in unique:
            unique.append(n)

    unique.sort()

    return unique[-2]


numbers = [10, 40, 20, 50, 30]

print("List:", numbers)
print("Second largest:", second_largest(numbers))