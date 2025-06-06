# conditional expression = A one line Shortcut for the if-else statement (ternary operator)
#               Print or assign one of two values based on a condition
#               X if condition else Y

num = 5
#num = -5
age = 23
#age = 16
temperature = 20
#temperature = 19
user_role = "Admin"
#user_role = "Guest"
print("\n")

print("Positive" if num > 0 else "Negative")
print("Adult" if age >= 18 else "Child")
print("It is HOT" if temperature >= 20 else "It is COLD")
print("Full Access" if user_role == "Admin" else "Limited Access")


#Finding the greatest number among two .....
first_num = int(input("Enter the first integer number: "))
second_num = int(input("Enter the second integer number: "))

greatest = (f"The greatest number is: {first_num}" if first_num > second_num else f"The greatest number is: {second_num}")
print(greatest)


print("\n")
print("----------- Enter There different number to find the middle number ---------")
first_number = int(input("Enter the first integer number: "))
second_number = int(input("Enter the second integer number: "))
third_number = int(input("Enter the third integer number: "))

if first_number > second_number and second_number > third_number:
    print(f"The middle number is: {second_number}")
    
elif first_number < second_number and first_number > third_number:
    print(f"The middle number is: {first_number}")
    
else:
    print(f"The middle number is: {third_number}")

