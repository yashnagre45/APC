import number_utils

n = int(input("Enter a number: "))

print("Prime:", number_utils.is_prime(n))
print("Palindrome:", number_utils.is_palindrome(n))
print("Armstrong:", number_utils.is_armstrong(n))
print("Perfect:", number_utils.is_perfect(n))