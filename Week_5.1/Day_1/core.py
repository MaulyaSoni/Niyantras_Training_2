from abc import ABC , abstractmethod
#Prodcut Interface
class Notification(ABC):

    @abstractmethod
    def send(self , message : str , sender : str):
        pass
    