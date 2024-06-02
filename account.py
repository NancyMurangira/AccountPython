
        
class Account:
    def __init__(self, number, pin, owner_name, overdraft_limit=0, interest_rate=0):
        self.number = number
        self.__pin = pin
        self.owner_name = owner_name
        self.__balance = 0
        self.__overdraft_limit = overdraft_limit
        self.__interest_rate = interest_rate
        self.__frozen = False
        self.__min_balance = 0
        self.__transactions = []
    def check_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong Pin"
    def deposit(self, amount):
        if not self.__frozen:
            self.__balance += amount
            self.__transactions.append(f"Deposit: +{amount}")
        else:
            return "Account is frozen"
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Wrong Pin"
        if self.__frozen:
            return "Account is frozen"
        if self.__balance - amount < -self.__overdraft_limit:
            return "Insufficient funds"
        self.__balance -= amount
        self.__transactions.append(f"Withdrawal: -{amount}")
    def view_account_details(self, pin):
        if pin == self.__pin:
            return {
                "Account Number": self.number,
                "Owner Name": self.owner_name,
                "Balance": self.__balance
            }
        else:
            return "Wrong Pin"
    def change_account_owner(self, new_owner_name):
        self.owner_name = new_owner_name
    def account_statement(self, pin):
        if pin == self.__pin:
            return self.__transactions
        else:
            return "Wrong Pin"
    def set_overdraft_limit(self, new_limit):
        self.__overdraft_limit = new_limit
    def apply_interest(self, pin):
        if pin == self.__pin:
            interest = self.__balance * self.__interest_rate / 100
            self.__balance += interest
            self.__transactions.append(f"Interest: +{interest}")
        else:
            return "Wrong Pin"
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__frozen = True
        else:
            return "Wrong Pin"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__frozen = False
        else:
            return "Wrong Pin"
    def set_minimum_balance(self, new_min_balance):
        self.__min_balance = new_min_balance
    def transfer_funds(self, amount, target_account, pin):
        if pin != self.__pin:
            return "Wrong Pin"
        if self.__frozen:
            return "Account is frozen"
        if self.__balance - amount < -self.__overdraft_limit:
            return "Insufficient funds"
        self.__balance -= amount
        target_account.deposit(amount)
        self.__transactions.append(f"Transfer to {target_account.number}: -{amount}")
        target_account.__transactions.append(f"Transfer from {self.number}: +{amount}")
    def close_account(self, pin):
        if pin == self.__pin:
            self.__balance = 0
            self.__transactions.clear()
            self.__frozen = True
        else:
            return "Wrong Pin"
    def transaction_history(self, pin):
        if pin == self.__pin:
            return self.__transactions
        else:
            return "Wrong Pin"
