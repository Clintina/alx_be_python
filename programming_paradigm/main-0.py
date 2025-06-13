from bank_account import BankAccount

account = BankAccount(100)
account.deposit(50)
# Try to withdraw more than the balance
account.withdraw(500)  # This will print "Insufficient funds." from the method
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

    def display_balance(self):
        """Prints the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")