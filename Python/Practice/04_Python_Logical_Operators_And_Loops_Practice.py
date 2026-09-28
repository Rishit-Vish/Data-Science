# ==========================================================
# Question 1
# Take an integer as input.
# Print "Yes" if the number is divisible by 2 or 3.
# Otherwise, print "No".
# ==========================================================

a = int(input("Enter a number: "))

if a % 2 == 0 or a % 3 == 0:
    print("Yes")
else:
    print("No")


# ==========================================================
# Question 2
# Take three numbers as input.
# Print "All numbers are positive" if all
# three numbers are greater than 0.
# Otherwise, print "Some numbers are non-positive".
# ==========================================================

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > 0 and b > 0 and c > 0:
    print("All numbers are positive")
else:
    print("Some numbers are non-positive")


# ==========================================================
# Question 3
# Take a character as input.
# Print "Vowel" if it is a vowel.
# Otherwise, print "Consonant".
# ==========================================================

ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


# ==========================================================
# Question 4
# Take age and marks as input.
# Print "Eligible" if age is greater than 18
# and marks are at least 40.
# Otherwise, print "Not Eligible".
# ==========================================================

age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

if age > 18 and marks >= 40:
    print("Eligible")
else:
    print("Not Eligible")


# ==========================================================
# Question 5
# Take a password as input.
# Print "Strong Password" if:
# - Its length is at least 8 characters, and
# - It contains either '@' or '#'.
# Otherwise, print "Weak Password".
# ==========================================================

password = input("Enter your password: ")

if len(password) >= 8 and ('@' in password or '#' in password):
    print("Strong Password")
else:
    print("Weak Password")

# Note:
# The 'in' operator checks whether a particular
# value exists inside a sequence such as a string,
# list, or tuple.


# ==========================================================
# Question 6
# Take three numbers as input.
# Print "At least one is negative" if any
# one of the numbers is less than 0.
# Otherwise, print "All are non-negative".
# ==========================================================

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a < 0 or b < 0 or c < 0:
    print("At least one is negative")
else:
    print("All are non-negative")


# ==========================================================
# Question 7
# Take the temperature as input.
# Print the corresponding weather category.
# ==========================================================

temp = int(input("Enter the temperature: "))

if temp < 0:
    print("Freezing Cold")
elif temp <= 10:
    print("Very Cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Pleasant")
elif temp <= 40:
    print("Hot")
else:
    print("Very Hot")


# ==========================================================
# Question 8
# Take an integer n as input.
# Print "Hello World" n times.
# ==========================================================

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    print("Hello World")


# ==========================================================
# Question 9
# Take an integer n as input.
# Print all natural numbers from 1 to n.
# ==========================================================

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    print(i)


# ==========================================================
# Question 10
# Take an integer n as input.
# Print the numbers from n to 1
# using a reverse loop.
# ==========================================================

num = int(input("Enter a number: "))

for i in range(num, 0, -1):
    print(i)


# ==========================================================
# Question 11
# Take an integer as input.
# Print its multiplication table
# from 1 to 10.
# ==========================================================

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")


# ==========================================================
# Question 12
# Take an integer n as input.
# Calculate and print the sum
# of the first n natural numbers.
# ==========================================================

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print(total)