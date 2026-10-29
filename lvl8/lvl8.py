#Eli Baker
#Bank account

from lvl8funct import BankAccount

print("Welcome to the Bogugie Bank")

name = input("Please enter your name: ")

account = BankAccount(name)

while True:
    print("Please choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("How much would you like to deposit? "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("How much would you like to withdraw? "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_info()

    elif choice == "4":
        print("Thank you for banking at Bogugie Bank")
        break

    else:
        print("Invalid choice. Please try again.")