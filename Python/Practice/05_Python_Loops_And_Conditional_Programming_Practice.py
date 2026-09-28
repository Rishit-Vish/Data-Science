# ==========================================================
# Question 1
# Take an integer as input.
# Calculate and print its factorial.
# ==========================================================

fact = int(input("Enter a number: "))

result = 1

for i in range(1, fact + 1):
    result *= i

print(result)


# ==========================================================
# Question 2
# Take an integer n as input.
# Calculate and print the sum of all even
# and odd numbers separately from 1 to n.
# ==========================================================

n = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")


# ==========================================================
# Question 3
# Take an integer as input.
# Print all of its factors.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


# ==========================================================
# Question 4
# Take three integers as input.
# Check whether:
# - All three numbers are equal.
# - Any two numbers are equal.
# - Otherwise, all numbers are different.
# ==========================================================

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b == c:
    print("All numbers are equal")
elif a == b or b == c or a == c:
    print("Any two numbers are equal")
else:
    print("All numbers are different")


# ==========================================================
# Question 5
# Take two integers as input.
# Print the greater number.
# ==========================================================

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")


# ==========================================================
# Question 6
# Take the user's name and age as input.
# Check whether the user is eligible to vote.
# If not, print after how many years
# the user will become eligible.
# ==========================================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are eligible to vote.")
elif age > 0:
    years = 18 - age
    print(f"Sorry {name}, you are not eligible to vote.")
    print(f"You will be eligible after {years} year(s).")
else:
    print("Please enter a valid age.")


# ==========================================================
# Question 7
# Take an English alphabet as input.
# Check whether it is a vowel or a consonant.
# ==========================================================

alphabet = input("Enter an alphabet: ")

if alphabet in "aeiouAEIOU":
    print(f"{alphabet} is a vowel.")
else:
    print(f"{alphabet} is a consonant.")


# ==========================================================
# Question 8
# Take an integer n as input.
# Print "Hello World" n times.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("Hello World")


# ==========================================================
# Question 9
# Take an integer n as input.
# Print all natural numbers from 1 to n.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)


# ==========================================================
# Question 10
# Take an integer n as input.
# Print the numbers from n to 1.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i)


# ==========================================================
# Question 11
# Take an integer as input.
# Print its multiplication table
# from 1 to 10.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")


# ==========================================================
# Question 12
# Take an integer n as input.
# Print the sum of the first n natural numbers.
# ==========================================================

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print(total)


# ==========================================================
# Question 13
# Take an integer n as input.
# Print the numbers from n to 1
# using a reverse loop.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i)


# ==========================================================
# Question 14
# Take an integer as input.
# Print its multiplication table
# from 1 to 10.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")


# ==========================================================
# Question 15
# Take an integer n as input.
# Calculate and print the sum of all even
# and odd numbers separately from 1 to n.
# ==========================================================

n = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")