# What is inheritance in OOP?
# What is super()?
# Multiple inheritance?
# Polymorphism?
# Implementation of all in real time?

############################################################################################################


'''
1. What is Inheritance in OOP?
--> Inheritance allows one class to acquire the properties and methods of another class.

The existing class = Parent/Base/Super class
The new class = Child/Derived/Sub class

It helps with:
--> Code reuse
--> Better organization
--> Extending functionality

Example:
'''

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print("Dog barks")

d = Dog()

d.speak()   # inherited method
d.bark()

############################################################################################################
'''
2. What is super()?
--> super() is used to call methods or constructors from the parent class.
--> Most commonly used inside __init__().

** Why use super()?
--> Avoid rewriting parent code
--> Supports multiple inheritance correctly
--> Cleaner and maintainable code

Example: 
'''

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed

d = Dog("Tommy", "Labrador")

print(d.name)
print(d.breed)

############################################################################################################
'''
3. What is Multiple Inheritance?
--> When a class inherits from more than one parent class, it is called multiple inheritance.

Example: 
'''

class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.skills()

# Python follows MRO (Method Resolution Order): It checks parents from left to right.
# You can see it using:

print(Child.mro())

############################################################################################################
'''
4. What is Polymorphism?
--> Polymorphism means: “One interface, many forms.”
--> The same method name behaves differently for different objects.

Example 1: Method Polymorphism
'''

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()

# Example 2: Operator Polymorphism

print(5 + 3)         # addition
print("Hi " + "All") # string concatenation

# Same + operator behaves differently.

############################################################################################################ 
'''
Concept	                   --> Meaning
Inheritance	               --> One class gets features of another
super()	                   --> Access parent class methods
Multiple                   --> Inheritance	Child inherits from multiple parents
Polymorphism	           --> Same method/operator behaves differently
'''
############################################################################################################

from loguru import logger

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name + "." + self.last_name + "@gmail.com"

    def print_details(self):
        return f"your first name is set as {self.first_name} and last name set as {self.last_name} with email id as {self.email}"
    

class Labour1(Person):
    def __init__(self, first_name, last_name, wage):
        super().__init__(first_name, last_name)
        self.wage = wage

    def print_details(self):
        return f"your first name is set as {self.first_name} and last name set as {self.last_name} and email id as {self.email} and total wage is {self.wage}"
    

class Mistri(Labour1):
    def __init__(self, first_name, last_name, wage, skill):
        super().__init__(first_name, last_name, wage)
        self.skill = skill

    def print_details(self):
        return f"your first name is set as {self.first_name} and last name set as {self.last_name} and email id as {self.email} and total wage is {self.wage} and skill set as {self.skill}"
    

obj_person = Person("Milan", "Pansuriya")
print(obj_person.print_details())

obj_Labour1 = Labour1("Milan", "Pansuriya", 3000)
print(obj_Labour1.print_details())

obj_Mistri = Mistri("Milan", "Pansuriya", 3000,"Python")
print(obj_Mistri.print_details())

############################################################################################################