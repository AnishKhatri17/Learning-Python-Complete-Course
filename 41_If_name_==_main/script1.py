# if __name__ == "__main__" construct in Python is used to ensure that specific code is only executed when the script is run directly, and not when it is imported as a module in another script


print("\n")
# This script defines a function
def greet():
    print("Hello from script1 !")
    
# This block runs only if script1.py is executed directly
if __name__ == "__main__":
    print("script1.py is being run directly.")
    greet()
    
else:
    print("script1.py has been imported.")