# Here your solution
from abc import ABC, abstractmethod
class PaymentInterface(ABC):
    @abstractmethod
    def pay(amount: float):
        pass
class PayPalService(PaymentInterface):
    @staticmethod
    def pay(amount: float):
        print(f"Paying {amount} using PayPal...")

class PaymentProcessor:
    def __init__(self,payment_service:PaymentInterface):
        self.payment_service = payment_service
    def process_payment(self, amount: float):
        self.payment_service.pay(amount)
