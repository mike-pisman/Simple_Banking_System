# Mikhail Pisman
# Simple Banking System
# https://github.com/mike-pisman/Simple_Banking_System

import sys
import random
import math
import sqlite3
from collections import namedtuple

connection = sqlite3.connect('card.s3db')
cursor = connection.cursor()

class Bank:
    global cursor, connection
    Account = namedtuple('Account', 'id, card, pin, balance')

    def __init__(self):
        cursor.executescript('create table if not exists card(' +
                            'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                            'number TEXT NOT NULL,' +
                            'pin TEXT NOT NULL,' +
                            'balance INTEGER NOT NULL DEFAULT 0' +
                            ')')
        connection.commit()
        self.main_menu()

    def main_menu(self):
        # self.cursor.execute('drop table card')
        # self.connection.commit()
        options = ["1. Create an account", "2. Log into account", "0. Exit"]
        functions = {"1": self.new_account, "2": self.log_in, "0": exit}

        print("", *options, sep="\n")
        choice = input(">").strip()

        if choice not in functions.keys():
            print("This option does not exist.\nPlease try again")
        else:
            functions[choice]()
        return self.main_menu()

    def log_in(self):
        print("Enter your card number:")
        card_number = input(">").strip()
        if card_number.isdigit():
            print("Enter your PIN:")
            pin = input(">").strip()
            if pin.isdigit():
                account = self.get_account(card_number, pin)
                if account:
                    account = Account(account)
                    print("You have successfully logged in!")
                    account.account_menu()
                    return
        print("Wrong card number or PIN!")

    def new_account(self):
        print("\nYour card has been created")
        accounts = self.get_all_accounts()
        while True:
            new_number = generate_account_number()
            if new_number not in accounts.keys():
                break
        pin = generate_pin()
        card = generate_card_number(new_number)

        print("Your card number:", card, "Your card PIN:", pin, sep="\n")
        cursor.execute("insert into card(number, pin) values (?, ?) ", (card, pin))
        connection.commit()

    def get_all_accounts(self):
        accounts = {}
        cursor.execute('select * from card')
        for acc in map(self.Account._make, cursor.fetchall()):
            accounts[acc.card] = acc.pin
        return accounts

    def get_account(self, account_numb, pin):
        cursor.execute("select * from card where number = ? and pin = ?", (account_numb, pin))
        f = cursor.fetchone()
        return self.Account._make(f) if f else None


class Account:
    def __init__(self, data):
        self.id = data.id
        self.card = data.card
        self.pin = data.pin
        self.balance = data.balance

    def account_menu(self):
        options = ["1. Balance", "2. Add income", "3. Do transfer", "4. Close account","5. Log out", "0. Exit"]
        functions = {"1": self.print_balance, "2": self.add_income, "3": self.transfer_money, "4": self.close_account, "5": self.log_out, "0": exit}
        print("", *options, sep="\n")
        choice = input(">").strip()

        if choice not in functions.keys():
            print("This option does not exist.\nPlease try again")
            return self.account_menu()
        else:
            functions[choice]()

    def print_balance(self):
        cursor.execute('select balance from card where id = ?', (self.balance, self.id))
        self.balance = cursor.fetchone()[0]
        print('Balance:', self.balance)
        return self.account_menu()

    def add_income(self):
        print("Enter income:")
        income = input(">").strip()
        if income.isdigit() and int(income) > 0:
            self.set_balance(int(income) + self.balance)
            print("Income was added!")
        else:
            print("Incorrect amount!")
        return self.account_menu()

    def set_balance(self, balance):
        self.balance = balance
        cursor.execute('update card set balance = ? where id = ?', (balance, self.id))
        connection.commit()

    def transfer_money(self):
        print("Transfer:", "Enter card number:", sep="\n")
        card = input(">").strip()
        if len(card) == 16 and card.isdigit() and check_card(card):
            if card != self.card:
                other_id = self.get_account_id(card)
                if other_id:
                    other_id = other_id[0]
                    print("Enter how much money you want to transfer:")
                    amount = input(">").strip()
                    if amount.isdigit() and int(amount) > 0:
                        amount = int(amount)
                        if amount <= self.balance:
                            self.balance -= amount
                            cursor.execute('update card set balance = ? where id = ?', (self.balance, self.id))
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

    def get_account_id(self, card):
        cursor.execute("select id from card where number = ?", (card, ))
        f = cursor.fetchone()
        return f

    def close_account(self):
        cursor.execute('delete from card where id = ?', (self.id, ))
        connection.commit()
        print("The account has been closed!")

    def log_out(self):
        print("You have successfully logged out!")

def check_card(card):
    luhn_sum = luhn_algorithm(card[:-1])
    checksum = 10 - luhn_sum % 10 if luhn_sum % 10 != 0 else 0
    return checksum == int(card[-1])

def exit():
    print("\nBye!")
    connection.close()
    sys.exit()

def generate_card_number(acc_number):
    iin = "400000"
    luhn_sum = luhn_algorithm(iin + acc_number)
    checksum = 10 - luhn_sum % 10 if luhn_sum % 10 != 0 else 0
    return iin + acc_number + str(checksum)

def generate_account_number():
    acc_number = ""
    for _ in range(9):
        acc_number += str(random.randrange(10))
    return acc_number

def generate_checksum(luhn_result):
    return 0

def luhn_algorithm(card_number):
    card_number = list(map(int, card_number))
    for i, _ in enumerate(card_number, 1):
        if i % 2 != 0:
            card_number[i - 1] *= 2
        if card_number[i - 1] > 9:
            card_number[i - 1] -= 9
    return sum(card_number)

def generate_pin():
    pin = ""
    for _ in range(4):
        pin += str(random.randrange(10))
    return pin

def main():
    bank = Bank()

if __name__ == '__main__':
    main()
