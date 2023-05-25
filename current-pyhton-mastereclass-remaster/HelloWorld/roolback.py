import datetime
import sqlite3

import pytz

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL ")
db.execute("CREATE TABLE IF NOT EXISTS transactions (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = opening_balance
        print("Account created for {}".format(self.name), end="")
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            new_balance = self._balance + amount
            deposit_time = pytz.utc.localize(datetime.datetime.utcnow())
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            db.commit()
            self._balance = new_balance
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            new_balance = self._balance - amount
            withdraw_time = pytz.utc.localize(datetime.datetime.utcnow())
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ? )", (new_balance, self.name))
            db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdraw_time, self.name, -amount))
            db.commit()
            self._balance = new_balance
            print("{:.2f} withdraw".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero a than you account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f} ".format(self.name, self._balance / 100))
    def
if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
