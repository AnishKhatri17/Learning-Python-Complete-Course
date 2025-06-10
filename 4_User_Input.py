# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string


name = input("What is your name?: ")
age = int(input("How old are you?: "))

#Instead of below typecast we can directly typecast to the input() function which saves time and complexity ....
#age = int(age)
age = age + 1 # this will cause error because age is taken as a string so we need to typecase it to integer first

print("\n")
print(f"Hello {name}")
print("HAPPY BIRTHDAY !")
print(f"You are now {age} years old")
print("\n")


# Exercise 1: Calculate the Area of A Rectangle

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
area = length * width 

print(f"The area is :{area}cm²")


#Exercise 2: Shopping Cart Program

print("\n")
item = input("What Item would you like to buy? :")
price = float(input("What is the price? :"))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity

print("\n")
print(f"You have bought {quantity} * {item}/s")
print(f"The total amount is Rs.{total}")

# End of the Program  !!!!!!!!!!