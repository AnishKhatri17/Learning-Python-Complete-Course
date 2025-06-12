# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    
    # Constructor of the Parent Class 'Animal'
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"This {self.name} is eating.")
        
    def sleep(self):
        print(f"This {self.name} is sleeping.")
        

# Example of Inheritance. Making child class and inheriting from the Parent Class Properties
class Dog(Animal):
    # A child class can have their own functions and attributes as well
    def speak(self):
        print(f"{self.name}'s sound is Whoof!")
        
    def dog_function(self):
        print("This is Dog's Function other class can't access this !")


class Cat(Animal):
    # A child class can have their own functions and attributes as well
    def speak(self):
        print(f"{self.name}'s sound is Meow!")


class Mouse(Animal):
    # A child class can have their own functions and attributes as well
    def speak(self):
        print(f"{self.name}'s sound is Squeeel!")
 
 
# Making objects of this Class Animal.
dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")


# printing the name and informations
print(dog.name)
dog.eat()    # eat() method is inheritated from Parent Class
dog.sleep()  # sleep() method is inheritated from Parent Class

print()
print(cat.name)
cat.eat() # eat() method is inheritated from Parent Class
cat.sleep() # sleep() method is inheritated from Parent Class

print()
print(mouse.name)
mouse.eat() # eat() method is inheritated from Parent Class
mouse.sleep() # sleep() method is inheritated from Parent Class

print("\n"+"Now, Printing child class own functions and properties: ")
dog.speak()
cat.speak()
mouse.speak()

# Now accessing the Dog Class own function with its object
print()
dog.dog_function()
# mouse.dog_function() # This will throw error as Mouse Class object can't access Dog Class function