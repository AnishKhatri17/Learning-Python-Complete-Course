# if = Do some code only IF some condition is True
#      Else do something else

 #Exercise 1: To check whether a person is eligible to vote or not (min age should be 18)
 
# age = input("")
print("\nTo check whether you are eligible to vote or not.")
age = int(input("Enter your age: "))

if age > 100:
    print("You are too old to vote, sorry you can't.")
 
elif age >=18 :
    print("You are eligible to vote.")

elif age <18 :
    print("You are not eligible to vote.")

elif age < 0:
    print("You have've been born yet, lol how can you vote !?")

else:
    print("Sorry, wrong input")
    

#Exercise 2: To check yes no from user...
print("\n")
response = input("Would you like some food if you're hungry? (y/n): ")

if response == "y":
    print("Okay, Have some food..")

elif response == "Y":
     print("Okay, Have some food..")
     
elif response == "n" :
    print("No food for you !!")

elif response == "N" :
    print("No food for you !!")
    
else :
    print("Wrong Input !!!")
    
    
#Exercise 3: To print your name in if statement
print("\n")
name = input("Enter your name: ")

if name =="":
    print("!!! You cannot leave your name Blank !!!")
    
else:
    print(f"Hello {name}")
    
    
# Exercise 4: using boolean in if statement
for_sale = True

print("\n")
if for_sale:
    print("Yes, this is for sale HURRY UP !!!")

else :
    print("No, this is NOT for sale anymore !!!")
    

print("\n")
is_online = False
if is_online:
    print("You are online !")

else:
    print("You are offline !")
