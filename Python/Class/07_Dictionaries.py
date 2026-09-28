"""
Question 1
Write a program to merge two dictionaries.
"""
d = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}

d.update(d2)
print(d)


"""
Question 2
Write a program to find the sum of all values in a dictionary.
"""
d = {1: 10, 2: 20, 3: 30, 4: 40}

s = 0
for i in d:
    s += d[i]

print("Sum =", s)


"""
Question 3
Write a program to count the frequency of each element in a list using a dictionary.
"""
l = [1, 2, 32, 1, 2, 3, 2, 2, 1, 2, 2, 1, 3]

d = {}

for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)


"""
Question 4
Write a program to find the key having the maximum value in a dictionary.
"""
d = {"A": 20, "B": 55, "C": 12, "D": 70}

max_key = max(d, key=d.get)

print("Key:", max_key)
print("Value:", d[max_key])


"""
Question 5
Write a program to find the key having the minimum value in a dictionary.
"""
d = {"A": 20, "B": 55, "C": 12, "D": 70}

min_key = min(d, key=d.get)

print("Key:", min_key)
print("Value:", d[min_key])


"""
Question 6
Write a program to remove a key from a dictionary if it exists.
"""
d = {1: 100, 2: 200, 3: 300}

key = 2

if key in d:
    del d[key]

print(d)


"""
Question 7
Write a program to check whether a key exists in a dictionary.
"""
d = {1: 10, 2: 20, 3: 30}

key = 2

if key in d:
    print("Key exists.")
else:
    print("Key not found.")


"""
Question 8
Write a program to create a dictionary from two lists.
"""
keys = ["A", "B", "C", "D"]
values = [10, 20, 30, 40]

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)


"""
Question 9
Write a program to invert a dictionary (swap keys and values).
"""
d = {"A": 10, "B": 20, "C": 30}

new = {}

for i in d:
    new[d[i]] = i

print(new)


"""
Question 10
Write a program to sort a dictionary by its keys.
"""
d = {3: 300, 1: 100, 4: 400, 2: 200}

for key in sorted(d):
    print(key, ":", d[key])


"""
Question 11
Write a program to sort a dictionary by its values.
"""
d = {"A": 40, "B": 10, "C": 60, "D": 20}

items = list(d.items())

items.sort(key=lambda x: x[1])

print(items)


"""
Question 12
Write a program to find the frequency of each character in a string.
"""
s = "programming"

d = {}

for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1

print(d)


"""
Question 13
Write a program to remove duplicate values from a dictionary.
"""
d = {"A": 10, "B": 20, "C": 10, "D": 30, "E": 20}

new = {}

for key, value in d.items():
    if value not in new.values():
        new[key] = value

print(new)