# ==========================================================
# Question 1
# Merge two dictionaries into a single dictionary.
# ==========================================================

d1 = {1: 10, 2: 20, 3: 30, 4: 40}
d2 = {5: 50, 6: 60}

for i in d1:
    if i not in d2:
        d2[i] = d1[i]

print(d2)

# Exercise:
# Print the merged dictionary in ascending order of keys.


# ==========================================================
# Question 2
# Write a function to calculate the sum
# of all even numbers in a list.
# ==========================================================

def even(a):

    sum = 0

    for i in a:
        if i % 2 == 0:
            sum += i

    return sum


a = [1, 2, 3, 4, 5, 6]

print(even(a))


# ==========================================================
# Question 3
# Remove duplicate elements from a list
# while preserving the original order.
# ==========================================================

l = [1, 3, 2, 3, 4, 1, 5]

l2 = []

for i in l:
    if i not in l2:
        l2.append(i)

print(l2)


# ==========================================================
# Question 4
# Print "Hello World" n times
# without using a for loop.
# ==========================================================

n = int(input("Enter a number: "))

print("Hello World\n" * n)


# ==========================================================
# Question 5
# Print "Hello World" n times
# using a for loop.
# ==========================================================

n = int(input("Enter a number: "))

for _ in range(n):
    print("Hello World")


# ==========================================================
# Question 6
# Print the first 10 Fibonacci numbers.
# ==========================================================

a = 0
b = 1

for i in range(10):
    print(a)
    a, b = b, a + b


# ==========================================================
# Question 7
# Print the first N Fibonacci numbers.
# Display all numbers in a single line
# separated by commas.
# ==========================================================

n = int(input("Enter the value of N: "))

a = 0
b = 1

for i in range(n):
    print(a, ",", end="")
    a, b = b, a + b


# ==========================================================
# Question 8
# Find whether a number
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
# Question 9
# Check whether a list
# is sorted in ascending order.
# ==========================================================

l = [1, 2, 3, 4, 6, 88]

for i in range(len(l) - 1):

    if l[i] > l[i + 1]:
        print("List is not sorted")
        break

else:
    print("List is sorted")


# ==========================================================
# Question 10
# Create a password checker.
# Keep asking the user for the password
# until the correct password is entered.
# ==========================================================

password = 123456

while True:

    n = int(input("Enter the password: "))

    if n == password:
        print("Access Granted")
        break

    else:
        print("Incorrect password. Try again.")


# ==========================================================
# Question 11
# Check whether two strings
# are anagrams of each other.
# ==========================================================

a = sorted("Silent".lower())
b = sorted("Listen".lower())

if len(a) != len(b):
    print("Not Anagrams")

else:
    for i in a:

        if i not in b:
            print("Not Anagrams")
            break

        else:
            print("Anagrams")
            break


# ==========================================================
# Question 12
# Find the first non-repeating
# character in a string.
# ==========================================================

# Logic:
# Traverse each character in the string.
# Count its occurrences.
# The first character whose count is 1
# is the first non-repeating character.

s = "aabccdeee"

for i in s:

    if s.count(i) == 1:
        print(i)
        break
