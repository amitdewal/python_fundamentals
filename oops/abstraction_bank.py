from abc import ABC,abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass



class SavingAccount(BankAccount):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def check_balance(self):
        print("Current Balance is : ", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited amount : ", amount)
        else:
            print("Invalid deposit amount: ",amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdrawn: ", amount)
        else:
            print("Insufficient balance")

account = SavingAccount("ravi", 5000)
account.check_balance()
account.deposit(1000)
account.withdraw(2000)
account.check_balance()
