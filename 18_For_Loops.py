# for loops = execute a block of code a fixed number of times.
#             We can iterate over a range, string, sequence, etc.

print("---------- Displaying Numbers from 1 to 10 using for loop ----------")
for x in range(1, 11): #last element i.e 11 is excluded so iterates to 10.
    print(x)
    
# Another same example of for loop .
# print("\n")
# print("---------- Displaying Numbers from 1 to 20 using for loop ----------")
# for counter in range(1, 21): #last element i.e 11 is excluded so iterates to 10.
#     print(counter)
    
    
# Reverse countdown in for loop using reversed() function
print("---------- Reversed Countdown from 10 to 1 to display Happy New Year ----------")

for x in reversed(range(1, 11)):
    print(x)

print("HAPPY NEW YEAR !")

# Third Example using sequence .....
print("\n")
for y in range(1, 6, 2):
    print(y)
    
# Fourth Example using sequence .....
print("\n")
for z in range(1, 6, 3):
    print(z)
    
# Fifth Example
print("\n")
print("----- Displaying Credit Card Info -----")
credit_card = "1234-5678-9012-3456"
for display in credit_card:
    print(display)
    

#Sixth Example using continue and break statements
print("\n")
print("----- Using continue statement -----")
for answer in range(1, 6):
    if answer == 3:
        continue
    else:
        print(answer)

print("\n")
print("----- Using break statement -----")
for answer in range(1, 6):
    if answer == 4:
        break
    else:
        print(answer)