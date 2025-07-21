
What You're Aiming For
The objective is to create a Python class named "Account" with methods for depositing, withdrawing, and checking balances, encapsulated in a script called "bank_account.py" to simulate basic bank account operations.
 
Create a class called "Account" that has the following attributes:
•	account_number (string)
•	account_balance (float)
•	account_holder (string)
The class should have the following methods:
•	deposit(amount: float) - This method should add the amount passed as an argument to the account balance.
•	withdraw(amount: float) - This method should subtract the amount passed as an argument from the account balance, but only if the account balance is greater than the amount being withdrawn.
•	check_balance() - This method should return the current account balance.
Instructions
 
1.	Define the Account class and its attributes as specified above.
2.	Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
3.	Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.
4.	Define the check_balance() method. It should return the current account balance.
5.	Create an instance of the Account class, and assign it to a variable called "my_account".
6.	Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
7.	Test the program by creating multiple instances of the class and performing different transactions on them.
