def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_armstrong(n):
    digits = str(n)
    total = sum(int(digit) ** len(digits) for digit in digits)
    return total == n


def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n