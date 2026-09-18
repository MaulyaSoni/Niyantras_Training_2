from interface import Bill
from strategies import RegularCustomer ,MemberCustomer , VIPCustomer
from observer import CartObserver

class Cart:
    def __init__(self , customer_type: Bill):
        self.customer_type = customer_type
        self.obs: List[CartObserver] = []

    #Concrete Strategies 
    def set_customer_type(self , customer_type : Bill):
        self.customer_type = customer_type

    def show_customer_type(self):
        return self.customer_type

    def display_bill(self) :
        return self.customer_type.calc_discount()

    #Subject Observer , methods of add/remove observer
    def add_obs(self , obs : CartObserver) -> None:
        self.obs.append(obs)
    
    def remove_obs(self , obs : CartObserver) -> None:
        self.obs.remove(obs)