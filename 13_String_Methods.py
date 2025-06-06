#   Different String methods in Python.

# find method finds the first occurance of a given number
# rfind method finds the reverse of a string from the ending
# capitalize returns capital Character to first index 0
# upper returns all characters to UPPERCASE
# lower returns all characters to lowercase
# isdigit() returns a boolean value "True" for all digits and otherwise "False"
# isalpha() returns a boolean value "True" if all are alphabets otherwise "False"
# count() is used to find the total number of characters specified in ""
# replace() method is used to replace a character with another in a string.

name = input("Enter your full name: ") #Anish Khatri
phone_number = input("Enter your phone number: ") #1-234-567-890

length = len(name)
find = name.find("K")
rfind = name.rfind("A")
capitalize = name.capitalize()
upper = name.upper()
lower = name.lower()
isdigit = name.isdigit() 
isalpha = name.isalpha()
phone = phone_number.count("-")
replace = phone_number.replace("-", "/")

print(length)
print(find)
print(rfind)
print(capitalize)
print(upper)
print(lower)
print(isdigit)
print(isalpha)
print(phone)
print(replace)


# validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

username = input("Enter a Username to see it's validation: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters.")
    
elif not username.find(" ") == -1:
    print("Your username can't conatin spaces.")
    
elif not username.isalpha():
    print("Your username can't contain numbers.")
    
else:
    print(f"Welcome {username}")

