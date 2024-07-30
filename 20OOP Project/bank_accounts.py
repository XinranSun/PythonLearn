class BalanceException(Exception):
    pass


class BankAccounts:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.acctName = acctName
        print(f"\nAccount Name: {self.acctName},\nInitial Amount: {self.balance}")

    def getBalance(self):
        print(f"\nAccount Name: {self.acctName},\n balance: {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nAccount Name: {self.acctName},\n balance: {self.balance:.2f},\n deposited: {amount}")

    def viableTransaction(self, amount):
        if self.balance < amount:
            raise BalanceException("Insufficient balance")
        elif self.balance >= amount:
            return

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\nwithdraw balance complete.")
        except BalanceException as e:
            print(f"\nwithdraw balance failed : {e}")

    def transfer(self, amount, account):
        try:
            print(f"\n--------transfer balance start-------")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer  complete.")
        except BalanceException as e:
            print(f"\ntransfer balance failed : {e}")


class InterestRewardsAcct(BankAccounts):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\ndeposit balance complete.")
        self.getBalance()

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee=10

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount - self.fee
            print(f"\nwithdraw balance complete.")
            self.getBalance()
        except BalanceException as e:
            print(f"\nwithdraw balance failed : {e}")


