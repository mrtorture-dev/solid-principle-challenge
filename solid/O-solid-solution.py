# Here your solution
from abc import ABC, abstractmethod

class PayMethodInterface(ABC):
    @abstractmethod
    def calculate_fee(self, amount:float):
        pass

class CreditCardFee(PayMethodInterface):
    def calculate_fee(self, amount:float):
        return amount * 0.03

class PayPalFee(PayMethodInterface):
    def calculate_fee(self, amount:float):
        return amount * 0.05

class BankTransferFee(PayMethodInterface):
    def calculate_fee(self, amount:float):
        return 2.50

class UnknownFee(PayMethodInterface):
    def calculate_fee(self, amount:float):
        return 0.00

class FeeCalculator:
    def __init__(self, payment_method: PayMethodInterface):
        self.payment_method = payment_method
        
    def calculate_fee(self, amount:float):
        return self.payment_method.calculate_fee(amount)

'''
if __name__ == "__main__":
    credit_calculator = FeeCalculator(CreditCardFee())
    paypal_calculator = FeeCalculator(PayPalFee())
    bank_calculator = FeeCalculator(BankTransferFee())
    
    amount = 100.0
    print(f"Credit Card Fee: S/.{credit_calculator.calculate_fee(amount)}")
    print(f"PayPal Fee: S/.{paypal_calculator.calculate_fee(amount)}")
    print(f"Bank Transfer Fee: S/.{bank_calculator.calculate_fee(amount)}")
'''
