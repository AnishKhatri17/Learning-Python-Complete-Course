# Python Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The addition of two number is: {round(result, 3)}")
    
elif operator == "-":
    result = num1 - num2
    print(f"The subtraction of two numbers is: {round(result, 3)}")
    
elif operator == "*":
    result = num1 * num2
    print(f"The subtraction of two numbers is: {round(result, 3)}")\

elif operator == "/":
    result = num1 / num2
    print(f"The subtraction of two numbers is: {round(result, 3)}")

else:
    print(f"The {operator} is a invalid Operator, Please check again !!!")  