# What is Config file?
# Why do we need this?
# What is ini file?   -->extension
# How to read and access it?

from loguru import logger
import configparser

config = configparser.ConfigParser()

config.read(r"C:\Users\milan.pansuriya\Documents\Python\config_file.ini")

brick_cost = config["raw_materials"]["brick_cost"]

logger.info(f"{brick_cost}, type of brick_cost {type(brick_cost)}")


def total_no_of_bricks(length,breadth,height):
    no_of_bricks_in_length_side = length * (height*2)
    total_no_of_bricks_in_length_side = no_of_bricks_in_length_side * 2

    no_of_bricks_in_breadth_side = breadth * (height*2) 
    total_no_of_bricks_in_breadth_side = no_of_bricks_in_breadth_side * 2

    total_no_of_bricks = total_no_of_bricks_in_length_side + total_no_of_bricks_in_breadth_side

    return total_no_of_bricks

def total_cost_for_bricks(config):
    brick_cost = float(config["raw_materials"]["brick_cost"])
    total_no_of_bricks1 = total_no_of_bricks(15,15,10)
    final_cost = brick_cost * total_no_of_bricks1
    return final_cost


result = total_cost_for_bricks(config)

logger.info(f"Total bricks cost to make 1 room {result}")

##############################################################################################
'''
2) Pragramming Question:

A) Calculate the cost of boeks bouget by each Student

book_name   :cost

Science 	: 262
moth        : 178
History     : 59
Ph&ics      : 231
Biologa     : 165
chemistry   : 110

student_details = {1:["Math","History"],2:["Biology","Chemistry","History"],3:["Science"]}

condition: book cost detail in the ini file
'''

from loguru import logger
import configparser

config = configparser.ConfigParser()

config.read(r"C:\Users\milan.pansuriya\Documents\Python\book_config_file.ini")

# Math_Book_Cost = config["Book"]["Math"]
# print(Math_Book_Cost)

student_details = {1:["Math","History"],2:["Biology","Chemistry","History"],3:["Science"]}

student_book_cost = {}
for key,values in student_details.items():
    book_price = 0
    for i in values:
        book_price = book_price + int(config["Book"][i])
    student_book_cost[key] = book_price
    
print(student_book_cost)

##############################################################################################
'''
B) What will be the sot for books if discount 10%.
but the condition to get discount is,  you will have to buy 2 or more books.
'''


from loguru import logger
import configparser

config = configparser.ConfigParser()

config.read(r"C:\Users\milan.pansuriya\Documents\Python\book_config_file.ini")

# Math_Book_Cost = config["Book"]["Math"]
# print(Math_Book_Cost)

student_details = {1:["Math","History"],2:["Biology","Chemistry","History"],3:["Science"]}

student_book_cost = {}
for key,values in student_details.items():
    book_price = 0
    count = 0 
    for i in values:
        count += 1
        book_price = book_price + int(config["Book"][i])
    
    if count>1:
        book_price = book_price - (book_price * 0.1)
    student_book_cost[key] = book_price
    
print(student_book_cost)


# print((178 + 59)- ((178 + 59)*0.1))
# print((165 + 110 + 59)- ((165 + 110 + 59)*0.1))
# print(262)