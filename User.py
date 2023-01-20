import json
import Account

"""The User class represents a user of the banking system. It contains for logging in and out, adding and removing accounts."""
class User:
        
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = {}
        self.isloggedin = None
        
    """Return string representation of self."""
    def __str__(self):
        return json.dumps(self.__dict__, indent=2, separators=(',', ': '))
        
    def show_details(self):
        print()
            
    """Verify user credentials"""
    def check_credentials(self, user, password):
        if user == self.username and password == self.password:
            return True
        else:
            return False

    def change_password(self, current_pwd, new_pwd):
        if current_pwd == self.password:
            self.password = new_pwd
            return True
        else:
            print("Invalid password.")
            return False

    """Add account """
    def add_account(self, accnumber):
        account = Account(accnumber)
        if accnumber not in self.accounts:
            self.accounts.update(account)
        else:
            print("Account already exist.")

    """Delete account"""
    def delete_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
        else:
            print("Account does not exist.")
        
    """Return list of all the customers accounts"""
    def get_accounts(self):
        return self.accounts

    """Logs user in"""
    def login(self, username, password):
        if self.username == username and self.password == password:
            self.isloggedin = True
            return True
        else:
            print("Invalid credentials.")
            return False

    """Logs user out"""
    def logout(self):
        self.isloggedin = False


"""Test"""

"""Initialize users"""
user1 = User("Petter", "hej")
user2 = User("Albus", "korv")

"""Loggedin"""
print(f"Logged in: {user1.isloggedin}")


print(user1.check_credentials("Petter", "hej"))     # Expected True - Returns True
print(user1.check_credentials("Petter", "hejdå"))   # Expected False - Returns False


accounts1 = user1.get_accounts()
print(accounts1)
