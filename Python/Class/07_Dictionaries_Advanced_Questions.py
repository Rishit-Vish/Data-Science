"""TOPIC: Dictionary Fundamentals"""

# Dictionary stores data in key:value pairs.
# Keys act like indexes.
# Keys must be unique and immutable.
# Values can be changed.

d = {
    "name": "Rishit",
    "age": 18,
    10: "Python"
}

print(d["name"])
print(d[10])



"""TOPIC: Traversing Dictionary"""

d = {
    1:100,
    2:200,
    3:300
}


# Keys
for i in d:
    print(i)


# Values
for i in d.values():
    print(i)


# Both keys and values
for key, value in d.items():
    print(key, value)



"""TOPIC: Dictionary Methods"""

d = {
    "name":"Rishit",
    "age":18
}


print(d.keys())

print(d.values())

print(d.items())

print(d.get("name"))


d.update({"city":"Delhi"})

d.pop("age")

print(d)



"""TOPIC: Merge Two Dictionaries"""


d1 = {
    1:10,
    2:20
}

d2 = {
    3:30,
    4:40
}


d1.update(d2)

print(d1)



"""TOPIC: Sum Dictionary Values"""


d = {
    1:10,
    2:20,
    3:30
}


total = 0

for value in d.values():
    total += value


print(total)



"""TOPIC: Frequency Counter"""


numbers = [
    1,2,1,3,2,1,4
]


frequency = {}


for i in numbers:

    if i not in frequency:
        frequency[i] = 1

    else:
        frequency[i] += 1


print(frequency)



"""TOPIC: Combine Dictionaries With Common Keys"""


d1 = {
    "a":10,
    "b":20
}

d2 = {
    "a":30,
    "c":40
}


for i in d2:

    if i in d1:
        d1[i] += d2[i]

    else:
        d1[i] = d2[i]


print(d1)