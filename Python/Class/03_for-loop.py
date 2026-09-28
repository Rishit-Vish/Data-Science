"""
Question 1
Write a program to print all even numbers from 2 to 20.
"""
a = range(2, 21, 2)
for i in a:
    print(i)


"""
Question 2
Write a program to print numbers from 4 to 9.
"""
for i in range(4, 10):
    print(i)


"""
Question 3
Write a program to print numbers from 16 to 1 in reverse order.
"""
for i in range(16, 0, -1):
    print(i)


"""
Question 4
Write a program to print even negative numbers from -12 to -38.
"""
for i in range(-12, -40, -2):
    print(i)


"""
Question 5
Write a program to print the multiplication table of a given number.
"""
n = int(input("Enter a number: "))
for i in range(n, (n * 10) + 1, n):
    print(i)


"""
Question 6
Write a program to print each character of a string using indexing.
"""
a = "SHERYIANS"
for i in range(len(a)):
    print(a[i])


"""
Question 7
Write a program to print each character of a string using a for loop.
"""
a = "SHERYIANS IS COOL"
for i in a:
    print(i)


"""
Question 8
Write a program to print numbers from 1 to 20, skipping 15 and 17.
"""
for i in range(1, 21):
    if i == 15 or i == 17:
        continue
    print(i)


"""
Question 9
Write a program to print 'Hello World' N times.
"""
n = int(input("Enter the number of times: "))
print("Hello World\n" * n)


"""
Question 10
Write a program to print numbers from 1 to N.
"""
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)


"""
Question 11
Write a program to print numbers from N to 1.
"""
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)


"""
Question 12
Write a program to print the multiplication table of a given number using two different approaches.
"""
n = int(input("Enter a number: "))

for i in range(n, n * 10 + 1, n):
    print(f"{n} x {i // n} = {i}")

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


"""
Question 13
Write a program to find the sum of the first N natural numbers.
"""
n = int(input("Enter a number: "))
s = 0

for i in range(n + 1):
    s += i

print("Sum =", s)


"""
Question 14
Write a program to find the factorial of a number.
"""
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)


"""
Question 15
Write a program to find the sum of even and odd numbers up to N.
"""
e = 0
o = 0

for i in range(n + 1):
    if i % 2 == 0:
        e += i
    else:
        o += i

print("Sum of Even Numbers =", e)
print("Sum of Odd Numbers =", o)


"""
Question 16
Write a program to print all the factors of a given number.
"""
for i in range(1, n + 1):
    if n % i == 0:
        print(i)


"""
Question 17
Write a program to check whether a number is a Perfect Number.
"""
copy = n
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

if copy == s:
    print("The number is a Perfect Number.")
else:
    print("The number is not a Perfect Number.")


"""
Question 18
Write a program to check whether a number is Prime or Not.
"""
for i in range(2, n):
    if n % i == 0:
        print("The number is not Prime.")
        break
else:
    print("The number is Prime.")


"""
Question 19
Reverse a string using slicing.
"""
a = "ABCDEF"
rev = a[::-1]
print(rev)


"""
Question 20
Reverse a string using a for loop.
"""
a = "ABCDEF"

rev = ""
for i in a:
    rev = i + rev

print(rev)


"""
Question 21
Reverse a string using reverse indexing.
"""
a = "ABCDEF"

rev = ""
for i in range(len(a) - 1, -1, -1):
    rev += a[i]

print(rev)


"""
Question 22
Reverse a string using reverse indexing (Alternative Approach).
"""
rev = ""

for i in range(len(a) - 1, -1, -1):
    rev += a[i]

print(rev)


"""
Question 23
Reverse the English alphabet.
"""
a = "ABCDEFGHIJKLNOPQRSTUVWXYZ"

rev = ""
for i in range(len(a) - 1, -1, -1):
    rev += a[i]

print(rev)


"""
Question 24
Write a program to check whether a string is a palindrome.
"""
x = "ABCBA"
copy = x
rev = ""

for i in x:
    rev = i + rev

if rev == x:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")


"""
Question 25
Write a program to count alphabets, digits, and special characters in a string.
"""
x = "P@ H4F%^  &ff  B(*NFI09 D"

chr = 0
spc = 0
n = 0

for i in x:
    if ("A" <= i <= "Z") or ("a" <= i <= "z"):
        chr += 1
    elif "0" <= i <= "9":
        n += 1
    elif i == " ":
        pass
    else:
        spc += 1

print("Alphabets:", chr)
print("Digits:", n)
print("Special Characters:", spc)


"""
Question 26
Write a program to count alphabets, digits, and special characters using string methods.
"""
chr = 0
spc = 0
n = 0

for i in x:
    if i.isdigit():
        n += 1
    elif i.isalpha():
        chr += 1
    elif i == " ":
        pass
    else:
        spc += 1

print("Alphabets:", chr)
print("Digits:", n)
print("Special Characters:", spc)


"""
Question 27
Display all the available methods of the string class.
"""
print(dir(str))