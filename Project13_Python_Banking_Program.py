# Python Banking Program
# 1. Show Balance
# 2. Deposit
# 3. Withdraw

def show_balance(balance):
    print("---------------------------------------")
    print(F"Your balance is Rs.{balance:.2f}")
    print("---------------------------------------")

def deposit():
    print("***************************************")
    amount = float(input("Enter the amount of money to be deposited: "))
    print(f"Thank you for depositing Rs. {amount}")
    # print(f"Your Total Balance is now: ")
    print("***************************************")
   
    if amount < 0: 
        print("***************************************")
        print("That's not a valid amount!! Please Try Again.")
        print("***************************************")
        return 0
    
    elif amount < 500:
        print("***************************************")
        print("Sorry, you cannot deposit amount less than 500, Please Try again.")
        print("***************************************")
        return 0
    
    else:
        return amount
    
    
def withdraw(balance):
    print("***************************************")
    amount = float(input("Enter the amount to be withdrawn: "))
    print(f"Thank you for withdrawing Rs. {amount}")
    # print(f"Your Total Balance is now: ")
    print("***************************************")
       
    if amount > balance:
        print("***************************************")
        print(f"Insufficient funds, you cannot withdraw {amount}")
        print("***************************************")
        return 0
        
    elif amount < 0:
        print("***************************************")
        print(f"{amount} must be greater than 0, Please Try Again !!!")
        print("***************************************")
        return 0
        
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n")
        print("***************************************")
        print(" ----------- Banking Program --------- ")
        print("***************************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("***************************************")
        
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("***************************************")
            print("This is not a valid input, please try again !!!")
            print("***************************************")
    
    print("---------------------------------------")
    print("Thank you! Have a Great Day !!!")
    print("---------------------------------------")

    
       
if __name__ == '__main__':
    main()
    