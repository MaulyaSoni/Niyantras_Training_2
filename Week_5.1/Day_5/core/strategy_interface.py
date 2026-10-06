from abc import ABC , abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def payment_type(self , amount : int):
        pass
