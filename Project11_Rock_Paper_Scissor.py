import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    
    player = None
    computer = random.choice(options)
    
    while player not in options:
        print("\n")
        player = input("Enter a choice (rock, paper, scissors): ")
        
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("!!! It's a Tie !!!")

    elif player == "rock" and computer == "scissors":
        print("Hurray, You Win !!")
        
    elif player == "paper" and computer == "rock":
        print("Hurray, You Win !!")
        
    elif player == "scissors" and computer == "paper":
        print("Hurray, You Win !!")
 
    else:
        print("Oppps, You Lose !!!")
        
    # play_again = input("Play Again? (y/n): ").lower()
    # if not play_again == "y":
    #     running = False
    if not input("Play Again? (y/n): ").lower() == "y":
        playing = False
        
print("Thanks for Playing! ")
    
