class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, money_to_withdraw):
        if self.balance - money_to_withdraw < 0:
            raise ValueEror()
        else:
            self.balance -= money_to_withdraw
            return f"{self.name} has {abs(self.balance)}."

    def check(self, name, money):
        if not name.checking_account or name.balance < money:
            raise ValueEror()
        self.balance += money
        name.balance -= money
        return f"{self.name} has {self.balance} and {name.name} has {name.balance}."

    def add_cash(self, money):
        self.balance += money
        return f"{self.name} has {abs(self.balance)}."