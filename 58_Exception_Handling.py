# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except 3.finally


# These are the exceptions thay may occur based on the current code.
# 1. Dividing by 0
# 1 / 0        # ZeroDivisionError: division by zero

# 2. Type Error
# 1 + "1"        # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 3. Value Error
# int("Anish Khatri")   # ValueError: invalid literal for int() with base 10: 'Anish Khatri'
# So, fot these type of errors we need 'Exception Handling' to ensure the normal flow of the program...


# Example Program of Exception Handling
try:
    number1 = int(input("Enter a divident number to be divided: "))
    number2 = int(input("Enter a divisor number to divide: "))
    
    print(number1 / number2)
    
except ZeroDivisionError:
    print("You can't divide a number by zero IDIOT !!!!!")
    
except ValueError:
    print("Enter only number please !!")
    
except Exception:
    print("Something Went Wrong!")
    
finally:
    print("\n"+"This is a clean up code. This will execute whether exception happens or not !")
    print("So I learned the basic concept of Exception Handling in Python.")
    print("Reminder: Also I need to explore more Exception Types in Python Documentary when required")