#Python Banking System
def show_balance(Balance):
    print(f"You balance is ${Balance:.2f}")
def deposit():
    amount = float(input("Enter an amount to be deposit:"))
    if amount<=0:
        print("That's not a valid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter an amount to be withdraw:"))
    if amount>balance:
        print("insufficient funds")
        return 0
    elif amount<0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True
    while is_running:
        print("Banking program")
        print("1.show Balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.Exit")
        choice = input("Enter your choice(1-4):")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance=balance+deposit
        elif choice == '3':
            balance-=withdraw(balance)
        elif choice =='4':
            is_running = False
        else:
            print("That is not a valid choice")
    print("Thank you! Have a nice day!")