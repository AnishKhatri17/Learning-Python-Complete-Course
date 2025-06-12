# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow us to share data among all objects created from that class

class Student:
    
    # Now I am defining class variables
    graduated_year = 2025
    num_of_students = 0
    
    # Constructor of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1
        
        
# Making objects of the class
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 50)
student4 = Student("Sandy", 24)

# Printing the attribute of the class object.
print(student1.name)
print(student1.age)
print(student1.graduated_year) # Class object also access the class variable but we should use Class name for accessing class variables...
print(Student.graduated_year) # We should use 'classname'.'class_varaible_name' for more specific rather than class_object.class_variable
print()

print("This is to print the class variables : ")
print(f"My graduating year {Student.graduated_year} has total of {Student.num_of_students} students."+" They are:")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)