#Python Number Guessing Game
import random

lower_num = 1
highest_num = 100
answer = random.randint(lower_num, highest_num)
guesses = 0
is_running = True
# print(answer)

print()
print("** --------- Python Number Guessing Game ---------- **")
print()
print(f"Select a number between {lower_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lower_num or guess > highest_num:
            print("The number is out of range !")
            print(f"Invalid Guess!! Select a number between {lower_num} and {highest_num}")
            
        elif guess < answer :
            print("Too Low! Please select higher number.")
            print()
            
        elif guess > answer:
            print("Too High! Please select lower number.")
            print()

        else:
            print()
            print()
            print("** ----------- HURRAY ------------ **")
            print(f"CORRECT! The Correct Answer Was {answer}")  
            print(f"Number of guesses: {guesses}") 
            is_running = False     
              
    else:
        print(f"Invalid Guess!! Select a number between {lower_num} and {highest_num}")
        