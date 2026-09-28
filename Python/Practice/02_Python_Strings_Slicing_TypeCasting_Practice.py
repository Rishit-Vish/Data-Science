"""
File Name: 
"""

# ==========================================================
# Question 1
# Take the string "Python".
# Slice the string from index 2 to index 4.
# If the sliced substring is not empty, print it in uppercase.
# Otherwise, print "Empty Slice".
# ==========================================================

text = "Python"

a = text[2:5]

if a:
    print(a.upper())
else:
    print("Empty Slice")


# ==========================================================
# Question 2
# Take a number as user input.
# Convert the input into an integer.
# If the number is greater than 100, print "Big Number".
# Otherwise, print "Small Number".
# ==========================================================

num = int(input("Enter a number: "))

if num > 100:
    print("Big Number")
else:
    print("Small Number")


# ==========================================================
# Question 3
# Take the string "programming".
# Find the Unicode value of its last character.
# If the Unicode value is less than 110, print "Small Char".
# Otherwise, print "Big Char".
# ==========================================================

s = "programming"

x = ord(s[-1])

if x < 110:
    print("Small Char")
else:
    print("Big Char")


# ==========================================================
# Question 4
# Print "ELOP" from the string "Developer"
# using only slicing and the upper() method.
# ==========================================================

word = "Developer"

a = word[3:7]
a = a.upper()

print(a)


# ==========================================================
# Question 5
# Take a number as a string.
# If the input is not empty, convert it into an integer,
# add 50, and print the result.
# Otherwise, print "Empty Input".
# ==========================================================

num = input("Enter a number: ")

if num != "":
    print(int(num) + 50)
else:
    print("Empty Input")


# ==========================================================
# Question 6
# Take a numeric string as input (e.g. "12345").
# Extract the last three digits using slicing.
# Convert them into an integer.
# Multiply the result by 2 and print it.
# ==========================================================

num = input("Enter a number: ")

num = int(num[-3:])
num = num * 2

print(num)


# ==========================================================
# Question 7
# Given the string "PYTHON123",
# extract only the numeric part using slicing.
# Find its average.
# If the average is greater than 3, print "BIG".
# Otherwise, print "SMALL".
# ==========================================================

text = "PYTHON123"

text = int(text[-3:])
avg = text // 3

if avg > 3:
    print("BIG")
else:
    print("SMALL")