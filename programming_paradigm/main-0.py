from bank_account import BankAccount

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.display_balance()

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Increase balance by the deposited amount."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds exist. Returns True if successful, False otherwise."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Prints the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")