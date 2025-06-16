
import datetime

date = datetime.date(2025, 6, 7)
# Printing today's date in python date and time
today = datetime.date.today()

# Printing our defined time in the terminal
time = datetime.time(12, 30, 0)

# Printing current now date of the computer system
now = datetime.datetime.now()
# Formatting the now datetime in the correct date and time format
now = now.strftime("%H:%M:%S %m-%d-%y")


print(date)
print(today)
print(time)
print(now)


print()
print()
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1) # year, month, day, hour, minute, second.
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
    
else:
    print("Target date has NOT passed")
