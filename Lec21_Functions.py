
'''
I.   What is functional programming?
     - Functional programming is a programming paradigm where programs are constructed by applying and composing functions. It emphasizes the use of pure functions, immutability, and avoids changing-state and mutable data.

II.  What is modular programming?
     - Modular programming is a software design technique that emphasizes separating the functionality of a program into independent, interchangeable modules. Each module contains everything necessary to execute only one aspect of the desired functionality.

III. Why do we need functions?
     - Functions help in breaking down complex problems into smaller, manageable pieces. They promote code reuse, improve readability, and make debugging and testing easier.

IV.  How function works?
     - A function is defined once and can be called multiple times. When called, it executes the code inside its block and can return a value. Functions can accept parameters and return results.

V.   1 Programming question?
     - Example: Write a function to calculate the factorial of a number.
       ```python
       def factorial(n):
           if n == 0 or n == 1:
               return 1
           else:
               return n * factorial(n - 1) 
       print(factorial(5))  # Output: 120
       ```

'''

def calculate_fencing_coast(Length,Bradth,Cost_per_meter):
    perimeter = 2*(Length+Bradth)
    total_cost = perimeter * Cost_per_meter
    return total_cost

fensing_cost = calculate_fencing_coast(20,10,50)
print(fensing_cost)


##Problem 2
# A land of 100m x 100m has a house of 80m x 60m and a garden of 100m x 20m.
# Find the cost of fencing the remaining area at the rate of 10 Rs per meter.
# (Land Area - (House Area + Garden Area)) * Cost per meter
# Land Area = 100m x 100m
# House Area = 80m x 60m
# Garden Area = 100m x 20m
# Cost per meter = 10 Rs per meter

land_perimeter = (100*100)
Home_perimeter = (80*60)
Garden_perimeter = (100*20)
# print(land_perimeter,Home_perimeter,Garden_perimeter)

fencing_perimeter = land_perimeter - Home_perimeter - Garden_perimeter
fencing_cost = fencing_perimeter * 10

print(fencing_cost)   