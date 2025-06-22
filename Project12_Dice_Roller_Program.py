import random

# using unicode character for symbol in our Python Code
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#These Are The Outputs of the Above ASCII Code
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",  
        "│ ●     ● │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("Enter the number of dice?: "))
print()

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
    
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)    
    
# print(dice)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end ="")
    print()

for die in dice:
    total += die
print(f"Total is: {total}")
    

 