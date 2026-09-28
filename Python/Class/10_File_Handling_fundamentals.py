"""
Question 1
Write a program to open and read the contents of a file.
"""
p = open(r"C:\Users\RMVMYT\Desktop\Pract.py")

print(p.read())

p.close()


"""
Question 2
Write a program to open and read a file from the current directory.
"""
p = open("main.py")

print(p.read())

p.close()


"""
Question 3
Write a program to append new content to an existing file.
"""
r = open("superman.txt", "a")

r.write("Adding new content inside the file.")

r.close()


"""
Question 4
Write a program to create a new file using file handling.
"""
x = open("suparimanva.txt", "x")

x.close()


"""
Question 5
Write a program to open a file in append mode.
"""
a = open("hulu.txt", "a")

a.write("Appending new content to the file.")

a.close()


"""
Question 6
Write a program to create a new Python file using file handling.
"""
x = open("crud.py", "x")

x.close()

