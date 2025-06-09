# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make our functions more flexible, reduces number of arguments
#                     1. positional, 2. DEFAULT 3. keyword, 4. arbitary


# def net_price(list_price, discount, tax ):
# now defining default values to arguments .....
def net_price(list_price, discount= 0, tax= 0.05):
    result = str(list_price * (1 - discount) * (1 + tax))
    # I used str() because I could not concatinate string value and a flost value in the below print result display...
    return result

# print(net_price(500, 0, 0.05))
print("The net price is: " + ""+ net_price(500)) # this will take default discount and tax values from the function
print("The net price is: "+ ""+ net_price(500, 0.1)) # This will take discount value 0.1 as passed rather than 0 as declared in the argument
print("The net price is: "+""+ net_price(500, 0.5, 0.25))  # This will take discount value 0.5 as passed rather than 0 as declared in the argument same for tax, it takes 0.25 not 0.05


# Second Exercise..
import time 

print()
print()
# def count(start = 0, end): # Non-default arguments follow default argument
def count(end, start = 0):
    for x in range(start, end+1): # because last value is excluded inside range()
        print(x)
        time.sleep(1)
    print("DONE !")

# count(10)  
count(30, 15)  
# countdown from 15 t0 30 with 1 second increment.