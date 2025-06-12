# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          We need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from Car_OOP_46 import Car
# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
    
# This will provide the memory address of this object where it's located    
# car1 = Car("Mustang", 2024, "red", False) 
# print(car1)

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
  
print()
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print()
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

print("\n"+"Invoking functions : ")
car1.drive()
car2.drive()
car3.drive()
car1.stop()
car2.stop()
car3.stop()
print()


car1.describe()
car2.describe()
car3.describe()

