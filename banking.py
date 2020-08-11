# Mikhail Pisman
# Simple Banking System
# https://github.com/mike-pisman/Simple_Banking_System
# banking.py
# File contains Bank class as well as main function

from collections import namedtuple
from functions import generate_account_number, generate_pin, generate_card_number
from account import Account
import sqlite3


# Bank class
class Bank:
    # Create tuple for handling SQL query
    Account = namedtuple('Account', 'id, card, pin, balance')

    # Init function
    def __init__(self):
        # Create global variables for SQL and establish connection to database
        global cursor, connection
        connection = sqlite3.connect('card.s3db')
        cursor = connection.cursor()
        # Create a table in database if it does not exist already
        cursor.executescript('create table if not exists card(' +
                            'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                            'number TEXT NOT NULL,' +
                            'pin TEXT NOT NULL,' +
                            'balance INTEGER NOT NULL DEFAULT 0' +
                            ')')
        connection.commit()
        # Show main Menu
        self.main_menu()

    # Function to print main menu
    def main_menu(self):
        options = ["1. Create an account", "2. Log into account", "0. Exit"]  # Menu options to display
        functions = {"1": self.new_account, "2": self.log_in, "0": exit}  # Function for each of menu options
        print("", *options, sep="\n")  # Print menu
        choice = input(">").strip()  # Get user input
        # Call function according to user choice from the list
        if choice not in functions.keys():
            print("This option does not exist.\nPlease try again")
        else:
            functions[choice]()
        return self.main_menu()  # Load menu again after completion

    # Function to log in to an account
    def log_in(self):
        print("Enter your card number:")
        card_number = input(">").strip()  # Get card number
        if card_number.isdigit():  # Check that input contains only digits
            print("Enter your PIN:")
            pin = input(">").strip()  # Get pin number
            if pin.isdigit():  # Check that input contains only digits
                account = self.get_account(card_number, pin)  # Get account from the database
                if account:  # If account is found
                    account = Account(connection, cursor, account)  # Create new instance of class Account
                    print("You have successfully logged in!")
                    account.account_menu()  # Load account menu
                    return
        print("Wrong card number or PIN!")

    # Function to create new account
    def new_account(self):
        print("\nYour card has been created")
        accounts = self.get_all_accounts()  # Get a dictionary of all accounts
        while True:
            new_number = generate_account_number()  # Generate new account number
            card = generate_card_number(new_number)  # Generate new card number
            if card not in accounts.keys():  # Make sure that new card number is unique
                break
        pin = generate_pin()  # Generate new pin number
        print("Your card number:", card, "Your card PIN:", pin, sep="\n")  # Print new account information
        cursor.execute("insert into card(number, pin) values (?, ?) ", (card, pin))  # Add new card and pin to database
        connection.commit()

    # Function returns dictionary with card numbers as keys and pins as their values
    def get_all_accounts(self):
        accounts = {}  # Create empty dictionary
        cursor.execute('select * from card')  # Get all accounts from the database
        for acc in map(self.Account._make, cursor.fetchall()):
            accounts[acc.card] = acc.pin  # Add pair to the dictionary as ("card number": "pin")
        return accounts  # Return the dictionary

    # Function returns named tuple of account from the database if account exist or None otherwise
    def get_account(self, account_numb, pin):
        # Request query with card number and pin
        cursor.execute("select * from card where number = ? and pin = ?", (account_numb, pin))
        f = cursor.fetchone()
        return self.Account._make(f) if f else None  # Return named tuple Account(id, card, pin, balance) or None


# Main Function
def main():
    bank = Bank()


if __name__ == '__main__':
    main()
