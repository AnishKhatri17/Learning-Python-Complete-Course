# class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

class Student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
    # Creating a Instanace Method
    def get_info(self):
        return f"{self.name} = {self.gpa}"
    
    # Creating a class method
    @classmethod
    def get_count(cls):
        return f"The total number of students is: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
    
# Creating Student class objects
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

# Printing the class method total count ...
print(Student.get_count())
print(Student.get_average_gpa())