"""
File Name: 03_Python_Pattern_Printing_And_Loop_Practice.py
"""


# ==========================================================
# Question 1
# Print a square pattern using stars.
#
# Example:
#
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# ==========================================================

rows = 5

for i in range(1, rows + 1):
    print("* " * rows)


# ==========================================================
# Question 2
# Print a right-angled triangle
# using stars.
#
# Example:
#
# *
# * *
# * * *
# * * * *
# * * * * *
# ==========================================================

rows = 5

for i in range(1, rows + 1):
    print("* " * i)


# ==========================================================
# Question 3
# Print a left-aligned triangle
# using stars.
#
# Example:
#
#     *
#    **
#   ***
#  ****
# *****
# ==========================================================

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)


# ==========================================================
# Question 4
# Print numbers in a triangle pattern.
#
# Example:
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ==========================================================

rows = 5

for i in range(1, rows + 1):

    for j in range(i):
        print(j + 1, end=" ")

    print()


# ==========================================================
# Question 5
# Print a right-angled triangle
# where every number represents
# the factorial value.
#
# Example:
#
# 1
# 1 2
# 1 2 6
# 1 2 6 24
# 1 2 6 24 120
# ==========================================================


# ==========================================================
# Question 6
# Print a right-angled triangle
# using numbers.
#
# Example:
#
# 1
# 12
# 123
# 1234
# 12345
# ==========================================================

rows = 5

for i in range(1, rows + 1):

    for j in range(1, i + 1):
        print(j, end="")

    print()


# ==========================================================
# Question 7
# Take a string input from the user
# and print it in a right triangle pattern.
#
# Example:
#
# Input:
# Python
#
# Output:
# P
# Py
# Pyt
# Pyth
# Pytho
# Python
# ==========================================================

a = input("Enter a string: ")

j = ""

for i in a:
    j += i
    print(j)


# ==========================================================
# Question 8
# Print alphabets in a right-angled
# triangle pattern.
#
# Example:
#
# A
# A B
# A B C
# A B C D
# ==========================================================

rows = 20

for i in range(1, rows + 1):

    for j in range(65, 65 + i):
        print(chr(j), end=" ")

    print()


# ==========================================================
# Notes
# ASCII Values
# ==========================================================

# chr() converts an ASCII value into a character.
#
# Example:
# chr(65) -> A
# chr(66) -> B
# chr(67) -> C


# ==========================================================
# Question 9
# Create a program that keeps asking
# the user for input until the user
# enters "exit".
# ==========================================================

while True:

    n = input("Enter value: ")

    if n == "exit" or n == "Exit":
        break

print(f"User entered {n}, Exiting Program")


# ==========================================================
# Question 10
# Create a program that keeps asking
# for input until the user enters
# "exit" (case-insensitive).
# ==========================================================

while True:

    n = input("Enter value: ")

    if n.lower() == "exit":
        break

print(f"User entered {n}, Exiting Program")
