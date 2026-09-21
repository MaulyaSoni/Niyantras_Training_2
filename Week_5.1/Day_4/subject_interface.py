from abc import ABC , abstractmethod
from observer import CartObserver

class Subject(ABC):

    @abstractmethod
    def add_obs(self , observer : CartObserver):
        pass
    
    @abstractmethod
    def remove_obs(self , observer : CartObserver):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass