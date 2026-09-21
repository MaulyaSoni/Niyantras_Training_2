from abc import ABC , abstractmethod

class CartObserver(ABC):
    
    @abstractmethod
    def update(self):
        pass