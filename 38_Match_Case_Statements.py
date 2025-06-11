# Match-case statement (switch): An alternative to using many 'elif' statements
#                               Execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"   
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"  
        case 5:
            return "It is Thursday"   
        case 6:
            return "It is Friday"  
        case 7:
            return "It is Saturday"  
        case _: # case _ acts like else 
            return "Invalid day of the week"
        
print(day_of_week(1)) # Sunday
print(day_of_week(6)) # Friday
print(day_of_week(10)) # Invalid day of the week

print()
def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return "Invalid Input !!!"    
        
# taking input from the user .....
question = input("Enter the day of the week to check Weekend or Not (Sunday to Saturday): ")
print(is_weekend(question))

print("\n"+"Manually displaying weekend :")
def day_weekend(day):
    match day:
        case "Sunday" | "Monday":
            return True
        case "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print("Is Sunday a Weekend ?")
print(is_weekend("Sunday"))
        
