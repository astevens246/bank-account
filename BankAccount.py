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


