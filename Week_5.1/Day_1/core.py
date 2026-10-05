from abc import ABC , abstractmethod
#Prodcut Interface
class Notification(ABC):

    @abstractmethod
    def send(self ,  receiptant : str ,message : str ):
        pass
    