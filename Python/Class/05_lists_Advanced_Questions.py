"""
Question 1
Given a list of numbers, find two elements whose sum is equal to the given target value.
Print the pair of numbers if found.
"""

l = [2, 10, 6, 34, 14, 7]
target = 9

for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            print(l[i], l[j])
            break


"""
Question 2
Given a list of numbers, find three elements whose sum is equal to the target value.
Print the three elements if found.
"""

l = [12, 34, 3, 5, 6, 7, 2, 8]
target = 11

for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            if l[i] + l[j] + l[k] == target:
                print(l[i], l[j], l[k])
                break


"""
Question 3
Separate positive and negative numbers from a list.
Store them in different lists.
"""

l = [-10, 12, 45, -18, -2, 4, 5]

positive = []
negative = []

for i in l:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)

print(positive)
print(negative)


"""
Question 4
Find the largest element from a list without using max().
"""

l = [12, 32, 549, 2, 36, 776, 3, 34]

largest = l[0]

for i in l:
    if i > largest:
        largest = i

print(largest)


"""
Question 5
Find the largest and second largest element from a list without sorting.
"""

l = [12, 34, 24, 6, 64, 7, 56, 112, 66]

largest = l[0]
second = l[0]

for i in l:
    if i > largest:
        second = largest
        largest = i

    elif i > second and i != largest:
        second = i

print("Second largest:", second)
print("Largest:", largest)


"""
Question 6
Find the smallest and second smallest element from a list without sorting.
"""

l = [12, 34, 44, 3, 54, 24, 2, 54]

small = l[0]
second_small = l[0]

for i in l:
    if i < small:
        second_small = small
        small = i

    elif i < second_small and i != small:
        second_small = i

print("Second smallest:", second_small)
print("Smallest:", small)


"""
Question 7
Reverse a list without using reverse() method.
"""

l = [1, 2, 3, 4, 5]

reverse = []

for i in range(len(l)-1, -1, -1):
    reverse.append(l[i])

print(reverse)


"""
Question 8
Remove duplicate elements from a list without using set().
"""

l = [10, 20, 30, 10, 40, 20, 50]

new_list = []

for i in l:
    if i not in new_list:
        new_list.append(i)

print(new_list)


"""
Question 9
Count frequency of each element in a list.
"""

l = [10, 20, 10, 30, 20, 10, 40]

frequency = []

for i in l:
    if i not in frequency:
        count = 0

        for j in l:
            if i == j:
                count += 1

        frequency.append(i)
        print(i, "appears", count, "times")


"""
Question 10
Search an element in a list using linear search.
Print its index if found.
"""

l = [12, 23, 4, 2, 34, 453, 54, 21]

search = 54

for i in range(len(l)):
    if l[i] == search:
        print("Found at index:", i)
        break

else:
    print("Not found")


"""
Question 11
Search an element from a sorted list using binary search.
"""

l = [10, 20, 30, 40, 50, 60, 70, 80]

search = 60

low = 0
high = len(l)-1

while low <= high:

    mid = (low + high) // 2

    if l[mid] == search:
        print("Found at index:", mid)
        break

    elif l[mid] < search:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Not found")


"""
Question 12
Check whether a list is sorted in ascending order or not.
"""

l = [12, 20, 30, 40, 50]

for i in range(len(l)-1):

    if l[i] > l[i+1]:
        print("Not sorted")
        break

else:
    print("Sorted")


"""
Question 13
Sort an unsorted list using Bubble Sort algorithm.
Do not use sort().
"""

l = [34, 2, 54, 29, 4, 44, 25]

for j in range(len(l)-1):

    for i in range(len(l)-1-j):

        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]

print(l)


"""
Question 14
Check whether a list is palindrome or not.
A palindrome list is same from both directions.
"""

arr = [2, 3, 15, 15, 3, 2]

if arr == arr[::-1]:
    print("Palindrome")

else:
    print("Not palindrome")


"""
Question 15
Find two elements whose multiplication equals the target value.
"""

l = [2, 4, 54, 323, 45, 3]

target = 6

for i in range(len(l)-1):

    for j in range(i+1, len(l)):

        if l[i] * l[j] == target:
            print(l[i], l[j])
            break


"""
Question 16
Rotate a list to the right by given number of positions.
"""

l = [1, 2, 3, 4, 5]

k = 2

for i in range(k):
    last = l.pop()
    l.insert(0, last)

print(l)


"""
Question 17
Merge two lists and sort the final list without using sort().
"""

l1 = [10, 30, 50]
l2 = [20, 40, 60]

l = l1 + l2

for j in range(len(l)-1):

    for i in range(len(l)-1-j):

        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]

print(l)


"""
Question 18
Find the maximum sum of continuous elements in a list.
"""

l = [-2, 3, 4, -1, 2, 1, -5, 4]

current_sum = l[0]
maximum_sum = l[0]

for i in range(1, len(l)):

    current_sum = max(l[i], current_sum + l[i])

    if current_sum > maximum_sum:
        maximum_sum = current_sum

print(maximum_sum)


"""
Question 19
Find common elements between two lists without using set().
"""

l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]

common = []

for i in l1:
    if i in l2:
        common.append(i)

print(common)


"""
Question 20
Move all zeros to the end of a list while maintaining order of other elements.
"""

l = [0, 1, 0, 3, 12, 0, 5]

result = []

zero_count = 0

for i in l:
    if i == 0:
        zero_count += 1
    else:
        result.append(i)

for i in range(zero_count):
    result.append(0)

print(result)

