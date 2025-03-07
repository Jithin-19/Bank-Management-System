# bank.py

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance):
        """Create a new account with a unique account number."""
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = {"name": name, "balance": initial_balance}
        return account_number

    def deposit(self, account_number, amount):
        """Deposit money into an account."""
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            return f"₹{amount} deposited successfully."
        return "Invalid account number."

    def withdraw(self, account_number, amount):
        """Withdraw money from an account."""
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                return f"₹{amount} withdrawn successfully."
            return "Insufficient balance."
        return "Invalid account number."

    def get_account_details(self, account_number):
        """Fetch account details."""
        return self.accounts.get(account_number, "Account not found.")


# Create a single instance of Bank to be used in app.py
bank = Bank()
