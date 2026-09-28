# ==========================================================
# Question 1
# Check whether a string is a palindrome.
#
# A palindrome is a string that remains the same
# when reversed.
#
# Example:
# madam → madam
# ==========================================================

text = "madaM"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# ==========================================================
# Question 2
# Check whether a number is a palindrome.
# ==========================================================

number = str(127)

if number == number[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# ==========================================================
# Question 3
# Check whether a string is palindrome
# without using slicing.
# ==========================================================

text = "madam"

reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse += text[i]

if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")


# ==========================================================
# Question 4
# Understand arithmetic operators:
#
# /   → Normal division
# //  → Floor division
# %   → Remainder
#
# Example:
# 10 / 3  → 3.33
# 10 // 3 → 3
# 10 % 3  → 1
# ==========================================================

a = 10
b = 3

print(a / b)
print(a // b)
print(a % b)


# ==========================================================
# Question 5
# Take two numbers and print:
# - Sum
# - Difference
# - Product
# - Quotient
# ==========================================================

a = 10
b = 3

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)


# ==========================================================
# Question 6
# Given a string:
# "Python is fun!"
#
# Perform:
# - Find length
# - Print first character
# - Print last character
# - Slice "is fun!"
# - Check whether "Python" exists
# ==========================================================

text = "Python is fun!"

print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Substring:", text[7:])

print("Python" in text)


# ==========================================================
# Question 7
# Take first name and last name from the user.
# Print the complete name in one line.
# ==========================================================

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print(full_name)


# ==========================================================
# Question 8
# Take a number from the user.
# Print:
# - Positive if number > 0
# - Negative if number < 0
# - Zero if number == 0
# ==========================================================

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")

elif num < 0:
    print("Negative")

else:
    print("Zero")


# ==========================================================
# Question 9
# Take age as input.
#
# Conditions:
# Age >= 18  → Adult
# Age 13-17  → Teenager
# Otherwise  → Child
# ==========================================================

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")

elif age >= 13:
    print("You are a teenager.")

else:
    print("You are a child.")


# ==========================================================
# Question 10
# Use a for loop to print numbers from 1 to 10.
# ==========================================================

for i in range(1, 11):
    print(i)


# ==========================================================
# Question 11
# Iterate through a string and print
# each character on a new line.
# ==========================================================

text = "Hello"

for char in text:
    print(char)


# ==========================================================
# Question 12
# Use a while loop to print numbers
# from 1 to 5.
# ==========================================================

number = 0

while number < 5:
    number += 1
    print(number)


# ==========================================================
# Question 13
# Keep taking numbers as input.
# Stop the loop when the user enters 0.
# ==========================================================

while True:

    number = int(input("Enter a number: "))

    if number == 0:
        print("Loop stopped.")
        break

    print(number, "Try again")


"""
Concept:

while True:

- Creates an infinite loop.
- The loop continues until a break statement
  is executed.

Example:

while True:
    user_input = input()

    if condition:
        break

The break statement is responsible for stopping
the loop.

If we write:

while False:

Python will never enter the loop because the
condition is already false.
"""