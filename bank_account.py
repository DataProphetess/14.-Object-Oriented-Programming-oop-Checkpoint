
# class Account:
#     def __init__(self, account_number: str, account_holder: str, account_balance: float = 0.0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.account_balance = account_balance


#     def deposit(self, desposit_amount: float):
#         self.account_balance += desposit_amount
#         return f"You have just desposited {desposit_amount} and your new balance is {self.account_balance}"
    
#     def withdrawal(self, withdrawal_amount: float):
#         if self.account_balance > withdrawal_amount:
#             self.account_balance -= withdrawal_amount
#             return f"You have withdrawn {withdrawal_amount} and your new balance is {self.account_balance}"
#         else:
#             return f"Insufficient funds"
        
#     def check_balance(self):
#         return f"Your account balance is {self.account_balance}"
    
#     def update_details(self, new_name):
#        self.account_holder = new_name
#        return f"You have successfully changed your name to {self.account_holder}"
    
    
#     def __str__(self):
#         return f"Account name: {self.account_holder}\nAccount Number: {self.account_number}"
    

# # #instantiating the class
# my_account = Account("123456789", "Brianna Gom")
# my_account.deposit(500)
# my_account.withdrawal(200)
# my_account.check_balance()

# print(my_account.deposit(500.00))
# print(my_account.withdrawal(200))
# print(my_account.check_balance())


    
        

























