# ---------------- main.py -------------------
# module = a file containing code we want to include in our program
#          use 'import' to include a module (built-in or our own)
#          useful to break up a large program reusable seperate files

pi = 3.14159

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2