"""
Question 1
Write a program to handle the ZeroDivisionError exception.
"""
a = int(input("Enter a number: "))

print("Start")

try:
    print(10 / a)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("End")


"""
Question 2
Write a program to handle exceptions using a generic Exception object and the else block.
"""
a = int(input("Enter a number: "))

print("Start")

try:
    print(10 / a)

except Exception as err:
    print(f"An error occurred: {err}")

else:
    print("Division performed successfully.")

print("End")


"""
Question 3
Write a program to demonstrate the use of try, except, else, and finally blocks.
"""
a = int(input("Enter a number: "))

print("Start")

try:
    print(10 / a)

except Exception as err:
    print(f"An error occurred: {err}")

else:
    print("Division completed successfully.")

finally:
    print("This block always executes.")

print("Program Finished")


"""
Question 4
Write a program to raise a custom exception using the raise keyword.
"""
age = int(input("Enter your age: "))

try:
    if age < 10 or age > 18:
        raise ValueError("Age must be between 10 and 18.")
    else:
        print("Welcome to the club!")

except Exception as err:
    print(f"Access denied: {err}")

print("The club session will begin shortly.")