# Python writing files (.txt, .json, .csv)

txt_data = "I love Cricket !"

file_path = "output.txt" # relative path
file_path_desktop = "C:/Users/97798/Desktop/output.txt" # absolute path

# with open(file=file_path, mode="w") as file: # 'w' is for write there are more modes like 'r' 'a' 'x' etc
with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created")
    # This code creates a txt file output.txt in the same repository
    

# Now I am trying to create a txt file in my desktop from python code.
# 'w' will override a file
try:
    with open(file_path_desktop, "w") as file: # 'x' doesnot allow to create a file if it already exists.
        file.write(txt_data)
        print(f"txt file {file_path_desktop} was created")

except FileExistsError:
    print("That file already exists!")
    

# 'a' will add contents to the file
# try:
#     with open(file_path_desktop, "a") as file: # 'x' doesnot allow to create a file if it already exists.
#         file.write("\n" +txt_data)
#         print(f"txt file {file_path_desktop} was created")

# except FileExistsError:
#     print("That file already exists!")
# If we just run this block of code 3 time, output is :
# I love Cricket !
# I love Cricket !
# I love Cricket !


# Second Example let's say we have a collection.
employees = ["Eugene", "Spongebob", "Patrick", "Sandy"]

file_path_list = "C:/Users/97798/Desktop/collection_python.txt"
try:
    with open(file_path_list, "w") as file:
        # file.write(employees) This will throw error for list so we need to itrate over it
            for employee in employees:
                file.write(employee + "\n")
            print(f"txt file {file_path_list} was created")

except FileExistsError:
    print("That file already exists!")
    
    
    
# Third Example for json files.
import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path_json = "C:/Users/97798/Desktop/collection_python.json"
try:
    with open(file_path_json, "w") as file:
            json.dump(employee, file, indent=4)
            print(f"json file {file_path_json} was created")

except FileExistsError:
    print("That file already exists!")


# Fourth Example for csv files.
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path_csv = "C:/Users/97798/Desktop/collection_python.csv"
try:
    with open(file_path_csv, "w", newline="") as file:
            writer = csv.writer(file)
            for row in employees:
                writer.writerow(row)
            print(f"json file {file_path_csv} was created")

except FileExistsError:
    print("That file already exists!")

