from loguru import logger
import time

labour_name = ["Jagmohan", "Rampyare", "Mohan"]

name_iter = len(labour_name) - 1 
while (name_iter >= 0):
    print(labour_name[name_iter])
    time.sleep(2)
    name_iter = name_iter - 1


# Calculator using while loop

num1 = input("Enter the number")
oper = input("Enter the operator (+, -, *, /): ")
result = num1

while (oper != "="):

    num2 = input("Enter the next number")

    if oper == "+":
        result = int(num1) + int(num2)
    elif oper == "-":
        result = int(num1) - int(num2)
    elif oper == "*":
        result = int(num1) * int(num2)
    elif oper == "/":
        result = int(num1) / int(num2)

    num1 = result

    oper = input("Enter the operator (+, -, *, /, =): ")

print(f"The answer is {result}")