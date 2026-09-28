"""
---------- Definition --------------
Attributes - var defined inside a class
Methods - Functions defined inside a class
"""

"""Prediction of a nation's development ?
Prediction of a company - bu tmaybe made by 10000's ?
https://www.datacamp.com/blog/machine-learning-projects-for-all-levels
"""
"""
Question 1
What is the data type of the result after dividing a number by a complex number?
"""
a = 1/3j
print(type(a))


"""
Question 2
How do you access a character from a string using negative indexing?
"""
a = "SHER"
print(a[-3])


"""
Question 3
How do string slicing and indexing work in Python?
"""
a = 'SHERYIANS coder'
print(a[2:11:3])
print(a[3:])


"""
Question 4
How do you convert an integer into a string?
"""
a = 12
a = str(a)
print(type(a))


"""
Question 5
How do you convert a string into an integer?
"""
a = "12"
a = int(a)
print(type(a))


"""
Question 6
What is the boolean value of a non-zero integer?
"""
a = 12
print(bool(a))


"""
Question 7
What is the boolean value of zero?
"""
a = 0
print(bool(a))


"""
Question 8
What is the result of normal division (/) in Python?
"""
print(12/3)  # answer - 4.0


"""
Question 9
How do you use f-strings to format and print variables?
"""
name = 'rishit'
age = 12
print(f"my name is {name} and age is {age}")


"""
Question 10
How do you take integer input from the user?
"""
a = int(input('what age are you? '))
print(a)


"""
Question 11
How do floor division (//), modulus (%), and operator precedence work?
"""
print(12//3)
a = 4
b = 2
print(32%5)
print(12 + 4//2)


"""
Question 12
How do assignment operators (+= and *=) modify a variable?
"""
a = 12
a += 12
a *= 5
print(a)


"""
Question 13
How do you find the ASCII/Unicode value of a character?
"""
print(ord('A'))


"""
Question 14
How do comparison operators work with characters and strings?
"""
print('A' > 'B')
print('abc' > 'acd')


"""
Question 15
How do logical operators (and, or) evaluate expressions?
"""
print(12 > 1 or 45 < 4 and 552 < 54)


"""
Question 16
How does the 'not' operator work in Python?
"""
print(not 12 == 14)


"""
Question 17
How does the 'and' operator work with boolean values?
"""
print(True and bool(0))

