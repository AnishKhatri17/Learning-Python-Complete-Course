# Typecating = the process of converting a variable from one data type to another 
# str(), int(), float(), bool()

name = "Anish"
fullname = ""
age = 23
gpa = 3.45
is_student = True

# to see the type of variable we use type() function
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))
print("\n")


# typecasting in Python
age = float(age)
print(f"Age is converted to float: {age} ")
print(type(age))

fullname = bool(fullname)
print(f"Name is converted to boolean: {fullname}")
print(type(fullname))

gpa = str(gpa)
print(f"GPA is converted to string: {gpa}")
print(type(gpa))