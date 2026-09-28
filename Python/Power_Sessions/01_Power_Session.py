"""
File Name: 01_Python_Notes_Fibonacci_And_Armstrong_Numbers.py
"""


# ==========================================================
# Question 1
# Print "Hello World" n times
# without using a for loop.
# ==========================================================

num = int(input("Enter a number: "))

print("Hello World\n" * num)


# ==========================================================
# Question 2
# Print "Hello World" n times
# using a for loop.
# ==========================================================

num = int(input("Enter a number: "))

for _ in range(num):
    print("Hello World")


# ==========================================================
# Notes
# Empty Loop Variable
# ==========================================================

# The underscore (_) is used when the loop variable
# is not needed inside the loop body.
# It improves code readability and indicates that
# the loop variable is intentionally ignored.


# ==========================================================
# Notes
# Assignment Evaluation Order
# ==========================================================

# In Python, the entire right-hand side (RHS)
# is evaluated before assignment is made
# to the left-hand side (LHS).

# Example:

a = 0

a, a = 1, 2

print(a)      # Output: 2


# ==========================================================
# Notes
# Swapping Variables
# ==========================================================

# During swapping, Python first evaluates
# the complete RHS, stores the values temporarily,
# and then assigns them to the variables
# on the LHS.

# Example:

# a, b = b, a


# ==========================================================
# Notes
# Fibonacci Series
# ==========================================================

# The Fibonacci series starts with 0 and 1.
# Every next number is the sum
# of the previous two numbers.

# Example:
# 0, 1, 1, 2, 3, 5, 8, ...


# ==========================================================
# Question 3
# Print all factors of a number
# except the number itself.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(1, n // 2 + 1):
    print(i if n % i == 0 else "")


# ==========================================================
# Question 4
# Print the first 10
# Fibonacci numbers.
# ==========================================================

n = 10

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


# ==========================================================
# Notes
# Armstrong Number
# ==========================================================

# An Armstrong number is a number
# whose value is equal to the sum of
# each of its digits raised to the power
# of the total number of digits.
#
# Example:
# 153
#
# Number of digits = 3
#
# 1³ + 5³ + 3³ = 153


# ==========================================================
# Question 5
# Check whether a number
# is an Armstrong number.
# ==========================================================

n = 153

copy = n
m = len(str(n))
sum = 0

while n > 0:

    z = n % 10
    multi = z ** m

    sum += multi

    n //= 10

if sum == copy:
    print("Yes")

else:
    print("Not")


# ==========================================================
# Question 6
# Print all Armstrong numbers
# in the range 1 to 999.
# ==========================================================

for i in range(1, 1000):

    sum = 0
    copy = i
    l = len(str(i))

    while i > 0:

        z = i % 10
        an = z ** l

        sum += an

        i //= 10

    if copy == sum:
        print(sum)
