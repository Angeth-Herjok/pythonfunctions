# class Account:
#     account_Name="Angeth"
#     account_number="164532"
#     balance="6745"


# assigments
# Add these attributes and behaviours to the class Account

# Add attributes deposits and withdrawals in the init method 
# which are empty lists by default and another attribute loan_balance
# which is zero by default.

# Add a method check_balance which returns the account’s balance

# Update the deposit method to append each withdrawal transaction
# to the deposits list. Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }

# Update the withdrawal method to append each withdrawal 
# transaction to the withdrawals list. Each transaction should be
# in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }

# Add a new method  print_statement which combines both deposits
# and withdrawals into one list and, using a for loop, prints each
# transaction in a new line like this
# deposit - 1000
# withdrawal - 500
# 
# Add a borrow_loan method which allows a customer to borrow if they 
# meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount

# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance

# Add a transfer method which accepts two attributes (amount and instance of another account).
# If the amount is less than the current instances balance, the method transfers the requested 
# amount from the current account to the passed account. The transfer is accomplished by 
# reducing the current account balance and depositing the requested amount to the passed account.



class Account:
    def __init__(self,account_Name,date_of_opening):
        self.account_Name=account_Name
        self.date_of_opening  = date_of_opening 
        self.balance=0

        
def deposit(self,amount):
        self.balance+=amount
        return f"{amount} has deposited 45764 and your balance is {self.balance}"
def withdraw(self,amount):
        if self.balance<=amount:
            self.balance-=amount
            return f"{amount} has been withdraw and your new balance is {self.balance}"
        else:
            return f"Your balance is {self.balance} you cannot withdraw {amount}"


# Add attributes deposits and withdrawals in the init method 
# which are empty lists by default and another attribute loan_balance
# which is zero by default.
def __init__(self,account_Name):
      self.count_Name=account_Name
    #   self.balance=0
      self.deposits=[]
      self.withdrawals=[]
      self.loan_balance=0

# Add a method check_balance which returns the account’s balance
def check_balance(self):
        return f"My balance is {self.balance}"

# Update the deposit method to append each withdrawal transaction
# to the deposits list. Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }

def deposit(self,amount):
      self.balance += amount
      self.deposits.append({
            "amount":amount,
            "narration":"deposit"     
      })
      return f"The amount deposited is {amount}.The total amount is {self.balance}"

def withdraw(self,amount):
      if self.balance >= amount:
            self.balance -= amount
            self.withdrawals.append({
                  "amount": amount,
                  "narration": "withdrawal"   
            })
            return f"The amount deposited is {amount}.The total amount is {self.balance}"
      else:
            return f"The remaining balance is {self.balance}.The remaining amount is {amount}"


# Add a new method print_statement which combines both deposits
# and withdrawals into one list and, using a for loop, prints
# each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")


# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= (sum(
                [transaction['amount'] for transaction in self.deposits]) / 3):
            self.loan_balance += amount
            return f"The loan granted was {amount}. The balance was{self.loan_balance}"
        else:
            return "Loan request denied"
        
# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
def repay_loan(self, amount):
        if self.loan_balance > 0:
            if amount > self.loan_balance:
                self.balance += amount - self.loan_balance
                self.loan_balance = 0
                return f"Loan has been fully repaid. Your new balance is {self.balance}"
            else:
                self.loan_balance -= amount
                return f"The loan repay is {amount}. The loan balance is {self.loan_balance}"
        else:
            return "No outstanding loan"

# Add a transfer method which accepts two attributes (amount and instance of another account).
# If the amount is less than the current instances balance, the method transfers the requested 
# amount from the current account to the passed account. The transfer is accomplished by 
# reducing the current account balance and depositing the requested amount to the passed account.
def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.deposit(amount)
            return f"The transferred amount is {amount} to {other_account.account_name} and was successfully transferred."
        else:
            return "Insufficient balance for transfer."

      
