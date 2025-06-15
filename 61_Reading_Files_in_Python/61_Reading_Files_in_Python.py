# Python reading files (.txt, .json, .csv)

# IMP NOTE: Make sure we have created the files to read in the desktop or location by writing it first before reading it. (I will only keep these files while learning this concept and may delete later..) 
# Because it will be like searching for something that doesn't even exists !

file_path_txt = "C:/Users/97798/Desktop/output.txt" # Absolute path and will throw filenotfound exception if not found

# Code to read a file .
try:
    with open(file_path_txt, "r") as file: # 'r' here means read
        content = file.read()
        print() # Just to print the contents in new line in the terminal...
        print("Reading my output.txt file :")
        print(content)
        
except FileNotFoundError:
    print("The file was not found, maybe file path wrong or file doesn't exist.")
    
except PermissionError:
    print("You do not have permission to read that file.")
    
    
# Example 2: Let's read our JSON File
import json

file_path_json = "C:/Users/97798/Desktop/collection_python.json" # Absolute path and will throw filenotfound exception if not found

# Code to read a file .
try:
    with open(file_path_json, "r") as file: # 'r' here means read
        content = json.load(file)
        print() # Just to print the contents in new line in the terminal...
        print("Reading my collection_python.json file :")
        print(content)
        
except FileNotFoundError:
    print("The file was not found, maybe file path wrong or file doesn't exist.")
    
except PermissionError:
    print("You do not have permission to read that file.")
    
    
# Example 3: Let's read our CSV file:
import csv

file_path_csv = "C:/Users/97798/Desktop/collection_python.csv"

# Code to read a file .
try:
    with open(file_path_csv, "r") as file: # 'r' here means read
        print()
        print("Reading my collection_python.csv file :")
        content = csv.reader(file) # This will just give the mmemory address
        for line in content:
            print(line)
        # print() # Just to print the contents in new line in the terminal...
        # print("Reading my collection_python.csv file :")
        # print(content)
        
except FileNotFoundError:
    print("The file was not found, maybe file path wrong or file doesn't exist.")
    
except PermissionError:
    print("You do not have permission to read that file.")
    
    
# Note to self: Run the 'Writing Files in Python' file to create different files in the desktop before running the Read File.