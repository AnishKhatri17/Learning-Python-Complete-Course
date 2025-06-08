# collection = single "variable" used to store multiple values
# List = [] ordered and changable. Duplicates OK
# Set = {} ordered and immutable, but Add/Remove OK. No dubplicates
# Tuple = () ordered and unchangable. Duplicates OK. FASTER


# ----- Using Lists ----- 
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits) # This is display all the elements
print(fruits[0]) # This is display the first element in the List
print(fruits[1]) # This is display the second element in the List
print(fruits[2]) # This is display the third element in the List
print(fruits[3]) # This is display the fourth element in the List
# print(fruits[4]) # This will throw error: IndexError: List index out of range

print(fruits[0:3]) # This will print the first three elements
print(fruits[:3]) # This will print the first three elements
print(fruits[::2])# This will print every second element
print(fruits[::3])# This will print every third element
print(fruits[::-1]) #This will print backwards or in reversed order

print()
print("Using for loop:")
for fruit in fruits:
    print(fruit)
    
# print(dir(fruits))
# print(help(fruits))

print(len(fruits)) # len() function returns the length of the list
print("apple" in fruits) # This will return a boolean "True" if found otherwise "False"
print("pineapple" in fruits) 

# fruits.append("pineapple")
# fruits.remove("banana")
# fruits.insert(0, "mango")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# fruits.index("coconot") # found in index 3
# fruits.count("banana")

fruits[0] = "pineapple" # changing the element of the list
for fruit in fruits:
    print(fruit)


print()
# ----- Using Sets ----- 
fruitsSet = {"apple", "orange", "banana", "coconut"}

print(fruitsSet) # This is displayed in unordered way...
# print(dir(fruitsSet))
# print(help(fruitSet))

print(len(fruitsSet))
print("banana" in fruitsSet)
# print(fruitsSet[0]) #This will throw an error because it is in unordered

# We cannot edit the elements in "Set" {} but we can add/remove elements
fruitsSet.add("Pineapple") # This will add "pineapple" in the set
print(fruitsSet)

fruitsSet.remove("banana") # This will remove "banana" in the set
print(fruitsSet)

fruitsSet.pop() # This will remove the first element but it will be random because it is in inordered form
print(fruitsSet)

# fruitsSet.clear() This will remove all the elements in the set
# print(fruitsSet)


print()
# ----- Using Tuple -----
fruitsTuple = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruitsTuple))
# print(help(fruitsTuple))
print(len(fruitsTuple))
print("pineapple" in fruitsTuple)

# There are two methods we have access to in Tuple
print(fruitsTuple.index("apple"))
print(fruitsTuple.count("coconut"))

# Lets use for loop to iterate all in the Tuple
for fruit in fruitsTuple:
    print(fruit, end=", ")