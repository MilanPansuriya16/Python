# 1) Instance variable vs Class variable
# 2) public variable vs Private variable

'''
Instance Variable
--> Belongs to an object
--> Each object gets its own copy
--> Created using self.variable

Example: 
'''

class Student:

    def __init__(self, name):
        self.name = name      # instance variable

s1 = Student("Rahul")
s2 = Student("Amit")

print(s1.name)
print(s2.name)

##################################################################################################################3

'''
Class Variable :
--> Belongs to the class
--> Shared by all objects
--> Defined inside class but outside methods

Example:
'''

class Student:

    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Amit")

print(s1.school)
print(s2.school)


##################################################################################################################3

'''
Public Variable:
--> Accessible everywhere.

Example:
'''

class Student:

    def __init__(self):
        self.name = "Rahul"   # public variable

obj = Student()

print(obj.name)

##################################################################################################################

'''
Private Variable:
--> A private variable is created by adding double underscores (__) before the variable name
--> Accessing Private Variable Inside Class
--> Python internally changes:  __age to _Student__age

Example:
'''

class Student:

    def __init__(self):
        self.__age = 21   # private variable

obj = Student()

print(obj.__age)

##################################################################################################################

# Private variable : A private variable is created by adding double underscores (__) before the variable name
# Ex : __wage
# accessible inside the class
# not directly accessible outside the class
# but you can still access it like this: _ClassName__name
# Ex : _Labour__wage


class Labour:
    def __init__(self, first_name, last_name, wage):
        self.first = first_name
        self.last = last_name
        self.__wage = wage
    pass


labour1 = Labour("manish","kumar",200)

print(labour1.first)
print(labour1.last)
print(labour1._Labour__wage)    # To access the Private variable





