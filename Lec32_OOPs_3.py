# Class Method 
# Static Method
# How to implement the class and static method in real world?


############################################################################################################

'''
Class Method : 
--> A class method works with the class itself, not with individual objects.
--> Uses: @classmethod
--> and first parameter is: cls (cls means class)

Example of Class Method:
'''

class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

# Accessing Class Method: Using Class

Student.show_school()

'''
Why Use Class Method?

Because it works with:
--> class variables
--> class-level operations
--> not object-specific data.
'''

############################################################################################################

'''
Static Method:
--> A static method is just a normal function placed inside a class.
--> It behaves like a normal function.

It:
--> does NOT use self
--> does NOT use cls

Uses decorator: @staticmethod

Example of Static Method
'''

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
    

# Accessing Static Method: Using Class

print(Calculator.add(10, 20))

# Using Object: 

obj = Calculator()
print(obj.add(5, 6))

############################################################################################################


