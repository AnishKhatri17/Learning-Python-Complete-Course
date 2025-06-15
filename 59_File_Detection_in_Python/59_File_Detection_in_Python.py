# File Detection in Python.

# There are two types of file paths :
# 1. Relative Path = folder/test.txt
# 2. Absolute Path = C:/Users/97798/Desktop/test.txt 

import os

file_path = "59_File_Detection_in_Python/test.txt" # relative path

# Providing Absolute Path (Below is the path based on my 'Victos HP Laptop')
# file_path = "C:\\Users\\97798\\Desktop\\test.txt" # Python treats \ as escape sequence so use \\ for file detection
# file_path = "C:/Users/97798/Desktop/test.txt"  # This is also valid. using /

# For Directory (Folder) created in my Desktop Location
# file_path = "C:\\Users\\97798\\Desktop\\test"


if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    
    if os.path.isfile(file_path):
        print("\n"+"That is a file.")
    
    elif os.path.isdir(file_path):
        print("\n"+"That is a directory (Folder).")
    
else:
    print("The location doesn't exist !")