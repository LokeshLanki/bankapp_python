class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

    def print_transactions(self):
        if not self.history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in self.history:
                print(transaction)
