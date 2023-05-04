class Account:
    account_Name="Angeth"

class Account:
    def __init__(self,account_Name):
        self.account_Name=account_Name
    def deposit(self):
        return f"{self.account_Name} has deposited 45764"
    def withdrawal(self):
        return f"{self.account_Name} has been our customer"
    def check_balance(self):
        return f"{self.account_Name} has a large balances"
        