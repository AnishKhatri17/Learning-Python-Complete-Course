# function = A block of reusable code place() after the function name to invoke it.

# defining a function in Python. 
# def and function_name
def happy_birthday():
    print("Happy Birthday to you 🎉!! ")
    print("Happy Birthday to you 🎉!! ")
    print("Happy Birthday Dear, Anish 🎂")
    print("Happy Birthday to you 🎉🎉🎉!!!")
    print()
    
happy_birthday()
happy_birthday()
happy_birthday()


print()
# Another Example of function in Python with Parameters now.
def function_parameters(name, position, address):
    print(f"Hey {name} how are you ?")
    print(f"You work as {position} in Sarbottam Steels.")
    print(f"{name} you are Awesome")
    print(f"Your address is {address}.")
    print()
    
function_parameters("Anish Khatri", "Laravel Developer", "Jarankhu")
function_parameters("Rustam Shrestha", "PHP Developer", "Samakhusi")
function_parameters("Unique Khanal", "Quality Assurance", "New Baneshwor")


print()
# Another Example of function in Python.
def display_Invoice(username, amount, due_date):
    print(f"Hello, {username}.")
    print(f"Your amount of Rs.{amount} is due till date: {due_date}")
    # print()
    
display_Invoice("Spongebob", 12899.45, "2082-02-29")
display_Invoice("Patrick", 8871.87, "2082-02-25")


print()
print()
print("--------- Now using return statement in functions -------------")
# Another example of function in Python that returns a value.
# return = statement used to end a function and send a result back to the caller
def addition(x, y):
    z = x + y
    return print(f"The sum of two numbers is: {z}")
    # return z

def subtraction(x, y):
    z = x - y
    return print(f"The subtraction of two numbers is: {z}")
    # return z

def multiply(x, y):
    z = x * y
    return print(f"The multiplication of two numbers is: {z:.2f}")
    # return z

def division(x, y):
    z = x / y
    return print(f"The division of two numbers is: {z:.2f}")
    # return z
    
addition(10,20)
subtraction(20, 100)
multiply(40, 40)
division(90, 29)


print()
print()
print("--------- Now using return statement in functions (Full Name) -------------")
#Another Example of Python
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print(create_name("anish", "khatri"))
print(create_name("spongebob", "squarepants"))

    
# Last example of function in Python. Asking input from the user and displaying it in the function call.....
print()
print()
def fullname():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    print(f"Your first name is: {first} and your last name is: {last}")
    
fullname()

# The basis syntax of Python is : def function_name():
# Indentation is also very important in function defination in Python.