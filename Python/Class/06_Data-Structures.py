"""
Question 1
Write a program to demonstrate the difference between an integer and a single-element tuple.
"""
a = (1)
print(type(a))

a = (1,)
print(type(a))


"""
Question 2
Write a program to unpack the elements of a tuple into separate variables.
"""
a, b, c = (1, 2, 3)
print(a, b, c)


"""
Question 3
Write a program to find the hash value of a string.
"""
a = hash("Hello")
print(a)


"""
Question 4
Write a program to perform the union operation on two sets.
"""
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)


"""
Question 5
Write a program to perform basic dictionary operations
(add, update, modify, and delete elements).
"""
d = {1: 1, 2: 1}

d[1] = 100
d.update({3: 300})
d[40] = 40
del d[2]

print(d)


"""
Question 6
Write a program to print all the values of a dictionary.
"""
d = {1: 100, 3: 300, 40: 40}

for i in d.values():
    print(i)


"""
Question 7
Write a program to remove all elements from a dictionary.
"""
d = {10: 100, 20: 200, 30: 300}

d.clear()

print(d)


"""
Question 8
Write a program to create a copy of a dictionary and modify the copied dictionary.
"""
d = {10: 100, 20: 200, 30: 300}

new = d.copy()
new[10] = 2002

print("Original Dictionary:", d)
print("Copied Dictionary:", new)

