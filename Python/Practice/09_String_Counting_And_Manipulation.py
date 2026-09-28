# ==========================================================
# Question 1
# Count the total number of letters, digits, and special
# symbols in a given string.
#
# Given:
# "P@#yn26at^&i5ve"
#
# Expected:
# Letters = 8
# Digits = 3
# Symbols = 4
# ==========================================================


# Method 1: Store characters separately

text = "P@#yn26at^&i5ve"

letters = ""
digits = ""
symbols = ""

for i in range(len(text)):
    if text[i].isalpha():
        letters += text[i]
    elif text[i].isdigit():
        digits += text[i]
    else:
        symbols += text[i]

print("Letters:", letters)
print("Digits:", digits)
print("Symbols:", symbols)


# ==========================================================
# Question 2
# Count the number of letters, digits, and symbols
# from a given string.
# ==========================================================

text = "P@#yn26at^&i5ve"

letter_count = 0
digit_count = 0
symbol_count = 0

for char in text:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1

print("Letters:", letter_count)
print("Digits:", digit_count)
print("Symbols:", symbol_count)


# ==========================================================
# Question 3
# Separate letters, digits, and special symbols
# into different strings.
# ==========================================================

text = "P@#yn26at^&i5ve"

letters = ""
digits = ""
symbols = ""

for char in text:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        symbols += char

print("Letters:", letters)
print("Digits:", digits)
print("Symbols:", symbols)


# ==========================================================
# Question 4
# Understand escape characters.
#
# \t represents a tab space.
# \n represents a new line.
# ==========================================================

tab = "\t"

print(len(tab))
print(tab + "X")


newline = "\n"

print(len(newline))
print("A" + newline + "B")


# ==========================================================
# Question 5
# Compare two strings without using
# any string comparison functions.
# ==========================================================

first = "hello"
second = "hello"

if len(first) != len(second):
    print("Strings are different")

elif first == second:
    print("Strings are same")

else:
    print("Strings are different")


# ==========================================================
# Question 6
# Compare two strings character by character
# without directly using == for the whole string.
# ==========================================================

first = "hello"
second = "heLlo"

if len(first) != len(second):

    print("Strings are different")

else:

    for i in range(len(first)):
        if first[i] != second[i]:
            print("Strings are different")
            break

    else:
        print("Strings are same")


# ==========================================================
# Question 7
# Convert a Unicode value into its character
# using chr().
#
# Example:
# 65 → A
# ==========================================================

print(chr(65))


# ==========================================================
# Question 8
# Count the number of vowels in a given string.
# ==========================================================

text = "Elephant"

count = 0

for char in text:
    if char in "AEIOUaeiou":
        count += 1

print("Number of vowels:", count)


# ==========================================================
# Question 9
# Reverse a string without using slicing.
# ==========================================================

text = "elephant"

reverse = ""

for i in range(len(text) - 1, -1, -1):
    reverse += text[i]

print(reverse)