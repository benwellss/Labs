class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = int(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return "deposit of £{} is successful!".format(amount)
        else:
            print("invalid amount")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return "withdrawal of £{} is successful!".format(amount)
        else:
            print("no funds to withdraw or invalid amount")

account = BankAccount("010022")
print("balance: ", account.balance)

Deposit.deposit(100) 
print("your balance is: ", account.balance)

Withdrawal.withdraw(50) 
print("your balance is: ", account.balance)

Withdrawal.withdraw(100) #to check if no funds works
print("your balance is: ", account.balance)
