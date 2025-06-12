# Multiple Inheritance = inherit from more than one parent class
#                        C(A, B)

# Multilevel Inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A


class Animal:
    
    # Okkk let's create a constructor for Grandparent class
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        

class Prey(Animal): # Parent Class, Inheriting the Grandparent Class "Animal"
    def flee(self):
        print(f"{self.name} is Fleeing.")

class Predator(Animal): # Parent Class, Inheriting the Grandparent Class "Animal"
    def hunt(self):
        print(f"{self.name} is Hunting.")


# child class 1
class Rabbit(Prey): # "Rabbit" child class is Inheritating Parent class "Prey"
    pass

# child class 2
class Hawk(Predator): # "Hawk" child class is Inheritating Parent class "Predator"
    pass

# child class 3
class Fish(Prey, Predator): # Multiple Inheritance: Fish(Prey, Predator) Inherit both Parent Class
    pass


# Making objects of the child classes
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
# rabbit.hunt() # Rabbit can't access tht hunt() method
hawk.hunt()
fish.flee()
fish.hunt()

print("\n"+"Accessing from the Grandparent Class : ")
rabbit.eat()
rabbit.sleep()
hawk.eat()
hawk.sleep()
rabbit.eat()
rabbit.sleep()
