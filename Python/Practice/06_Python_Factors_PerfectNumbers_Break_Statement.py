# ==========================================================
# Question 1
# Take two integers as input.
# Print all numbers in the given range that are
# divisible by either 3 or 5.
# ==========================================================

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for i in range(start, end + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)


# ==========================================================
# Question 2
# Take an integer as input.
# Print all of its factors.
# ==========================================================

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


# ==========================================================
# Question 3
# Take an integer as input.
# Calculate and print the sum of all its proper factors
# (excluding the number itself).
#
# Example:
# 50 → 1 + 2 + 5 + 10 + 25 = 43
# ==========================================================

n = int(input("Enter a number: "))

factor_sum = 0

for i in range(1, n):
    if n % i == 0:
        factor_sum += i

print(factor_sum)


# ==========================================================
# Question 4
# Take an integer as input.
# Check whether it is a Perfect Number.
#
# A Perfect Number is a number whose sum of proper
# factors (excluding itself) is equal to the number.
#
# Example:
# 6 → 1 + 2 + 3 = 6
# ==========================================================

n = int(input("Enter a number: "))

factor_sum = 0

for i in range(1, n):
    if n % i == 0:
        factor_sum += i

if factor_sum == n:
    print(f"{n} is a Perfect Number.")
else:
    print(f"{n} is not a Perfect Number.")


# ==========================================================
# Question 5
# Print numbers from 1 to 9.
# Stop the loop before printing 5.
# ==========================================================

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# ==========================================================
# Question 6
# Print numbers from 1 to 9.
# Print 5 first, then stop the loop.
# ==========================================================

for i in range(1, 10):
    print(i)
    if i == 5:
        break


# ==========================================================
# Question 7
# Print numbers from 1 to 10.
# Stop the loop when the number becomes 7.
#
# Output:
# 1 2 3 4 5 6
# ==========================================================

for i in range(1, 11):
    if i == 7:
        break
    print(i)


# ==========================================================
# Question 8
# Print numbers starting from 1.
# Stop when a number is divisible by both
# 3 and 5.
#
# Output ends at 15.
# ==========================================================

for i in range(1, 100):
    print(i)

    if i % 3 == 0 and i % 5 == 0:
        break


# ==========================================================
# Question 9
# Demonstrate the difference between placing
# break before and after print().
# ==========================================================

# Example 1: break before print()
for i in range(1, 20):
    if i == 10:
        break
    print(i)

print("-" * 30)

# Example 2: print() before break
for i in range(1, 20):
    print(i)
    if i == 10:
        break

"""
Key Difference:

1. If 'break' comes before 'print()', the loop exits
   before printing the target value.

2. If 'print()' comes before 'break', the target value
   is printed first, and then the loop terminates.

Choose the order depending on whether you want the
stopping value to appear in the output.
"""


# ==========================================================
# Question 10
# Take an integer as input.
# Print its smallest factor greater than 1.
# If no such factor exists, print "Prime".
# ==========================================================

n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print(i)
        break
else:
    print("Prime")


# ==========================================================
# Question 11
# Print numbers from 1 to 10.
# Stop the loop before printing 5.
# ==========================================================

for i in range(1, 11):
    if i == 5:
        break
    print(i)