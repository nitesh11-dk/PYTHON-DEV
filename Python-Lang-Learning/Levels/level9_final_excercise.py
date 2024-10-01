class BankAccount:
    def __init__(self, account_num, balance=0):
        self.__balance = balance
        self.account_num = account_num

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount >= self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount


accounts = {}

while True:
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show balance")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    # Check if the input is a valid number
    if not choice.isdigit():
        print("Invalid input! Please enter a valid option.")
        continue

    choice = int(choice)

    if choice == 1:
        account_num = input("Enter your account number: ")
        balance = input("Enter your initial balance: ")
        
        # Check if the balance input is a valid number
        if not balance.isdigit():
            print("Invalid input for balance! Please enter a number.")
            continue
        
        balance = int(balance)
        account = BankAccount(account_num, balance)
        accounts[account_num] = account
        print("Account Created Successfully !!!")

    elif choice == 2:
        account_num = input("Enter your account number: ")
        if account_num in accounts:
            amount = input("Enter the amount you want to deposit: ")
            
            # Check if the amount input is a valid number
            if not amount.isdigit():
                print("Invalid input! Please enter a number.")
                continue
                
            amount = int(amount)
            accounts[account_num].deposit(amount)
            print("Amount deposited successfully! New balance is: " + str(accounts[account_num].get_balance()))
        else:
            print("Account Number is invalid")

    elif choice == 3:
        account_num = input("Enter your account number: ")
        if account_num in accounts:
            amount = input("Enter the amount you want to withdraw: ")
            
            # Check if the amount input is a valid number
            if not amount.isdigit():
                print("Invalid input! Please enter a number.")
                continue
            
            amount = int(amount)
            accounts[account_num].withdraw(amount)
            print("Amount withdrawn successfully! New balance is: " + str(accounts[account_num].get_balance()))
        else:
            print("Account Number is invalid")

    elif choice == 4:
        account_num = input("Enter your account number: ")
        if account_num in accounts:
            print("Your bank balance is: " + str(accounts[account_num].get_balance()))
        else:
            print("Account Number is invalid")

    elif choice == 5:
        print("Thanks for using our service!")
        break

    else:
        print("Please enter a valid option from the list.")
