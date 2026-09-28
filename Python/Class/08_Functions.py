"""TOPIC: FUNCTIONS FUNDAMENTALS"""


"""
Functions are used to avoid writing repetitive code.
A function is created using the def keyword and executed by calling its name.
"""


"""
Question 1
Create a function that takes two numbers and prints their sum.
"""
def add():

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Sum =", a + b)
add()



"""
Question 2
Create a function that returns the sum of two numbers.
"""
def add():

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    return a + b


result = add()

print(result)



"""
Question 3
Create a function to check voting eligibility.
"""
def voting():

    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible to vote.")

    else:
        print("You are not eligible to vote.")


voting()



"""
Question 4
Create a function that takes parameters and arguments.
"""
def add(a, b):

    print("Sum =", a + b)


add(12, 55)



"""
Question 5
Create a function using keyword arguments.
"""
def student(name, age):

    print("Name:", name)
    print("Age:", age)


student(age=18, name="Rishit")



"""
Question 6
Create a function using default parameters.
"""
def registration(name, country="India"):

    print("Name:", name)
    print("Country:", country)


registration("Rishit")

registration("Akash", "USA")



"""TOPIC: FUNCTION CALLING & STACK"""


"""
Question 7
Demonstrate how functions are executed using the call stack.
"""
def hello():

    hello2()
    print("Hello 1")


def hello2():

    hello3()
    print("Hello 2")


def hello3():

    print("Hello 3")


hello()



"""TOPIC: RECURSION"""


"""
Question 8
Print numbers from 1 to 10 using recursion.
"""
def count(n):

    print(n)

    if n == 10:
        return

    count(n + 1)


count(1)



"""
Question 9
Print numbers from 10 to 1 using recursion.
"""
def count(n):

    print(n)

    if n == 1:
        return

    count(n - 1)


count(10)



"""
Question 10
Print even numbers from 1 to 10 using recursion.
"""
def even(n):

    if n > 10:
        return

    if n % 2 == 0:
        print(n)

    even(n + 1)


even(1)



"""
Question 11
Reverse print numbers using recursion.
"""
def count(n):

    if n == 10:
        return

    count(n + 1)

    print(n)


count(1)



"""TOPIC: PRACTICAL FUNCTION PROBLEMS"""


"""
Question 12
Create a function to check whether a number is palindrome or not.
"""
def palindrome(x):

    if x < 0:
        return False

    copy = x
    rev = 0

    while x > 0:

        digit = x % 10

        rev = (rev * 10) + digit

        x = x // 10


    return copy == rev


print(palindrome(11311))



"""
Question 13
Create a function to check whether a number is prime or not.
"""
def is_prime(num):

    for i in range(2, (num // 2) + 1):

        if num % i == 0:
            return False

    return True


print(is_prime(13))



"""
Question 14
Count the number of prime numbers between 1 and 100.
"""
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, (num // 2) + 1):

        if num % i == 0:
            return False

    return True



count = 0

for i in range(1, 100):

    if is_prime(i):
        count += 1


print("Prime numbers:", count)