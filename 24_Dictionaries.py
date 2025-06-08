# dictionary = a collection of {key:value} pairs
#              ordered and changable. No duplicates

capitals = {"USA": "Washington D.C.",
            "Nepal" : "Kathmandu",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# .get() function returns the :'value' of the key 
print(capitals.get("Nepal"))
print(capitals.get("Japan")) # This will return none because "Japan" is not a key

print()
isExist = capitals.get("Pakistan") # It doesn't exist in my current dictionary
# if capitals.get("Nepal"):
if isExist:
    print(f"The capital {isExist} exists in the dictionary")
else:
    print(f"The capital doesn't exist")
    

print()
# Using .update() method we can add new key:value pair or update the existing one.
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "New York"})

# Using .pop() method removes a key value pair from the dictionary.
capitals.pop("China")
# This way China is removed from the dictionary
print(capitals)

# popitem() removes the latest key: value pair element. It doesnot need to pass a key
capitals.popitem() # this removes "Russia":"Moscow"
print(capitals)

# capitals.clear() # this clears Everything .....

# To get all the keys, and not the values we use keys() method
keys = capitals.keys()
print()
print(keys)
for key in capitals.keys():
    print(key) 

# To get all the values, and not the keys we use values() method
print()
values = capitals.values()
print()
print(values)
for values in capitals.values():
    print(values)
    
    
print()
# items() methods returns in a format like Tuples
items = capitals.items()
print(items)

print("\n")
for key, value in capitals.items():
    print(f"{key}:{value}")