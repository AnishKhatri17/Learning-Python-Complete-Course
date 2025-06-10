# *args    = allows us to pass multiple non-key arguments
# **kwargs = allows us to pass multiple keyword-arguments
#            * unpacking operator
#            1.positional 2.default 3.keyword 4.ARBITARY

# Example 1: *args (taking any number of arguments in the function)
def add(a, b):
    return a + b

print(add(1, 3))
# print(add(1, 3, 4)) # This will throw because only 2 arguments are accepted by function
# now using *args to take multiple number of arguments

def addition(*args):
    print()
    print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total

print("The addition after using *args is : "+ str(addition(1,2,3,4,5,6,7,8,9)))

print()
def displaying(*names):
    for arg in names:
        print(arg, end=" ")

displaying("Anish", "Ashma", "Rustam", "Unique")
print()
print()


# Example 1: *args (taking any number of keyword arguments in the function)
def print_address(**kwargs):
    print(type(kwargs))
    for value in kwargs.values():
        print(value)
    
print_address(street="Gairigaun",
                  city="Kathmandu",
                  municipality="Tarkeshwor-8",
                  country="Nepal")

def print_address(**kwargs):
    print()
    for key in kwargs.keys():
        print(key)
    
print_address(street="Gairigaun",
                  city="Kathmandu",
                  municipality="Tarkeshwor-8",
                  country="Nepal")

def print_address(**kwargs):
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_address(street="Gairigaun",
                  city="Kathmandu",
                  municipality="Tarkeshwor-8",
                  country="Nepal")
print()
print()

# Example 3: *args and **kwargs using both
def shipping_label(*args, **kwargs):
    for arg in args:    
        print(arg, end=" ")
    print()
    
    if "apartment" in kwargs:
         print(f"{kwargs.get('street')} {kwargs.get('apartment')}")
         
    elif "pobox" in kwargs:
         print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
         
    else:
         print(f"{kwargs.get('street')}")
         
    print(f"{kwargs.get('country')} {kwargs.get('municipality')} {kwargs.get('district')} {kwargs.get('apartment')} {kwargs.get('tole')}") 


shipping_label("Mr.", "Anish", "Khatri",
               country="Nepal",
               municipality="Trakeshwor-8",
               district="Kathmandu",
               street="Gairigaun, Shivamandir",
               apartment="#1040",
               tole= "Pragati Tole")
