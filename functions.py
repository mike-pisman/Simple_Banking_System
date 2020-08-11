# Mikhail Pisman
# Simple Banking System
# https://github.com/mike-pisman/Simple_Banking_System
# functions.py
# File with general functions used by all classes

import sys
import random

# Get global variables for connection
global cursor, connection

# Function returns true if card last digit has correct checksum number according to Luhn algorithm
def check_card(card):
    luhn_sum = luhn_algorithm(card[:-1])  # Pass the number through luhn algorithm without last digit
    checksum = get_checksum(luhn_sum)  # Get correct checksum number based on Luhn algorithm
    return checksum == int(card[-1])  # Check that last digit of the card matches correct checksum

# Function exits program and closes SQL connection
def exit():
    print("\nBye!")
    connection.close()
    sys.exit()  # Close program

# Function returns new card number from account number parameter
def generate_card_number(acc_number):
    iin = "400000"  # IIN given by the assignment
    luhn_sum = luhn_algorithm(iin + acc_number)  # Calculate Luhn sum
    checksum = get_checksum(luhn_sum)  # Get checksum
    return iin + acc_number + str(checksum)  # Return 16-digit card number as a string

# Generate 9-digit account number
def generate_account_number():
    acc_number = ""
    for _ in range(9):
        acc_number += str(random.randrange(10))
    return acc_number

# Function takes Luhn sum as a parameter and returns checksum
def get_checksum(luhn_sum):
    # Check sum added to the luhn sum must return round number
    return 10 - luhn_sum % 10 if luhn_sum % 10 != 0 else 0

# Function returns Luhn sum based on 15-digit number
def luhn_algorithm(card_number):
    card_number = list(map(int, card_number))  # Create a list of integers from the string
    for i, _ in enumerate(card_number, 1):
        # Multiply each odd digit by 2
        if i % 2 != 0:
            card_number[i - 1] *= 2
        # Subtract 9 from any digit bigger than 9
        if card_number[i - 1] > 9:
            card_number[i - 1] -= 9
    return sum(card_number)  # Return sum

# Function returns a random generated 4-digit pin-code as a string
def generate_pin():
    pin = ""
    for _ in range(4):
        pin += str(random.randrange(10))
    return pin
