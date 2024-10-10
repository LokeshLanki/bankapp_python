from account import BankAccount
from transactions import TransactionHistory

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        if name in self.accounts:
            print("Account already exists.")
            return None
        new_account = BankAccount(name, initial_balance)
        self.accounts[name] = new_account
        print(f"Account created for {name} with balance ${initial_balance:.2f}.")
        return new_account

    def get_account(self, name):
        return self.accounts.get(name, None)

    def fund_transfer(self, from_name, to_name, amount):
        from_account = self.get_account(from_name)
        to_account = self.get_account(to_name)

        if from_account and to_account:
            if amount > 0 and amount <= from_account.get_balance():
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred ${amount:.2f} from {from_name} to {to_name}.")
            else:
                print("Invalid transfer amount.")
        else:
            print("One or both accounts not found.")

def main():
    bank = Bank()
    
    while True:
        print("\nWelcome to the Bank App")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Fund Transfer")
        print("6. Print Transactions")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance (default is 0): ") or 0)
            bank.create_account(name, initial_balance)

        elif choice == '2':
            name = input("Enter your name: ")
            account = bank.get_account(name)
            if account:
                details = account.get_details()
                print(f"Account Name: {details['name']}, Balance: ${details['balance']:.2f}")
                print("Transactions:")
                for transaction in details['transactions']:
                    print(transaction)
            else:
                print("Account not found.")

        elif choice == '3':
            name = input("Enter your name: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(name)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            name = input("Enter your name: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(name)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '5':
            from_name = input("Enter your name: ")
            to_name = input("Enter the recipient's name: ")
            amount = float(input("Enter amount to transfer: "))
            bank.fund_transfer(from_name, to_name, amount)

        elif choice == '6':
            name = input("Enter your name: ")
            account = bank.get_account(name)
            if account:
                account.print_transactions()
            else:
                print("Account not found.")

        elif choice == '7':
            print("Thank you for using the Bank App!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
