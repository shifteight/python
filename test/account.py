"""
A module
"""


class BankAccount:
    """
    A class.
    """

    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        """withdraw an amount."""
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """deposit an amount."""
        self.balance += amount
        return self.balance


A = BankAccount()
B = BankAccount()
A.deposit(100)
B.deposit(50)
B.withdraw(10)
B.withdraw(10)
