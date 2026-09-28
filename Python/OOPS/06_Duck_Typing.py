"""TOPIC: DUCK TYPING"""


"""
Duck Typing means Python focuses on what an object can do,
rather than what class it belongs to.

If an object has the required method, it can be used.
"""


class Animal:

    def show(self):
        print("This is Animal class.")


class Dog:

    def show(self):
        print("This is Dog class.")


obj = Animal()
obj.show()

obj = Dog()
obj.show()



"""
Example 2:
Different classes can have the same behavior without inheritance.
"""

class Employee:

    def __init__(self, name):
        self.name = name


    def show_details(self):
        print(f"Employee Name: {self.name}")


class Developer(Employee):

    def __init__(self, name, programming):
        super().__init__(name)
        self.programming = programming


    def show_details(self):
        print(f"Developer: {self.name}, Language: {self.programming}")


class Manager(Employee):

    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size


    def show_details(self):
        print(f"Manager: {self.name}, Team Size: {self.team_size}")


def display_details(employee):
    employee.show_details()


developer = Developer("Deepak", "Python")
manager = Manager("Akash", 23)


display_details(developer)
display_details(manager)