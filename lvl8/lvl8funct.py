#Eli Baker
#Bank account functions

import random

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.00

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid amount or insufficient funds.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")                