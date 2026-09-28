# ==========================================================
# Question 1
# Find all occurrences of a given element
# in a list using Linear Search.
# If the element is not found,
# print "Not Found".
# ==========================================================

l = [3, 7, 2, 7, 9, 7]

target = 7
pos = []

for i in range(len(l)):
    if l[i] == target:
        pos.append(i)

if pos == []:
    print("Not found")

else:
    print(target, "found at index", end=" ")

    for i in pos:
        print(i, end=" ")


# ==========================================================
# Question 2
# Count the total number of letters,
# digits, and special characters
# in a string without using
# built-in functions.
# ==========================================================

# print(ord('9'))

a = "P@#yn26at^&i5ve"

al = 0
dig = 0
spc = 0

for i in a:

    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        al += 1

    elif '0' <= i <= '9':
        dig += 1

    elif i == " ":
        pass

    else:
        spc += 1

print(al, dig, spc)


# ==========================================================
# Question 3
# Implement Binary Search
# to find an element
# in a sorted list.
# ==========================================================

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
     13, 14, 15, 16, 17, 18, 19, 20, 21]

t = 18

low = 0
high = len(a) - 1
mid = (low + high) // 2

while low <= high:

    if t == a[mid]:
        print("found at", mid)
        break

    elif t < a[mid]:
        high = mid - 1
        mid = (low + high) // 2

    elif t > a[mid]:
        low = mid + 1
        mid = (low + high) // 2

else:
    print("Not found")


# ==========================================================
# Question 4
# Implement Binary Search
# using a function.
# ==========================================================

def bin(a, s):

    low = 0
    high = len(a) - 1
    mid = (low + high) // 2

    while low <= high:

        if a[mid] == s:
            return f"found at {mid}"

        elif s > a[mid]:
            low = mid + 1
            mid = (low + high) // 2

        elif s < a[mid]:
            high = mid - 1
            mid = (low + high) // 2

    else:
        return "not found"


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(bin(a, 1))


# ==========================================================
# Question 5
# Check whether a list
# is sorted in ascending order.
# ==========================================================

a = [12, 13, 34, 45, 56, 65, 88, 99]

for i in range(len(a) - 1):

    if a[i] > a[i + 1]:
        print("Not sorted")
        break

else:
    print("Sorted")
