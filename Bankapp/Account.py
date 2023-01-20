import json
import re

"""BankAccount class"""
class Account:

    def __init__(self, accountnbr, balance = 0):
        self.accountnbr = accountnbr
        self.balance = balance
        
    """Returns account details as string."""
    def __str__(self):
        return json.dumps(self.__dict__, indent=2, separators=(',', ': '))
        
    def to_dict(self):
        return {
            "account_number": self.accountnbr,
            "balance": self.balance
        }
    
    """Check for valid accountnumber"""
    def is_valid_account_number(self, accountnbr): 
        pattern = re.compile("^[0-9]{5,10}$")
        if not pattern.match(accountnbr):
            return False
        return True


    """Check for valid amount."""
    def is_valid_amount(self, amount):
        if isinstance(amount, (int, float)) == True:
            return True
        else:
            return False 
    
    """Allow user to deposit money into specified account""" 
    def deposit(self, amount):    
        if amount >= 0:
            self.balance += amount
            return True
        else: 
            print("Invalid amount.")
            return False
    
    """Allow user to withdraw specified amount. Return True if succeeded.""" 
    def withdraw(self, amount):
        if self.is_valid_amount(amount) and self.balance >= amount: 
            self.balance = self.balance - amount
            return self.balance
        else:
            print("\n Insufficient funds!")
            return False
        
    """Return account balance"""
    def get_balance(self):
        return self.balance
        
    """Sets account balance. Return True if succeded."""
    def set_balance(self, balance):
        if balance >= 0:
            self.balance = balance
            return True
        else:
            print("Balance can't be negative. Please specify a valid amount.")
            return False

    """Returns the accountnumber"""
    def get_accnumber(self):
        return self.accountnbr



"""Test"""

acc = Account(123456, 0)

acc.set_balance(5000)       # setbalance(balance) - sets balance OK
print(acc.balance)

acc.withdraw(500)           # Withdraw(amount) - subtracts amount OK
print(acc.balance)    

acc.deposit(500)            # Deposit(amount) - adds amount OK
print(acc.balance)

print(acc.get_accnumber())  # get_accnumber() - Returns number OK




