import datetime

class ATM:
    def __init__(self, initial_balance=0):
        # Init  initializes the ATM with an initial balance, default PIN, and an empty transaction history.
        self.balance = initial_balance
        self.pin = "1234"
        self.transactions = []

    def check_pin(self, entered_pin):
        # Check pin verifies if the entered PIN is correct.
        return self.pin == entered_pin

    def change_pin(self, old_pin, new_pin):
        # It changes the PIN if the old PIN is correctly entered.
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.transactions.append(f"PIN changed at {datetime.datetime.now()}")
            return "PIN successfully changed."
        else:
            return "Incorrect PIN."

    def inquire_balance(self):
        # It returns the current balance and logs the inquiry.
        self.transactions.append(f"Balance inquiry at {datetime.datetime.now()}")
        return f"Your current balance is ${self.balance:.2f}"

    def deposit_cash(self, amount):
        # It deposits the specified amount and logs the transaction.
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount:.2f} at {datetime.datetime.now()}")
            return f"Successfully deposited ${amount:.2f}. Your new balance is ${self.balance:.2f}"
        else:
            return "Invalid deposit amount."

    def withdraw_cash(self, amount):
        #  Withdraws the specified amount if sufficient balance is available and logs the transaction.
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount:.2f} at {datetime.datetime.now()}")
            return f"Successfully withdrew ${amount:.2f}. Your new balance is ${self.balance:.2f}"
        elif amount > self.balance:
            return "Insufficient balance."
        else:
            return "Invalid withdrawal amount."

    def transaction_history(self):
        #  Returns the list of all transactions.
        return "\n".join(self.transactions)

# Demonstration of ATM functionality
def main():
    atm = ATM(initial_balance=5000)
    pin = input("Enter your PIN: ")
    if not atm.check_pin(pin):
        print("Incorrect PIN. Access denied.")
        return

    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(atm.inquire_balance())
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            print(atm.withdraw_cash(amount))
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: "))
            print(atm.deposit_cash(amount))
        elif choice == "4":
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN: ")
            print(atm.change_pin(old_pin, new_pin))
        elif choice == "5":
            print(atm.transaction_history())
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
