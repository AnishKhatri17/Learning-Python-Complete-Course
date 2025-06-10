# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over a loop

#Example 1: lists
numbers = [1, 2, 3, 4, 5]
print("----- Using Lists -----")
for number in numbers:
    print(number, end=" ")
    
print()

#Example 2: Tuple
numbers = (1, 2, 3, 4, 5)
print()
print("----- Using Tuples -----")
for number in numbers:
    print(number, end="-")
    
print()
print("Now, printing in reversed order")
for number in reversed(numbers):
    print(number, end="-")

#Example 3: Sets
numbers = {1, 2, 3, 4, 5}
print("\n"+"\n")
print("----- Using Sets -----")
for number in numbers:
    print(number, end=" - ")
    
print("\n"+"\n")
fruits = {"apple", "banana", "orange", "coconut", "mango"}
for fruit in fruits:
    print(fruit)

print("\n"+"\n")
# Note: Sets can't be printed in reversed order !!!

# Example 4: strings 
name = "anish khatri"
print("----- Using Characters -----")
for character in name:
    print(character, end = " ")
    
print()
print("Now, printing in reversed order")
for character in reversed(name):
    print(character, end= " ")
print("\n"+"\n")


# Example 5: working with dictionaries
my_dictionary = {"A":1, "B":2, "C":3}
print("This will print only the key ")
for test in my_dictionary:
    print(test, end =" ")
print()
for key in my_dictionary.keys():
    print(key, end="")    
    
print("\n"+"\n"+"This will print the value ")
for value in my_dictionary.values():
    print(value)
    
print("\n"+"\n"+"This will print the both key and value ")
for key, value in my_dictionary.items():
    print(f"{key}: {value}")

print()