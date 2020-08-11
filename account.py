# Mikhail Pisman
# Simple Banking System
# https://github.com/mike-pisman/Simple_Banking_System
# account.py
# File contains Account class definition

from functions import check_card


# Account class contains all the information of the bank account
class Account:
    # Create objects
    def __init__(self, con, cur, data):
        self.id = data.id
        self.card = data.card
        self.pin = data.pin
        self.balance = data.balance
        # Load global variables connection and cursor passed from Bank class
        global connection, cursor
        connection = con
        cursor = cur

    # Display account menu
    def account_menu(self):
        # Menu options to display
        options = ["1. Balance", "2. Add income", "3. Do transfer", "4. Close account", "5. Log out", "0. Exit"]
        # Function for each of menu options
        functions = {"1": self.print_balance, "2": self.add_income, "3": self.transfer_money, "4": self.close_account,
                     "5": self.log_out, "0": exit}
        print("", *options, sep="\n")  # Print menu
        choice = input(">").strip()  # Get user input
        # Call function according to user choice from the list
        if choice not in functions.keys():
            print("This option does not exist.\nPlease try again")
            return self.account_menu()  # Get the account menu again
        else:
            functions[choice]()

    # Function updates balance and prints it out
    def print_balance(self):
        # Get the balance of the account from the database
        cursor.execute('select balance from card where id = ?', (self.id, ))
        self.balance = cursor.fetchone()[0]  # Update account's balance
        print('Balance:', self.balance)  # Print it out to the console
        return self.account_menu()  # Load account menu after completion

    # Function asks user for amount of money to add to the balance of the account
    def add_income(self):
        print("Enter income:")
        income = input(">").strip()  # Get user input
        if income.isdigit() and int(income) > 0:  # Check that input contains only digits
            self.set_balance(int(income) + self.balance)  # Update balance
            print("Income was added!")
        else:
            print("Incorrect amount!")
        return self.account_menu()  # Load account menu after completion

    # Function changes balance and update info in the database
    def set_balance(self, balance):
        self.balance = balance  # Update balance
        # Pass updated balance to the database
        cursor.execute('update card set balance = ? where id = ?', (balance, self.id))
        connection.commit()

    # Function asks user for amount and card number to transfer, then transfers amount between accounts
    def transfer_money(self):
        print("Transfer:", "Enter card number:", sep="\n")
        card = input(">").strip()  # Get card number
        if len(card) == 16 and card.isdigit() and check_card(card):  # Check if card number is correct
            if card != self.card:  # Check that it's not the same account
                other_id = self.get_account_id(card)  # Get other account from the database by card number
                if other_id:  # If account was found
                    other_id = other_id[0]  # Get the other account's id
                    print("Enter how much money you want to transfer:")  # Ask user for amount of money to transfer
                    amount = input(">").strip()
                    if amount.isdigit() and int(amount) > 0:  # Check that amount of money contains only digits
                        amount = int(amount)
                        if amount <= self.balance:  # Check that account has enough fund to transfer
                            self.balance -= amount  # Remove funds from the account
                            # Update balance int he database
                            cursor.execute('update card set balance = ? where id = ?', (self.balance, self.id))
                            # Add fund to the other account
                            cursor.execute('update card set balance = balance + (?) where id = ?', (amount, other_id))
                            connection.commit()
                            print("Success!")
                        else:
                            print("Not enough money!")
                    else:
                        print("Incorrect amount!")
                else:
                    print("Such a card does not exist.")
            else:
                print("You can't transfer money to the same account!")
        else:
            print("Probably you made mistake in the card number. Please try again!")
        return self.account_menu()

    # Function return account's id if account is found in the database, otherwise returns None
    def get_account_id(self, card):
        cursor.execute("select id from card where number = ?", (card, ))
        f = cursor.fetchone()
        return f

    # Function to close account and remove it from the database
    def close_account(self):
        cursor.execute('delete from card where id = ?', (self.id, ))
        connection.commit()
        print("The account has been closed!")

    # Function to Log out and return to the bank menu
    def log_out(self):
        print("You have successfully logged out!")
