# ==========================================================
# Question 1
# Take two numbers as input representing a range.
# Print all even numbers within the given range.
# ==========================================================

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)


# ==========================================================
# Question 2
# Take two numbers as input representing a range.
# Calculate and print the sum of all odd numbers
# within the given range.
# ==========================================================

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

odd_sum = 0

for i in range(start, end + 1):
    if i % 2 != 0:
        odd_sum += i

print(odd_sum)


# ==========================================================
# Question 3
# Check whether a number is a Strong Number.
#
# A Strong Number is a number where the sum of the
# factorials of its digits is equal to the original number.
#
# Example:
# 145 = 1! + 4! + 5!
#     = 1 + 24 + 120
#     = 145
# ==========================================================

num = int(input("Enter a number: "))

original = num
factorial_sum = 0

while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    factorial_sum += fact
    num //= 10

if factorial_sum == original:
    print("Strong Number")
else:
    print("Not a Strong Number")


# ==========================================================
# Question 4
# Check whether a number is a palindrome.
#
# A palindrome number remains the same when reversed.
#
# Example:
# 123443321 → 123443321
# ==========================================================

num = 123443321

reverse = 0
original = num

while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num //= 10

print(reverse)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# ==========================================================
# Question 5
# Check whether a number is prime using a loop.
#
# A prime number has exactly two factors:
# 1 and the number itself.
# ==========================================================

n = 34

for i in range(2, n):
    if n % i == 0:
        print("Composite Number")
        break
else:
    print("Prime Number")


# ==========================================================
# Question 6
# Check whether a number is prime by counting
# the total number of factors.
# ==========================================================

n = 13

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")


# ==========================================================
# Question 7
# Check whether a 3-digit number is an Armstrong Number.
#
# An Armstrong Number is a number where the sum of
# cubes of its digits equals the original number.
#
# Example:
# 153 = 1³ + 5³ + 3³
# ==========================================================

n = int(input("Enter a 3-digit number: "))

original = n
digit_sum = 0

while n > 0:
    digit = n % 10
    digit_sum += digit ** 3
    n //= 10

if digit_sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# ==========================================================
# Question 8
# Print characters of a string using indexing.
# ==========================================================

text = "NATURE"

for i in range(len(text)):
    print(text[i])


# ==========================================================
# Question 9
# Print a string in reverse order using indexing.
# ==========================================================

text = "NATURE"

for i in range(len(text) - 1, -1, -1):
    print(text[i])


# ==========================================================
# Question 10
# Given a string:
# - Print it in uppercase.
# - Print it in lowercase.
# - Copy it into another string.
# - Reverse the string.
# ==========================================================

text = "PythOn"

print(text.upper())
print(text.lower())

copy_text = text
print(copy_text)

print(text[::-1])


# ==========================================================
# Question 11
# Given a string, create two separate strings:
# 1. One containing uppercase letters.
# 2. One containing lowercase letters.
# ==========================================================

text = "PythoN"

uppercase = ""
lowercase = ""

for i in range(len(text)):
    if text[i].isupper():
        uppercase += text[i]
    else:
        lowercase += text[i]

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)


# ==========================================================
# Question 12
# Arrange string characters such that:
# - Lowercase letters are stored separately.
# - Uppercase letters are stored separately.
# ==========================================================

text = "HeLlo BroThEr"

uppercase = ""
lowercase = ""

for i in range(len(text)):
    if text[i].isupper():
        uppercase += text[i]
    else:
        lowercase += text[i]

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)