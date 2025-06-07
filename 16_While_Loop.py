# while loop = execute some code WHILE some condition remains true

# By using if else statement
# name = input("Enter your name: ")
# if name == "":
#     print("You did not enter your name. ")

# else:
#     print(f"Your name is {name}")


#using while loop, Example 1:
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name, you leave it blank !!!")
    name = input("Enter your name: ")
    
print(f"Your name is: {name}")
print("\n")


#using while loop, Example 2:
age = int(input('Enter your age: '))
while age < 0:
    print("Age can't be Negative !!! ")
    age = input('Enter your age: ')
    
print(f"Okay, you are {age} years old")
print("\n")
    
    
#using while loop, Example 3:
food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
    
print("Okay bye, thank you for telling your favourite foods !")


#using while loop, Example 4:
num = int(input("Enter a number between (1 -10): "))
while num < 1 or num > 10:
    print(f"{num} is not valid !!!")
    num = int(input("Enter a number between (1 -10): "))

print(f"Your entered number {num} is valid ")
    