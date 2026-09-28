# ==========================================================
# Question 1
# Find the largest element in a list
# and print both the element and its index.
# ==========================================================

# Logic:
# Assume the first element is the largest.
# Compare it with every remaining element.
# If a larger element is found, update both
# the maximum value and its index.

l = [2, 96, 69, 77, 145, 20]

max = l[0]
index = 0

for i in range(len(l) - 1):

    if max < l[i + 1]:
        max = l[i + 1]
        index = i + 1

print(max, index)


# ==========================================================
# Question 2
# Find the smallest element in a list
# and print both the element and its index.
# ==========================================================

l = [2, 96, 69, 77, 145, 20]

less = l[0]
index = 0

for i in range(len(l) - 1):

    if less > l[i + 1]:
        less = l[i + 1]
        index = i + 1

print(less, index)


# ==========================================================
# Question 3
# Find the second largest element
# in a list.
# ==========================================================

l = [2, 96, 69, 77, 145, 20]

max = l[0]
sec_max = l[0]

for i in range(len(l)):

    if l[i] > max:
        sec_max = max
        max = l[i]

print(sec_max)


# ==========================================================
# Question 4
# Find the second smallest element
# in a list.
# ==========================================================



# ==========================================================
# Question 5
# Call one function from another function.
# ==========================================================

def greet():
    print("Hello, how are you?")

def m(a, b):
    greet()
    print(a * b)

m(2, 3)


# ==========================================================
# Question 6
# Demonstrate how the return statement
# exits a function after returning a value.
# ==========================================================

# The return statement performs two tasks:
# 1. Returns a value.
# 2. Immediately exits the function.


# ==========================================================
# Question 7
# Print numbers from 1 to 9
# using recursion.
# ==========================================================

def count(n):

    if n == 10:
        return

    print(n)
    count(n + 1)

count(1)


# ==========================================================
# Question 8
# Find the factorial of a number
# using recursion.
# ==========================================================

def factorial(n):

    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial(n - 1)

print(factorial(5))


# ==========================================================
# Notes
# Recursion Doubts
# ==========================================================

# def count(n)
# count(n + 1)
# count = n + 1
# count = count + 1


# ==========================================================
# Question 9
# Print all even numbers between
# 1 and 20 using a for loop.
# ==========================================================

n = 20

for i in range(1, n + 1):

    if i % 2 == 0:
        print(i)


# ==========================================================
# Question 10
# Take a word as input
# and print it in reverse order.
# ==========================================================

word = input("Enter a word: ")

print(word[::-1])


# ==========================================================
# Question 11
# Create a program that checks whether
# the length of a word is even or odd.
# ==========================================================



# ==========================================================
# Question 12
# Create a list of five numbers
# and print the square of each element.
# ==========================================================

l = [10, 20, 30, 40, 50]

for i in l:
    print(i ** 2)


# ==========================================================
# Question 13
# Create a new list containing only
# the fruits whose names have
# more than five letters.
# ==========================================================

fruits = ["apple", "banana", "cherry", "mango", "kiwi"]

new_list = []

for i in fruits:

    if len(i) > 5:
        new_list.append(i)

print(new_list)


# ==========================================================
# Notes
# Using the 'end' parameter in print()
# ==========================================================

# If you write:
#
# print("Hello ", end="")
# print("Brother")
#
# Output:
# Hello Brother
