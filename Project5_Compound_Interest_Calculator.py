# python compound interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount can't be less than or equal to zero.")
        
while rate <= 0:
    rate = float(input("Enter the Interest Rate: "))
    if rate <= 0:
        print("Interest Rate can't be less than or equal to zero.")
        
while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero.")
        
# print(principal)
# print(rate)
# print(time)

#formula to calculate compound interest
total = principal * pow((1 + rate), time)
print(f"Balance after {time} year/s: Rs {total:.2f}")


#Another example for self learning 
print("\n"+"Another Example for Self Learning.")
num = 0

while True:
    num = int(input("Enter a non zero number: "))
    if num == 0:
        print("You can enter a zero !!! Please try again ")
        num = int(input("Enter a non zero number: "))
    else:
        print(f"Okay you entered {num}, which is valid.")
        break
    #here break keyword is very important to exit the infinite while loop