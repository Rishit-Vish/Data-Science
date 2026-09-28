# ==========================================================
# Question 1
# Print the last, second last, and third last characters
# of the string "COMPUTER" using negative indexing.
# ==========================================================

word = "COMPUTER"
print(word[-1], word[-2], word[-3])


# ==========================================================
# Question 2
# Print the index of the last character of the string
# "COMPUTER" using len().
# ==========================================================

word = "COMPUTER"
print(len(word) - 1)


# ==========================================================
# Question 3
# Print the negative index of the first character of
# the string "COMPUTER" using len().
# ==========================================================

word = "COMPUTER"
print(-len(word))


# ==========================================================
# Question 4
# Print every second character from the string
# "COMPUTER" using slicing.
# ==========================================================

word = "COMPUTER"
print(word[::2])


# ==========================================================
# Question 5
# Print every second character from the string
# "DEVELOPER" in reverse order using slicing.
# ==========================================================

word = "DEVELOPER"
print(word[::-2])


# ==========================================================
# Question 6
# Print the file path
# C:\new_folder\test
# without using escape characters.
# ==========================================================

print(r"C:\new_folder\test")


# ==========================================================
# Question 7
# Take a number as input (string), convert it to an integer,
# and print its square.
# ==========================================================

a = input("Number? ")
b = int(a)
print(b ** 2)


# ==========================================================
# Question 8
# Convert the string "20" into an integer,
# add 5, and print the result.
# ==========================================================

a = "20"
b = int(a) + 5
print(b)


# ==========================================================
# Question 9
# Combine the string "20" and integer 5
# to get the string "205".
# ==========================================================

a = "20"
b = "5"
c = a + b
print(c)


# ==========================================================
# Question 10
# Convert the string "3.5" into a float,
# add 2.5, and print the result.
# ==========================================================

a = float("3.5")
b = 2.5
print(a + b)


# ==========================================================
# Question 11
# Combine the integer 100 and string "kg"
# to print "100kg".
# ==========================================================

a = "100" + "kg"
print(a)


# ==========================================================
# Question 12
# Extract the number from "100kg",
# convert it to an integer,
# add 50, and print the result.
# ==========================================================

a = "100kg"
b = a[:3]
print(b)

b = int(b) + 50
print(b)


# ==========================================================
# Question 13
# Convert the strings "10" and "20"
# into integers and print their sum.
# ==========================================================

a = int("10")
b = int("20")
print(a + b)


# ==========================================================
# Question 14
# Concatenate the strings "10" and "20"
# to print "1020".
# ==========================================================

print("10" + "20")


# ==========================================================
# Question 15
# Repeat the string "7" three times.
# ==========================================================

print("7" * 3)


# ==========================================================
# Question 16
# Predict and verify the output of
# 7 * "3".
# ==========================================================

print(7 * "3")


# ==========================================================
# Question 17
# Print "Python3" by combining the string
# "Python" and integer 3 without an error.
# ==========================================================

a = str(3)
print("Python" + a)


# ==========================================================
# Question 18
# Print the Unicode value of the character 'A'
# using ord().
# ==========================================================

print(ord('A'))


# ==========================================================
# Question 19
# Check whether an empty dictionary is
# truthy or falsy.
# ==========================================================

x = {}

if x:
    print("Truthy")
else:
    print("Falsy")


# ==========================================================
# Question 20
# Convert the character 'Z' into its Unicode value
# using ord(). If it is even, print "Even Unicode",
# otherwise print "Odd Unicode".
# ==========================================================

a = ord('Z')

if a % 2 == 0:
    print("Even Unicode")
else:
    print("Odd Unicode")