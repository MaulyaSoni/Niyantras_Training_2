from abc import ABC , abstractmethod

class ShippingDecorator(ABC):  

    @abstractmethod
    def status_log(self , status : str):
        pass
