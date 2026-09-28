"""TOPIC: SINGLE LEVEL INHERITANCE"""


"""
Question 1
Create a parent class and inherit its attributes and methods into a child class.
"""
class A:

    xyz = "Hello"

    def greet(self):
        print("Hello, how are you?")


class B(A):
    pass


obj = B()

obj.greet()
print(obj.xyz)


"""
Question 2
Create a company class and inherit its features into another class.
"""
class Reebok:

    def show(self):
        print("This is Reebok company.")

    def bag(self):
        print("Reebok manufactures bags.")


class Bata(Reebok):

    def show2(self):
        print("This is Bata class inherited from Reebok.")


person = Bata()

person.show()
person.bag()
person.show2()



"""TOPIC: MULTIPLE INHERITANCE"""


"""
Question 3
Create a child class that inherits properties from two parent classes.
"""
class Father:

    def show1(self):
        print("This is Father class.")


class Mother:

    def show2(self):
        print("This is Mother class.")


class Child(Father, Mother):

    def show3(self):
        print("This is Child class.")


obj = Child()

obj.show1()
obj.show2()
obj.show3()



"""
Question 4
Create a factory class and inherit it into another class using super().
"""
class Factory:

    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity


    def show(self):
        print(f"Location: {self.location}")
        print(f"Capacity: {self.capacity}")


class Reebok(Factory):

    def __init__(self, location, capacity, brand_name):
        super().__init__(location, capacity)
        self.brand_name = brand_name


    def show2(self):
        print(f"Brand Name: {self.brand_name}")


obj = Reebok("Mumbai", 20.5, "Reebok")

obj.show()
obj.show2()



"""TOPIC: MULTILEVEL INHERITANCE"""


"""
Question 5
Create a multilevel inheritance structure where a child inherits from a parent class.
"""
class A:

    def show(self):
        print("This is A class.")


class B(A):

    def show2(self):
        print("This is B class.")


class C(B):
    pass


obj = C()

obj.show()
obj.show2()



"""
Question 6
Demonstrate constructor overriding in multilevel inheritance.
"""
class A:

    def __init__(self):
        print("This is Parent class constructor.")


class B(A):

    def __init__(self):
        print("This is B class constructor.")


class C(B):

    def __init__(self):
        B.__init__(self)
        A.__init__(self)


obj = C()



"""TOPIC: HIERARCHICAL INHERITANCE"""


"""
Question 7
Create multiple child classes that inherit from the same parent class.
"""
class A:

    def show(self):
        print("This is A class.")


class B(A):

    def show2(self):
        print("This is B class.")


class C(A):

    def show3(self):
        print("This is C class.")


obj = C()

obj.show()
obj.show3()



"""
Question 8
Create different product classes inheriting common factory details.
"""
class Factory:

    def __init__(self, name, location):
        self.name = name
        self.location = location


    def show(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")


class Shoe(Factory):

    def __init__(self, name, location, shoe_size):
        super().__init__(name, location)
        self.shoe_size = shoe_size


    def show2(self):
        print(f"Shoe Size: {self.shoe_size}")


class Tshirt(Factory):

    def __init__(self, name, location, color):
        super().__init__(name, location)
        self.color = color


    def show3(self):
        print(f"T-Shirt Color: {self.color}")


obj = Tshirt("Shaktiman", "Pune", "Black")

obj.show()
obj.show3()


obj2 = Shoe("Superman", "Bhopal", 8)

obj2.show()
obj2.show2()



"""TOPIC: HYBRID INHERITANCE"""


"""
Question 9
Create a hybrid inheritance structure using multiple and hierarchical inheritance.
"""
class Factory:

    def show(self):
        print("This is Factory class.")


class Shoe(Factory):

    def show2(self):
        print("This is Shoe class.")


class Tshirt(Factory):

    def show3(self):
        print("This is T-Shirt class.")


class Store(Shoe, Tshirt):

    def display(self):
        print("This is Store class.")


obj = Store()

obj.show()
obj.show2()
obj.show3()
obj.display()
