length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

print("length of land is ", length_of_land)
print("breadth of land is ", breadth_of_land)
print("bricks cost per piece is ", bricks_cost_per_piece)
print("labour mistri 1 is ", labour_mistri1)
print("labour mistri 2 is ", labour_mistri2)
print("is home is ", is_home)

print("My home is of 4 BHK \nLength of the total land is 100")   #\n is used for new line, it is called escape sequence
print('''My home is of 4 BHK
Length of the total land is 100''') #Triple quotes are used for multi line string
print("My home is of \"4 BHK\" Flat") #\ is used to escape the special character, in this case it is used to print double quotes inside a string.


#String Formatting
# 1) F String
# 2) .format() method

# F String
print(f"cost of bricks per unit is {bricks_cost_per_piece} and labour mistri 1 is {labour_mistri1} and labour mistri 2 is {labour_mistri2}")

# .format() method
print("cost of bricks per unit is {} and labour mistri 1 is {} and labour mistri 2 is {}".format(bricks_cost_per_piece,labour_mistri1,labour_mistri2))


#logging
from loguru import logger

logger.info(f"coast of bricks per unit is {bricks_cost_per_piece}")