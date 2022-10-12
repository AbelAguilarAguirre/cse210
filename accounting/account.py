class Account:

    def __init__(self):
        self._transactions = []    # if we change this...

    def deposit(self, amount):
        self._transactions.append(amount)
account = Account()
account.deposit(100)
print(account._transactions)