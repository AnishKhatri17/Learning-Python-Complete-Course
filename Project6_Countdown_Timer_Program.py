# Countdown Timeout Game

# import time
# my_time = int(input("Enter the time in seconds for the countdown: "))
# for x in range(0, my_time):
#     time.sleep(1)
# time.sleep(3) # sleep for 3 seconds
# print("Time's Up !!")


# Now making Countdown Timeout Game
import time

my_time = int(input("Enter the time is seconds for timeout: "))

# for x in range(0, my_time):
# for x in reversed(range(0, my_time)):
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) # after each iteration we want to sleep for 1 seconds
    
print("\n\n")
print("TIME'S UP, BOOOOOOOM !!!!!!!!!!!")
    