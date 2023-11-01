import random
class BankAccount:
    def __init__(self, full_name):
    #initialize a bank account with a full_name, generate a random 8 digit number and set inital balance to 0 
        self.full_name = full_name
        self.account_number = self.generate_account_number()
        self.balance = 0
def generate_account_number(self):
    #generate a random 8-digit account number 
    return str(random.randint(100000000, 99999999))

