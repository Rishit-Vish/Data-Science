# ==========================================================
# Question 1
# Take the string "Developer".
# If the string is not empty, print its first
# four characters in uppercase.
# Otherwise, print "Empty Word".
# ==========================================================

word = "Developer"

if word:
    word = word[:4]
    word = word.upper()
    print(word)
else:
    print("Empty Word")


# ==========================================================
# Question 2
# Given the string "python is fun":
# 1. Capitalize only the first word using slicing.
# 2. Print the total number of characters,
#    excluding spaces.
# ==========================================================

msg = "python is fun"

first_word = msg[:6].capitalize()
print(first_word)

total_characters = len(msg.replace(" ", ""))
print(total_characters)


# ==========================================================
# Question 3
# Take an integer as input.
# If the number is even, divide it by 2 using
# floor division (//).
# If the number is odd, multiply it by 3
# and add 1.
# ==========================================================

num = int(input("Enter a number: "))

if num % 2 == 0:
    num = num // 2
    print(num)
else:
    print(num * 3 + 1)


# ==========================================================
# Question 4
# Take an integer as input.
# Check whether the number is positive,
# negative, or zero.
# ==========================================================

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


# ==========================================================
# Question 5
# Given:
# x = 15
# y = 15
# Check whether:
# 1. x >= y
# 2. x <= y
# Print the result of both comparisons.
# ==========================================================

x = 15
y = 15

print(x >= y)
print(x <= y)


# ==========================================================
# Question 6
# Take three numbers as input.
# Print the largest number.
# ==========================================================

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    print("A is the largest")
elif b >= a and b >= c:
    print("B is the largest")
else:
    print("C is the largest")


# ==========================================================
# Question 7
# Take a string as input.
# If its length is greater than 5,
# print "Long String".
# Otherwise, print "Short String".
# ==========================================================

name = input("Enter a string: ")

if len(name) > 5:
    print("Long String")
else:
    print("Short String")


# ==========================================================
# Question 8
# Take two numbers as input.
# Print:
# - "Equal" if both numbers are equal.
# - "First is greater" if the first number is greater.
# - "Second is greater" otherwise.
# ==========================================================

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == num2:
    print("Equal")
elif num1 > num2:
    print("First is greater")
else:
    print("Second is greater")


# ==========================================================
# Question 9
# Take two numbers as input.
# Check whether the first number is divisible
# by the second number.
# Print "Divisible" or "Not Divisible".
# ==========================================================

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a % b == 0:
    print("Divisible")
else:
    print("Not Divisible")


# ==========================================================
# Question 10
# Take three numbers as input.
# Find the largest number using a variable.
# ==========================================================

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest number is:", largest)


# ==========================================================
# Question 11
# Take two numbers as input.
# Print True if both numbers are positive.
# Otherwise, print False.
# ==========================================================

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > 0 and b > 0:
    print(True)
else:
    print(False)