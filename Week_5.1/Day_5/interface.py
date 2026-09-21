from abc import ABC , abstractmethod

class Payment(ABC):

    @abstractmethod
    def payment_type(self , amount : int):
        pass
