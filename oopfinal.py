class Account:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print("Deposited:", amt)

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(self.holder, "balance:", self.balance)


class SavingsAccount(Account):   # inheritance
    def add_interest(self):
        self.balance += self.balance * 0.05
        print("Interest added")


# accounts
a1 = SavingsAccount("Varshini", 6000)
a2 = Account("prassu", 2500)

a1.deposit(500)
a1.withdraw(1000) 
a1.add_interest()

a1.check_balance()
a2.check_balance()