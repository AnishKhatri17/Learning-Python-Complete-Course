# Multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import time

def walk_dog(first, last): # Example: This function takes arguments
    time.sleep(5)
    print(f"You walk {first} {last} with you.")
    
def take_out_trash(day): # This only takes one parameter.
    time.sleep(3)
    print(f"You take out the trash on {day}.")
    
def get_mail():
    time.sleep(1)
    print("You get the mail.")
    
    
# walk_dog() # THIS WILL TAKE 5 SECONDS TO EXECUTE FIRST 
# take_out_trash() # THIS WILL TAKE 3 SECONDS TO EXECUTE SECOND
# get_mail() # THIS WILL TAKE 1 SECOND TO EXECUTE THIRD
# The drawback is that we have to wait all the remainging tasks just because the first task requires so much time to execute. So we use MultiThreading in Python


chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo")) # Let's pass arguments here in 'Tuple'
chore1.start()

chore2 = threading.Thread(target=take_out_trash, args=("Saturday",)) # , should be given otherwise it will be interpreted as a string exclosed in parentheses ""
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print()
print("All chores are completed.") # This will print instantly before executing the threading that's why we use 'join' to let this execute only after all the threads are executed concurrently...