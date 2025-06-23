# Hangman in Python
import random
from Project16_Wordslist import words
# words = ("apple", "orange", "banana", "coconut", "pineapple")

# Dictionary of key:()
hungman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")
               }

# for line in hungman_art[6]:
#     print(line)

def display_man(wrong_guesses):
    print("---------------")
    for line in hungman_art[wrong_guesses]:
        print(line)
    print("---------------")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))
    

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    # print(answer)
    # print(hint)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        # This is to prevent user from inserting wrong input.
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input !!!")
            continue 
        
        if guess in guessed_letters:
            
            print(f"{guess} is already guessed.")
            continue
        
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations !!! YOU WIN.")
            print()
            is_running = False
            
        elif wrong_guesses >= len(hungman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose the Game !!!")
            print()
            is_running = False
            
            
   
if __name__ == "__main__":
    while True:  # Loop to allow replaying
        main()  # Run the game

        play_again = input("Do you want to play again (Y/N): ").upper()
        print()

        if play_again != 'Y':  
            break
        