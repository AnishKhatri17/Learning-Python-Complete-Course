# Concession Stand Program
# dictionary = {key}:{value}

menu = {"pizza": 350.00,
        "nachos": 100.50,
        "popcorn":120.00,
        "fries":90.50,
        "chips":50.00,
        "pretzel":30.50,
        "soda": 65.00,
        "lemonade": 40.25  
        }

cart = []
total = 0

print("--------- MENU -----------")
for key, value in menu.items():
    print(f"{key:10}: Rs.{value:.2f}")
    
print("-----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
print()
print()
# print(cart)
print("------------ YOUR ORDER --------------") 
print() 
for food in cart:
    total += menu.get(food)
    print(food, end="--")
    
print()
print(f"Total is: Rs.{total:.2f}")
print()
print()
