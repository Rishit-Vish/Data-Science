"""
File Name: 06_Leetcode_Array_Math_And_Sorting_Practice.py
"""


# ==========================================================
# Question 1
# Keep multiplying a number by 2 until the multiplied value
# is not found in the given array.
#
# Start with the original value.
# If it exists in nums, multiply it by 2.
# Continue this process until the value is missing.
#
# Return the final value.
# ==========================================================

def find_unique_double(original, nums):

    while original in nums:

        original *= 2

    return original


nums = [5, 3, 6, 1, 12]
original = 3

print(find_unique_double(original, nums))



# ==========================================================
# Question 2
# Count equal and divisible pairs in an array.
#
# Find pairs (i, j) where:
#
# 1. nums[i] == nums[j]
# 2. i < j
# 3. (i * j) is divisible by k
#
# Return the total number of valid pairs.
# ==========================================================

def countPairs(nums, k):

    count = 0
    n = len(nums)

    for j in range(1, n):

        for i in range(j):

            if nums[i] == nums[j] and (i * j) % k == 0:

                count += 1

    return count


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2

print(countPairs(nums, k))



# ==========================================================
# Question 3
# Rearrange an array based on index positions.
#
# Sort values at even indexes in increasing order.
# Sort values at odd indexes in decreasing order.
#
# Return the rearranged array.
#
# Example:
# Input:
# [4,1,2,3]
#
# Output:
# [2,3,4,1]
# ==========================================================

nums = [4, 1, 2, 3]

even = sorted(nums[::2])
odd = sorted(nums[1::2], reverse=True)

newnums = []

ei = 0
oi = 0

for i in range(len(nums)):

    if i % 2 == 0:

        newnums.append(even[ei])
        ei += 1

    else:

        newnums.append(odd[oi])
        oi += 1


print(newnums)



# ==========================================================
# Question 4
# Count the number of operations required to make
# either num1 or num2 equal to zero.
#
# In one operation:
#
# If num1 >= num2:
#     Subtract num2 from num1
#
# Otherwise:
#     Subtract num1 from num2
#
# Return total operations.
# ==========================================================

num1 = 2
num2 = 3

count = 0

while num1 > 0 and num2 > 0:

    if num1 >= num2:

        num1 = num1 - num2

    else:

        num2 = num2 - num1

    count += 1


print(count)



# ==========================================================
# Question 5
# Rearrange array values according to index rules.
#
# Even index values:
# Sort in increasing order.
#
# Odd index values:
# Sort in decreasing order.
#
# Return the final rearranged array.
# ==========================================================

nums = [4, 1, 2, 3]

even = sorted(nums[::2])
odd = sorted(nums[1::2], reverse=True)

result = []

even_index = 0
odd_index = 0


for i in range(len(nums)):

    if i % 2 == 0:

        result.append(even[even_index])
        even_index += 1

    else:

        result.append(odd[odd_index])
        odd_index += 1


print(result)



# ==========================================================
# Question 6
# Split a four digit number into two numbers such that
# their sum is minimum.
#
# Use all digits exactly once.
#
# Example:
# Input:
# 2932
#
# Possible:
# 22 + 93
#
# Return the minimum possible sum.
# ==========================================================

num = 2932

digits = sorted(str(num))

num1 = int(digits[0] + digits[2])

num2 = int(digits[1] + digits[3])

print(num1 + num2)



# ==========================================================
# Question 7
# Find the smallest index where:
#
# index % 10 == nums[index]
#
# Return the index.
# If no such index exists, return -1.
# ==========================================================

def smallestEqual(nums):

    for i in range(len(nums)):

        if i % 10 == nums[i]:

            return i

    return -1



nums = [0, 1, 2]

print(smallestEqual(nums))
