# List Comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# tarditional loop to print
print("----- Traditional Loop -----")
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
    
print(doubles)
print("\n")

# List Comprehension
print("----- List Comprehension -----")
# Double = [expression for value in iterable if condition]
list = [x * 2 for x in range(1, 11)] 
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(list)
print(triples)
print(squares)
print("\n")


# List Comprehension
print("----- Second Example using Expression -----")
fruits = ["apple", "orange", "banana", "mango", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits] # jsut prints the first character of each from the list
fruits = [fruit.upper() for fruit in fruits]

# we can also do this
# fruits = [fruit.upper for fruit in ["apple", "orange", "banana", "mango", "coconut"]]

print(fruit_chars)
print(fruits)
print("\n")


# List Comprehension
print("----- Third Example using If Condition -----")
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

print("Positive numbers are: "+str(positive_nums))
print("Negative numbers are: "+str(negative_nums))
print("Even numbers are: "+str(even_nums))
print("Odd numbers are: "+str(odd_nums))
print("\n")


# List Comprehension
print("----- Third Example using If Condition -----")
grades = [85, 42, 79, 56, 90, 30, 61, 35, 67, 24, 100, 37]
passing_grades = [grade for grade in grades if grade >= 35 ]
failed_grades = [grade for grade in grades if grade < 35]

print(f"The passed grades are: {passing_grades}")
print(f"The failed grades are: {failed_grades}")


