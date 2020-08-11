# Simple Banking System

### About
Everything goes digital these days, and so does money. Today, most people have credit cards, which save us time, energy and nerves. From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways. In this project, I developed a simple banking system with database.

### Learning outcomes
In this project, I found out how the banking system works and learn about SQL. I also learnt how Luhn algorithm can help us avoid mistakes when entering the card number. As an overall result, I got new experience in Python.

### Additional Description
In our banking system, the IIN is 400000, the customer account number can be any number, but it should be unique and have a length of 16 digits. The very last digit of a credit card is the check digit or checksum. It is used to validate the credit card number using the Luhn algorithm.

Once the program starts, program prints the menu:
```
1. Create an account
2. Log into account
0. Exit
```
If the customer chooses **Create an account**, program will generate a new card number which satisfies all the conditions described above. Then it will generate a PIN code that belongs to the generated card number. A PIN code is a sequence of any 4 digits. PIN should be generated in a range from 0000 to 9999.

If the customer chooses **Log into account**, program will ask them to enter their card information. The program will store all generated data until it is terminated so that a user is able to log into any of the created accounts by a card number and its pin.

After all information is entered correctly, program will allow the user to check the account balance; right after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.

The program uses Luhn algorithm to validate a credit card number or other identifying numbers, such as Social Security. The Luhn algorithm, also called the Luhn formula or modulus 10, checks the sum of the digits in the card number and checks whether the sum matches the expected result or if there is an error in the number sequence. After working through the algorithm, if the total modulus 10 equals zero, then the number is valid according to the Luhn method.

The program also uses SQLite as a database engine to store all of the accounts. sqlite3 module is required.

**Account menu:**
```
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
```
If the user asks for **Balance**, the program will read the balance of the account from the database and output it into the console.

**Add income** item allows user to deposit money to the account.

**Do transfer** item allows transferring money to another account. The program will the following errors:

If the user tries to transfer more money than he/she has, output: "Not enough money!"
If the user tries to transfer money to the same account, output: “You can't transfer money to the same account!”
If the receiver's card number doesn’t pass the Luhn algorithm, output: “Probably you made mistake in the card number. Please try again!”
If the receiver's card number doesn’t exist, output: “Such a card does not exist.”
If there is no error, ask the user how much money they want to transfer and make the transaction.

If the user chooses the **Close account** item, the program will delete that account from the database.

### Example of a program run
The symbol ```>``` represents the user input. Notice that it's not a part of the input.

**Example 1:**
```
1. Create an account
2. Log into account
0. Exit
>1

Your card have been created
Your card number:
4000009455296122
Your card PIN:
1961

1. Create an account
2. Log into account
0. Exit
>1

Your card have been created
Your card number:
4000003305160034
Your card PIN:
5639

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000009455296122
Enter your PIN:
>1961

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>2

Enter income:
>10000
Income was added!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1

Balance: 10000

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160035
Probably you made mistake in the card number. Please try again!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305061034
Such a card does not exist.

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>15000
Not enough money!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>3

Transfer
Enter card number:
>4000003305160034
Enter how much money you want to transfer:
>5000
Success!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>1

Balance: 5000

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit

>0
Bye!
```
**Example 2:**
```
1. Create an account
2. Log into account
0. Exit
>1

Your card has been created
Your card number:
4000007916053702
Your card PIN:
6263

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000007916053702
Enter your PIN:
>6263

You have successfully logged in!

1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
>4

The account has been closed!

1. Create an account
2. Log into account
0. Exit
>2

Enter your card number:
>4000007916053702
Enter your PIN:
>6263

Wrong card number or PIN!

1. Create an account
2. Log into account
0. Exit
>0

Bye!
```
### Files:
``` 
banking.py
account.py
functions.py
```
