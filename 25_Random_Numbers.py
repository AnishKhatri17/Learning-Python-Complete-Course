import random

# print(help(random))
low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# number = random.randint(1, 6)
intNumber = random.randint(low, high) # random.randint() is used to random integer number
floatNumber = random.random() # random.random() is used to random float number between 0 and 1
option = random.choice(options) #choice() is for random elements
random.shuffle(cards) # shuffle() will shuffle all the elements 
 
print(intNumber)
print(floatNumber)
print(option)
print(cards)