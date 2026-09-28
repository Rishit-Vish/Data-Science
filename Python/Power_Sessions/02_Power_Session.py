"""
File Name: 02_Python_Assignment_Tracing_And_Niven_Numbers.py
"""


# ==========================================================
# Question 1
# Trace the values of two variables
# after each iteration of the loop.
# ==========================================================

a, b = 2, 5

for i in range(3):
    a, b = b, a + b
    print("After step", i + 1, ":", a, b)


# ==========================================================
# Question 2
# Trace the values of two variables
# after each iteration of the loop.
# ==========================================================

a, b = 3, 7

for i in range(4):
    a, b = b, a + b
    print(a, b)


# ==========================================================
# Question 3
# Print the sequence generated
# by repeated variable swapping
# and addition.
# ==========================================================

a, b = 1, 2

for i in range(6):
    print(a)
    a, b = b, a + b


# ==========================================================
# Question 4
# Trace the values of two variables
# after each iteration of the loop.
# ==========================================================

a, b = 2, 4

for i in range(5):
    a, b = a + 2, b + a
    print(a, b)


# ==========================================================
# Question 5
# Trace the values of two variables
# after each iteration of the loop.
# ==========================================================

a, b = 5, 8

for i in range(4):
    b, a = a, b - a
    print(a, b)


# ==========================================================
# Question 6
# Check whether a number
# is a Harshad (Niven) Number.
#
# A Harshad (Niven) Number is a number
# that is divisible by the sum
# of its digits.
#
# Example:
# 18 → 1 + 8 = 9
# 18 ÷ 9 = 2
# Therefore, 18 is a Harshad Number.
# ==========================================================

n = 18

copy = n
sum = 0

while n > 0:

    digit = n % 10
    sum += digit

    n //= 10

if copy % sum == 0:
    print("Harshad (Niven) Number")

else:
    print("Not a Harshad (Niven) Number")


# ==========================================================
# Question 7
# Print all Harshad (Niven) Numbers
# in the range 1 to 100.
# ==========================================================

for i in range(1, 101):

    copy = i
    sum = 0

    while i > 0:

        digit = i % 10
        sum += digit

        i //= 10

    if copy % sum == 0:
        print(copy)
