"""TOPIC: ENCAPSULATION (Private Members & Name Mangling)"""


"""
Question 1
Create a private method inside a class and access it using name mangling.
"""
class ABC:

    def __hulu(self):
        print("Hello World, I am Rishit.")


obj = ABC()

obj._ABC__hulu()



"""
Question 2
Create a private variable and access it using name mangling.
"""
class Student:

    def __init__(self):
        self.__marks = 95


obj = Student()

print(obj._Student__marks)



"""
Question 3
Create a class with private data and access it using a getter method.
"""
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks


    def get_marks(self):
        return self.__marks


student = Student("Rishit", 90)

print(student.get_marks())



"""
Question 4
Create a class with private data and update it using a setter method.
"""
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


    def get_balance(self):
        return self.__balance


    def set_balance(self, amount):

        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid balance amount.")


account = BankAccount(5000)

print("Old Balance:", account.get_balance())

account.set_balance(8000)

print("New Balance:", account.get_balance())



"""
Question 5
Create a real-world bank system using encapsulation.
"""
class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance


    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")

        else:
            print("Invalid amount.")


    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")

        else:
            print("Insufficient balance.")


    def show_balance(self):
        print(f"Current Balance: {self.__balance}")


customer = Bank("Rishit", 10000)

customer.show_balance()

customer.deposit(5000)

customer.withdraw(3000)

customer.show_balance()