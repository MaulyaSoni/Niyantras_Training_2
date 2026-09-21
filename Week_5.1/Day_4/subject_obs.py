from subject_interface import Subject
from observer import CartObserver

class SubjectLogger(Subject):

    def __init__(self):
        self.obs: List[CartObserver] = []
      
    def add_obs(self , obs : CartObserver) -> None:
        self.obs.append(obs)
    
    def remove_obs(self , obs : CartObserver) -> None:
        self.obs.remove(obs)
    
    def notify_observers(self) -> None:
        for observer in self.obs:
            observer.update()