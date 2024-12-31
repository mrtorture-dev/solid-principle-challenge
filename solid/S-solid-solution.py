# Here your solution
import datetime

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

class DepositOperation:
    def execute(self, account, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        account.balance += amount
        
        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Deposited {amount} into {account.account_number}\n"
            )
        
        print(f"Sending email notification: {amount} deposited into account {account.account_number}.")
        return amount

class WithdrawOperation:
    def execute(self, account, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > account.balance:
            raise ValueError("Insufficient funds.")
        
        account.balance -= amount
        
        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: Withdrew {amount} from {account.account_number}\n"
            )
        
        print(f"Sending email notification: {amount} withdrawn from account {account.account_number}.")
        return amount

class StatementOperation:
    def execute(self, account):
        statement = f"Statement for Account: {account.account_number}\nBalance: {account.balance}\n"
        
        print(statement)
        
        with open("statements.log", "a") as stmt_file:
            stmt_file.write(
                f"{datetime.datetime.now()}: Generated statement for {account.account_number}\n"
            )
        
        print(f"Sending email with statement for account {account.account_number}...")
        return statement
'''
if __name__ == "__main__":
    account = BankAccount("1234-5678", 1000.0)
    deposit = DepositOperation()
    withdraw = WithdrawOperation()
    statement = StatementOperation()

    try:
        deposit.execute(account, 500.0)
        withdraw.execute(account, 200.0)
        statement.execute(account)
        
    except ValueError as e:
        print(f"Error en la operación: {str(e)}")
'''
