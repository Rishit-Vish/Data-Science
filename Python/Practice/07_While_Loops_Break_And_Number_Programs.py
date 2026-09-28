# ==========================================================
# Question 1
# Print numbers from 1 to 20.
# Stop the loop when the number becomes 8.
#
# Output:
# 1 2 3 4 5 6 7
# ==========================================================

for i in range(1, 21):
    if i == 8:
        break
    print(i)


# ==========================================================
# Question 2
# Print numbers from 1 to 50.
# Stop the loop when the number is a multiple of 10.
#
# Output:
# 1 2 3 4 5 6 7 8 9
# ==========================================================

for i in range(1, 51):
    if i % 10 == 0:
        break
    print(i)


# ==========================================================
# Question 3
# Print numbers from 1 to 100.
# Stop the loop when the number becomes 25.
#
# Output:
# 1 2 3 ... 24
# ==========================================================

for i in range(1, 101):
    if i == 25:
        break
    print(i)


# ==========================================================
# Question 4
# Print numbers from 1 to 15.
# Stop the loop when the number becomes greater than 7.
#
# Output:
# 1 2 3 4 5 6 7
# ==========================================================

for i in range(1, 16):
    if i > 7:
        break
    print(i)


# ==========================================================
# Question 5
# Print numbers from a given number up to 10
# using a while loop.
# ==========================================================

n = int(input("Enter the starting number: "))

while n <= 10:
    print(n)
    n += 1


# ==========================================================
# Question 6
# Print numbers from 10 to 1
# using a while loop.
# ==========================================================

n = 10

while n >= 1:
    print(n)
    n -= 1


# ==========================================================
# Question 7
# Print all even numbers from 2 to 20
# using a while loop.
# ==========================================================

i = 1

while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# ==========================================================
# Question 8
# Print all odd numbers from 1 to 15
# using a while loop.
# ==========================================================

i = 1

while i <= 15:
    if i % 2 != 0:
        print(i)
    i += 1


# ==========================================================
# Question 9
# Print all odd numbers from 1 to 15
# using an increment of 2.
# ==========================================================

i = 1

while i <= 15:
    print(i)
    i += 2


# ==========================================================
# Question 10
# Print the multiplication table of 5
# using a while loop.
# ==========================================================

i = 1

while i <= 10:
    print(f"5 × {i} = {5 * i}")
    i += 1


# ==========================================================
# Question 11
# Print the sum of the first
# 10 natural numbers using a while loop.
# ==========================================================

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum:", total)


# ==========================================================
# Question 12
# Print the square of numbers
# from 1 to 5 using a while loop.
# ==========================================================

i = 1

while i <= 5:
    print(f"{i} → {i ** 2}")
    i += 1


# ==========================================================
# Question 13
# Print numbers from 10 to 1
# in reverse order using a while loop.
# ==========================================================

i = 10

while i >= 1:
    print(i)
    i -= 1


# ==========================================================
# Question 14
# Demonstrate the use of
# division, modulus, and floor division.
# ==========================================================

print(1234 / 10)    # Normal division
print(1234 % 10)    # Remainder
print(1234 // 10)   # Quotient


# ==========================================================
# Question 15
# Separate and print each digit of a number
# using a while loop.
# ==========================================================

number = 145

while number > 0:
    print(number % 10)
    number //= 10


# ==========================================================
# Question 16
# Take a year as input.
# Check whether it is a leap year.
# ==========================================================

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
elif year % 100 == 0 and year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# ==========================================================
# Question 17
# Take an integer as input.
# Check whether it is a prime number.
# ==========================================================

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

"""
Why do we use count += 1 instead of count += i?

A prime number has exactly two factors:
1 and the number itself.

We only need to count how many factors exist,
not add the values of those factors.

For example:
7 is divisible by 1 and 7.

Using:
count += 1

Factor count:
1 → count = 1
7 → count = 2

Since the count is exactly 2,
7 is a prime number.

If we used:
count += i

The result would be:
1 + 7 = 8

This no longer represents the number of factors,
so it cannot be used to determine whether a number
is prime.
"""

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")