from subject_interface import Subject
from observer import CartObserver
from context import Cart
class SubjectLogger(Subject):

    def __init__(self , cart_obj : Cart):
        self.obs: list[CartObserver] = []
        self.cart_obj = cart_obj


    def add_obs(self , obs : CartObserver) -> None:
        if obs not in self.obs: 
            self.obs.append(obs)
    
    def remove_obs(self , obs : CartObserver) -> None:
        self.obs.remove(obs)
    
    def notify_observers(self) -> None:
        customer = self.cart_obj.show_customer_type()
        bill = self.cart_obj.display_bill()
        for observer in self.obs:
            observer.update(customer , bill)