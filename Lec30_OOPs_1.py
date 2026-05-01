
'''
class
--> Class describe ojbect
--> Class is a blue print of a object
--> Class contain property(variable) and behaviours(Method)


object
--> A collection of data and associated behaviours

--> Funtion in the class is called as method


** Jargons of OOP **
1) Blue Print
2) Class
3) Object
4) Instance of a class
5) Attributes | Member | Property
6) Methods | Behaviours | Action
7) Instance Variable 
8) Class Variable
9) Encapsulation
10) Inheritance
11) Abstraction
12) Method Overloading
13) Polymorphism

'''
from loguru import logger

class User:
    def __init__(self, ip, phone_details, location = None):
        self.ip = ip
        self.phone_details = phone_details
        self.location = location

    def signup(self):
        print("signup done")
        pass

    def login(self):
        pass

    def profile_update(self):
        pass


user1 = User("10.12.23.2","9939494939","Mumbai")
print(user1)
print(user1.ip,user1.phone_details,user1.location)
print(user1.signup())