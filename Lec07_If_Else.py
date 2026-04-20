
from loguru import logger

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

length_of_land = int(input("Enter the length of the land: "))

if(length_of_land < 100):
    logger.info(f"Your length is not sufficient to build a 4 BHK home")
elif(length_of_land > 500):
    logger.info(f"You can build more than 2 buildings")
else:
    logger.info(f"Share more details with us")


##################################################################################################

# How to find the number is even or odd

number = int(input("Enter a number: "))
if(number % 2 == 0):
    logger.info(f"{number} is an even number")
else:
    logger.info(f"{number} is an odd number")   
