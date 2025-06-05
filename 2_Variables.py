# A container for a value (string, integer, float, boolean) 
# A variable behaves as if it was the value it contains

# string
first_name = "Anish"
last_name = "Khatri"
email = "anish@example.com"

print(first_name)
print(last_name)
#using f-string, it is the easiest way to display a variable...
print(f"Your first name is : {first_name} ")
print(f"Your last name is: {last_name}")
print(f"Your email is: {email}")


# integer 
age = 25
runs = 86
num_of_crowds = 22190
print(f"Your age is {age} years old")
print(f"You have scored {runs} runs in the cricket match")
print(f"You scored {runs} runs in front of {num_of_crowds} number of crowds.")


# float
price = 75000.54
gpa = 3.45
distance = 4.3
print(f"The price of your cricket bat is Rs.{price}")
print(f"The GPA you scored in BCA 2nd Semester is: {gpa}")
print(f"The distance you travel to reach your Campus is {distance} kilometers")


# boolean
is_student = True
is_sale = False
is_online = False

if is_student:
    print("Yes, you are a Student.")
else :
    print("No, you are not a student")
    

if is_sale:
    print("The product is on sale, Hurry Up !!!!")
else :
    print("The product is not in sale !!!!")
    
if is_online:
    print("Yes, you are Online !")
else :
    print("No, you are not online")
    
    
# calculating simple interest
SI = None
principle = 1200
rate = 9.23
time = 4.3

print("\n\n"+"-------------------- Calculating Simple Interest-----------------------")
SI = (principle * rate * time) / 100
print(f"The simple interest is : {SI}")

