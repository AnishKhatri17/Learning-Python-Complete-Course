# Python Slot Machine

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results
    
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("\t"+"-------------")
    print("\t"+" | ".join(row))
    print("\t"+"-------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
        
    return 0 # Return 0 if no match ...
    
def main():
    balance = 100
    print("*********************************")
    print("---- Welcome to Python Slots ----")
    print("Symbols: 🍒   🍉    🍋   🔔   ⭐")
    print()
    print("---------- Prize Pool -----------")
    print("🍒 × 3 = Your bet amount (Three Times)") # multiply symbol in windows: Alt + 0215 
    print("🍉 × 3 = Your bet amount (Four Times)")
    print("🍋 × 3 = Your bet amount (Five Times)")
    print("🔔 × 3 = Your bet amount (Ten Times)")
    print("⭐ × 3 = Your bet amount (Twenty Times)")
    
    print("*********************************")
    
    while balance > 0:
        print(f"Current Balance: Rs.{balance}")
        
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit():
            print("Please Enter a Valid Number: ")   
            continue 
    
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient Fund.")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
    
        balance -= bet
        
        row = spin_row()
        print("Spinning...\n")
        print_row(row) 
    
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"Congratulation!! You won Rs.{payout}")

        else:
            print("Sorry! You lost this round.")
            
        balance += payout       
        
        play_again = input("Do you want to spin again (Y/N): ").upper()
        
        if play_again != 'Y':
            break    
    
    print()
    print("-----------------------------------------------")
    print(f"Game Over! Your Final Balance is Rs. {balance}")
    print("-----------------------------------------------")
    
if __name__ == '__main__':
    main()