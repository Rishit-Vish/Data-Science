# ==========================================================
# Question 1
# Create a password checker.
# Keep asking the user for a password until the correct
# password is entered.
# ==========================================================

correct_password = "bro123"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break

    print("Wrong password, try again")


# ==========================================================
# Question 2
# Temperature Converter
#
# Take temperature in Celsius from the user.
# Convert it into Fahrenheit using:
#
# Fahrenheit = (Celsius × 9/5) + 32
#
# Print the result using an f-string.
# ==========================================================

celsius = int(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperature in Fahrenheit is {fahrenheit}")


# ==========================================================
# Question 3
# Palindrome Checker
#
# Take a word as input.
# Check whether it reads the same forward and backward.
# Use slicing and if/else.
# ==========================================================

word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# ==========================================================
# Question 4
# Vowel Counter
#
# Take a sentence as input.
# Count the total number of vowels.
# ==========================================================

sentence = input("Enter a sentence: ")

count = 0

for char in sentence:
    if char in "AEIOUaeiou":
        count += 1

print("Total vowels:", count)


# ==========================================================
# Question 5
# Factorial Calculator
#
# Take a non-negative number as input.
# Calculate its factorial.
#
# Example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# ==========================================================

number = int(input("Enter a non-negative number: "))

factorial = 1

if number == 0:
    print("Factorial is 1")

else:
    for i in range(1, number + 1):
        factorial *= i

    print("Factorial:", factorial)


# ==========================================================
# Question 6
# Strong Number Checker
#
# A Strong Number is a number where the sum of
# factorials of its digits is equal to the original number.
#
# Example:
# 145 = 1! + 4! + 5!
#     = 1 + 24 + 120
#     = 145
# ==========================================================

number = int(input("Enter a number: "))

original = number
factorial_sum = 0

while number > 0:

    digit = number % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial *= i

    factorial_sum += factorial

    number //= 10


if original == factorial_sum:
    print("Strong Number")
else:
    print("Not a Strong Number")


# ==========================================================
# Question 7
# Armstrong Number Explanation
#
# An Armstrong Number is a number where:
#
# Sum of (each digit raised to the power of total digits)
# is equal to the original number.
#
# Example:
#
# 153 has 3 digits:
#
# 1³ + 5³ + 3³ = 153
# ==========================================================


# ==========================================================
# Question 8
# Take a string as input and print its length.
# ==========================================================

text = input("Enter a string: ")

print("Length:", len(text))


# ==========================================================
# Question 9
# Take a string as input and print its
# first and last character.
# ==========================================================

text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])


# ==========================================================
# Question 10
# Convert a string into uppercase and lowercase.
# ==========================================================

text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


# ==========================================================
# Question 11
# Separate lowercase and uppercase characters
# from a string.
# ==========================================================

text = "HelLoBrooTheR"

lowercase = ""
uppercase = ""

for char in text:

    if char.islower():
        lowercase += char

    else:
        uppercase += char


print("Lowercase:", lowercase)
print("Uppercase:", uppercase)