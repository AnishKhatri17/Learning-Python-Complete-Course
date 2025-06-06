
# Arithmetic operators in Python 
friends = 10

#friends = friends + 1
friends += 1
#friends = friends - 2
friends -= 2
#friends = friends * 3
friends *= 3
#friends = friends / 2
#friends /= friends
#friends = friends ** 2
friends **= 2

remainder = friends % 2

print(friends)
print(remainder)


# ------ Another Example---- 
# Math related functions

x = 3.14
y = 4
z = 5
absolute = -4

#Different Math functions 
result = round(x)
power = pow(4, 3)
maximum = max(x, y, z)
minimum = min(x, y, z)
absoluteValue = abs(absolute)

print("\n")
print("Different Math Functions in Python")
print(result)
print(absoluteValue)
print(maximum)
print(minimum)
print(power)


print("\n")
print("Another Example of Math Functions in Python")
import math


x = 9
y = 9.1
z = 9.9
print(math.pi)
print(math.e)
result = math.sqrt(x)
ceilFunction = math.ceil(y) # 9.1 is rounded up to 10
floorFunction = math.floor(z) # 9.9 is now 9 using floor()

print(result)
print(ceilFunction)
print(floorFunction)

# Exercise 1
print("\n")
print("Exerice to calculate circumference of a circle in Python")

radius = float(input("Enter the radius of a Circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference of a circle is: {round(circumference, 2)}cm")

# Exercise 2
print("\n")
print("Exerice to calculate Area of a circle in Python")
rad = float(input("Enter the Radius of a circle: "))
area = math.pi * pow(rad, 2)
print(f"The area of a circle is: {round(area, 2)} cm^2")

print("\n")
print("Exerice to calculate hypotenuse of a right angle triangle in Python")

# Exercise 3
a = float(input("Enter the perpendicular of the right angle triangle: "))
b = float(input("Enter the base of the right angle triangle: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of the right angle triangle is : {round(c, 2)}")
