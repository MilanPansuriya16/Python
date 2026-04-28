# Waht is Join method?
# How it works?
# Real Time usage of join method?

# The .join() method in Python is used to combine (concatenate) elements of an iterable (like a list or tuple) into a single string, using a specified separator.
# All elements must be strings, otherwise you'll get an error.

from loguru import logger

# Example of join method with a list of strings
lst_of_strings = ["Hello", "World", "Python", "Programming"]
result = " ".join(lst_of_strings) # it will join all the elements of the list with a space in between
print(result)

list1 = ["apple", "banana", "cherry"]
saparate = " & "
result = saparate.join(list1)
print(result)

# Example of join method with a tuple of strings
labour_with_cost = {"Mahesh":500, "Ramesh":400, "Mithilesh":400, "Sumesh":300}
result = " # ".join(labour_with_cost) # it will join all the keys of the dictionary with a " # " in between
print(result)

##################################################################################################################################################


# Question 1
# You have two table employee_tbl and department
# employee_tbl have emp_id, employee_name, state, zip, salary
# department have emp_id, department
# You have to write a query to find out all the employee name, state, zip, salary, department
# whose salary is greater than 100000 and state is either Bihar or Delhi and department is either IT or Marketing.
# You have to write a dynamic query because the filter condition can change in each run.

state_dept_info = [
    {"state": "Bihar", "department": "IT"},
    {"state": "Delhi", "department": "Marketing"}
]

# Find out all the employee name who are available in the above condition.
# You don't know the exact number of filter condition which will come in the above list.
# It can change in each run.

Query = """select * from (
    select e.employee_name, e.state, e.zip, e.salary, d.department
    from employee_tbl e
    inner join department d
    ON e.emp_id = d.emp_id
)a
where salary > 100000"""

filter_condition = []

for condition in state_dept_info:
	for key,value in condition.items():
		filter_condition.append(f"{key} = '{value}'")

# print (filter_condition)

result = " or ".join(filter_condition)

# print(result)
final_query = Query + " and (" + result + ")"
print(final_query)