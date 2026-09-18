from abc import ABC , abstractmethod

class CartObserver(ABC):
    
    @abstractmethod
    def status(self):
        pass