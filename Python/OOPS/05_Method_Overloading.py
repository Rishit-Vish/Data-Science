"""TOPIC: METHOD OVERLOADING (Not Directly Supported in Python)"""


"""
Question 1
Demonstrate why Python does not support traditional method overloading.
"""
class Animal:

    def show(self):
        print("This is animal class.")


    def show(self, name):
        print(f"Animal name is {name}")


obj = Animal()

# First show() method gets overwritten by the second show()
obj.show("Lion")



"""
Question 2
Demonstrate method overriding along with method replacement.
"""
class Animal:

    def show(self):
        print("This is Animal class.")


class Dog(Animal):

    def show(self):
        print("This is Dog class.")


obj = Dog()

obj.show()



