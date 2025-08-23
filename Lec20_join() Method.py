list1 = ["apple", "banana", "cherry"]
saparate = " & "
result = saparate.join(list1)
print(result)


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
where salary > 100000'"""

filter_conditions = []
for condition in state_dept_info:
    for key,value in condition.items():
        filter_conditions.append(f'{key} = "{value}"')
print(filter_conditions)


saparate = " or "
final_filter_condition = saparate.join(filter_conditions)

final_query = Query + " and (" + final_filter_condition + ")"
print(final_query)