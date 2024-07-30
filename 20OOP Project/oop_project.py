from bank_accounts import *

sxr = BankAccounts(100, "sxr")
# sxr.getBalance()
# sxr.deposit(20)
# sxr.withdraw(1000)
# sxr.withdraw(10)

# dava = BankAccounts(100, "dava")
# sxr.transfer(1000000, dava)
# sxr.transfer(1, dava)


Jim=InterestRewardsAcct(1000,'Jim')
print("------")
Jim.getBalance()
Jim.deposit(20)
Jim.getBalance()
Jim.transfer(1,sxr)
Jim.getBalance()


print("------")
Bla=SavingAcct(1000,'Bla')
Bla.withdraw(100)
Bla.getBalance()
Bla.deposit(1000)