class BankAccount:
    def __init__(self):
        self._account_balance = 0  #Private Variable

    @property   #this means getter
    def account_balance(self):
        return self._account_balance

    def deposit(self, amount):
        self._account_balance += amount

    def withdraw(self, amount):
        self._account_balance -= amount

    def __str__(self):
        return f"Balance: {self.account_balance}"
    

def main():
    bank_account = BankAccount()
    print(bank_account.account_balance)
    bank_account.deposit(110)
    bank_account.withdraw(51)
    print(bank_account.account_balance)
    print(bank_account)


if __name__ == "__main__":
    main()
