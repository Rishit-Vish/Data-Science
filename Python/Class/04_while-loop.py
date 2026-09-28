"""
Question 1
Write a program to print the digits of a number in reverse order.
"""
a = 256

while a > 0:
    print(a % 10)
    a = a // 10


"""
Question 2
Write a program to separate and print each digit of a number.
"""
a = 254

while a > 0:
    d = a % 10
    print(d)
    a = a // 10


"""
Question 3
Write a program to reverse a number.
(Using a for loop and string conversion)
"""
a = 543
rev = 0

for i in str(a):
    d = a % 10
    rev = rev * 10 + d
    a = a // 10

print(rev)


"""
Question 4
Write a program to separate each digit of a number.
"""
a = 456

while a > 0:
    print(a % 10)
    a = a // 10


"""
Question 5
Write a program to reverse a number using a while loop.
"""
a = 654
rev = 0

while a > 0:
    d = a % 10
    rev = rev * 10 + d
    a = a // 10

print(rev)


"""
Question 6
Write a program to check whether a number is a palindrome.
"""
a = 1221
rev = 0
copy = a

while a > 0:
    d = a % 10
    rev = rev * 10 + d
    a = a // 10

if copy == rev:
    print("The number is a Palindrome.")
else:
    print("The number is not a Palindrome.")


"""
Question 7
Write a number guessing game that keeps asking until the correct number is guessed.
"""
import random

a = random.randint(1, 9)
n = int(input("Guess a number (1-9): "))

while a != n:
    n = int(input("Incorrect! Try again: "))

print("Congratulations! You guessed the correct number.")


"""
Question 8
Write a number guessing game that gives hints (Higher/Lower).
"""
import random

a = random.randint(1, 100)
n = int(input("Guess a number (1-100): "))

while n != a:
    if n > a:
        print("Try a smaller number.")
        n = int(input("Guess again: "))
    else:
        print("Try a larger number.")
        n = int(input("Guess again: "))

print("Congratulations! You guessed the correct number.")


"""
Question 9
Write a number guessing game with only three attempts.
"""
import random

a = random.randint(1, 9)
trial = 3

while trial > 0:
    n = int(input("Guess a number (1-9): "))

    if n == a:
        print("Congratulations! You guessed the correct number.")
        break

    trial -= 1

    if trial > 0:
        print(f"Incorrect guess. You have {trial} attempt(s) remaining.")

else:
    print("Game Over! You have used all your attempts.")
    print(f"The correct number was {a}.")

'''while loop works on cond, and for loop works on number'''


"""
Question 10
Write a program to print numbers from 10 to 30 using a while loop.
"""
a = 10

while a <= 30:
    print(a)
    a = a + 1


"""
Question 11
Write a function to find the sum of two numbers and observe its return value.
"""
def sum(a, b):
    print(a + b)

new = sum(12, 12)
print(new)  # Output: None (because the function does not return any value)


"""
Question 12
Write a program to traverse and print all elements of a list.
"""
a = [1, 32, 4, 3, 33, 2]

for i in a:
    print(i)


