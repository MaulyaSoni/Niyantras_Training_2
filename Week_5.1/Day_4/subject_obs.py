from subject_interface import Subject
from observer import CartObserver
from strategy_interface import Bill
class SubjectLogger(Subject):

    def __init__(self , bill_obj ):
        self.obs: List[CartObserver] = []
        self.bill_obj :bill_obj


    def add_obs(self , obs : CartObserver) -> None:
        if obs not in self.obs: 
            self.obs.append(obs)
    
    def remove_obs(self , obs : CartObserver) -> None:
        self.obs.remove(obs)
    
    def notify_observers(self) -> None:
        customer = self.bill_obj.show_customer_type()
        bill = self.bill_obj.display_bill()
        for observer in self.obs:
            observer.update(self , customer , bill)