# keyword argument = an argument preceded by identifier
#                    helps with readability
#                    order of arguments doesn't matter
#                    1. positional 2. default 3. KEYWORD 4. arbitary


# Example 1:
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
    
print()
hello("Hello", "Mr.", "Anish", "Khatri")
hello("Hello", "Anish", "Khatri", "Mr.") # order does matter here
hello("Hello", last="Khatri", first="Anish", title="Mr.") # using keyword arguments
# prefix any arguments with the name of the parameter like first="Anish" title="Mr."

# hello(last="Khatri", first="Anish", title="Mr.", "Hello") # SyntaxError: positional argument follows keyword argument
hello(last="Khatri", first="Anish", title="Mr.", greeting="Hello") # This works as well


# Example 2: 
for x in range(1, 11):
    print(x, end=" ") # end is keyword argument
    
print()
print("1","2","3", "4", "5", sep="-") # sep is keyword argument


# Example 3:
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="Nepal", area="+977", first="98", last="XXXXXXXX")

print(phone_num)