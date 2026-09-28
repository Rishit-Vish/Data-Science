# ==========================================================
# Question 1
# Create a function to calculate the factorial
# of a given number.
# ==========================================================

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(100))


# ==========================================================
# Question 2
# Create a function with an optional parameter.
# If the user is not an NRI, keep the default value as None.
# ==========================================================

def reg(name, number, address, NRI=None):
    pass

reg("rishit", 54641691468, "Ayodhya Nagar")


# ==========================================================
# Question 3
# Create a function that greets the user
# using their name.
# ==========================================================

def greet(name):
    print(f"hello {name}, welcome to python")

greet("rishit")


# ==========================================================
# Question 4
# Create a function that returns
# the square of a number.
# ==========================================================

def sq(n):
    return n ** 2

print(sq(4))


# ==========================================================
# Question 5
# Build a simple calculator using functions
# and conditional statements.
# Perform addition, subtraction,
# multiplication, and exponentiation.
# ==========================================================

def calc():

    a = int(input("Tell "))
    b = int(input("tell 2 "))
    oper = input("tell your operator ")

    if oper == "+":
        print(a + b)

    elif oper == "-":
        print(a - b)

    elif oper == "*":
        print(a * b)

    elif oper == "**":
        print(a ** b)

    else:
        print("Invalied operation")

calc()

# Exercise:
# Modify this program so that the function
# returns the result instead of printing it.


# ==========================================================
# Question 6
# Create a function to calculate
# the average of three numbers.
# ==========================================================

def avg(a, b, c):

    sum = a + b + c
    div = 3
    average = sum // div

    return average

print(avg(2, 6, 4))


# ==========================================================
# Question 7
# Implement Binary Search to find
# a target element in a sorted list.
# ==========================================================

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

search = 14

low = 0
high = len(l) - 1
mid = (low + high) // 2

while low <= high:

    if l[mid] == search:
        print(f"found at the midlle index = {mid}")
        break

    elif l[mid] > search:
        high = mid - 1
        mid = (low + high) // 2

    elif l[mid] < search:
        low = mid + 1
        mid = (low + high) // 2

else:
    print("Noo elements found")


# ==========================================================
# Question 8
# Implement Binary Search to find
# a negative number in a sorted list.
# ==========================================================

a = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
     10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

low = 0
high = len(a) - 1
mid = (low + high) // 2

search = -5

while low <= high:

    if search == a[mid]:
        print(f"found at this index {mid}")
        break

    elif a[mid] > search:
        high = mid - 1
        mid = (low + high) // 2

    elif a[mid] < search:
        low = mid + 1
        mid = (low + high) // 2

else:
    print("noo elements found")


# ==========================================================
# Question 9
# Implement Linear Search to find
# an element in a list and print its index.
# ==========================================================

l = [12, 34, 45, 56, 63, 78, 98]

search = 78

for i in range(len(l)):

    if l[i] == search:
        print(f"{l[i]} is on the index {i}")
        break

else:
    print("nothing found")
