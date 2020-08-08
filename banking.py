# Mikhail Pisman
# Simple Banking System
#

import sys

class Bank:

    accounts = {}

    def show_menu(self):
        options = ["1) Log into account", "2) Create an account", "0) Exit"]
        functions = {"1": self.log_in, "2": self.new_account, "0": self.exit}

        print("", *options, sep="\n")
        choice = input(">").strip()

        if choice not in functions.keys():
            print("This option does not exist.\nPlease try again")
        else:
            functions[choice]()
        return self.show_menu()

    def exit(self):
        print("\nBye!")
        sys.exit()

    def log_in(self):
        print("Enter your card number:")
        account = input(">").strip()
        if account.isdigit():
            print("Enter your PIN:")
            pin = input(">").strip()
            if pin.isdigit():
                if self.get_account(int(account), int(pin)):
                    print("You have successfully logged in!")
                    return
        print("Wrong card number or PIN!")

    def new_account(self):
        print("\nYour card has been created")
        new_number = 4000004938320895
        pin = 6826
        print("Your card number:", new_number, "Your card PIN:", pin, sep="\n")
        self.accounts[new_number] = pin

    def get_account(self, account, pin):
        if account in self.accounts.keys():
            return self.accounts[account] == pin
        return False


def main():
    bank = Bank()
    bank.show_menu()

if __name__ == '__main__':
    main()
