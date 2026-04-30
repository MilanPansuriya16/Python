
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
