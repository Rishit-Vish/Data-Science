"""TOPIC: POLYMORPHISM (Method Overriding & Multiple Forms)"""


"""
Question 1
Create a parent class and override its method in the child class.
"""
class Animal:

    def show(self):
        print("This is Animal class.")


class Dog(Animal):

    def show(self):
        print("This is Dog class.")


obj = Dog()

obj.show()



"""
Question 2
Create multiple classes with the same method name and call them using different objects.
"""
class Dog:

    def sound(self):
        print("Dog barks.")


class Cat:

    def sound(self):
        print("Cat meows.")


class Cow:

    def sound(self):
        print("Cow makes a sound.")


animals = [Dog(), Cat(), Cow()]


for animal in animals:
    animal.sound()



"""
Question 3
Create a function that accepts different objects and demonstrates polymorphism.
"""
class Circle:

    def area(self):
        print("Area of circle = πr²")


class Square:

    def area(self):
        print("Area of square = side × side")


def calculate_area(shape):
    shape.area()


circle = Circle()
square = Square()


calculate_area(circle)
calculate_area(square)



"""
Question 4
Demonstrate polymorphism using operator overloading.
"""
class Number:

    def __init__(self, value):
        self.value = value


    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)


print(num1 + num2)



"""
Question 5
Create a real-world example of polymorphism using payment methods.
"""
class UPI:

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class Card:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card.")


class Cash:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")


payments = [UPI(), Card(), Cash()]


for payment in payments:
    payment.pay(500)