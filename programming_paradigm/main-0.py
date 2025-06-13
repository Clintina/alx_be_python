from bank_account import BankAccount

account = BankAccount(100)
account.deposit(50)
account.withdraw(500)  # Only the method prints this message
account.display_balance()
