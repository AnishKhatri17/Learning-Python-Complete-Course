# Logical Operators = evalaute multiple conditions (or, and, not)
#                or = at least one condition must be True
#               and = both conditions must be True
#               not = inverts the condition (not False, not True)


# or operator
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is Cancelled !!")
    
else:
    print("The outdoor event is still scheduled .")
    
    
# and operator example
temperature = 35
is_sunny = True

if temperature >=28 and is_sunny:
    print("It is Hot outside 🥵")
    print("It is Sunny 🌞")
    
elif temperature <=0 and is_sunny:
    print("It is Cold outside")
    print("It is Sunny 🌞")
    
elif 28 > temperature > 0 and is_sunny:
    print("It is Warm outside")
    print("It is Sunny 🌞")
    

# not operator
elif 30 > temperature > 0 and not is_sunny:
    print("It is cloudy ☁️")
    