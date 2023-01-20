import json
import User as user
import Account as acc
import unittest

"""The Bank class is responsible for managing the users, with methods for creating new users, modify users,
logging in existing users, and loading and saving user data to a JSON file."""
class Bank:
    
    """Constructor"""
    def __init__(self):
        self.users = {} # Dictionary containing Contains all banks users
        self.load_users() 

    """Lets user login to the bank"""
    def login_user(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user["username"] == username and user["password"] == password:
                user["isloggedin"] = True
                self.save_user
                return True
        else:    
            print('Invalid username/password')
            return False
        
    """Logs user out --> Sets current users login flag to false."""  
    def logout_user(self, username):
        if username in self.users:
            user = self.users[username]
            user["isloggedin"] = False
            self.save_users(username)
            return True
        else:
            return False

    """Load user from JSON-file"""
    def load_users(self):
        with open('users.json', 'r') as file:
            self.users = json.load(file)
            for user in self.users:
                user["isloggedin"] = False # Users are logged out by default. 
            
    """Save users to JSON-file"""
    def save_users(self): 
        with open('users.json', 'w') as file:
            json.dump(self.users, file)
            
    
    """Create and register new user"""
    def add_user(self, username, password):
        if username not in self.users:
            user = {
                "username" : username,
                "password" : password,
                "isloggedin" : False,
                "accounts": {} 
            }
            self.users[username] = user
            self.save_users()
            return True
        else:
            return False
    
    """Deletes user from """
    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            self.save_users()
            return True
        else:
            print("User does not exist.")
            return False

    """Return a list of all bank users"""
    def get_user(self):
        if self.customerlist != None:
            return self.users
   
    """Return a specific user from list of users"""    
    def get_user(self, user):
        if user not in self.users:
            print("User not found.")
        else:
            return user
        
    """Removed customer from customer list"""
    def remove_user(self, user):
        if user not in self.users:
            print("User does not exist.")
            False
        else:
            self.users.pop(user)
            print(f"User {user} was removed from bank.")
            return True
    
    """Add user to bank"""
    def create_user(self, name, password):
        
        user = user(name, password)
        return user           
    
    """Update user password"""
    def change_password(self, current_pwd, new_pwd):
        if current_pwd == new_pwd:
            self.current_pwd = new_pwd
            return True
        else:
            print("Incorrect password")
            return False
