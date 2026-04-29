# Exception Handling in Python

# What is exception handling?
# --> Exception handling is a mechanism to handle runtime errors in a Python program gracefully.

# Why do we need it?
# --> To prevent the program from crashing when an error occurs, allowing it to continue execution or handle the error appropriately.

# When to raise an exception and when not to?
# --> Raise an exception when you want to signal an error condition that should stop normal execution (e.g., invalid input).
# --> Do not raise unnecessarily; handle errors gracefully where possible instead of breaking the program.

# Some real-time use cases:
# --> HTTP exceptions during web requests (e.g., network errors, 404 errors).
# --> Database connection errors (e.g., connection timeouts, authentication failures).

# Example Program:
# Write a program to open a file. If the file is empty, raise an exception.
# If it is not empty, find all unique names in the file (assuming names are separated by spaces or newlines).

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if not content.strip():
                raise ValueError("The file is empty.")
            # Assuming names are words separated by spaces or newlines
            names = content.replace('\n', ' ').split()
            unique_names = set(names)
            print(f"Unique names in the file: {unique_names}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
process_file('names.txt')

######################################################################################

from loguru import logger

def final_cart_amount (*args,discount = 0.1):
    try:
        result = 0
        for amount in args:
            result = result + amount

        amount_after_discount = result - (result * discount)

        return amount_after_discount
    except TypeError:
        logger.info("Please provide the amount in integer")
        raise Exception("Value provided is not an interger coming from Type Error")
    except Exception:
        logger.info("Can not process the cart amount")
        raise 

try:
    final_amount_to_be_paid = final_cart_amount(100,200,300,400,"500",discount = 0.5)
    logger.info(f"final amount to be paid = {final_amount_to_be_paid}")
except Exception as e:
    logger.info(e)