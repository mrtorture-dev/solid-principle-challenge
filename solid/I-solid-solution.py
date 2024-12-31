# Here your solution
from abc import ABC, abstractmethod

class PaymentInterface(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class IPaymentGateway(PaymentInterface):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass

class BasicGiftCard(PaymentInterface):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")
