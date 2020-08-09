# Mikhail Pisman
# Simple Banking System
#

import sys
import random


class Bank:
    def __init__(self):
        self.accounts = {}
        self.main_menu()

    def main_menu(self):
        options = ["1. Create an account", "2. Log into account", "0. Exit"]
        functions = {"1": self.new_account, "2": self.log_in, "0": self.exit}

        print("", *options, sep="\n")
        choice = input(">").strip()

        if choice not in functions.keys():
            print("This option does not exist.\nPlease try again")
        else:
            functions[choice]()
        return self.main_menu()

    def account_menu(self, account):
        options = ["1. Balance", "2. Log out", "0. Exit"]
        functions = {"1": self.print_balance, "2": self.main_menu, "0": self.exit}
        print("", *options, sep="\n")
        choice = input(">").strip()

        if choice not in functions.keys():
            print("This option does not exist.\nPlease try again")
        else:
            functions[choice]()

    def exit(self):
        print("\nBye!")
        sys.exit()

    def log_in(self):
        print("Enter your card number:")
        card_number = input(">").strip()
        if card_number.isdigit():
            print("Enter your PIN:")
            pin = input(">").strip()
            if pin.isdigit():
                account_number = card_number[6:15]
                print(account_number)
                if self.get_account(int(account_number), pin):
                    print("You have successfully logged in!")
                    self.account_menu(account_number)
                    return
        print("Wrong card number or PIN!")

    def new_account(self):
        print("\nYour card has been created")
        while True:
            new_number = generate_account_number()
            if new_number not in self.accounts.keys():
                break
        pin = generate_pin()
        print("Your card number:", generate_card_number(new_number), "Your card PIN:", pin, sep="\n")
        self.accounts[new_number] = pin

    def get_account(self, account, pin):
        if account in self.accounts.keys():
            return self.accounts[account] == pin
        return False

    def print_balance(self):
        print("0")
        return self.account_menu()

def generate_card_number(acc_number):
    iin = "400000"
    checksum = "5"
    return int(iin + str(acc_number) + checksum)

def generate_account_number():
    acc_number = ""
    for _ in range(9):
        acc_number += str(random.randrange(10))
    return int(acc_number)

def generate_pin():
    pin = ""
    for _ in range(4):
        pin += str(random.randrange(10))
    return pin

def main():
    bank = Bank()

if __name__ == '__main__':
    main()
