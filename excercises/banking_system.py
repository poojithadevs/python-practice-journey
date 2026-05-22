class BankAccount():
    balance=0
    def __init__(self,accountholder,balance):
        self.accountholder=accountholder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("deposited successfully...")
        print(f"your current balance{bankaccount.balance}")
    def withdraw(self,amount):
        
        if amount>self.balance:
            print("insufficient funds...")
        else:
            self.balance-=amount
            print("withdraw successfully....")
            print(f"your current balance{bankaccount.balance}")

        

class SavingsAccount(BankAccount):
    def withdraw(self,amount):
        if self.balance-amount<1000:
            print("cant withdraw minimum balance 1000")
        else:
            super().withdraw(amount)
class CurrentAccount(BankAccount):
    def __init__(self,accountholder,name,overdraft_limit):
        super().__init__(accountholder,name)
        self.overdraft_limit=overdraft_limit
    def withdraw(self, amount):
        if self.balance-amount<=self.overdraft_limit:
            print("you exceeded overdraft limit...")
        else:
            self.balance-=amount
            print("withdrawl successfully....")
            print(f"current balance:{self.balance}")

bankaccount=CurrentAccount("pooja",8000,-1000)
bankaccount.deposit(200)
bankaccount.withdraw(300)
bankaccount.withdraw(8899)


