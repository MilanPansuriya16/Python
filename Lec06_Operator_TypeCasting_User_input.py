
from loguru import logger

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

# calculate the total area of of the land

total_area_of_land = length_of_land * breadth_of_land
logger.info(f"Total area of my land is {total_area_of_land} sq ft")

# calculate the perimeter of the land

perimeter_of_land = 2 * (length_of_land + breadth_of_land)
logger.info(f"Perimeter of my land is {perimeter_of_land} ft")


# module operator used in armstrong number program
number1 = 15%4
print(number1)

# Division
print(15/6) # it will give the result in float
print(15//6) # it will give the result in integer but floor value of the result

import math
print(math.floor(15/6)) # it will give the result in integer but floor value of the result
print(math.ceil(15/6)) # it will give the result in integer but ceil value of the result



########################################################################################################33

# Type Casting

a = "10"
b = "34"
print(a+b) # it will concatenate the two strings and give the result as 1034


# to convert the string into integer we can use int() function
a1 = int(a)
b1 = int(b)
print(a1+b1) # it will add the two integers and give the result as 44


c = str(a1) # it will convert the integer into string
print(b + c) # it will concatenate the two strings and give the result as 3410

# Two type of type casting
# 1) Implicit type casting
# 2) Explicit type casting

a2 = 10.3
b2 = 5
print(a2 + b2) # it will give the result in float because of implicit type casting
#python will automatically convert the integer into float and then perform the addition operation


########################################################################################################
# User Input

length_of_land = float(input("Please enter the length of your land: "))
breadth_of_land = float(input("Please enter the breadth of yourland: "))
total_area_of_your_land = int(length_of_land) * int(breadth_of_land)
logger.info(f"Total area of my land is {total_area_of_your_land} sq ft")

#When we used input function to take the input from the user, it will take the input as a string. So we need to convert the string into the required data type using type casting. In this case we have converted the string into float and then into integer to perform the multiplication operation.
