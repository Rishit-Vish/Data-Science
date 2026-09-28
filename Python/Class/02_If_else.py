"""
Question 1
How do if-else statements execute based on a condition?
"""
a = 13
if a > 10:
    print('hello')
else:
    print('noo')

"""
Question 2
Write a program to check whether the entered amount is enough to buy a snack.
"""
a = int(input("Enter the amount: "))
if a > 10:
    print("You have enough money to buy a snack.")
else:
    print("Insufficient amount. Please enter at least ₹10.")


"""
Question 3
Write a program to suggest an ice cream based on the entered budget.
"""
a = int(input("Enter your budget: "))
if a >= 10 and a <= 20:
    print("Recommended Ice Cream: Chocobar")
elif a >= 20 and a <= 30:
    print("Recommended Ice Cream: Mango Ice Cream")
else:
    print("Recommended Ice Cream: Cone Ice Cream")


"""
Question 4
Write a program to find the greater of two numbers.
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print(a, "is greater than", b)
else:
    print(b, "is greater than", a)


"""
Question 5
Write a program to greet the user based on the entered gender.
(F/f for Female, M/m for Male)
"""
g = input("Enter your gender (M/F): ")
if g in "fF":
    print("Good Morning, Ma'am!")
elif g in "mM":
    print("Good Morning, Sir!")
else:
    print("Please enter a valid character (M/F).")


"""
Question 6
Write a program to check whether a number is even or odd.
"""
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


"""
Question 7
Write a program to check whether a person is eligible to vote.
"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Congratulations {name}, you are eligible to vote.")
else:
    a = 18 - age
    print(f"Sorry {name}, you can vote after {a} year(s).")


"""
Question 8
Write a program to check whether a given year is a leap year.
"""
yr = int(input("Enter a year: "))
if yr % 100 == 0 and yr % 400 == 0:
    print("It is a Leap Year.")
elif yr % 4 == 0 and yr % 100 != 0:
    print("It is a Leap Year.")
else:
    print("It is not a Leap Year.")


"""
Question 9
Write a program to display the weather condition based on temperature.
"""
temp = int(input("Enter the temperature: "))
if temp <= 0:
    print("Freezing Cold")
elif temp >= 0 and temp <= 10:
    print("Very Cold")
elif temp >= 10 and temp <= 20:
    print("Cold")
elif temp >= 20 and temp <= 30:
    print("Pleasant")
else:
    print("Very Hot")