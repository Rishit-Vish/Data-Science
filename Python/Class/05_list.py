"""
Question 1
Write a program to access and print the first element of a list.
"""
l = [1, 2, 3, 4, 5]

print(l[0])


"""
Question 2
Write a program to separate positive and negative elements of a list.
"""
l = [1, -2, 43, 3, -89, -4]

p = []
n = []

for i in range(len(l)):
    if l[i] > 0:
        p.append(l[i])
    else:
        n.append(l[i])

print("Positive Elements:", p)
print("Negative Elements:", n)


"""
Question 3
Write a program to find the mean (average) of the elements in a list.
"""
l = [1, 2, 3, 4, 5]

print("Mean =", sum(l) / len(l))


"""
Question 4
Write a program to find the largest element in a list and print its index.
"""
l = [1, 2, 34, 5, 43, 5, 6]

largest = l[0]
idx = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        idx = i

print("Largest Element:", largest)
print("Index:", idx)


"""
Question 5
Write a program to find the second largest element in a list.
"""
l = [12, 3, 54, 3, 56, 78, 6, 7, 99, 55, 78, 990]

lar = l[0]
sec_lar = l[0]

for i in range(len(l)):
    if l[i] > lar:
        sec_lar = lar
        lar = l[i]
    elif l[i] > sec_lar and l[i] != lar:
        sec_lar = l[i]

print("Largest Element:", lar)
print("Second Largest Element:", sec_lar)


"""
Question 6
Write a program to sort a list using Bubble Sort.
"""
l = [12, 43, 55, 3, 5, 22, 1, 12, 7, 88, 65, 46]

for j in range(len(l)):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]

print("Sorted List:", l)
