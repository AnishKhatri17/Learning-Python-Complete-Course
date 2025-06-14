# Magic Methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behaviour of objects

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self): # dunder string method to print the string message
        return f"'{self.title}' by {self.author}"
         
    def __eq__(self, other): # __eq__ means equals to compare two objects
        return self.title == other.title and self.author == other.author
         
    def __lt__(self, other): # __lt__ means less than to comapre two objects
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other): # __add__ is for addition of two objects
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword): # __contains__ searching for a keyword in object
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"The '{key}' was not found !"

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 171)
book4 = Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)

# __str__(): function output
print(book1) # If we print directly the object it will return the memory address but after __str__(): we print the messsage
print(book2)
print(book3)
print()

# __eq__(): function output
print("Is book1 equals to book2? :"+ str(book1 == book2)) # False
# Python doesnot allow cancatinate string and boolean value that's why I converted to str(book1 == book2)
print("Is book2 equals to book3? :"+str(book2 == book3)) # False
print("Is book3 equals to book4? :"+str(book3 == book4)) # True
print()

# __lt__(): function output
print("Is page number of book1 < book2? :"+str(book1 < book2))
print("Is page number of book2 < book3? :"+str(book2 < book3))
print("Is page number of book3 < book4? :"+str(book3 < book4))
print()

# __gt__(): function output
print("Is page number of book1 > book2? :"+str(book1 > book2))
print("Is page number of book2 > book3? :"+str(book2 > book3))
print("Is page number of book3 > book4? :"+str(book3 > book4))
print()

# __add()__: function output
print("Addding pages of book1 and book2: "+str(book1 + book2))
print("Addding pages of book2 and book3: "+str(book2 + book3))
print("Addding pages of book3 and book4: "+str(book3 + book4))
print()

# __contains__: function output
print("Harry" in book2)
print("Tolkien"in book1)
print("Anish" in book3)
print("Lewis" in book4)
print()

# __getitem__: function output
print("Info of book1: ")
print(book1["title"])
print(book1["author"])
print(book1["num_pages"])
print()

print("Info of book2: ")
print(book2["title"])
print(book2["author"])
print(book2["num_pages"])
print()

print("Info of book3: ")
print(book3["title"])
print(book3["author"])
print(book3["num_pages"])
print()





