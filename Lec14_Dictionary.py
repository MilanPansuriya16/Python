# How to create a dictionary?
# Hwo to update dictionary?
# How to iterate dictionary?


from loguru import logger

labour_with_cost = {"Mahesh":500, "Ramesh":400, "Mithilesh":400, "Sumesh":300}

# Update the dictionary # if key is not present then it will add the key and value in the dictionary
labour_with_cost["Jagmohan"] = 1000
labour_with_cost["Mahesh"] = 800

logger.info(labour_with_cost)

# Funcation

logger.info(labour_with_cost.keys())
logger.info(labour_with_cost.values())
logger.info(labour_with_cost.items())

# Iterating the dictionary
# By default it will pass the key of the dictionary in the loop
for i in labour_with_cost:
    logger.info(i) # it will print the key of the dictionary

# If we want to print the value of the dictionary then we can use the key to get the value
for i in labour_with_cost:
    logger.info(labour_with_cost[i]) # it will print the value of the dictionary

# If we want to print the key and value of the dictionary then we can use the items() function to get the key and value of the dictionary
for key, value in labour_with_cost.items():
    logger.info(f"{key} : {value}")

# Method 2 to iterate the dictionary
for name in labour_with_cost:
    logger.info(f"{name}: {labour_with_cost[name]}")

##############################################################################################################################

# Calculate the total labour cost if total working days were 50
# Mahesh was absent for 3 days and Jagmohan was absent for 7 days
# Find the total labour cost
	
labour_with_cost = {"Mahesh":500, "Ramesh":400, "Mithilesh":400, "Sumesh":300, "Jagmohan":1000,"Rampyare":800}

total_labour_cost = 0
working_days = 50
Mahesh_absent_days = 3
Jagmohan_absent_days = 7

for name in labour_with_cost:
	if name == "Mahesh":
		total_labour_cost = total_labour_cost + (labour_with_cost[name] * (working_days - Mahesh_absent_days))
	elif name == "Jagmohan":
		total_labour_cost = total_labour_cost + (labour_with_cost[name] * (working_days - Jagmohan_absent_days))
	else:
		total_labour_cost = total_labour_cost + (labour_with_cost[name] * working_days)
		
print(total_labour_cost)

# print(500*47 + 400*50 + 400*50 + 300*50 + 1000*43 + 800*50)