class InsufficientBalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("withdraw amount exceeds balance.")
        self.balance -= amount
        print("withdraw successful Remaining balance: ", self.balance)


account = BankAccount(1000)
try:
    account.withdraw(1500)
except InsufficientBalanceError as e:
    print("Error:", e)

account.withdraw(800)
