# 2D Collections just like in the excelsheet

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# fruits[0] = "pineapple"
# print(fruits)
print(groceries[0]) # This will print the entire collection of fruits i.e index 0
print(groceries[1]) # This will print the entire collection of vegetables i.e index 1
print(groceries[2]) # This will print the entire collection of meats i.e index 2

print()
print("Printing Fruits: ")
print(groceries[0][0]) # Targets fruits: "apple"
print(groceries[0][1]) # Targets fruits: "orange"
print(groceries[0][2]) # Targets fruits: "banana"
print(groceries[0][3]) # Targets fruits: "coconut"

print()
print("Printing Vegetables: ")
print(groceries[1][0]) # Targets vegetables: "celery"
print(groceries[1][1]) # Targets vegetables: "carrotd"
print(groceries[1][2]) # Targets vegetables: "potatoes"
# print(groceries[1][4]) # Throws out of bound error: "4"

print()
print("Printing Meats: ")
print(groceries[2][0]) # Targets meats: "chicken"
print(groceries[2][1]) # Targets meats: "fish"
print(groceries[2][2]) # Targets meats: "turkey"


# Also we can define like this, diresctly, it also works
anotherGrocery = [["apple", "orange", "banana", "coconut"],
                  ["celery", "carrots", "potatoes"],
                  ["chicken", "fish", "turkey"]]

# We can also define 2D collection in sets like this [{}]
anotherGrocery = [{"apple", "orange", "banana", "coconut"},
                  {"celery", "carrots", "potatoes"},
                  {"chicken", "fish", "turkey"}]

# We can also define 2D collection in Tuple inside a Tuple like this (())
anotherGrocery = (("apple", "orange", "banana", "coconut"),
                  ("celery", "carrots", "potatoes"),
                  ("chicken", "fish", "turkey"))
# And other format based on our requirements .....

print()
for collection in anotherGrocery:
    for food in collection:
        print(food, end=" ")
    print()  



# Number Pad or Dial Pad using 2D Collection in Python
print()
print()
print("---------- Displaying a Number Pad in a Phone ----------")
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
        