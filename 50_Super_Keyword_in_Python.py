# super() = Function used in a child class to call methods from a parent class(superclass).
#           Allows us to extend the functionality of the inherited methods


class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
        

class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        # self.color = color 
        # self.is_filled = is_filled
        # Replacing the above two lines of code by inheriting parent class function using super()
        super().__init__(color, is_filled)
        self.radius = radius
        
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        # This is overriding the Parent Class 'describe' function
        super().describe() # super() uses the parent class function
  
        
class Square(Shapes):
      def __init__(self, color, is_filled, width):
        # self.color = color
        # self.is_filled = is_filled
        # Replacing the above two lines of code by inheriting parent class function using super()
        super().__init__(color, is_filled)
        self.width = width
        
      def describe(self):
            print(f"It is a square with an area of {self.width * self.width}cm^2")
            # This is overriding the Parent Class 'describe' function
            super().describe() # super() uses the parent class function
        
class Triangle(Shapes):
      def __init__(self, color, is_filled, width, height):
        # self.color = color
        # self.is_filled = is_filled
        # Replacing the above two lines of code by inheriting parent class function using super()
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
      def describe(self):
            print(f"It is a square with an area of {self.width * self.height / 2 }cm^2")
            # This is overriding the Parent Class 'describe' function
            super().describe() # super() uses the parent class function
        

# color, is_filled properties are common in the above classes so we make a parent class and reuse the function uaing super()

# Now creating object of the child classes
circle = Circle(color="red", is_filled= True, radius=5) # Keyword Arguments not necessary but good for readability
square = Square(color="blue", is_filled= False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
print()
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
print()
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

print("\n")
print("Using the Describe Function: ")
circle.describe()
print()
square.describe()
print()
triangle.describe()