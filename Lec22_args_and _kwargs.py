# Type of argument in python funcation?
# 1) Positional Argument
# 2) Arbitary Argument (*args, **kwargs)
# 3) Default Arguments

# What is *args?
# --> Variable-Length Arguments
# --> def sum(*cost):
# --> tuple

# What is **kwargs?
# --> Keyword Variable-Length Arguments
# --> def generic_logging(**logging)
# --> Dictionary

###############################################################################################
'''
 Types of Arguments in Python Function
 🔹 1) Positional Arguments
 --> Passed in order
 --> Order matters
 def greet(name, age):
     print(name, age)

 greet("Alice", 25)
 
 🔹 2) Default Arguments
 --> Provide a default value
 --> Optional while calling
 def greet(name, age=18):
     print(name, age)

 greet("Alice")      # age = 18
 greet("Bob", 25)

 🔹 3) Arbitrary Arguments
 👉 *args (Non-keyword variable-length arguments)
 --> Accepts multiple positional arguments
 --> Stored as a tuple
 def total(*cost):
     print(cost)

 total(10, 20, 30)

 ✔ Output: (10, 20, 30)

 👉 **kwargs (Keyword variable-length arguments)
 --> Accepts multiple keyword arguments
 --> Stored as a dictionary
 def generic_logging(**logging):
     for key,value in logging.items():
        print(f"{key} = {value}")

 generic_logging(status = "Failed", status_code = 25 , Error = "Table not found")

 ✔ Output: 
 status = "Failed"
 status_code = 25
 Error = "Table not found"
'''

###############################################################################################
# Creat a funcation to calculate the amount after discount


from loguru import logger

def final_cart_amount (*args,discount = 0.1):
    result = 0
    for amount in args:
        result = result + amount
    
    amount_after_discount = result - (result * discount)

    return amount_after_discount

final_amount_to_be_paid = final_cart_amount(100,200,300,400,500,discount = 0.5)
logger.info(f"final amount to be paid = {final_amount_to_be_paid}")

final_amount_to_be_paid = final_cart_amount(100,200,300,400,500)
logger.info(f"final amount to be paid = {final_amount_to_be_paid}")


###############################################################################################
'''
1) Write a program in which a function takes logs input from the user and writes this into a file. 
How to write into file has not been taught yet so google and try to complete it.
'''
# Method 1:
def capture_log(**kwargs):
    with open("python_logs.txt","a") as file:
        file.write(kwargs + "\n")

    print("log saved successfully!")

capture_log(status = "Done", status_code = 101, message = "Job run successfully")


# Method 2:
from datetime import datetime       # used to print the datetime

def capture_log(**kwargs):

    timestamp = datetime.now()
    log_line = ", ".join(f"{key} = {value}" for key, value in kwargs.items())
    log_line = f"{timestamp} | {log_line}"
    with open("python_logs.txt","a") as file:
        file.write(log_line  + "\n")

    print("log saved successfully!")

capture_log(status = "Done", status_code = 101, message = "Job run successfully")