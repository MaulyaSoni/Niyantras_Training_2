from abc import ABC , abstractmethod

class Payment(ABC):

    @abstractmethod
    def payment_type(self , amt : int):
        pass
