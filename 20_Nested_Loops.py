# nested loop = A loop within another loop (outer, inner)
#                outer loop:
#                        inner loop:

#Example 1 of nested loop
for x in range(3):
    for y in range(1, 10):
        #print(x, end="")
        print(y, end=" ")
        #print(x, end="-")
    print()
    
print("\n")
#Example 2, making a rectangle
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use : ")
print()

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()