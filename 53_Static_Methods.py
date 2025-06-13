# static methods = A method that belong to a class rather than any object from that class (instance) usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need to access to class data

class Employee:
    
    # Defining a constructor of Employee
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    # Let's create a instance method that can be accessed by class objects
    def get_info(self):
        return f"{self.name} = {self.position}"

    # Let's create a static method that accessed by Class directly
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"] 
        return position in valid_positions
    

# okay now making objects of class Employee
employee1 = Employee("Eugene", "Manager") 
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

# Accessing the static method from the class directly without making objects
print(Employee.is_valid_position("Scirntist"))   
print(Employee.is_valid_position("Boss"))
print(Employee.is_valid_position("Janitor"))

print()
print(employee1.get_info())
print(employee2.get_info())   
print(employee3.get_info())   
print(employee3.is_valid_position("Manager"))

        
        