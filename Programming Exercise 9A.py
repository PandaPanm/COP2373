from datetime import timedelta

class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.01):
        """
        Initialize a new Bank Account.
        :param name: Name of the account holder.
        :param account_number: Account number as a unique identifier.
        :param amount: Initial balance (default is 0).
        :param interest_rate: Annual interest rate as a decimal (default is 0.01 or 1%).
        """
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def set_interest_rate(self, new_rate):
        """Set a new interest rate for the account."""
        if new_rate >= 0:
            self.interest_rate = new_rate
        else:
            print("Interest rate must be non-negative.")

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw an amount if it is within the current balance."""
        if 0 < amount <= self.amount:
            self.amount -= amount
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        """Return the current balance."""
        return self.amount

    def calculate_interest(self, days):
        """
        Calculate interest for a given number of days.
        :param days: Number of days for interest calculation.
        :return: Calculated interest based on the number of days.
        """
        daily_rate = self.interest_rate / 365
        interest = self.amount * (1 + daily_rate) ** days - self.amount
        return interest

    def __str__(self):
        """Display account details with balance and interest rate."""
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")

def test_bank_acct():
    """Test function for the BankAcct class."""
    # Creating an account with an initial balance and interest rate
    account = BankAcct("Weslee Williams", "123456789", 1000.0, 0.03)

    # Display initial account details
    print(account)

    # Deposit some money
    account.deposit(500)
    print("\nAfter depositing $500:")
    print(account)

    # Withdraw some money
    account.withdraw(200)
    print("\nAfter withdrawing $200:")
    print(account)

    # Display the current balance
    print("\nCurrent balance:", account.get_balance())

    # Set a new interest rate
    account.set_interest_rate(0.04)
    print("\nAfter setting a new interest rate of 4%:")
    print(account)

    # Calculate interest for 30 days
    interest = account.calculate_interest(30)
    print(f"\nInterest earned over 30 days: ${interest:.2f}")

# Run the test function
if __name__ == "__main__":
    test_bank_acct()
