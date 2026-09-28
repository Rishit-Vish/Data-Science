"""
Question 1
Create a class with attributes and methods, then access them using the class name.
"""
class Factory:
    a = 12

    def hello():
        return "Hello, I am a method."

print(Factory.a)
print(Factory.hello())


"""
Question 2
Create a class and access its attributes and methods using an object.
"""
class Animal:
    name = "Lion"

    def speak(self):
        print("Roar!")

obj = Animal()

print(obj.name)
obj.speak()


"""
Question 3
Create a class with a constructor (__init__) and initialize object attributes.
"""
class Registration:

    def __init__(self, name, age, gender, email):
        print("Constructor called.")
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

student = Registration("Rishit", 12, "Male", "example@gmail.com")


"""
Question 4
Create a class that stores student details and displays them using a method.
"""
class Registration:

    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Email: {self.email}")


Student1 = Registration("Chavi", 23, "Female", "chh@gmail.com")
Student2 = Registration("Chaava", 18, "Male", "hao@gmail.com")

Student1.show_details()
Student2.show_details()


"""
Question 5
Create a class for Class 12 registration and allow admission only if age is 17 or above.
"""
class Class12Registration:

    def __init__(self, name, age, gender):

        if age < 17:
            print("Admission rejected. Minimum age required is 17.")
            self.valid = False

        else:
            self.name = name
            self.age = age
            self.gender = gender
            self.valid = True


    def show_details(self):

        if self.valid:
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")

        else:
            print("No details available.")


student = Class12Registration("Akash", 18, "Male")
student.show_details()


"""
Question 6
Create a class for Class 10 registration and allow admission only if age is 14 or above.
"""
class Class10Registration:

    def __init__(self, name, age, gender):

        if age < 14:
            print("Admission rejected. Minimum age required is 14.")
            self.valid = False

        else:
            self.name = name
            self.age = age
            self.gender = gender
            self.valid = True


    def show_details(self):

        if self.valid:
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")

        else:
            print("Unable to display details.")


student = Class10Registration("Hulu", 15, "Male")
student.show_details()


"""
Question 7
Demonstrate the difference between class attributes and instance attributes.
"""
class Animal:

    breed = "Dog"       # Class attribute

    def __init__(self, name):
        self.name = name   # Instance attribute


dog1 = Animal("Dogesh")

print(dog1.name)
print(dog1.breed)


"""
Question 8
Create and use a class method to access class attributes.
"""
class Robot:

    name = "Alpha1"

    def __init__(self, version):
        self.version = version


    @classmethod
    def info(cls):
        print("Robot Name:", cls.name)


obj = Robot(12.34)

obj.info()


"""
Question 9
Create and use a static method inside a class.
"""
class Robot:

    name = "Alpha1"

    def __init__(self, version):
        self.version = version


    @staticmethod
    def hello():
        print("Hello, how are you?")


obj = Robot(12.34)

obj.hello()


"""
Question 10
Create a class that generates account numbers using a class method.
"""
class BankDetails:

    @classmethod
    def generate_account_number(cls):
        return 1234


    def __init__(self, name, age, gender):

        self.name = name
        self.age = age
        self.gender = gender
        self.account_number = BankDetails.generate_account_number()


customer = BankDetails("Rishit", 20, "Male")

print(customer.name)
print(customer.account_number)