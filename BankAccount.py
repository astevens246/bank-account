import random

class BankAccount:
    def __init__(self, full_name):
        # Initialize a bank account with a full_name, generate a random 8-digit number, and set the initial balance to 0.
        self.full_name = full_name
        self.account_number = self.generate_account_number()
        self.balance = 0

    def generate_account_number(self):
        # Generate a random 8-digit account number.
        return str(random.randint(10000000, 99999999))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount")

    def withdraw(self, amount):
        # Withdraw money from the account, deducting the amount from the balance and printing the new balance.
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Amount withdrawn: ${amount:.2f} new balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds. Overdraft fee charged: $10")
                self.balance -= 10
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
    
    def get_balance(self):
        # Print the account balance for the account owner and return the current account balance.
        print(f"Account balance for {self.full_name}: ${self.balance:.2f}")
        return self.balance

    def add_interest(self):
        # Adds interest to the account based on a 1% annual rate.
        monthly_interest = self.balance * 0.00083
        self.balance += monthly_interest

    def print_statement(self):
        # Print a statement with the account owner's name, the last 4 digits of the account number, and the balance.
        print(f"{self.full_name}")
        print(f"Account No.: ****{self.account_number[-4:]}")
        print(f"Balance: ${self.balance:.2f}\n")
