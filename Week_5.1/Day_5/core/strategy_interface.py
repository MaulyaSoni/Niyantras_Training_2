from abc import ABC , abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def payment_type_choice(self , amount : int):
        pass
