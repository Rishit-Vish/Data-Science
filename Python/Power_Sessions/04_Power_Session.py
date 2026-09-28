"""
File Name: 19_Python_Loops_Number_Logic_And_List_Rotation.py
"""


# ==========================================================
# Question 1
# Create a password checker.
# Keep asking the user for the password
# until the correct password is entered.
# ==========================================================

a = 123

while True:

    n = int(input("Enter password: "))

    if n == a:
        break

    else:
        print("Incorrect password")

print(f"User entered {n}. Access Granted")


# ==========================================================
# Question 2
# Implement the Collatz Sequence.
#
# Rules:
# If n is even:
#     Divide n by 2
#
# If n is odd:
#     Multiply n by 3 and add 1
#
# Repeat until n becomes 1.
# Count the number of steps required.
# ==========================================================

n = int(input("Enter your number: "))

count = 0

while n > 1:

    if n % 2 == 0:
        n /= 2

    else:
        n = (n * 3) + 1

    count += 1

print("Total steps:", count)


# ==========================================================
# Question 3
# Rotate a list by K positions.
#
# Example:
#
# Input:
# l = [1,2,3,4,5,6]
# k = 2
#
# Output:
# [5,6,1,2,3,4]
#
# The last K elements should move
# to the beginning of the list.
# ==========================================================

l = [1, 2, 3, 4, 5, 6]

k = 2

for i in range(k):

    last = l[-1]

    for j in range(len(l) - 1, 0, -1):
        l[j] = l[j - 1]

    l[0] = last

print(l)
