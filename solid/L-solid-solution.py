# Here your solution
from abc import ABC, abstractmethod
class PaymentMethodInterface(ABC):
    def __init__(self, balance: float):
        self.balance = balance
    
    @abstractmethod
    def pay(self, amount: float):
        pass

class RefundablePaymentMethodInterface(PaymentMethodInterface):
    @abstractmethod
    def refund(self, amount: float):
        pass

class RefundablePaymentMethod(RefundablePaymentMethodInterface):
    def __init__(self, balance: float):
        self.balance = balance

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    def refund(self, amount: float):
        self.balance += amount
        print(f"[PaymentMethod] Refunded {amount}. New balance: {self.balance}")

class NonRefundableGiftCard(PaymentMethodInterface):
    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[NonRefundableGiftCard] Paid {amount}. New balance: {self.balance}")

