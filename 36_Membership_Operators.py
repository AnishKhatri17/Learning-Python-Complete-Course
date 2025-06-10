# Membership Operators = used to test whether a value or variables is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in

# Example 1: string
word = "APPLE"
letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")

else:
    print(f"{letter} was not found")
    
# if letter in word:
#      print(f"{letter} was not found")

# else:
#     print(f"There is a {letter}")


# Example 2: sets 
print("\n")
students = {"Anish", "Sarad", "Raman", "Archana", "Junel", "Kiran"}
student = input("Enter the name of the student in SMC BCA 8th sem : ")  

if student not in students:
    print(f"{student} is not found in !")
    
else:
    print(f"{student} is a student of BCA 8th semester.") 
    
    
# Example 3: Dictionaries
print("\n")
# dictionary with "key: value"
people = {"Anish":"A+",
          "Archana": "A",
          "Sarad": "B+",
          "Sushil": "B",
          "Shirish": "C"
          }

info = input("Enter the name of the student: ")

if info in people:
    print(f"{info}'s grade is {people[info]}")
    
else:
    print(f"{info} was not found")
    
    
# Example 4
print("\n")
# email = "anish@gmail.com"
email = input("Enter your email address: ")

if "@" in email and "." in email:
    print(f"Yes, your {email} is valid.")
    
elif "@" not in email:
    print(f"No, your {email} is invalid it does not contain '@'")
    
elif "." not in email:
    print(f"No, your {email} is invalid it does not contain '.'")

else:
    print(f"No, the {email} you entered is invalid")    
