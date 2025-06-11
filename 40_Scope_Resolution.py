# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# There is this order: First checks 1.Local and then 2.Enclosed and then 3.Global and then 4.Built-in

print("---------- Using Local Variable Example ----------")
# Local Variables
def function1():
    x = 1 # local variable of function1()
    print(x)

def function2():
    x = 2 # local variable of function2()
    print(x)

function1()
function2()
print("\n")


print("---------- Using Enclosed Variable Example ----------")
# Enclosed Variables, function declared inside a function
def functionA():
    a = 1
    
    def functionB():
        a = 10
        print(a) 
    functionB() # This prints the local variable a = 10
    
functionA()

def functionC():
    a = 1
    
    def functionD():
        # a = 10
        print(a)
    functionD() # Now, there is no local variable and uses enclosed variable a = 1 
    
functionC()
print("\n")
    
    
print("---------- Using Global Variable Example ----------")
# Global Variable (If there is no local and enclosed variables then uses the Global Variable)
def Anish():
    # fname = None
    print(fname)
    
def Khatri():
    # lname = None
    print(lname)
    
# Defining Global variable for fname and lname
fname = "Anish"
lname = "Khatri"
Anish()
Khatri()
print("\n")


print("---------- Using Built-in Variable Example ----------")
# Built-in variable (already declared and built-in like value of PI and exponent e)
from math import e
from math import pi

def imported_function():
    print(e) # This will print exponent value of e as we imported the built-in variable
    print(pi)
    
# Now declaring global variables for the same built-n variables
# NoTe: since (LEGB) global variable comes before built-in order so global variable will override it .
e = 100 

# but there is no global variable for pi so built-in variable value will be printed
imported_function() 