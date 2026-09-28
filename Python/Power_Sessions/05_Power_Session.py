"""
File Name: 05_Leetcode_Array_And_Hashing_Practice.py
"""


# ==========================================================
# Question 1
# Count the number of unique elements in a list
# and find how many elements appear only once.
#
# Example:
# [1,3,1,5,3,5]
#
# Unique values are the elements that appear
# only one time after removing duplicates.
# ==========================================================

d = {}                         
for i in d:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

pairs = 0
leftovers = 0

for j in d.values():
    pairs = pairs + j // 2
    leftovers = leftovers + j % 2


# ==========================================================
# Question 2
# Count hills and valleys in an array.
#
# A hill is an element that is greater than
# its closest non-equal neighbours.
#
# A valley is an element that is smaller than
# its closest non-equal neighbours.
#
# Ignore consecutive duplicate values.
# ==========================================================

def count_hills_and_valleys(nums):

    new = []

    for i in nums:

        if not new or i != new[-1]:
            new.append(i)


    count = 0

    for j in range(1, len(new) - 1):

        if new[j] > new[j - 1] and new[j] > new[j + 1]:
            count += 1

        elif new[j] < new[j - 1] and new[j] < new[j + 1]:
            count += 1


    return count


nums = [2, 4, 1, 1, 6, 5]

print(count_hills_and_valleys(nums))


# ==========================================================
# Question 3
# Divide an array into equal pairs.
#
# Given an array with 2*n elements,
# check whether it can be divided into pairs
# where every pair contains equal elements.
#
# Return True if all elements can form pairs,
# otherwise return False.
# ==========================================================

def divideArray(nums):

    d = {}

    for i in nums:

        if i not in d:
            d[i] = 1

        else:
            d[i] += 1


    pairs = 0
    leftovers = 0

    for j in d.values():

        pairs += j // 2
        leftovers += j % 2


    if pairs == len(nums) // 2:
        return True

    return False


nums = [3, 2, 3, 2, 2, 2]

print(divideArray(nums))


# ==========================================================
# Question 4
# Find the number of pairs and leftover elements
# after making maximum possible pairs.
#
# A pair can only be formed using two equal numbers.
#
# Return:
# [number_of_pairs, number_of_leftover_elements]
#
# Example:
# [1,3,2,1,3,2,2]
# Output:
# [3,1]
# ==========================================================


nums = [1, 3, 2, 1, 3, 2, 2]

d = {}

for i in nums:

    if i not in d:
        d[i] = 1

    else:
        d[i] += 1


p = 0
l = 0

for j in d.values():

    p += j // 2
    l += j % 2


print(p, l)


# ==========================================================
# Question 5
# Find the minimum number of operations required
# to make all elements of an array zero.
#
# In one operation, subtract the smallest
# non-zero value from all positive elements.
#
# Count how many operations are needed.
# ==========================================================


nums = [1, 5, 0, 3, 5]

s = set()

for i in nums:

    if i == 0:
        continue

    s.add(i)


print(len(s))


# ==========================================================
# Question 6
# Apply the given min-max algorithm repeatedly
# until only one element remains.
#
# For even indexes:
# Store the minimum of the pair.
#
# For odd indexes:
# Store the maximum of the pair.
#
# Return the final remaining number.
# ==========================================================


nums = [1, 3, 5, 2, 4, 8, 2, 2]

while len(nums) > 1:

    newNums = []

    for i in range(len(nums) // 2):

        if i % 2 == 0:

            newNums.append(
                min(nums[2 * i], nums[2 * i + 1])
            )

        else:

            newNums.append(
                max(nums[2 * i], nums[2 * i + 1])
            )

    nums = newNums


print(nums[0])


# ==========================================================
# Question 7
# Count hills and valleys in an array.
#
# First remove consecutive duplicate elements.
# Then count elements which are either:
#
# Hill:
# Previous < Current > Next
#
# Valley:
# Previous > Current < Next
# ==========================================================


def count_hills_and_valleys(nums):

    new = []

    for i in nums:

        if not new or i != new[-1]:
            new.append(i)


    count = 0

    for j in range(1, len(new) - 1):

        if new[j] > new[j - 1] and new[j] > new[j + 1]:
            count += 1

        elif new[j] < new[j - 1] and new[j] < new[j + 1]:
            count += 1


    return count



nums = [2, 4, 1, 1, 6, 5]

print(count_hills_and_valleys(nums))


# ==========================================================
# Question 8
# Remove duplicate elements from a list
# while keeping only unique values.
# ==========================================================


nums = [2, 4, 1, 1, 6, 5]

new = []

for i in nums:

    if i not in new:
        new.append(i)


print(new)
