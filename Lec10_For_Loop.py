from loguru import logger

labour_name = ["Jagmohan", "Rampyare", "Mohan"]

# Method 1
for name in labour_name:
    logger.info(f"labour name is {name}")

# Method 2
# range(5)      --> 0,1,2,3,4
# range(5,11)   --> 5,6,7,8,9,10
# range(5,11,2) --> 5,7,9
for i in range(len(labour_name)):
    logger.info(f"labour {i+1} name is {labour_name[i]}")


# enumerate()
for index, name in enumerate(labour_name):
    logger.info(f"labour {index+1} name is {name}")


# Star(*) Patten printing using for loop
for i in range(1,6):
    print("* " * i)

# Print the even numbers from 1 to 100
for number in range(1,101):
    if number%2 == 0:
        print(number)
